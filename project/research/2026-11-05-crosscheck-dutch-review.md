# Cross-check: "Vol huis, stille klacht, schaars geld" against the evidence pack

Review under test: *Goodnight Inn — data en visueel verhaal* (Dutch, 15 pages, dated
4 Nov 2026, filed as `2026-11-04-goodnight-inn-data-en-visueel-verhaal.pdf` in this
folder). It recomputes the dataset independently from the Excel workbook, reports
seven findings, three money pages, a five-page report sketch and an advice.
Verification script: `project/analysis/17_crosscheck_dutch_review.py`, output in
`project/analysis/output/crosscheck.txt`. Prepared 2026-11-05.

## Verdict

Numerically sound. Every claim the review shares with the mission reproduces within
rounding; its four genuinely new findings hold and are adopted below. One statement
conflicts with the starter file (a five-page structure), one is incomplete (the Official
Rules' four judging criteria, without the starter's fifth) and one method choice
overstates an effect (the event-study window). Its advice package is
the mission's plan A plus the breakfast upgrade.

## Claim by claim

| # | Review claim | Recomputed | Verdict |
|---|---|---|---|
| 1 | Occupancy 79.4 %, margin 44.4 %, NPS +3; highest and lowest of the four brands | 79.4 % · 44.4 % · +3.3; sisters NPS +15 / +20 / +32 | ✓ |
| 2 | NPS fell at 45 of 50 hotels; 12 below zero | 45 of the 48 hotels with 2021 survey data (Valencia, Porto opened later); 12 below zero; 38 of 50 fell in 2025 alone | ✓ with nuance |
| 3 | Room condition is the largest complaint category per night and rose +9 % in 2025; other categories −4.3 % to +0.9 %; +17 % since 2021 | 1.80 per 1,000 nights; +9.0 % in 2025; others −4.3 % (F&B) to +0.9 % (Wi-Fi); +16.8 % since 2021 | ✓ |
| 4 | Check-in & waiting rose most over the window (+25 %) but flattened in 2025 (−2 %) | +24.8 % 2021→2025; −1.6 % in 2025 | ✓ — the mission called check-in "fastest-rising" (true over the window); the 2025 momentum is room condition. Adopted. |
| 5 | Margin peaked 2023 at 46.1 %, now 44.4 %, staff cost 26.9 → 28.3 % of revenue; 48 of 50 hotels below their peak, all 50 down in 2025 | identical | ✓ |
| 6 | Value for money 7.66, lowest of the group, below P&K Select 7.72; ADR +15 % since 2021 vs +13 / +24 / +20 % | 7.659 vs 7.724 / 7.940 / 8.040; ADR +14.6 % vs Pebble & Pine +13.3, P&K +23.7, Maison d'Or +20.2 | ✓ |
| 7 | No relation between NPS decline and occupancy decline per hotel (r ≈ 0): the dissatisfaction is not yet in demand | r = −0.04 (2021→25), +0.03 (2023→25) | ✓ |
| 8 | Years since renovation vs room comfort 2025: r = −0.92 over the 44 hotels with a date | −0.923; and −0.919 over all 50 when the six never-renovated hotels use their opening date | ✓ — stronger than the NPS correlation (−0.78) the mission used. Adopted as the lead KPI. |
| 9 | Nine of the ten GI-07 hotels are the longest un-renovated; Ottawa (opened 2015) is the tenth | identical | ✓ |
| 10 | Renovation spend since 2018: Goodnight $48.8 M vs $211 / $317 / $266 M; ≈ $1.0 M per hotel vs $6–8 M; no Goodnight renovation started after 2020; sisters started four in 2022–23 | $48.8 M (18 jobs) vs Maison d'Or $211.1 M, P&K $317.0 M, Pebble & Pine $265.9 M; $0.98 M per hotel vs $7.0 / $7.9 / $5.9 M; last Goodnight start December 2020; sisters 2022: 3, 2023: 1 | ✓ — new finding, adopted |
| 11 | Event study, 11 sister renovations completed 2021–23: comfort +0.9, room-condition complaints −50 % (range 28–77 %) | Stricter window (6 months before *start* vs 6 months after *end*, ≥ 3 months each side) leaves 4 cases (Paris, London, Chicago Loop, Myrtle Beach): comfort +0.98, NPS +21, room-condition complaints −38 % (−26 … −55 %) | ✓ direction; magnitude depends on the window (see method note) |
| 12 | OTA = 50.0 % of room revenue; commission $18.1 M; all channels $22.7 M; margin after distribution ≈ 34 % | 50.0 % · $18.06 M · $22.65 M · 33.7 % | ✓ (conditional on the Contents-sheet statement, see below) |
| 13 | GI-01 app = $2.35 M/yr ≈ 13 % of the OTA commission; revenue effect only $0.6 M, the rest is cost | identical | ✓ |
| 14 | Airport hotels fullest (82.0 %): Toronto 91.9, Gatwick 90.4, Montréal 90.2; seven hotels above 85 %; Kingston lowest at 61.2 %; GI-06 Low case 5 % occupancy and a negative profit effect | identical | ✓ |
| 15 | App + kiosks + energy + Gatwick + Boston + breakfast + RMS = exactly $60.0 M | $60.0 M | ✓ — a built-in "everything except the refresh" route; adopted as the trade-off foil |
| 16 | NPV through 2032, constant 2025 dollars: refresh −21.9, Boston −16.9, energy −9.7, Gatwick −3.1, Toronto −3.3, Kingston −3.6, app +3.1, breakfast −1.1, RMS +0.5, kiosks −0.4 | With the review's disruption convention (lost revenue × 45 % margin): −22.7, −17.5, −10.0, −3.2, −3.4, −3.7, +3.3, −1.0, +0.5, −0.4. With the mission's (full revenue loss): refresh −26.0, energy −11.6, rest unchanged | ✓ within $0.8 M; ranking identical under both |
| 17 | 456 of 1,024 combinations are feasible (budget, ≥ 3 projects, ≥ 1 growth, kiosks only with app); best NPV package app + kiosks + RMS, $9.4 M, +3.2 constant / +4.0 nominal | 456 exactly; +3.4 M (Expected) | ✓ |
| 18 | Advice package GI-07 + 01 + 02 + 10 + 09 + 04 + 05 = $55.6 M, cumulative ≈ −$26 M constant through 2032 | = mission plan A + GI-09; $55.55 M; cumulative −$25.6 M | ✓ identical plan |
| 19 | Deadline 18 Nov 2026 23:59 PT = 19 Nov 08:59 NL time | Confirmed from the Official Rules received 5 Nov (§3: Round 1 ends 11:59 p.m. PT on November 18, 2026) | ✓ |

## What the review adds (adopted into the mission)

1. **The margin is booked before commissions.** The review reads the workbook's
   Contents sheet as stating that performance costs *exclude distribution costs*. If
   so, the honest margin pair is 44.4 % / **33.7 % after commissions** ($71.8 M), and
   the sister ranking flips: P&K Select 34.7 %, Goodnight 33.7 %, Maison d'Or 32.9 %,
   Pebble & Pine 28.2 %. "Best margin in the group" is partly an artefact of where the
   commission is booked. After commissions, the slide since 2023 is 2.8 points, not
   1.7. This resolves the mission's open trap (DistributionCost vs OtherOperatingCost)
   in the direction of *not inside* — confirm the sheet wording before it ships.
2. **Room comfort is the welcome KPI.** r = −0.92 with years since refresh (NPS −0.78).
   Room condition is the only complaint category still accelerating (+9 % in 2025);
   check-in has plateaued. Framing: the kiosks answer a complaint that stopped growing,
   the refresh answers the one that is growing.
3. **The group starved the brand.** $0.98 M of renovation per hotel since 2018 against
   $5.9–7.9 M at the sisters, and nothing started since December 2020. The refresh is
   catch-up, not pampering, and the cause of the fading welcome sits in the Board's own
   capital history. This is the strongest "why" in the dataset.
4. **Sister renovations prove the mechanism.** Comfort +0.9 to +1.0, room-condition
   complaints −38 to −50 %, NPS +21 at the four to eleven renovations completed inside
   the window. The organisers' GI-07 satisfaction effect (+0.6) is conservative.
5. **Value for money is the lowest in the group** at a brand whose promise is value;
   the ADR rose 15 % in four years, less than two sisters but on a falling score.
6. **The $60.0 M foil.** The dataset carries a route that spends the budget to the
   dollar without touching a room. Show it, name it, reject it.
7. **Two valuation conventions, one ranking.** Constant 2025 dollars (the dataset's
   rule) beside a nominal variant with FinanceAssumptions; the order of projects does
   not change. Adopt as the method overlay's honesty line.

## Where the review needs correction

1. **Five pages.** The starter's Read Me requires *exactly two visible report pages*
   (hidden tooltip pages allowed). The review's sequence survives intact: its P1–P3
   (paradox, cause, which hotels) is the Brand Review page; its P4–P5 (the money, the
   plan) is the Investment Strategy page. That is direction D1's layout.
2. **Four criteria.** The review follows the Official Rules (§8), which name four; the
   starter file's Judging Criteria page adds a fifth, *Analytical Quality*, the one that
   rewards the review's own rigour. Design for all five.
3. **"17 tables."** The workbook has a Contents sheet; the starter loads 16 tables.
   Contents is documentation, not data to pull, so reading it is within the rules.
4. **Event-study window.** "Six months before the *end* date" overlaps the works
   period, when scores are depressed, so it overstates the lift. Measured before the
   *start* date the lift is still large (+0.98 comfort, −38 % complaints) on the four
   cases the data allows. The 2021 completions (including Goodnight's own seven) have
   no pre-period in the data; Goodnight's renovation effect can only be read
   cross-sectionally (the 2021 cohort holding NPS +6…+9 while peers slid +8.9 → +2.7).
5. **"45 of 50."** 45 of 48; two hotels have no 2021 survey data.
6. **Disruption convention.** The review values rooms out of service at lost revenue ×
   45 % margin; the mission at full revenue. The stage-2 contract decides (lost revenue
   less variable cost relief sits between); GI-07 moves from −22.7 to −26.0 M across
   that range and the plan does not change.

## Enhanced conclusions

The story after the cross-check, in one paragraph: Goodnight Inn looks like the
group's best business and is quietly its most neglected. Occupancy is pinned at 79 %,
the margin everyone quotes (44.4 %) is 33.7 % once commissions are counted, and it has
slid every year since 2023 at all 50 hotels. Half of room revenue now books through
OTAs at 18 %; at the 2021 mix the brand would keep $4.8 M more a year. Guests notice:
value for money is the lowest in the group, room comfort tracks years since a refresh
almost perfectly (r = −0.92), room-condition complaints are the only category still
accelerating, and NPS has fallen at 45 of 48 hotels. The cause is on the Board's own
books: $0.98 M of renovation per hotel since 2018 against $6–8 M at the sister brands,
and nothing started since 2020. Meanwhile the airport hotels are full. The plan buys
the guest back, catches up on the rooms, and builds where the brand is full; it also
shows the $60.0 M route that spends everything without touching a room, and says why
not.

Page-1 consequences: the KPI band carries both margins (sister flip in the tooltip);
the welcome block uses room comfort vs years since refresh with the renovation-spend
bar ($1.0 M vs $6–8 M per hotel) as the "why"; the complaints chart highlights room
condition as the one still rising. Page-2 consequences: the refresh is framed as
catch-up, evidenced by the sister event study; the $60.0 M foil sits in "Not funded,
and why"; the method overlay states both valuation conventions and the disruption
convention.

## Decisions for Björn

| Decision | Default if deferred |
|---|---|
| Confirm the Contents-sheet wording ("excludes distribution costs") in the workbook | Both margins shown with the assumption labelled |
| Deadline time — confirmed 5 Nov from the Official Rules (11:59 p.m. PT, 18 Nov) | Submit by 17 Nov evening CET regardless |
| GI-09 breakfast in the plan ($55.6 M) or $8.7 M held as reserve ($51.3 M) | Reserve; breakfast as the Board's optional add |
| Disruption convention (full revenue / 45 % margin / revenue less variable relief) | Full revenue (conservative) with the sensitivity stated |
| Direction (unchanged by this review; its sketch is D1) | Stage 5 re-runs divergence |
