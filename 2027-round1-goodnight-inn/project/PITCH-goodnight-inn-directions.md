# PITCH — three directions for the Goodnight Inn entry, and the dataset codex

Built the pbi-atelier way: three directions that differ in *kind* (design-critique
divergence), each argued against `design/design-doctrine.md` and scored 0-10 on the seven
G5 passes from `references/scoring.md`, polish and showpiece moves named per
`dataviz-polish`, chart forms chosen by intent per `chart-grounding`. Scores inform; you
decide. Part B is the codex: every table, every column, every quirk, and the idea seeds
they carry, so you can draw your own directions from the same ground.

All numbers are from the offline decode of `PillowKey_Starter.pbix` and are hypotheses
until re-derived in the model. Prepared 2026-11-04.

---

## Part A — Three directions

The shared contract (from the mission): one brand (Goodnight Inn), two visible pages
(Brand Review / Investment Strategy), ≥ 4 core visuals, ≤ $60 M, ≥ 3 initiatives with
≥ 1 growth, impact through 2032, must render under Publish-to-Web, built-in fonts only.
The *story* is fixed; what diverges is the stance: how the Board is made to see it.

### The divergence test, up front

| | D1 Wake-up call | D2 Fifty keys | D3 Two futures |
|---|---|---|---|
| Stance | editorial briefing: *here is what is wrong and what we do about it* | operations wall: *fifty units, one decision each* | finance ledger: *2032 twice, with and without the plan* |
| Unit of analysis | the brand | the hotel | the year |
| Analytical spine | channel counterfactual + renovation-age cohort | hotel segmentation + capacity timing | baseline projection + scenario bands + payback |
| Page 2 engine | plan builder (tick projects, watch budget/impact) | the wall re-lit by the plan, year by year | plan curve vs baseline with Low/High band |
| Signature moment | the folio (what a $109 night nets, by channel) | the key-card wall lighting up | the diverging fan |
| Surface | paper white, editorial type | night navy, amber lights | cream ledger, ink, tabular figures |

Swap the accent colours and these are still three different reports. Divergence holds.

---

### D1 · "Wake-up call" — the Board briefing

**Organizing concept.** A one-page briefing memo the chair reads before the meeting,
and a second page that is the decision itself. Headline, three findings, a plan. The
report *is* the argument; nothing on it is furniture.

**Why it wins on the criteria.** Analytical Quality from two pieces of evidence most
entries will not have: the channel-mix counterfactual ("at the 2021 mix, 2025
distribution cost would be $4.8 M lower") and the 2021 renovation cohort (seven hotels
that held NPS +6…+9 while the other 43 slid +8.9 → +2.7). Insightfulness from a diagnosis
with three named causes that each map to a funded move. Creativity from the plan builder
the judges can click in the gallery.

**Visual language.** Paper white surface, one accent (lamp amber) on a navy ink, the
good/bad pair never alone. Showpiece type hierarchy (S3): a display serif for hero
numbers and headlines, a grotesk for labels, a mono for kickers (all from Power BI's
built-in list: Georgia / Segoe UI / Consolas). Density *balanced*, variance *strict*.
Signature layout move: the page is three vertical story columns under a one-line
headline, the way a briefing is written, not a grid of equal cards.

**Page 1 — "Wake-up call"** (3-second message: *full, flat, and paying the middleman;
the group's best margin is slipping*)

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ GOODNIGHT INN · BRAND REVIEW 2021-2025 · for the Board of Pillow & Key Group   [ⓘ]  │
│ Full, flat, and paying the middleman: the group's best margin is slipping.           │
├──────────────┬──────────────┬──────────────┬──────────────┬──────────────────────────┤
│ Occupancy    │ RevPAR       │ GOP margin   │ NPS          │  sister-brand benchmark  │
│ 79.4%  ─ flat│ $84.8  +1.0% │ 44.4% ▼1.7pt │ +3.3  ▼5.2   │  margin 44 vs 35-40      │
├──────────────┴──────────────┼──────────────┴──────────────┼──────────────────────────┤
│ THE PLATEAU                 │ THE MIDDLEMAN               │ THE FADING WELCOME       │
│ Revenue/occupied room vs    │ Channel share of room       │ NPS by years since last  │
│ cost/occupied room, indexed │ revenue 2021→2025, stacked  │ refresh: dot strip of 50 │
│ 2023=100 (line, 2 series)   │ area; OTA 33%→50%           │ hotels, ≤5y / 6-9y / 10+ │
│                             │                             │                          │
│ GOP bridge 2024→2025        │ ┌─ THE FOLIO ─────────────┐ │ Complaints per 1k nights │
│ (waterfall: volume, rate,   │ │ Room night        $109  │ │ by category, check-in &  │
│ staff, energy, maint, other)│ │ OTA commission   -$20   │ │ room condition in accent │
│                             │ │ We keep           $90   │ │                          │
│                             │ │ … direct: we keep $107  │ │                          │
│                             │ └─────────────────────────┘ │                          │
├─────────────────────────────┴─────────────────────────────┴──────────────────────────┤
│ WHERE WE'RE FULL  airport 82% · highway 78% · city 79% │ Gatwick ▁▃▆█████▇▆ 90%     │
│                                                         │ Toronto ▂▅██████▇▆ 92%     │
│                                                         │ Kingston ▁▂▃▃▂▁▂▂▁ 61%     │
│ Data: Pillow & Key Group dataset · scores response-weighted · 2021 is a depressed base│
└──────────────────────────────────────────────────────────────────────────────────────┘
```

Chart forms by intent: index lines (change over time, 2 series, one accent); waterfall
(flow); stacked area for the channel mix (part-to-whole over time) with the "$4.8 M at
the 2021 mix" annotation (S2); the folio is a table set for scanning (detail lookup
dressed as a receipt); dot strip for the age cohort (distribution, items findable);
sparklines in the "where we're full" strip (move 5).

**Page 2 — "The morning plan"** (3-second message: *$51 M of $60 M on three moves,
+$7.6 M a year by 2032; no to Boston, Kingston and kilowatts*)

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ THE MORNING PLAN · 2027-2032                                       [Reset to our plan]│
│ $51.3 M of $60 M on three moves: +$7.6 M a year of operating profit by 2032.          │
├──────────────────────────┬───────────────────────────────────┬───────────────────────┤
│ PLAN BUILDER             │ IMPACT (Expected ▾ Low · High)    │ DEPARTURES            │
│ Buy the guest back       │ 2032 run-rate   +$7.6 M  (+8%)    │ GI-01 app  JAN27→OCT27│
│  ☑ Booking app   $5.0 M  │ Cumulative 2027-32 curve with     │ GI-10 RMS  JAN27→JUL27│
│  ☑ Revenue mgmt  $2.4 M  │ Low-High band; payback year per   │ GI-02 kiosk OCT27→MAR28│
│  ☑ Kiosks        $2.0 M  │ initiative as a strip             │ GI-07 rooms JAN27→MAR28│
│ Fix the welcome          │                                   │ GI-05 LGW  JAN27→MAY28│
│  ☑ 10 oldest    $29.5 M  │ Operational: +80 rooms, 1,180     │ GI-04 YYZ  JAN27→MAY28│
│ Build where we're full   │ rooms refreshed, direct share     │ status / disruption   │
│  ☑ Gatwick       $6.6 M  │ target, check-in time             │ months per hotel      │
│  ☑ Toronto       $5.8 M  │                                   │                       │
│ Not funded               ├───────────────────────────────────┴───────────────────────┤
│  ☐ Boston   ☐ Kingston   │ NOT FUNDED, AND WHY      Boston 41% of budget, opens 2029 │
│  ☐ Energy   ☐ Breakfast  │ Kingston 61% occupancy, Low case loses · Energy 8.5-y payback│
│ ████████░░ $51.3 M / $60 M│ RISKS & TRADE-OFFS  rooms vs kilowatts · 15% of 1,180 rooms│
│ ● 6 projects ● 4 growth  │ out for 14 months · app adoption is the swing · horizon   │
│ ● dependencies met       │ honesty: capital projects pay back after 2032              │
└──────────────────────────┴───────────────────────────────────────────────────────────┘
```

Polish moves contracted: insight titles from measures (1), semantic colour on the
budget bar and constraint lamps (2), one focal accent on the chosen plan (3), the $60 M
reference line (4), hero KPI at full dress for the run-rate (S4), editorial framing (S1),
annotation layer on the cumulative curve (S2), info affordance for the method (S6). One
story bookmark per page (the "how we calculated this" overlay on P2 is a utility state).

**Signature moment.** The folio: a hotel bill that shows the Board, in the brand's own
idiom, that an OTA guest and a direct guest pay the same $109 and leave $90 vs $107 on
the desk. Readers quote it.

**Risk.** Words. A briefing lives on copy; if the copy-polish sweep is weak the page
reads as a text document with charts, and the KPI band at the top is one lazy build away
from a card wall.

**Design read.** The headline, then the amber OTA wedge growing across the middle
column, then the folio. The order is the argument.

---

### D2 · "Fifty keys" — the night-desk wall

**Organizing concept.** Behind every reception desk is a wall of key hooks. Goodnight
Inn is fifty hotels, and every investment decision is made hotel by hotel: this one is
full, this one is tired, this one we leave alone. Page 1 is the wall as it is; page 2 is
the wall as the plan lights it up, year by year to 2032.

**Why it wins on the criteria.** Creativity & Innovation: the wall is the element a
judge describes afterwards, and it is native (a matrix with data bars and conditional
formatting, or small multiples). Analytical Quality from a hotel-level segmentation
nobody reaches from brand totals — *Full* (7 hotels at ≥ 85 %: Toronto, Montréal,
Gatwick, Phoenix, Kansas City, Orlando, Kuala Lumpur), *Tired* (12 hotels with negative
NPS, 8 of them in the refresh list), *Fine* (the rest), *Weak* (Kingston, 61 %, never
above 74 %) — plus capacity timing from the organisers' own demand assumptions (Toronto
hits the wall in 2028, Montréal 2029, Gatwick 2030). Operational impact is literal: which
rooms, which desks, which hotels, when.

**Visual language.** Night navy surface, amber key-card lights, white type; compact
density, expressive variance (the wall is allowed to be dense because it is one
visual). Grotesk throughout (Segoe UI), tabular figures. Signature layout move: the
wall occupies two-thirds of each page; everything else is a margin note.

**Page 1 — "The wall tonight"** (3-second message: *seven hotels are full, twelve are
tired, and the tired ones are the oldest*)

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ GOODNIGHT INN · 50 HOTELS · 6,485 ROOMS      Seven are full. Twelve are tired.       │
├────────────────────────────────────────────────────────────┬─────────────────────────┤
│ THE WALL  (matrix: one row per hotel, sorted by NPS)       │ FULL vs TIRED           │
│ hotel ▏occupancy bar▕ RevPAR ▕ NPS chip ▕ yrs since refresh │ scatter: occupancy ×    │
│ Toronto Pearson   ████████████ 92%  $94  −0.3   9y          │ NPS, bubble = rooms,    │
│ Montréal-Trudeau  ███████████▌ 90%  $98  −4.2  10y          │ quadrants labelled      │
│ Gatwick           ███████████▌ 90% $145  +6.8   8y          │                         │
│ …                                                          ├─────────────────────────┤
│ Sydney Airport    ██████████   83%  $99  −9.2  13y          │ THE MIDDLEMAN (one      │
│ Chicago Midway    █████████▌   78%  $85  −7.3  13y          │ number): OTA takes 50%  │
│ Lyon              ██████████▌  83%  $74  −7.3  14y          │ of room revenue at      │
│ Kingston          ███████▌     61%  $55  −1.8  11y          │ every hotel (49-51%);   │
│ (amber = ≥85% full · bad-colour chip = NPS < 0, with sign) │ cost $22.7 M, +80% in 4y│
├────────────────────────────────────────────────────────────┴─────────────────────────┤
│ CAPACITY WALL  demand vs rooms 2026-2032 for the 8 hotels that run out (small mult.) │
│ Toronto 2028 · Montréal 2029 · Gatwick 2030 · Sydney · KL · Osaka · Phoenix · KC     │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

**Page 2 — "The wall in 2032"** (3-second message: *every amber light is a funded
decision: 20 kiosks, 10 refreshes, 2 extensions, 0 new hotels*)

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ THE PLAN ON THE WALL      year ◂ 2027 2028 2029 2030 2031 2032 ▸     $51.3 M / $60 M │
├────────────────────────────────────────────────────────────┬─────────────────────────┤
│ THE WALL, RE-LIT  (same matrix; cells light up by project  │ THE PLAN                │
│ and year: app ● kiosk ● refresh ● +rooms ●)                │ 6 projects, 4 growth    │
│ Toronto Pearson   ● ● ● +40 rooms (May 2028)               │ budget bar, lamps       │
│ Gatwick           ● ● +40 rooms (May 2028)                 │ run-rate +$7.6 M/yr     │
│ Sydney Airport    ● ● refreshed (Mar 2028)                 │ Low/High band           │
│ …                                                          │ payback per initiative  │
│ Kingston          ○ (not funded: 61% occupancy)            ├─────────────────────────┤
│ Boston Logan      ○ (not funded: 41% of budget)            │ WHY NOT: Boston,        │
│ legend: ● funded this year · ○ considered, not funded      │ Kingston, Energy        │
├────────────────────────────────────────────────────────────┴─────────────────────────┤
│ IMPACT BY HOTEL  rooms added 80 · rooms refreshed 1,180 · kiosks at 20 desks ·       │
│ direct-share target · cumulative 2027-2032 curve (small)                             │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

The year stepper is a **slicer on Date[Year]** (a filter), not a chain of bookmarks, so
the one-story-bookmark budget per page is respected. Polish: semantic colour with a
sign/label in every chip (2), one accent (3), reference line on the budget bar (4), full
in-cell encoding on the wall (S5), editorial masthead (S1), ⓘ for method (S6).

**Signature moment.** The wall lighting up as the year slider moves from 2027 to 2032.

**Risk.** Density and the dark surface. Fifty rows at 1080 px means ~16 px per row:
legible, but every chip needs a printed value, every amber needs AA contrast on navy,
and the Board may read it as an operations screen rather than a strategy. Publish-to-Web
rendering time with a 50 × 8 conditional-formatted matrix must be tested early.

**Design read.** The amber band at the top of the wall (the full hotels), then the red
chips clustering at the bottom with the big age numbers, then the capacity wall.

---

### D3 · "Two futures" — the ledger

**Organizing concept.** The Board is shown 2032 twice. First the brand if nothing is
funded, projected with the organisers' own `FinanceAssumptions` (demand, ADR and cost
inflation by region): the market hands Goodnight Inn +14 % demand, fills it to 90 %,
and every one of those dollars arrives at a thinner margin (44.4 % → 41.7 %) through a
dearer channel, while eight hotels run out of rooms. Then 2032 with the plan, as a
band, not a line.

**Why it wins on the criteria.** Analytical Quality: it uses the table most entries
will ignore (`FinanceAssumptions`), it decomposes the baseline (volume the market gives,
price inflation, cost inflation, channel drift), and it states uncertainty with the
Low/Expected/High scenarios the organisers provided. Insightfulness: the capacity wall
turns "extend Gatwick and Toronto" from a preference into a dated necessity.

**Visual language.** Cream paper, ink text, one accent, hairline rules, tabular
numerals in a mono (Consolas) for every figure; airy density, strict variance. Signature
layout move: each page is two large charts and a column of figures, like an annual
report spread.

**Page 1 — "2032, if we do nothing"** (3-second message: *the market will fill our
rooms; it will not protect our margin*)

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ GOODNIGHT INN · TWO FUTURES              2025 actual │ 2032 if nothing is funded      │
├─────────────────────────────────────────┬────────────┴────────────────────────────────┤
│ MARGIN 2021-2032: actual line, then the │ WHAT 2032 IS MADE OF (bridge 2025 → 2032)   │
│ do-nothing projection as a fan          │ + volume the market gives   (demand +13.7%) │
│ 46.1% (2023) → 44.4% (2025) → 41.7%     │ + price inflation           (ADR +17.7%)    │
│ (2032, scenario: provided assumptions)  │ − cost inflation            (opex +23.4%)   │
│                                         │ − channel drift             (OTA 33% → 50%) │
│ [scenario logic, labelled on the chart] │ = margin 41.7%                              │
├─────────────────────────────────────────┼─────────────────────────────────────────────┤
│ THE CAPACITY WALL  demand vs available  │ THE MIDDLEMAN, PRICED                       │
│ rooms, 8 hotels, first capped year      │ distribution cost 8.9% → 11.3% of room      │
│ Toronto 2028 · Montréal 2029 ·          │ revenue; $4.8 M/yr above the 2021 mix;      │
│ Gatwick 2030 · Sydney, KL, Osaka,       │ OTA and direct guests pay the same rate     │
│ Phoenix, Kansas City by 2032            │ (folio as a figure column)                  │
└─────────────────────────────────────────┴─────────────────────────────────────────────┘
```

**Page 2 — "2032, with the plan"** (3-second message: *the plan lifts operating profit
+$7.6 M a year by 2032 against a baseline that is already thinning*)

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ THE PLAN AGAINST THE BASELINE           Expected ▾   Low · High     $51.3 M / $60 M  │
├──────────────────────────────────────────────────────┬───────────────────────────────┤
│ OPERATING PROFIT 2025-2032: baseline (grey) vs plan  │ THE LEDGER (table)            │
│ (accent) with the Low-High band; capex phasing and   │ initiative · capex · start ·  │
│ disruption shown as the dip in 2027-28; the ramp     │ live · 2032 run-rate · payback│
│ 50/85/100% annotated                                 │ app  5.0  Jan27 Oct27 2.35 2030│
│                                                      │ RMS  2.4  …                   │
│ "Capital projects pay back after the horizon; the    │ …                             │
│ run-rate is the number to read"                      │ not funded rows, greyed, with │
├──────────────────────────────────────────────────────┤ the one number that killed    │
│ CUMULATIVE NET 2027-2032 per initiative (bars from   │ them                          │
│ zero, diverging), payback year labelled              ├───────────────────────────────┤
│                                                      │ PLAN SELECTOR (compact) +     │
│                                                      │ start-delay what-if (months)  │
└──────────────────────────────────────────────────────┴───────────────────────────────┘
```

**Signature moment.** The fan: one line splitting into a grey do-nothing future and an
amber funded band.

**Risk.** Honesty optics. The baseline is scenario logic built from the organisers'
assumptions; if any chart shows it without the label, a judge can call it simulated
data (rule: "fabricate or simulate data" is forbidden). Every projected mark carries
the caveat, and the impact figures stay in 2025 dollars as the parameters prescribe.
Second risk: it is finance-first; the "why" (what is actually wrong at the hotels) is
thinner, so Insightfulness leans entirely on the capacity wall and the margin bridge.

**Design read.** The split in the fan, then the bridge, then the dates on the capacity
wall.

---

### Critique — the seven passes (0-10; 8+ minor notes, 5-7 named gaps, < 5 rework)

| Pass | D1 Wake-up call | D2 Fifty keys | D3 Two futures |
|---|---|---|---|
| 1 Reading path | **8** — headline → OTA wedge → folio lands unaided; 3-minute path via folio, counterfactual and benchmark tooltips. Gap: P1 is text-dense; the third column needs a hero number or it reads last. | **6** — the wall is texture before it is a message; needs a one-line verdict above it and the amber band sorted to the top. The 3-minute path is excellent (every hotel findable). | **7** — the fan lands; the bridge needs reading time. 3-minute path depends on the scenario label being *on* the chart, not in a tooltip. |
| 2 State coverage | **7** — builder with nothing ticked must be a designed state ("tick a project"); longest project name fits. Gap: the Low/High toggle cleared → default to Expected via bookmark. | **6** — longest hotel name (39 chars) truncates in a 50-row matrix at 1080 px; year slicer cleared shows all years lit at once, needs a designed default. | **7** — scenario toggle cleared → Expected; start-delay parameter at 0 is the default state. Gap: the fan with Low = High (no band) on cheap projects. |
| 3 Slop risk | **6** — the KPI band is the risk (uniform card wall); mitigated only by S3 type and benchmark deltas. The three-column briefing itself is not generic. | **8** — nothing on the page swaps into a SaaS dashboard; the wall is the brand's own idiom. | **5** — fan + bridge + ledger is the classic finance deck; the cream ledger type is the only defence. |
| 4 Brand alignment | **7** — paper, folio, lamp amber: hospitality-native. Kit still to be built. | **8** — key cards and a night desk *are* Goodnight Inn; a reader says "that's a hotel" before reading a number. | **6** — a ledger is any company's ledger; brand lives in the accent only. |
| 5 Accessibility | **8** — light surface, few states, one bookmark; alt text and tab order straightforward. | **6** — AA amber-on-navy is achievable but every chip must print its value; the wall is one visual (one tab stop), which helps; dark overlays double the contrast checks. | **7** — bands need a pattern or label, not colour alone; otherwise light and simple. |
| 6 Dial fit | **7** — "balanced/strict" is at risk of cramped on P1 (KPI band + three columns + bottom strip at 1080 px). | **6** — "compact/expressive" can leak into cramped; the rule must be: the wall is dense, everything else airy. | **8** — "airy/strict" is exactly what two big charts and a figure column produce. |
| 7 Signature strength | **7** — the folio is buildable (table + formatting) and the brand's own; smaller than a wall, but quotable. The plan builder is shared with D2/D3 so it is not D1's alone. | **9** — the lit wall is the element a judge describes; buildable natively (matrix + conditional formatting driven by a year slicer); its own, not a trope. | **8** — the fan is buildable (area with Low/High measures or Deneb errorband); strong, but fan charts are a borrowed finance trope. |
| **Total** | **50** | **49** | **48** |

**Biggest gap per direction.** D1: the KPI band (slop) and copy weight — fix with S3
type, benchmark deltas on every card, and a hard word budget. D2: reading path — fix
with a verdict headline and a sort that puts the story rows first; and test the
dark-surface contrast before the comp is approved. D3: honesty optics — fix by
labelling every projected mark on the canvas and keeping impacts in 2025 dollars; and
borrow one hotel-level panel so the "why" is not only macro.

**Recommendation.** **D1, with D3's fan adopted as the impact panel on page 2** (an
analytic, not a mood; it survives D1's fidelity checklist). D1 has the highest floor on
the criteria the judges weight (analysis, insight, accessibility) on a 14-day clock, and
its signature is quotable. **If you want the bolder bet, take D2**: it has the highest
ceiling on Creativity and the most memorable artefact, at the cost of ~2 extra craft
days (contrast, density, matrix performance under Publish-to-Web). D3 alone is the
riskiest: its best ideas are better as borrowed panels than as the whole stance.

Convergence rule: one element may cross directions (D3's fan into D1; D2's capacity
wall into either), a mood may not. The chosen direction's fidelity checklist decides.

**Fidelity checklist (if D1):** the three-column briefing layout under a one-line
headline on P1; the folio with real channel figures; the plan builder with budget bar
and constraint lamps on P2; S3 type hierarchy identical on both pages; the amber accent
on exactly one story series per visual.

**Unresolved decisions**

```
DECISION NEEDED                                     | IF DEFERRED, WHAT HAPPENS
----------------------------------------------------|----------------------------------------------
Direction: D1 / D2 / D3 (or D1 + D3 fan)?            | Stage 5 re-runs divergence from scratch (2 days)
Do-nothing baseline on the canvas at all?           | Impact shown vs static 2025 only (safe, duller)
Disruption = total revenue or room revenue only?    | Model ships conservative (total), understating NPV
Reserve $8.7 M as contingency or fund GI-09?        | Page 2 shows $51.3 M and an unexplained remainder
Dark surface allowed (D2) given AA on Publish-to-Web?| D2 is not a candidate
pbiviz go/no-go date Nov 11 stands?                 | Native departures board ships
```

---

## Part B — The dataset codex

Source: `PillowKey_Dataset.xlsx` (public Azure blob) loaded by the starter into 16
tables, 17 single-direction many-to-one relationships, **no measures, no calculated
columns, no hierarchies, no marked date table**. Canvas 1920 × 1080, Fluent 2 base
theme. Four hidden starter pages (Read Me, Judging Criteria, Overview, empty Page 1).
Integrity verified: revenue and opex components sum exactly to their totals; channel
room revenue and room nights reconcile exactly to MonthlyPerformance; zero nulls in the
facts; 161-165 hotels per month (late openers).

### B1 · Dimensions

**Hotels** (165 rows; one per hotel)
`HotelID` (MO/PP/PS/GI + 3 digits) · `HotelName` · `Brand` · `City` (131) · `Country` (28)
· `Region` (North America 73 / Europe 65 / Asia-Pacific 27) · `Latitude`, `Longitude`
· `LocationType` (9 values: City center, City, Airport, Highway, Resort - Coastal /
Lake & Countryside / Mountain / Tropical / Theme park) · `Rooms` (90-475, median 225;
group total 39,400) · `OpeningDate` (1975-2023) · `LastRenovationDate` (2007-2023,
**10 nulls** = never renovated).
Goodnight Inn: 50 hotels, 6,485 rooms (90-170, avg 130), 17 Airport / 22 Highway / 11
City, 25 NA / 20 EU / 5 APAC, opened 1998-2023, 6 never renovated (Orlando, Ottawa,
Paris CDG, Valencia, Porto, Lisbon).
Seeds: product age (years since refresh, falling back to opening date); location-type
economics; map only if place is the point (airport clusters); latitude as a seasonality
proxy.

**Brands** (4): `Brand`, `Segment`, `Properties`, `Positioning` (one sentence each),
`InvestmentBudgetUSD` (210 / 145 / 135 / **60** M). Seeds: budget per room ($9.3 k for
GI vs $34.9 k Maison d'Or); positioning text as copy source.

**Region** (3) — lookup only. **Scenario** (3: Low 1 / Expected 2 / High 3) — **not
related to anything**; relate it or TREATAS it to InvestmentScenarios.

**Date** (4,383 daily rows 2021-01-01 → 2032-12-31): `Year`, `Quarter`, `MonthNumber`,
`Month` (Jan…), `YearMonth` (2028-01), `Period` (Historical 2021-25 / Planning year
2026 / Investment horizon 2027-32). Facts join on the first of the month. Mark it as the
date table; it already spans the projection years, which is a hint about what the
organisers expect you to chart.

### B2 · Monthly facts (hotel × month, Jan 2021 → Dec 2025, 60 months)

**MonthlyPerformance** (9,810): `RoomsAvailable`, `RoomsSold`, `RoomRevenue`,
`FoodBeverageRevenue`, `OtherRevenue`, `TotalRevenue`, `StaffCost`, `EnergyCost`,
`MaintenanceCost`, `FoodBeverageCost`, `OtherOperatingCost`, `TotalOperatingExpenses`.
Derivable: occupancy, ADR, RevPAR, GOP, GOP margin, CPOR, revenue per occupied room,
cost ratios, F&B margin, revenue mix, seasonality, capacity (RoomsAvailable ÷ days =
rooms in service, which drops during renovations). GI 2025: revenue $212.8 M (94 % rooms,
3.8 % F&B, 2.4 % other), opex $118.4 M (staff 28.3 %, other 16.9 %, energy 4.9 %,
maintenance 4.4 %, F&B cost 1.2 % of revenue), GOP $94.4 M.
Quirks: 2021 is a depressed base everywhere (recovery 2021-23); margins in every brand
peak 2023 and slip after; GI's cost per occupied room rose 3.5 % in 2025 against +0.9 %
revenue per occupied room.
Seeds: the plateau; the scissors; quarterly margin pattern (GI Q3 48 % vs Q1 39 %);
energy share fell from 5.9 % (2022) to 4.9 % without any project; hotel-level margin is
*uniform* (43.5-45.5 %) — the brand runs a template, so differences are volume and rate,
not cost discipline.

**BookingChannels** (49,050; hotel × month × 5 channels): `Bookings`, `RoomNights`,
`RoomRevenue`, `DistributionCost`. Channels: Direct Website & App, Direct Phone &
Walk-in, Online Travel Agencies, Corporate Contracts, Travel Agents & Tour Operators.
Cost rates are fixed per channel and brand (GI: 4 / 1.5 / 18 / 5 / 10 %; MO OTA 16 %, PS
& PP OTA 15 %, PP TA/TO 18 %). Nights per booking 1.44 (corporate) to 2.04 (TA/TO).
GI 2025 revenue share: OTA 50.0 %, direct web 23.0 %, corporate 12.6 %, phone 8.3 %, TA
6.1 %. Distribution cost $22.65 M = 11.3 % of room revenue (2021: 8.9 %).
Quirks: OTA share is identical at every GI hotel (49-51 %), so the drift is a brand
policy effect, not a local one; whether DistributionCost sits inside OtherOperatingCost
is **not stated** (never double-count; state the assumption).
Seeds: the middleman; the $4.8 M counterfactual; ADR by channel (no OTA premium); the
folio; booking length by channel; corporate contracts shrinking at GI (16 % → 13 %)
while business-travel *segment* grows — guests book business trips through OTAs.

**GuestSegments** (49,050; hotel × month × 5 segments): `Bookings`, `RoomNights`,
`RoomRevenue`. Segments: Leisure, Family, Business Travel, Groups & Events, Long Stay.
GI 2025 nights: leisure 38 %, business 24 % (from 20 %), family 23 %, groups 8 %, long
stay 8 %; ADR leisure $114 > family $108 > business $108 > groups $92 > long stay $81.
Seeds: who pays the most per night; segment mix as a hotel-type fingerprint (airport =
business); segment ADR vs channel ADR (two cuts of the same revenue).

**GuestExperience** (9,810; hotel × month): `SurveyResponses` (21-452), six scores 0-10
(`Overall`, `Cleanliness`, `Service`, `RoomComfort`, `Amenities`, `ValueForMoney`;
observed 6.1-9.65) and `NetPromoterScore` (−20.5 … 64.1). **Scores are averages: weight
every aggregate by SurveyResponses.** GI 2025 weighted: overall 7.31 (from 7.50), room
comfort 7.17 (from 7.43, the largest fall), value 7.66, NPS +3.3 (from +8.5).
Seeds: the fading welcome; score vs renovation age (r = −0.78 at GI, −0.93…−0.95 at the
other brands); NPS vs occupancy (none: full hotels are not happier); response volume as
a proxy for engagement.

**GuestComplaints** (88,290; hotel × month × 9 categories): `Complaints` (0-40 per
cell). Categories: Room condition, Cleanliness, Noise, Staff & service, Check-in &
waiting times, Wi-Fi & technology, Food & beverage, Facilities & activities, Billing &
pricing. Normalise per 1,000 room nights. GI 2025: 9.9 per 1k (from 9.4); room condition
1.80 (+17 % since 2021), check-in 1.10 (+25 %, fastest), billing 1.21, cleanliness 1.22.
Seeds: which complaint each project answers (kiosks ↔ check-in; refresh ↔ room
condition; app ↔ billing?); complaint mix as a hotel signature.

### B3 · History

**Renovations** (201; 1985-2023): `HotelID` (155 distinct; 10 hotels never renovated),
`StartDate`, `EndDate` (8 months typical), `RenovationType` (Full renovation 125 / Rooms
refresh 76), `RoomsOutOfServicePct` (20-35 %), `CostUSD` ($1.5-38.9 M). Only four
renovations finish inside the data window (Paris 2022, London 2023, Chicago Loop 2023,
Myrtle Beach 2023) and 17 finish in 2021 (seven at GI, $2.1-3.5 M each).
Seeds: the natural experiment (renovated vs peers 2021→2025); the 2021 GI cohort that
held its NPS; cost benchmarks for the refresh project ($2.95 M/hotel vs $2.1-3.5 M
historic); disruption benchmarks (OOS 20-35 % for 8 months vs GI-07's 15 % for 14).

### B4 · The investment layer

**InvestmentProjects** (40; 10 per brand): `ProjectID`, `Brand`, `ProjectName`,
`Category` (Renovation 6 / New services 10 / Expansion 10 / New property 4 / Digital 5
/ Efficiency 4 / Commercial 1), `Scope` (Single property 23 / Multiple properties 4 /
Brand-wide 9 / New property 4), `GrowthInitiative` (Yes 28 / No 12; GI 7 / 3),
`CapexUSD` ($2-136 M), `EarliestStart` (Jan 2027 for 38, Jul 2027 for MO-06, MO-10,
PP-09), `DurationMonths` (6-36), `RoomsOutOfServicePct` (0-30 %), `AddedRooms` (0-260),
`AnnualRunningCostUSD` (0 / 0.3 / 0.6 / 0.8 / 1.5 / 2.0 M), `DependsOn` (GI-02 → GI-01,
PS-01 → PS-03), `ExclusiveWith` (MO-04/05, PS-08/10, PP-02/03), `Description`.
Sum of asks per brand always exceeds budget (GI $100.7 M vs $60 M).

**InvestmentProjectProperties** (467; project → hotel): brand-wide projects map to all
hotels of the brand; multi-property projects list their hotels (GI-02's "20 busiest",
GI-07's "10 oldest"); single-property projects map to one; the four new-property
projects map to none.

**InvestmentScenarios** (120; project × Low/Expected/High): drivers
`OccupancyChangePts`, `ADRChangePct`, `AddedRoomsOccupancy`, `FoodBeverageRevenueChangePct`,
`OtherRevenueChangePct`, `OperatingExpenseChangePct`, `DistributionCostChangePts`,
`SatisfactionChangePts`, `NewPropertyOccupancy`, `NewPropertyADR`; results
`AnnualRevenueImpactUSD`, `AnnualOperatingProfitImpactUSD` (one project goes negative in
Low: GI-06 Kingston). Reconciliation: revenue impacts reproduce from drivers × the
mapped hotels' 2025 actuals; OP impacts **net the running cost**; added rooms carry the
property's F&B/other mix.
Seeds: impact per capex dollar (app 47 %, RMS 32 %, kiosks 21 %, breakfast 20 %, Gatwick
16 %, energy 12 %, Toronto 12 %, Kingston 8 %, Boston 8 %, refresh 8 %); satisfaction
points as a non-financial return; the Low-High spread as a risk measure (app ±$1.75 M,
extensions ±$0.1 M: digital is high-variance, bricks are low-variance).

**FinanceParameters** (10): discount rate 8 % to 2026; base year 2025 (impacts in 2025
dollars vs 2025 actuals); ramp-up 50 % / 85 % / 100 % by year after completion; capex
spent evenly over duration; rooms out of service earn nothing during works; earliest
start 2027; horizon 2032; USD. **Read these from the table in DAX, never retype.**

**FinanceAssumptions** (21; region × 2026-2032): `MarketDemandGrowthPct` (NA 2.0 → 1.7 %,
EU 1.8 → 1.5 %, APAC 3.2 → 2.9 %), `ADRInflationPct` (2.0-2.8 %), `CostInflationPct`
(2.7-3.4 %). Cumulative NA 2026-32: demand +13.7 %, ADR +17.7 %, cost +23.4 %. Cost
inflation beats ADR inflation every year in every region: the organisers built margin
erosion into the baseline. The only table that lets you project a no-investment 2032
(label it as scenario logic).

### B5 · Traps and conventions (write them into the metric contracts)

1. 2021 is a COVID-shaped base year; trend claims use 2022/2023 → 2025.
2. Weighted scores only (SurveyResponses); an unweighted AVERAGE of NPS is wrong.
3. NPS is already a net score (−100…100), not a 0-10 score; do not average it with the
   others or format it as a percentage.
4. Late openers (GI Valencia 2023, Porto 2022; PS Melbourne, Warsaw) distort growth
   rates; use like-for-like sets.
5. Six GI hotels have no renovation date; product age = years since opening.
6. DistributionCost sits outside MonthlyPerformance opex per the workbook's Contents sheet
   ("excludes distribution costs", as read by the Dutch review of 4 Nov; confirm): show the
   margin before and after commissions (44.4 % / 33.7 %); after commissions P&K Select leads.
7. Impacts are in 2025 dollars; the baseline in FinanceAssumptions is nominal. Never mix
   on one axis without saying so.
8. Portfolio Low/High = sum of each project's Low/High; never mix scenarios across
   projects on one line.
9. `Scenario` is a disconnected table; `InvestmentProjectProperties` has no row for new
   hotels; `DependsOn`/`ExclusiveWith` are text, parse them.
10. Hidden tooltip pages are allowed; any other hidden page risks the two-page rule.

### B6 · What is **not** in the data (do not fabricate)

Daily rates or lead times, cancellations, market/competitor data (RevPAR index), app or
loyalty member counts, marketing spend, staff headcount, energy in kWh, booking
sources below channel, review text, financing, tax, depreciation, cash, a terminal value
beyond 2032, and any demand figure that is not the FinanceAssumptions growth rate.
Real-world hospitality knowledge may appear as narrative, never as a number.

### B7 · Idea seeds beyond the three directions (Goodnight Inn, each one chart)

1. **The $4.8 M middleman tax** — distribution cost at actual vs 2021 mix, one bar pair.
2. **Same room, two bills** — OTA vs direct guest: same $109, $90 vs $107 kept.
3. **Half of every hotel** — OTA share is 49-51 % at all 50 hotels: a dot strip with no
   spread is itself the insight (policy, not place).
4. **Business travellers at a budget brand** — segment 20 % → 24 %, booked through OTAs
   while corporate contracts shrink: a slope chart of segment vs channel share.
5. **The scissors** — revenue vs cost per occupied room, indexed, crossing in 2025.
6. **The template brand** — hotel GOP margins all within 43.5-45.5 %: a strip plot that
   says cost discipline is not the problem, volume and rate are.
7. **Age vs welcome** — NPS by years since refresh, three buckets, with the 2021 cohort
   as the control group.
8. **The twelve** — the hotels guests would not recommend, eight of them in the refresh
   list: a ranked bar with the project badge.
9. **Full means full** — Gatwick, Toronto, Montréal months ≥ 90 %: a 24-month heat strip.
10. **The capacity wall** — organisers' demand growth vs rooms: first capped year per
    hotel (2028-2032), the growth case for extensions, dated.
11. **Check-in is the fastest-rising complaint** (+25 %) — the kiosk case in one line.
12. **Energy already fell** — 5.9 % → 4.9 % of revenue without capex: why GI-03 waits.
13. **Kingston** — 61 % occupancy, Low case negative: the hotel to leave alone (or
    the polite question nobody funded: exit?).
14. **Risk shape of the plan** — Low-High spread per project: digital swings, bricks
    don't; a dumbbell chart.
15. **Payback after the horizon** — cumulative net per project to 2032 and the year it
    crosses zero: honesty as a chart.
16. **What $60 M buys per room** — GI's budget per room ($9.3 k) vs the sister brands
    ($11-35 k): the Board gave the cheapest brand the least, so choose harder.
17. **Seasonality by hotel type** — airport flat, highway H2 dip: where RMS pays.
18. **Rooms in service** — RoomsAvailable dips reveal past renovations without the
    Renovations table; a validation chart for the trust path.
