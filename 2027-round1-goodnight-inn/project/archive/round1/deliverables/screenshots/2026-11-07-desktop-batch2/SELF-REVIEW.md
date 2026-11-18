# Self-review, batch 2 (7 Nov 2026)

Written by the builder (Claude Code), not an independent reviewer. This file:
- checks every item of `project/project-state/active/07-fixgids-review-v2.md` against the batch-2 renders in this
  folder;
- lists what I found myself while looking at them;
- lists what is still open.

It is written so the next independent review can check each claim against a screenshot. File numbers refer to this
folder.

Status words: **fixed** = visible in the renders and checked in the model; **partly** = improved, with a stated rest;
**open** = not done in this round.

## The seven errors (F1-F7)

| # | Item (REVIEW id) | Status | Where to see it | What changed |
|---|---|---|---|---|
| F1 | B in Low broke the plan, with a false payback year (B1) | **fixed** | 13, 15 | A, B and C are fixed packages now (K1), so B has a package in every scenario: 01+09+10, NPV -$6.9M in Low. Plan Risk is guarded against an empty package anyway: no "+M", no invented year. |
| F2 | "Fund the three moves that pay" contradicted by the kiosks (M3) | **fixed** | 02, 03, 04 | Headline: "Fund one package of three moves: $9.4M now, $50.6M held back." Under the numbers: "On their own the kiosks at 20 desks return -$0.6M by 2032; they stay as the cheapest answer to F3." The not-funded reason is now the one the selection applies ("A has the highest NPV of all packages in the Expected case, so adding any of them lowers it"). Outside Expected the subtitle adds "the recommendation is set on the Expected case". |
| F3 | C had two Low NPVs, -$34.8M and -$34.5M (M6) | **fixed** | 03, 12, 14, 16 | C is 01+07+10 in every scenario; its Low NPV is -$34.8M in the risk line, on the landing and in plan C Low. |
| F4 | Parts did not add up to totals (M8) | **fixed**, with one trade-off | 08-14, 01 | Capex to two decimals where needed ($24.75M, $4.25M, $11.65M), so the $60M budget can never read as $60.1M. NPV and profit-a-year parts are rounded to $0.1M by largest remainder, so the waterfall bars and table rows add up to the shown package total; checked in the model for 9 combinations. The folio's "keeps" is the difference of the two shown amounts ($89.63 / $107.10). The KPI change is computed from the shown values (-2.8 pt, matching F1's 36.5% to 33.7%). See the trade-off under N1. |
| F5 | Two number formats side by side (M7) | **partly** | 01, 08 | Every card, KPI value, folio cell and plan-table cell is DAX text now, from one formatter, so a card can no longer mix formats. Charts still format their own labels (waterfall, F3, F4 bars); in this nl-NL Desktop those show "+$3,4M", "+6,8", "91,9%" and "Totaal". See N2: this needs the Publish-to-Web check. |
| F6 | The Back label disappeared on hover (M1) | **fixed** | L2b, L3c, L4b | Hover and pressed states are set on both buttons: Back gets plum-black text on the seam grey, Open gets white text on plum. Theme colours only (`pbir_detect` passes). |
| F7 | P1 headline overclaimed (M4) | **fixed** | 01 | "Full rooms, a slipping margin: Goodnight Inn pays the middleman, and its welcome is fading." |

## Risks (R1-R6)

| # | Item | Status | Where | Notes |
|---|---|---|---|---|
| R1 | Scatter: heavy cloud, B/C hidden, $60M dots clipped, selection stuck (M2, m7) | **fixed** | 02, 06, 07, 16, L4a-c | The cloud is lighter and smaller (kit lilac). A, B and C are drawn on top with their letters. The capex axis runs to $62M, so no dot is cut. Clicking A leaves no dimmed state after the round trip (L4c). How it works is under N3. |
| R2 | Cumulative chart could not show the payback years (M9) | **fixed** | 08-14 | Years 2027-2032, a zero line, Low / Expected / High named at the line ends, and the scenario in view drawn in raspberry. The chart is taller now that the zero ops tiles became one text line. |
| R3 | Codes in board text, "Funded" under B and C (M5) | **fixed** | 11-14, L3a | Plan titles read "Package B (considered, not recommended): $11.65M on 3 initiatives, ...". The dropdown has three named entries only: "A · Our recommendation", "B · Breakfast instead of kiosks", "C · Refresh instead of kiosks". Under B and C the status reads Included / Excluded. |
| R4 | Legibility at 1366 (M10) | **open** | all | The minimum text is still 10 pt (13 px at 1920, about 9 px at 1366). Not changed in this round. |
| R5 | Rule compliance invisible (M11) | **fixed** | 02, 08 | Landing line: "Within the rules: 3 initiatives, 2 of them growth (booking app and revenue management), $9.4M of the $60.0M budget, impact counted through 2032." The plan table has a Type column with "Growth". |
| R6 | Publish to Web not tested | **open** (needs Björn) | | The P2W link must be tested in an nl-NL and an en-US browser; that settles N2. Visual header icons (p10) were already off on every visual in batch 1 (`visualHeader` show=false through `pbir_lib.vco`); the icons in the screenshots are Desktop's edit-mode chrome, which the P2W test confirms. |

## Polish (S1-S11)

| # | Item | Status | Notes |
|---|---|---|---|
| S1 | Scenario tiles in default style (m10) | **open** | Still the classic slicer tiles; the selected tile is the default dark grey. |
| S2 | Truncated dropdown labels (m1) | **fixed** | Short labels (see R3). |
| S3 | Tables: sort arrows, header alignment, row order, emphasis (m5) | **partly** | Numeric headers are right-aligned. The plan table sorts the package first, then by NPV, through a key inside the chip column, so its sort arrow now sits under the blank chip header. The folio's arrow is gone. Not done: a bold "Goodnight Inn keeps" row. |
| S4 | F2 legend of three identical grey dots (m3) | **fixed** | The line ends carry the brand names (01). |
| S5 | F3: no zero line, wrapping labels, 44 of 50 (m4, m8) | **fixed** | Zero line, one-line band labels, and the note says "Bands of 14, 20 and 10 hotels; 6 of the 50 were never renovated." |
| S6 | Zero ops tiles (p9) | **fixed** | One line, e.g. "In the hotels: 1,180 rooms refreshed, a guest-score effect in 10 hotels". |
| S7 | Waterfall details (m6) | **fixed** | The scenario is in the title, labels sit outside the bars, and zero reads "$0.0M" without a sign (10, the kiosks in High). "Totaal" remains (N2). |
| S8 | Focus change hardly visible (m2) | **fixed** | A focus line under the dropdown ("In focus: C · Refresh instead of kiosks · $36.9M · NPV -$23.4M (Expected)"), and the button names the package ("Open the plan for package C"), L3b/L3d. |
| S9 | Names drift (m9) | **fixed** | Not-funded uses the table names ("Toronto +40 rooms"); "profit a year" on the landing, "Profit/yr" in the table header. |
| S10 | Which 20 hotels get kiosks; what $50.6M is held back for (m11) | **open** | Not answered: the model has the hotel list, but the copy is not written. |
| S11 | Smaller polish (p2-p8) | **partly** | Done: both headers sit on one grid (P1 headline and subtitle are cards like P2's); no rank arrows in the KPI band; F1 axis 30-50%; footer text. Not done: an F4 caption and baseline. |

## Opportunities (K1-K6) and the new switch

- **K1:** done. A, B and C are fixed packages in `Package[Preset]`, picked by their rules on the Expected case.
- **K2:** done in part. The dropdown is cut to A, B and C and the zero tiles are gone. The table still lists all ten
  initiatives.
- **K3:** done (R1).
- **K4:** done. Every change is in `sketch_model.py`, `opzet_report.py` and `opzet-layout.json`; nothing was edited
  in Desktop.
- **K5:** open (R6).
- **K6:** this batch.
- **New (Björn, 7 Nov):** a scatter switch "All packages | Zoom on A, B, C", default all, built natively (a
  disconnected slicer drives the axis ends through measures; no Deneb, no HTML, no extra bookmark state). The zoom
  range comes from the data: A, B and C over all three scenarios, rounded out to $10M ($0-40M by -$40M to +$20M).
  The scenario switch still never rescales the axes. Renders 07 and 16; live L5a/L5b.

## What I found myself (for the next review)

- **N1. Rounding trade-off.** Because the parts of each package add up to its total, one initiative can show a
  different rounded value in another package's plan:
  - the booking app's profit a year is +$2.3M in A and +$2.4M in B and C;
  - the breakfast upgrade's NPV is -$1.1M in A's table and -$1.2M inside B (11 against 08).

  The footer says "In the plan, parts are rounded so they add up to the package total." The alternative is two
  decimals in the plan table and waterfall: exact, but busier.
- **N2. Locale.** Chart labels follow the viewer's locale; DAX text follows the model culture in Desktop (en-US). I
  expect the service to use the viewer's locale for both, but have not verified it. If DAX stays en-US there, a nl-NL
  viewer still sees commas in charts beside points in text; the cards themselves stay consistent. The waterfall's
  total label is localised by Power BI ("Total" / "Totaal") and has no rename option. Only the P2W test (R6) settles
  this.
- **N3. The scatter is two layers.** Power BI draws larger markers first, so small cloud dots always landed on top of
  B and C, whatever the data order. A colour with alpha (#RRGGBBAA) is not honoured. So the cloud is one scatter and
  A, B and C a second, transparent one on top with the same axis measures, same size and labels, and no gridlines.
  - Cost: the top layer catches the mouse, so the 453 cloud dots show no tooltip. A, B and C do.
  - Watch for: any change to one layer's axis or size that is not made to the other would misalign them.
    `opzet_report.py` builds the second layer as a copy of the first for that reason.
- **N4. Duplication when A is in focus.** The focus line ("In focus: A · Our recommendation · $9.4M · NPV +$3.3M")
  repeats the block below it. It earns its place when B or C is in focus. It could be shown only then.
- **N5. Landing rhythm.** The gap above "Read with care" is smaller but still there (02, 03).
- **N6. Cumulative chart.** The raspberry line is the scenario in view; only the alt text says so, the title does not.
  Its line-end label is hidden, so the label of its grey twin names it.
- **N7. Live testing in edit mode** (process, not report). A bookmark that hides the button under the cursor left
  Desktop in a drag; the next mouse move dragged the selected visual. The click runner now releases again and presses
  Escape after every click, and every sequence starts from a fresh reload. The repo files were never affected: the
  runs used a throwaway copy, deleted afterwards.
