# MISSION — "Wake-up call"
### Power BI Dataviz World Champs 2027 · Round 1 "The Investment Challenge" · Goodnight Inn · build brief for pbi-atelier

This file is the **stage-0 source of truth** for a contest build. Drop it into
`project/` of a fresh pbi-atelier project copy and reference it from the kickoff
prompt (bottom of this file). It seeds every lifecycle stage so the agents spend
their effort building, not rediscovering.

**Read me under pbi-atelier's invariants.** Everything below labeled *evidence*
was derived from the organisers' starter model (`PillowKey_Starter.pbix`, 16
tables, decoded offline) by prior analysis and is trustworthy as direction. Per
the *do-not-fabricate* and *research-first* rules, every number that lands in a
visual must be **re-derived from the model** at stage 4/6 and recorded in the
evidence manifest. Treat my figures as hypotheses with high prior, not as
citable facts. The companion `SCOUT-pillowkey-round1.md` holds the four-brand
comparison and the dataset mechanics; this file holds the build.

---

## 0 · Project initialization

```
python scripts/init_project.py --name <repo-name> --client-alias fabric-contest \
  --language en \
  --modules brand-kit-studio,nav-studio,tooltip-studio,a11y-studio,table-studio,icon-studio,canvas-studio,px-prototype,deneb-studio,custom-visual-studio \
  --brand-kit none
```

- `px-prototype` is on: the proven HTML-comp → verbatim-rect PBIR pipeline from
  the previous World Champs build (see `.claude/skills/px-prototype/references/gotchas.md`
  before the first page).
- `deneb-studio` and `custom-visual-studio` are both enabled, but **gated** by
  §6 (the "works online" rule). Nothing non-native ships without the gate.
- Brand kit: none at init; stage 5 creates `design/brand-kits/goodnight-inn/`
  with brand-kit-studio (§5).
- Data: the starter's `DataFile` parameter points at the organisers' public
  blob (`https://datavizcontests.blob.core.windows.net/worldchamps-atl27/PillowKey_Dataset.xlsx`).
  Keep it, and keep a local copy under `project/data/` (gitignored) as fallback
  with the parameter switchable. The starter `.pbix` goes in `project/data/`
  too; the PBIP (report + TMDL) is the versioned source of truth, and the
  submission `.pbix` is exported from Desktop at stage 7.
- Credits (attribution.md): add to `CREDITS.md` at init — dataset and starter
  file: Microsoft Fabric Community, Power BI Dataviz World Champs 2027 Round 1
  (post by slindsay); Contest Advisory Committee: Karin Szilágyi, Aanor Le
  Gouic, Taylor Amy, Santhana Lakshmi Ponnurasan, Paulo Grijo.
- After init: `/next` as usual. Do not skip gates; the deadline (§1) is 14 days
  out and the gates are what make this entry championship-grade.

## 1 · Contest constraints (hard requirements — blocker-severity)

Sources: blog post "Power BI Dataviz World Champs 2027 | Round 1"
(community.fabric.microsoft.com, article 5390883) and the starter file's hidden
*Read Me* and *Judging Criteria* pages, and the Official Rules (ATL 2027, filed
as `contest/official-rules-ATL-2027.pdf`, digest in
`contest/official-rules-digest.md`). Deadline: **November 18, 2026, 11:59 p.m.
Pacific = November 19, 08:59 CET** (Official Rules §3, confirmed). Round 2 runs
November 25 – December 9, 2026; the live finale is at FabCon Atlanta, March
8–12, 2027, open to Round 1–2 winners only (two per round). Brief prepared
November 4; cross-checked against the Dutch review on November 5 (see
`research/2026-11-05-crosscheck-dutch-review.md`).

1. **One brand only: Goodnight Inn.** Name it visibly on both pages and in the
   gallery description.
2. **Exactly two visible report pages** (starter Read Me). Hidden tooltip pages
   are allowed. Delete the starter's own hidden pages (Read Me, Judging
   Criteria, Overview) and note it in the BUILD_LOG. No hidden "method" page:
   methodology lives in tooltips and an in-page bookmark overlay.
3. **Page 1 = The Brand Review** ("where does the brand stand today?"),
   **Page 2 = The Investment Strategy** ("where should the money go, and why?").
4. The proposal must: recommend **≥ 3 initiatives**; include **≥ 1 with
   `GrowthInitiative = Yes`**; **stay within $60,000,000** (`Brands[InvestmentBudgetUSD]`);
   show the allocation with estimated costs and expected returns; show
   financial **and operational** impact through **December 2032**; explain
   choices, risks and trade-offs; tie each initiative to a Page 1 finding.
5. **≥ 4 core (built-in) visuals.** Custom visuals, images, icons, themes and
   AI design tools are allowed — subject to §6's online gate.
6. **Provided data only.** Allowed: measures, calculated tables, scenario
   (what-if) parameters, calculated columns, reshaped tables, helper/derived
   tables, field parameters. Forbidden: changing values, pulling extra sheets
   from the workbook, external data, fabricated or simulated data. Scenario
   logic is allowed when it is derived from the provided assumptions and
   **labeled as such**.
7. **Accessibility is a judging criterion**: alt text on every visual, logical
   tab order, WCAG-AA contrast. `ax-audit` is a named stage-7 gate item;
   `scripts/check_contrast.py` on the theme.
8. **Must work online.** The user's requirement: the entry is submitted as a
   `.pbix` *and* viewed through a Publish-to-Web link in the Contests Gallery.
   Therefore: built-in fonts only (Power BI's own font list; no custom fonts,
   they fall back on the viewer's machine), all images embedded as registered
   resources (no external URLs), no R/Python visuals, no live connection, and
   a Publish-to-Web rendering test in an incognito browser at 1920×1080 and on
   a 1366-wide laptop before submission (§7).
9. Judging criteria. The Official Rules (§8) name four: **Insightfulness**,
   **Visual Effectiveness**, **Creativity and Innovation**, **Accessibility**;
   the starter file's Judging Criteria page adds **Analytical Quality**
   (accuracy, appropriate methods, correct interpretation, well-supported
   conclusions) and the judges' note *"thoughtful analysis, not just beautiful
   dashboards … support their recommendations with evidence."* Design for all
   five: the rules' four are what a tie-break is scored on, and Analytical
   Quality is what makes the other four defensible.
10. Submission: Fabric Community Contests Gallery (aka.ms/contestsgallery) —
    report image, short description naming Goodnight Inn, `.pbix` and/or
    Publish-to-Web link, the official contest tag (not in the post or the
    rules; take it from the gallery). **One entry per round**, three across the
    contest; entries do not carry over between rounds. Two Round-1 winners
    advance to the live finale (prize: conference admission plus three hotel
    nights; airfare is the winner's own; virtual presentation permitted).
11. Rules that shape the build (Official Rules §4, §6, §7): entrant 18+ and
    **not a government or public-sector employee**; the entry must be
    **original work** with all licences obtained, and Microsoft receives a
    royalty-free licence to reuse and publish it — so every font, image and
    icon must be ours or built-in (already required by item 8); Microsoft
    trademarks may be used under a limited licence; no content that is
    offensive, political, or **promotes alcohol or tobacco** (the plan has
    none; keep bar imagery out of the chrome). "Use of any automated system to
    participate is prohibited" concerns entry mechanics; the starter file
    explicitly allows AI-assisted design tools.

## 2 · The story (stage 0/1 seed)

**Concept: "Wake-up call."** Goodnight Inn looks like the group's most profitable
brand per dollar of revenue — 44.4 % before commissions, 33.7 % after, where P&K
Select actually leads — and it has quietly stopped growing: occupancy is pinned
at 79 %, revenue rose 0.8 % last year while cost per occupied room rose 3.5 %,
and operating profit fell for the first time. Two things explain it. Half of
every room dollar now arrives through online travel agencies at an 18 %
commission (a third did in 2021), so the brand pays $22.7 M a year to be
booked — $4.8 M more than at its 2021 channel mix. And the welcome is fading:
NPS has slid from +8.5 to +3.3, room comfort tracks years since a refresh almost
perfectly (r = −0.92), and the ten hotels that have gone longest without one are
the ones guests no longer recommend. The cause sits in the Board's own books:
$0.98 M of renovation per hotel since 2018 against $6–8 M at the sister brands,
and nothing started since 2020. Meanwhile the airport hotels are full. The plan buys the guest back (app, revenue management,
kiosks), fixes the welcome (refresh the ten oldest), and builds where the brand
is full (Gatwick, Toronto) — $51.3 M of the $60 M, +$7.6 M a year of operating
profit by 2032 — and says no, with numbers, to a new hotel in Boston, an
extension in Kingston, and an energy programme that pays back after the horizon.

**Audience & decision (stage 1 framing):** the fictional audience is the Board
of Pillow & Key Group deciding Goodnight Inn's 2027–2031 capital plan; the real
audience is the judging panel scoring five criteria. Every requirement traces
to a criterion: the channel-mix counterfactual and the renovation-age cohort →
Analytical Quality; the plateau/middleman/welcome diagnosis → Insightfulness;
the plan builder and the rejected-with-reasons strip → Creativity; the folio
and departures-board motifs → Visual Effectiveness; alt-text/tab-order/contrast
discipline → Accessibility.

### Evidence pack (verify all at stage 4; grain noted per item)

| # | Claim (hypothesis) | Value found in prior analysis | Grain / method |
|---|---|---|---|
| E1 | Portfolio | 50 hotels, 6,485 rooms (avg 130): 17 airport, 22 highway, 11 city; 25 North America, 20 Europe, 5 Asia-Pacific | Hotels |
| E2 | 2025 P&L | Revenue $212.8 M (room revenue 94 %), GOP $94.4 M, **GOP margin 44.4 % before commissions** (46.1 % in 2023, 45.8 % in 2024) and **33.7 % after distribution cost** ($71.8 M; 36.5 % in 2023). After commissions P&K Select leads (34.7 %; Maison d'Or 32.9, Pebble & Pine 28.2): "best margin in the group" is partly where the commission is booked | MonthlyPerformance, brand sums; opex excludes distribution cost per the workbook's Contents sheet (confirm wording) |
| E3 | The plateau | Occupancy 78.3 / 79.3 / 79.4 % (2023–25); revenue +0.8 % in 2025; **GOP −$2.2 M (−2.3 %)**, the first decline in the window | brand sums by year |
| E4 | The scissors | Revenue per occupied room +0.9 % in 2025, cost per occupied room (CPOR) +3.5 % ($60.9 → $63.0); staff cost 26.9 % → 28.3 % of revenue since 2023 | TotalRevenue / TotalOpex ÷ RoomsSold |
| E5 | The middleman | OTA share of room revenue **33.0 % (2021) → 50.0 % (2025)**, identical across hotels (49–51 %); direct web/app 31.4 % → 23.0 %, and direct web room nights fell 14 % from their 2022 peak while OTA nights rose 89 % since 2021 | BookingChannels, brand sums |
| E6 | What it costs | Distribution cost $12.6 M → **$22.65 M (11.3 % of room revenue**; other brands 7.5–8.0 %); OTA commission is 80 % of it ($18.1 M). Channel costs: OTA 18 %, TA/TO 10 %, corporate 5 %, direct web 4 %, phone 1.5 % | DistributionCost ÷ RoomRevenue |
| E7 | Counterfactual | At the 2021 channel mix, 2025 distribution cost would be $17.8 M: the mix shift costs **$4.8 M/yr**; each 1 pt of room revenue moved OTA → direct web saves $0.28 M/yr | 2021 shares × 2025 channel cost rates × 2025 room revenue |
| E8 | No OTA premium | ADR by channel 2025: OTA $109.3, direct web $111.6, phone $109.4 — OTA guests pay the same, net $89.6 vs $107.1 per night after commission | RoomRevenue ÷ RoomNights by channel |
| E9 | The fading welcome | NPS **+8.5 → +3.3** (response-weighted); room comfort 7.43 → 7.17 (largest score drop); complaints per 1k room nights 9.4 → 9.9: **room condition 1.54 → 1.80 (+17 %, and the only category still accelerating: +9 % in 2025)**, check-in & waiting 0.88 → 1.10 (+25 % over the window, flat in 2025); NPS fell at 45 of the 48 hotels with 2021 data, margin fell at all 50 in 2025 | GuestExperience weighted by SurveyResponses; GuestComplaints ÷ RoomsSold |
| E10 | Age explains it | NPS 2025 by years since last renovation: ≤5 y +6.8 (14 hotels), 6–9 y +4.0 (20), 10–15 y **−4.6** (10); r = −0.78 with NPS and **r = −0.92 with room comfort** (44 dated hotels; −0.92 over all 50 with the opening-date fallback). Occupancy (79–80 %) and GOP margin (44 %) are identical across buckets, and per-hotel NPS change vs occupancy change correlates at −0.04: age hurts loyalty, not (yet) money | Hotels.LastRenovationDate; 6 hotels never renovated — use OpeningDate as product age |
| E11 | 2021 cohort | Seven hotels fully renovated in 2021 ($2.1–3.5 M each) held NPS at +6 to +9 through 2025 while the other 43 slid from +8.9 to +2.7; their RevPAR grew +39 % vs peers +36 % 2021→25 (no large revenue premium) | Renovations ⋈ MonthlyPerformance ⋈ GuestExperience |
| E12 | The ten oldest | GI-07's ten hotels (Dallas DFW, Lyon, Schiphol, Chicago Midway, Richmond, Sydney, Madrid Barajas, Bologna, Kingston, Ottawa; 1,180 rooms, 11–14 y since works) include **8 of the 12 hotels with negative NPS**; $29.5 M = $2.95 M/hotel, in line with the 2021 cohort's cost | InvestmentProjectProperties ⋈ Hotels |
| E13 | Where we're full | Airport hotels: 82 % occupancy, ADR $116, RevPAR $95 (highway 77.5 % / $82, city 79 % / $76). **Gatwick 90.4 %** (≥90 % in 14 of the last 24 months, RevPAR $145, highest in brand), **Toronto 91.9 %** (17 of 24 months ≥90 %), Montréal 90 %. **Kingston 61 %**, never above 74 % | MonthlyPerformance by hotel/month |
| E14 | Seasonality | Mild: brand 68.5 % (Jan) → 89.8 % (Jul); airport hotels flat 78–91 %; highway dips to 68–71 % in H2 | 2025 by location type × month |
| E15 | Mix | Business travel 20 % → 24 % of room nights (growing), leisure 40 % → 38 %, family 24 % → 23 %; leisure pays the highest ADR ($113.6) | GuestSegments |
| E16 | Benchmarks | GI distribution cost 11.3 % vs Maison d'Or 8.0 %, P&K 7.5 %, Pebble & Pine 10.2 %; GI GOP margin 44.4 % vs 38.0 / 40.0 / 35.1 % before commissions, 33.7 % vs 32.9 / 34.7 / 28.2 % after | brand sums (sister-brand comparison is provided data, allowed) |
| E17 | The group starved the brand | Renovation spend started 2018–2025: Goodnight **$48.8 M over 18 jobs = $0.98 M per hotel** vs Maison d'Or $211 M ($7.0 M/hotel), P&K $317 M ($7.9 M), Pebble & Pine $266 M ($5.9 M). Goodnight started 4 / 7 / 7 renovations in 2018–20 and **none since December 2020**; the sisters started four more in 2022–23 | Renovations ⋈ Hotels, by StartDate |
| E18 | Sister renovations prove the mechanism | Four renovations completed inside the window (Paris 2022, London 2023, Chicago Loop 2023, Myrtle Beach 2023), measured 6 months before start vs 6 months after end: **room comfort +0.98**, NPS +21, room-condition complaints −38 % (−26 … −55 %). The organisers' GI-07 satisfaction effect (+0.6) is conservative | GuestExperience + GuestComplaints around Renovations.StartDate/EndDate; the 2021 completions have no pre-period in the data |
| E19 | The promise | Value for money 7.66, **lowest of the four brands** (P&K 7.72, Pebble & Pine 7.94, Maison d'Or 8.04) at the brand whose positioning is "affordable"; ADR +14.6 % since 2021 (Pebble & Pine +13.3, Maison d'Or +20.2, P&K +23.7) on a falling score | GuestExperience weighted; ADR = RoomRevenue ÷ RoomsSold |
| E20 | The $60.0 M foil | App + kiosks + energy + Gatwick + Boston + breakfast + RMS costs **exactly $60.0 M**: the dataset carries a route that spends the budget to the dollar without touching a room. Show it, name it, reject it | InvestmentProjects capex sums |

Anything not derivable from the tables (market share, competitor rates, app
adoption, marketing spend, financing, tax, depreciation, terminal value beyond
2032) goes on the **metrics-NOT-available list**. Real-world hospitality
context may appear as *narrative text*, clearly separated from data claims.

### The projects (organisers' data, Expected scenario; Low/High exist for each)

| ID | Project | Capex | Growth | Months | Rooms OOS | Annual OP impact (Exp / Low / High) | Note |
|---|---|---|---|---|---|---|---|
| GI-01 | Direct booking app & member rates | $5.0 M | Yes | 9 | 0 % | **$2.35 M** / 0.60 / 4.10 | distribution cost −1.2 pts, ADR +0.3 %; running cost $0.6 M/yr; prerequisite for GI-02 |
| GI-10 | Revenue management system | $2.4 M | Yes | 6 | 0 % | $0.77 M / 0.23 / 1.48 | ADR +0.6 %; running cost $0.3 M/yr |
| GI-02 | Self check-in kiosks, 20 busiest hotels | $2.0 M | No | 6 | 0 % | $0.41 M / 0.21 / 0.62 | opex −0.8 %, satisfaction +0.25; **depends on GI-01** |
| GI-05 | 40-room extension, London Gatwick | $6.6 M | Yes | 16 | 3 % | $1.04 M / 0.88 / 1.11 | added-room occupancy 85 % |
| GI-04 | 40-room extension, Toronto Pearson | $5.8 M | Yes | 16 | 3 % | $0.67 M / 0.58 / 0.72 | added-room occupancy 86 % |
| GI-07 | Room refresh, 10 oldest hotels | $29.5 M | No | 14 | **15 %** | $2.34 M / 1.32 / 3.38 | occupancy +2 pts, ADR +5 %, satisfaction +0.6 |
| GI-09 | Breakfast & grab-and-go upgrade | $4.25 M | Yes | 8 | 0 % | $0.84 M / 0.42 / 1.12 | F&B revenue +30 % (F&B is 3.8 % of revenue) |
| GI-03 | Energy efficiency programme | $15.0 M | No | 18 | 1 % | $1.78 M / 1.18 / 2.37 | opex −1.5 %; energy already fell from 5.9 % to 4.9 % of revenue; 8.5-year simple payback |
| GI-06 | 40-room extension, Kingston | $5.4 M | Yes | 16 | 3 % | $0.44 M / **−0.14** / 0.48 | hotel at 61 % occupancy; Low case loses money |
| GI-08 | New hotel, Boston Logan Airport | $24.75 M | Yes | 26 | — | $2.00 M / 1.63 / 2.23 | 41 % of the budget, opens Mar 2029, 12-year payback |

Reconciliation already done (see SCOUT §2): revenue impacts reproduce from the
driver columns × the mapped hotels' 2025 actuals; **the OP impacts net the
annual running cost** (GI-01 and GI-10 reconcile only if they do) — confirm in
the metric contract.

### Recommended plan (hypothesis "A"; stages 2–3 re-derive, stage 5 may re-cut)

| Move | Projects | Capex | Answers Page 1 finding |
|---|---|---|---|
| **Buy the guest back** | GI-01 app, GI-10 RMS, GI-02 kiosks | $9.4 M | E5–E8 (middleman), E9 (check-in complaints) |
| **Fix the welcome** | GI-07 refresh of the ten oldest | $29.5 M | E9–E12 (fading welcome, age), E17–E19 (under-investment, proven mechanism, the promise) |
| **Build where we're full** | GI-05 Gatwick, GI-04 Toronto | $12.4 M | E13 (airport hotels at 90 %+) |
| Total | 6 projects, 4 growth initiatives | **$51.3 M of $60 M** (86 %) | $8.7 M held as contingency on the refresh (≈ 30 % of its capex), or GI-09 breakfast ($4.25 M) if the Board prefers to deploy it |

Through-2032 economics of plan A in my simplified model (2025 dollars, earliest
starts, organisers' ramp-up 50/85/100 %, capex phased evenly, rooms out of
service = full revenue loss, 8 % discount to 2026, no terminal value):
**2032 run-rate +$7.6 M/yr OP** (Low $3.8 M, High $11.4 M) = +8 % on 2025 GOP;
benefits inside the horizon $33.2 M against $51.3 M capex and $7.2 M disruption;
NPV through 2032 −$29.5 M. **This is the horizon trap** (SCOUT §2): every capital
project in the dataset is cumulative-negative by 2032 because the ramp finishes
in 2030; the honest presentation shows the run-rate, the cumulative curve, and
the payback year per initiative (app 2030, RMS 2031, refresh ≈ 2040 on Expected)
and says so. Explicit alternatives to show on Page 2, not hide: plan "B" swaps
the refresh for the energy programme (better in-horizon cash, −$10.6 M net, but
leaves the satisfaction decline untouched: *rooms vs kilowatts*); plan "D"
funds Boston instead of the refresh and extensions (the budget-eater).

## 3 · Model blueprint seed (stage 2/3)

Grain declarations first, per the star-schema rule. The starter model is a
usable star (17 single-direction M:1 relationships, no measures, no
bidirectional filters); extend, don't rebuild. Keep **all four brands** in the
model: sister-brand benchmarks (E16) are provided data and strengthen the
review; the report pages filter `Brands[Brand] = "Goodnight Inn"` and the
benchmark measures lift the filter with `ALL(Brands)`.

- **MonthlyPerformance** — grain: one row per (hotel, month), 2021-01…2025-12.
  Revenue and opex components sum exactly to totals (verified).
- **BookingChannels** — one row per (hotel, month, channel); room revenue and
  room nights reconcile exactly to MonthlyPerformance (verified).
- **GuestSegments** — one row per (hotel, month, segment).
- **GuestExperience** — one row per (hotel, month): scores are *averages*;
  every brand-level score **must be weighted by SurveyResponses**. An unweighted
  AVERAGE is a contract violation.
- **GuestComplaints** — one row per (hotel, month, category). Normalise per
  1,000 room nights (join to MonthlyPerformance.RoomsSold at hotel-month).
- **Renovations** — one row per renovation (201, 1985–2023). Used for E10/E11
  only.
- **Hotels / Brands / Region / Date** — dimensions as shipped. Mark `Date` as
  the date table (daily, 2021–2032, `Period` column distinguishes Historical /
  Planning year / Investment horizon). Add to Hotels: `YearsSinceRenovation`
  (2025 − year of LastRenovationDate, falling back to OpeningDate), the
  renovation-age bucket, `IsRefreshCandidate`, and `OccupancyBand2025` if the
  design wants it — Power Query or calculated columns, both allowed.
- **InvestmentProjects / InvestmentScenarios / InvestmentProjectProperties /
  FinanceParameters / FinanceAssumptions / Scenario** — as shipped. Add to
  InvestmentProjects a calculated column `InRecommendedPlan` (Yes/No) and a
  `Move` column (Buy the guest back / Fix the welcome / Build where we're full
  / Not funded) so Page 2 can show *our plan* next to *your plan*. Relate
  `Scenario[Scenario]` to `InvestmentScenarios[Scenario]` (it ships
  disconnected) or use TREATAS in the measures — decide at stage 3.
- **New: `ProjectCashflow`** — calculated table, grain: one row per (project,
  scenario, month 2027-01…2032-12) with `Capex` (evenly phased over
  `DurationMonths` from the start month), `Disruption` (RoomsOutOfServicePct ×
  the mapped hotels' 2025 monthly revenue for the works months; brand-wide
  projects map to all 50 hotels), `Benefit` (AnnualOperatingProfitImpactUSD ÷ 12
  × ramp: 50 % months 1–12 after completion, 85 % 13–24, 100 % from 25),
  `Net`, `Year`. Built from FinanceParameters so the rules are *read*, not
  typed. Start month = `EarliestStart` (every month of delay costs in-horizon
  impact; say so). A "delay by N months" what-if parameter is an optional
  flourish only if the measures stay simple — decide at stage 3, default no.
  Relationships: ProjectCashflow → InvestmentProjects (M:1), → Date (on month
  start). The plan-builder slicer on `InvestmentProjects` then filters it
  through the relationship.
- Single-direction only; any dimension-through-fact count uses `CROSSFILTER`
  inside a measure.

Metric contracts to write at stage 2 (one YAML each; names final at G2):
`Occupancy`, `ADR`, `RevPAR`, `Total Revenue`, `GOP`, `GOP Margin %`, `GOP after
Distribution`, `GOP Margin after Distribution %`, `Room Comfort (weighted)`,
`Renovation Spend per Hotel`, `CPOR`,
`Revenue per Occupied Room`, `Distribution Cost`, `Distribution Cost % of Room
Revenue`, `OTA Share %`, `Direct Share %`, `Distribution Cost at 2021 Mix`
(counterfactual, labeled), `NPS (weighted)`, `Overall Score (weighted)`,
`Complaints per 1k Room Nights`, `Years Since Renovation`, `Budget`, `Capex
Selected`, `Budget Used %`, `Growth Initiatives Selected`, `Plan Valid` (≥3
projects, ≥1 growth, ≤ budget, dependencies met), `Annual Impact (ramped)`,
`Cumulative Net Impact through 2032`, `2032 Run-rate`, `NPV @ 8 %`, `Payback
Year`, `Rooms Added`, `Rooms Refreshed`, `Disruption Months`. Edge cases to
write down: 2021 is a depressed base year (trend claims use 2023→2025 or
2022→2025, never 2021); late openers (Valencia 2023, Porto 2022) excluded from
like-for-like growth; six never-renovated hotels; `DistributionCost` sits
**outside** MonthlyPerformance opex (the workbook's Contents sheet states that
costs exclude distribution costs, per the Dutch review — confirm the wording
once, then show both margins and never double-count); Low/High portfolio = sum of each
project's Low/High (no mixing); disruption applies to total revenue with no
cost relief (conservative) unless the contract argues otherwise.

## 4 · Design contract seed (stage 5)

Stage 5 must still run properly — three divergent directions, critique,
convergence — but the user has pre-chosen the *story* and the page map below
is contractual. Divergence explores **mood/metaphor/layout**, not alternative
stories. Suggested directions: *"Night desk"* (navy + lamp amber, motel-sign
typography, dark surface — contrast risk, highest drama), *"The folio"*
(paper white, guest-bill ledger, tabular numerals — the distribution story as
a receipt), *"Departures"* (airport board, black + amber flap tiles — 17 of 50
hotels are airport hotels and the plan's timeline reads like a board).

**Theme direction:** brand-kit-studio builds `goodnight-inn` from scratch (the
dataset carries no brand assets, and Goodnight Inn is fictional — no trademark
risk). Palette: one accent only (consistency lock), good/bad pair never the
only carrier of meaning, WCAG-AA checked with `check_contrast.py` in every
state including overlays. **Fonts: Power BI built-ins only** (Segoe UI family,
DIN, Consolas for tabular figures) — a custom font is a Publish-to-Web
failure, not a style choice. Images: embedded registered resources only.

Page map (exactly 2 visible pages + hidden tooltip pages):

**P1 · Brand Review — "Wake-up call."**
3-second message: *full, flat, and paying the middleman — the group's best
margin is slipping.* Grid: KPI band (occupancy 79 %, RevPAR $85, GOP margin
44.4 % before and 33.7 % after commissions with the two-year slide, NPS +3.3
with the four-year slide; each with sister-brand benchmark in the tooltip —
after commissions P&K Select leads). Three story blocks, left to right:
**The plateau** (revenue-per-occupied-room vs cost-per-occupied-room index
2023–2025, GOP bridge 2024 → 2025); **The middleman** (channel share of room
revenue 2021–2025 as stacked area or bump, distribution-cost line in $, the
"$4.8 M at the 2021 mix" callout, and the *folio* visual: what a $109 room
night nets us by channel); **The fading welcome** (room comfort vs years
since refresh as a dot strip of 50 hotels, r = −0.92; the renovation-spend bar,
$1.0 M vs $6–8 M per hotel since 2018, as the why; complaint categories trend
with room condition highlighted as the one still rising). Bottom strip: **Where we're full** — airport
/ highway / city occupancy and the Gatwick/Toronto/Kingston monthly occupancy
sparklines. Title names the brand; subtitle names the Board.

**P2 · Investment Strategy — "The morning plan."**
3-second message: *$51 M of $60 M on three moves; +$7.6 M a year by 2032; no to
Boston, Kingston and kilowatts.* Grid: left, the **plan builder** — a button
slicer (nav-studio) listing the ten projects grouped by move, pre-selected to
the recommended plan via a bookmark ("Reset to our plan"), with a budget bar
($ used of $60 M, turns bad-colour over budget), a growth-initiative counter,
and constraint lamps (dependency GI-02 ← GI-01; ≥ 3 projects; ≥ 1 growth).
Centre, the **impact panel** driven by the selection and a Low/Expected/High
scenario toggle: 2032 run-rate, cumulative net curve 2027–2032 with the
Low–High band, NPV @ 8 %, payback year per initiative, rooms added / rooms
refreshed / direct-share target as operational impact. Right, the
**departures board**: initiatives × (gate = hotels, departs = start, arrives
= completion, disruption months, status Funded / Not funded / Needs GI-01)
styled per the chosen direction, native matrix first (§6). Bottom: **Not
funded, and why** (Boston, Kingston, Energy with one number each, and the
$60.0 M route that funds everything except the refresh, named and rejected) and the
**Risks & trade-offs** panel (rooms vs kilowatts; refresh disruption 15 % of
1,180 rooms for 14 months; app adoption is the Low/High swing; horizon
honesty). A bookmark overlay "How we calculated this" carries the
FinanceParameters rules, the counterfactual method, both valuation conventions
(constant 2025 dollars per the dataset, nominal with FinanceAssumptions — same
ranking) and the disruption convention (keeps the page count at two).

Every page: page-purpose contract with its 3-second message and 3-minute trust
path, alt text for every visual, explicit tab order, brand name visible,
footer "Data: Pillow & Key Group dataset, Power BI Dataviz World Champs 2027".

## 5 · Data prep recipes (stage 4 quick reference)

- Keep the starter's Power Query (Excel.Workbook over `DataFile`); add the
  local-path fallback with a second parameter and a `try … otherwise`.
- Weighted scores: `NPS (weighted) := DIVIDE ( SUMX ( GuestExperience, GuestExperience[NetPromoterScore] * GuestExperience[SurveyResponses] ), SUM ( GuestExperience[SurveyResponses] ) )`.
- Complaint rate: complaints ÷ RoomsSold at hotel-month, ×1,000 — join on
  (HotelID, Month) through the Hotels and Date dimensions, never a lookup
  column.
- Data categories: Hotels.Latitude/Longitude for an optional map; no Image
  URLs (nothing external).
- Key DAX (final form at stage 4 under dax-patterns; sketches):

```dax
Distribution Cost %      := DIVIDE ( SUM ( BookingChannels[DistributionCost] ), SUM ( BookingChannels[RoomRevenue] ) )
Dist Cost at 2021 Mix    := -- counterfactual, labeled scenario logic
    VAR Rev25 = [Room Revenue]
    RETURN SUMX ( VALUES ( BookingChannels[Channel] ),
        CALCULATE ( [Channel Revenue Share], Date[Year] = 2021 ) * [Channel Cost Rate] * Rev25 )
Capex Selected           := SUM ( InvestmentProjects[CapexUSD] )            -- slicer context = the plan
Budget                   := MAX ( Brands[InvestmentBudgetUSD] )
Plan Valid               := [Capex Selected] <= [Budget] && [Projects Selected] >= 3 && [Growth Selected] >= 1 && NOT [Dependency Broken]
Dependency Broken        := VAR s = VALUES ( InvestmentProjects[ProjectID] ) RETURN "GI-02" IN s && NOT "GI-01" IN s
2032 Run-rate            := CALCULATE ( SUM ( ProjectCashflow[Benefit] ), ProjectCashflow[Year] = 2032 )
NPV through 2032         := SUMX ( VALUES ( ProjectCashflow[Year] ), CALCULATE ( SUM ( ProjectCashflow[Net] ) ) / ( 1 + [Discount Rate] ) ^ ( ProjectCashflow[Year] - 2026 ) )
```

`[Discount Rate]` reads `FinanceParameters` (Parameter = "Discount rate"), never
a typed 0.08. The ramp percentages likewise.

## 6 · The showpieces and the "works online" gate

Mandatory, native: the **plan builder** (§4/P2). Slicers, bookmarks, buttons
and conditional formatting all render in Publish-to-Web; this is the
"innovative use of Power BI" a judge can click in the gallery.

Candidates for extra wow, in order of risk, each with a justification gate in
the design handoff:

1. **The folio** (native): a card/table styled as a guest bill — *Room $109.31,
   OTA commission −$19.68, Goodnight Inn keeps $89.63* vs direct — pure
   conditional formatting and layout. Zero risk; do it.
2. **The departures board** (native matrix with monospace figures and dark
   tiles; optionally a Deneb version if the matrix can't carry the look).
3. **Deneb/Vega-Lite** for the channel-mix Sankey or bump chart, only if the
   native stacked area reads worse in critique. Deneb is a certified AppSource
   visual; still subject to the online test.
4. **pbiviz custom visual** (a flip-animated departures board or a
   drag-to-allocate budget bar) only if (a) Microsoft Learn confirms that
   visuals imported from file render under Publish-to-Web — verify at stage 5,
   research-first — and (b) the toolchain (Node ≥ 20, `pbiviz`) runs on the
   user's machine by **November 11**. Otherwise the native board ships.

Hard rule for anything non-native: it must pass the Publish-to-Web test in §7
*and* leave the four-core-visual minimum untouched (the build will have
~15 core visuals regardless). Native fallback is a pre-approved deviation in
the design handoff so a switch does not re-open gate G5.

## 7 · Stage-7 delivery checklist (beyond the standard gate)

- Contest compliance sweep against §1, item by item, in the evidence
  manifest: one brand, named; exactly two visible pages (tooltip pages hidden,
  starter pages deleted); ≥ 4 core visuals (count them); ≥ 3 initiatives and
  ≥ 1 growth initiative in the recommended plan; capex ≤ $60 M shown on page;
  costs and returns per initiative visible; impact through 2032 visible;
  every initiative linked to a Page 1 finding; risks and trade-offs present;
  no external data, no changed values.
- Every number visible in the report traces to a measure + evidence-manifest
  entry (re-derived, not copied from §2).
- **Online test**: publish to the service, create the Publish-to-Web link,
  open it in an incognito window at 1920×1080 and at 1366×768; check fonts,
  images, slicers, bookmarks, tooltips, any Deneb/custom visual, and the
  alt-text reading order with a screen reader. Then open the exported `.pbix`
  on a machine without the dev toolchain.
- `ax-audit` gate: alt text everywhere, tab order set on both pages, contrast
  in every bookmark state and overlay; keyboard-only walk-through of the plan
  builder.
- `copy-polish` sweep: no AI-tells, titles are insights not topics, Board
  register.
- Submission package: `.pbix` + Publish-to-Web link + gallery post (image,
  description naming Goodnight Inn and crediting the organisers' dataset, the
  official tag). Content-complete by **November 15**; online test and
  submission mechanics November 16–17; submit **November 17** evening (CET),
  one day inside the deadline whatever its time zone turns out to be.

### Timeline (14 days)

| Dates | Stages | Gate |
|---|---|---|
| Nov 4–5 | init, intake, requirements, metric contracts | G0–G2 |
| Nov 6–7 | model design, model build, ProjectCashflow, number verification | G3–G4 |
| Nov 8–10 | three directions as HTML comps, critique, design handoff quartet | G5 |
| Nov 11 | custom-visual go/no-go (§6) | — |
| Nov 11–14 | report build (px-prototype), tooltips, plan builder, polish | — |
| Nov 15 | content-complete; fidelity review, ax-audit, copy-polish | G6 |
| Nov 16–17 | online test, business validation, gallery post, submit | G7 |

---

## Kickoff prompt (paste into Claude Code in the project copy)

> Read `project/MISSION-goodnight-inn.md` in full — it is the stage-0 source
> of truth for a Power BI contest build with a hard deadline of November 18
> (submit November 17). Read `project/SCOUT-pillowkey-round1.md` for the
> dataset mechanics. Initialize the project exactly as §0 specifies, then run
> the lifecycle via `/next` stage by stage. The mission file seeds each stage:
> treat its evidence pack and recommended plan as hypotheses to re-verify
> against the data, its page map and plan-builder spec as contractual, and its
> contest constraints — including "must work online" — as blocker-severity.
> At stage 5, run real divergence on mood/metaphor only — the story and page
> map are fixed. Flag anything in the mission that conflicts with a repo rule
> before working around it. First action: confirm the module list and ask me
> for the path to the starter .pbix and the dataset copy.

*Prepared November 4, 2026, from the Round 1 starter model
(`PillowKey_Starter.pbix`, Pillow & Key Group dataset, Microsoft Fabric
Community) and the contest brief. All evidence-pack numbers are brand sums over
hotel-month facts unless noted; guest scores are response-weighted.*
