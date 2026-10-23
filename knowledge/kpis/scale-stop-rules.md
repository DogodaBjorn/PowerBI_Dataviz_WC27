# Scale / Hold / Stop Rules (how to write them)

A rule = unit + metric + minimum data + threshold + action + next review. Write them as numbers relative to target CPA (T), never as vibes.
Numbers below are starting defaults, adjust for event volume, cost per event and risk. [CHECK] against account history.

## 1. Minimum data: count events, not days

| Decision | Minimum before acting | Why |
|---|---|---|
| Kill a clear loser | Spend >= 2-3x T with 0 target events (or <=1) | You've paid for the chance of 2-3 conversions and got none |
| Rank / early cut on upstream metric (CTR, IPM) | >= 1,000-2,000 impressions and >= 50-100 clicks per creative | Rough read only |
| Scale a winner | >= 10-15 target events at CPA <= 0.75x T (prefer 20+) | Below this, CPA is mostly noise |
| Declare a statistical winner | >= 30-50 events per arm, and test power per experiment-design.md | Intervals still wide at 30 |
| Platform exits learning | ~50 optimization events per ad set / 7 days (Meta) [CHECK] | Algorithm needs signal |
| Judge ROAS / payback | Full attribution window + purchase lag | Late conversions land after |

Rough 90% interval on a conversion count N: N +/- 1.65 x sqrt(N). With N=10 the CPA can be off by about +/-50%; with N=30 about +/-30%; N=100 about +/-16%. Use this to justify your minimum.

Time is a secondary guard: at least 3-4 days (to cover day-of-week) and, for apps, wait for install-to-event lag (D1-D3 for ride/purchase events).

## 2. Thresholds relative to target CPA (T)

| Band | Condition (after min data) | Action |
|---|---|---|
| Scale hard | CPA <= 0.5x T | Step budget up 30%, duplicate to new ad set / audience, produce variants of this concept |
| Scale | 0.5x < CPA <= 0.75x T | Step budget up 20% every 3-4 days |
| Hold | 0.75x < CPA <= 1.25x T | Keep budget, collect data, test one change |
| Watch | 1.25x < CPA <= 1.5x T | Reduce budget 20-30% or hold one more window; cap review at 2 windows |
| Stop | CPA > 1.5x T and spend >= 2-3x T | Pause; archive learnings |
| Instant stop | Spend >= 3x T and 0 events; or policy/brand risk; or tracking fault confirmed | Pause now |

Never decide on one metric:
- Scale only if downstream quality holds (activation / D7 / SQL rate within 80% of account average).
- Do not scale a creative that wins on CPA with n<10 or is dominated by one day.

## 3. Budget step-ups

- Meta: raise a budget by 20-30% at most every 3-4 days (some practitioners go to 50% once; larger jumps risk learning reset and CPA spike) [CHECK]. Alternative: duplicate the winning ad set with a higher budget (a new learning phase starts; check cannibalization).
- Google: gradual changes (about 20-30%) every 1-2 weeks on tROAS/tCPA campaigns; do not change target and budget the same day.
- TikTok: budget increases of about 20-30% per day max on ad group level, and plan more creatives [CHECK].
- LinkedIn: scale slowly; tighten the audience before raising budgets.
- Scale in order: budget -> duplicate to new audience/geo -> new creative variants -> new platform.
- Expect efficiency to decay on scale: CPA often rises with spend. Plan a stop-loss: if CPA > 1.25x the pre-scale CPA for 2 consecutive windows after a step, revert the last step.

## 4. Creative fatigue triggers

Any 2 of the following, over a window of 3+ days with enough volume:
- Frequency > ~3-4 in 7 days (prospecting; adjust by audience size) [CHECK].
- CTR falls >= 20-25% vs its own first-week level.
- Hook rate falls >= 20%.
- CPM rises >= 20% with unchanged audience.
- CPA rises >= 25-30% with stable CVR and tracking.
Action: swap or add new creatives from the same winning concept (new hook/format), keep the old ad alive but low budget; do not edit the live ad (resets learning), create a new ad.
TikTok fatigue is faster (refresh weekly or twice weekly on high spend); Meta slower; LinkedIn slowest but small audiences saturate.

## 5. Test-budget rule of thumb

- Reserve 10-20% of total budget for tests (explore) and 80-90% for proven allocations (exploit), as a start.
- Per test cell, fund enough to reach the "scale" evidence bar if the cell is good: cell budget = T x events needed. Example: T=$20, need 15 events -> about $300 per cell for a cell performing near T. A losing cell is cut at 3x T = $60.
- Kill-early rule keeps the cost of a loser at about 3x T. Expected cost of testing N concepts = N x 3x T for the losers.
- Number of cells = test budget / per-cell budget; if you can't fund 20 cells, test fewer, cleaner ones.

## 6. When the target KPI is lagged (apps: first ride)

- Use a two-stage rule: upstream gate (IPM, CPI, activation within first 24-72 h) to filter, downstream gate (cost per first ride after the lag) to scale.
- Be explicit: "Scale decisions use first-ride CPA from installs >= 3 days old; younger installs use CPI + early activation as provisional."
- Provisional decisions get smaller budget steps (10-15%).

## 7. Copy-paste template

Rule table:

| Rule ID | Unit | Metric | Min data | Condition | Action | Review |
|---|---|---|---|---|---|---|
| S1 | Creative x channel | CPA(first ride) | >= 15 events | CPA <= 0.75x T | +20% budget / 3 days; make 3 variants | every 3 days |
| S2 | Creative x channel | CPA(first ride) | >= 15 events | CPA <= 0.5x T | +30% budget; duplicate to new audience | every 3 days |
| H1 | Creative x channel | CPA(first ride) | >= 10 events | 0.75x T < CPA <= 1.25x T | Hold, collect data | weekly |
| W1 | Creative x channel | CPA(first ride) | >= 10 events | 1.25x T < CPA <= 1.5x T | -20% budget, review in 3 days | 3 days |
| X1 | Creative x channel | CPA(first ride) | Spend >= 2-3x T | CPA > 1.5x T | Pause | immediate |
| X2 | Creative x channel | Spend vs events | Spend >= 3x T | 0 events | Pause | immediate |
| F1 | Creative | CTR / freq | 3 days, >= 1k impr/day | CTR -20% and freq > 3.5 | Replace creative | daily |
| Q1 | Creative | Quality gate | n/a | activation < 80% of avg | Do not scale even if CPA good | per review |

One-liner version for a jury: "Scale at <= 0.75x target CPA after 15 conversions in steps of 20% per 3 days; hold between 0.75x and 1.25x; stop above 1.5x once spend has reached 2-3x target CPA. Refresh creative at frequency > 3.5 with a 20% CTR drop. 15% of budget stays in tests."

Worked numbers: T = $20. Scale <= $15 (n>=15), hold $15-$25, watch $25-$30, stop > $30 after $40-$60 spend. Winner at $12 with n=20 -> +30%.
