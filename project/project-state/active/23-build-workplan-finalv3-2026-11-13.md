# 23 · Build workplan FinalV3: twelve steps, one prompt each (13 Nov 2026)

**For:** Bjorn and the local Claude Code sessions that build the approved rebuild.
**How to use:** one step per session. Open Claude Code on the Windows machine (Power BI Desktop is needed), pick the
model, paste the step's prompt. The session does that step only, writes its log below, updates the progress table,
commits and pushes. When it reports "ready for the next step", paste the next prompt in a **new** session.
**Model:** Claude Fable 5.2 at effort high (alternative: Claude Opus 5.5 at effort xhigh). Same for every step.
**What is built:** exactly the comp `project/design-prototypes/rebuild-comp-v10.html`. Content: doc 20. Construction:
doc 21. Where doc 22 differs from doc 21, doc 22 is newer. Positions: `opzet-layout-v10.json`. Column widths, axes,
label positions and the exact text per view: `rebuild-v10-spec.json`.

**Timing:** steps 1 to 4 on Sat 14 Nov; 5 to 7 on Sun 15 Nov (the cut line is that evening); 8 to 11 on Mon 16 Nov;
12 on Tue 17 Nov, then submit. The estimates are agent time; a step can be split with the resume prompt (section 3).

---

## 0 · Progress (each session updates its own row)

| Step | Title | Status | Date | Commit | Note |
|---|---|---|---|---|---|
| 1 | Branch and the five small spikes | done | 13 Nov | see step 1 log commit | S-1, S-5, S-6, S-8 pass; S-7 pass in a table cell, fallback for a card (`c_rec_lines` as two cards). Bjorn was not needed in Desktop |
| 2 | The two big spikes: hero table and native selector | todo | | | |
| 3 | Model foundations and the number checks | todo | | | |
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
10. **Cut line (doc 20 §1):** if the hero table is not verified by the evening of 15 Nov, switch to R-P2-3-FB. Tier order
    T1 before T2 before T3; when time runs short, drop T3 first, never a gate.
11. **Never publish.** Publish to Web is Bjorn's, on 17 Nov.
12. **Close-out (every step):** write your step's log below (built · verified, with the render or check that proves
    it · deviations from the comp and why · open items), set the progress row, commit, push, and end your reply with
    five lines: built · verified · deviations · what Bjorn must do · ready for the next step yes/no.

---

## 2 · The steps

### Step 1 · Branch and the five small spikes (Sat 14 Nov, about 1 to 1.5 h)

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

```text
Build step 1 of 12 · Branch and the five small spikes
Goodnight Inn, Power BI Dataviz World Champs 2027 · submission 17 Nov 2026 · today <date>

1. Git: git fetch origin; git checkout -b rebuild-finalv3 origin/claude/laughing-mendel-ruw64g; git push -u origin rebuild-finalv3
2. Read CLAUDE.md, then project/project-state/active/23-build-workplan-finalv3-2026-11-13.md: section 1 (rules, binding),
   the progress table and "Step 1". Read only the sources step 1 lists.
3. Do step 1 only. Stop when its "Done when" holds, or at a blocker you cannot solve within the rules.
4. Tell me exactly when you need me in Desktop (S-5, S-6) and what to click.
5. Close-out per rule 12: log, progress row, commit, push, five-line report.
```

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

### Step 2 · The two big spikes: hero table and native selector (Sat 14 Nov, about 1.5 to 2 h)

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

```text
Build step 2 of 12 · The two big spikes: hero table and native selector
Goodnight Inn, Power BI Dataviz World Champs 2027 · submission 17 Nov 2026 · today <date>

1. Git: git fetch origin; git checkout rebuild-finalv3; git pull
2. Read CLAUDE.md, then project/project-state/active/23-build-workplan-finalv3-2026-11-13.md: section 1 (rules, binding),
   the progress table, the log of step 1, and "Step 2". Read only the sources step 2 lists.
3. If step 1 is not done in the progress table, stop and tell me.
4. Do step 2 only. Stop when its "Done when" holds, or at a blocker you cannot solve within the rules.
5. Close-out per rule 12: log, progress row, commit, push, five-line report.
```

**Log:** _(filled in by the session)_

### Step 3 · Model foundations and the number checks (Sat 14 Nov, about 2 h)

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

```text
Build step 3 of 12 · Model foundations and the number checks
Goodnight Inn, Power BI Dataviz World Champs 2027 · submission 17 Nov 2026 · today <date>

1. Git: git fetch origin; git checkout rebuild-finalv3; git pull
2. Read CLAUDE.md, then project/project-state/active/23-build-workplan-finalv3-2026-11-13.md: section 1 (rules, binding),
   the progress table, the logs of steps 1 and 2, and "Step 3". Read only the sources step 3 lists.
3. If step 2 is not done in the progress table, stop and tell me.
4. Do step 3 only. Stop when its "Done when" holds, or at a blocker you cannot solve within the rules.
5. Close-out per rule 12: log, progress row, commit, push, five-line report.
```

**Log:** _(filled in by the session)_

### Step 4 · Text measures and `build_checks.py` (Sat 14 Nov, about 2 h)

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

```text
Build step 4 of 12 · Text measures and build_checks.py
Goodnight Inn, Power BI Dataviz World Champs 2027 · submission 17 Nov 2026 · today <date>

1. Git: git fetch origin; git checkout rebuild-finalv3; git pull
2. Read CLAUDE.md, then project/project-state/active/23-build-workplan-finalv3-2026-11-13.md: section 1 (rules, binding),
   the progress table, the log of step 3, and "Step 4". Read only the sources step 4 lists.
3. If step 3 is not done in the progress table, stop and tell me.
4. Do step 4 only. Stop when its "Done when" holds, or at a blocker you cannot solve within the rules.
5. Close-out per rule 12: log, progress row, commit, push, five-line report.
```

**Log:** _(filled in by the session)_

### Step 5 · Page 1 (Sun 15 Nov, about 2 h)

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

```text
Build step 5 of 12 · Page 1
Goodnight Inn, Power BI Dataviz World Champs 2027 · submission 17 Nov 2026 · today <date>

1. Git: git fetch origin; git checkout rebuild-finalv3; git pull
2. Read CLAUDE.md, then project/project-state/active/23-build-workplan-finalv3-2026-11-13.md: section 1 (rules, binding),
   the progress table, the logs of steps 1 to 4, and "Step 5". Read only the sources step 5 lists, and open the comp
   project/design-prototypes/rebuild-comp-v10.html (#p1).
3. If step 4 is not done in the progress table, stop and tell me.
4. Do step 5 only. Stop when its "Done when" holds, or at a blocker you cannot solve within the rules.
5. Close-out per rule 12: log, progress row, commit, push, five-line report.
```

**Log:** _(filled in by the session)_

### Step 6 · Page 2 frame and the decision card (Sun 15 Nov, about 2 h)

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

```text
Build step 6 of 12 · Page 2 frame and the decision card
Goodnight Inn, Power BI Dataviz World Champs 2027 · submission 17 Nov 2026 · today <date>

1. Git: git fetch origin; git checkout rebuild-finalv3; git pull
2. Read CLAUDE.md, then project/project-state/active/23-build-workplan-finalv3-2026-11-13.md: section 1 (rules, binding),
   the progress table, the logs of steps 4 and 5, and "Step 6". Read only the sources step 6 lists, and open the comp
   (#rec) in all three scenarios.
3. If step 5 is not done in the progress table, stop and tell me.
4. Do step 6 only. Stop when its "Done when" holds, or at a blocker you cannot solve within the rules.
5. Close-out per rule 12: log, progress row, commit, push, five-line report.
```

**Log:** _(filled in by the session)_

### Step 7 · Hero table and capital plan; the cut line (Sun 15 Nov, about 2 h, ends the evening)

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

```text
Build step 7 of 12 · Hero table and capital plan; the cut line
Goodnight Inn, Power BI Dataviz World Champs 2027 · submission 17 Nov 2026 · today <date>

1. Git: git fetch origin; git checkout rebuild-finalv3; git pull
2. Read CLAUDE.md, then project/project-state/active/23-build-workplan-finalv3-2026-11-13.md: section 1 (rules, binding),
   the progress table, the logs of steps 2, 3 and 6, and "Step 7". Read only the sources step 7 lists, and open the
   comp (#rec) in all three scenarios.
3. If step 6 is not done in the progress table, stop and tell me.
4. Do step 7 only. Stop when its "Done when" holds, or at a blocker you cannot solve within the rules.
5. Close-out per rule 12: log, progress row, commit, push, five-line report. Put the three cut-line decisions first.
```

**Log:** _(filled in by the session)_

### Step 8 · What waits, and why (Mon 16 Nov, about 1.5 h)

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

```text
Build step 8 of 12 · What waits, and why
Goodnight Inn, Power BI Dataviz World Champs 2027 · submission 17 Nov 2026 · today <date>

1. Git: git fetch origin; git checkout rebuild-finalv3; git pull
2. Read CLAUDE.md, then project/project-state/active/23-build-workplan-finalv3-2026-11-13.md: section 1 (rules, binding),
   the progress table, the log of step 7 (cut-line decisions), and "Step 8". Read only the sources step 8 lists, and
   open the comp (#alts) in all three scenarios.
3. If step 7 is not done in the progress table, stop and tell me.
4. Do step 8 only. Stop when its "Done when" holds, or at a blocker you cannot solve within the rules.
5. Close-out per rule 12: log, progress row, commit, push, five-line report.
```

**Log:** _(filled in by the session)_

### Step 9 · Build your own (Mon 16 Nov, about 2 h)

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

```text
Build step 9 of 12 · Build your own
Goodnight Inn, Power BI Dataviz World Champs 2027 · submission 17 Nov 2026 · today <date>

1. Git: git fetch origin; git checkout rebuild-finalv3; git pull
2. Read CLAUDE.md, then project/project-state/active/23-build-workplan-finalv3-2026-11-13.md: section 1 (rules, binding),
   the progress table, the logs of steps 2, 7 and 8, and "Step 9". Read only the sources step 9 lists, and open the
   comp (#build): opening state, nothing picked, over budget.
3. If step 8 is not done in the progress table, stop and tell me.
4. Do step 9 only. Stop when its "Done when" holds, or at a blocker you cannot solve within the rules.
5. Close-out per rule 12: log, progress row, commit, push, five-line report.
```

**Log:** _(filled in by the session)_

### Step 10 · Tooltips, alt text, tab order (Mon 16 Nov, about 1.5 h)

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

```text
Build step 10 of 12 · Tooltips, alt text, tab order
Goodnight Inn, Power BI Dataviz World Champs 2027 · submission 17 Nov 2026 · today <date>

1. Git: git fetch origin; git checkout rebuild-finalv3; git pull
2. Read CLAUDE.md, then project/project-state/active/23-build-workplan-finalv3-2026-11-13.md: section 1 (rules, binding),
   the progress table, the log of step 9, and "Step 10". Read only the sources step 10 lists.
3. If step 9 is not done in the progress table, stop and tell me.
4. Do step 10 only. Stop when its "Done when" holds, or at a blocker you cannot solve within the rules. Guide me
   through the keyboard pass and the Narrator pass one screen at a time.
5. Close-out per rule 12: log, progress row, commit, push, five-line report.
```

**Log:** _(filled in by the session)_

### Step 11 · Final checks and the FinalV3 render set (Mon 16 Nov, about 2 h)

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

```text
Build step 11 of 12 · Final checks and the FinalV3 render set
Goodnight Inn, Power BI Dataviz World Champs 2027 · submission 17 Nov 2026 · today <date>

1. Git: git fetch origin; git checkout rebuild-finalv3; git pull
2. Read CLAUDE.md, then project/project-state/active/23-build-workplan-finalv3-2026-11-13.md: section 1 (rules, binding),
   the progress table, all step logs, and "Step 11". Read only the sources step 11 lists.
3. If step 10 is not done in the progress table, stop and tell me.
4. Do step 11 only. Stop when its "Done when" holds, or at a blocker you cannot solve within the rules.
5. Close-out per rule 12: log, progress row, commit, push, five-line report. Tell me what to look at in the render set.
```

**Log:** _(filled in by the session)_

### Step 12 · Publish to Web gate (Bjorn publishes), then submit (Tue 17 Nov, about 1 h)

**Goal:** the published report works for a judge in any browser and locale; then Bjorn submits.
**Sources:** doc 21 §13 step 9, §16 (Publish to Web items); doc 20 R-X-3, R-G1.
**Do (with Bjorn, who publishes):** check the published report for: SVG cells in the hero and the A chip; tooltips;
the page buttons; an nl and a de browser locale (decimal points, no Dutch word, R-G1); the visual headers against the
hover tags; tooltip scale at 1366 px; one touch test. Every failure: fix in the generators, re-render, Bjorn
re-publishes. Record the results here and in doc 21 §16.
**Bjorn:** Publish to Web, the browser checks with the session, then the submission.
**Done when:** every check recorded as pass; the submission is in.

```text
Build step 12 of 12 · Publish to Web gate
Goodnight Inn, Power BI Dataviz World Champs 2027 · submission 17 Nov 2026 · today <date>

1. Git: git fetch origin; git checkout rebuild-finalv3; git pull
2. Read CLAUDE.md, then project/project-state/active/23-build-workplan-finalv3-2026-11-13.md: section 1 (rules, binding),
   the progress table, the log of step 11, and "Step 12". Read only the sources step 12 lists.
3. If step 11 is not done in the progress table, stop and tell me.
4. I publish (you never do). Walk me through the checks of step 12 one at a time; for every failure, find the cause,
   fix it in the generators, re-render, and tell me when to re-publish.
5. Close-out per rule 12: log, progress row, commit, push, five-line report.
```

**Log:** _(filled in by the session)_

---

## 3 · Resume prompt (a step that stopped before "Done when")

```text
Resume build step <N> of 12 · <title>
Goodnight Inn, Power BI Dataviz World Champs 2027 · submission 17 Nov 2026 · today <date>

1. Git: git fetch origin; git checkout rebuild-finalv3; git pull
2. Read CLAUDE.md, then project/project-state/active/23-build-workplan-finalv3-2026-11-13.md: section 1 (rules, binding),
   the progress table, "Step <N>" and its log so far. Start where the log stops; do not redo finished work.
3. Do the rest of step <N> only. Stop when its "Done when" holds, or at a blocker you cannot solve within the rules.
4. Close-out per rule 12: log, progress row, commit, push, five-line report.
```

## Open questions

None at the start. A session that meets a question only Bjorn can answer adds it here and sets its step to `blocked`.
