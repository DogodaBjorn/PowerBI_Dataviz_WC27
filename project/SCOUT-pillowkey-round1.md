# SCOUT — Power BI Dataviz World Champs 2027 · Round 1 · "The Investment Challenge"

Pre-mission scouting report. Derived from the blog post (saved .mht), the starter .pbix
(`PillowKey_Starter.pbix`, 16 tables decoded with pbixray) and a first analytical pass over
the data. Every number below is a hypothesis with high prior: re-derive at stage 4/6 before
it lands in a visual. Prepared 2026-11-04.

---

## 1 · Contest facts (blocker-severity)

Source: blog post 5390883 (Round 1) + the starter file's hidden "Read Me" and "Judging Criteria" pages.

| Rule | Detail |
|---|---|
| Deadline | **November 18, 2026** (time zone in the Official Rules PDF, not fetchable from this sandbox; read it) |
| Scope | **One brand only.** Report helps the Board decide its five-year investment strategy |
| Page 1 | *The Brand Review*: where does the brand stand today? Insights, not every number |
| Page 2 | *The Investment Strategy*: where should the money go, and why? |
| Proposal must | ≥ 3 initiatives; ≥ 1 flagged `GrowthInitiative = Yes`; within the brand's `InvestmentBudgetUSD`; show budget allocation incl. costs and expected returns; show impact through **Dec 2032**; explain choices, risks, trade-offs; each initiative responds to a Page 1 finding |
| Pages | **Exactly two visible report pages**; hidden tooltip pages allowed (starter Read Me) |
| Visuals | ≥ 4 core (built-in) visuals. Custom visuals, images, icons, themes, AI design tools allowed |
| Data | Provided data only. May create measures, calculated tables, scenario parameters, calculated columns, helper/derived tables, field parameters. **May not** change values, pull extra sheets from the source workbook, use external data, or fabricate/simulate |
| Timeline | 2021–2025 historical · 2026 planning year · 2027–2031 projects may start · impact measured through 2032 |
| Audience | The Board of Directors |
| Accessibility | Labels, alt text, contrast, tab order (explicit judging criterion) |
| Submission | Fabric Community **Contests Gallery** (aka.ms/contestsgallery): report image + short description naming the brand + **.pbix or Publish-to-Web link** + the official contest tag (tag not in the post; check gallery/rules) |
| Prize | Two Round-1 entrants advance to the live finale at FabCon Atlanta, March 2027 |
| Starter canvas | 1920 × 1080; Fluent 2 base theme; starter pages are hidden in view mode |

**Judging criteria (five, from the starter file):**
1. **Analytical Quality** — accuracy of calculations, appropriate methods, correct interpretation, well-supported conclusions *(new vs. last year; this is the one to win)*
2. **Insightfulness** — relevance of insights, how well the two questions are answered, usefulness for decisions
3. **Visual Effectiveness** — layout, navigation, text, colors, choice of visuals
4. **Creativity & Innovation** — creativity, design, storytelling, innovative use of Power BI
5. **Accessibility** — alt text, logical tab order, sufficient contrast

Judges' note, verbatim: *"We're looking for thoughtful analysis, not just beautiful dashboards.
Strong entries tell a compelling story, support their recommendations with evidence, and make
complex information easy to understand."*

Deadline math: 14 days from today. Content-complete **Nov 15**, two days QA + submission mechanics.

---

## 2 · The dataset (what the starter model contains)

Source: `PillowKey_Dataset.xlsx` on Azure Blob (parameter `DataFile`, public). 16 tables, 17
single-direction relationships, **no measures**. Row counts in brackets.

**Dimensions:** `Hotels` [165: brand, city, country, region, lat/long, location type, rooms,
opening date, last renovation date] · `Brands` [4: segment, positioning, **InvestmentBudgetUSD**] ·
`Region` [3] · `Date` [2021-01-01 … 2032-12-31, with `Period` = Historical / Planning year /
Investment horizon] · `Scenario` [Low / Expected / High].

**Monthly facts, Jan 2021 – Dec 2025, per hotel:** `MonthlyPerformance` [9,810: rooms
available/sold, room / F&B / other / total revenue, staff / energy / maintenance / F&B / other
opex, total opex] · `BookingChannels` [49,050: 5 channels × bookings, room nights, room revenue,
**distribution cost**] · `GuestSegments` [49,050: 5 segments] · `GuestExperience` [9,810: survey
responses, 6 scores 0–10, NPS] · `GuestComplaints` [88,290: 9 categories].

**History:** `Renovations` [201, 1985–2023: type, rooms-out-of-service %, cost].

**Investment layer:** `InvestmentProjects` [40 = 10 per brand: category, scope, growth flag,
capex, earliest start, duration, rooms-out-of-service %, added rooms, annual running cost,
**DependsOn**, **ExclusiveWith**, description] · `InvestmentProjectProperties` [467: project →
hotel mapping; new-property projects map to no hotel] · `InvestmentScenarios` [120 = 3 per
project: driver deltas + **AnnualRevenueImpactUSD** + **AnnualOperatingProfitImpactUSD**] ·
`FinanceParameters` [10] · `FinanceAssumptions` [21: per region × year 2026–2032 market demand
growth, ADR inflation, cost inflation].

Integrity checks passed: revenue and opex components sum exactly to totals; channel room revenue
and room nights reconcile exactly to MonthlyPerformance; no nulls; 161–165 hotels per month
(late openings).

### The impact model the organisers expect (FinanceParameters, verbatim intent)

- Discount rate **8 %**, discounting to 2026. Base year **2025**: impacts are versus 2025 actuals, in 2025 dollars.
- Ramp-up after completion: **50 %** of annual impact in months 1–12, **85 %** in 13–24, **100 %** from month 25.
- Capex spent evenly over the project duration. Rooms out of service during works earn nothing (apply `RoomsOutOfServicePct` to the property's rooms for the duration).
- No start before Jan 2027; impact measured through Dec 2032.
- `FinanceAssumptions` give the no-investment baseline drift per region (demand, ADR, cost inflation).

Reconciliation I ran: the Expected `AnnualRevenueImpactUSD` reproduces from the driver columns ×
the mapped properties' 2025 actuals (ratios 0.85–1.00 for occupancy/ADR/F&B drivers; added-room
projects come out at 0.55–0.77, so added rooms almost certainly also carry the property's F&B and
other revenue mix — pin this in the metric contract). New properties: rooms × 365 × occupancy ×
ADR ≈ 0.66–0.94 of the given figure (same F&B/other uplift). Whether `AnnualOperatingProfitImpactUSD`
already nets `AnnualRunningCostUSD` must be tested at stage 2 (GI-01, MO-08, PS-06, PP-08 are the
test cases).

**Horizon trap (important for Analytical Quality):** with ramp-up, capex phasing and disruption,
and no value beyond 2032, every capital project in the dataset is NPV-negative *within the
horizon*; only the cheap digital/soft projects turn positive by 2032. A naïve "NPV through 2032"
ranking would tell the Board to build nothing. The entry must show **both** the cumulative
impact through 2032 *and* the 2032 run-rate ("exit velocity") plus payback year, and say so
explicitly. That framing is itself an insight.

Constraint pairs to model: exclusive `MO-04/MO-05`, `PS-08/PS-10`, `PP-02/PP-03`; dependencies
`GI-02 → GI-01`, `PS-01 → PS-03`.

---

## 3 · Group-wide patterns (true for all four brands)

- **Renovation age predicts guest satisfaction almost perfectly.** Across hotels, years since
  last renovation vs. 2025 overall score: r = −0.94 (Maison d'Or), −0.95 (P&K), −0.93
  (Pebble & Pine), −0.80 (Goodnight Inn); vs. complaints per room night r ≈ +0.86–0.90.
  Margin does *not* yet correlate (r ≈ 0): satisfaction is the leading indicator.
- **Every brand's NPS falls every year** and room-condition complaints rise every year.
- **Natural experiment in the data:** four hotels were fully renovated inside the window
  (Paris 2022, London 2023, Chicago Loop 2023, Myrtle Beach 2023). All four outgrew their brand
  peers 2021→2025 (London +104 % RevPAR vs peers +76 %; Chicago Loop +167 % vs +135 %;
  Myrtle Beach +37 % vs +29 %), with margin recovering the year after works. Evidence that
  renovation projects pay, usable by any brand.
- 2021 is a depressed base year everywhere (recovery years 2021→2023). Growth claims must use
  2023→2025 or 2022→2025, never 2021.

---

## 4 · The four brands

### 4.1 Pebble & Pine — family resorts · 45 hotels · 12,910 rooms · budget **$145M** · projects total $245.3M

**Where it stands (2025):** revenue $1,089M, GOP $382M (**35.1 %, down from 38.7 % in 2022**),
occupancy **64.7 % — flat for four years**, RevPAR $156 (+4 % in three years), staff cost up from
27 % to 30 % of revenue, NPS 26 → 20, the group's highest room-condition complaint count
(3,136 → 4,384), OTA share 29 % → 36 %.

**The finding:** seasonality, and it is type-specific. Brand level: 43 % occupancy in November
vs 89 % in July, seven months below 60 %. By resort type (2025):

| Type (hotels) | Trough | Peak |
|---|---|---|
| Lake & Countryside (16) | Jan 36 %, Nov 38 % | Jul–Aug 97 % |
| Coastal (15) | Jan 38 % | Jul–Aug 97 % |
| Mountain (10) | May 40 % | Jan–Feb 93–95 % |
| Tropical (3) | ~56–72 % flat | |

Lake and coastal resorts sell out in summer and sit one-third empty for five months; mountain
resorts are the mirror image. A brand-average chart hides this; most entries will show the
average.

**Projects map 1:1 onto the finding:** indoor water parks at Muskoka (min month 31 %) and Lake
Garda (32 %) are literally "to attract families outside summer"; the Algarve meeting centre
targets spring/autumn; kids-club upgrades in six resorts; a revenue-management system on a brand
that hits 97 % every July (yield left on the table); Black Forest cabins; Banff extension (the
brand's fullest hotel, 77 %); Poconos full renovation (worst NPS 0.3, 18 years since works).

**Trade-offs that tell themselves:** Lake Garda water park *or* 80 more rooms at a resort running
57 % (fill what you have vs. build more); Charlevoix new resort = $88.4M (61 % of budget), opens
2030, ~2.5 years of ramped impact inside the horizon.

**Candidate portfolio (within budget):** PP-08 RMS 6.0 + PP-05 kids clubs 8.4 + PP-01 Muskoka
28.0 + PP-02 Lake Garda 29.0 + PP-06 Algarve 9.5 + PP-10 cabins 8.4 + PP-07 Poconos 24.0 =
$113.3M; + PP-04 Banff 20.4 = $133.7M. Reject PP-09 Charlevoix, PP-03 Lake Garda rooms.

**Thesis line:** *"Sold out every July, one-third empty from November to February. Spend the
budget on the other nine months."*

### 4.2 Maison d'Or — luxury · 30 hotels · 6,015 rooms · budget **$210M** · projects total $349.6M

**Where it stands:** revenue $1,334M (the largest brand), GOP $507M (38.0 %, down from 39.4 %),
occupancy 72.9 %, **ADR $527.9 in both 2024 and 2025 — pricing power has stalled**, NPS 39 → 32,
room-condition complaints +89 % since 2021. Direct web share healthy (34 → 37 %).

**The finding:** a two-speed portfolio. Renovated hotels (London 2 y, Paris 3 y, Aspen 4 y) carry
NPS 43–47; the un-renovated flagships are the laggards: Rome (16 y, NPS 19), Hong Kong (15 y,
NPS 16), Chicago (14 y, NPS 15), Whistler (17 y, NPS 6), Mallorca (15 y, NPS 16, **58 %
occupancy**). New York runs 86 % occupancy, 93–96 % in Mar–May and Sep–Oct: it is turning guests
away.

**Projects:** Rome ($27M) and Hong Kong ($36M) full renovations hit exactly the worst houses;
NY 40-suite extension ($38M, $7.1M/yr — the best large project, capacity-justified); loyalty
platform ($12M, $4.9M/yr, best ROI); Maui spa ($14M) vs restaurant ($7M), exclusive, at the
crown-jewel hotel (RevPAR $602, NPS 47); European energy retrofit ($28.6M, $5.5M/yr).

**Trade-offs:** Lisbon new hotel = $136M (65 % of budget), opens 2030; Mallorca villas add 30
keys to a hotel that is 42 % empty; London redesign on a hotel renovated two years ago.

**Candidate portfolio:** MO-08 loyalty 12 + MO-06 NY suites 38 + MO-04 Maui spa 14 + MO-02 HK 36
+ MO-01 Rome 27 + MO-09 energy 28.6 = $155.6M (+ MO-03 London 18 = $173.6M).

**Thesis line:** *"Luxury is a promise. We keep it where we've renovated, we're breaking it in
Rome and Hong Kong, and we're turning guests away in New York."*

Caveat: the biggest budget and the glamour brand; likely the most-picked brand in the field.

### 4.3 Goodnight Inn — budget & economy · 50 hotels · 6,485 rooms · budget **$60M** · projects total $100.7M

**Where it stands:** revenue $213M, GOP $94M (**44.4 %, the group's best margin**, down from
46.1 %), occupancy 79 % and stable, RevPAR $85. NPS 8.5 → 3.3, room-condition complaints +45 %.

**The finding:** intermediaries. OTA share of room revenue **33 % → 50 %** (every hotel 49–51 %),
direct web/app share 31 % → 23 %, distribution cost **8.9 % → 11.3 % of room revenue** (other
brands 7.5–8 %), OTAs cost 18 % per booking vs 4 % direct. Airport hotels are full (Gatwick 90 %,
Toronto 92 %, Montréal 90 %); Kingston is not (61 %).

**Projects:** direct booking app ($5M, cuts distribution cost 1.2 pts ≈ $2.4M/yr), RMS ($2.4M),
kiosks ($2M, needs app), Gatwick and Toronto extensions at full hotels ($6.6M, $5.8M), 10-oldest
room refresh ($29.5M — half the budget, 15 % rooms out for 14 months), energy ($15M), breakfast
($4.25M), Boston Logan new hotel ($24.75M), Kingston extension at a 61 % hotel.

**Candidate portfolio:** GI-01 app 5 + GI-10 RMS 2.4 + GI-02 kiosks 2 + GI-05 Gatwick 6.6 +
GI-04 Toronto 5.8 + GI-07 refresh 29.5 = $51.3M (+ GI-09 breakfast 4.25 = $55.6M). Reject
Boston, Kingston, and energy (does not fit beside the refresh).

**Thesis line:** *"Our most profitable brand hands one in nine room dollars to intermediaries.
Buy the guest back, extend where we're full, fix the oldest rooms."*

Caveat: smallest numbers; least visual drama; but the $60M budget makes the sharpest
prioritisation story.

### 4.4 P&K Select — business & conference · 40 hotels · 13,990 rooms · budget **$135M** · projects total $228.7M

**Where it stands:** the comeback brand. 2021: occupancy 38 %, GOP −0.1 %; 2025: 72 %, GOP
40.0 % ($479M on $1,197M). The recovery was bought with mix: groups & events 11 % → 29 % of room
nights, corporate contracts 26 % → 35 % of revenue, leisure 42 % → 22 %. Meanwhile complaints
more than doubled (room condition +158 %, **Wi-Fi & technology +118 %** in a business brand), NPS
18.5 → 14.7. Business seasonality: dips in Jul/Aug (62–65 %) and Dec (59 %).

**Projects:** hybrid meeting tech ($6.4M, brand-wide, prerequisite for Las Vegas), SME sales
programme ($6M, best ratio), Las Vegas conference expansion ($19M), Houston expansion ($17M, at
the weakest RevPAR hotel), Washington DC full renovation ($34.2M, NPS −5, 16 y), Seattle
extended-stay floor ($7.2M, fills the summer/December dip), energy ($18M), Madrid rooftop vs
co-working, Austin new hotel ($112.8M = **84 % of budget**).

**Candidate portfolio:** PS-03 6.4 + PS-06 6 + PS-01 Vegas 19 + PS-04 DC 34.2 + PS-05 Seattle
7.2 + PS-09 energy 18 + PS-08 Madrid rooftop 5.5 = $96.3M. Reject Austin, Houston.

**Thesis line:** *"The recovery was bought with meetings and contracts; the product hasn't kept
up. Lock in the engine, fix the worst house, don't bet the budget on Austin."*

Caveat: the strongest *backward* story (the recovery) but the forward projects are the least
coherent set; Austin dominates the budget conversation.

---

## 5 · Recommendation

**Pick Pebble & Pine.** Reasons, in judging-criteria order:

1. *Analytical Quality*: the two-season finding (lake/coast vs mountain) is a real analytical
   result that brand averages hide, and the impact model can be made seasonal (water-park uplift
   lands in off-season months), which is a defensible, labelled modelling choice.
2. *Insightfulness*: one diagnosis (empty shoulder seasons, flat occupancy, margin erosion from
   seasonal staffing) explains the brand's stall, and every recommended project is a direct
   answer to it. The Board sees cause → remedy on one axis.
3. *Visual Effectiveness*: the hero chart draws itself (45 hotels × 12 months, sorted by resort
   type: a seasonality ridge/heatmap). It is a single image that makes the case.
4. *Creativity*: a warm family-resort visual world is distinctive next to the gold-and-ink
   luxury entries the field will produce; the "fill what you have vs. build more" Lake Garda
   trade-off and the Charlevoix rejection give the strategy page genuine drama.
5. The budget bites ($245M of asks, $145M available) without one project swallowing it.

**Runner-up: Maison d'Or** — the richest evidence (NY capacity, renovation natural experiment,
Lisbon trap) and the biggest numbers, at the cost of probably being the most-chosen brand.

---

## 6 · Open items to resolve before/at stage 2

- Official Rules PDF: deadline time zone, eligibility, the exact contest tag, whether hidden
  tooltip pages count (starter says allowed).
- Does the source workbook contain sheets the starter does not load? (Rule says don't pull them;
  we only need to know we are not missing a loaded one.)
- Metric contracts: OP impact nets running cost (reconciled); disruption = room revenue only or total
  revenue, with or without variable-cost relief; do added rooms carry F&B/other mix; how the
  Low/High scenarios combine across a portfolio (sum per scenario, not mix).
- Distribution cost sits **outside** MonthlyPerformance opex (the workbook's Contents sheet says
  costs exclude distribution costs, per the Dutch review of 4 Nov; confirm the wording). Margin
  after commissions: Goodnight 33.7 %, P&K 34.7 %, Maison d'Or 32.9 %, Pebble & Pine 28.2 %.
  See `project/research/2026-11-05-crosscheck-dutch-review.md`.
- Start-month policy: earliest start maximises in-horizon impact; the report may expose
  start year as a what-if parameter (allowed: "scenario parameters").
- Baseline: whether to project the no-investment 2026–2032 baseline with FinanceAssumptions
  (demand, ADR, cost inflation) and show impact as delta over baseline, in 2025 dollars.
