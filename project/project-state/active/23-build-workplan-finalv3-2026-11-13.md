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
| 1 | Branch and the five small spikes | todo | | | |
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

**Log:** _(filled in by the session)_

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

**Log:** _(filled in by the session)_

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

**Log:** _(filled in by the session)_

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

None at the start. A session that meets a question only Bjorn can answer adds it here and sets its step to `blocked`.
