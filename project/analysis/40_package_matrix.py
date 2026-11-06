"""The P2 package matrix for Goodnight Inn (offline reference for the model's Package table).

Usage:  python -I project/analysis/40_package_matrix.py <parquet dir> <out dir>
Writes: <out>/packages.csv (one row per valid package) and prints the evidence summary.

Specification: project/project-state/active/04-p2-build-method.md ("The package matrix").
Conventions (recorded in 05-doorlichting-nieuwe-opzet.md):
  - 10 Goodnight Inn initiatives -> 1,024 subsets. Valid: capex <= Brands budget, >= 3
    initiatives, >= 1 GrowthInitiative = "Yes", GI-02 only together with GI-01.
  - Dependent projects start when their prerequisite goes live (GI-02 starts the month
    GI-01 completes). Every other project starts at EarliestStart.
  - Capex evenly over DurationMonths; rooms out of service lose RoomsOutOfServicePct of the
    mapped hotels' 2025 total revenue during works, no cost relief; benefit = annual
    operating-profit impact / 12, ramped 50 / 85 / 100 % (FinanceParameters).
  - Constant 2025 dollars; horizon Jan 2027 - Dec 2032; no residual value.
  - Discounting (decided in 04-p2-build-method.md: "8% monthly discounting"): each month's
    net flow / 1.08 ** (k / 12), k = months after January 2027 (January 2027 = 0), i.e.
    discounted to the close of the 2026 planning year. "--annual" switches to the earlier
    sketch convention (each year's net flow / 1.08 ** (year - 2026)) for comparison.
  - Package values are sums of project values: the dataset gives no interaction effects.
"""
import itertools
import sys
from pathlib import Path

import pandas as pd

d = Path(sys.argv[1]); out = Path(sys.argv[2]); MONTHLY = "--annual" not in sys.argv
out.mkdir(parents=True, exist_ok=True)
r = lambda t: pd.read_parquet(d / f"{t}.parquet")
P = r("InvestmentProjects"); S = r("InvestmentScenarios"); PP = r("InvestmentProjectProperties")
H = r("Hotels"); MP = r("MonthlyPerformance"); FP = r("FinanceParameters").set_index("Parameter").Value; B = r("Brands").set_index("Brand")

BRAND = "Goodnight Inn"
P = P[P.Brand == BRAND].set_index("ProjectID").sort_index()
IDS = list(P.index)
BUDGET = float(B.InvestmentBudgetUSD[BRAND])
RATE = float(FP["Discount rate"]); RAMP = (float(FP["Ramp-up - first year after completion"]), float(FP["Ramp-up - second year after completion"]), float(FP["Ramp-up - third year onwards"]))
FIRST, LAST = int(FP["Earliest investment date"]), int(FP["Impact horizon"])
MONTHS = pd.period_range(f"{FIRST}-01", f"{LAST}-12", freq="M")
SCEN = ["Low", "Expected", "High"]

rev25 = MP[MP.Month.dt.year == 2025].groupby("HotelID").TotalRevenue.sum()
brand_hotels = set(H[H.Brand == BRAND].HotelID)


def start_of(pid):
    s = pd.Period(P.EarliestStart[pid], freq="M")
    dep = P.DependsOn[pid]
    if isinstance(dep, str) and dep in P.index:
        s = max(s, start_of(dep) + int(P.DurationMonths[dep]))
    return s


def hotels_of(pid):
    hs = set(PP[PP.ProjectID == pid].HotelID)
    return hs if hs else (brand_hotels if P.Scope[pid] == "Brand-wide" else set())


rows = []; yearly = []
for pid in IDS:
    st = start_of(pid); dur = int(P.DurationMonths[pid]); live = st + dur
    mapped_rev = rev25[rev25.index.isin(hotels_of(pid))].sum()
    for sc in SCEN:
        e = S[(S.ProjectID == pid) & (S.Scenario == sc)].iloc[0]
        op = float(e.AnnualOperatingProfitImpactUSD)
        f = pd.DataFrame(index=MONTHS, columns=["capex", "disr", "ben"], data=0.0)
        for m in MONTHS:
            if st <= m < live:
                f.loc[m, "capex"] = float(P.CapexUSD[pid]) / dur
                f.loc[m, "disr"] = float(P.RoomsOutOfServicePct[pid]) * mapped_rev / 12
            elif m >= live:
                k = (m - live).n
                f.loc[m, "ben"] = op / 12 * (RAMP[0] if k < 12 else RAMP[1] if k < 24 else RAMP[2])
        f["net"] = f.ben - f.capex - f.disr
        if MONTHLY:
            npv = sum(v / (1 + RATE) ** (((m.year - FIRST) * 12 + m.month - 1) / 12) for m, v in f.net.items())
        else:
            y = f.net.groupby(f.index.year).sum()
            npv = sum(v / (1 + RATE) ** (yr - (FIRST - 1)) for yr, v in y.items())
        for yr, v in f.net.groupby(f.index.year).sum().items():
            yearly.append(dict(ProjectID=pid, Scenario=sc, Year=int(yr), Net=v))
        cum = f.net.groupby(f.index.year).sum().cumsum()
        payback = next((int(yr) for yr, v in cum.items() if v >= 0), None)
        rows.append(dict(ProjectID=pid, Scenario=sc, Start=str(st), Live=str(live), Capex=f.capex.sum(), Disruption=f.disr.sum(),
                         Benefit=f.ben.sum(), Net=f.net.sum(), NPV=npv, RunRate2032=f.ben[f.index.year == LAST].sum(), Payback=payback,
                         SatPts=float(e.SatisfactionChangePts), Hotels=len(hotels_of(pid))))
PR = pd.DataFrame(rows)

print(f"== conventions: {'monthly, (1+r)^(k/12), k = months after Jan 2027' if MONTHLY else 'annual, (1+r)^(year-2026)'}; rate {RATE:.0%}; ramp {RAMP}; horizon {FIRST}-{LAST}; budget ${BUDGET/1e6:.1f}M")
print("\n== per project")
for sc in SCEN:
    t = PR[PR.Scenario == sc].set_index("ProjectID")
    print(f"-- {sc}")
    for pid, x in t.iterrows():
        print(f"  {pid} {P.ProjectName[pid][:42]:42} capex {P.CapexUSD[pid]/1e6:6.2f}  start {x.Start} live {x.Live}  disr {x.Disruption/1e6:5.2f}  benefit {x.Benefit/1e6:6.2f}  "
              f"NPV {x.NPV/1e6:6.2f}  run-rate 2032 {x.RunRate2032/1e6:5.2f}  payback {int(x.Payback) if pd.notna(x.Payback) else "after 2032"}  sat {x.SatPts:+.2f} on {x.Hotels} hotels  growth {P.GrowthInitiative[pid]}")

V = {sc: PR[PR.Scenario == sc].set_index("ProjectID") for sc in SCEN}
packs = []
for k in range(1, len(IDS) + 1):
    for combo in itertools.combinations(IDS, k):
        cs = set(combo)
        capex = float(P.CapexUSD[list(combo)].sum()); growth = int((P.GrowthInitiative[list(combo)] == "Yes").sum())
        dep_ok = all(not (isinstance(P.DependsOn[x], str) and P.DependsOn[x] not in cs) for x in combo)
        excl_ok = all(not (isinstance(P.ExclusiveWith[x], str) and P.ExclusiveWith[x] in cs) for x in combo)
        valid = capex <= BUDGET and len(cs) >= 3 and growth >= 1 and dep_ok and excl_ok
        if not valid:
            continue
        rated = set().union(*[hotels_of(x) for x in combo if V["Expected"].SatPts[x] > 0]) if any(V["Expected"].SatPts[x] > 0 for x in combo) else set()
        row = dict(PackageID="+".join(x[-2:] for x in combo), Projects=len(cs), Growth=growth, CapexUSD=capex,
                   ContainsRefresh="Yes" if "GI-07" in cs else "No", RoomsAdded=int(P.AddedRooms[list(combo)].sum()), HotelsRated=len(rated))
        for sc in SCEN:
            row[f"NPV_{sc}"] = float(V[sc].NPV[list(combo)].sum())
            row[f"RunRate_{sc}"] = float(V[sc].RunRate2032[list(combo)].sum())
            row[f"Net_{sc}"] = float(V[sc].Net[list(combo)].sum())
        packs.append(row)
K = pd.DataFrame(packs)
print(f"\n== valid packages: {len(K)} of {2**len(IDS)} subsets")
for sc in SCEN:
    print(f"  NPV >= 0 in {sc}: {(K[f'NPV_{sc}'] >= 0).sum()}")


def presets(sc):
    n = f"NPV_{sc}"
    a = K.loc[K[n].idxmax()]
    pos = K[K[n] >= 0]
    b = pos.sort_values(["HotelsRated", n], ascending=False).iloc[0] if len(pos) else None
    c = K[K.ContainsRefresh == "Yes"].sort_values(n, ascending=False).iloc[0]
    return a, b, c


K["Shortlist_Expected"] = ""
for sc in SCEN:
    a, b, c = presets(sc)
    print(f"\n== presets, {sc} lens")
    for lab, x in (("A max NPV", a), ("B widest rated reach, NPV >= 0", b), ("C best with the refresh (GI-07)", c)):
        if x is None:
            print(f"  {lab}: none (no package has NPV >= 0)"); continue
        print(f"  {lab}: {x.PackageID}  capex {x.CapexUSD/1e6:.2f}M  NPV L/E/H {x.NPV_Low/1e6:+.1f} / {x.NPV_Expected/1e6:+.1f} / {x.NPV_High/1e6:+.1f}  "
              f"run-rate E {x.RunRate_Expected/1e6:+.2f}M  rated hotels {x.HotelsRated}  rooms added {x.RoomsAdded}")
    if sc == "Expected":
        for lab, x in (("A", a), ("B", b), ("C", c)):
            if x is not None:
                K.loc[K.PackageID == x.PackageID, "Shortlist_Expected"] += lab

for pid in ("01+02+04+05+07+10", "01+02+04+05+07+09+10", "01+02+03+05+08+09+10"):
    x = K[K.PackageID == pid]
    if len(x):
        x = x.iloc[0]
        print(f"\n== reference package {pid}: capex {x.CapexUSD/1e6:.2f}M  NPV L/E/H {x.NPV_Low/1e6:+.1f} / {x.NPV_Expected/1e6:+.1f} / {x.NPV_High/1e6:+.1f}  run-rate E {x.RunRate_Expected/1e6:+.2f}M")
    else:
        print(f"\n== reference package {pid}: not valid")

# sensitivity: running cost read as NOT yet netted in the organisers' OP impact
gross = {x: float(P.AnnualRunningCostUSD[x]) for x in IDS if P.AnnualRunningCostUSD[x] > 0}
print("\n== sensitivity: annual running cost subtracted on top of the OP impact (gross reading)")
for pid, rc in gross.items():
    t = V["Expected"].loc[pid]
    print(f"  {pid}: running cost ${rc/1e6:.2f}M/yr; Expected run-rate {t.RunRate2032/1e6:.2f} -> {(t.RunRate2032 - rc)/1e6:.2f}")
K.sort_values("NPV_Expected", ascending=False).to_csv(out / "packages.csv", index=False, float_format="%.0f")
PR.to_csv(out / "project_economics.csv", index=False, float_format="%.2f")
pd.DataFrame(yearly).to_csv(out / "project_yearly.csv", index=False, float_format="%.2f")
print(f"\nwritten: {out/'packages.csv'} ({len(K)} rows), {out/'project_economics.csv'}")
