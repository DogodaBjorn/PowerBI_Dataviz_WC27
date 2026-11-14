# 21 · Power BI build guideline: from critique to a workable plan (13 Nov 2026)

**Role:** the Power BI specialist hired for a last technical and functional check. Not the jury. The question
here is how the report is constructed, which Power BI parts it uses and why, and how the approved requirements
(doc 20) become something that can be built, rendered and published without surprises.
**For:** (1) the session that builds the **Claude artifact** of the fixed dashboard (section 12), (2) the
**builder** (`pbir-operator`, through the generators) who takes that version live (sections 4 to 11, 13).
**Inputs:** `19-jury-review`, `19-review-ui-ux`, `19-investor-review` (critique), `20-requirements-storytelling`
(the approved contract). The content is peer reviewed and stays as it is. This document decides the
construction. Where construction forces a change to doc 20, it is listed in section 2 as a point for Bjorn. He approved all five on 13 Nov (section 2.2).
**Version reviewed:** pbip at `6ec5b58` (12 Nov 20:04), branch head `cf50fcc`. The working tree under
`project/pbip` is clean, so the renders of 13 Nov 09:28 (`screenshots/Clarity-review-2026-11-13/`, P1, three P2
states, eight tooltips) show the latest version. I did not open Desktop.
**Method:** every visual, bookmark and report setting read from the PBIR files; every measure traced from the
report into the model (dependency closure); the generators read (`opzet_report.py`, `sketch_model.py`,
`pbir_lib.py`, the layout and layering files).

IDs: `PB-nn` = a construction finding of mine. `P-n` = a reusable pattern. `S-n` = a spike that must pass before
the build depends on it. `N-n` = a point that needed Bjorn's nod (all five approved on 13 Nov). `R-…` = doc 20.

---

## 0 · Verdict

The report is well built for what it had to prove. The generator-driven set-up (slot map, layering file,
display-only bookmarks, alt text from measures) is better engineering than most contest entries have. The
weakness is the same one the jury named from the outside (J-CI-1): **page 2 carries a lot of scaffolding to make
Power BI do things it does not do natively**, and part of that scaffolding is what leaks the locale, hides content
behind hover and makes the page slow to change.

| Fact (measured on the files) | Value |
|---|---|
| P1 | 43 visuals: 19 cards, 15 text boxes, 4 images, 2 line, 2 column, 1 table |
| P2 | 79 visuals, of which 35 to 43 hidden per state; 7 scatter visuals draw one chart in two sizes; 6 buttons draw 3 tabs; 10 image visuals fed by SVG measures; 1 custom visual (Deneb) |
| Tooltip pages | 9, each with its own background image |
| Measures | 462. The report reaches 257 (188 bound, 69 through dependencies). 56 more serve only the D1 to D3 sketch reports. **149 are dead** |
| Text measures | 211 of the 257 live ones return text. The two largest in the model draw a table and a range bar as SVG (`TT Moves SVG`, `TT Range SVG`, 3.6 and 4.3 KB of DAX) |
| Number formatting | No dynamic format strings anywhere. Every native data label follows the viewer's locale |
| Broken reference | `tt-package/tt_payback` binds its font colour to `[TT Payback Color]`, which does not exist in the model |
| Theme | Only wildcard styles. All real formatting sits per visual in the generator |

### Keep (technically right, do not touch)

1. **Generators as the source of truth**, with the slot map and the layering file. A rebuild reproduces the report.
2. **Display-only bookmarks** (`applyOnlyToTargetVisuals`, `suppressData`) with the scenario in a slicer. A bookmark
   never changes data. This is the correct way to build page states.
3. **Alt text bound to measures.** It follows the scenario and cannot drift from the canvas.
4. **Text measures for sentences that contain numbers.** They print with a point in an nl-NL session, which the
   renders prove. They are the reason the titles and tiles are locale-proof today.
5. **Tab buttons as on/off twins at one position.** Six visuals for three tabs looks wasteful, but it guarantees the
   active tab is drawn at first load. Restyle them (P-2), do not replace them.
6. **The hover layer on top of the scatter.** A visual on top takes the mouse over its whole rectangle, so one
   transparent layer that owns the tooltip is the only way to hover 456 dots under lettered markers.
7. Filter pane hidden, default tooltips off where no tooltip page is bound, `useScaledTooltips`, charts not
   responsive, visual headers kept on data visuals for "Show as a table".

### The seven construction problems, in order of cost

| ID | Problem | What it costs | Fixed by |
|---|---|---|---|
| PB-01 | **Native data labels carry numbers.** F3 bars, F4 bars and both waterfalls print "+6,8", "91,9%", "+$3,4M" on a non-English machine, next to text measures with points | J-VE-1, UX-11, INV §5. A judge in a nl, de or fr browser sees mixed formats under Publish to Web | P-1 |
| PB-02 | **The waterfall visual.** Its total label ("Totaal") is translated by Power BI and cannot be renamed | Same. No setting fixes it | Retire both waterfalls (R-P2-4, R-B-4) |
| PB-03 | **The argument is drawn with overlays.** The hero is a stack of scatters; the package contents, the findings and the definitions are tooltip pages | J-AC-1, J-CI-1, J-VE-9 | Doc 20's static hero, ledger and capital plan, built as tables and plain charts (sections 6, 7) |
| PB-04 | **Page-level controls live inside a card** and three control styles exist | UX-03, UX-04, J-AC-5 | P-2, section 5 |
| PB-05 | **One custom visual carries the best interaction.** Deneb has no keyboard support, cannot open with a saved selection, and is the largest open risk at the Publish to Web gate | J-AC-3, R-B-2, R-X-3 | N-1: native selector |
| PB-06 | **Things drawn in DAX that Power BI draws natively**: a table as SVG, a range bar as SVG, pills as SVG images, static sentences as measures in card visuals | Model weight, queries, unreadable DAX, text that is an image | Section 9, P-3, P-7 |
| PB-07 | **Model hygiene for a file a judge can open**: 149 dead measures, five helper tables no live measure reads, one broken binding, two-decimal money helpers that contradict R-G1 | Credibility with a judge who opens the PBIX; R-G1 | Section 10 |

### What the rebuild does to the numbers

| | Today | Target |
|---|---|---|
| P2 visuals, total / visible in Recommended | 79 / 39 | about 65 / about 40 |
| Scatter visuals | 7 | 4 (one stack, one size) |
| SVG measures | 12 | 3 (two hero bars, the A chip) |
| Custom visuals | 1 | 0 (N-1; Deneb only if spike S-3 fails) |
| Tooltip pages | 9 | 5 (N-4) |
| Card frames that switch per state | 5 | 4, the bottom card is shared |
| Visuals that can leak the locale | 4 | 0 |
| Measures in the submitted model | 462 | about 280 (section 10.4) |

The count of objects barely drops. What changes is what they are: content instead of scaffolding.

---

## 1 · Construction audit, element by element

| Element | How it is built now | Verdict | Why, and what to do |
|---|---|---|---|
| Card surfaces | Empty text boxes with fill, radius and shadow (`z_card_*`, `z_tile_*`) | Keep | They scale with the content in every host, which a background image did not (rounds 6 to 10). Only the per-state variants shrink (section 5) |
| KPI row | Per KPI: text box label + card value + card context line | Keep | A single multi-callout card could replace 12 visuals, but the current row renders correctly and R-P1-2 only needs a code in the label. Not worth the risk before 17 Nov |
| Titles, notes | `cardVisual` showing one text measure, fill switched off by `no_card_fill()` | Keep for dynamic text. **New static text goes in a text box** (P-3) | A constant string in a measure costs a query and a hack to hide the card's fill |
| F1, F2 line charts | Native line charts, series labels or legend | Change | R-P1-3 band, R-P1-4 end labels. Sections 4.2, 4.3 |
| F2 folio | Native table on text measures | Keep | Locale-proof, exact, accessible |
| F3 columns | Native columns, native data labels | Change the labels | P-1 |
| F4 | Multi-callout card + seven columns from zero | Retire | R-P1-7. Section 4.5 |
| Hero scatter, large | 3 scatter layers, guide tile, view slicer | Retire | R-P2-4. The small stack stays for What waits and Build |
| Hero scatter, small | 4 scatter layers | Keep | The technique is justified (see Keep 6) |
| Tabs | 6 action buttons, bookmark action | Keep, restyle, move | P-2 |
| Scenario | Button slicer on `Scenario` | Keep, restyle, move | P-2 |
| View switch | Button slicer on `ScatterView` | Retire with its table | R-P2-4 |
| Recommendation tile | Glow frame, chip, 4 cards | Simplify | No frame of its own; two text boxes replace three cards (section 6.2) |
| Waterfalls | Native waterfall, twice | Retire | PB-02 |
| Cumulative charts | Native line, legend, reference line | Change | Direct labels, no legend (P-5) |
| B and C cards | 2 × (image, 5 cards) in fixed slots | Retire | One table (section 7.2, N-3) |
| Build selector | Deneb, advanced cross-filter | Replace | N-1 |
| Hover tags, pills | 10 image visuals (3 on P1, 7 on P2) fed by 6 SVG measures | Replace | Native text boxes and one card with its own border (P-7) |
| Footer chips F1 to F4 | 4 transparent cards over one SVG pill, 4 tooltip pages | Retire | R-P2-12, N-4 |
| tt-package | Cards + SVG range bar + SVG moves table | Change | A sentence and a native table (section 9) |
| Theme | Wildcard only | Extend a little | Button and slicer states into the theme (P-2), so the three control visuals cannot drift |
| Page filters | P2 page filter on brand and projects; visual-level filters elsewhere | Keep | Correct scope |
| Interactions | Explicit `NoFilter` for overlays, `DataFilter` from the selector to six targets | Keep the pattern | Re-list the targets after the rebuild (section 8) |

---

## 2 · Decisions

### 2.1 Taken here, inside the options doc 20 leaves open

| # | Decision | Reason |
|---|---|---|
| K-1 | **The hero (R-P2-3) is one native table with two SVG bar columns**, the option doc 20 lists as "allowed", not the two bar charts it lists as "preferred" | Rows align by construction. Status, finding and growth get their own text columns. Every number is a text measure, so nothing leaks. One visual, one tab stop, real text for a screen reader. Two bar charts need pixel-matched plot areas, labels inside the category axis and P-1 on both. Fallback if S-2 fails: the two bar charts |
| K-2 | **The ledger (R-P2-5) is a native table** on a four-row `Finding` table | Static on the canvas, wraps text, reads row by row for a screen reader, follows the scenario |
| K-3 | **One row split for all three P2 states: top row y 168 to 656, bottom row y 672 to 1016.** Within doc 20's ±32 px | The bottom card becomes one frame that never switches, and the page stops jumping between states |
| K-4 | **Both waterfalls go.** Build shows a sorted bar chart of the picked moves, the total stays in the tile (R-B-4's own fallback, taken now) | PB-02 has no fix |
| K-5 | **Tabs stay action-button twins**; no bookmark navigator | The navigator does not reliably show the active tab at first load |
| K-6 | **Milestones are one text line under the chart plus one labelled constant line at the 2028 gate.** No per-milestone markers | Jul 2027, Oct 2027 and Apr 2028 sit 30 px apart on the axis; native labels would collide |
| K-7 | **Hover tags and the Definitions chip become native text**, in the D5 style | Removes six SVG measures and the queries of ten image visuals (three on P1, seven on P2); the words become real text |

### 2.2 Approved by Bjorn on 13 Nov (construction changes something he or doc 20 decided)

Bjorn approved all five as recommended. Doc 20 carries them as amendments. The last column is a technical
fallback the builder may take without a new question; it is not a second option to choose from.

| # | Point | Decision | Technical fallback |
|---|---|---|---|
| N-1 | **Build selector: Deneb or native.** Bjorn chose Deneb on 10 Nov | **Native.** Bjorn, 13 Nov: "if it's better without, do it without." A button slicer (multi-select, selection icon as the check mark) beside a table with the same ten rows. It opens with A picked (a slicer's saved selection), works by keyboard, needs no custom visual and no Publish to Web exception. `deneb_selector()`, `build_selector_spec.py` and `publicCustomVisuals` leave the report once S-3 has passed | Only if S-3 fails by the evening of 15 Nov: Deneb stays as it is, with the new column, square marks and "Click", the empty state of R-B-2, and the keyboard limit noted in the submission |
| N-2 | **C0: 2.8 or 2.7 points.** Doc 20 leaned to 2.7 | **2.8 stays**, on Bjorn's condition: only true data, nothing made up. Checked against `analysis/output/storytelling_checks.txt`: margin after commissions 36.45 % to 33.73 % (exact fall 2.72 points); operations 46.14 % to 44.37 % (1.77); commissions 9.68 % to 10.65 % of revenue (0.97). Every figure on the card is one of these real values rounded to one decimal: 36.5, 33.7, 1.8, 1.0. None is adjusted to fit. 2.8 is the difference of the two shown values and the sum of the two shown parts, so a reader who checks the card gets the title. `F1 Title (text)` and `KPI Margin after Context (text)` keep their logic (`REVIEW M8`). The copy of R-P1-3 reads 2.8 | None. The exact figure (2.72) goes in the build log for anyone who asks |
| N-3 | **What waits: three cards side by side do not fit.** At the 12 pt floor a 344 px card holds about 42 characters a line. Tranche 3 needs 13 lines of text plus title and four numbers; the card has room for 9 | **One comparison table**: three rows (B, Tranche 2, Tranche 3), columns Option · The numbers · Why it's on the table · Why not now · When we decide (section 7.2). Same grammar by construction, rows size themselves, one visual instead of about 21 | If S-7 fails (no line breaks inside a cell): the four numbers become four narrow columns. Never three side-by-side cards |
| N-4 | **The four finding tooltip pages (tt-f1 to tt-f4) lose their only binding** when R-P2-12 removes the footer chips. R-TT-2 asked to improve tt-f3 | **Delete the four pages**, their canvases and their measures. The ledger carries the findings on P2, and P1 is one click away. R-TT-2 closes by removal | None |
| N-5 | **Capital plan card (R-P2-7): the gate copy does not fit under two full-width elements.** Title, labels, bar, chart, strip and four lines of gate copy need about 364 px; the card has 312 | Budget bar full width on top. Below it, **gate copy left, cumulative chart right** (section 6.3). The chart also reads better at 7:1 than at 16:1 | If the artifact still shows overflow: the gate copy in its short form on this card, the full text in What waits |

---

## 3 · Reusable patterns

These are the parts to build once and use everywhere. Each replaces several one-off solutions in the current
report, and each belongs in the pbi-atelier template afterwards.

### P-1 · Label-safe numbers

**Rule:** a number a reader sees is either (a) text from a text measure, or (b) an axis tick without a decimal
or thousands separator ("40%", "$10M", "2028"), or (c) a native data label whose measure has a **literal dynamic
format string**. Nothing else.

(c) is new for this project. A measure keeps its numeric value for the bar or the line, and its format string
expression returns the finished text in quotes, so Power BI prints that text and applies no locale:

```tmdl
measure 'NPS 2025 (label-safe)' = [NPS 2025 (signed)]
    formatStringDefinition = """" & [NPS 2025 (signed, text)] & """"
```

**Corrected by spike S-1 (13 Nov, section 13, "Step 2 results"):** the literal goes in all three sections of the
format string (positive; negative; zero), or a negative value prints a second minus. And `formatStringDefinition` is
written after the measure's properties, in a backtick block:

```tmdl
measure 'NPS 2025 (label-safe)' = [NPS 2025 (signed)]
    displayFolder: 15 Storytelling rebuild

    formatStringDefinition = ```
            VAR t = [NPS 2025 (signed, text)] RETURN """" & t & """;""" & t & """;""" & t & """"
            ```
```

- In `sketch_model.py`: give `m()` an optional `fmt_def=` argument that writes `formatStringDefinition`, and a
  helper `label_safe(name, value_expr, text_expr, …)`. The text expression is one of the existing formatters
  (`fm`, `sfm`, a new `pct1`, `pt1`), so labels and tiles print the same characters.
- **Corrected by build step 3 (13 Nov, doc 23):** a label-safe measure carries **no** static `formatString`. With
  both properties Desktop refuses the whole project; the engine says the combination is not supported. So
  `validate_tmdl --strict` warns once per label-safe measure ("no formatString"): expected. Built as `label_safe()`
  and `m(..., fmt_def=)`; eleven measures use it.
- Use only on visuals whose value axis is hidden (the axis would repeat one literal on every tick). That is
  already the house rule: "no value axis, every bar carries its label". Where the axis shows (the cumulative
  charts), the label-safe end series come after the line series, so the axis takes a line's format.
- Needed on: F3 bars, the capital-plan bar segments, the Build bar chart, the line-end labels (P-5).
- **S-1:** render F3 with this measure in the nl-NL Desktop. Pass = "+6.8", "−4.9" with points. Fallback: data
  labels off and three text cards over the bars.

One formatter set, R-G1: `fm` ($ + one decimal + M), `sfm` (signed), `pct1`, `pt1`. `fmc`, `fmc2` and `sfm2` (two
decimals) are retired; a two-decimal value below $1M is an explicit, named exception. A check in
`a11y_check.py` greps the text measures for `"$#,0.00"`.

### P-2 · One control language

One family, two sizes, two surfaces. All four control types are native and share the same state model (default,
hover, selected), so the look is set **once in the theme** (`visualStyles` for `actionButton` and
`advancedSlicerVisual`) and only the size and the text are set per visual.

| | Large (40 px high) | Small (28 to 32 px high) |
|---|---|---|
| Used for | The three state tabs | Scenario pills, page-navigation buttons, the Build invitation |
| Radius | 8 px | half the height (pill) |
| Text | Segoe UI Semibold 12 pt | Segoe UI 12 pt |

| Surface | On / primary | Off / secondary | Hover |
|---|---|---|---|
| Night masthead | fill `#F7F5EE`, text `#12233D` (15.8:1) | **solid** fill `#12233D`, 1 px outline `#C9D0DC`, text `#F7F5EE` (15.8:1) | fill `#C9D0DC`, text `#12233D` |
| Light card or footer | fill `#12233D`, text `#FFFFFF` | fill `#FFFFFF`, 1 px outline `#4B5466`, text `#12233D` | fill `#E3DFD3` |

The off state on the masthead is a solid fill, not transparent: the masthead artwork (the hanger shape) runs
behind the control row and would change the contrast.

- Tabs: `tab_*_on` / `tab_*_off` twins as now, bookmark action, new labels (R-P2-2).
- Scenario: the existing button slicer, restyled.
- Page navigation (R-P1-8, R-P2-1): `actionButton` with action type page navigation. **S-6:** author one in a
  throwaway Desktop copy and copy the `visualLink` shape back into `button()`; do not guess the property names
  (invariant 2).
- Build invitation (R-P2-8): the same button with the bookmark action `bm_p2_build`.

### P-3 · Which visual carries which text

| Text | Visual | Why |
|---|---|---|
| Static sentence, label, link line, kicker | Text box (runs for mixed colour) | No query, reads its own words to a screen reader |
| Sentence with a number or a scenario word | `cardVisual` on a text measure, alt text = the same measure | Current pattern, proven |
| Several paragraphs that must keep an even gap, or rows of mixed text and numbers | Native table (`tableEx`), word wrap on, header on or off | Power BI has no auto-layout between visuals. A table is the only native thing that flows text and keeps rows aligned |
| A table | A table. Never an SVG | `TT Moves SVG` is the example to remove |

Line breaks inside one measure (`UNICHAR(10)`) are used for the two-line ledger cells. **S-7:** confirm that a
table cell and a card value both honour the break with word wrap on. **Result (13 Nov):** a table cell does, a card
value does not. Text that needs a break sits in a table cell, or is split over two cards (section 13, "Step 2 results").

### P-4 · Bars inside a table (the hero)

One Python function in `sketch_model.py` writes a bar-cell measure: `bar_cell(name, value_expr, domain_min,
domain_max, ref_value, fill_expr, w, h)`. It returns an SVG data URI with one rectangle from the zero point and
one full-height reference line. The measure gets `dataCategory: ImageUrl`.

- Fixed pixel width and a **fixed domain** from the model (the minimum and maximum over all three scenarios,
  rounded outward), so the reference line sits at the same x in every row and every scenario, and bars move when
  the scenario changes.
- Row padding 0 and image height = row height, so the reference line reads as one continuous line down the ten
  rows.
- The value is **not** in the SVG. It sits in its own right-aligned text column next to the bar.
- Numbers concatenated into the SVG go through the existing `_svg()` helper conventions (points, no locale).

**Corrected by spike S-2 (13 Nov, section 13, "Results of the two big spikes"):** the image size is set in `grid`
(`imageHeight` and `imageWidth`, one width for the whole table). Desktop draws an image 7 px from the left edge of
its cell and needs the column to be the image + 11 px. So `bar_cell()` takes the comp's column width for its
geometry, subtracts 7 from every x, and writes an image as wide as the narrowest bar column minus 7. The visual is
2 px wider than the sum of its columns. Prototype: `project/tools/desktop_shots/spikes_step2/spike2_prep.py`.

### P-5 · Direct labels at line ends

Legends go; every line is named and valued at its right end.

- Series name: native series labels (as F1 does today).
- Value at the end: a second measure per line that returns the value only for the last year (and for F2 also the
  first), added as its own series with the line hidden and data labels on, label-safe (P-1).
- A tick below zero and the zero line named "Cash positive above this line" (R-G2) on every cumulative chart.

### P-6 · Status is a word first, a colour second

Wherever a row or a mark has a status (A, 2028 gate, not now; over budget; your plan), a text column or a text
label carries it, and the colour of R-G3 repeats it. `Move Status` and `Move Status Color` come from one small
table (section 10.1), never from separate SWITCH statements per visual.

### P-7 · Hover cues and chips, native

- **Hover tag** (decorative): a text box with two runs, "ⓘ" in Tangerine and "Hover a bar" in Night, on a white
  fill with a 1 px `#E3DFD3` border and radius 14. Negative tab order, as now.
- **Definitions chip** (a hover target): one `cardVisual` with its own container fill, border and radius, the
  text measure "ⓘ Definitions" in Night, the tooltip page bound to it. The SVG pill under it goes.
- **S-8:** check that "ⓘ" (U+24D8) renders from the Segoe UI stack in Desktop and in a browser. Fallback: keep
  the SVG disc, restyled to D5.

### P-8 · One skeleton, one slot map, checked by script

The slot map (`opzet-layout.json`) is the contract between the artifact and the report (section 12). Extend
`a11y_check.py` or add `tools/build_checks.py` with four checks that run after every generator run:

1. every measure the report binds exists in the model (would have caught `TT Payback Color`);
2. no visible string contains a "Never" word of R-G2;
3. no text measure formats money with two decimals;
4. exactly one measure holds the release rule (`Gate Rule (text)`), and no other measure or text box contains
   "release", "revisit" or "broken even".

---

## 4 · Page 1, The Brand Review: build sheet

Canvas 1920 × 1080. Unchanged: masthead zone to y 168, KPI card y 168 to 288, F1 to F3 cards y 312 to 776
(x 32 / 656 / 1280, w 608), F4 card y 800 to 1024, footer row y 1044. Card padding 24, so content starts at
card x + 24. Coordinates below are the starting slot map; the artifact step may move them by ±16 px.

### 4.1 Masthead, KPI row, footer

| Slot | x, y, w, h | Visual | Content | Closes |
|---|---|---|---|---|
| `z_eyebrow` | 248, 20, 640, 24 | text box | "1 / 2 · THE WAKE-UP CALL · THE BRAND REVIEW" | R-P1-1 |
| `c_subtitle` | 32, 108, 1856, 24 | card | new copy of R-P1-1 in `Subtitle P1 Briefing (text)` | R-P1-1 |
| `kpi_*_label` | unchanged | text box, two runs | code in Night semibold + label: "F4 · Occupancy", "F1 · Operating margin after commissions", "F2 · Room revenue booked through online agencies", "F3 · Guest quality: net promoter score (−100 to +100)" | R-P1-2 |
| `z_footer` | 32, 1044, 1320, 28 | text box | unchanged | |
| `btn_next` | 1376, 1044, 352, 28 | button, small, light surface, primary (P-2) | "Next: what we fund, and why →", page navigation to P2. Tab order after F4, before Definitions | R-P1-8 |
| `chip_def` | 1744, 1044, 144, 28 | card (P-7) | "ⓘ Definitions", tooltip `tt-glossary` | D5 |

The KPI code is a run in the existing label text box. No new visual, no chip image.

F-code kickers (`kicker()` in `opzet_report.py`): the code run changes from `BAD` to `INK` (R-G3).

### 4.2 F1 The margin

| Slot | x, y, w, h | Visual |
|---|---|---|
| `c_f1_title` | 56, 352, 560, 32 | card, `F1 Title (text)` |
| `ch_f1_margin` | 56, 392, 560, 248 | **stacked area chart** |
| `c_f1_note` | 56, 648, 560, 72 | card, `F1 Note (text)`, three lines |
| `lnk_f1` | 56, 728, 560, 24 | text box, Night, "→ Page 2: revenue management and the kiosks." |

Chart recipe (R-P1-3, the "preferred" form made honest):

- Series 1 `Trend Margin after GI`: line 3 px Coffee Blue, **area fully transparent**.
- Series 2 new measure `Trend Commission Take GI` = before − after: area in Warm Grey at about 70 % transparency,
  line 2 px Warm Grey. Its top edge is the margin before commissions.
- Value axis 30 % to 50 % as now. The base series is invisible, so the cut axis does not distort an area; the
  band's thickness stays true to scale, and the fall of the blue line stays visible.
- Series labels at the right: "After commissions", "Commissions". Legend off.
- **S-5:** per-series area transparency in PBIR. Author once in Desktop, read the JSON back. Fallback (doc 20's
  "allowed" form): keep the two lines and shade under "Before commissions" only, in the same grey.

### 4.3 F2 The middleman

| Slot | x, y, w, h | Visual |
|---|---|---|
| `ch_f2_ota` | 680, 392, 560, 144 | line chart, no legend, **no value axis** |
| `tbl_f2_folio` | 680, 544, 560, 112 | table, unchanged |
| `c_f2_note` | 680, 664, 560, 72 | card, new copy (R-P1-4), "Our reading…" deleted |
| `lnk_f2` | 680, 736, 560, 24 | text box, "→ Page 2: the booking app with member rates." |

- Without the legend row and the axis the plot is as tall as today and wider.
- End labels (P-5): `Trend OTA GI (ends)` returns the value for 2021 and 2025, `Trend OTA Sisters (end)` for 2025.
  Whole percentages ("33%", "50%"), so they are locale-safe without P-1. Series labels name the two lines at
  the right.
- F2 is the tightest card on the page. If the note needs four lines, take 24 px from the table (row padding), not
  from the chart.

### 4.4 F3 The fading welcome

| Slot | x, y, w, h | Visual |
|---|---|---|
| `ch_f3_age` | 1304, 392, 560, 216 | columns, data labels from `NPS 2025 (label-safe)` (P-1), tooltip `tt-f3-band` |
| `c_f3_count` | 1304, 608, 560, 24 | card, new `F3 Count (text)`: "44 of 50 hotels; 6 have no renovation date." |
| `c_f3_note` | 1304, 640, 560, 96 | card, new copy (R-P1-5) |
| `lnk_f3` | 1304, 736, 560, 24 | text box, "→ Page 2: the refresh waits for the 2028 gate, and why." |

`F3 Count (text)` counts from the model (hotels with and without `Renovation Age Sort`), it is not typed in.

### 4.5 F4 Where we are full (R-P1-6, R-P1-7)

| Slot | x, y, w, h | Visual |
|---|---|---|
| `c_f4_kicker` | 56, 816, 560, 24 | text box |
| `c_f4_title` | 56, 840, 1640, 32 | card, new title (R-P1-6) |
| `tag_f4` | 1704, 812, 160, 28 | hover tag (P-7), "ⓘ Hover a hotel" |
| `c_f4_note` | 56, 880, 416, 48 | card: "Gatwick did in 14, Montréal in 13; Kingston, the third extension on offer, in none." |
| `lnk_f4` | 56, 936, 416, 48 | text box, two lines |
| `c_f4_rows` | 496, 872, 160, 120 | the existing three-callout card, laid out as three rows: "Airport 82.0%", "City 79.1%", "Highway 77.5%" |
| `ch_f4_avg` | 656, 872, 1208, 144 | scatter, bottom layer: three diamond markers, one per location type, at the row average |
| `ch_f4_dots` | 656, 872, 1208, 144 | scatter, top layer: 50 hotels, tooltip `tt-f4-hotel` |

Native recipe:

- X = `Occupancy % 2025`, axis 60 % to 95 %, whole-percent ticks. X constant line at 0.9, labelled "90%".
- Y = new measure `F4 Row Y`: Airport 3, City 2, Highway 1, plus a fixed offset of ±0.3 for hotels whose
  neighbour in the same row is within one point (keeps Gatwick 90.4 and Montréal 90.2 apart). Axis 0.5 to 3.5,
  hidden.
- Details = new calculated column `Hotels[F4 Dot Label]`: the short name without "Airport" for the seven fullest
  and for Kingston; for every other hotel a unique string of zero-width spaces, so 50 points stay separate and 42
  of them print nothing. Category labels on, 12 pt Night.
- Fill = `F4 Dot Color`: Night for the seven fullest, Warm Grey for the rest. No blue (R-G3).
- Both layers read their axis ends from the same measures (the `scatter_axes()` pattern), so the plot areas match.
- "Topped 90%" gets its definition in `tt-glossary` and in the tooltip.

**S-4:** one render. Pass = eight names visible, none overlapping, none dropped by Power BI, Kingston readable at
the left of the airport row. If two renders do not get there, this visual becomes a Deneb strip plot
(`dn_f4_strip`): about 40 lines of Vega-Lite, the tooltip page stays bound. That is the one place where Deneb is
the better tool, because the label placement is under control.

---

## 5 · Page 2, the shared frame (all three states)

| Slot | x, y, w, h | Visual | Content |
|---|---|---|---|
| `z_eyebrow2` | 248, 20, 480, 24 | text box | "2 / 2 · ROOM TO INVEST · THE INVESTMENT STRATEGY" |
| `btn_back` | 744, 16, 184, 28 | button, small, Night surface, secondary | "← The Brand Review", page navigation to P1 |
| `z_headline2` | 32, 60, 1160, 48 | card | `Headline P2 (text)`, D6 copy, numbers from A |
| `c_subtitle2` | 32, 108, 1160, 48 | card, two lines | R-P2-1 copy, the case word from the slicer |
| `tab_rec_*`, `tab_alts_*`, `tab_build_*` | 1224 / 1448 / 1672, 60, 216, 40 | button twins, large, Night surface | "Recommended: A" · "What waits, and why" · "Build your own" |
| `lbl_scenario` | 1512, 112, 80, 32 | text box, `#C9D0DC` | "Scenario" |
| `sl_scenario` | 1600, 112, 288, 32 | button slicer, small, Night surface | Low · Expected · High |
| `z_card_bottom` | 32, 672, 1856, 344 | card frame | always visible, not a bookmark target |
| `z_footer2` | 32, 1044, 1696, 28 | text box (static now) | R-P2-12 source line |
| `chip_def2` | 1744, 1044, 144, 28 | card (P-7) | "ⓘ Definitions" |

- Tab order: logo → eyebrow → back → headline → subtitle → tabs → scenario → content → footer (R-P2-2, J-AC-5).
- The two top frames exist in two variants: `z_card_hero` (32, 168, 1040, 488) and `z_card_decision`
  (1088, 168, 800, 488) for Recommended; `z_card_scatter_s` (32, 168, 720, 488) and `z_card_panel_w`
  (768, 168, 1120, 488) for What waits and Build.
- Bookmarks keep their names (`bm_p2_rec`, `bm_p2_alts`, `bm_p2_build`); only the display names and the target
  lists change. `bookmark()` already derives both from the slot map.
- Removed from the frame: `z_pill_facts`, `chip_f1` to `chip_f4`, `sl_view`, `z_tile_guide`, `c_guide*`,
  `z_tile_rec`.

---

## 6 · P2 "Recommended: A"

### 6.1 The hero: `tbl_hero` (R-P2-3, K-1)

| Slot | x, y, w, h | Visual |
|---|---|---|
| `c_hero_title` | 56, 184, 992, 32 | card, `Hero Title (text)`, follows the scenario |
| `lbl_hero_8`, `lbl_hero_0` | y 220, h 20, x at the two reference lines | text boxes, decorative: "8%: our cost of money", "pays back by 2032 →" |
| `tbl_hero` | 56, 240, 992, 372 | **table**: header 32 px, ten rows of 34 px, row padding 0, no gridlines except one hairline under the header |
| `c_hero_caption` | 56, 616, 992, 24 | text box, R-P2-3 caption |

Rows: `InvestmentProjects` (page filter Goodnight Inn), sorted by the new column `Hero Sort` (rank of the
Expected "a year on cost", fixed at refresh, so the order never follows the scenario).

| Column | Width | Source | Format |
|---|---|---|---|
| Move | 280 | `InvestmentProjects[Move Name]` | Night; semibold look through font colour only |
| Answers | 104 | `Move Answers (text)`: "F2 · growth" | Dusk |
| Status | 96 | `Move Status (text)`: "A", "2028 gate", "not now" | font colour = `Move Status Color` |
| A year on cost | 196 | `Hero Yield Bar SVG` (P-4), domain 0 to 50 %, reference 8 % | image |
| (value) | 64 | `Move Yield (text)`: "47.0%" | right-aligned |
| NPV through 2032 | 180 | `Hero NPV Bar SVG` (P-4), fixed domain about −32 to +12 $M, reference 0 | image |
| (value) | 72 | `Move NPV (text)`: "+$3.4M" | right-aligned; negative in Burnt Tangerine |

- Bar fill = `Move Status Color` (A Coffee Blue, 2028 gate Night, not now Warm Grey). The status word carries the
  same information in greyscale.
- No tooltip page on this table. Alt text `Alt Hero (text)` names the top three moves and the 8 % line.
- `lbl_hero_8` and `lbl_hero_0` sit at fixed x because the column widths and the domains are fixed. The generator
  computes both x values from the same constants it passes to `bar_cell()`.
- **S-2 result (13 Nov): pass.** Columns 280 / 104 / 96 / 196 / 64 / **184** / **74**, visual width **1000**, image
  173 px drawn 7 px into its cell (section 13, "Results of the two big spikes"). The widths in the table above are the
  comp's and are too narrow by those pixels.
- **S-2:** build this table first, alone on a page, and render it in Desktop: the reference line continuous, no
  scrollbar, values aligned. Then one Publish to Web check of SVG cells at the gate. Fallback: two bar charts
  with identical category sort, row padding and height, category axis on the left chart only, labels by P-1,
  constant lines from the analytics pane.
- **Cut line (doc 20):** not verified by the evening of 15 Nov → R-P2-3-FB.

### 6.2 The decision card

| Slot | x, y, w, h | Visual | Content |
|---|---|---|---|
| `img_rec_chip` | 1112, 184, 40, 32 | image | the blue A chip (kept) |
| `c_rec_head` | 1160, 184, 704, 56 | text box, two paragraphs | "Our recommendation: package A" (20 px semibold) and the mix line (R-P2-6) |
| `c_rec_nums` | 1112, 248, 752, 64 | card, four callouts | "$9.4M" capex · "+$3.3M" NPV through 2032 · "+$3.5M" a year by 2032 · "37.5%" a year on cost |
| `c_rec_lines` | 1112, 320, 752, 72 | card, one measure with a line break | Line 1 worst case (always Low), line 2 the app carries it (R-P2-6) |
| `tbl_ledger` | 1112, 400, 752, 208 | **table**: header 28 px, four rows of 45 px | R-P2-5 |
| `c_ledger_caption` | 1112, 616, 440, 24 | text box | "2025 brand plus A's full yearly effect, in 2025 dollars." |
| `btn_build_invite` | 1560, 612, 304, 28 | button, small, light surface, secondary | "Think you can beat A? Build your own →", bookmark `bm_p2_build` |

- No tile frame, no glow, no outline (R-P2-6). The card itself is the tile.
- The mix line is static text: A's composition never changes with the scenario (decision of 7 Nov).
- Ledger: rows from a new `Finding` table (Code, Name, Ledger Sort = F2, F1, F4, F3). Columns:
  Finding (176, "F2 The middleman", Night) · What we track (248, two lines: the measure, a line break, the moves)
  · 2025 (72) · 2032 with A (96) · Status (160). All five are text measures that switch on
  `SELECTEDVALUE(Finding[Code])` and follow the scenario. Values of E11.
- Tab order inside the card: head → numbers → lines → ledger → invitation (R-P2-9).

### 6.3 The capital plan (R-P2-7, N-5), in `z_card_bottom`

| Slot | x, y, w, h | Visual | Content |
|---|---|---|---|
| `c_plan_title` | 56, 688, 1600, 32 | text box | "The $60M plan: $9.4M now, two decisions in 2028" |
| `tag_plan_cum` | 1712, 692, 152, 28 | hover tag | "ⓘ Hover a year" |
| `c_plan_t1` … `c_plan_t4` | y 724, h 60; x 56 / 339 / 713 / 1602; w 275 / 366 / 881 / 262 | four cards, three lines each | segment labels, left-aligned at their segment |
| `ch_plan_bar` | 56, 788, 1808, 32 | **stacked bar**, one bar, four measures, no axes, padding 0 | Tranche 1 Coffee Blue, Tranche 2 Night, Tranche 3 Night at 60 %, Not needed Warm Grey; short data labels by P-1 ("$9.4M", "$12.4M", "$29.5M", "$8.7M") |
| `c_plan_gate` | 56, 836, 704, 128 | card, `Gate Rule (text)` | the gate copy, verbatim |
| `ch_plan_cum` | 792, 828, 1072, 148 | line chart, numeric year axis | A's cumulative net: selected case 3 px Coffee Blue, the two others 1.5 px Warm Grey (Low dashed, High dotted); end labels by P-5; ticks at −10, 0, +10, +20; zero line "Cash positive above this line"; one X constant line at 2028.5 labelled "The 2028 gate"; tooltip `tt-year` |
| `c_plan_milestones` | 792, 976, 1072, 24 | card, `Milestones (text)` | "RMS live Jul 2027 · App live Oct 2027 · Kiosks live Apr 2028 (they need the app) · Cash positive 2031 (Expected)" |

- Label x positions follow the shares 9.4 / 12.4 / 29.5 / 8.7 of 60.0. Capex does not depend on the scenario, so
  static slots are safe. `build_checks.py` asserts that the model's shares match the slots within 0.5 %.
- Label text: T1 "Tranche 1 · package A" / "$9.4M · 2027". T2 "Tranche 2 · Gatwick and Toronto +40 rooms" /
  "$12.4M · 2028 gate" / "+$1.7M a year once live · 13.8% a year on cost". T3 the same pattern with $29.5M,
  +$2.3M, 7.9 %. T4 "Not needed · $8.7M".
- Tranche 2 and 3 show no NPV (doc 20 rule). The dates in the milestone line come from
  `InvestmentProjects[Completion Date]`; the cash-positive year from the existing payback measure.
- The Low line no longer uses Tangerine (R-G3).

Retired from this state: `hero_packages*` (3), `c_scatter_title`, `sl_view`, `c_guide*` (3), `z_tile_guide`,
`z_tile_rec`, `c_rec_title`, `c_rec_mix`, `c_rec_note`, `ch_rec_waterfall`, `ch_rec_cumulative`, `c_uncertainty`,
`tag_scatter`, `tag_rec_cum`. Removed from the files, not hidden (R-P2-9).

---

## 7 · P2 "What waits, and why"

### 7.1 The proof chart (R-W-1)

| Slot | x, y, w, h | Visual |
|---|---|---|
| `c_scatter_title_s` | 56, 184, 520, 56 | card, two lines: "We checked all 456 packages the rules allow: none beats A through 2032" |
| `tag_scatter_s` | 584, 188, 144, 28 | hover tag, "ⓘ Hover a dot" |
| `c_scatter_sub` | 56, 240, 672, 24 | text box: "Only 6 pay back by 2032, all under $15M. Each dot is a package." |
| `hero_s_packages`, `_named`, `_build`, `_hover` | 56, 272, 672, 368 | the existing small stack |

- The named layer keeps the lettered-disc route of the large stack if it fits at this size (R-W-4). If the
  letters fall beside the dots again (measured on 10 Nov), keep the tag under the dot; it is the lesser evil.
- Shaded band label: "Pays back by 2032" stays (R-G2 term).
- The check "A is the NPV maximum in all three scenarios" becomes a DAX assertion in the build log.

### 7.2 The panel: `tbl_waits` (R-W-2, N-3)

| Slot | x, y, w, h | Visual |
|---|---|---|
| `c_waits_head` | 792, 184, 1072, 56 | text box, two paragraphs: "What waits, and why" and the intro |
| `tbl_waits` | 792, 248, 1072, 392 | **table**, three rows, word wrap on, hairline between rows, header on |

Rows from a new `WaitOption` table (Key, Title, Sort): "B · Breakfast instead of kiosks", "Tranche 2 · Airport
extensions, +80 rooms", "Tranche 3 · The refresh of the 10 oldest hotels (in package C)".

| Column | Width | Measure |
|---|---|---|
| Option | 176 | the Title column, Night |
| The numbers | 208 | `Wait Numbers (text)`: four lines with a line break each, scenario-aware |
| Why it's on the table | 216 | `Wait Why (text)` |
| Why not now | 256 | `Wait WhyNot (text)` |
| When we decide | 216 | `Wait When (text)`; the gate rows use `Gate Rule Short (text)` |

Copy and values exactly as R-W-2. At these widths the longest cell (Tranche 3, why not now) takes five lines;
the table needs about 362 px of the 392.

### 7.3 The comparison chart (R-W-3)

`ch_cmp_alts` at 56, 688, 1808, 312, title inside the visual. A 3 px Coffee Blue, B 2 px Night, C 2 px Warm Grey
dashed. End labels by P-5, no legend, a tick below zero, zero line named by R-G2. `tag_cmp_alts` at 1712, 692.

Retired: `c_alts_title`, `c_alts_intro`, `img_b_chip`, `img_c_chip`, `c_b_*` (5), `c_c_*` (5), `z_tile_b`,
`z_tile_c`.

---

## 8 · P2 "Build your own"

| Slot | x, y, w, h | Visual | Content |
|---|---|---|---|
| `c_build_head` | 792, 184, 1072, 56 | text box | "Build your own" and "Click a move to add or remove it." |
| `sl_moves` | 792, 280, 216, 320 | **button slicer**, 10 rows, multi-select, square tiles, selection icon on | `BuildMove[Short Name]`, saved selection = A's three moves |
| `tbl_moves` | 1008, 248, 344, 352 | **table**, header 32 px + 10 rows of 32 px | Answers · Capex · NPV · A year by 2032, on `BuildMove`, same sort |
| `c_sel_footer` | 792, 608, 560, 24 | card | "Picked: 3 moves, $13.2M of $60.0M" |
| `z_tile_you` | 1368, 248, 496, 392 | frame, outline kind | |
| `c_you_title` | 1384, 256, 464, 40 | card | title and budget alarm (unchanged mechanism) |
| `c_you_nums` | 1384, 304, 464, 56 | card, four callouts | capex · NPV through 2032 · a year by 2032 · a year on cost |
| `c_you_range` | 1384, 368, 464, 24 | card | "−$8.3M to +$9.1M" (R-G1) |
| `c_you_rules` | 1384, 392, 464, 40 | card | the rules line |
| `ch_build_bars` | 1384, 440, 464, 192 | **bar chart**, horizontal | NPV of each picked move on `BuildMove[Short Name]`, sorted, labels by P-1, value axis hidden. Horizontal bars take the full short names, so the 12-character `Waterfall Label` column is no longer needed |
| `ch_cmp_build` | 56, 688, 1808, 312 | line chart | A Coffee Blue, your plan Night solid; end labels "A" and "You" |

- The slicer filters only the six build targets (edit interactions, the existing `interactions()` list with
  `ch_build_bars` in place of the waterfall). `tbl_moves` is **not** filtered by it, so all ten rows stay.
- The Build measures already read the selection with `ISFILTERED(BuildMove[…])` through `ALLSELECTED`, so they
  work with a slicer without change.
- Opening with A picked makes the empty state rare, but it must still be clean (deselect everything): the tile
  shows the R-B-2 sentence, no numbers, no chart. `Build … (text)` measures already return blank at n = 0; the
  bar chart has no rows then.
- The plan dot in the small scatter: Night, a ring. A native scatter marker cannot be hollow, so use a Night
  marker with a white `BuildPoint` label "You" drawn as the category label beside it. Over budget keeps
  Tangerine (R-B-3).
- Kiosks answer F4 (D4): change the `Answers` mapping in one place, the `MoveDecision` table (section 10.1).
- **S-3 result (13 Nov): pass.** `tbl_moves` at **1008, 237, 350, 363** with row padding 5.36 (the header becomes 43 px)
  and a hidden `Short Name` column; the slicer slot stays (section 13, "Results of the two big spikes").
- **S-3:** render the slicer and the table side by side. Pass = the ten rows line up within 1 px over the full
  height, the check icon shows on selected tiles, the saved selection survives a reload, Tab and Space select a
  tile. If it fails by the evening of 15 Nov: Deneb stays (N-1, technical fallback).

---

## 9 · Tooltip pages

| Page | Action |
|---|---|
| `tt-package` | Replace `tt_range_svg` by a card on `TT Range (text)` in the R-TT-1 wording. Replace `tt_moves_svg` by a native table (Move · Capex · NPV, body size, P-1 formatters, total row from a measure, not the visual's own total). Trim the page height to the content. **Fix the broken binding:** define `TT Payback Color` or drop the font-colour binding of `tt_payback` |
| `tt-f3-band`, `tt-f4-hotel` | Keep. Colour roles of R-G3 inside (R-TT-4) |
| `tt-year` | Keep. "Break-even" wording to R-G2. Your plan in Night |
| `tt-glossary` | R-TT-3 terms. Remove "Case in view" |
| `tt-f1`, `tt-f2`, `tt-f3`, `tt-f4` | Delete (N-4), with `canvas-tt-tt-f1…f4.jpg`, `finding_page_visuals()` and the `Facts Chip F# (text)` measures |

Tooltips at 1366 px: with `useScaledTooltips` a 480 px page shrinks with the canvas. The native table in
`tt-package` must stay at 12 pt; check its legibility at the gate (UX review, check 2).

---

## 10 · Model work list (`sketch_model.py`)

### 10.1 New tables and columns

| Object | Kind | Content | Note |
|---|---|---|---|
| `MoveDecision` | small table written by the generator | ProjectID, Finding ("F2"), Status ("A" / "2028 gate" / "not now"), Tranche (1, 2, 3, blank) | **Decision data, not source data** (D2, D4). Its docstring says so (invariant 5). The "A" rows are derived from preset A, not typed |
| `InvestmentProjects[Move Name]` | calculated column | the ten names of R-P2-3 | One naming source: `Move Name` (full) and `Short Name` (selector, build bars); `BuildMove[Waterfall Label]` goes |
| `InvestmentProjects[Hero Sort]` | calculated column | rank by Expected run-rate ÷ capex | fixed order |
| `Finding` | small table | Code, Name, Ledger Sort | drives the ledger |
| `WaitOption` | small table | Key, Title, Sort | drives `tbl_waits` |
| `Hotels[F4 Dot Label]` | calculated column | section 4.5 | top seven by 2025 occupancy computed in DAX |

### 10.2 New measures (each with docstring, display folder, format string; folder `15 Storytelling rebuild`)

| Measure | Definition (sketch) | Contract |
|---|---|---|
| `A Year on Cost` | `DIVIDE ( [2032 Run-rate], SUM ( InvestmentProjects[CapexUSD] ) )`, scenario-aware through `[2032 Run-rate]` | **Metric contract** (invariant 4): derived ratio, not a valuation |
| `Package A Year on Cost (sel)`, `Build A Year on Cost (sel)`, `Build Run-rate (sel)` | the same ratio on `[Package Run-rate (sel)]` and on the build selection (`BTREAT`) | same contract |
| `Move Yield (text)`, `Move Run-rate (text)`, `Move Status (text)`, `Move Status Color` | text and colour for hero and selector | |
| `Hero Yield Bar SVG`, `Hero NPV Bar SVG`, `Hero Domain Min/Max` | P-4 | `dataCategory: ImageUrl` |
| `Hero Title (text)`, `Alt Hero (text)` | R-P2-3, scenario variants in one grammar | |
| `Ledger Measure (text)`, `Ledger 2025 (text)`, `Ledger 2032 (text)`, `Ledger Status (text)`, `Alt Ledger (text)` | switch on `Finding[Code]`; numbers from `Dist Cost % 2032 with A (sel)`, `Margin after 2032 with A (sel)` | **Metric contracts** for the two 2032 values. Port the derivation of `analysis/50_storytelling_checks.py` section 6 to DAX (2025 brand + A's `DistributionCostChangePts` and `AnnualOperatingProfitImpactUSD`); assert E11 for Low, Expected, High |
| `Tranche 1…3 Capex`, `Not Needed Capex`, `Tranche 2/3 Run-rate`, `Tranche 2/3 Yield (text)`, `Plan T1…T4 (text)` | sums over `MoveDecision[Tranche]`; budget from `FinanceParameters` | segment sum asserted = budget |
| `Gate Rule (text)`, `Gate Rule Short (text)` | the gate copy, once | the only release rule in the model (P-8 check 4) |
| `Milestones (text)` | from completion dates and the payback year | |
| `Rec Lines (text)` | worst case (Low, always) + the app's share + the yearly leak (E13) | |
| `Wait Numbers / Why / WhyNot / When (text)` | switch on `WaitOption[Key]` | |
| `F3 Count (text)`, `F4 Row Y`, `F4 Dot Color`, `F4 Type Avg`, `Trend Commission Take GI`, `Trend OTA GI (ends)`, `Trend OTA Sisters (end)` | sections 4.2 to 4.5 | |
| `… (label-safe)` twins | P-1, for F3, the plan bar, the build bars, the line ends | |

### 10.3 Changed

- Copy measures of R-P1-1 to R-P1-6, R-P2-1, R-P2-6, R-B-1, R-TT-1, R-TT-3: new text, R-G2 vocabulary.
- `F1 Title (text)` and `KPI Margin after Context (text)`: unchanged logic (N-2); the note states 1.0 + 1.8.
- `Move Answers (text)`: reads `MoveDecision[Finding]`.
- All money text through `fm` / `sfm`; `fmc`, `fmc2`, `sfm2` removed (R-G1).
- Colour constants: F-codes and "your plan" to Night, the Low line and C's line to Warm Grey.

### 10.4 Retired, and the submission prune

- With their visuals: `ScatterView` (table), `Guide (text)`, `Scatter Title (text)`, the waterfall family
  (`Focus Project NPV (shown)`, `Waterfall …`, `Build Project NPV (shown)`, `Build WF …`), `Uncertainty (text)`,
  `Rec Note (text)`, `Alt B/C Why/WhyNot`, `Preset B/C Payback (text)`, `Facts Bar SVG`, `Facts Chip F#`,
  `Hover Tag … SVG`, `Definitions Pill SVG`, `Chip Plain`, `TT Range SVG`, `TT Moves SVG`, every old release-rule
  sentence (R-P2-10).
- **Submission prune (T3, last step before the PBIX is made):** a flag `sketch_model.py --submission` that writes
  only the measures reachable from `GoodnightInn-opzet.Report` and drops the helper tables that no remaining
  measure, column or visual reads. Today those are `BridgeStep`, `KpiLine`, `Timeline`, `PlanYear` and
  `HotelOutlook`; `PlanSelector` stays, seven live measures read it. Source tables from the workbook always stay.
  The reachability script decides, not this list, and it is the gate: 0 bound measures missing, 0 unreachable
  measures left. The default build keeps everything, so the sketches still open.

---

## 11 · Report generator work list (`opzet_report.py`, `pbir_lib.py`, layout files)

1. `opzet-layout.json` v10: the slots of sections 4 to 8; cards and tiles per state as in section 5. Take the
   coordinates from the approved artifact (section 12), not from this document, if they differ.
2. `opzet-layering.json`: new slots get z and tab values on the file's scale; removed slots leave the file.
3. New builders: `hero_table()`, `ledger_table()`, `waits_table()`, `plan_bar()`, `nav_button()`,
   `native_selector()` (rewrite of the existing fallback: slicer + table), `f4_dots()`, `text_tag()` (P-7),
   `link_line()`.
4. Changed builders: `button()` and `button_slicer()` take a `surface` and a `size` (P-2); `cumulative_chart()`
   loses the legend and gains end-label series; `f1_chart()`, `f2_chart()`, `f3_chart()` as in section 4;
   `kicker()` colour; `tt_visuals()`.
5. Removed: `scatter_stack("hero_packages", …)`, `waterfall()`, `facts_bar()`, `hover_chip()`'s SVG layer,
   `finding_page_visuals()`, the `tint` and `glow` tile kinds, `deneb_selector()` and
   `publicCustomVisuals` (N-1, once S-3 has passed).
6. Theme (`deliverables/theme.json` through `compile_theme.py`): `visualStyles` for `actionButton` and
   `advancedSlicerVisual` with the P-2 states for the light surface (the Night surface is the per-visual
   exception).
7. After every run: delete `PillowKey.SemanticModel/definition/cultures`; run `a11y_check.py`, `schema_check.py`
   and the new `build_checks.py`.

---

## 12 · Action 1: the Claude artifact of the fixed dashboard

**Purpose:** a clickable picture of the report as it will be built, so Bjorn can approve layout and copy before
any PBIR is written, and so the builder gets final coordinates.

**The rule that makes it useful:** the artifact shows only what this document specifies, built only from things
Power BI can draw. It is a constraint-true comp, not a redesign.

| Topic | Specification |
|---|---|
| Stage | A fixed 1920 × 1080 stage, scaled to the viewport with one CSS transform. No reflow, no responsive layout |
| Screens | P1; P2 in three states. The tabs, the scenario pills and the two navigation buttons work. The Build selector toggles moves and recomputes the tile, the bars and the line |
| Slot map | One `SLOTS` object in the page: slot name → x, y, w, h, state. The names are the slot names of sections 4 to 8. Every element is absolutely positioned from it |
| Data | From `project/design-prototypes/opzet-data.json` (`projects`: capex, NPV and run-rate per scenario, yearly net; `hotels`: type, occupancy; `packages`: the 456 dots) and the E-facts of doc 20 section 0 for the copy. A year on cost is computed in the page as run-rate ÷ capex. No number is typed twice |
| Tokens | Canvas `#F3F1EA`, card `#FFFFFF` radius 12 with one soft shadow, Night `#12233D`, Dusk `#4B5466`, hairline `#E3DFD3`, Coffee Blue mark `#2589D8` and text `#1763A8`, Warm Grey `#8E897D`, Tangerine `#E05A22`, Burnt Tangerine `#A63F0E`, masthead text `#F7F5EE` / `#C9D0DC`. Type: Segoe UI and Segoe UI Semibold with the report's fallbacks; 28 pt headline, 20 px card heads, 14 pt titles, 12 pt (16 px) floor |
| Masthead | Flat Night to y 168 is enough; the night-glow artwork is not needed to judge the layout |
| Power BI-true limits | Charts as plain SVG in the native idiom: straight lines, rectangular bars, circle markers, one reference line, labels at line ends. Tables as real HTML tables with fixed column widths (section 6.1, 6.2, 7.2). No animation, no gradient on a mark, no hover effect Power BI lacks. Text that does not fit its slot must **overflow visibly** (red outline), never shrink |
| Tooltips | Optional. If shown: the 480 px tooltip card for a dot, a hotel and a year, static content |
| Builder aids | A toggle "show slots" that outlines every slot and prints its name and x, y, w, h. A button "copy slot map" that puts the `SLOTS` JSON on the clipboard in the shape of `opzet-layout.json` |
| Acceptance | Each state shows exactly the elements of its section; R-G4 holds with tooltips off; no red overflow outline in Low, Expected or High; the five N-points are visible as approved (section 2.2) |

After Bjorn approves it, the copied slot map **is** `opzet-layout.json` v10. That is the link between action 1
and action 2.

**Hand-over between the two sessions (added 13 Nov).** The artifact session runs from a clone of GitHub, the
build session runs on Bjorn's machine because it needs Power BI Desktop. They only share what is pushed.

- Base for both: branch `claude/relaxed-noether-nwhfs9`. `main` is behind it and misses the current report.
- The artifact session saves the comp as `project/design-prototypes/rebuild-comp-v10.html` and, after Bjorn's
  approval, the slot map as `project/design-prototypes/opzet-layout-v10.json`. It commits both on its own working
  branch, pushes that branch and reports the branch name.
- The build session fetches that branch and creates `rebuild-finalv3` from it. `opzet-layout.json` itself is only
  changed by the builder (section 11, point 1).

---

## 13 · Action 2: taking it live (order for the builder)

Rules that do not change: the generators are the source of truth, commit before opening Desktop, no Desktop
saves, close every window yourself without saving, renders through the throwaway copy.

| Step | When | What | Gate |
|---|---|---|---|
| 0 | Fri 13 Nov | **Done:** Bjorn approved N-1 to N-5 (section 2.2; doc 20 amended). Docs 19 to 21 committed and pushed on `claude/relaxed-noether-nwhfs9` | answers recorded in this file |
| 1 | Fri 13 Nov | Artifact (section 12), approval, slot map v10 pushed (hand-over in section 12) | no overflow in any scenario |
| 2 | Sat 14 Nov, first | Spikes on a scratch page in a throwaway copy: **S-1** label-safe labels, **S-2** hero table, **S-6** navigation button shape, **S-7** line breaks in cells, **S-5** area transparency, **S-8** ⓘ glyph | each spike: pass, or its fallback chosen and written here |
| 3 | Sat 14 Nov | Model: section 10.1 to 10.3. DAX assertions for E9, E10, E11 in all three scenarios through the modelling MCP | values equal `storytelling_checks.txt` |
| 4 | Sat 14 Nov | T1 without layout risk: P-1 everywhere, both waterfalls gone, R-G2 words, R-G3 colours, the gate rule in one measure, P1 copy, navigation buttons, footer, `tt-package`, the broken binding | `build_checks.py` 4 of 4; nl-NL render of P1 shows points only |
| 5 | Sun 15 Nov | P2 frame (section 5), decision card with the ledger, capital plan | render Recommended × Low / Expected / High |
| 6 | Sun 15 Nov | Hero table. **S-3** native selector, **S-4** F4 dots | **cut line, evening:** hero or R-P2-3-FB; native selector or Deneb; native F4 or Deneb strip  **Decided 14 Nov (build step 7 of doc 23):** hero = the native table, verified in Low, Expected and High, no R-P2-3-FB; selector = native slicer and table (S-3 passed), Deneb goes in build step 9; F4 = the native dot plot (S-4 solved in build step 5), no Deneb strip. Bjorn confirms |
| 7 | Mon 16 Nov | What waits, Build, tooltips, alt texts, tab order, layering file | keyboard pass and Narrator pass logged (R-X-1); `a11y_check.py` 0 errors |
| 8 | Mon 16 Nov | Render set `screenshots/FinalV3/` (R-X-3). Submission prune (10.4). Parity check, contest compliance (R-X-2) | visual types present: line, area, column, bar, stacked bar, scatter, table |
| 9 | Tue 17 Nov | Publish to Web gate. **Bjorn publishes.** Checks: SVG cells in the hero, tooltips, page buttons, nl and de browser, visual headers against the hover tags, tooltip scale at 1366 px, one touch test | then submit |

Tier order inside each step follows doc 20: T1 before T2 before T3. If a day slips, drop T3 first
(R-P1-9, R-P2-11, R-W-4, R-TT-3/4, the submission prune), never the gate.

### Results of What waits (14 Nov, build step 8 of doc 23)

Built and verified against the comp in Low, Expected and High; the full log is in doc 23, step 8. What this document
said and what was built:

- **7.1, the named layer:** the lettered discs are kept (R-W-4), natively. Power BI sets a scatter label under its dot at
  this plot size, so the letters are a layer of their own: three invisible points a fixed $4.34M above the discs
  (`Named Letter NPV (sel)`), whose labels land inside the discs. The fallback (a tag under the dot) is not used. A's disc
  is Deep Coffee for its white letter (doc 23, open question 7).
- **7.1, the check:** A is the NPV maximum in all three scenarios (0 of 456 packages above it; DAX query, 14 Nov).
- **7.1, axes:** fixed from the spec ($5M to $62M, −$60M to +$20M), ticks in whole $M (`USDM0`, `SUSDM0` on the four
  scatter measures). `c_scatter_sub` is a card on `Proof Subtitle (text)`, not a text box: it follows the case.
- **7.2:** `tbl_waits` with doc 22's columns (168 / 224 / 216 / 256 / 208) at row padding 4.9; the header is 10 px taller
  than the comp's, so the table starts 10 px above its slot; a bottom outline on the values draws the last rule.
- **7.3:** `ch_cmp_alts` by `cmp_chart()` (doc 22 section 3: one label per line end, A Above, B and C Under). The value
  axis ends come from the model (`Cmp Alts Y Start`, `Cmp Alts Y End`, the comp's `niceTicks` with 8 % headroom); the
  first series (`Preset C Cumulative Line`) carries the whole-$M tick format. `tag_cmp_alts` is the native hover tag.

### Results of the hero table and the capital plan, and the cut line (14 Nov, build step 7 of doc 23)

- **Cut line, three decisions (Bjorn confirms):** (1) the hero is the native table of 6.1, verified in Low, Expected and
  High; R-P2-3-FB is not needed. (2) The Build selector is the native slicer beside a table (S-3); the Deneb visual and
  `publicCustomVisuals` go in build step 9. (3) F4 is the native dot plot of 4.5 (S-4, build step 5); no Deneb strip.
- **Sections 6.1 and 6.3 are built:** `p2_hero()` and `p2_capital_plan()` in `opzet_report.py`. Recommended is complete.
- **6.1, the hero table as built:** `tableEx` at 56, **244**, 1000, **374** (the slot is 56, 240, 992, 372). A native table
  is 32.5 px of header, 1 px of rule and ten rows of 34 px: 373 px, so at 372 it showed both scrollbars. A cell's text is
  set from the top of its row, 5.25 px above where the comp centres it; so the table starts 4 px lower and the bars sit
  5 px higher in their images (`HERO_TEXT_LIFT`: bar y 3 to 21 of 34). Row text, header text and bars are then within
  2 px of the comp; the header rule and the two reference lines are 4.5 px under the comp's. Status and NPV take their
  ink from `Move Status Ink` and `Move NPV Ink`. The two value columns carry a zero-width space as their header.
- **6.3, the plan bar:** a `barChart` needs a category: `Brands[Brand]`, one value under the page's brand filter. Value
  axis 0 to the budget (`Move Budget (num)`), `layout.stackedGapSize` 0 (without it 2.7 px of white between the
  segments), both axes off. Its visual rect is 56, 780, 1808, 40: Power BI keeps about 8 px above a bar.
- **6.3, the cumulative chart, three things Power BI decides:**
  1. **No label position Right** (doc 22 section 3). A line chart's data label goes Above or Under its point (the
     catalog, the theme schema and Microsoft's validator list the same enum). Built: Low Under, Expected and High Above,
     and Power BI moves a label sideways where it has room (High stands right of its line end). The emphasised line has
     one end series per case (`A Cumulative End Sel Low / Expected / High (label-safe)`), because a series has one
     position. Open question 6 in doc 23.
  2. **Two ticks, not four.** In 102 px of plot Power BI draws +$20M and $0M; the comp's -$10M and +$10M do not appear
     and there is no property for the tick step.
  3. **An axis format needs its decimal point.** `+\$#,0,,\M` printed "+$20.000.000M" (the commas do not scale without
     a point); `+\$#,0,,.\M` prints "+$20M". The thin lines carry that format (`SUSDM0`) and come first in the chart,
     so the axis is locale-safe (P-1 b).
  The names of the zero line and of the gate line are semibold (a constant line's label has no weight property, as F4's
  "90%" in build step 5). The label background is white from the theme (`compile_theme.py`, `lineChart` labels): the
  same fill inside the visual trips Microsoft's validator (PBIR_FORMATTING_PROP_NESTED), wrongly.
- **Multi-line labels with fixed breaks** (`c_plan_t1` to `t4`): one card per line at a 21.3 px pitch (`line_cards()`),
  as `c_rec_lines` in build step 6.
- **Measuring a table in a narrow window:** a tile seam through a table is no reference. At a fractional zoom Desktop
  snaps a visual by up to 1.6 page px, and a table's rows by a device pixel each. A scratch page that shows the table
  whole gives the real sizes (`tools/desktop_shots/step7/`).

### Results of page 2, frame and decision card (13 Nov, build step 6 of doc 23)

- **Sections 5 and 6.2 are built** on the v10 slot map (`opzet-layout-v9.json` is no longer read): `p2_frame()` and
  `p2_decision_card()` in `opzet_report.py`. Recommended matches the comp within 2 px in Low, Expected and High, with two
  exceptions that are Power BI's, listed below. The retired frame and Recommended visuals of sections 5 and 6.3 are out
  of the files, and so are `tt-f1` to `tt-f4` as pages (N-4; their canvases and measures go in step 10).
- **P-2 on the Night masthead** is set per visual (`ctl_button()` with the looks `night_on`, `night_off`, `light_sec`;
  `button_slicer(night=True)`): the theme carries the light surface only. Every state names its fill, text and outline;
  the slicer's hover and press states name their text colour too (`interaction:hover`, `interaction:press`).
- **A native table sets every cell at the top of its row** (no vertical alignment in the catalog), a ruled row carries
  1 px for its rule, and the header is taller than a row (34 px at row padding 0.5). So `tbl_ledger` uses row padding
  0.5 and starts 6 px above its slot: the four row tops are on the comp's, a one-line cell sits on the first line of
  its row where the comp centres it. The same will hold for `tbl_waits` (7.2) and `tbl_hero` has one-line rows only.
- **`c_rec_lines` is two cards** (S-7), 21 px apart; **`c_rec_nums`** takes the ink of its two signed numbers per
  measure (`value` with a `metadata` selector, bound to `Rec NPV Ink` and `Rec Run-rate Ink`).
- **The comp draws the three tab labels in regular weight** (its rule `#stage button {font: inherit}` outranks
  `.btn.lg {font-weight: 600}`); the report follows P-2 above, Segoe UI Semibold. Open question 5 in doc 23.

### Results of page 1 (13 Nov, build step 5 of doc 23)

- **S-4, pass with a different cure than doc 22 section 5 planned.** In its slot Power BI's F4 plot was 0.7 % wider and
  12 px shorter than the comp's, so shifting the seven name boxes could not work. Both scatter layers take the rect that
  puts Power BI's plot on the comp's (655, 863, 1200, 161); the boxes keep the spec's positions. No Deneb.
- **Three rules for the remaining pages** (details in doc 23, log of step 5): a cardVisual centres its text and hides
  lines that do not fit (two lines need 60 px, three 88: `note()`); a chart's slot is not its plot (`PLOT_RECT`); and in a
  narrow Desktop window only the tile render (`tools/desktop_shots/tiles/`) is a pixel reference.
- **P-2:** the light-surface control states are in the theme (`compile_theme.py`); a button's pill is
  `rectangleRoundedByPixel` on the `default` selector, not `pill`.

### Results of the model step (13 Nov, build step 3 of doc 23)

Section 10.1 and the number measures of 10.2 are in `sketch_model.py` (folder `15 Storytelling rebuild`, 56 measures;
`MoveDecision`, `Finding`, `WaitOption`; `Move Name`, `Hero Sort`). The assertions of step 3 in the table above run as
`python project/tools/number_checks.py --port <AS port>`: 763 checks against the workbook and the spec's `text` block
in Low, Expected and High, all pass; the one known difference is 20.5 against 20.6 % for the kiosks. Details, the
names of the end-label series and what the next steps must know: doc 23, step 3 log. Section 10.3 (the text
measures) and `build_checks.py` are build step 4.

### Results of the two big spikes (13 Nov, build step 2 of doc 23)

Run in a throwaway copy on four scratch pages, Desktop 2.159 in nl-NL. Proof, measures and method: doc 23, step 2
log; renders in `project/deliverables/screenshots/Spikes-step2-2026-11-13/`. Both feed the cut line of step 6 above.

| Spike | Result | Shape to build |
|---|---|---|
| S-2 | **Pass**, native table, no fallback | `tableEx`, columns **280 / 104 / 96 / 196 / 64 / 184 / 74**, visual 56, 240, **1000**, 372. `grid`: rowPadding 0, imageHeight 34, **imageWidth 173**, gridlines off. `columnHeaders.outlineStyle` `'BottomOnly'`. Both SVGs 173 x 34, every x = the comp's cell x minus 7. Lines measured at 573.6 and 925.1 (computed 573.84 and 925.09), unbroken over ten rows in Low, Expected and High, no scrollbar. The 72 px value column cut "−$12.2M" to "−$12.2…"; 74 holds it |
| S-3 | **Pass**, native slicer and table, Deneb can go (N-1) | Slicer 792, 280, 216, 320: 10 rows, cellPadding 0, tile shape `'rectangle'`, multi-select, selection icon 16 px in Night on the default **and** the selected state, saved selection in `general.filter`. Table **1008, 237, 350, 363**: `grid.rowPadding` **5.36**, columns `Short Name` at width 0 + **92 / 64 / 74 / 118**, `NoFilter` from the slicer. Tile pitch and row pitch 32.05 px, 0.44 px apart on all ten rows. Space and Tab work on a tile; a reload brings the saved selection back; nothing picked leaves ten rows and "Nothing picked yet" |

### Step 2 results: the five small spikes (13 Nov, build step 1 of doc 23)

Run in a throwaway copy on a scratch page, Desktop 2.159 in nl-NL. Proof and method: doc 23, step 1 log; renders in
`project/deliverables/screenshots/Spikes-step1-2026-11-13/`. S-2 belongs to build step 2.

| Spike | Result | Shape to build |
|---|---|---|
| S-1 | **Pass**, with two corrections to P-1 | The format string repeats the literal in three sections, `"""" & t & """;""" & t & """;""" & t & """"`. One section prints a negative value as "−−4.9". In TMDL, `formatStringDefinition` follows the measure's properties (display folder, lineage tag), in a backtick block; right after the expression the project does not open. U+2060 keeps "−" and "$" together in a wrapping table cell |
| S-5 | **Pass**, the fallback is not needed | `lineStyles`: `areaShow` false on the base series (`selector.metadata`), true on the band. `dataPoint`: `transparency` 70 without a selector |
| S-6 | **Pass** | `visualLink`: `show` true, `type` `'PageNavigation'`, `navigationSection` `'<page folder name>'`. Ctrl+click in Desktop navigated |
| S-7 | **Table cell: pass. Card value: fallback** | A table cell honours `UNICHAR(10)` with `values.wordWrap` on. A `cardVisual` value honours no break character (LF, CR+LF, U+2028, U+2029). `c_rec_lines` (6.2) becomes two cards, one per line |
| S-8 | **Pass** on Windows (Desktop, Edge) | "ⓘ" from a text box run and from a card measure; the SVG disc is not needed. One look on a phone at the Publish to Web gate |

---

## 14 · Requirement coverage

| Doc 20 | Built by | Doc 20 | Built by |
|---|---|---|---|
| R-G1 | P-1, 10.3, P-8 check 3 | R-P2-6 | 6.2 |
| R-G2 | 10.3, P-8 check 2 | R-P2-7, R-P2-10 | 6.3, K-6, N-5, P-8 check 4 |
| R-G3 | P-6, 4.1, 6, 7, 8 | R-P2-8 | 6.2 `btn_build_invite` |
| R-G4 | 6.1, 6.2, 6.3 (all static) | R-P2-9, R-P2-11 | 6, 13 step 7 |
| R-P1-1, R-P1-2 | 4.1 | R-P2-12 | 5 |
| R-P1-3 | 4.2, N-2 | R-W-1, R-W-4 | 7.1 |
| R-P1-4 | 4.3 | R-W-2 | 7.2, N-3 |
| R-P1-5 | 4.4 | R-W-3 | 7.3, P-5 |
| R-P1-6, R-P1-7 | 4.5, S-4 | R-B-1, R-B-2 | 8, N-1, S-3 |
| R-P1-8 | 4.1 to 4.5 `lnk_*`, `btn_next` | R-B-3, R-B-4 | 8, K-4 |
| R-P1-9 | unchanged KPI subline; 12 pt floor | R-TT-1 | 9 |
| R-P2-1, R-P2-2 | 5, P-2 | R-TT-2 | 9, N-4 (closed by removal) |
| R-P2-3, R-P2-3-FB | 6.1, K-1, S-2 | R-TT-3, R-TT-4 | 9 |
| R-P2-4 | 5, K-3, 6 | R-X-1, R-X-2, R-X-3 | 13 steps 7 to 9 |
| R-P2-5 | 6.2, K-2, 10.2 | | |

---

## 15 · What to take back to the template (pbi-atelier), after the contest

1. **P-1 from day one.** Decide the number grammar and the label-safe twin before the first chart; the locale
   problem here was built in on day one and found on day eight.
2. **Controls belong to the frame, not to a card**, and their states belong in the theme.
3. **A table before an overlay.** Whenever rows must align or text must flow, the native table is the layout
   engine Power BI has.
4. **A static state first, a tooltip second.** Build the page so it argues with every tooltip off, then add depth.
5. **`build_checks.py` in the validation sweep**: bound measures exist, vocabulary, formats, one rule one measure,
   and the reachability report with the dead-measure count.
6. **Prefer the native selector until a custom visual is proven in Publish to Web**, not the other way round.
7. **One comp, one slot map.** The artifact with a "copy slot map" button replaces the separate HTML comp
   pipeline (`build_opzet_comp.py`).

---

## 16 · Open items

| # | Item | Owner |
|---|---|---|
| N-1 to N-5 | Closed: approved on 13 Nov (section 2.2) | none |
| Comp and slot map v10 | Come back from the artifact session by push (hand-over in section 12) | artifact session, then Bjorn approves |
| S-1 to S-8 | Spikes, each with its fallback | builder |
| Publish to Web | SVG data URIs in table cells and in the A chip; the gate of R-X-3 | Bjorn publishes, builder checks |
| Earlier findings still open | `pbir_detect` header 4 px grid; the MS validator's scatter `categoryLabels` error (the small stack stays, so this stays) | builder, T3 |
