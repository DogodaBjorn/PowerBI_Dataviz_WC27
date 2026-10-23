# Experiment Design

Goal in a timed round: a clean test plan a jury trusts. Hypothesis, one variable, a metric chosen in advance, a sample-size logic, a decision rule.

## 1. Hypothesis format

"If we [change], for [audience/placement], then [primary metric] will [direction + size] because [mechanism]. We will decide with [rule] after [N events / budget]."

Example: "If we lead with the fare-negotiation hook (vs the generic app demo) for Lagos Android users on TikTok, first-ride CPA will fall by at least 20% because the hook states the product's distinct benefit. Decision: scale if CPA <= 0.75x target after 15 first rides; stop if > 1.5x after $60 spend."

Fields to write per test: ID | Hypothesis | Variable | Control | Variant(s) | Audience/placement | Primary metric | Guardrail metrics | MDE | Budget | Duration | Decision rule | Owner.

## 2. Test types

| Type | Compares | Use when | Cost |
|---|---|---|---|
| A/B | 1 change, 2 arms | One clean question | Lowest |
| A/B/n | 1 variable, n values | Several hooks/offers at once | Per-arm sample multiplied; control for multiple comparisons |
| Multivariate (MVT) | Combinations of several variables | Large traffic only; want interactions | Sample explodes; usually too heavy for paid social |
| Holdout / lift | Exposed vs unexposed | Causal impact of the whole channel/tactic | Need volume and design (see incrementality-mmm.md) |
| Sequential / bandit | Allocates traffic to the leader | Many cheap creatives, short life | Faster exploitation but weaker inference |
| Pre/post | Before vs after | Last resort | Confounded by time |

## 3. Sample size: formula and rule of thumb

Two-proportion test (conversion-rate type metrics), per arm:

n ≈ 16 x p(1-p) / delta^2   (about 80% power, alpha 0.05 two-sided)

where p = baseline rate, delta = absolute difference you want to detect. Exact: n = 2 x (z_a + z_b)^2 x p(1-p) / delta^2 with z_a = 1.96, z_b = 0.84 -> 15.7 x p(1-p)/delta^2.

Worked examples:
- p = 4% CVR, want +20% relative (delta 0.8 pts = 0.008): n ≈ 16 x 0.04 x 0.96 / 0.008^2 = 0.6144 / 0.000064 = 9,600 clicks per arm.
- p = 10% activation, +20% relative (delta 0.02): n ≈ 16 x 0.1 x 0.9 / 0.0004 = 3,600 installs per arm.
- p = 1% (click to rare event), +30% relative (0.003): n ≈ 16 x 0.0099 / 0.000009 = 17,600 per arm.

Simple heuristics:
- Halving the detectable effect quadruples the sample.
- Rare events (low p) need huge samples; test on an upstream metric (CTR, IPM) first and confirm downstream.
- Event-count rule of thumb: you need on the order of 100+ conversions per arm to detect a 20-30% difference in CPA; below 30 per arm, only huge (>2x) differences are credible.
- CPA/CPI are ratios of spend to counts; the noise is dominated by the number of conversions.

Python:
```python
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
es = proportion_effectsize(0.048, 0.04)   # variant vs baseline
n = NormalIndPower().solve_power(es, power=0.8, alpha=0.05, alternative="two-sided")
```

## 4. Significance, power, MDE in plain words

- Significance (alpha 0.05): if there were no real difference, we'd see a gap this large by chance only 5% of the time. p-value is NOT the probability the variant is better.
- Power (80%): if the real difference is at least the MDE, we'd detect it 80% of the time. Low power = "no significant difference" is meaningless.
- MDE (minimum detectable effect): smallest change worth acting on and detectable with your budget. Decide it before the test. If MDE at your budget is 40%, say so.
- Confidence interval: range of plausible effect sizes; report it, not just win/lose.
- Practical significance: a 3% CPA gain that costs more to implement than it saves is not a win.

## 5. Peeking and multiple comparisons

- Peeking: checking repeatedly and stopping at the first p<0.05 inflates false positives (can exceed 20-30%). Fix: pre-set sample size and stopping rule, or use sequential methods/Bayesian with stated thresholds.
- Multiple arms/metrics: with 20 creatives, 1 will look "significant" by chance. Use a pre-chosen primary metric, Bonferroni/Holm for a small set, or treat results as a ranking and confirm winners in a second round (winner's curse: the top performer regresses toward the mean).
- Don't slice after the fact without labelling it exploratory.

## 6. Bayesian vs frequentist (one-liner)

- Frequentist: "How surprising is this data if there's no difference?" (p-value, fixed sample).
- Bayesian: "What's the probability variant B beats A, and by how much?" (posterior, handles continuous monitoring and small data, needs a prior; decisions like "ship if P(B>A) > 95% and expected loss < X").
- In a short paid-social test, a Bayesian read plus a spend-based stop rule is often more practical; for audit-grade claims use the frequentist design.

## 7. Platform A/B tools

| Platform | Tool | Notes |
|---|---|---|
| Meta | Ads Manager A/B test (Experiments), also via API [CHECK]; Advantage+ creative tests | Splits audiences randomly so that no overlap; tests creative, audience, placement, optimization; reports probability of winning / cost per result; minimum duration ~7 days recommended [CHECK] |
| Google | Experiments (campaign experiments, custom), Performance Max experiments, video experiments (YouTube) | 50/50 traffic splits, cookie/search-based; PMax asset-level A/B [CHECK] |
| TikTok | Split Test in Ads Manager | Splits ad groups/audiences; one variable, enough budget [CHECK] |
| LinkedIn | A/B test (campaign-level) | Small audiences; slower |
| App stores | Google Play Store Listing Experiments, Apple Product Page Optimization | Test icon, screenshots, copy (installation conversion) |

Native splits avoid audience overlap contamination, which running two ads in one ad set does not (the algorithm picks favorites early; that's not an A/B).

## 8. Creative testing framework (iteration ladder)

Test big before small. Each rung needs fewer variants and finer variables.

1. Concept (the big idea / problem-solution / emotional territory): 3-5 truly different concepts. Cheapest big lever.
2. Angle (benefit/proof: price, safety, speed, social proof, status): 2-3 per winning concept.
3. Hook (first 1-3 s, first frame, headline): 3-5 per winning angle. Measure hook rate and hold rate.
4. Format (UGC vs motion graphic vs static, length, aspect ratio, language/voice): 2-3.
5. Details (CTA, colours, end card, captions, music): small gains; last.

Rules:
- Same budget, audience, placement, optimization event, timing per cell.
- Change one rung's variable at a time; label every creative with concept/angle/hook/format/language tags (naming convention) so you can do segment analysis afterward.
- Read upstream (hook rate, CTR, IPM) first, confirm on the business event (CPA, activation).
- Keep the winner alive as control in the next round.
- Production reality: iterate by splicing new hooks onto the winning body.

## 9. Holding variables constant (checklist)

- Same campaign objective and optimization event; same bid strategy and bid.
- Same audience and exclusions, same geo, same device/OS split (or split by it deliberately).
- Same placements, same start time and run window (no day-of-week mismatch), same budget per cell.
- Same landing page/store listing/deep link and attribution window.
- No edits mid-test; no overlapping tests on the same audience.
- Same naming/UTMs for traceability.
- Watch for external shocks (holiday, outage, promo, competitor).

## 10. Test plan template (copy)

| ID | Hypothesis | Variable | Control | Variant | Audience | Primary metric | Guardrail | MDE | Budget | Duration | Decision rule |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T1 | Hook A beats generic on first-ride CPA by >= 20% | Hook | Generic demo | Fare-negotiation hook | Lagos Android, TikTok | CPA first ride | activation >= 80% of avg | 20% | $X | until 15 events / arm or $60 per arm | scale <= 0.75x T; stop > 1.5x T |
