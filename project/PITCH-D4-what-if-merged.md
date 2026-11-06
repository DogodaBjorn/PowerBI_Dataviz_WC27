# D4 · "What if" — Two futures, one plan (merged direction, for a second opinion)

Written 2026-11-06 at Björn's request: take the what-if direction (D3 *Two futures*)
as the basis and fold in what the other two directions (D1 *Wake-up call*, D2 *Fifty
keys*) and the Dutch review contribute where it makes sense, inside the contest's
two-page rule (`contest/page-count-ruling.md`). This document is self-contained so
that a reviewer can judge it without reading the rest of the repository; the three
original directions are in `PITCH-goodnight-inn-directions.md` and the browsable
pitch page, the evidence behind every number in `MISSION-goodnight-inn.md` §2 and
`research/2026-11-05-crosscheck-dutch-review.md`.

---

## For the reviewer: what we want a second opinion on

1. **Is the merge better than the best single direction?** D1 scored highest on the
   atelier's seven passes (50/70); D4 below scores 48 by my own count. The trade is
   analytical completeness and interactivity against density. Is that the right trade
   for a jury that scores Insightfulness, Visual Effectiveness, Creativity &
   Innovation, Accessibility (Official Rules) plus Analytical Quality (starter file)?
2. **Does the do-nothing projection survive the "no fabricated or simulated data"
   rule?** It is built only from the organisers' `FinanceAssumptions` table and
   labelled as scenario logic on the canvas. A judge could still read it as
   simulation. Keep it as the page-1 hero, demote it to the method overlay, or drop
   it?
3. **Density.** Page 1 carries a fan, a bridge and three driver blocks; page 2 a
   builder, a reacting fan, a ledger and two text panels. Which element would you cut
   first? (My delete-test answer is at the end.)
4. **Look.** D4 proposes D1's paper surface in two built-in families (Georgia, Segoe
   UI). Would D3's cream ledger or D2's night desk serve the what-if frame better?
5. **The plan itself.** Plan A ($51.3 M, six projects) vs the review's package (plan A
   plus breakfast, $55.6 M). Reserve or spend?

Write the answer anywhere convenient — a reply in the PR, a comment in this file, or
a new file in `project/research/` — and the lifecycle picks it up at stage 5.

---

## 1 · The story, rewritten

**Where we stand.** Goodnight Inn looks like Pillow & Key's best business: the
highest occupancy of the four brands (79.4 %) and the highest reported margin
(44.4 %). Counted after the commissions it pays to be booked, the margin is 33.7 %,
and P&K Select leads the group. The brand has stopped growing — occupancy has been
pinned at 79 % for three years, revenue rose 0.8 % in 2025 while cost per occupied
room rose 3.5 %, and profit fell at every one of the 50 hotels. Half of room revenue
now arrives through online travel agencies at 18 %, up from a third in 2021; at the
2021 mix the brand would keep $4.8 M more a year. Guests have noticed: value for money
is the lowest in the group at the brand whose promise is value, room comfort tracks
years since a refresh almost perfectly (r = −0.92), room-condition complaints are the
only kind still rising, and NPS has fallen at 45 of 48 hotels. The cause is on the
Board's own books: $0.98 M of renovation per hotel since 2018 against $6–8 M at the
sister brands, and nothing started since 2020. Meanwhile the airport hotels are full.

**What if we do nothing.** On the organisers' own assumptions the market is kind:
demand grows 14 % by 2032 and fills the rooms to 90 %. But cost inflation outruns
price inflation every year in every region, so the margin thins from 44.4 % to
41.7 %, the OTA drift keeps taking a larger share of a larger revenue, and eight
hotels run out of rooms — Toronto in 2028, Montréal in 2029, Gatwick in 2030. Doing
nothing is not standing still; it is growing thinner and turning guests away.

**What if we do this.** Three moves for $51.3 M of the $60 M. *Buy the guest back*:
the booking app, revenue management and self check-in ($9.4 M) — the app alone
recovers a seventh of the OTA commission and pays back by 2030. *Fix the welcome*:
refresh the ten oldest hotels ($29.5 M), the eight-year catch-up the brand never got,
with the sister brands' own renovations as proof it works (comfort +1 point,
room-condition complaints down a third or more). *Build where we're full*: forty rooms
each at Gatwick and Toronto ($12.4 M), the two hotels that hit the wall first. By 2032
operating profit runs $7.6 M a year higher (Low $3.8 M, High $11.4 M); inside the
horizon the capital projects have not yet paid back, and we say so. We also show the
route that spends exactly $60.0 M without touching a room, and the Boston hotel that
would take 41 % of the budget to open in 2029, and say why not.

## 2 · The stance

**Organizing concept.** The Board decides by asking *what if*. Page 1 answers *what if
we do nothing* (today, and the organisers' assumptions carried to 2032) with the
three findings as the drivers of that path. Page 2 answers *what if we do this* with a
plan the Board can change under its own eyes: tick projects, switch Low / Expected /
High, watch the future move. The projection frame is D3's; the diagnosis is D1's; the
hotel-level proof (capacity wall, the ten oldest, the wall itself as a tooltip) is
D2's; the margin-after-commissions, the renovation history and the event study come
from the Dutch review.

**Unit of analysis.** The year, anchored on the hotel wherever a decision is local.

**Signature moment.** The fan that reacts: tick a project in the builder and the
funded band on the two-futures chart moves. "What if" made physical. The folio (same
$109 night, $90 vs $107 kept) travels along as the quotable detail.

**Look.** D1's paper-white surface, navy ink and a single amber accent (no second
hue: the canon audit flagged D1's blue as a second accent, so channel lines use ink
and greys). Two families only, both built into Power BI and present on the service:
Georgia for headlines and hero numbers, Segoe UI for everything else, with tabular
figures in the ledger and the builder (the audit notes Consolas is absent on macOS
under Publish-to-Web, so D3's typewriter numerals do not travel). Body text floor
12 pt. Density *balanced*, variance *strict*. Reason: a fan chart reads best on a
light surface, the serif keeps a finance frame from looking like a generic deck, and
the light surface keeps the accessibility floor high. Stage 5 still renders the looks
as comps; this is the recommendation.

## 3 · Page 1 — Brand Review: "Where we stand, and where this is heading"

3-second message: *the market will fill our rooms; it will not protect our margin or
our welcome.*

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ GOODNIGHT INN · BRAND REVIEW 2021–2025 AND THE DO-NOTHING PATH TO 2032 · for the Board│
│ The market will fill our rooms. It will not protect our margin, or our welcome.      │
├──────────────┬──────────────┬──────────────────┬──────────────┬──────────────────────┤
│ Occupancy        │ Margin before / after commissions │ NPS           │ Value for money  │
│ 79.4% · flat 3 y │ 44.4% ▼1.7 pt  ·  33.7% ▼2.8 pt   │ +3.3 ▼5.2 '21 │ 7.66 lowest of 4 │
├──────────────┴──────────────┴──────────────────┴──────────────┴──────────────────────┤
│ WHAT IF WE DO NOTHING (the one hero)                    │ WHAT 2032 IS MADE OF       │
│ Operating margin 2021–2032: actual, then the projection │ four figures, no chart:    │
│ from the provided assumptions (fan); annotations on the │ demand +27.7 · price +41.7 │
│ fan: "cost inflation outruns ADR inflation", "OTA share │ cost of volume −15.4 ·     │
│ 33 → 50%", "8 hotels out of rooms by 2032"              │ cost inflation −30.7       │
│ [scenario logic · provided FinanceAssumptions]          │ = $117.7 M at 41.7%        │
├─────────────────────────┬───────────────────────────────┼────────────────────────────┤
│ THE MIDDLEMAN           │ THE FADING WELCOME            │ WHERE WE'RE FULL           │
│ channel share of room   │ room comfort vs years since   │ capacity wall: first year  │
│ revenue 2021–25 (area,  │ refresh, 50 hotels (dot strip,│ demand passes the rooms,   │
│ OTA on the baseline,    │ r = −0.92); renovation spend  │ 8 hotels (bars): Toronto   │
│ 33 → 50%); the folio:   │ per hotel since 2018: $1.0 M  │ 2028, Montréal 2029,       │
│ $109 → $90 vs $107 kept;│ vs $6–8 M (bar); hover a      │ Gatwick 2030 …; Kingston   │
│ "$4.8 M at the 2021 mix"│ bucket → tooltip page lists   │ 61% as the counter-example │
│                         │ the hotels (D2's wall)        │                            │
├─────────────────────────┴───────────────────────────────┴────────────────────────────┤
│ Data: Pillow & Key Group dataset · scores weighted by responses · 2026–2032 marks are │
│ scenario logic from the provided FinanceAssumptions · margin after commissions assumes│
│ performance costs exclude distribution cost (workbook Contents sheet)                 │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

Visuals by intent (chart-grounding): four KPI cards with reference labels (magnitude);
line into fan (change over time with labelled uncertainty), the only hero; four
figures for the bridge (a sentence beats a truncated waterfall, audit B3); stacked
area with OTA on the baseline (part-to-whole over time) and one annotation; table
styled as a receipt (detail lookup); dot strip (distribution, items findable) with a
reference line and the renovation-spend bar beside it; sorted bars (ranking: first
capped year). Core visuals on this page: 8, inside the audit's budget of nine
elements; copy budget 180 words. The page tab keeps the organisers' name *The Brand
Review*; the editorial title and the brand name live in the masthead.

Tooltip pages (hidden, allowed): *hotel wall* — the 50-hotel list sorted by comfort
with occupancy bar, NPS chip, years since refresh and the GI-07 badge, shown when
hovering a bucket of the dot strip or a bar of the capacity wall; *definitions* —
each KPI's contract line.

## 4 · Page 2 — Investment Strategy: "What if we do this"

3-second message: *$51 M of $60 M on three moves lifts 2032 profit $7.6 M a year
against a baseline that is thinning; here is what else we could do, and why we
don't.*

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ WHAT IF WE DO THIS · 2027–2032                 Low · [Expected] · High   [Our plan ↺] │
│ $51.3 M of $60 M on 6 projects: +$7.6 M a year of operating profit by 2032 (Expected)│
├──────────────────────────┬───────────────────────────────────┬───────────────────────┤
│ BUILD THE PLAN           │ TWO FUTURES                       │ THE LEDGER            │
│ Buy the guest back       │ operating profit 2025–2032:       │ initiative · capex ·  │
│  ☑ app $5.0 ☑ RMS $2.4  │ actual, do-nothing (grey), with   │ return/yr · payback · │
│  ☑ kiosks $2.0 (needs app)│ the selected plan (amber) and its│ satisfaction pts ·    │
│                          │ band = sum of each project's Low  │ answers P1 finding    │
│                          │ and High (stated once, on canvas) │ · live date           │
│ Fix the welcome          │ Low–High band; the dip in 2027–28 │ app 5.0 Oct-27 +2.35  │
│  ☑ refresh 10 oldest 29.5│ is capex and rooms out of service │  5.8 2030             │
│ Build where we're full   │ ┌─ impact strip ─────────────────┐│ RMS 2.4 Jul-27 +0.77 │
│  ☑ Gatwick 6.6 ☑ Toronto │ │ +$7.6 M/yr · +8% on 2025 GOP · ││  1.3 2031            │
│    5.8                   │ │ −$25.3 M cum. to 2032 · NPV −29.5││ … not-funded rows    │
│ Also on the table        │ │ · +80 rooms · 1,180 refreshed  ││ greyed with the one  │
│  ☐ breakfast ☐ energy    │ └────────────────────────────────┘│ number that killed   │
│  ☐ Kingston  ☐ Boston    │                                   │ them                  │
│ ████████░░ $51.3 of $60 M│                                   │                       │
│ ● 6 projects ● 4 growth  │                                   │                       │
│ ● dependencies met       │                                   │                       │
├──────────────────────────┴─────────────────┬─────────────────┴───────────────────────┤
│ NOT FUNDED, AND WHY                        │ RISKS & TRADE-OFFS                      │
│ Boston: 41% of budget, opens 2029 · Kingston│ rooms vs kilowatts · 15% of 1,180 rooms │
│ 61% occupancy, Low case loses · Energy: 8.5-│ out for 14 months · app adoption is the │
│ yr payback · the $60.0 M route that funds  │ swing (Low 0.6 / High 4.1) · capital    │
│ everything except a room                   │ projects pay back after the horizon  [ⓘ]│
└────────────────────────────────────────────┴─────────────────────────────────────────┘
```

The headline sentence, the impact strip and the fan are measure-driven: they read the
builder's selection and the scenario slicer (`Headline Plan (text)` exists in the
sketch model). The ledger carries, per initiative, what the contest requires on the
canvas (audit compliance item 6): capex, the annual operating-profit return, the
payback year, the satisfaction points from `InvestmentScenarios[SatisfactionChangePts]`
as the operational impact, and the Page 1 finding it answers (a column on
`InvestmentProjects`). The band's meaning is printed once beside the fan (audit B7).
Scenario switching keeps its format strings (DC-056). Page tab name *The Investment
Strategy*; brand name in the masthead. Core visuals on this page: 7 plus the
builder's slicers. The ⓘ opens a bookmark overlay (same page) with the method:
FinanceParameters rules, the counterfactual, both valuation conventions (constant
2025 dollars per the dataset, nominal with FinanceAssumptions — same ranking), the
disruption convention. Tooltip page: *project card* — hotels, drivers, Low / Expected /
High, dependency — on hover of a builder row or a ledger row.

## 5 · The what-if mechanics (all native, all Publish-to-Web safe)

| Mechanic | How | Already in the sketch model (`project/pbip/PillowKey.SemanticModel`)? | Allowed by |
|---|---|---|---|
| Do-nothing baseline 2025–2032 | calculated table hotel × year: 2025 actuals × cumulative regional demand growth (capped at 97 % occupancy), ADR inflation, cost inflation from `FinanceAssumptions` | **yes**: `HotelOutlook`, measures `Baseline GOP Margin %`, `Margin Baseline (timeline)`, `First Capped Year`, `Unmet Room Nights` | "calculated tables"; labelled scenario logic |
| Project cash flows | calculated table project × scenario × month: capex phased, disruption, ramped benefit, from `FinanceParameters` | **yes**: `ProjectCashflow`, measures `Capex Phased`, `Disruption`, `Benefit (ramped)`, `Net Impact`, `Cumulative Net Impact`, `2032 Run-rate`, `NPV @ 8%`, `Payback Year` (each with Low/High variants) | "calculated tables" |
| Plan selection | slicer on `InvestmentProjects[Short Name]` (multi-select), bookmark "Our plan" resets to plan A; budget, counts, dependency lamp | **yes**: `Capex Selected`, `Budget Used %`, `Projects Selected`, `Growth Initiatives Selected`, `Plan Valid (text)`, `Rooms Added`, `Rooms Refreshed` | slicers, bookmarks |
| Scenario switch | slicer on the disconnected `Scenario` table, applied as a column filter on `ProjectCashflow[Scenario]`; Expected when nothing is selected | **yes**: `Selected Scenario` | "scenario parameters" |
| Reacting fan | line chart on `Timeline` with actual, baseline, plan, Low, High | **yes**: `GOP Baseline (timeline)`, `GOP Plan (timeline)`, `GOP Plan (timeline, Low)`, `GOP Plan (timeline, High)` | native |
| Headline that talks back | text measure bound to the title | **yes**: `Headline Plan (text)` | native |
| The welcome block | comfort vs refresh age; renovation spend per hotel | **yes**: `Room Comfort (weighted)`, `Refresh Age`, `Renovation Spend per Hotel since 2018` | native |
| The folio | receipt table | **yes**: `FolioLine`, `Folio OTA Guest`, `Folio Direct Guest` | native |
| Start delay (optional) | numeric what-if parameter, months; shifts the cash-flow months in measures | no | "scenario parameters" — only if the measures stay simple |
| Still to add for D4 | `Satisfaction Points Selected` (sum of `SatisfactionChangePts` over the selected plan), `Band Meaning (text)`, a `P1 Finding` column on `InvestmentProjects`, dynamic format strings if the scenario switch moves to a calculation group | no — three small objects | model work at stage 3/4 |

Everything left of the line "2025 actual" is data; everything right of it is labelled
projection; impacts stay in 2025 dollars as `FinanceParameters` prescribes.

### Sketching D4 on the existing generator

`project/tools/sketch_reports.py` already builds every block D4 needs. A `build_d4()`
would reuse, from `build_d3()`, `hero_margin_fan` (page 1 hero) and
`hero_op_vs_baseline` + `tbl_ledger` (page 2); from `build_d1()`, `ch_channel_mix`
(with OTA moved to the baseline), `ch_comfort_vs_age`, `folio_table` and the plan
builder slicer with `ch_budget_bar`; from `build_d3()` again, `tbl_capacity_wall` as
the "where we're full" block. Only the four bridge figures (cards on `BridgeStep`),
the renovation-spend bar and the ledger's three new columns are new. That is a
half-day sketch, which is the cheapest way to let a reviewer compare D4 with D1–D3
on the same screen before stage 5 renders comps.

## 6 · What D4 keeps, borrows and drops

| From | Kept on a visible page | Moved to a tooltip page / overlay | Dropped |
|---|---|---|---|
| D1 Wake-up call | the three driver blocks (compressed), the folio, the plan builder, "not funded and why", the KPI band, the look | the complaints lines (room-condition momentum stays as a number) | the departures board (the ledger replaces it) |
| D2 Fifty keys | the capacity wall, the ten-oldest evidence inside the welcome block | the 50-hotel wall (tooltip on the dot strip), the year-by-year re-lighting (not kept) | the night surface, the quadrant scatter |
| D3 Two futures | the fan (both pages), the 2032 bridge, the ledger, both valuation conventions | the assumptions table (overlay) | the cream ledger look |
| Dutch review | margin after commissions, renovation spend per hotel, event-study proof, value-for-money, the $60.0 M foil | the sister-brand flip (tooltip on the margin card) | its five-page sequence (two-page rule) |

## 7 · Critique — the seven passes, D4 against the originals

| Pass | D1 | D2 | D3 | **D4** | D4 gap and how to close it |
|---|---|---|---|---|---|
| 1 Reading path | 8 | 6 | 7 | **7** | page 1 has two heroes (fan, bridge) over three blocks; the headline must do the work and the bridge may need to shrink to a figure column |
| 2 State coverage | 7 | 6 | 7 | **7** | builder empty state; scenario cleared → Expected via bookmark; tooltip pages with no hover context |
| 3 Slop risk | 6 | 8 | 5 | **6** | fan + KPI band + ledger is the finance-deck pattern; the folio, the renovation-spend bar and the editorial type are the defence |
| 4 Brand alignment | 7 | 8 | 6 | **7** | paper, folio, lamp amber; nothing of the night desk survives |
| 5 Accessibility | 8 | 6 | 7 | **7** | bands need labels; many interactive elements → tab order designed, not inherited; tooltip pages carry alt text |
| 6 Dial fit | 7 | 6 | 8 | **6** | "balanced" is under the most pressure of the four; the delete test (below) is mandatory |
| 7 Signature strength | 7 | 9 | 8 | **8** | the reacting fan is the direction's own and native |
| **Total** | **50** | **49** | **48** | **48** | |

Honest reading: D4 buys the strongest Analytical Quality and Creativity story of the
four (projection + reacting plan) and pays for it in density and reading path. It is
not better than D1 on the scoreboard; it is better on the two criteria where entries
differentiate at the finale. That is a judgment call, which is why this document
exists.

**Against the canon audit** (`project-state/active/00-best-in-class-audit.md`, 17/40
on the pitch comp). D4 is designed to answer its must-change list rather than inherit
it: one margin definition on the card with both numbers (item 1); one hero per page,
the bridge demoted to figures, a nine-element and 180-word budget (item 3); no
truncated waterfall, OTA on the baseline, no index line (item 4); cost, return,
payback, satisfaction points and the P1 finding per initiative on the canvas (item 6);
the headline as a measure (item 7); the band's meaning stated once (item 9); the brand
name and the organisers' page names in the chrome (item 10). Items 2 (canvas and
fonts in the comp), 5 (AA palette, alt text and tab order as design inputs) and 8
(format strings on the scenario switch) are stage-5 and stage-3/4 work whichever
direction is chosen. The audit's open question "does the do-nothing baseline go on
the canvas?" is the one D4 answers with yes, labelled, as the page-1 hero, and the
one the reviewer is asked to judge (question 2).

**Delete test, in order:** (1) the 2032 bridge on page 1 → becomes four figures beside
the fan; (2) the complaints chart (already a tooltip); (3) the KPI band's fifth card
(value for money → a sentence under the headline); (4) the ledger's not-funded rows →
the "not funded" panel alone. After (1) the page reads as one hero, three drivers,
one strip.

**Fidelity checklist (if D4 is chosen):** the fan on both pages with the projection
label on the canvas; the builder that moves the fan; the folio with real channel
figures; the renovation-spend bar beside the comfort strip; the ledger in typewriter
figures; one amber accent, one story series per visual; two visible pages and tooltip
pages only.

## 8 · Risks

- **Honesty optics.** The projection must carry its label on the canvas, every time,
  including in the tooltip pages; impacts stay in 2025 dollars. A reviewer's view on
  question 2 above decides whether the fan stays the page-1 hero.
- **Two mechanics on one page.** Builder + scenario + reacting fan is more DAX surface
  than any single direction; it is all native and tested on Publish-to-Web in the
  first build day, not the last.
- **Density.** The delete test is applied before the comp is approved, not after.
- **The Contents-sheet wording.** The after-commissions margin rests on one sentence in
  the workbook; confirm it or label the card "assumes performance costs exclude
  distribution cost".

## 9 · Open decisions

| Decision | Default if deferred |
|---|---|
| D4 vs D1 (or D1 with D3's fan only, the earlier recommendation) | stage 5 renders D1 and D4 as comps and the critique decides |
| Fan as page-1 hero, or in the overlay | hero, labelled |
| Breakfast in ($55.6 M) or reserve ($51.3 M) | reserve |
| Disruption convention | full revenue loss, sensitivity stated |
| Start-delay what-if parameter | no |
