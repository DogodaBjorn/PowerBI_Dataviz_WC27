# KPI Driver Trees

Purpose: turn "CPA is bad" into "which link in the chain is bad, and which lever moves it".
Every tree is multiplicative, so changes can be split into drivers with logs or simple ratios.

## A. Revenue / profit tree (ecommerce, direct response)

```
Spend
 -> / CPM x 1000 = Impressions                    (auction price, placement, audience size, creative quality score)
 -> x CTR        = Clicks                         (creative, hook, offer visibility, audience fit)
 -> x CVR        = Conversions (orders)           (landing page, price, trust, speed, offer, tracking loss)
 -> x AOV        = Revenue                        (bundles, upsell, price, mix)
 -> x Margin %   = Gross profit                   (COGS, discounts, returns, shipping)
 -> - Spend      = Contribution (profit after ads)
```
Identities:
- CPA = CPM / (1000 x CTR x CVR)
- ROAS = AOV / CPA = AOV x 1000 x CTR x CVR / CPM
- POAS = ROAS x margin %
- Break-even CPA = AOV x margin % (before other variable costs)
- Break-even ROAS = 1 / margin %
- Target CPA from LTV: allowed CPA = LTV (margin) / required LTV:CAC ratio

## B. App tree (installs, first key event)

```
Spend
 -> / CPM x 1000 = Impressions
 -> x IPM / 1000 = Installs          (IPM = CTR x click-to-install CVR x 1000; CPI = CPM / IPM)
 -> x Activation = First key event   (first ride / first purchase / registration; onboarding, promise-product fit, incentive, tracking lag)
 -> x Retention  = Repeat users      (D1 / D7 / D30; product + quality of the user)
 -> x Value      = Revenue / LTV
```
Identities:
- CPI = CPM / IPM
- CPA(key event) = CPI / activation rate
- CPA(key event) = CPM / (IPM x activation rate)   [IPM per mille impressions]
- Cost per retained user D7 = CPA(key event) / (key-event-to-D7 retention)

Reading tip: when ranking creatives, look at IPM (upstream), then activation (downstream). A creative with great IPM and poor activation attracts the wrong people or over-promises. A creative with modest IPM and high activation is often the scalable one. Final judge = CPA of the business event, with a sample-size check.

## C. Lead-gen tree (B2B / services)

```
Spend
 -> / CPM -> Impressions
 -> x CTR -> Clicks
 -> x Lead CVR -> Leads (MQL)         (form friction, offer, message match)
 -> x Lead-to-SQL -> SQLs             (targeting quality, qualification, speed to lead)
 -> x SQL-to-opportunity -> Opps      (sales process; out of marketing control)
 -> x Win rate -> Customers
 -> x ACV x margin -> Gross profit
```
Identities: CPL = CPC / lead CVR; cost per SQL = CPL / lead-to-SQL; CAC = cost per SQL / (SQL-to-win rate).
Trap: optimizing CPL while lead-to-SQL collapses. Report cost per SQL or cost per pipeline $ as the headline; CPL is a diagnostic.

## D. Decomposing a CPA change (worked example)

CPA = CPM / (1000 x CTR x CVR). Compare period 1 vs period 2.

| Driver | Period 1 | Period 2 | Ratio P2/P1 |
|---|---|---|---|
| CPM | $5.00 | $6.00 | 1.200 |
| CTR | 1.00% | 0.80% | 0.800 |
| CVR (click to event) | 4.00% | 4.50% | 1.125 |
| CPA | $12.50 | $16.67 | 1.333 |

Check: CPA1 = 5 / (1000 x 0.01 x 0.04) = 5 / 0.40 = $12.50. CPA2 = 6 / (1000 x 0.008 x 0.045) = 6 / 0.36 = $16.67.

CPA ratio = CPM ratio / (CTR ratio x CVR ratio) = 1.200 / (0.800 x 1.125) = 1.333.

Attribution of the +33% (log method, shares add to 100%):
- CPM: ln(1.200) = 0.182 (63% of the change)
- CTR: ln(1/0.800) = 0.223 (78%)
- CVR: ln(1/1.125) = -0.118 (-41%, helped)
- Total ln(1.333) = 0.288. Shares: 63% + 78% - 41% = 100% (rounded)

Read-out: "CPA rose 33% because CTR fell 20% and CPM rose 20%; better CVR offset a third. Fix the front of the funnel (creative fatigue / audience saturation), not the landing page."

```python
import numpy as np
r = {"cpm":6/5, "ctr_inv":0.01/0.008, "cvr_inv":0.04/0.045}
tot = np.log(np.prod(list(r.values())))
print({k: round(np.log(v)/tot,2) for k,v in r.items()})
```

For the app tree, same method with CPA = CPM / (IPM x activation): split into CPM, IPM, activation.

## E. Finding the binding constraint

Binding constraint = the link that, if brought to benchmark, moves the end KPI the most (or the one that physically caps scale).

1. Write the chain with actual numbers per row (campaign, creative, channel).
2. Compare each link to a reference: best-in-set, target, or prior period. Gap ratio = reference / actual.
3. The link with the biggest gap ratio (largest drag on CPA) is the candidate. Because CPA is multiplicative, a 2x gap anywhere costs 2x CPA, regardless of which link.
4. Then check whether it is fixable at the layer you control:
   - CPM high: audience too narrow, placement, competition/seasonality, low quality/relevance. Lever: broaden, placements, creative.
   - CTR low: creative/hook/offer. Lever: new concepts.
   - Click-to-install low: store page, load time, wrong audience, click fraud. Lever: store listing, deep links, exclude placements.
   - Activation low: onboarding, expectation mismatch, incentive, tracking lag. Lever: creative promise alignment, optimize to a deeper event.
   - Retention low: product/user quality; no ad fix beyond targeting and value-based bidding.
5. Cap constraints (not efficiency): audience size (frequency rising), budget cap, learning limit (<50 events/week/ad set on Meta), inventory, approval, creative supply.
6. Report as: "Binding constraint = X (value vs reference, gap Y x). Lever = Z. Expected CPA effect if closed = W."

Quick table for a creative CSV:

| Creative | CPM | CTR | Click-to-install | Activation | CPA | Weakest link vs best-in-set |
|---|---|---|---|---|---|---|
| fill | | | | | | pick the column with the lowest ratio to the best |

## F. Sensitivity (which lever is worth the most)

Because of the multiplicative form, a +10% in CTR or CVR gives -9.1% CPA; -10% in CPM gives -10% CPA. Compare the cost and feasibility of a 10% improvement at each link, not the absolute value. Typically the cheapest 10% is in creative (CTR/IPM) or onboarding (activation), not in CPM.
