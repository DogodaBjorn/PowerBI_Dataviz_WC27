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
| 4 | Text measures and `build_checks.py` | done | 13 Nov | 8849312 | Every measure-backed slot of the spec in Low, Expected, High and the empty Build state: 127 equal, 2 known (open question 1, 20.5/20.6 %), 0 different. Checks 1, 3, 4 pass; check 2 is strict on the new copy and open on the old visuals until step 11. Bjorn was not needed in Desktop |
| 5 | Page 1 | done | 13 Nov | 29e2a7b | P1 on the v10 slot map and on the comp: text rows within 2 px, F3 bars and the F4 plot on the comp's grid, nl-NL prints points only, `a11y_check` 0. Verified with a new tile render (the session window was 540 px wide). Seven small deviations for Bjorn to confirm (open question 4). Bjorn was not needed in Desktop |
| 6 | Page 2 frame and the decision card | done | 13 Nov | 5116804 | P2 on the v10 slot map (v9 no longer read). Frame and decision card on the comp in Low, Expected and High: every text row within 2 px, the same line wraps, the ledger fits its slot in all three; `a11y_check` 0. Two things are Power BI's or a choice: ledger cells sit at the top of their rows, tab labels are Semibold (open question 5). What waits and Build show their frame with the old visuals that still have a slot. Bjorn was not needed in Desktop |
| 7 | Hero table and capital plan; the cut line | done | 14 Nov | a09c731 | Recommended is complete: hero table and capital plan on the comp in Low, Expected and High, text rows and bars within 2 px, the plan bar and the chart's plot on the comp's grid; `a11y_check` 0, 763 number checks and the text diff pass. Cut line: native hero table, native selector, native F4 (Bjorn confirms). Three things are Power BI's: end labels above or under their line ends, not right of them (open question 6); two axis ticks instead of four; the hero's rule 4.5 px low. Bjorn was not needed in Desktop |
| 8 | What waits, and why | done | 14 Nov | ff2baa2 | What waits on the comp in Low, Expected and High: every text row within 2 px, all fifteen table cells wrap as the comp's, the table fits in High, both plots within 1.3 px; the lettered discs are native (a letter layer of its own); A is the NPV maximum in all three cases; `a11y_check` 0, 763 number checks and the text diff pass, Microsoft's validator 0 errors. Outside 2 px, all Power BI's: header words 8.7 px high, ticks every $20M, axis labels 4 to 5 px high, A's end label 5 px high, Low's plot 3 px high. One choice for Bjorn: A's disc in Deep Coffee for the letter's contrast (open question 7). Bjorn was not needed in Desktop |
| 9 | Build your own | done | 14 Nov | 42e280e | Build on the comp with package A picked in Low, Expected and High, with nothing picked, over the budget and with a broken rule: every text row within 2 px, bars and boxes within about 2 px, the empty state shows the rules sentence once and no numbers, the saved selection survives a reload, Space on a tile changes the plan and leaves the table's ten rows; `a11y_check` 0, 766 number checks and the text diff pass, Microsoft's validator 0 errors. Deneb and the waterfalls are gone. Outside 2 px: the table's header words 9.2 px high, its last column 3 px right, A's end label 5 px high. Three things for Bjorn (open question 8): the bars scroll from eight picked moves on, the zero line of the bars runs under the empty rows, a plan beyond $62M has no dot. Bjorn was not needed in Desktop |
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

**Log (Fri 13 Nov 2026, one session, done):**

*Built* (in `sketch_model.py`, block "FinalV3 storytelling rebuild: text measures"; 562 measures, was 518; the report
generator writes the same report as before):

- **Text measures for every measure-backed slot**, with their scenario branches, in folder 15. P1: subtitle, F1 note
  (the 2.8-point fall split into commissions 1.0 and running costs 1.8, with the staff share; N-2), F2 note (from the
  folio's shown amounts), `F3 Count (text)`, F3 note (spend per hotel since 2018, last start year), F4 title and note
  (hotel with the most months topped 90 %, the next two, the extension outside them). P2 frame: headline (follows the
  scenario), subtitle, footer, all from `FinanceParameters`. Recommended: `Hero Title (text)` (moves that pass both
  tests, then the first move in hero order that passes only the first), `Move Yield / Status / Run-rate (text)`,
  `Rec A Year on Cost (text)`, `Rec Line 1 / 2 (text)` (Low branch of doc 22 §6) and `Rec Lines (text)`, the four
  ledger columns (status words from the shares of step 3), `Capital Plan Title (text)`, `Plan T1…T4 L1…L3 (text)`
  plus the joined `Plan T# (text)`, `Gate Rule (text)`, `Gate Rule Short (text)`, `Milestones (text)`. What waits:
  `Proof Title (text)`, `Proof Subtitle (text)`, `Wait Numbers / Why / WhyNot / When (text)` (Tranche 3 High branch,
  doc 22 §6), `Tranche 3 NPV`, `Cmp Alts Title (text)`. Build: `Build Picked`, `Build Run-rate`, `Build A Year on
  Cost (text)`; `Build Valid (text)` carries the R-B-2 empty-state sentence; `Build Range (text)` through `sfm`.
- **One slot map of the text:** `TEXT_SLOTS` (slot → measure, card lines with their static labels, table rows and
  columns) and `TEXT_STATIC` (the slots typed in `opzet_report.py`, with the step that builds them). Steps 5 to 9 bind
  from it.
- **R-G1:** `fmc`, `fmc2` and `sfm2` removed; every caller prints through `fm` / `sfm` (also the old tooltip and alt
  measures). New `FORMAT` calls carry `"en-US"`.
- **R-P2-10:** the old release rule in `Alt C WhyNot (text)` ("Revisit once A has broken even…") is gone; `Gate Rule
  (text)` is the only rule.
- **Smaller:** `Hotels[Copy Name]` (the city, Gatwick for London Gatwick; label data `HOTEL_COPY_NAMES`); `MOVE_P` reads
  the hero row (`InvestmentProjects`) or the selector row (`BuildMove`), so one set of row measures serves both tables;
  `Move Answers (text)` reads `MoveDecision[Finding]` (10.3); `TT Payback Color` defined (the broken binding of
  `tt-package`, found by check 1); `Staff Cost`, `Staff Cost % of Revenue`.
- **Tools:** `tools/build_checks.py` (checks 1 to 5; `--static` runs 1 to 4 without Desktop, `--dump <dir>` keeps the
  DAX and the result). `run_dax.ps1` now stops on an error raised while reading a row; before, it returned an empty
  table (that hid a broken measure here).

*Verified.*

| What | Result | Proof |
|---|---|---|
| Check 5, text against the spec | **127 ok, 2 known, 0 failed** over 11 views (P1; Recommended, What waits, Build in Low, Expected, High; Build with nothing picked). Every slot of the spec is mapped, typed in the report (`TEXT_STATIC`) or a chart's labels (`number_checks.py`). The 2 known: "20.6%" where the spec says "20.5%" (hero title and hero row, Expected; open question 1) | `analysis/output/build_checks.txt` |
| Check 1, bound fields exist | pass (it failed on `TT Payback Color` until that measure was defined) | same file |
| Check 3, no two-decimal $M | pass over 274 text measures (fm's own branch under $0.05M and the folio's cents are the named exceptions) | same file |
| Check 4, one release rule | pass: only `Gate Rule (text)` says "releases"; no other measure or report string says release, revisit or broken even | same file |
| Check 2, R-G2 | strict on the rebuilt copy: pass (DAX literals of the mapped measures and every printed value). Old report and old measures: 17 measures, 4 report strings, listed as open; they go with their visuals (steps 5 to 9) and the prune (step 11) | same file |
| Step 3 still holds | `number_checks.py`: 763 checks, 762 ok, 1 known, 0 failed | `analysis/output/number_checks.txt` |
| Generators and validators | `validate_tmdl --strict` 0 errors, the 11 expected label-safe warnings; `schema_check` 197 files, 0 failing; `a11y_check` 0; `validate_json` 0; the report generator writes an identical report | repeatable |
| The current report opens | both pages render on the new model in the throwaway copy (small renders, the session's screen was narrow again) | `deliverables/screenshots/Step4-text-2026-11-13/` |

*Found on the way (binding for the next steps).*

1. **`all` is a reserved word too** (after `after` and `typed` in step 3): `VAR all = …` fails as "SYNTAXERROR", and only
   when the row is read.
2. **The spec takes differences from shown values.** B against A ("$0.6M less", High "$0.1M less") is the gap between
   the two rounded NPVs, not the rounded gap ($0.5M / $0.2M). `Wait WhyNot (text)` does the same now.
3. **One row measure, two tables.** `Move … (text)` evaluate on `InvestmentProjects` (hero) and on `BuildMove`
   (selector); the hero needs the page filter Brand = Goodnight Inn and the selector must stay unfiltered by the slicer.

*Deviations from the comp.* None; nothing was built in the report. Visible now in today's report (old slots): the new
P1 notes, the P2 headline and subtitle, and one-decimal money in the old tooltip and plan texts.

*Open items for later steps.*
- **Open question 1** (20.5 or 20.6 %) still open; `build_checks.py` lists it as KNOWN. When Bjorn decides, correct
  the spec (or the formatter) and drop the KNOWN entries in both check scripts.
- **Step 5 to 9:** bind from `TEXT_SLOTS`. Multi-line cards are one callout per line (`Plan T# L#`, `Rec Line 1/2`,
  the four numbers with their static labels). The folio table needs its Brand filter; `tbl_moves` reads all ten rows.
- **Static slots** (`TEXT_STATIC`) are checked by the report steps against the spec (rule 7), including
  `c_hero_caption` (open question 3, step 7).
- **Step 11:** the prune must keep the measures `TEXT_SLOTS` names; check 2 then has to pass on everything.

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

**Log (Fri 13 Nov 2026, one session, done):**

*Built* (generators only; P1 62 visuals, P2 unchanged apart from renumbered filter names; 564 measures, was 562):

- **Layout switch (rule 9).** `opzet-layout-v10.json` copied over `opzet-layout.json`, the old map kept as
  `opzet-layout-v9.json`. New `tools/slot_map.py`: the report generator and `a11y_check.py` read P1 and the tooltip pages
  from the current map, and P2 with its `tt-f1` to `tt-f4` from v9 until step 6 empties `V9_PAGES`. Z and tab order of the
  new P1 slots are in `opzet-layering.json` (reading order: F4 note, rows, link, dots; footer, button, chip).
- **Masthead, KPI row, kickers.** Eyebrow "1 / 2 · THE WAKE-UP CALL · THE BRAND REVIEW"; KPI labels with the code run in
  Night semibold; kicker codes in Night (R-G3), single spaces around the dot.
- **F1** stacked area as S-5 found it (base series unfilled, band at 70 % transparency), years on a categorical axis so
  each sits in the middle of its band as in the comp, the grey label background and the leader lines off. Note in three
  lines, forward link.
- **F2** without legend and value axis; the two lines named at their ends; the end numbers are two label-only series
  (`Trend OTA GI (ends)` above, `Trend OTA Sisters (end)` under), without line or marker. Folio with fixed columns and
  the Dusk rule under the header.
- **F3** on `NPS 2025 (label-safe)`, the count card, note, link.
- **F4** note and link at the left; the rows as a Dusk text box plus a semibold value card per row; two scatter layers
  on one rect (three Dusk diamonds under 50 dots, Night for the seven fullest, Warm Grey for the rest, no category labels,
  no marker border), X 60 % to 95 % with whole-percent ticks, the 90 % constant line dashed with its label; the seven
  `lbl_f4_*` boxes on the spec's positions; the hotel tooltip page bound to the dots.
- **Footer row.** `btn_next`: a Night pill with the S-6 link (`PageNavigation`, `p2-investment-strategy`); the Definitions
  chip as one card with its own fill, border and radius (P-7); the two hover tags as text boxes (P-7).
- **Theme (P-2).** `compile_theme.py` writes the light-surface state model for `actionButton` (fill, text, outline with
  default, hover, selected) and outline and value states for `advancedSlicerVisual`; validated against
  reportThemeSchema-2.159 (0 errors). No shape in the theme (it would turn P2's tabs into pills).
- **Model, two text measures:** `Chip Definitions (text)` ("ⓘ Definitions") and `Link F4 (text)` (the F4 link; its "20"
  is counted from the kiosk move's hotels, because `a11y_check.py` allows no typed number but a year). Both are in
  `TEXT_SLOTS`, so the text diff covers them.
- **Tools:** `tools/desktop_shots/tiles/` (see "Found on the way", 1).

*Verified* (Desktop 2.159, Windows culture nl-NL, throwaway copy; renders in
`project/deliverables/screenshots/Step5-p1-2026-11-13/`).

| What | Result | Proof |
|---|---|---|
| P1 against the comp | Text rows, render minus comp, in px: KPI cell +1.5 / −1.0 / +2.0; F1 kicker and title +1.0 / +2.0; F1 note −2.0 / −2.0 / −1.0, link +2.0; F2 note −2.0 / −1.5 / −1.5, link 0; F3 count, note and link −0.5 to −1.0; F4 kicker, title, note, link −1.0 to +1.5; F4 rows −1.0 / +1.0 / 0; footer +1.5; chip +0.5. Every note wraps on the comp's words. F3 bars: centres −1.3 px, width 72.4 against 72. F4 gridlines at x 672.7 to 1840.8 (comp 672 to 1840); the seven names sit beside their dots as in the comp. Outside 2 px: see deviations | render 01, overlay 02 (comp red, render cyan), comp 03 |
| nl-NL | The session is nl-NL; every number prints with a point (79.4%, +3.3, $109.31, +6.8, −4.9, 82.0%), ticks are whole percentages | render 01 |
| S-4 | In the slot 656, 872, 1208, 144 Power BI's plot ran x 672.7 to 1848.7 and y 881 to 988 (the comp: 672 to 1840, 872 to 992). The scale differed by 0.7 %, so a shift of the boxes could not fix it. Instead both layers take the rect 655, 863, 1200, 161, which puts Power BI's plot on the comp's; the name boxes keep the spec's positions | `F4_RECT` in `opzet_report.py`; render 01 |
| Typed text | 23 typed slots (eyebrow, kickers, KPI labels, links, tags, footer, button, seven names) equal the spec letter for letter | script run in the session |
| `build_checks.py` (with the engine) | check 5: 129 ok, 2 known (20.5 / 20.6 %), 0 failed; checks 1, 3, 4 pass; check 2 strict passes, old copy open until step 11 | `analysis/output/build_checks.txt` |
| `a11y_check.py` | 0 failures (it failed first on five points, all fixed: see deviations and "Found", 4) | repeatable |
| Other validators | `schema_check` 217 files, 0 failing; `validate_json` 0; `validate_tmdl --strict` 0 errors, the 11 expected label-safe warnings; Microsoft's validator: the one known P2 error (`hero_s_packages_named`) | repeatable |
| The button | Desktop lists it as "Paginanavigatie … CTRL+klik hier om volgen" with the spoken name. A posted Ctrl+click did not land (open item) | UI Automation in the session |

*Found on the way (binding for the next steps).*

1. **A full-page capture in a narrow window is not a pixel reference; the tile render is.** The session's screen was
   540 px wide again. A 1920 px page then comes out at 0.46 capture px per page px, x and y scaled differently (0.4594
   and 0.4565), the background image off the header, and text inside visuals reading up to 8 px off. A 480 × 270 page
   in the same window comes out at 1.84. `tiles/mk_tiles.py` cuts a page into 16 tile pages in the throwaway copy
   (visuals shifted, Desktop clips them at the page edge), `stitch.py` joins the captures, `overlay.py` and `bands.py`
   compare with the comp. About three minutes a round. Steps 6 to 9 should verify this way (`tiles/README.txt`).
2. **A cardVisual centres its text in its box and hides lines that do not fit.** 12 pt lines are 21.9 px apart; two
   lines show from 60 px of height, three from 88 (the comp's 48 and 64 to 72 showed one and two lines with an
   ellipsis). So a note of n lines gets the height `CARD_H[n]` (64 / 92 / 120) centred on the comp's text block
   (`note()` in `opzet_report.py`); a one-line 14 pt title in a 32 px slot sits 4.5 px low and is lifted by 5
   (`title(..., lift=5)`). `layout.alignment` and the callout padding change nothing. Text boxes set their text at the
   top, as the comp does (first glyph within 1 px).
3. **A chart's slot is not its plot.** Power BI keeps margins of its own inside a visual. `PLOT_RECT` and `F4_RECT` hold
   the visual rect that puts the plot where the comp draws it (F1 68, 392, 526, 248; F2 700, 397, 505, 144; F3 1310,
   392, 560, 221); the slot map keeps the comp's rects. F2's value axis runs 20.1 % to 59.4 % and F3's −8.11 to 10.3 for
   the same pixels per point as the comp. F3's bar spacing came from six padding variants on a scratch page (inner 54,
   outer 27: step 187, width 72).
4. **Shapes.** A button's `shape` needs the `default` selector, and `tileShape` `'pill'` pushes the label out of the
   middle and clips it: the pill is `'rectangleRoundedByPixel'` with `rectangleRoundedCurve` = half the height. The
   text box and card helpers take `off_grid=True` for slots the data placed (`pbir_lib.visual`). `seriesLabels.maximumOffset`
   does not move a series name.
5. **A native table's header is taller than its rows** (35 px against 23.7 px at row padding 1.2). At the spec's
   28 + 3 × 28 the folio scrolled; see deviations.
6. **A new page is unknown to the bridge for a few seconds after `reload`:** retry the capture.

*Deviations from the comp, and why* (open question 4 asks Bjorn to confirm them).

- **Hover tags, the ring-i:** Burnt Tangerine `#A63F0E` instead of Tangerine `#E05A22`. Tangerine on white is 3.7:1 and
  `a11y_check.py` holds every text run to 4.5:1.
- **Folio table:** header 35 px and rows 23.7 px instead of 28 and 28; the first row sits 4.5 px lower than in the comp,
  the others within 1.5 px. Columns 216 / 171 / 171 (2 px of slack, as in step 2).
- **Line-end names of F1 and F2** start 9 to 10 px left of the comp's: Power BI sets them at the plot's edge with no gap.
  Lines, numbers and years are on the comp. F1's year labels sit 3 px higher and its axis labels 4 px right.
- **F3:** the value labels stand 4 px further from their bars; the category names differ by a few px sideways.
- **F4:** the "90%" label is bold (the constant line's label has no font weight property).
- **Reading order in F4:** note, rows, link, dots (the comp suggests note, link, rows): `a11y_check.py` reads by rows.
  `btn_next` comes after the footer line and before the Definitions chip.
- **`lnk_f4` and `chip_def` are cards on a measure,** not typed text (see "Built").

*Open items for later steps.*

- **Step 6:** empty `V9_PAGES` in `slot_map.py` when P2 moves to v10; `EYEBROW_V10` takes page 2; `nav_button()` builds
  `btn_back`; `chip_native()` and `hover_tag_text()` are ready for P2; the masthead controls set their own fills (the
  theme carries the light surface only). The old `Definitions Chip (text)`, `Definitions Pill SVG` and `Hover Tag … SVG`
  stay until P2 no longer binds them (prune in step 11).
- **Steps 6 to 9:** use `note()` for every card of more than one line, and verify with the tile render.
- **Step 10:** alt texts of the P1 charts are the old ones (`Alt F1 Chart`, `Alt F4 Chart`: still true, but written for
  the old charts); `tt-f4-hotel` now opens from a dot.
- **Step 11 or 12:** one real Ctrl+click on `btn_next` (and in the browser a plain click). The posted click of step 1
  did not land here: in the narrow window the button's UI Automation rectangle does not match the scaled button.
- **Step 12:** look at the header in the published report: this step changed only the eyebrow's words there, and the
  tile render cannot show the Night zone.
- **Before the session:** the working tree was clean. The throwaway window was ended with `Stop-Process` (throwaway
  only); the project was not opened in Desktop.

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

**Log (Fri 13 Nov 2026, one session, done):**

*Built* (generators only; P2 42 visuals, was 79; 568 measures, was 564; seven pages, was eleven):

- **Layout switch (rule 9).** `slot_map.V9_PAGES` is empty: every page reads `opzet-layout.json` (v10), the v9 file is
  no longer read. Page 2 of `opzet-layering.json` is rewritten for the v10 slots, all three states, in reading order
  (doc 21 section 5 and R-P2-9), decorative slots with a negative tab; steps 7 to 10 adjust their own slots there.
- **Frame** (`p2_frame()`). Eyebrow "2 / 2 · ROOM TO INVEST · THE INVESTMENT STRATEGY"; `btn_back`, a pill on the Night
  zone with the S-6 link to page 1; headline and two-line subtitle; the tab twins with the new labels, 40 px high,
  radius 8, the current one Oat White with Night text, the others solid Night with a Mist outline; "Scenario" in Mist
  and the three pills in the same look; the source line on `Footer P2 (text)` (its three parameters come from the
  model); the Definitions chip (P-7, as on page 1). The five cards and the outline tile come from the slot map, all with
  the one card shadow, as the comp's `.frame`. Bookmarks keep their names; display names "P2 Recommended: A",
  "P2 What waits, and why", "P2 Build your own"; target lists follow the slot map.
- **Decision card** (`p2_decision_card()`). The A chip; `c_rec_head` as a text box with two paragraphs; `c_rec_nums`,
  four callouts (capex, NPV through 2032, a year by 2032, a year on cost) with the two signed numbers in Burnt Tangerine
  below zero; `c_rec_lines` as two cards 21 px apart (S-7); `tbl_ledger` on `Finding` with columns 112 / 280 / 88 / 96 /
  176, "What we track" in Dusk with its line break, header ruled in Dusk, rows in Seam, no sort arrow (the model sorts
  `Finding[Label]`); the caption; `btn_build_invite`, a white pill with a Dusk outline and the bookmark `bm_p2_build`.
- **Removed, not hidden** (doc 21 sections 5 and 6.3): `z_pill_facts`, `chip_f1` to `chip_f4`, `sl_view`, `z_tile_guide`,
  `c_guide*`, `z_tile_rec`, `hero_packages*`, `c_scatter_title`, `c_rec_title`, `c_rec_mix`, `c_rec_note`,
  `ch_rec_waterfall`, `ch_rec_cumulative`, `c_uncertainty`, `tag_scatter`, `tag_rec_cum`; the SVG Definitions pill of
  page 2. With the facts chips the pages `tt-f1` to `tt-f4` left the report (nothing opens them; N-4), and their chart
  builders left the generator.
- **The states of steps 7 to 9** (`p2_pending()`, rule 9). Recommended shows the hero card and the bottom card empty.
  What waits and Build show the new frame with the old visuals that still have a slot in the v10 map, in their new
  rects: the small scatter stack, the two comparison charts with their hover tags, the three your-plan cards. The old
  visuals without a slot are gone from the files already: the B and C tiles, the state titles, the Deneb selector and
  both waterfalls (so `publicCustomVisuals` is no longer written).
- **Model, four measures:** `Rec NPV Ink`, `Rec Run-rate Ink`, `Alt Rec Head (text)` (the head read from the package,
  because `a11y_check.py` allows no typed number in a static alt text and the mix line says "20"), `Alt Ledger (text)`
  (the ledger read row by row). `Alt Rec Nums (text)` now reads the four new numbers.
- **Tools:** `tiles/mk_tiles.py` takes `--page`, `--scenario` and `--mast` (see "Found", 1); new `tiles/slotdiff.py`.

*Verified* (Desktop 2.159, Windows culture nl-NL, throwaway copy; renders in
`project/deliverables/screenshots/Step6-p2-frame-card-2026-11-13/`).

| What | Result | Proof |
|---|---|---|
| Recommended renders in Low, Expected and High | yes, each from its own tile render | renders 01, 02, 03 |
| Frame against the comp, render minus comp | eyebrow −0.5 px; back button text −0.2; headline +1.1 (after a 2 px move, see deviations); subtitle +0.3 / +1.6, same wrap; tab labels 0 in y; "Scenario" −0.4; pill labels −0.3 to 0, x within 2; footer −0.4; chip +0.3 | `slotdiff.py` on the stitched capture; overlay 04 |
| Decision card against the comp | head −0.7 / −1.3; the four values −0.8 to −1.7, their labels +0.5 to +0.7, x within 2; the two lines −1.7 / +0.2; caption −0.9; invitation text −0.8, x 0. In all three cases 65 text rows pair one to one with the comp's: no line wraps differently | same |
| The ledger fits its slot | header 34 px, rows 44.6 / 44.6 / 65.8 / 44.6: the last row ends at page y 597, the slot at 608; no scrollbar; row tops within 2 px of the comp's in all three cases; High's "three quarters of the rise since 2021 undone" takes two lines, as in the comp | renders 01 to 03 |
| Typed text | 12 typed slots (eyebrow, back, six tab twins, Scenario, head, caption, invitation), the ledger's five headers and the four number labels equal the spec letter for letter | script run in the session |
| `build_checks.py` (with the engine) | check 5: 129 ok, 2 known (20.5 / 20.6 %), 0 failed; checks 1, 3, 4 pass; check 2 strict passes, the old list is down to 16 measures and 3 report strings | `analysis/output/build_checks.txt` |
| `number_checks.py` | 763 checks, 762 ok, 1 known, 0 failed | repeatable |
| `a11y_check.py` | 0 failures | repeatable |
| Other validators | `schema_check` 156 files, 0 failing; `validate_json` 0; `validate_tmdl --strict` 0 errors, the 11 expected warnings; Microsoft's validator: the one known error (`hero_s_packages_named`, goes in step 8) | repeatable |
| The other two states | What waits and Build draw their frame and the old visuals without an error | renders 07, 08 |

*Found on the way (binding for the next steps).*

1. **The tile render can show the masthead and a scenario.** `mk_tiles.py --mast 168` draws the Night zone as a
   rectangle on the tile pages, so light text is readable and measurable; `--scenario Low` sets the slicer on its own
   tile and gives every other tile the case as a page filter (a slicer only reaches its own page); the page's own
   filters are copied to every tile. `slotdiff.py` measures on any background. A card's line can read 1.5 px off
   depending on where the card's top falls on the capture's pixel grid: a difference under 2 px is noise.
2. **A native table:** every cell at the top of its row; a ruled row is the text plus twice the padding plus 1 px;
   the header is about 34 px whatever the padding. So a table starts above its slot by the header's surplus, and the
   comp's centred cells cannot be had. Step 8 (`tbl_waits`) meets the same.
3. **A tab's label centres in 40 px with margins 0 / 0;** a 28 px pill needs bottom margin 3 (step 5). In a button the
   Semibold face is 2.7 % wider than regular, as doc 22 says.
4. **The comp's scenario cannot be set from its URL.** For the Low and High comp pictures a scratch copy of the comp
   read `?scen=` into `ST.scen`; the comp itself is untouched. Headless Edge returns before the PNG is written.
5. **A capture taken right after a reload can miss the cards** (the Build tile looked empty at first): take it twice.
6. **A region capture through the bridge (`cap.mjs` with x y w h) hung for two minutes** and had to be stopped; the
   tile pages do that job.

*Deviations from the comp, and why* (open question 5 asks Bjorn to confirm them).

- **Ledger, vertical alignment.** A cell with fewer lines than its row sits on the row's first line; the comp centres
  it. That is 10 to 12 px higher for "11.3%", "10.1%", "33.7%", "35.1%", "F1 The margin" and the F3 values, 20 px for
  "0 of 20 · 0" and "20 of 20 · 0", 10 px for the two-line cells of the F4 row. The header words sit 8.5 px higher
  (the header is 34 px, the comp's 28; the rule under it is on the comp's line). The F3 row sits 1.4 to 2.1 px low.
- **Ledger, position.** The visual is 1111, 362, 754, 246 in the slot 1112, 368, 752, 240: 6 px up for the header,
  1 px left and 2 px wide for the cell padding and the scrollbar slack.
- **Tab labels in Semibold,** 3 to 5 px wider than in the comp's picture, which draws them in regular weight through
  a CSS accident (doc 21, results of this step). P-2 and the comp's own class say Semibold.
- **Headline, both pages:** the card sits 2 px under its slot. On page 2's masthead the line measured 2.2 px above the
  comp's; page 1 has the same card in the same slot, so both moved together (step 5 could not see the header).
- **`c_rec_nums`** sits 4 px above its slot (a card centres value and label; the comp sets them from the top).
- **`c_rec_head`** is typed, but a screen reader hears `Alt Rec Head (text)`: the hero's move names ("Booking app &
  member rates"), not the mix line's ("Booking app with member rates").
- **`z_footer2` is a card on a measure,** not the static text box of doc 21 section 5: its 8 %, 2025 and 2032 come from
  `FinanceParameters`, and step 4 mapped it that way.

*Open items for later steps.*

- **Step 7:** the hero card and the bottom card are empty and wait for `tbl_hero` and the capital plan; their z and
  tab are in `opzet-layering.json` already. `rec_lines()`, `ledger()` and `ctl_button()` show the patterns; the plan's
  segment cards are multi-line cards (`note()`).
- **Step 8:** replace the old small scatter stack, `c_scatter_title_s` (still on `Scatter Title Short (text)`) and
  `ch_cmp_alts`; build `tbl_waits` with the table rules of "Found", 2. The Microsoft validator's one error leaves with
  the old `hero_s_packages_named`.
- **Step 9:** `waterfall()`, `deneb_selector()`, `native_selector()`, `SELECTOR`, `DENEB_SPEC` and `DENEB_GUID` are
  unused since this step and still in `opzet_report.py`: remove them there. `interactions()` points at
  `dn_build_selector`, which no longer exists: point it at `sl_moves`. The three your-plan cards are the old ones.
- **Step 10:** `tt-f1` to `tt-f4` are out of the report; their canvases (`canvas-tt-tt-f#.jpg`) and measures
  (`Facts Chip F# (text)`, `Facts Bar SVG`, `Definitions Pill SVG`, `Definitions Chip (text)`) are still there.
  `Alt Ledger (text)`, `Alt Rec Head (text)` and `Alt Rec Nums (text)` are written; check them in the Narrator pass.
- **Step 11 or 12:** one real Ctrl+click on `btn_back` and on a tab (in the browser a plain click), and a look at the
  hover state of the pills and tabs: the hover fill is Mist with Night text, set but not seen in a capture.
- **Before the session:** the working tree was clean. The throwaway window was ended with `Stop-Process` (throwaway
  only); the project was not opened in Desktop, and no Desktop window is left open.

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

**Log (Sat 14 Nov 2026, one session, done):**

*The three cut-line decisions (doc 20 section 1, rule 10; Bjorn confirms).*

| Decision | Outcome | Why |
|---|---|---|
| Hero: the table, or R-P2-3-FB (two bar charts) | **The native table.** No fallback | Built in the report and rendered in Low, Expected and High: both reference lines unbroken over the ten rows, no scrollbar, every value complete ("+$0.03M", "−$30.5M"), rows and bars within 2 px of the comp |
| Build selector: native, or Deneb | **Native** (button slicer beside a table). Deneb goes in step 9 | S-3 passed in step 2: rows aligned within 1 px, the saved selection survives a reload, Space and Tab work |
| F4: native dot plot, or Deneb strip | **Native.** No Deneb strip | S-4 solved in step 5 with `F4_RECT`; the seven names sit beside their dots |

Written in doc 21 section 13 (row 6 and "Results of the hero table and the capital plan") and as one line in the gate
note of `status.yaml`.

*Built* (generators only; P2 62 visuals, was 42; 575 measures, was 568).

- **Hero card** (`p2_hero()`): `c_hero_title` on `Hero Title (text)`; `lbl_hero_8` and `lbl_hero_0` as decorative text
  boxes at the x of their lines (the generator asserts that the slot map's x equals `hero_ref_x()`); `tbl_hero`
  (`hero_table()`): `Move Name` in the model's order, Answers in Dusk, Status and NPV with their ink from the model, the two
  SVG bar cells, columns 280 / 104 / 96 / 196 / 64 / 184 / 74, row padding 0, image 173 x 34, one Dusk rule under the
  header; the caption as approved.
- **Capital plan** (`p2_capital_plan()`): title on `Capital Plan Title (text)`; the hover tag (P-7); the four segment
  labels as one card per line (`line_cards()`, the pattern of `c_rec_lines`); `ch_plan_bar`, one stacked bar of the four
  capex measures on a value axis that ends at the budget, no labels; the gate rule as a four-line card; `ch_plan_cum`
  (`plan_cum()`): the case in view 3 px Coffee Blue, the other two 1.5 px Warm Grey (Low dashed, High dotted), the zero
  line named, the gate as a dashed line at mid-2028, x axis to 2032.8, one label per line end, `tt-year` on hover; the
  milestone line.
- **Model** (`sketch_model.py`): `Move Status Ink`, `Move NPV Ink`; `A Cumulative End Sel Low / Expected / High
  (label-safe)` in place of the one `A Cumulative End Sel (label-safe)` (see deviations); `SUSDM0`, a whole-$M format, on
  the three `A Cumulative Line (...)` measures; `HERO_TEXT_LIFT` moves the bar 5 px up inside its image; first alt texts
  for the three new data visuals (`Alt Hero`, `Alt Plan Bar`, `Alt Plan Cum (text)`; step 10 reviews them).
- **Theme** (`compile_theme.py`): the background of a line chart's data label is white and opaque.
- **Layering** (`opzet-layering.json`): the five extra line cards of the segment labels, out of the tab order.
- **Tools:** `tools/desktop_shots/step7/` (scratch pages that show a table or a chart whole, and their measuring scripts).

*Verified* (Desktop 2.159, Windows culture nl-NL, throwaway copy; the session window was 540 px wide, so every render is
a tile render; renders in `project/deliverables/screenshots/Step7-rec-hero-plan-2026-11-14/`).

| What | Result | Proof |
|---|---|---|
| Recommended renders in Low, Expected and High | yes, each from its own tile render; the hero title, the bars, the tranche lines, the milestone and the emphasised line follow the case | renders 01, 02, 03 |
| Hero against the comp, render minus comp | title +0.7 to +1.2 px; the two reference labels −0.2, x +1; header words −0.1 / +0.1; the ten rows of Move, Answers, Status and A year on cost −0.3 to −1.9, x within 1; the bars start at y 279.7 (comp 280) at a 34 px pitch; caption −0.8. Same in all three cases. Outside 2 px: see deviations | `slotdiff.py` on the stitched captures; overlay 04 |
| The hero's real sizes | header 32.5 px, rule 1 px, rows 34.0 px, a cell's cap centre 12.25 px under its row's top: measured on a scratch page that shows the table whole, with a marker | `tools/desktop_shots/step7/hero_probe.py` |
| No scrollbar, values complete | none in the three cases; "+$0.03M", "−$30.5M" and "−$27.3M" print whole | renders 01 to 03 |
| Capital plan against the comp | title +0.9; the nine label lines −1.0 to +1.5, x within 2; gate rule +0.9 to +2.3 (four lines, the comp's wraps); milestones −0.8, x +2; hover tag +0.9 | same |
| The plan bar | y 788.3 to 819.9 (comp 788 to 820); segment ends at x 338.5 / 712.4 / 1601.1 (comp 339.3 / 712.9 / 1601.8), no white between the segments | `step7/bar_probe.py`, `bar_measure.py`; render 01 |
| The chart's plot | +$20M gridline at y 846.5 (comp 846), zero line 914.9 (914), gate line x 1120.8 (1120.6), 2027 at x 864.2 (864), 2032 at 1717.6 by the line's last pixel (1719.2) | `step7/scan_cum.py`, `bar_measure.py` |
| nl-NL | the session is nl-NL: axis "+$20M" and "$0M", labels "Low −$4.6M", every value in the table with a point | renders 01 to 03 |
| Typed text | `lbl_hero_8`, `lbl_hero_0`, `c_hero_caption`, `tag_plan_cum`, the hero's seven headers and the two line names of the chart equal the spec letter for letter, in all three views | script run in the session |
| `build_checks.py` (with the engine) | check 5: 129 ok, 2 known (20.5 / 20.6 %), 0 failed; checks 1, 3, 4 pass; check 2 strict passes, the old list unchanged (16 measures, 3 report strings) | `analysis/output/build_checks.txt` |
| `number_checks.py` | 763 checks, 762 ok, 1 known, 0 failed | `analysis/output/number_checks.txt` |
| `a11y_check.py` | 0 failures | repeatable |
| Other validators | `schema_check` 175 files, 0 failing; `validate_json` 0; `validate_tmdl --strict` 0 errors, 13 expected label-safe warnings (11 + 3 new − 1 retired); Microsoft's validator: the one known error (`hero_s_packages_named`, goes in step 8) | repeatable |

*Found on the way (binding for the next steps).*

1. **A tile seam through a table or a chart is no reference.** At this zoom Desktop snapped a visual's position by up
   to 1.6 page px (a 2 px move showed as 0 or 3.3) and rounded each table row to a device pixel (33.75 px for 34). For a
   table or a chart, make a scratch page of 480 x 270 that shows it whole, with a marker at a known y
   (`step7/hero_probe.py`, `bar_probe.py`). Text in cards and text boxes measured as before.
2. **A native table of n rows is 33.5 + 34 n px here** (header 32.5, rule 1); give the visual 1 px more or it scrolls.
   A cell's text sits 5.25 px above the middle of a 34 px row. Step 9's `tbl_moves` uses row padding instead (S-3), so
   its text is centred; step 8's `tbl_waits` wraps and meets the ledger's rule (step 6).
3. **A line chart's data label goes Above or Under**, nothing else. Power BI shifts it sideways when it has room.
   Steps 8 and 9 planned A Above, B and C Below, You Below: those exist.
4. **A value axis format must keep its decimal point** (`#,0,,.`) or the commas do not scale. `SUSDM0` is that format;
   the first series of a chart with a visible value axis carries it. Steps 8 and 9: `Preset A Cumulative Net (sel)` is
   still `SUSDM` ("+$10.0M", and "+$10,0M" in a Dutch session); give the comparison charts a first series in `SUSDM0`.
5. **Power BI picks the ticks.** 102 px of plot gave two (+$20M, $0M). The taller comparison charts will get more.
6. **A bar chart needs a category** (Microsoft's validator: PBIR_ROLE_REQUIRED_MISSING); `layout.stackedGapSize` 0
   closes the white seams of a stacked bar; about 8 px stay free above a bar.
7. **Microsoft's validator reads `labels.backgroundColor` as a misplaced colour**; the theme schema has exactly that
   fill. Set it in the theme.
8. **Do not refresh the copy twice.** A second `refresh_desktop_model.ps1` on the same window left Desktop "not ready"
   for ten minutes; the port is in the first run's output. `opzet_report.py` now imports `sketch_model` (geometry, gate
   year), as the two check scripts do.

*Deviations from the comp, and why* (open question 6 asks Bjorn about the first; the others are Power BI's).

- **End labels of the chart:** above or under their line ends, not right of them. Render minus comp: High 2 px lower, Expected
  21 px higher, Low 8 px lower, and all three start 50 to 70 px further left (Power BI sets High right of its line end,
  the other two over theirs). No label meets another or a line in any case. The comp's picture cannot be had natively.
- **Axis ticks:** +$20M and $0M; the comp also shows +$10M and −$10M. Tick labels sit 2 px higher than the comp's (Power
  BI centres them on their gridline) and the year labels 2 px higher.
- **Line names in the chart** ("Cash positive above this line", "The 2028 gate") are semibold; the comp's are regular.
- **The zero line runs to the plot's right edge** (2032.8); the comp ends it at 2032.
- **Hero, header rule and reference lines:** 4.5 px under the comp's (rule at y 276.5, lines from 277.5 to 617.5), so
  that text and bars are on the comp. The lines end 4 px above the caption's letters (the comp: 9).
- **Hero, width:** the table runs to x 1056, not 1048, and the NPV values end 6 px further right (step 2, open question
  2). The header rule runs to 1054.
- **Hero, bars:** 5 px higher inside their rows than the spec's `bar_y` 8, to stay on their row's text.
- **`tbl_hero` and the slot map:** the visual is 56, 244, 1000, 374; `ch_plan_bar` 56, 780, 1808, 40; `ch_plan_cum`
  792, 834, 1077, 146 (`PLAN_RECT`). The slot map and the spec keep the comp's numbers.
- **The two value columns of the hero have a zero-width space as header** (the comp: empty). A table column needs a name;
  step 10's Narrator pass decides whether it should be a spoken one.
- **`c_plan_title` is a card on a measure** (doc 21 says text box): its amounts come from the model, as step 4 mapped it.

*Open items for later steps.*

- **Open question 3** (the caption's second sentence) is still open; the caption is built as approved. It is one
  constant, `HERO_CAPTION`.
- **Open question 2:** the hero's pixels are built as step 2 found them; `opzet-layout-v10.json` and the spec were not
  changed (the comp is the contract until Bjorn says so).
- **Step 8:** `cumulative_chart()` still builds the old comparison charts (legend, "Break-even", `SUSDM` axis). Rebuild
  it on `plan_cum()`'s pattern; see "Found" 3 to 5.
- **Step 10:** the three new alt texts are first versions; the hero's value headers; `tt-year` now opens from
  `ch_plan_cum` too.
- **Step 11:** the prune must keep `Move Status Ink`, `Move NPV Ink`, the six `A Cumulative End ...` series and the
  measures only an alt text reads.
- **Step 12:** look at the hero's SVG cells and the row seams in the browser (step 2's item), and at the end labels of
  the chart at 1366 px.
- **Before the session:** the working tree was clean. The throwaway windows were ended with `Stop-Process` (throwaway
  only); the project was not opened in Desktop, and no Desktop window is left open.

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

**Log (Sat 14 Nov 2026, one session, done):**

*Built* (generators only; P2 66 visuals, was 62; 580 measures, was 575).

- **Proof card** (`p2_proof()`, shared by What waits and Build): `c_scatter_title_s` on `Proof Title (text)` (two lines),
  the native hover tag "ⓘ Hover a dot" (P-7), `c_scatter_sub` on `Proof Subtitle (text)`, and the scatter stack
  (`scatter_stack()`): axes typed from the spec (capex $5M to $62M, NPV −$60M to +$20M, `PROOF_X`, `PROOF_Y`), ticks in
  whole $M, the zero line in Dusk, the shaded band named "Pays back by 2032", the cloud's dots 8 px, A, B and C as
  22 px discs with their letters inside.
- **The letters are a layer of their own** (`hero_s_packages_letters`): on a sized dot Power BI sets the label under the
  dot at this plot size (measured again), and on an invisible, unsized point it sets the label 17.2 px under the point. So
  the letters hang from three invisible points a fixed $4.34M (16.7 px) above their discs (`Named Letter NPV (sel)`,
  `sketch_model.PROOF_LETTER_LIFT`) and land in the middle of the discs. Doc 21 7.1's fallback (a tag under the dot) is
  not needed, and Microsoft's validator's one error left with the tag.
- **Panel** (`p2_waits()`): `c_waits_head`, a text box with two paragraphs; `tbl_waits` (`waits_table()`), a native table
  on `WaitOption` with columns 168 / 224 / 216 / 256 / 208, word wrap, the line breaks of "The numbers" and "When we
  decide", header ruled in Dusk, rows ruled in Seam, a rule under the last row.
- **Comparison chart** (`cmp_chart()`, written so that step 9 can call it for A and You): `ch_cmp_alts` with C (Warm
  Grey, dashed), B (Night) and A on top (Coffee Blue, 3 px); one label per line end from the label-safe end series, A
  Above in Deep Coffee semibold, B and C Under; no legend; x axis to 2032.6; the zero line named; the title inside the
  visual on `Cmp Alts Title (text)`; `tt-year` on hover; the native hover tag "ⓘ Hover a year".
- **Model** (`sketch_model.py`): `Cmp Alts Y Start` / `Cmp Alts Y End` (`nice_axis()`: the comp's `niceTicks` in DAX, zero
  inside, 8 % headroom, whole steps: −50 to +10, −50 to +20, −40 to +40 $M in Low, Expected, High); `Preset C Cumulative
  Line` in whole $M as the chart's first series; `Package Capex`, `Package NPV (sel)`, `Build Capex`, `Build NPV (sel)`
  formatted in whole $M (`USDM0`, `SUSDM0`: every scatter layer must print the same ticks, P-1 b); `Named Point Size
  (small)` one size for the three discs; `Named Letter NPV (sel)`; `Alt Waits (text)`, a first version (step 10 reviews it).
- **Layering** (`opzet-layering.json`): the letters layer above the discs; the plan dot under the discs (doc 22 section 3).
  `STATE_ONLY` in `opzet_report.py` shows the plan dot in Build only (the comp draws no "You" in What waits).
- **Removed:** the old small stack's tag labels, the SVG hover tags of this state, the old comparison chart of A, B and C
  (legend, "Break-even"). The retired visuals of doc 21 7.3 (`c_alts_title`, `c_alts_intro`, the B and C chips, cards and
  tiles) left the report in step 6; none is left in the files.
- **Tools:** `tiles/mk_tiles.py --rows 1` and `tiles/stitch.py --rows 1` (see "Found", 1).

*Verified* (Desktop 2.159, Windows culture nl-NL, throwaway copy; renders in
`project/deliverables/screenshots/Step8-what-waits-2026-11-14/`).

| What | Result | Proof |
|---|---|---|
| What waits renders in Low, Expected and High | yes, each from its own strip render; subtitle, table, chart title, axis and labels follow the case | renders 01, 02, 03 |
| Text rows against the comp, render minus comp | proof title +1.8 / +1.3 px; subtitle +0.2; hover tags 0.2 to 0.8; panel head within 1.1; chart title −0.7. The same in all three cases | `slotdiff.py` on the stitched captures |
| The table against the comp | all fifteen cells wrap as the comp's, in all three cases (52 text rows pair one to one; Low 51, as the comp); rows within 1.4 px, x within 2; header rule at y 280.0 (comp 279.5), row rules at 376.9 / 495.0 / 634.8 (comp 376.5 / 494.5 / 634.5) | same; `meas.py` of the session |
| **The table fits in High** | yes: its last rule is at y 634.8, the slot ends at 640; no scrollbar in any case | render 03 |
| The scatter's plot | band from x 144.2 to 716.7 (comp 144 to 716); +$20M at y 279.7, zero line 356.7, −$20M 434.0, −$40M 510.7, −$60M 587.8 (comp 280 / 357 / 434 / 511 / 588); discs 21.8 px, A at 188.3, 343.9 (comp 188.2, 344.2); the three letters inside their discs in Low, Expected and High | same; renders 01 to 03 |
| The comparison chart's plot | Expected: +$20M at y 730.6, zero 798.9, −$20M 868.3, −$40M 936.9 (comp 731 / 799.9 / 868.7 / 937.6); 2027 at x 128, 2032 at 1670.9 (comp 128 and 1670.9); High within 1 px too. Low: see deviations | same |
| End labels | A Above, B and C Under in all three cases; no label meets another; B and C within 1.3 px of the comp's, A 4.6 to 6.5 px higher | `slotdiff.py` |
| The axis ends from the model | −50 / +10, −50 / +20, −40 / +40 $M: the comp's in every case | DAX query in the session |
| **A is the NPV maximum in all three scenarios** (doc 21 7.1) | 0 of 456 packages above A in Low (−$5.47M), Expected (+$3.28M) and High (+$12.72M) | DAX query in the session |
| The letters stay inside the plot | the highest letter anchor is $17.06M (A in High), under the axis end of $20M; every package lies inside −$60M to +$20M and $5M to $62M | DAX query in the session |
| nl-NL | the session is nl-NL: ticks "+$20M", "$10M", labels "A +$6.8M", every amount in the table with a point | renders 01 to 03 |
| Typed text | `tag_scatter_s`, `c_waits_head`, `tag_cmp_alts`, the table's five headers, "Pays back by 2032" and "Cash positive above this line" equal the spec letter for letter, in all three views | script run in the session |
| `build_checks.py` (with the engine) | check 5: 129 ok, 2 known (20.5 / 20.6 %), 0 failed; checks 1, 3, 4 pass; check 2 strict passes, the old list unchanged (16 measures, 3 report strings) | `analysis/output/build_checks.txt` |
| `number_checks.py` | 763 checks, 762 ok, 1 known, 0 failed | `analysis/output/number_checks.txt` |
| `a11y_check.py` | 0 failures | repeatable |
| Other validators | `schema_check` 180 files, 0 failing; `validate_json` 0; `validate_tmdl --strict` 0 errors, the 13 expected label-safe warnings; **Microsoft's validator: 0 errors** (the known one left with the tag labels) | repeatable |

*Found on the way (binding for the next steps).*

1. **Render in strips, not in tiles.** The narrow Desktop window is tall (the capture is 1200 x 5142 px), and a tile page is
   fitted to its width. `mk_tiles.py --rows 1` writes four strips of 480 x 1080 at the same 1.84 px per page px, and
   `stitch.py --rows 1` joins them: no horizontal seam. With 270 px tiles a chart higher than a tile read up to 4 px
   wrong across the seam (the first two rounds of this step). Step 9 should render Build this way.
2. **A scatter's category label:** under the dot on a sized dot, 17.2 px under the point on an unsized one, never inside.
   A letter inside a disc is a second layer with lifted, invisible points (see "Built"). The lift is in dollars, so it
   holds only while the value axis is fixed.
3. **A scatter's dot sizes here:** `bubbleSize` −15 without a Size field gives 8 px, 0 gives 11 px; with a Size field
   in magnitude mode, 7.2 at −22 gives 21.8 px.
4. **`visualContainerObjects.spacing`** (`customizeSpacing` true, `spaceBelowTitle` n) moves a chart's plot 1 px per unit
   under its title (default 2), the title stays; `spaceBelowTitleArea` did nothing. Power BI sets a 14 pt title 2.6 px
   lower in its row than the comp, so the chart starts 3 px above its slot.
5. **A native table's text line is 21.5 to 21.6 px,** not the comp's 21.28: a wrapping row is lines x 21.55 + twice the
   padding + 1. Padding 4.9 puts the three rules within 0.5 px of the comp's. The header is 31.9 px + twice the padding
   down to the centre of its rule. A native table rules between rows only: `values.outlineStyle` BottomOnly draws the
   rule under the last row.
6. **A line chart's plot starts about 3 px higher when no tick sits on the axis end** (Low: the axis ends at +$10M, Power
   BI ticks every $20M). The plot's bottom does not move.
7. **A value axis bound to two measures works** (`start` and `end` as measure expressions): the comp's `niceTicks` is
   `nice_axis()` in `sketch_model.py`; step 9 calls it for `ch_cmp_build` ("as ch_cmp_alts").
8. **Never cut a block out of a generator by its neighbours' names without reading what lies between** (a slip of this
   session, caught by the next run and restored from git before anything was committed).

*Deviations from the comp, and why* (open question 7 asks Bjorn about the first; the others are Power BI's).

- **A's disc is Deep Coffee** (`#1763A8`), not the comp's Coffee Blue (`#2589D8`): the white letter reads at 6.2:1
  instead of 3.7:1 (the floor for 12 pt text is 4.5:1). It is the colour the lettered discs had before (R-W-1: "the same
  lettered discs as before"); the same choice as the ring-i of step 5.
- **Table, header words:** 8.7 px higher than the comp's (the native header is 41.7 px to its rule, the comp's 32; the
  rule is on the comp's line). As the ledger (open question 5).
- **Ticks:** both charts tick every $20M, the comp every $10M (Power BI picks the ticks).
- **Axis labels:** the scatter's capex ticks 4.1 px and its axis title 4.9 px higher, the comparison chart's year labels
  4 px higher (Power BI sets them closer to the plot); the comparison chart's value labels end 12 px further left.
- **A's end label** stands 4.6 to 6.5 px higher above its line end than the comp's 15 px.
- **Zero line of the comparison chart:** its name starts 16 px further left (the plot starts 10 px left of 2027), and the
  line and the gridlines run to the plot's right edge; the comp ends them at 2032.
- **Low only:** the comparison chart's plot starts 3 px higher ("Found", 6): zero line 3.3 px, the −$20M line 2 px and
  the lines of A and B about 3 px above the comp's; the bottom is on the comp.
- **Visual rects:** scatter 56, 269, 682, 369 (slot 56, 272, 672, 368); `ch_cmp_alts` 56, 685, 1819, 316 (slot 56, 688,
  1808, 312); `tbl_waits` 791, 238, 1074, 402 (slot 792, 248, 1072, 392); the proof title's card 56, 173, 520, 72. The
  slot map and the spec keep the comp's numbers.
- **`c_scatter_sub` is a card on a measure,** not the text box of doc 21 7.1: its count and its amount follow the case.

*Open items for later steps.*

- **Step 9:** `p2_proof()` already serves Build; the plan dot (`hero_s_packages_build`) is the old Tangerine dot, now
  under the discs and shown in Build only: rebuild it as the comp's "You" (Night, Tangerine over budget, label above).
  `cmp_chart()` and `nice_axis()` are ready for `ch_cmp_build`; `cumulative_chart()` and `hover_tag()` are used by Build
  only and go with it. `BUILD_TARGETS` still names the waterfall.
- **Step 10:** `Alt Waits (text)` is a first version; the letters layer and the plan dot are decorative; `tt-year` now
  opens from `ch_cmp_alts` as rebuilt; the keyboard cloud layer's table view now lists the exact capex and NPV as text.
- **Step 11:** the prune must keep `Named Letter NPV (sel)`, `Preset C Cumulative Line`, `Cmp Alts Y Start`, `Cmp Alts Y
  End` and the three `Preset … Cumulative End (label-safe)`. Unused since this step: `Scatter Title Short (text)`,
  `Scatter X Start`, `Scatter X End`, `Scatter Y Start`, `Scatter Y End`, `Hover Tag Dot SVG`.
- **Step 12:** look at the letters in the discs and at A's label in the browser at 1366 px (the letter lift is in page
  pixels through a fixed axis, so it should hold; it has not been seen outside Desktop).
- **Before the session:** the working tree was clean. The throwaway windows were ended with `Stop-Process` (throwaway
  only); the project was not opened in Desktop, and no Desktop window is left open.

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

**Log (Sat 14 Nov 2026, one session, done):**

*Built* (generators only; P2 81 visuals, was 66; 601 measures, was 580; 34 tables, was 33).

- **Panel** (`p2_build()` in `opzet_report.py`): `c_build_head`, a text box with two paragraphs; `sl_moves`
  (`move_slicer()`), the native selector as S-3 found it, with a 1 px Seam rule at the foot of every tile (the slicer's
  accent bar) and package A as its saved selection; `tbl_moves` (`moves_table()`): the move's name at width 0, Answers in
  Dusk, Capex, NPV with its ink from the model, A year by 2032, rows ruled in Seam at the tile's 32 px; `c_sel_footer`.
- **Your-plan tile:** `c_you_title` as two cards (`you_title()`: the plain title, and the alarm band with its own
  padding); `c_you_nums` as a value card and a label card for each of the four numbers (`you_nums()`); `c_you_range`;
  `c_you_rules` as a shape whose text and ink are measures (`top_text()`: set from the top, one line or two);
  `ch_build_bars` (`build_bars()`), a clustered bar chart on the new table `BuildBar`.
- **Bottom card:** `ch_cmp_build` by `cmp_chart()` (your plan Night, Tangerine over the budget, A on top; "You" Under,
  "A" Above; no legend; `tt-year` on hover) and the native hover tag `tag_cmp_build`.
- **Proof chart:** the plan dot rebuilt (Night, Tangerine over the budget, under the discs) and its name "You" as a layer
  of its own, `hero_s_packages_you` (`you_label()`), in the Build state only.
- **Model** (`sketch_model.py`): table `BuildBar` (the ten moves and four empty rows) with `Build Bar NPV`, `(label-safe)`,
  `Color`, `Order`, `Build Bars X Start` / `End` / `Zero`; `Build Cumulative Line`, `Build Cumulative Line (over)`,
  `Preset A Cumulative Line` (whole $M), `Cmp Build Y Start` / `End` (`nice_axis()`); `Build Title Plain (text)`,
  `Build Title Alarm (text)`; the four `Build Label ... (text)`; `Build NPV Ink`, `Build Run-rate Ink`; `Build Point
  Color`, `Build You Ink`, `Build You Label NPV`; `BuildPoint[Name]`. The five text measures of the tile return an empty
  text while nothing is picked (they printed "$0.0M" or a blank), and `Build Valid Color` is Night for the empty state.
  First alt texts: `Alt You Nums` (rewritten), `Alt Build Bars`, `Alt Moves`.
- **Interactions:** `sl_moves` filters the your-plan cards, the footer, the bars, the comparison chart, the plan dot and
  its name (DataFilter); every other visual, `tbl_moves` included, is NoFilter.
- **Removed:** `deneb_selector()`, `native_selector()`, `waterfall()`, `cumulative_chart()`, the SVG `hover_tag()`,
  `p2_pending()`, the `--selector` switch and `publicCustomVisuals`. No visual of type Deneb or waterfall is left.
- **Theme** (`compile_theme.py`): a scatter's category label with a background gets the card's white (the name "You").
- **Layering** (`opzet-layering.json`): the nine extra cards of the tile and the name layer, on the file's scale.
- **Checks:** `a11y_check.py` reads a category label with a background of its own against that background;
  `number_checks.py` reads the bars from `BuildBar` and checks the two empty rows.
- **Tools:** `tiles/mk_tiles.py --picked`, and `tools/desktop_shots/step9/` (`round.py`, `comp_shots.py`, `marks.py`,
  `summary.py`, README): the render round as scripts, so the next session does not rebuild them.

*Verified* (Desktop 2.159, Windows culture nl-NL, throwaway copy; renders and the per-slot summary in
`project/deliverables/screenshots/Step9-build-your-own-2026-11-14/`).

| What | Result | Proof |
|---|---|---|
| Build renders: package A picked in Low, Expected, High; nothing picked; over the budget; a broken rule | yes, each from its own strip render, each beside the comp at the same view | renders 01 to 06 |
| Text rows against the comp, worst case over the six views | head 1.2 px; the ten names of the selector 1.1; Answers 1.1, Capex 0.5, NPV 1.0, A year 0.5; footer 0.7; title 0.5; the four numbers 1.6, their labels 1.7; range 0.8; rules 1.1; bar names 2.4; chart title 0.7; hover tag 0.4. Every slot has the comp's number of text rows in every view ("NPV through 2032" wraps, the empty-state sentence is two lines) | `summary-render-minus-comp.txt` (`step9/summary.py`) |
| Selector | the ten boxes within 0.3 px in y and 1.0 in x; names within 1 px; tile rules and table rules run on | `step9/marks.py`; renders |
| Bars | three rows 32 px apart from the top, as the comp: bars at y 472.0 to 488.8, 503.5 to 520.4, 535.1 to 552.5 (comp 471 to 489, 503 to 521, 535 to 553); bar ends within 2.3 px in x, names within 3 | `step9/marks.py` |
| **Empty state** | "Nothing picked yet", the R-B-2 sentence once (in `c_you_rules`), no number, no label, no bar, no zero line, no plan dot; the chart shows A alone; the footer reads "Picked: 0 moves, $0.0M of $60.0M" as the spec | render 04 |
| Over the budget | the alarm band fills the slot (within 1.4 px), white title 12 px inside it; the plan's line and the rules line change colour | render 05 |
| A broken rule | "Not yet within the rules: the kiosks need the booking app." in Burnt Tangerine, one line | render 06 |
| The plan dot and its name | "You" above its dot within 0.4 (Low), 0.9 (Expected) and 1.5 px (High) of the comp's; the dot 13 px (comp 12); at the opening state it lies under A. Tangerine dot and Burnt Tangerine name for a plan over the budget and inside the chart | renders 01 to 03, 06, 10 |
| Comparison chart | title follows the case; gridlines within 1.8 px; "You" 0.7 px from the comp's; ticks −$10M to +$10M by 5, as the comp | renders 01 to 03 |
| **A real toggle on the real page** | focus on the tile "Breakfast upgrade" (UI Automation), Space posted: the tile goes from off to on; four moves, $13.7M; title, numbers, range, rules, bars and footer follow; `tbl_moves` keeps ten rows | render 07 (`spikes_step2/s3_keys.ps1`) |
| **The saved selection survives a reload** | after `powerbi-desktop reload` the three tiles of A are on again and the tile reads "3 moves" | render 08; the tiles' toggle states read back |
| Typed text | `c_build_head`, `tag_cmp_build` and the table's four headers equal the spec letter for letter | script run in the session |
| `build_checks.py` (with the engine) | check 5: 129 ok, 2 known (20.5 / 20.6 %), 0 failed, Build with nothing picked included; checks 1, 3, 4 pass; check 2 strict passes, the old list is 16 measures and 2 report strings | `analysis/output/build_checks.txt` |
| `number_checks.py` | 766 checks, 765 ok, 1 known, 0 failed (3 new: the empty rows of the bars per case) | `analysis/output/number_checks.txt` |
| `a11y_check.py` | 0 failures | repeatable |
| Other validators | `schema_check` 195 files, 0 failing; `validate_json` 0; `validate_tmdl --strict` 0 errors, the 13 expected label-safe warnings; Microsoft's validator 0 errors | repeatable |

*Found on the way (binding for the next steps).*

1. **A strip render moves by about 3 px for 1 px of a visual's rect.** Desktop snaps a visual to device pixels at this
   zoom. To settle an edge, render at two rects one px apart and take the position both readings allow. The bars' rect was
   settled that way (x 1379 and 1380, right edge 1844 and 1847); a 1 px lift of the number cards read as 3.2 px.
2. **A native bar chart spreads its rows over its plot** and keeps 8 px above it and an outer padding of its own. To set
   bars from the top at a fixed pitch: a row source with empty rows (name of no-break spaces, value zero, a space as
   label), `outerPadding` 0, and a rect that makes five rows 32 px. The row source must be a table of its own.
3. **A reference line still draws in an empty chart.** Bind its value to a measure that is blank then.
4. **A card cannot hide its label** while its value is empty, and it centres its text. For text that must start at the top
   whatever its length, a `shape` takes its text and its ink from measures and has a vertical alignment.
5. **A scatter label hangs 16.7 px under an invisible point** (step 8). Above a dot near the plot's top the anchor leaves
   the plot: give the label a layer with hidden axes (its plot is then its rect) and a taller value range at the same
   scale. That layer stood 8 px low at first; it is set by its rect.
6. **A category label's colour can be a measure** (the name "You"), and its background must come from the theme:
   Microsoft's validator rejects `categoryLabels.backgroundColor` in a visual, as it did `labels.backgroundColor`.
7. **The slicer's accent bar** (position Bottom, width 1) is a tile's row rule; an outline has all four sides.
8. `s3_keys.ps1` finds no tile on its first run after a reload (it only opens the page tab); run it twice.
9. Scripts with nested quotes: the Write tool, never a heredoc (again).

*Deviations from the comp, and why* (open question 8 asks Bjorn about the first three; the others are Power BI's or
corrections that earlier steps already made).

- **Bars, from six moves on:** the rows share a plot of 157 px (the comp's 168), so six rows stand 26.2 px apart (28).
  **From eight moves on Power BI scrolls the bars** (it keeps about 22 px a row); the comp squeezes ten rows of 16 px
  text into 168 px, which no chart can print. Eight moves fit the budget ($46.5M), so a reader can meet the scrollbar.
- **Bars, the zero line:** it runs down the five rows (to y 617) while fewer are picked; the comp ends it under the last
  bar. The bars are 16.8 px thick (18).
- **A plan beyond $62M has no dot:** the proof chart's axis ends there, and Power BI draws nothing outside it. The comp
  draws that dot outside the chart, over the panel (and marks it red itself). Over the budget and inside the axis the
  dot is Tangerine (render 10). Its name is Burnt Tangerine there, not the comp's Tangerine (3.7:1 on white).
- **`tbl_moves`:** header words 9.2 px higher than the comp's (the native header is about 42 px, the comp's 32; S-3);
  "A year by 2032" 3 px further right and the table ends at x 1356, not 1352 (columns 74 and 118, S-3). The table starts
  2 px left of its slot, so Answers, Capex and NPV are within 2 px.
- **Comparison chart:** A's end label 4.9 to 6.8 px higher than the comp's; the zero line's name 3.8 px higher and 8 px
  right; gridlines run to the plot's right edge; over the budget (axis −$80M to +$20M) Power BI prints two ticks, the
  comp six. As in steps 7 and 8.
- **Proof chart:** ticks every $20M (step 8). The dot is 13 px (12).
- **Constructions that differ from doc 21 section 8:** the title is two cards, the numbers eight, the rules line a shape,
  the bars read `BuildBar`; reasons in "Built" and in doc 21 section 13.
- **Visual rects:** `tbl_moves` 1006, 238, 350, 364; `ch_build_bars` 1379, 462, 467, 157; `ch_cmp_build` 56, 685, 1819,
  316; the name layer 144, 195, 572, 385. The slot map and the spec keep the comp's numbers.

*Open items for later steps.*

- **Bjorn's keyboard try** was done through UI Automation: Space switches a tile (render 07). Tab was posted too, but
  where the focus went could not be read back in this session (step 2 read it: the next tile). The walk from the page
  into the selector with a real keyboard is part of step 10's keyboard pass.
- **Step 10:** `Alt You Nums`, `Alt Build Bars` and `Alt Moves` are first versions; the selector's spoken name is typed
  (`SELECTOR_ALT`); a tile's name is read with a trailing mark (the check icon), look at it in the Narrator pass. The
  extra cards of the tile, the alarm band, the name layer and the plan dot are out of the tab order. The hidden first
  column of `tbl_moves` gives each row its move's name for a screen reader.
- **Step 11:** the prune must keep the measures of "Built" and `BuildBar`, `BuildPoint[Name]`. Unused since this step:
  the waterfall measures (`Build WF Note (text)`, `Build WF Y Start` / `End`, `Build Project NPV (shown)`, `Build Row
  Flag`, `Alt Build Waterfall (text)`, the `Preset ... WF ...` and `Waterfall ...` families), `Build Point Size`, `Move
  Case (text)`, `Move Capex (num)`, the `Hover Tag ... SVG` measures, `BuildMove[Waterfall Label]`. The files
  `deliverables/deneb-specs/dn_build_selector.json` and `tools/build_selector_spec.py` are no longer read; they and
  Deneb's line in CREDITS.md are step 11's to settle.
- **Step 12:** in the browser, look at the name "You" over its dot, at the selector's check boxes and at the bars with
  eight moves picked.
- **Before the session:** the working tree was clean. The throwaway windows were ended with `Stop-Process` (throwaway
  only); the project was not opened in Desktop, and no Desktop window is left open.

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
4. **The deviations of step 5 on page 1 (no step is blocked by them).** Listed in the log of step 5 under "Deviations":
   the ring-i of the two hover tags in Burnt Tangerine instead of Tangerine (contrast floor); the folio table's header
   35 px and rows 23.7 px instead of 28 and 28 (a native table's header is taller than its rows); the line-end names of
   F1 and F2 9 to 10 px left of the comp; the "90%" label of F4 bold; the tab order note, rows, link in F4; the F4 link
   and the Definitions chip as measures. Recommended: accept them as technical corrections. If the Tangerine ring-i
   matters more than the check, say so and it gets a recorded waiver in `a11y_check.py`. Bjorn confirms, or names
   what must change.
5. **The deviations of step 6 on page 2 (no step is blocked by them).** Listed in the log of step 6 under "Deviations".
   Two need a word from Bjorn. (a) The ledger is a native table, and a native table sets every cell at the top of its
   row: "11.3%" stands on the first line of its row, where the comp centres it. Recommended: accept; the only other
   route is an image or an HTML table, which doc 21 rules out (P-3). (b) The three tab labels are Segoe UI Semibold, as
   doc 21 P-2 and the comp's own style sheet say; the comp's picture shows them in regular weight because of a CSS
   accident. Recommended: keep Semibold. If the picture is what was approved, say so: it is one argument in
   `tab_bar()`. The rest (the 2 px move of the headline on both pages, the ledger 6 px above its slot, the spoken head)
   are technical corrections.
6. **The end labels of the capital plan's chart (from step 7; no step is blocked by it).** The comp sets each label
   right of its line end ("Expected +$6.8M" beside the blue line). Power BI's line chart can set a data label above or
   under its point only. Built: Low under its line end, Expected and High above theirs; nothing overlaps in any case,
   but Expected's label stands 21 px above its line, close under High's. Recommended: accept. The alternatives are a
   legend-like key in the title row (three typed names, the values in the tooltip) or series names at the right edge
   without their values. Steps 8 and 9 use Above and Below as the comp has them, so this question is about this chart
   only. Bjorn confirms, or picks an alternative. The same answer covers the two ticks instead of four and the semibold
   line names (see the log of step 7, deviations).
7. **A's disc in the proof chart (from step 8; no step is blocked by it).** The comp fills A's disc with Coffee Blue
   (`#2589D8`) and sets a white "A" in it: 3.7:1, under the 4.5:1 floor for 12 pt text that `a11y_check.py` holds every
   label to. Built: Deep Coffee (`#1763A8`, 6.2:1), the colour the lettered discs had before the rebuild. Recommended:
   keep Deep Coffee. If the comp's lighter blue matters more, say so: it is one colour in `Named Point Color` and a
   recorded waiver in `a11y_check.py`. The same answer covers the other deviations of step 8, all Power BI's own (see
   the log of step 8, deviations): the table's header words 8.7 px high, ticks every $20M instead of every $10M, axis
   labels 4 to 5 px closer to their plots, A's end label 5 px higher, and Low's comparison plot 3 px higher at the top.
8. **The bars of the picked moves, and the plan dot (from step 9; no step is blocked by it).** Three things in Build are
   Power BI's and differ from the comp. (a) From eight picked moves on the bar chart scrolls: it keeps about 22 px a row
   and the tile holds seven. Eight moves fit the budget. Recommended: accept. The alternative is a smaller chart font for
   that chart only (under the 12 pt floor), or bars without names. (b) While fewer than five moves are picked the zero
   line of the bars runs on under the last bar, to the foot of the chart. Recommended: accept; without the line the bars
   lose their base. (c) A plan of more than $62M has no dot in the proof chart, because the axis ends there; the alarm
   band, the Tangerine line and the bars say that it is over the budget. Recommended: accept; the comp drew that dot
   outside the chart. The same answer covers the other deviations of step 9 (see its log): the table's header words
   9.2 px high and its last column 3 px right, and the name "You" in Burnt Tangerine over the budget.
