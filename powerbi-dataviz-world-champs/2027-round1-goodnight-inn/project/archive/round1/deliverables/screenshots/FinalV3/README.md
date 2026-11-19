# FinalV3 render set · GoodnightInn-opzet (14 Nov 2026, build step 11 of doc 23)

Renders of `project/pbip/GoodnightInn-opzet.pbip` on the **submission model** (333 measures, 29 tables; commit
`14163ef` and later on `rebuild-finalv3`). Power BI Desktop 2.159, Windows culture nl-NL, a throwaway copy of the
project (the project itself was not opened). Every page render has its comp view beside it in `comp/` under the same
file name: `project/design-prototypes/rebuild-comp-v10.html` at the same state, scenario and picked moves.

## What to look at first

1. **03** (Recommended, Expected) next to `comp/03`: this is the page a judge opens after page 1.
2. **02 and 04** (Low and High): the headline, the hero title, the four numbers, the ledger's status words and the
   thick line of the chart follow the case.
3. **07** (What waits, High): the longest text of the three cases; the table still ends above the card's edge.
4. **09 and 10** (Build with six moves, and over the budget): the bars, the alarm band, the Tangerine line.
5. **16** (the package tooltip with eight moves): the tallest tooltip, 616 px.
6. The nine open questions in doc 23. Each "Outside 2 px" line below names the question it belongs to.

## The renders

| File | View | Comp view (`comp/`, same name) |
|---|---|---|
| `01_p1-brand-review.png` | Page 1, The Brand Review, as it opens | `#p1` |
| `02_p2-recommended-low.png` | Page 2, Recommended: A, Low case | `#rec`, Low |
| `03_p2-recommended-expected.png` | Page 2, Recommended: A, Expected case (the opening state) | `#rec`, Expected |
| `04_p2-recommended-high.png` | Page 2, Recommended: A, High case | `#rec`, High |
| `05_p2-what-waits-low.png` | Page 2, What waits, and why, Low | `#alts`, Low |
| `06_p2-what-waits-expected.png` | Page 2, What waits, and why, Expected | `#alts`, Expected |
| `07_p2-what-waits-high.png` | Page 2, What waits, and why, High | `#alts`, High |
| `08_p2-build-opening-package-a.png` | Page 2, Build your own as it opens: package A picked, Expected | `#build`, Expected |
| `09_p2-build-filled-six-moves.png` | Build your own, six moves picked ($26.1M), Expected | `#build`, the same six moves |
| `10_p2-build-over-budget.png` | Build your own, Energy + Refresh + Boston ($69.3M), Expected | `#build`, the same three moves |
| `11_p2-build-nothing-picked.png` | Build your own, nothing picked (the empty state) | `#build`, nothing picked |
| `12_tt-package-a-expected.png` | Package tooltip on A, Expected | none (the comp has no tooltips; doc 21 section 9) |
| `13_tt-package-a-low.png` | Package tooltip on A, Low | none |
| `14_tt-package-b-expected.png` | Package tooltip on B | none |
| `15_tt-package-c-expected.png` | Package tooltip on C | none |
| `16_tt-package-eight-moves.png` | Package tooltip on a package of eight moves | none |
| `17_tt-year-2030.png` | Year tooltip, 2030 (the cumulative charts) | none |
| `18_tt-f3-band-oldest.png` | Renovation-band tooltip, "10 years or more" (F3 bars) | none |
| `19_tt-f4-hotel-gatwick.png` | Hotel tooltip, Gatwick (F4 dots) | none |
| `20_tt-glossary.png` | Definitions tooltip (the chip at the bottom right of both pages) | none |

`slot-sheet-render-minus-comp.txt`: every slot of every page view, render minus comp, one line each.

## How they were made, and what they cannot show

- **Page renders (01 to 11):** the session's Desktop window is 540 px wide, so a page is rendered as four strips of
  480 x 1080 in the throwaway copy and stitched (`tools/desktop_shots/tiles`, `step9/round.py`), at 1.84 capture px per
  page px, here scaled to 1920 x 1080. A slicer only reaches its own page: the strip with the scenario pills or the
  selector carries the selection, the other strips get the same choice as a page filter.
- **The header artwork is not on them.** A strip page has no background image: the Night header zone is a plain
  rectangle, without the night-glow and the faded door hanger. A whole-page capture in this narrow window is no
  substitute (Desktop draws the background image off its place at that zoom). **Look at the header in the published
  report** (step 12).
- **Vertical seams** at page x 480, 960 and 1440: a chart or a table that crosses one can read up to 2 px off there.
- **Tooltip renders (12 to 20):** the tooltip page as an ordinary page with the hover's context as page filters
  (`tools/desktop_shots/step10/tt_pages.py`), 2.09 px per page px (the glossary 1.08). A real hover is step 12's.
- **Nothing changed on the canvas with the prune.** Renders 08, 10, 11 and all nine tooltip renders are byte for byte
  the renders of the same views made in steps 9 and 10, before the model was pruned. Renders 05, 06 and 07 equal step
  8's within capture noise (about 500 of two million pixels differ, none by more than 20 of 255).

## Against the comp

Measured per slot (`tools/desktop_shots/step11/slot_sheet.py`): the number of text rows, and the largest difference in
y, left edge and right edge.

| View | Text slots within 2 px | Outside |
|---|---|---|
| 01 Page 1 | 31 of 37 | the four KPI cells 2.3 to 2.5 px, `c_f3_note` 2.4, `lbl_f4_phoenix` 2.1 |
| 02 to 04 Recommended, Low / Expected / High | 23 of 27 each | `c_plan_t2`, `c_plan_t3` 2.1 px, `c_plan_gate` 2.3; the active tab (see below) |
| 05 to 07 What waits, Low / Expected / High | 14 of 15 each | the active tab |
| 08, 09, 11 Build | 20 of 20 each | none |
| 10 Build, over the budget | 19 of 20 | `c_you_title`: the white title starts 12 px inside the alarm band, as designed |

Every text slot has the comp's number of lines in every view: no line wraps differently. The figures of 2.1 to 2.5 px
are at the method's limit (one device pixel of a strip is 0.54 page px, and Desktop snaps a card to it). The "active
tab" reads off because the sheet measures the tab's outline; the label itself is within 0.1 px in y and 3 px in x
(Semibold, open question 5).

### Outside 2 px, by design or by Power BI (all recorded in doc 23; none is new in this step)

**Page 1** (open question 4)
- Folio table: header 35 px and rows 23.7 px (comp 28 and 28); the first row sits 4.5 px lower.
- Line-end names of F1 and F2 start 9 to 10 px left of the comp's; F1's year labels 3 px higher.
- F3: value labels 4 px further from their bars.
- F4: the "90%" label is bold; reading order note, rows, link.
- The ring-i of the hover tags is Burnt Tangerine, not Tangerine (contrast floor 4.5:1).

**Page 2, frame and Recommended** (open questions 2, 5, 6)
- Tab labels in Semibold, 3 to 5 px wider than the comp's picture.
- Ledger: cells stand at the top of their rows (the comp centres them): 10 to 20 px higher for the short cells; the
  header words 8.5 px higher.
- Hero table: 8 px wider than the comp (it runs to x 1056), the NPV values end 6 px further right; the header rule
  and the two reference lines 4.5 px lower; the bars 5 px higher inside their rows.
- Chart of the capital plan: end labels above or under their line ends, not right of them (Expected 21 px higher
  than the comp's); two axis ticks (+$20M, $0M) instead of four; the two line names semibold; the zero line runs to
  the plot's right edge.

**What waits** (open question 7)
- A's disc is Deep Coffee, not Coffee Blue (the white letter needs 4.5:1).
- Table header words 8.7 px higher; both charts tick every $20M (comp: every $10M); axis labels 4 to 5 px closer to
  their plots; A's end label 5 to 6.5 px higher; in Low the comparison plot starts 3 px higher.

**Build your own** (open question 8)
- From six moves on the bars stand 26.2 px apart (comp 28); **from eight moves on Power BI scrolls the bars**.
- The zero line of the bars runs down the five rows while fewer are picked.
- A plan beyond $62M has no dot in the proof chart (render 10); the comp drew it outside the chart.
- `tbl_moves`: header words 9.2 px higher, the last column 3 px further right.
- Comparison chart: A's end label 5 to 7 px higher; over the budget two ticks instead of six.

**Tooltips** (open question 9)
- `tt-package` is 616 px high (was 552): the moves table at 12 pt needs the room for eight moves.
- The glossary's seventeen definitions and C's name in its tooltip are the build's wording.

**One number** (open question 1): the kiosks' Expected "a year on cost" prints 20.6 % (exactly 20.55 %); the approved
text says 20.5 %. It shows in the hero title and the hero row of render 03.

## Checks behind this set (14 Nov, on the pruned model)

`build_checks.py` 6 of 6 (bound fields, vocabulary, formats, one release rule, 129 texts equal the spec with the 2
known of question 1, the reachability gate); `number_checks.py` 766 checks, 765 ok, 1 known; `alt_texts.py` 136 stops,
0 flags; `a11y_check.py` 0 failures; `schema_check.py` 196 files, 0 failing; Microsoft's validator 0 errors;
`compliance_check.py` 5 of 5. Details in doc 23, step 11.
