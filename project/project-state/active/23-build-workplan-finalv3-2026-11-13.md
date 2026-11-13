# 23 · Build workplan FinalV3: twelve steps, one prompt each (13 Nov 2026)

**For:** Bjorn and the local Claude Code sessions that build the approved rebuild.
**How to use:** one step per session, back to back, no schedule. Open Claude Code on the Windows machine (Power BI
Desktop is needed), pick the model and say "Read project/build-steps/next.txt and execute it" (or name a step file,
`step-01.txt` to `step-12.txt`). The session does that step only, writes its log below, updates the progress table,
commits and pushes. When it reports "ready for the next step", start a **new** session with `next.txt` again.
**Model:** Claude Fable 5.2 at effort high (alternative: Claude Opus 5.5 at effort xhigh). Same for every step.
**What is built:** exactly the comp `project/design-prototypes/rebuild-comp-v10.html`. Content: doc 20. Construction:
doc 21. Where doc 22 differs from doc 21, doc 22 is newer. Positions: `opzet-layout-v10.json`. Column widths, axes,
label positions and the exact text per view: `rebuild-v10-spec.json`.

**Timing:** none fixed; run the steps as fast as they pass. The estimates are agent time.

---

## 0 · Progress (each session updates its own row)

| Step | Title | Status | Date | Commit | Note |
|---|---|---|---|---|---|
| 1 | Branch and the five small spikes | done | 13 Nov | 3bbc28e | S-1, S-5, S-6, S-8 pass; S-7 pass in a table cell, fallback for a card (`c_rec_lines` as two cards). Bjorn was not needed in Desktop |
| 2 | The two big spikes: hero table and native selector | done | 13 Nov | f7f3afc | S-2 and S-3 pass natively, no fallback. Both tables need a few pixels the comp did not plan (wider value columns, 2 px of slack, `tbl_moves` 11 px higher); see the log. Bjorn was not needed in Desktop |
| 3 | Model foundations and the number checks | done | 13 Nov | c404091 | 56 number measures, 3 tables, 2 columns; 763 checks, all pass in Low, Expected and High, 1 known difference (open question 1). New: a measure cannot carry a static and a dynamic format string; open question 3 (hero caption). Bjorn was not needed in Desktop |
| 4 | Text measures and `build_checks.py` | todo | | | |
| 5 | Page 1 | todo | | | |
| 6 | Page 2 frame and the decision card | todo | | | |
| 7 | Hero table and capital plan; the cut line | todo | | | |
| 8 | What waits, and why | todo | | | |
| 9 | Build your own | todo | | | |
| 10 | Tooltips, alt text, tab order | todo | | | |
| 11 | Final checks and the FinalV3 render set | todo | | | |
| 12 | Publish to Web gate (Bjorn publishes), then submit | todo | | | |

Status values: `todo`, `doing` (stopped mid-step; see its log), `done`, `blocked` (needs Bjorn).

---

## 1 · Rules for every step (binding)

1. **Branch:** `rebuild-finalv3` (step 1 creates it from `origin/claude/laughing-mendel-ruw64g`). Pull before work,
   push at the end. Never push to `main`, never open or merge a pull request unless Bjorn asks.
2. **Read first:** `CLAUDE.md`, this document (section 1, the progress table, your step), then only the sources your
   step lists. The previous step's log tells you where things stand.
3. **One step only.** Do not start the next step's work, even if there is time left; report instead.
4. **Generators are the source of truth.** Only the `pbir-operator` agent changes `project/pbip/`, through
   `opzet_report.py`, `sketch_model.py`, `pbir_lib.py`, `compile_theme.py`. Small diffs; run `schema_check.py` and
   `a11y_check.py` after each batch (and `build_checks.py` from step 4 on). **Every step ends green:** the generators
   run, the checks show no new errors, the report opens.
5. **Research first.** Verify every PBIR and TMDL property against its `$schema` or Microsoft Learn before writing it.
   Shapes that only Desktop knows (spikes S-5, S-6) are authored once in a throwaway copy and read back.
6. **Desktop discipline.** Commit before opening Desktop. Never save in Desktop; close every window without saving.
   Renders and click tests run in the throwaway copy (doc 16, "Werkwijze renders"; `project/tools/desktop_shots/`).
   Delete `PillowKey.SemanticModel/definition/cultures` after every `opzet_report.py` run.
7. **Build to the comp.** After every render, lay it over the comp at the same view and scenario (±2 px; skill
   `px-prototype`) and compare the visible text with `rebuild-v10-spec.json` → `text`. Text that wraps where the comp
   does not, or labels that meet, go back to the comp first (doc 22 rule 2), never into the report.
8. **Copy is approved.** Do not rewrite it. If something cannot be built as specified, take the technical fallback
   doc 21 names, record it in your log, and tell Bjorn.
9. **Layout switch, page by page:** step 5 copies `opzet-layout-v10.json` over `opzet-layout.json` (doc 21 §11.1)
   and keeps the old file as `opzet-layout-v9.json`, read for page 2 only until step 6 moves page 2 over. From step 6
   on, P2 states that are not rebuilt yet may show only their frame; the generator must still run.
10. **Cut line (doc 20 §1):** if the hero table cannot be verified in step 7, switch to R-P2-3-FB. Tier order
    T1 before T2 before T3; when time runs short, drop T3 first, never a gate.
11. **Never publish.** Publish to Web is Bjorn's, on 17 Nov.
12. **Close-out (every step):** write your step's log below (built · verified, with the render or check that proves
    it · deviations from the comp and why · open items), set the progress row, commit, push, and end your reply with
    five lines: built · verified · deviations · what Bjorn must do · ready for the next step yes/no.

---

## 2 · The steps

### Step 1 · Branch and the five small spikes (about 1 to 1.5 h)

**Goal:** the build branch exists, and the five small unknowns are settled before anything depends on them.
**Sources:** doc 21 §3 (P-1, P-2, P-3, P-7), §4.2 (S-5), §13 step 2; doc 22 §1 rule 4.
**Do:** in a throwaway copy, on a scratch page:
- **S-1** a label-safe number (`formatStringDefinition` returning the finished text): render in nl-NL; pass = "+6.8" and
  "−4.9" with points, and "−$0.6M" (U+2060 between sign and `$`) on one line.
- **S-5** per-series area transparency for the F1 stacked area: Bjorn sets it once in Desktop, the session reads the
  JSON back. Fallback (doc 21 §4.2): two lines, band shaded under "Before commissions".
- **S-6** a page-navigation `actionButton`: Bjorn inserts one in Desktop, the session copies the `visualLink` shape.
- **S-7** a line break (`UNICHAR(10)`) inside a table cell and a card value, word wrap on.
- **S-8** "ⓘ" (U+24D8) from the Segoe UI stack in Desktop and in a browser. Fallback: the SVG disc, restyled to D5.

**Not in this step:** any change to the real report or model.
**Bjorn:** in the throwaway copy only, set the area transparency (S-5) and insert a page-navigation button (S-6), then
save that copy (the only save allowed, and only in the throwaway copy).
**Done when:** `rebuild-finalv3` is pushed; S-1, S-5, S-6, S-7, S-8 each recorded as pass or fallback, here and in doc 21
§13 step 2.

**Prompt:** `project/build-steps/step-01.txt` (say: "Read project/build-steps/step-01.txt and execute it").

**Log (Fri 13 Nov 2026, one session, done):**

*Built.* Branch `rebuild-finalv3` from `origin/claude/laughing-mendel-ruw64g`, pushed. A throwaway copy in the session
scratchpad with one scratch page (`spike`) and fifteen spike measures; nothing in `project/pbip/` changed. The copy
builder, the click test and the browser page are kept in `project/tools/desktop_shots/spikes_step1/`
(`spike_prep.py <pbip dir> <dest dir> [--report-only]`, `s6_click.ps1`, `s8_browser.html`). Property names came from
Microsoft's catalog (`powerbi-report-author formatting describe-object | search`), not from memory.

*Verified* (Desktop 2.159, Windows culture nl-NL; renders in `project/deliverables/screenshots/Spikes-step1-2026-11-13/`):

| Spike | Result | Proof | What the builder must do |
|---|---|---|---|
| S-1 label-safe number | **pass, with two corrections** | render 02: "+6.8", "+3.8", "−4.9" next to today's "+6,8", "−4,9"; "−$0.6M" and "$0.0M" on a column, a bar and a card | (1) The format string needs the literal in **all three sections** (`"t";"t";"t"`). With one section a negative value gets a second sign: "−−4.9" (seen on the column chart). (2) In TMDL `formatStringDefinition` goes **after** the measure's own properties, in a backtick block. Directly after the expression Desktop refuses to open the project ("Invalid indentation") |
| S-1 minus and `$` on one line | **pass** | render 02 and 03, table columns "Wrap, joiner" / "Wrap, no joiner": without U+2060 the cell breaks after "−" on every other line, with it never | keep U+2060 in `fm` and `sfm` |
| S-5 area per series | **pass, no fallback, Bjorn not needed** | render 01, top chart: "After commissions" is a line without a fill, the commission band is grey at 70 %; the bottom chart is the same visual without the two properties | `lineStyles.areaShow` = false with `selector.metadata` of the base series (true on the band) and `dataPoint.transparency` = 70 (no selector) |
| S-6 page-navigation button | **pass, Bjorn not needed** | Desktop lists the button as "Paginanavigatie … CTRL+klik hier om volgen"; a Ctrl+click moved the selected page tab from the spike page to "The Investment Strategy" (`s6_click.ps1` prints NAVIGATED) | `visualContainerObjects.visualLink`: `show` true, `type` `'PageNavigation'`, `navigationSection` `'<page name>'` (the folder name, here `p2-investment-strategy`) |
| S-7 line break, table cell | **pass** | render 03: "First line GI-01 / Second line" in a 232 px column that fits both on one line; also in a table that holds one measure only | `UNICHAR(10)`, `values.wordWrap` true |
| S-7 line break, card value | **fallback** | render 03: the card prints `UNICHAR(10)` and CR+LF as a space, U+2028 and U+2029 as nothing; text wrap on | a card never carries a break. This hits `c_rec_lines` (doc 21 §6.2, slot 1112, 312, 752, 48): build it as two cards, one per line (see open items) |
| S-8 "ⓘ" (U+24D8) | **pass** on Windows | render 03: text box in Tangerine, card chip, 30 pt, on Night; render 04: Edge with the report's font stack, without Segoe UI, and plain sans-serif | text box runs and the card measure as P-7 says; no SVG disc needed |

*Checks.* `powerbi-report-author validate` on the copy: 1 error, the known one (`hero_s_packages_named`, scatter
`categoryLabels`), none from the spike page. `a11y_check.py`: 0 failures. `schema_check.py`: 0 failing. The project was
not opened in Desktop and the generators were not run (nothing changed that they write).

*Deviations from the comp.* None; nothing was built in the report.

*Open items for later steps.*
- **Step 6, `c_rec_lines`:** doc 21 names no fallback for a card that cannot break. Chosen here: two cards in the same
  slot, one text measure per line, the second card 21 px below the first so the line pitch matches the comp (a 24 px
  pitch would put line 2 about 3 px low). The alternative, a table with one measure, also breaks correctly, but a table
  has no property to switch its header off.
- **Step 5, F1:** the series labels of the stacked area chart come with a grey label background by default; switch it
  off when the chart is built.
- **Step 12:** "ⓘ" is proven on Windows only (Desktop and Edge). Look at it once in the published report on a phone.
- **Work method:** `powerbi-desktop reload` only works when the `.pbip` and the `.Report` folder share a name. A model
  change still needs a close and reopen of the copy. The "Niet opslaan" button could not be pressed through UI
  Automation this time; the throwaway window was ended with `Stop-Process` (throwaway only, never the project).
- **Before the session:** the working tree held a Desktop save of the project from 13 Nov 14:06 (236 files, Desktop
  artefacts only, no measure changed). It is parked in `git stash` ("Desktop-save 2026-11-13 14:06"), nothing lost.

### Step 2 · The two big spikes: hero table and native selector (about 1.5 to 2 h)

**Goal:** know early whether the two riskiest constructions work natively; both feed the cut line.
**Sources:** doc 21 §3 P-4, §6.1 (S-2), §8 (S-3); doc 22 §3 (hero domains −10 % to 90 % and −32 to +12 $M, status
colours); spec `construction.tables.tbl_hero` and `tbl_moves`.
**Do:** in the throwaway copy, alone on scratch pages (spike measures live in that copy only):
- **S-2** the hero table: SVG bar cells from a `bar_cell()` prototype, columns 280/104/96/196/64/180/72, header 32,
  rows 34, row padding 0. Pass = the reference lines run unbroken down ten rows, no scrollbar, values aligned.
- **S-3** the native selector: multi-select button slicer (square tiles, selection icon on) beside a ten-row table,
  rows 32 px, saved selection = A's three moves. Pass = rows aligned within 1 px over the full height, check icon on
  selected tiles, the saved selection survives a reload, Tab and Space select a tile.

**Not in this step:** the real model or report.
**Bjorn:** a reload of the throwaway copy and one keyboard try (Tab, Space) on the slicer.
**Done when:** S-2 and S-3 recorded as pass or fallback (S-2 fallback: two bar charts; S-3 fallback: Deneb stays,
doc 21 N-1), here and in doc 21 §13.

**Prompt:** `project/build-steps/step-02.txt` (say: "Read project/build-steps/step-02.txt and execute it").

**Log (Fri 13 Nov 2026, one session, done):**

*Built.* A throwaway copy in the session scratchpad with four scratch pages (`s2-hero-expected`, `-low`, `-high`,
`s3-selector`), three spike columns on `InvestmentProjects` and twelve spike measures; nothing in `project/pbip/`
changed. The tools are kept in `project/tools/desktop_shots/spikes_step2/`: `spike2_prep.py <pbip dir> <dest dir>
[--report-only] [--diag] [key=value …]` (holds the `bar_cell()` prototype and both table builders),
`measure.py hero|selector <png>` (row pitch, reference lines, scrollbars, tile against row) and `s3_keys.ps1`
(Space, Tab and click on a slicer tile). Before the work, the step files were merged in from
`claude/laughing-mendel-ruw64g` (69121c6): they had landed there after this branch split off.

*Verified* (Desktop 2.159, Windows culture nl-NL; renders in `project/deliverables/screenshots/Spikes-step2-2026-11-13/`;
all measures taken from bridge captures at 2.29 capture pixels per page pixel):

| Spike | Result | Proof | What the builder must do |
|---|---|---|---|
| S-2 hero table | **pass, native, four corrections** | renders 01 to 03 (Expected, Low, High): both reference lines unbroken over the ten rows (340 px), at page x 573.6 and 925.1 against 573.84 and 925.09 computed; no scrollbar; values right-aligned and complete, "+$0.03M" and "−$30.5M" included; row pitch 34.0, header 32.6. Render 04 shows the line across row boundaries, enlarged | see the four points below |
| S-3 native selector | **pass, native, three corrections** | render 05: tile pitch 32.05 and row pitch 32.05, row centre minus tile centre 0.44 px on all ten rows (spread 0.01); check icon on A's three tiles; "Picked: 3 moves, $9.4M of $60.0M". Render 06: Space on "Breakfast upgrade" gives four moves. Render 07: after a reload the saved three are back (the table was still loading in that capture). Render 08: nothing picked, the table keeps its ten rows | see the three points below |

**S-2, what the hero table needs** (`tbl_hero`, doc 21 §6.1):
1. **Image size sits in `grid`, and the width must be set.** `grid.imageHeight` 34 and `grid.imageWidth`. With the
   height alone Desktop fits each bar into a 34 px square (the "squared image cell" of 10 Nov).
   `pbir_lib.table_objects()` writes both into `values`; move them to `grid`. The width is one value for the whole table.
2. **An image is drawn 7 px from the left edge of its cell, and its column must be the image + 11 px.** At image
   + 9 Desktop draws a clipped ellipsis mark beside the image. So both bar images are **173 px wide** (the narrow
   bar column of the comp, 180, minus 7), every x inside the SVG is the comp's cell x minus 7, and the NPV bar column
   is **184**, not 180. With that offset the lines land where `lbl_hero_8` and `lbl_hero_0` expect them.
3. **A text cell pads about 7.7 px left and 5 px right** (the comp counted 5 and 5). "−$27.3M" is 60 px wide: the
   last column must be **74**, not 72, or the three long values end in "…".
4. **The visual is 2 px wider than its columns.** At exactly the column sum Desktop shows a horizontal scrollbar,
   and then a vertical one. The height of 372 holds.

Built that way: columns **280 / 104 / 96 / 196 / 64 / 184 / 74**, visual **56, 240, 1000, 372**, row padding 0, grid off,
`columnHeaders.outlineStyle` `'BottomOnly'` in Dusk (1 px), auto-size off. Other shapes that worked: the status and
NPV font colours as `values.fontColor` bound to a measure (selector: `dataViewWildcard` + `metadata`), Answers in
Dusk through `columnFormatting.fontColor`, the two empty headers as a zero-width space, the order through
`Move Name` sorted by `Hero Sort` in the model (no sort in the visual). `Hero Sort` is a calculated column without
context transition (column-only tables, `SUMX ( FILTER ( InvestmentScenarios … ) )`).

**S-3, what the selector needs** (`sl_moves`, `tbl_moves`, doc 21 §8):
1. **Slicer:** `layout` rowCount 10, columnCount 1, maxTiles 10, cellPadding 0; `shapeCustomRectangle.tileShape`
   `'rectangle'`; `selection.singleSelect` false; `selectionIcon` show, size 16, position Left, **colour Night on the
   default and on the `selection:selected` state** (without the second one the checked box is white on white);
   `fillCustom` white when selected, Seam on hover; the saved selection as `general.filter` (In, the three short
   names of A). The slot 792, 280, 216, 320 stays.
2. **Table rows of 32 px need `grid.rowPadding` 5.36** (a 12 pt line is 21.28 px; Desktop honours the fraction).
   **The header takes the same padding and becomes 43 px** (32.6 at padding 0), so the table starts at **y 237**, not
   248, with height 363: then row 1 starts at 280, beside the first tile.
3. **Columns 92 / 64 / 74 / 118 and 2 px of slack: 1008, 237, 350, 363.** The table also needs one `BuildMove` column
   to get a row per move: `Short Name` at `columnWidth` 0. Nothing shows, and a screen reader reads the name with
   the row. `visualInteractions`: `sl_moves` to `tbl_moves` = `NoFilter`.

The Build measures read the slicer as they are: no selection means no filter, so `ISFILTERED` is false and the title
says "Nothing picked yet". **Keyboard:** every tile is a focusable button with a toggle state. With the focus on
"Breakfast upgrade", Space switched it from off to on; Tab moved the focus to "Gatwick +40 rooms"; Space switched
that one on. The focus was set through UI Automation and the keys were posted to the report's render widget
(`s3_keys.ps1`), so Bjorn was not needed. Not tested here: the walk from the page into the slicer with a real
keyboard (Tab to the visual, Enter). That is part of the keyboard pass of step 10.

*Checks.* `powerbi-report-author validate` on the copy: 1 error, the known one (`hero_s_packages_named`, scatter
`categoryLabels`), none from the scratch pages. `a11y_check.py`: 0 failures. `schema_check.py`: 0 failing. The project
was not opened in Desktop and the generators were not run (nothing changed that they write). The final renders 01 to
05 come from a copy rebuilt from scratch with the committed script.

*Deviations from the comp* (nothing is built yet; these are what steps 7 and 9 will meet):
- **Hero:** the table runs to x 1056 instead of 1048 and the NPV values end 7 px further right (1051 against about
  1043). Bars, reference lines and both reference labels are on the comp's positions. Text in the other columns
  starts 2.7 px right of the comp (cell padding).
- **Selector:** the four header labels of `tbl_moves` sit 9 px higher than in the comp (table at y 237), and the
  table ends at x 1358 instead of 1352 (the tile frame starts at 1368).
- The slot map and the spec still hold the comp's numbers (`tbl_hero` 992 wide, 180 / 72; `tbl_moves` 1008, 248,
  344, 352 and 72 / 116). They were not changed in this step: the comp is Bjorn's approved contract.

*Open items for later steps.*
- **Step 3 or 4, one number:** the kiosks' Expected "a year on cost" is exactly 20.55 % ($411,000 on $2.0M). DAX
  prints **20.6 %**; the comp and the spec print **20.5 %** (a rounding accident of the browser; in High it rounds
  30.85 up to 30.9). The hero title carries this number. See "Open questions".
- **Step 7:** the 173 px image shows a yield up to 83.6 %. The highest value in the data is 82.1 % (the app, High).
  The domain of −10 % to 90 % stays; a value above 83.6 % would be cut off at the image's edge.
- **Step 7, row seam:** at a fractional zoom each row boundary shows one half-tone pixel in the line (render 04);
  at 100 % there is none. Look at it once in the browser at the Publish to Web gate (step 12), with the SVG cells.
- **Step 9:** "Picked: 4 moves, $13.65M" still comes from the old two-decimal formatter (`Build Capex (text)`);
  step 4 replaces it. Capex "$15.0M" and NPV "−$12.2M" stand 4 px apart in `tbl_moves`; it fits, but there is no room left.
- **Work method:** a bridge capture also holds Desktop's canvas margin and the pane strip, so `measure.py` finds the
  page through two Night squares in the page corners. `powerbi-desktop reload` keeps the open page; `s3_keys.ps1`
  selects the page tab first. A changed measure reaches the running copy through the modelling MCP
  (`measure_operations` Update), a changed calculated column needs a rebuild and a reopen. The first capture after
  opening can be empty: take it again. The throwaway windows were ended with `Stop-Process` (throwaway only).

### Step 3 · Model foundations and the number checks (about 2 h)

**Goal:** the model holds every number the rebuild shows, re-derived, asserted in all three scenarios.
**Sources:** doc 21 §10.1, §10.2 (number measures), §3 P-1 and P-4; doc 22 §3; `analysis/50_storytelling_checks.py`
and `analysis/output/storytelling_checks.txt`; skills `tmdl-patterns`, `dax-patterns`, `ms-authoring`.
**Do** (in `sketch_model.py`, then validate):
- §10.1 tables and columns: `MoveDecision`, `Move Name`, `Hero Sort`, `Finding`, `WaitOption`.
  `Hotels[F4 Dot Label]` is **not** needed (doc 22 §3).
- P-1 formatters `fm`, `sfm` (U+2060 between sign and `$`), `pct1`, `pt1`; the `label_safe()` helper.
- Number measures: a year on cost (package, move, build), tranche sums and yields, ledger 2032 values (port section 6
  of the checks script), hero bar SVG measures and domains (S-2 result), label-safe twins for F3, the build bars and
  the line-end labels (name and value in one string, doc 22 §3). No twins for the plan bar (its labels are off).
- Metric contracts (invariant 4) for "a year on cost" and the two ledger 2032 values.
- DAX assertions for E9, E10, E11 in Low, Expected and High (modeling MCP, or DAX query view).

**Not in this step:** text measures, visuals.
**Bjorn:** none, unless the modeling MCP needs Desktop open (read-only).
**Done when:** the model validates; every assertion equals `storytelling_checks.txt`; the current report still opens
with no broken binding.

**Prompt:** `project/build-steps/step-03.txt` (say: "Read project/build-steps/step-03.txt and execute it").

**Log (Fri 13 Nov 2026, one session, done):**

*Built* (all in `sketch_model.py`; the model regenerated: 33 tables and 518 measures, was 30 and 462; the report
generator was run and writes the same report as before):

- **Tables and columns (10.1).** `MoveDecision` (ProjectID, Finding, Status, Tranche): a calculated table without a
  relationship. Finding and the two gate tranches are typed once in the generator as decision data (`MOVE_FINDING`,
  `MOVE_GATE`); status "A" and tranche 1 are read from `Package[Preset]`. `Finding` (Code, Name, Label, Ledger Sort) and
  `WaitOption` (Key, Title, Sort) as row sources. `InvestmentProjects[Move Name]`, sorted by `[Hero Sort]`.
  `[Answers Finding]` now reads the same mapping as `MoveDecision`, so the kiosks answer F4 (D4) everywhere.
  `Hotels[F4 Dot Label]` was not built (doc 22).
- **Formatters (P-1).** `fm` and `sfm` follow the comp's rule: one decimal, two decimals only where one would print 0.0
  ("+$0.03M"), `en-US` in every FORMAT, the word joiner after the sign. New: `pct1`, `pt1`, `label_safe()`. `m()` takes
  `fmt_def=` and writes `formatStringDefinition`. 36 existing text measures changed their expression through `fm` and
  `sfm`; what they print is the same, except a non-zero amount under $0.05M.
- **56 measures in folder `15 Storytelling rebuild`:** a year on cost (move, package, A, build, tranches), `Rec NPV Low`,
  `Rec Run-rate Low`, `Build Run-rate (sel)`, `Move Run-rate (num)`, `Move Status Color`; the hero bar cells
  (`Hero Yield Bar SVG`, `Hero NPV Bar SVG`, through `bar_cell()` with the S-2 geometry) and four domain measures; tranche
  capex, run-rate and yield, `Not Needed Capex`; the ledger (`Dist Cost % 2032 with A (sel)`,
  `Margin after 2032 with A (sel)`, the two status shares, `App Commission Saving / NPV / Run-rate (sel)`); the
  cumulative lines of A per case and nine end-label series; label-safe twins for F3 and the build bars, `Build Bar Color`;
  page 1: `Trend Commission Take GI`, `Trend OTA GI (ends)`, `Trend OTA Sisters (end)`, `F4 Row Y`, `F4 Dot Color`,
  `F4 Type Avg`, `Months Topped 90% (last 24)`.
- **Metric contracts** (invariant 4) in `project-state/active/metric-contracts/`: M-101 a year on cost, M-102 distribution
  cost 2032 with A, M-103 margin after commissions 2032 with A.
- **Tools:** `tools/number_checks.py` (the assertions, with `run_dax.ps1`), `tools/engine_probe.ps1` (asks Desktop's
  engine why it refuses a model, and lists every object with an error), `tools/desktop_shots/throwaway_copy.py`.

*Verified.*

| What | Result | Proof |
|---|---|---|
| The model validates | `validate_tmdl --strict`: 0 errors, 11 warnings, all "no formatString" on the eleven label-safe measures (expected, see below). `engine_probe.ps1`: Desktop's engine accepts the model, 0 objects with an error. The copy opens and refreshes in 7 s | repeatable with the two commands |
| Every assertion equals `storytelling_checks.txt` | `number_checks.py`: **763 checks, 762 ok, 1 known difference, 0 failed**, in Low, Expected and High. Against the workbook, re-derived with pandas to nine digits: E9 (a year on cost and profit a year of the ten moves; package A 11.1 / 37.5 / 66.0 %; tranche 2 11.7 / 13.8 / 14.8 %; tranche 3 4.5 / 7.9 / 11.5 %), E11 (distribution cost 11.3 % to 10.7 / 10.1 / 9.5 %; margin 33.7 % to 34.1 / 35.1 / 36.1 %; the app saves $1.2M / $2.4M / $3.6M a year), E5 (17, 14, 13 and 0 months), the F4 row of all 50 hotels by the comp's rule, the seven Night dots. Against the spec's `text` block, as the model's formatters print it: E10 (A: $9.4M, NPV −$5.5M / +$3.3M / +$12.7M, +$1.0M / +$3.5M / +$6.2M a year), the hero table (order, status, yield and NPV, 30 rows), the plan segments (9.4 + 12.4 + 29.5 + 8.7 = 60.0), the end labels of the three cumulative charts, the selector table (120 cells), the build bars, the F2 and F3 labels | `project/analysis/output/number_checks.txt` |
| The hero domains hold | the model's own minimum and maximum over ten moves and three scenarios, rounded outward, equal −10 % to 90 % and −$32M to +$12M; all 60 bar cells are well-formed SVGs with the reference line at its constant x. `hero_ref_x()` returns 573.84 and 925.09, the x values of step 2 | same file |
| The current report still opens, no broken binding | both pages render complete on the new model in the throwaway copy; `a11y_check.py` 0 failures; `schema_check.py` 198 files, 0 failing; `validate_json` 0 errors; `opzet_report.py` writes an identical report | `deliverables/screenshots/Step3-model-2026-11-13/`, 01 and 02 |
| A label-safe label from the generator | the F3 chart of the copy, bound to `NPS 2025 (label-safe)`, prints "−4.9" with a point in the nl-NL Desktop; the F4 bars beside it still print "87,4%" | same folder, 03 |

The renders are small: this session's screen was 540 px wide, so the page was captured at about 1000 px. Enough to see
that every visual draws; not a pixel reference.

*Found on the way (binding for the next steps).*

1. **A measure cannot carry `formatString` and `formatStringDefinition` together.** Desktop refuses the whole project
   ("Er zijn problemen gevonden"; the dialog's text cannot be read by script). The engine's own message: "zowel de
   eigenschap FormatString als de eigenschap FormatStringDefinition ... wordt niet ondersteund". So a label-safe
   measure has no static format string, and `validate_tmdl --strict` gives one warning for each: expected, not a
   defect. The validator is a framework file and was left alone (a template item for doc 21 section 15).
2. **`after` and `typed` are reserved words in DAX.** A measure and a calculated table failed on them as variable
   names. TMDL parses them, Desktop's engine does not. `engine_probe.ps1` shows this in seconds: run it before an open.
3. **The cumulative end series must come after the line series** in a chart whose value axis shows: the axis takes
   the first series' format, and a label-safe series would print its literal on every tick (P-1).
4. **A Desktop that refused a project keeps running as "Naamloos".** Its engine is the one the probe can use.

*Deviations from the comp.* None; nothing was built in the report. One change shows in today's report: the kiosks'
answer reads F4 instead of F3 (plan table, selector, the recommendation's note "F2, F4, F1"). That is D4, through the
shared mapping.

*Open items for later steps.*
- **Step 4:** the text measures can read every number from folder 15. `Move Answers (text)` must read
  `MoveDecision[Finding]` (10.3); `fmc`, `fmc2` and `sfm2` are still used by old measures and go there. The ledger's
  status words switch on `Dist Cost Rise Undone % (sel)` (0.25 / 0.50 / 0.75) and `Margin Fall Recovered % (sel)`
  (0.14 / 0.50 / 0.87). `number_checks.py` with `run_dax.ps1` is the base for the fifth check of `build_checks.py`.
- **Step 4, open question 1** (20.5 or 20.6 %) is still open; the model prints 20.6 %.
- **Step 5:** `F4 Row Y` returns the row for a location type and the stepped row for a hotel, so both layers bind one
  measure. `F4 Dot Color` reads the hotel's brand, so it needs no page filter of its own.
- **Steps 7 to 9:** the end series are `A Cumulative End Low / Expected / High / Sel (label-safe)`,
  `Preset A / B / C Cumulative End (label-safe)`, `A Cumulative End Name (label-safe)` and
  `Build Cumulative End Name (label-safe)`. The thin lines are `A Cumulative Line (Low / Expected / High)`, blank for the
  case in view. The plan bar binds `Tranche 1 / 2 / 3 Capex` and `Not Needed Capex`.
- **Step 7, open question 3:** the hero caption's second sentence (see "Open questions").
- **Step 11:** the prune must keep a measure that only a dynamic format string reads.
- **Work method:** `throwaway_copy.py` leaves the caches out; after the open, `refresh_desktop_model.ps1` loads the data
  in seconds, without a click. The modelling MCP writes the `.bim` the probe needs (ConnectFolder, then
  ExportToBimFile). The throwaway windows were ended with `Stop-Process` (throwaway only). A heredoc in the Bash tool
  eats backslashes and trips over quotes: edit Python and Markdown with the Edit tool.

### Step 4 · Text measures and `build_checks.py` (about 2 h)

**Goal:** every sentence on the canvas comes from one measure and matches the approved text in every scenario.
**Sources:** doc 20 (copy), doc 21 §10.2 (text measures), §10.3, §3 P-8; doc 22 §4 and §6 (the v10.1 branches);
`rebuild-v10-spec.json` → `text`.
**Do:**
- Every text measure behind a text slot, with its scenario branches, exactly as the spec's `text` block: P1 copy,
  P2 headline (follows the scenario) and subtitle, hero title, recommendation lines (Low branch, doc 22 §6),
  ledger cells and status words, plan labels and milestones, scatter title and subtitle, What-waits cells
  (Tranche 3 High branch), comparison titles, Build title, rules line and empty-state sentence.
- `Gate Rule (text)` and `Gate Rule Short (text)`, the only release rule in the model.
- The R-G2 vocabulary across all text measures.
- `tools/build_checks.py` with the four P-8 checks, plus a fifth: evaluate each text measure in Low, Expected and
  High and diff it against the spec's `text` (strings there have no U+2060; strip it before comparing).

**Not in this step:** visuals, retiring old measures (step 11 prunes).
**Bjorn:** none.
**Done when:** the text diff is empty for all mapped measures in all three scenarios; checks 1, 3 and 4 pass (check 2
passes once the old visuals are gone, step 11).

**Prompt:** `project/build-steps/step-04.txt` (say: "Read project/build-steps/step-04.txt and execute it").

**Log:** _(filled in by the session)_

### Step 5 · Page 1 (about 2 h)

**Goal:** P1 matches the comp, pixel for pixel within 2 px, and shows decimal points in an nl-NL session.
**Sources:** doc 21 §4.1 to §4.5, §3 P-2 and P-7; doc 22 §2, §3 (F4 names), §5 (S-4); spec
`construction.charts.ch_f4` (with the seven name boxes) and `construction.tables.tbl_f2_folio`; the comp, P1.
**Do:**
- Layout switch (rule 9): v10 over `opzet-layout.json`, v9 kept for P2 until step 6.
- Masthead eyebrow "1 / 2 · …", subtitle, KPI labels with the code run, kicker codes in Night, the three
  forward links, `btn_next` (S-6 shape), the Definitions chip (P-7), footer.
- F1 stacked area (S-5 result), F2 without value axis and with end labels, F3 label-safe labels and the count card.
- F4: the rows card, the average diamonds, the 50 dots (Night for the seven fullest, Warm Grey for the rest, no
  category labels, ±0.3 as doc 22 §3), the 90 % constant line, the seven `lbl_f4_*` text boxes (white fill).
- The P-2 control states in the theme (`compile_theme.py`).
- Render P1 (rule 6) and an nl-NL render. **S-4:** measure where 60 % and 95 % land in `ch_f4_dots`; if the plot
  area differs from the comp's (x 16 to 1184 inside the visual), shift the seven name boxes by that amount.

**Not in this step:** P2.
**Bjorn:** close the Desktop windows without saving when the session asks.
**Done when:** the P1 render matches the comp (±2 px); the nl-NL render shows points only; `a11y_check.py` has 0 errors
on P1.

**Prompt:** `project/build-steps/step-05.txt` (say: "Read project/build-steps/step-05.txt and execute it").

**Log:** _(filled in by the session)_

### Step 6 · Page 2 frame and the decision card (about 2 h)

**Goal:** P2 runs on the v10 slot map; the frame and the Recommended decision card match the comp.
**Sources:** doc 21 §5, §6.2, §3 P-2; doc 22 §2 (decision card slots) and §3 (ledger columns); spec
`tables.tbl_ledger`; the comp, Recommended, three scenarios.
**Do:**
- P2 reads v10 (rule 9); `opzet-layout-v9.json` is no longer read.
- Frame: eyebrow, `btn_back`, headline and subtitle, the tab twins with the new labels (P-2, large, Night surface),
  scenario pills restyled, the static source line, the Definitions chip, the five cards; bookmark target lists.
- Decision card: A chip, head, four numbers, the two lines, the ledger table (`Finding`, columns 112/280/88/96/176,
  `UNICHAR(10)`), caption, the invitation button (bookmark `bm_p2_build`).
- Remove (not hide) the retired frame and Recommended visuals (doc 21 §5 and §6.3 lists).

**Not in this step:** the hero table and the capital plan (step 7); What waits and Build (steps 8, 9).
**Bjorn:** close Desktop without saving when asked.
**Done when:** Recommended renders in Low, Expected and High; frame and decision card match the comp (±2 px), the
ledger fits its slot in all three.

**Prompt:** `project/build-steps/step-06.txt` (say: "Read project/build-steps/step-06.txt and execute it").

**Log:** _(filled in by the session)_

### Step 7 · Hero table and capital plan; the cut line (about 2 h)

**Goal:** Recommended is complete; the cut-line decisions are taken and written down.
**Sources:** doc 21 §6.1, §6.3, §3 P-4 and P-5; doc 22 §2 (`lbl_hero_*`, `c_plan_t*`), §3 (hero domains, status
colours, plan bar labels off, end labels); spec `tables.tbl_hero`, `charts.ch_plan_cum`, `charts.ch_plan_bar`.
**Do:**
- `tbl_hero` (S-2 result) with the two reference labels at their computed x, the caption and the hero title.
- Capital plan: title, hover tag, the four segment cards (y 720, h 64), the plan bar without data labels, the gate
  card, the cumulative chart (axis end 2032.8, end labels Right with a white background, selected case thick Coffee
  Blue, Low dashed, High dotted, zero line named, gate line at 2028.5), the milestone line.
- Render Recommended × Low, Expected, High.
- **Cut line:** hero verified or R-P2-3-FB; native selector or Deneb (S-3); native F4 or Deneb strip (S-4). Write
  each decision in doc 21 §13 step 6 and here; append one line to the gate note in `status.yaml`.

**Not in this step:** What waits, Build.
**Bjorn:** look at the three Recommended renders and confirm the cut-line decisions.
**Done when:** Recommended matches the comp (±2 px) in all three scenarios; the three cut-line decisions are recorded.

**Prompt:** `project/build-steps/step-07.txt` (say: "Read project/build-steps/step-07.txt and execute it").

**Log:** _(filled in by the session)_

### Step 8 · What waits, and why (about 1.5 h)

**Goal:** the What-waits state matches the comp in all three scenarios.
**Sources:** doc 21 §7.1 to §7.3; doc 22 §3 (waits columns, end labels, axis headroom); spec `tables.tbl_waits`,
`charts.ch_cmp_alts`, `charts.hero_s_packages`; the comp, What waits.
**Do:**
- The small scatter stack: title, subtitle (scenario), hover tag, the four layers (lettered discs A Coffee Blue,
  B and C Night; the shaded "Pays back by 2032" band; axes −60 to +20 and 5 to 62 $M).
- Head and `tbl_waits` (`WaitOption`, columns 168/224/216/256/208, word wrap, `UNICHAR(10)`).
- `ch_cmp_alts`: title measure, A / B / C, end labels A Above, B and C Below (white background), axis end 2032.6,
  auto value axis with one tick below zero and 8 % headroom, the zero line named; `tag_cmp_alts`; `tt-year` binding.
- Remove the retired What-waits visuals (doc 21 §7.3 list).
- Render What waits × Low, Expected, High.

**Bjorn:** close Desktop without saving when asked.
**Done when:** What waits matches the comp (±2 px) in all three scenarios; the table fits in High.

**Prompt:** `project/build-steps/step-08.txt` (say: "Read project/build-steps/step-08.txt and execute it").

**Log:** _(filled in by the session)_

### Step 9 · Build your own (about 2 h)

**Goal:** the Build state works with the native selector (or the Deneb fallback from step 7) and matches the comp.
**Sources:** doc 21 §8; doc 22 §2 (`c_you_*`, `ch_build_bars`), §3 (build bars, plan dot "You", end labels), §6
question 4 (`tag_cmp_build`); spec `tables.tbl_moves`, `charts.ch_build_bars`, `charts.ch_cmp_build`; the comp, Build
(opening state, nothing picked, over budget).
**Do:**
- `sl_moves` (saved selection = A's three moves), `tbl_moves` (columns 92/64/72/116, not filtered by the slicer),
  `c_sel_footer`, the outline tile, `c_you_title` (budget alarm), `c_you_nums` (h 72), `c_you_range`, `c_you_rules`
  (empty-state sentence at n = 0), `ch_build_bars` (horizontal, sorted, Night and Tangerine, label-safe), `ch_cmp_build`
  (A Above, You Below), `tag_cmp_build`, the plan dot "You" under the discs with its label above.
- Interactions: the slicer filters the six build targets (`ch_build_bars` instead of the waterfall), not `tbl_moves`.
- Remove the waterfalls; remove `deneb_selector()` and `publicCustomVisuals` if S-3 passed.
- Click renders in the throwaway copy: opening state × Low, Expected, High; nothing picked; over budget; a broken
  rule (kiosks without the app).

**Bjorn:** one keyboard try on the slicer in Desktop (Tab, Space); close without saving.
**Done when:** every Build render matches the comp (±2 px); the empty state shows the R-B-2 sentence once and no
numbers; the saved selection survives a reload.

**Prompt:** `project/build-steps/step-09.txt` (say: "Read project/build-steps/step-09.txt and execute it").

**Log:** _(filled in by the session)_

### Step 10 · Tooltips, alt text, tab order (about 1.5 h)

**Goal:** the hover layer is cleaned up, and the report passes the accessibility checks by keyboard and screen reader.
**Sources:** doc 21 §9, §5 (tab order); doc 20 R-TT-1, R-TT-3, R-TT-4, R-P2-9, R-X-1; skills `tt-tooltips`, `ax-audit`.
**Do:**
- `tt-package`: the R-TT-1 sentence card, a native moves table at 12 pt, trimmed page height, the broken
  `TT Payback Color` binding fixed. `tt-year`: R-G2 words, your plan in Night. `tt-glossary`: the R-TT-3 terms,
  "Case in view" removed. `tt-f3-band`, `tt-f4-hotel`: R-G3 colour roles. Delete `tt-f1` to `tt-f4` with their canvases
  and measures.
- Dynamic alt text on every new visual (hero, ledger, capital bar, cumulative charts, tables); tab order per doc 21 §5
  and R-P2-9; z and tab of the new slots in `opzet-layering.json`.
- `a11y_check.py` with 0 errors. Keyboard pass and Narrator pass through both pages and all three states (R-X-1),
  done with Bjorn and logged here.

**Bjorn:** the keyboard pass and the Narrator pass in Desktop (the session guides and logs); close without saving.
**Done when:** `a11y_check.py` 0 errors; both passes logged with what was heard and where focus went; tooltip renders
match their specs.

**Prompt:** `project/build-steps/step-10.txt` (say: "Read project/build-steps/step-10.txt and execute it").

**Log:** _(filled in by the session)_

### Step 11 · Final checks and the FinalV3 render set (about 2 h)

**Goal:** a clean model, a complete render set that matches the comp, and contest compliance on paper.
**Sources:** doc 21 §10.4 (prune), §3 P-8, §13 step 8; doc 20 R-X-2, R-X-3; doc 22 §1.
**Do:**
- `build_checks.py` 5 of 5 (the four P-8 checks and the text diff), `schema_check.py`, `a11y_check.py`.
- Submission prune: `sketch_model.py --submission`, the reachability gate (0 bound measures missing, 0 unreachable left).
- Render set `project/deliverables/screenshots/FinalV3/` per R-X-3 (P1; P2 Recommended × L/E/H; What waits; Build:
  opening, filled, over budget; every tooltip page) with a README that pairs each render with its comp view and lists
  every deviation (target: none beyond ±2 px).
- R-X-2 compliance: two visible pages, at least four built-in visual types (line or area, column, bar, scatter,
  table), A = three moves with two growth and the label visible, within budget, financial and operational impact
  through 2032 on the canvas, provided data only, built-in fonts, embedded images.
- Append one line to the gate note in `status.yaml`.

**Bjorn:** review the render set.
**Done when:** all checks pass; FinalV3 complete; the compliance list ticked; the branch is pushed and ready to publish.

**Prompt:** `project/build-steps/step-11.txt` (say: "Read project/build-steps/step-11.txt and execute it").

**Log:** _(filled in by the session)_

### Step 12 · Publish to Web gate (Bjorn publishes), then submit (about 1 h)

**Goal:** the published report works for a judge in any browser and locale; then Bjorn submits.
**Sources:** doc 21 §13 step 9, §16 (Publish to Web items); doc 20 R-X-3, R-G1.
**Do (with Bjorn, who publishes):** check the published report for: SVG cells in the hero and the A chip; tooltips;
the page buttons; an nl and a de browser locale (decimal points, no Dutch word, R-G1); the visual headers against the
hover tags; tooltip scale at 1366 px; one touch test. Every failure: fix in the generators, re-render, Bjorn
re-publishes. Record the results here and in doc 21 §16.
**Bjorn:** Publish to Web, the browser checks with the session, then the submission.
**Done when:** every check recorded as pass; the submission is in.

**Prompt:** `project/build-steps/step-12.txt` (say: "Read project/build-steps/step-12.txt and execute it").

**Log:** _(filled in by the session)_

---

## 3 · Prompt files

All prompts live in `project/build-steps/`: `step-01.txt` to `step-12.txt`, `next.txt` (runs the first step that is
not done) and `resume.txt` (finishes a step that stopped part-way). Say "Read project/build-steps/next.txt and
execute it" to keep going, or name a step file.


## Open questions

A session that meets a question only Bjorn can answer adds it here and sets its step to `blocked`.

1. **20.5 % or 20.6 % for the kiosks (from step 2, needed in step 4; no step is blocked by it).** The value is exactly
   20.55 %. The approved text says "the kiosks earn 20.5% a year on cost"; Power BI's own rounding gives 20.6 %, the
   same rule that gives 30.9 % in High. Recommended: 20.6 %, and the spec's `text` block is corrected in step 4 so the
   text diff stays honest. Bjorn decides.
2. **The pixel changes of step 2** (hero table 8 px wider with its last two columns at 184 and 74; `tbl_moves` at
   y 237 with columns 74 and 118). Recommended: accept them as technical corrections and put them into
   `opzet-layout-v10.json` and `rebuild-v10-spec.json` in steps 7 and 9. Bjorn confirms, or names what must stay.
3. **The hero caption's second sentence (from step 3, needed in step 7; no step is blocked by it).** The approved
   caption reads "A year on cost = what a move adds to operating profit in 2032 ÷ what it costs. Late moves are still
   ramping up in 2032." In the data no move on the page is still ramping up in 2032. At its earliest start every move
   is live for 34 months or more by January 2032, and the extensions and the refresh started at the mid-2028 gate would
   be in their third year too (live by November 2029). Only a Boston hotel started that late would not be.
   Recommended: drop the second sentence; the first is exact as it stands. Bjorn decides.
