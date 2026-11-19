# Analysis Recipes for a Campaign / Creative CSV (timed round)

> Fast path on this machine: `python -I scripts/kpi_calc.py <file>.csv --target-cpa <x> --by Channel,Format` covers steps 1-6 with the standard library only (pandas is not installed here). The pandas/scipy snippets below need `pip install pandas scipy` first; use them for deeper cuts.

Assumed columns (rename to match): creative_id, channel, format, language, concept, spend, impressions, clicks, installs, rides (business event, e.g. first_rides). Target KPI = CPA of the business event. Order: 1 load/sanity -> 2 recompute -> 3 rank -> 4 concentration -> 5 correlation -> 6 segments -> 7 outliers/CI -> 8 budget split -> 9 write-up. About 20 minutes.

## 1. Load and sanity checks
```python
import pandas as pd, numpy as np
df = pd.read_csv("creatives.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
print(df.shape); print(df.dtypes); print(df.describe(include="all").T)
print("nulls:\n", df.isna().sum())
print("dupes:", df.duplicated().sum(), "| dup ids:", df.creative_id.duplicated().sum())
checks = {
 "clicks>impr":     df.clicks > df.impressions,
 "installs>clicks": df.installs > df.clicks,      # may be legit with view-through; flag
 "rides>installs":  df.rides > df.installs,
 "negative":        (df[["spend","impressions","clicks","installs","rides"]] < 0).any(axis=1),
 "spend0_impr>0":   (df.spend == 0) & (df.impressions > 0),
 "impr0_spend>0":   (df.impressions == 0) & (df.spend > 0),
}
for k, m in checks.items():
    print(k, int(m.sum()))
    if m.sum(): print(df[m].head())
# If the file has CTR/CPA columns, compare them with your recomputed values.
```
Say in the deck: "All ratios recomputed from raw spend and counts; N rows failed integrity checks and were excluded/flagged."

## 2. Recompute KPIs (never trust provided ratios)
```python
def kpis(g):
    s = g[["spend","impressions","clicks","installs","rides"]].sum()
    return pd.Series({
        "spend": s.spend, "impr": s.impressions, "clicks": s.clicks,
        "installs": s.installs, "rides": s.rides,
        "cpm": s.spend/s.impressions*1000, "ctr": s.clicks/s.impressions,
        "cpc": s.spend/s.clicks, "click_to_install": s.installs/s.clicks,
        "ipm": s.installs/s.impressions*1000, "cpi": s.spend/s.installs,
        "activation": s.rides/s.installs if s.installs else np.nan,
        "cpa": s.spend/s.rides if s.rides else np.nan})
by_creative = df.groupby("creative_id").apply(kpis)
total = kpis(df)   # blended = sum(spend)/sum(rides), NOT mean of row CPAs
```
Identity check: cpa == cpm/(1000*ctr*click_to_install*activation).

## 3. Rank by the business KPI
```python
r = by_creative.sort_values("cpa")
r["share_spend"] = r.spend/r.spend.sum(); r["share_rides"] = r.rides/r.rides.sum()
r["cpa_vs_blended"] = r.cpa/total.cpa
print(r[["spend","rides","cpi","activation","cpa","cpa_vs_blended","share_spend","share_rides"]].round(3))
```
- Rank by CPA of the business event, not CTR or CPI. Show rides beside CPA. Rows with rides < 10-15 = "directional". Zero-ride rows: "CPA undefined, wasted spend $X".
- Quadrants: high IPM + high activation = scale; high IPM + low activation = wrong users or over-promise (fix promise/onboarding); low IPM + high activation = good quality, weak hook (test new hooks, keep); low + low = stop.

## 4. Concentration check
```python
r = r.sort_values("rides", ascending=False)
top = r.index[0]; share_top = r.loc[top,"rides"]/r.rides.sum()
cpa_wo = r.drop(top).spend.sum()/r.drop(top).rides.sum()
print(f"{top}: {share_top:.0%} of rides | blended CPA {total.cpa:.2f} | without winner {cpa_wo:.2f}")
sh = r.rides/r.rides.sum(); print("top3:", sh.head(3).sum().round(2), "HHI:", (sh**2).sum().round(3))
print(sh.cumsum().round(2).head(10))
```
If one creative gives >40-50% of rides, performance is a single-asset story: say it is fragile, build variants and backups. If CPA without the winner is much worse than blended, the portfolio is carried by one asset.

## 5. Correlation: does the upstream metric predict the downstream KPI?
```python
m = by_creative[by_creative.rides >= 10]
print(m[["ctr","ipm","cpi","activation","cpa"]].corr(method="spearman").round(2)); print("n =", len(m))
print(by_creative.cpi.rank().corr(by_creative.cpa.rank()))   # is CPI-winner = CPA-winner?
```
- |rho| < 0.3 or sign flip between IPM/CPI and CPA = upstream is not a usable proxy; optimize on the deeper event.
- Negative correlation CTR vs activation = clickbait pattern.
- n < 15 creatives: anecdotal, say "directional, n=12".

## 6. Segment splits (channel x format x language x concept)
```python
for dim in ["channel","format","language","concept"]:
    print(dim); print(df.groupby(dim).apply(kpis)[["spend","rides","cpi","activation","cpa"]].round(2).sort_values("cpa"))
pv = df.pivot_table(index="channel", columns="format", values=["spend","rides"], aggfunc="sum")
print((pv["spend"]/pv["rides"]).round(1))      # CPA heatmap
```
- Aggregate spend and counts first, then divide. Grey out cells with < 10 rides.
- Simpson's paradox: if format and channel are correlated (video only on TikTok), look at format within channel.
- Look for concept x channel interaction; compare language within channel only.

## 7. Uncertainty and outliers
```python
from scipy import stats
def cpa_ci(spend, n, conf=0.90):               # exact Poisson interval on event count
    if n == 0: return (np.nan, np.nan)
    a = (1-conf)/2
    lo = stats.chi2.ppf(a, 2*n)/2; hi = stats.chi2.ppf(1-a, 2*n+2)/2
    return (spend/hi, spend/lo)
by_creative[["cpa_lo","cpa_hi"]] = by_creative.apply(lambda x: pd.Series(cpa_ci(x.spend, x.rides)), axis=1)
x = by_creative.cpa.dropna(); med = x.median(); mad = (x-med).abs().median()
by_creative["cpa_robust_z"] = (by_creative.cpa-med)/(1.4826*mad)
print(by_creative[by_creative.cpa_robust_z.abs()>3])
print(df[(df.clicks/df.impressions>0.15)|(df.rides/df.installs>0.6)])   # impossible-looking rates
```
- Outlier = bad data until proven real: check the row, decide include/exclude, state it.
- Overlapping intervals = no basis to claim A beats B.
- 2% of spend with best CPA = candidate to scale, not proof.

## 8. Quick budget allocator
```python
seg = df.groupby("channel").apply(kpis)
seg["split"] = (1/seg.cpa)/(1/seg.cpa).sum()     # inverse-CPA start
```
Then adjust: trust shares only where rides >= 15, respect diminishing returns (not 80% in one channel on a 2-week sample), keep 10-20% test reserve, cap any channel at 50-60% until proven.

## 9. Write-up pattern: Insight · Evidence · So what
Format: Insight (one sentence) | Evidence (numbers, n, comparison) | So what (action + expected effect + risk).

Example 1 (illustrative numbers):
- Insight: Cheapest installs are not the cheapest first rides.
- Evidence: Across 17 creatives with >= 10 rides, Spearman rho CPI vs first-ride CPA = 0.18. C07 ranks #2 on CPI ($1.10) but #14 on CPA ($31): 3.1% of its installs ride vs 7.4% average.
- So what: Select and scale on first-ride CPA, not CPI. Move C07 budget to C03 (CPA $14, activation 9.0%, 24 rides). Risk: C03 holds 38% of rides, build 3 hook variants.

Example 2:
- Insight: Blended CPA depends on one creative.
- Evidence: C03 = 38% of rides on 22% of spend; blended CPA $19.4, without C03 $24.6 (+27%).
- So what: Keep C03 as control, fund 3 variants (hook, language, format) at 15% of budget, set stop rules for the rest.

Deliverable structure: 1 headline (best channel/creative/segment, CPA vs blended, confidence); 2 3-5 insights by money impact; 3 hypotheses (metric + MDE); 4 scale/stop rules (kpis/scale-stop-rules.md) with target CPA; 5 budget split proven vs test (e.g. 80/20) by channel with logic; 6 risks and data caveats (n, lag, attribution, tracking); 7 next 7-day plan.

## 10. Pitfalls
Averaging row CPAs; dropping zero-event rows from blended CPA; comparing creatives with different spend/flight/channel mix; winners on < 10-15 events; CTR from "all clicks"; mixing D1 vs D7 windows or cohorts of different age; winner's curse (confirm in round two); correlation presented as causation.
