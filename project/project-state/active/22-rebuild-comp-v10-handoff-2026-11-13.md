# 22 · Rebuild comp v10: build handoff (13 Nov 2026)

**For:** the build session (`pbir-operator`, through the generators), doc 21 section 13 steps 2 to 8.
**Status:** Bjorn approved the comp on 13 Nov ("looks great") and asked for the remaining overlap and clutter to be fixed
and handed over as files the build can use. This document records those fixes and the rules behind them.
**v10.1 (same day):** the four open questions of v10 are closed (section 6). The comp, `opzet-layout-v10.json` and
`rebuild-v10-spec.json` carry the closures.
**Inputs:** `20-requirements-storytelling-2026-11-13.md` (content), `21-powerbi-build-guideline-2026-11-13.md`
(construction). Where this document and doc 21 differ, this document is newer: every difference is listed in
sections 2 to 4, with the reason.

---

## 0 · The three files

| File | What it is | How the build uses it |
|---|---|---|
| `project/design-prototypes/rebuild-comp-v10.html` | The comp: P1 and P2 in three states, Low / Expected / High, working tabs, scenario pills, page buttons and Build selector. Toolbar: **Show slots**, **Copy slot map**, and an overflow check across all 12 views | The picture to build to. Open it next to every render |
| `project/design-prototypes/opzet-layout-v10.json` | The slot map, exported from the comp. Same shape as `opzet-layout.json` v9 | Doc 21 section 11 point 1: copy it over `opzet-layout.json` in the build branch. Tooltip pages carried over from v9; tt-f1 to tt-f4 dropped (N-4) |
| `project/design-prototypes/rebuild-v10-spec.json` | What a slot map cannot hold: column widths, row heights, bar domains, axis ends, label positions, formatters (`construction`), and the exact visible text of every slot in every view (`text`) | Constants for `opzet_report.py` and `sketch_model.py`; the `text` block is the target for the DAX assertions of step 3 and the copy check of step 8 |

All three come from the same page: the slot map and the spec are exported from the constants the comp draws with, so
they cannot disagree with the picture. To change anything, change the comp, re-run its overflow check, and export again.

## 1 · How the comp measures fit (and the rules that follow)

The comp sets text in Segoe UI where it is installed. Elsewhere it uses Selawik, Microsoft's metric-compatible
fallback, embedded in the page (CREDITS.md). Measured against the 13 Nov renders, Selawik Regular is within 0.5 % of
Segoe UI. Weight 600 is a derived proxy within 0.4 % of Segoe UI Semibold. So a line that wraps in the comp wraps in
Power BI.

**Red** in the comp means the text needs more than 2 px beyond its slot, or two chart labels meet. **Amber** means
within 2 px. The only amber left is the two headlines and the four KPI values (1.6 px of line box). They are unchanged
from today and render fine in the current report.

Rules learned from the v10 check:

1. **Height per line.** A 12 pt line is 21.3 px. A slot for 1 / 2 / 3 / 4 lines of 12 pt needs **24 / 48 / 64 / 88 px**.
   A 14 pt title line is 24.9 px; a 20 px head is 26.6 px. Doc 21's 60 px for three lines and 20 px for one line were too small.
2. **Check the longest scenario.** High adds a digit (+$12.6M, −$11.4M) and wrapped two cells of What waits that fit
   in Expected. The comp's check runs all three scenarios; a copy change is checked the same way before it is built.
3. **Semibold is about 2.7 % wider than regular.** Titles that fit as regular text can wrap as semibold.
4. **No line break after a minus.** Chrome and Power BI break between U+2212 and `$`. The formatters `fm` and `sfm`
   put U+2060 WORD JOINER between the sign and the `$`. The `text` block of the spec leaves the joiner out.
5. **Never let Power BI place two labels that can meet.** Scatter category labels and line series labels do not dodge
   each other. Where two can meet, the comp fixes the position per series, or uses a text box (section 3).
6. **Leave room for end labels inside the plot.** The x axis of the cumulative charts ends after 2032 (2032.6 or 2032.8)
   so a label on the 2032 point fits; no 2033 tick appears.
7. **One number, one place.** A data label that repeats a number printed next to it is clutter. If it also fails
   4.5:1, remove it (section 3, plan bar).

## 2 · Slots changed against doc 21 (all in `opzet-layout-v10.json`)

| Slot | Doc 21 (x, y, w, h) | v10 | Why |
|---|---|---|---|
| `lbl_hero_8` | x at the 8 % line, 220, –, 20 | 574, 216, 176, 24 | One 12 pt line needs 24 px. Starts at the 8 % line |
| `lbl_hero_0` | x at the 0 line, 220, –, 20 | 757, 216, 168, 24 | Same; **ends** at the 0 line (right-aligned), because starting there runs past the card |
| `c_rec_head` | 1160, 184, 704, 56 | 1160, 184, 704, 48 | The two paragraphs need 48; frees 8 px for the ledger |
| `c_rec_nums` | 1112, 248, 752, 64 | 1112, 240, 752, 64 | Follows the head up |
| `c_rec_lines` | 1112, 320, 752, 72 | 1112, 312, 752, 48 | Two lines need 43; 72 left a gap |
| `tbl_ledger` | 1112, 400, 752, 208 | 1112, 368, 752, 240 | The ledger needs 227 px with the v10 columns and copy; still ends at 608 |
| `c_ledger_caption` | 1112, 616, 440, 24 | 1112, 616, 408, 24 | Gives 32 px to the button (the caption needs 368) |
| `btn_build_invite` | 1560, 612, 304, 28 | 1528, 612, 336, 28 | The label wrapped at 304 |
| `c_plan_t1` … `t4` | y 724, h 60 | y 720, h 64 | Three lines need 64 |
| `c_you_nums` | 1384, 304, 464, 56 | 1384, 304, 464, 72 | "NPV through 2032" wraps in a quarter of 464 |
| `c_you_range` | 1384, 368, 464, 24 | 1384, 384, 464, 24 | Follows `c_you_nums` |
| `c_you_rules` | 1384, 392, 464, 40 | 1384, 408, 464, 48 | The empty-state sentence (R-B-2) takes two lines |
| `ch_build_bars` | 1384, 440, 464, 192 | 1384, 464, 464, 168 | Follows; ends at 632 inside the tile |
| `lbl_f4_*` (7, new) | – | see the spec, `charts.ch_f4.name_slots` | Section 3 |
| `tag_cmp_build` (back, v10.1) | not in section 8 | 1712, 692, 152, 28, state build (v9's place, z and tab) | Section 6, question 4 |

Doc 21's `c_plan_t*` x and w follow the capex shares and stay as they were. The K-3 row split (168 to 656, 672 to
1016) is untouched. Every slot a person placed is on the 8 px grid; the data-placed ones (hero reference labels, F4
names, plan labels) are not.

## 3 · Construction changed against doc 21

| Where | Doc 21 | v10 | Why |
|---|---|---|---|
| `tbl_ledger` columns | 176 / 248 / 72 / 96 / 160 | **112 / 280 / 88 / 96 / 176** | "What we track" holds its measure on one line at 280; Status holds "three quarters of the rise since 2021 undone" (High) in two lines at 176. Rows need 45 / 45 / 64 / 45 |
| `tbl_waits` columns | 176 / 208 / 216 / 256 / 216 | **168 / 224 / 216 / 256 / 208** | In High "The numbers" wrapped two cells and the table ran 20 px over |
| `tbl_moves` columns | not given | 92 / 64 / 72 / 116 | Header "A year by 2032" needs 116 on one line, so the rows stay aligned with the slicer |
| Hero "A year on cost" domain | 0 to 50 % (6.1) | **−10 % to 90 %** | P-4's own rule (min and max over three scenarios, rounded outward): the app reaches 82.1 % in High, Kingston −2.6 % in Low. NPV domain −32 to +12 $M as doc 21 |
| F4 names (4.5) | Scatter category labels from `Hotels[F4 Dot Label]`, zero-width spaces for the rest | **Seven text boxes `lbl_f4_*`** beside their dots, 12 pt Night, white fill, no border, decorative, out of the tab order. Category labels off; `F4 Dot Label` is not needed | With native labels above the dots, Toronto, Gatwick, Montréal and Phoenix overlapped and the airport row's names left the visual (S-4 failed in the comp). P1 does not follow the scenario, so the dots never move and static boxes are safe. The placement avoids all 50 dots, so no box covers a dot's tooltip |
| F4 close neighbours | ±0.3, sign open | Alternate −0.3, +0.3 … in occupancy order: Gatwick 0.3 below the Airport row, Montréal 0.3 above | Needed for a placement where nothing overlaps |
| Cumulative charts, end labels (P-5) | Series label for the name + a hidden series with a data label for the value | **One data label on the 2032 point per line**: the name and value come from the label-safe format string ("A +$6.8M"), white label background, legend and series labels off. Position per series: `ch_cmp_alts` A **Above**, B and C **Below**; `ch_cmp_build` A Above, You Below; `ch_plan_cum` **Right** for all three. X axis end 2032.6 (comparisons) or 2032.8 (plan) | A and B end close together in every scenario (Expected +$6.8M both; within $1.2M in Low), and You equals A when Build opens. Fixed Above/Below cannot collide; the axis end keeps the labels inside the plot |
| Comparison charts, value axis | auto | auto, with one tick below zero and 8 % headroom above the top line | In High, A's label above its line otherwise leaves the visual |
| `ch_plan_bar` data labels | "$9.4M", "$12.4M", "$29.5M", "$8.7M" (P-1) | **Off** | The four segment cards directly above print the same amounts. In the bar, $9.4M (Night on Coffee Blue, 4.2:1) and $29.5M (white on Night at 60 %, 4.3:1) failed 4.5:1. This also removes the plan bar's label-safe twins from the model work |
| Hero status words | font colour = `Move Status Color` | A `#1763A8`, 2028 gate `#12233D`, not now `#4B5466` (Dusk) | Warm Grey text is 3.5:1. The bars keep the mark colours |
| `ch_build_bars` | colours not given | positive Night, negative Tangerine; no title; category axis as wide as the longest picked name | R-G3 (Night = your plan, Tangerine = negative) |
| Plan dot "You" (8) | Night marker with a white label beside it | Night marker (Tangerine over budget) drawn **under** the A/B/C discs, "You" above it on white | At the opening state You sits on A; a label beside it covered B (R-B-3: B stays readable) |

## 4 · Copy that changed or was decided (for Bjorn to see once)

| Where | Doc 20 / 21 | v10 | Why |
|---|---|---|---|
| Ledger F4, "What we track" | "self check-in at the 20 busiest hotels · rooms added" | "self check-in hotels · rooms added" | Two lines at any width that fits the card; the "of 20" sits in the values ("0 of 20 · 0") and the hero names the 20 busiest hotels |
| Ledger F3, second line | "why: R-W-2" (a pointer) | "why: see What waits, and why" | Reads as a pointer to the tab that holds the reasoning, in one line |
| F4 names | Short name without "Airport" | **Toronto, Gatwick, Montréal** as the title and note say them; Phoenix, Orlando, Kansas City, Kuala Lumpur, Kingston; Gatwick and Montréal share one label "Gatwick, Montréal" (4 px apart at this scale) | Fewer, shorter words in a crowded corner; the same names as the copy |
| P2 headline | "$3.5M a year by 2032" | Follows the scenario: $1.0M / $3.5M / $6.2M | Every scenario-dependent number follows the slicer, as the subtitle's case word does |
| Empty Build state | R-B-2 sentence, place not given | In `c_you_rules` (the `Build Valid (text)` measure at n = 0); "Nothing picked yet" only in the title | One sentence, one place |
| Recommendation, line 2, **Low only** (v10.1) | "The app carries it: −$2.8M of the −$5.5M." (doc 20's grammar on Low numbers) | "The app carries it: **+$0.6M of that +$1.0M**. Every year without it leaves about $1.2M with the agencies." Expected and High keep doc 20's NPV wording | Section 6, question 1 |
| Tranche 3, "Why not now", **High only** (v10.1) | "It earns 11.5% a year on cost, above our 8% cost of money." | "It earns 11.5% a year on cost **but does not pay back by 2032 (−$24.1M)**." Low and Expected keep doc 20's wording; the second sentence is unchanged everywhere | Section 6, question 2 |

Copy variants for Low and High, written in doc 20's grammar, are in the spec's `text` block (hero title, ledger status
words, scatter subtitle, comparison titles, tranche numbers, B's and Tranche 2's "Why not now"). The two that read badly
in v10 were rewritten in v10.1 (the last two rows above).

## 5 · Build checklist (doc 21 section 13)

- **Step 1 (layout):** copy `opzet-layout-v10.json` over `opzet-layout.json`; add z and tab for the new slots to
  `opzet-layering.json` (the map carries proposals: negative tab = decorative).
- **Step 2 (spikes):**
  - S-1 also covers the word joiner: the nl-NL render must show "−$0.6M" on one line.
  - S-4 changes: render P1 once and measure where 60 % and 95 % land in `ch_f4_dots`. If the plot area differs from
    the comp's (x 16 to 1184 inside the visual), shift the seven `lbl_f4_*` boxes by that difference.
- **Step 3 (model):**
  - Assert the text measures against the spec's `text` block in all three scenarios.
  - Drop `Hotels[F4 Dot Label]` and the plan bar's label-safe twins.
  - Add the end-label format strings ("A +$6.8M", "Low −$4.6M") to the cumulative-chart end series.
- **Steps 5 to 7:** after every render, lay the PNG over the comp (px-prototype, ±2 px). Any text that wraps where the
  comp does not, or any label that meets another, goes back to the comp first (rule 2), not into the report.
- **Step 8:** `build_checks.py` can read the spec's `text` block as its vocabulary list.

## 6 · The four questions of v10, closed (v10.1, 13 Nov)

Bjorn asked to fix them. Each closure keeps doc 20's Expected copy and changes only the branch that was wrong.

1. **Recommendation line 2 in Low.** In Low, A loses $5.5M through 2032, so "the app carries it: −$2.8M of the −$5.5M"
   says the app carries the loss. On the yearly figure the app is the larger part in every case: 58 % in Low, 67 %
   Expected, 66 % High. **Rule:** when A does not pay back by 2032 in the case in view (only Low), line 2 weighs the app
   on the yearly figure line 1 has just given: "The app carries it: +$0.6M of that +$1.0M." ("that" points at line 1's
   "+$1.0M a year by 2032"; the line fits in 719 of 752 px.) Expected and High are unchanged. One branch in `Rec Lines (text)`.
2. **Tranche 3 in High.** The refresh earns 4.5 % / 7.9 % / 11.5 % a year on cost, so "under our 8 % cost of money"
   is false in High. What holds in every case is that it does not pay back by 2032 (−$30.5M / −$27.3M / −$24.1M), the
   same reason Tranche 2's row gives. **Rule:** at or above 8 % (only High) the first sentence becomes "It earns 11.5% a
   year on cost but does not pay back by 2032 (−$24.1M)." Low reads "under", Expected "just under", as doc 20. One branch
   in `Wait WhyNot (text)`; the What-waits table still fits in High.
3. **F4, Gatwick and Montréal on one label.** Kept. Both are named next to their dots, no name wraps, and R-P1-7's other
   checks hold (5 of the 7 Night dots in the Airport row, Kingston far left). Separate labels are impossible at this axis:
   the two dots are 0.13 points (4 px) apart, the upper one sits 8 px under the plot's top, Toronto's dot is 54 px to its
   right and Phoenix's 57 px to its left, so neither name fits on any side. The tooltip separates them (90.4 % and 90.2 %).
   The only other route is more height for the Airport row (axis end 4.2), which breaks the alignment with `c_f4_rows`.
4. **`tag_cmp_build`.** Back, at v9's place (1712, 692, 152, 28, build only; v9's z and tab). Doc 21 section 9 keeps
   `tt-year` with "your plan in Night", which only the Build comparison shows, so that chart opens a tooltip; doc 18 and
   P-7 give every tooltip target its hover tag. Its omission from section 8 reads as an oversight.

The comp now also checks that no hover tag, F4 name box or hero reference label sits on another visual's chart text.

## 7 · Kickoff prompt for the build session

Run the build in **local** Claude Code sessions on Bjorn's Windows machine: it needs Power BI Desktop for the spikes and
the renders, which a cloud session does not have. One session per build day keeps the context clean; each starts with
the prompt below and the day's steps.

| Session | Doc 21 section 13 steps | Ends with |
|---|---|---|
| Sat 14 Nov | 1 to 4: layout v10, spikes S-1 to S-8, model (10.1 to 10.3), T1 changes | spikes recorded in doc 21; `build_checks.py` 4 of 4; P1 render in nl-NL |
| Sun 15 Nov | 5 and 6: P2 frame, decision card, ledger, capital plan, hero, native selector, F4 | the cut-line decisions of the evening (hero, selector, F4) |
| Mon 16 Nov | 7 and 8: What waits, Build, tooltips, alt text, tab order, layering, render set, prune, parity check | `screenshots/FinalV3/`, keyboard and Narrator pass logged |
| Tue 17 Nov | 9: Publish to Web gate | Bjorn publishes, then submits |

```text
You are the build session for the Goodnight Inn entry (Power BI Dataviz World Champs 2027, round 1).
Submission 17 Nov 2026. Today: <date>. Today's steps: doc 21 section 13, steps <n to m>.

Setup (first session only): git fetch origin; create branch rebuild-finalv3 from
origin/claude/laughing-mendel-ruw64g. Later sessions: continue on rebuild-finalv3.

Read first, in this order: CLAUDE.md; project/project-state/status.yaml;
project/project-state/active/20-requirements-storytelling-2026-11-13.md (content);
21-powerbi-build-guideline-2026-11-13.md (construction); 22-rebuild-comp-v10-handoff-2026-11-13.md
(the approved comp: where 22 and 21 differ, 22 is newer). Open
project/design-prototypes/rebuild-comp-v10.html in a browser: that page is what we build, exactly.
Positions: project/design-prototypes/opzet-layout-v10.json. Column widths, axes, label positions,
formatters and the exact text of every slot per view and scenario: rebuild-v10-spec.json.

Rules:
- Only the pbir-operator agent changes project/pbip/, through the generators (opzet_report.py,
  sketch_model.py, pbir_lib.py); small diffs, validate after each (a11y_check.py, schema_check.py, and
  build_checks.py once step 4 has written it, doc 21 P-8). Research first: verify every PBIR/TMDL
  property against its schema, never memory.
- Commit before opening Desktop. Never save in Desktop; close every window without saving.
  Render through the throwaway copy. Delete PillowKey.SemanticModel/definition/cultures after
  each opzet_report.py run.
- After every render, compare the PNG with the comp at the same view and scenario (px-prototype,
  +-2 px) and the text measures with rebuild-v10-spec.json "text". Text that wraps where the comp
  does not, or labels that meet, go back to the comp first (doc 22 rule 2), never into the report.
- Copy is approved and peer reviewed: do not rewrite it. If something cannot be built as specified,
  take doc 21's technical fallback where it names one, record it, and tell Bjorn.
- Cut line (doc 20 section 1): if the hero table is not verified by the evening of 15 Nov, switch to
  R-P2-3-FB. Tier order T1 before T2 before T3; drop T3 first.
- Record spike results in doc 21 section 13 and what you built in a build log
  (project/project-state/active/23-finalv3-bouwlog-<date>.md). Update status.yaml at each gate.
- Never publish. Bjorn runs Publish to Web on 17 Nov.

End the session with: what was built, what was verified (renders, checks), what deviates from the
comp and why, and what the next session starts with. Commit and push rebuild-finalv3.
```

## Open questions

None. Doc 20's copy is unchanged except where sections 4 and 6 say so; Bjorn sees those rows once.
