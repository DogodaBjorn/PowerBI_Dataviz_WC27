# KPI Glossary (performance marketing)

Use: look up a metric mid-round. Format per row: formula | tells you | does NOT tell you | pitfall.
Rule zero: recompute every ratio from raw spend and counts. Never trust provided ratio columns.

## 1. Delivery and cost of attention

| KPI | Formula | Tells you | Does NOT tell you | Pitfall |
|---|---|---|---|---|
| Impressions | count of ad renders | Volume of delivery | Whether anyone saw/noticed it | Counted on render, not viewability; video "impression" can be 1 ms on some platforms |
| Reach | unique people (or accounts/devices) | Breadth | Depth, quality | Not additive across campaigns/platforms (overlap); platform reach is modeled and cross-device dedup differs |
| Frequency | impressions / reach | Avg exposures per person | Distribution (avg hides a tail of 15+ hits) | High frequency on a small audience = fatigue; low frequency on a conversion goal = under-exposure |
| CPM | spend / impressions x 1000 | Price of attention; auction pressure | Quality of the attention | Low CPM often = junk placements or low-intent audience. Never optimize CPM alone |
| CTR (link) | link clicks / impressions | Whether the ad earns a click to the destination | Intent after click | Use link CTR (outbound), not "CTR (all)" |
| CTR (all) | all clicks / impressions | Engagement of any kind (likes, shares, profile, expand) | Traffic to the site/store | Meta "CTR (all)" inflates with non-link clicks; looks 2-3x better than link CTR; clickbait lifts it |
| CPC | spend / clicks | Cost of a visit | Visit value | Define which click (link vs all). Cheap CPC + bad CVR = expensive CPA |
| CPV (video) | spend / views | Cost of a view | View quality | View definition differs: Meta 3 s / ThruPlay, TikTok 2 s / 6 s, YouTube 30 s or interaction [CHECK current definitions] |

## 2. Conversion funnel

| KPI | Formula | Tells you | Does NOT tell you | Pitfall |
|---|---|---|---|---|
| CVR (click to conv.) | conversions / clicks | Post-click funnel quality | Pre-click audience fit | Denominator must match: link clicks vs landing page views vs sessions. Click-to-install differs by platform |
| CPI (cost per install) | spend / installs | Cost to get an app on a device | Whether the user does anything | Cheapest installs are often lowest quality. Judge by cost per downstream event |
| IPM (installs per mille) | installs / impressions x 1000 | Creative + audience efficiency independent of CPM | Quality of installs | Mixes CTR and click-to-install CVR. Good for ranking creatives only if the CPM is comparable |
| Install-to-action rate (activation) | users doing key event / installs | Install quality, onboarding friction | Cause (creative promise vs product vs tracking lag) | Cohort and window matter: "within 7 days of install". Same-day vs eventual rates are not comparable |
| CPA (generic) | spend / conversions of the chosen event | Efficiency at that event | Value, quality, incrementality | Must state the event. "CPA" in a deck without event = ambiguous |
| CPA of the business event (first ride, first purchase, first deposit) | spend / users completing the event | The cost of the thing the business pays for | Retention or LTV of those users | Lags install by days. Recent creatives have immature data: compare on equal windows. Small counts (n<30) = noisy |
| Cost per lead (CPL) | spend / leads | Lead acquisition price | Lead quality | Cheapest CPL usually = lowest quality (instant forms, no friction) |
| Lead-to-SQL rate | SQL / leads | Lead quality | Revenue | Needs CRM feedback and a consistent SQL definition; lag of weeks |
| Pipeline | sum of open opportunity value | Future revenue potential | Close rate | Inflated by stage definitions; use weighted pipeline and cost per pipeline $ |

## 3. Value and unit economics

| KPI | Formula | Tells you | Does NOT tell you | Pitfall |
|---|---|---|---|---|
| ROAS | revenue / ad spend | Revenue return on spend | Profit | Platform ROAS = attributed revenue, over-claims. Ignores margin and returns |
| MER / blended ROAS | total revenue / total marketing spend | Whole-business efficiency, attribution-free | Which channel works | Includes organic/brand/repeat revenue, moves with seasonality |
| POAS | gross profit / ad spend | Profit return on spend | Long-term value | Needs correct margin (after COGS, shipping, returns). POAS > 1 = break-even on gross profit |
| Contribution margin | revenue - variable costs (COGS, fulfilment, payment, discounts) - ad spend | What is left to cover fixed costs | Fixed-cost recovery | Choose whether ad spend is inside or outside. State it |
| AOV | revenue / orders | Basket size | Margin | Raising AOV through discounts can lower margin |
| CAC | (acquisition spend, + salaries/tools if fully loaded) / new customers | Cost to win a customer | Whether the customer pays back | Blended vs paid CAC; "customer" must be new, not repeat. Fully loaded vs media-only: state which |
| LTV | avg margin per period x expected lifetime (or discounted cumulative margin) | Long-run value per customer | Short-term cash | Use margin, not revenue. Early cohorts extrapolated = guesswork; flag assumptions |
| LTV:CAC | LTV / CAC | Scalability of acquisition | Cash timing | Rule of thumb ~3:1 is a SaaS heuristic, not universal [CHECK vs sector]. Ratio can look great with 36-month payback |
| Payback period | CAC / (monthly margin per customer) | Months to recover CAC | Lifetime profit | Cash constraint decides how long a payback you can afford |
| Incrementality / iROAS | incremental revenue / spend, where incremental = test - control | Causal return | Why it works | Needs a holdout/lift/geo test. Typically lower than platform ROAS |

## 4. Retention

| KPI | Formula | Tells you | Does NOT tell you | Pitfall |
|---|---|---|---|---|
| Retention D1 / D7 / D30 | users active on day N / installs (cohort day 0) | Product-market fit, install quality | Why they left | Classic (exact day N) vs rolling (day N or later): not comparable. Define active (open vs key event) |
| Churn | customers lost in period / customers at start | Leak rate | Why | Monthly churn of 5% = ~46% lost per year, not 60%; compound it |

## 5. Video / attention

| KPI | Formula | Tells you | Does NOT tell you | Pitfall |
|---|---|---|---|---|
| Hook rate | 3-second views / impressions | Whether the first seconds stop the scroll | Whether the message works | Definition varies (Meta 3 s plays; TikTok 2 s). Autoplay-by-placement bias. High hook + low hold = misleading opener |
| Hold rate | ThruPlays or 15 s views / 3 s views (or / impressions; state which) | Whether the body keeps people | Action | Compare only at equal video length |
| ThruPlay | views to completion or 15 s, whichever first (Meta) | Quality view count | Intent | Short videos (<15 s) inflate completion |
| VTR (view-through rate) | views / impressions | Share viewing | Quality | YouTube VTR counts views at 30 s or interaction [CHECK]; do not mix with Meta 3 s |

## 6. Brand

| KPI | Formula | Tells you | Does NOT tell you | Pitfall |
|---|---|---|---|---|
| Brand lift | (exposed positive rate - control positive rate) | Causal shift in awareness/consideration/intent | Sales | Needs sample size; survey-based; platform-run (Meta, YouTube, TikTok) |
| Ad recall (est. ad recall lift people) | modeled people who would recall within 2 days | Memorability proxy | Brand effect | Meta metric is modeled, not a survey |
| Share of search | brand searches / (own + competitor brand searches) | Mental availability proxy, leads market share | Cause | Needs a clean competitor set, Google Trends or keyword tools; correlates with share in many categories, not all |

## 7. Compute it yourself (sanity checks, do before any analysis)

Checks that should fail loudly:
- Conversions cannot exceed installs for the same cohort; installs cannot exceed clicks (except view-through installs: flag it).
- Clicks cannot exceed impressions. Any rate above 100% = bad data (or wrong denominator).
- Reach cannot exceed impressions; frequency below 1.0 = bad data.
- CTR > ~10% on cold paid social, CVR > ~50% click-to-purchase, or CPM < $0.50 = look closer before believing [CHECK vs market].
- Spend per row = 0 with impressions > 0 = missing spend; impressions = 0 with spend > 0 = broken row.
- Totals: sum of parts must equal the grand total; compare the provided total with your sum.
- Weighted vs simple averages: blended CPA = SUM(spend) / SUM(conversions), never the mean of row CPAs.
- Duplicates: same creative ID repeated across rows without a dimension that explains it.
- Zero conversions: CPA is undefined, not 0. Show "n/a" and spend wasted.
- Small n: with fewer than ~30 conversions, treat CPA ranking as directional; give an interval.

Recompute table (do all of these first):

| Metric | Formula |
|---|---|
| CPM | spend / impressions x 1000 |
| CTR | clicks / impressions |
| CPC | spend / clicks |
| CVR click-to-install | installs / clicks |
| IPM | installs / impressions x 1000 |
| CPI | spend / installs |
| Activation | key events / installs |
| CPA (business event) | spend / key events |
| Identity check | CPA = CPM / (1000 x CTR x CVR_click_to_event) |

Identity check: if your recomputed CPA does not match CPM/(1000 x CTR x CVR), a column is mis-defined.

```python
df["cpm"]=df.spend/df.impressions*1000
df["ctr"]=df.clicks/df.impressions
df["cpi"]=df.spend/df.installs
df["act"]=df.rides/df.installs
df["cpa"]=df.spend/df.rides.replace(0,float("nan"))
bad=df[(df.clicks>df.impressions)|(df.rides>df.installs)|(df.installs>df.clicks)]
```
