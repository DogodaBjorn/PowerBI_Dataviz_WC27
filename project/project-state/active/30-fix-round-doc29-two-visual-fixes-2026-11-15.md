# 30 · The two visual fixes of doc 29, on a branch of their own (15 Nov 2026)

**For:** Bjorn, and the agent that wrote the review and the prompt (docs 28 and 29).
**Sources:** `28-review-final-check-publish7-2026-11-15.md` and
`29-prompt-publish7-final-visual-fixes-2026-11-15.md`, both on `main` only (commits `5c86eb2`, `ee462ff`); the
package they reviewed, `project/deliverables/final-check-publish7/` (publish 7, build `a86e4ef` on `rebuild-finalv3`).
**Scope, as doc 29 sets it:** two visual fixes. No data, model, calculation, selection, sorting, colour or wording
changed. **Not merged, not published.** Branch `fix/publish7-visual-fixes`, cut from `rebuild-finalv3` at `a86e4ef`.
**Rules:** doc 23 section 1 (generators only, checks green, Desktop in a throwaway copy, every window closed without
saving, Bjorn publishes).

---

## 0 · Result

| Point of doc 29 | Status | In one line |
|---|---|---|
| 1 · "Your plan" shows every picked move, up to ten, without scrolling | done | The your-plan tile starts 64 px higher and its bar chart is 234 px high instead of 157 |
| 2 · "Hover a year" stands clear of "Cash positive above this line" | done | The hint moved along its row to the right of "The 2028 gate" |
| Rebuilt from the generators, checks rerun | done | Texts 142 of 142, numbers 809 of 809, alt texts 0 flags, accessibility 0 failures |
| Rendered with 3, 8 and 10 moves and on Recommended, at both sizes | done | Evidence in `project/deliverables/fix-publish7-visual-fixes/` |
| Merge, publish | **not done, on purpose** | The published report is still publish 7, without these fixes |

**What this means for the submission.** Publish 7 stays the version on the link until Bjorn decides otherwise. Taking
the fixes means an eighth publish and the gate once more (section 5). Not taking them costs nothing that the
reviewers of round 3 scored: both points were found after their round.

---

## 1 · Fix 1: the bars of "Your plan"

**What was wrong.** With eight moves picked (capture `walkthrough/19_p2-build-eight-moves.png`) the chart drew seven
bars and a scrollbar; the eighth, Energy programme at −$12.2M, was out of sight.

**Why a smaller row does not solve it.** Power BI draws a bar row no lower than 20 px. The setting that carries that
floor (`categoryAxis.preferredCategoryWidth`, "Minimum category width" in the format pane) was set to 16 and
rendered: the rows stayed 21 px and the scrollbar came back. So ten rows need 200 px of plot, and the chart had 157.
Inside the tile there was no room to find: title, four numbers, range, rules line (two lines in some states) and
200 px of bars come to 404 px, the tile was 392.

**What changed.** The room is above the tile. The panel's head ("Build your own / Click a move to add or remove it.")
has its text at the left and nothing beside it. So:

| Slot (page 2, Build your own) | Before | After |
|---|---|---|
| The your-plan tile (outline) | y 248, 392 px high | y 184, 456 px high: level with the head, 16 px under the card's top edge, as at its foot |
| Title or budget alarm, the four numbers, the range, the rules line | y 256, 304, 384, 408 | each 64 px higher; their spacing among themselves is as it was |
| The bar chart | y 462, 157 px high | y 392, 234 px high; its foot 7 px lower than before, 14 px inside the tile |
| The head's text box | 1072 px wide (ran under the tile's area) | 560 px wide: it ends 16 px left of the tile. Its text did not move |

Two settings of the chart changed with it. A quarter row of padding at both ends puts every bar in the middle of a
row of its own: without it the last bar ended on the chart's edge and the last name lost its descenders ("Energy
programme" in the eight-move view; publish 7 cut "Kingston +40 rooms" the same way). And the bar is half its row
instead of 60 %, so that it keeps its weight in the view everyone sees first.

**How it reads now** (measured on the renders):

| Moves picked | Rows apart | Bar | Before |
|---|---|---|---|
| 3 to 5 (the view opens with A's three) | 45 px | 20 px | 31 px apart, 19 px bar |
| 8 | 28 px | 13 px | 7 rows and a scrollbar |
| 10 | 23 px | 11 px | 7 rows and a scrollbar |

Names and values are 12 pt as everywhere else on the page. No colour, no sort order and no label changed.

**What you will notice besides the fix.** The opening state of Build your own looks different from publish 7: the
tile is taller and starts beside the head instead of beside the table's header row, and A's three bars stand 45 px
apart instead of 31. That is the price of ten rows: the chart always draws at least five rows (the model's rule, not
touched), and five rows fill whatever height ten rows need.

**Where it lives.** The slot map `project/design-prototypes/opzet-layout.json` (the tile and six slots; its `_doc`
says so; `opzet-layout-v10.json` keeps the comp's values) and `project/tools/opzet_report.py` (`BARS_RECT`,
`BARS_INNER`, `BARS_OUTER`, with the measurements in the comment above them). A rebuild reproduces it.

---

## 2 · Fix 2: the hover hint on Recommended

**What was wrong.** In the capital plan's chart the hint "ⓘ Hover a year" stood right above the zero line's name,
"Cash positive above this line": 17 px apart, both starting at the plot's left edge, so they read as one block.

**Why not a few px.** The hint sits between the gridlines at +$20M and +$10M, 34 px apart, and is 28 px high: there
are 3 px to gain upwards, and the caption stands above that. The zero line's name is placed by Power BI (left or
right end of its line, above or under it); at the right end it would run through the Expected line.

**What changed.** The hint moved along its own row, from the left of the gate line to the right of the gate's name:
x 872 to x 1260, 28 px after "The 2028 gate". Its wording, size and height on the page are as they were. No line
reaches that spot in any case: the High line passes 9 to 10 px under the hint's right end. (40 px after the gate's
name was rendered first and gave the same picture; 28 px keeps the hint a little further from the High line.)

**Where it lives.** The slot `tag_plan_cum` in `opzet-layout.json`; the reason is in `p2_capital_plan()` of
`opzet_report.py` and in the spec's note `charts.ch_plan_cum.hover_tag`.

---

## 3 · Verified

Rendered in a throwaway copy of the project in Power BI Desktop 2.159, the page cut into four strips
(`project/tools/desktop_shots/fix29/shoot.py`). Two sizes per view: the page at 100 % (one px per page px, what a
1920 px wide window shows) and at 64 % (what Power BI fits the page to in a 1366 px wide window, measured on
publish 7). Every render listed here was looked at.

| View | 100 % (1920) | 64 % (1366) | What was looked for, and found |
|---|---|---|---|
| Build your own, 3 moves (as it opens) | seen | seen | three bars, names and values whole, no scrollbar |
| Build your own, 8 moves (the selection of capture 19, with the Energy programme) | seen | seen | eight bars, Energy programme the last at −$12.2M, its name whole, no scrollbar |
| Build your own, 10 moves | seen | seen | ten bars down to "Refresh, 10 oldest −$27.3M", no scrollbar, no name or value cut or on another |
| Build your own, 9 moves without the booking app | seen | seen | the rules line takes two lines ("... over the budget; the kiosks need the booking app."); the first bar stands clear of it |
| Build your own, nothing picked | seen | seen | the empty state: title, one sentence, no chart, no zero line |
| Recommended: A, Expected | seen | seen | the hint 28 px right of "The 2028 gate"; "Cash positive above this line" alone at the left, 200 px from the hint |
| Recommended: A, Low and High | seen | seen | the same; in the High case the High line, then 3 px wide, passes 9 px under the hint's right end (10 px in the other two cases) |
| What waits, and why, Expected | seen | seen | as publish 7: this round does not touch it |

At 64 % everything on the page is small, the bar names as much as the table beside them (doc 27 left that on all
five reviewers' advice); the names and values of the ten rows stay apart and readable at that size.

**The numbers still agree.** 8 moves, the selection of capture 19: "Picked: 8 moves, $46.5M of $60.0M"; the tile
says 8 moves, $46.5M, −$21.2M, +$8.3M a year, 17.9%; the dot "You" stands at $46.5M and −$21M in the package chart;
the cash chart's title says yours ends behind A by $21.5M. All as on publish 7's capture. 3 moves: $9.4M, +$3.3M,
+$3.5M, 37.5%, the dot on A, the two cash lines one. 10 moves: $100.7M, −$66.8M (the ten bars add up to −$66.7M:
rounding of parts), the alarm "Over the $60.0M budget by $40.7M", the cash line Tangerine. The engine holds every
number against the organisers' workbook: `number_checks.py`, 809 of 809.

**Nothing else moved.** Against publish 7's build (`a86e4ef`) the generated report differs in sixteen visuals of
page 2 and nowhere else, and in each only by its position or size, plus the bar chart's two row paddings
(`checks/changed-against-publish7.txt` in the evidence folder lists every changed line). The model, the bookmarks,
page 1, the tooltip pages and the theme do not differ. As pixels: `fix29/diff_boxes.py` laid this branch's render of
Build as it opens over the same view rendered from `a86e4ef` earlier that day; every difference lies inside the
your-plan tile (x 1368 to 1872, y 180 to 648).

**Checks rerun on the rebuilt report** (reports in the evidence folder, `checks/`):

| Check | Result |
|---|---|
| `build_checks.py` (every text against the approved wording, the vocabulary, reachability) | 142 of 142 |
| `number_checks.py` (every number against the workbook) | 809 of 809 |
| `alt_texts.py` | 137 visuals in the tab order, 0 flags |
| `a11y_check.py` (alt texts, contrast, tab order against the reading order) | 0 failures |
| `strip_check.py` (nothing lies over a live visual or in its header strip) | 0 failures |
| `compliance_check.py`, `schema_check.py` (207 files), `pbir_detect.py`, `validate_tmdl.py --strict` | pass; 0 failing; 0 unwaived; 0 errors |
| The model, regenerated with `sketch_model.py --submission` | no difference to `a86e4ef` |

The tab order did not change: the same stops in the same order, and the reading order check passes with the tile
at its new place.

---

## 4 · What this round does not establish

- **These are Desktop renders, not the published report in a browser.** A browser at 1366 or 1920 px can only be
  driven on a published report, and this round does not publish. The page's layout is the same at every size (Power
  BI scales the whole page), so the scrollbar and the spacing cannot differ; how the service draws the text at 64 %
  is seen only after a publish.
- **The click test in a private window** that doc 28 asks for is still Bjorn's, on the public link.
- **No gate.** The technical gate (mouse, keyboard walk, languages, pixel comparison) ran on publish 7. A publish
  with these fixes needs it again; the tile's new place is inside the checks' reach (`strip_check.py` passes), but
  the gate is a test of the published report.
- **The dot "You" with nine or ten moves.** The package chart's capex axis ends at $62M, so a plan above that has no
  dot (10 moves: $100.7M). Publish 7 does the same from $62M on (capture 20, $69.3M); doc 29 did not ask for it and
  it is not touched.
- **The comp** (`rebuild-comp-v10.html`) still draws the tile and the hint where they were. From this round on the
  slot map, not the comp, is the reference for these seven slots.

---

## 5 · If Bjorn takes the fixes

Nothing here is done; each step waits for his word.

1. Merge `fix/publish7-visual-fixes` into `rebuild-finalv3` (a fast-forward: the branch is `rebuild-finalv3` plus
   this round).
2. A new publish copy from the generators, as for publish 7 (doc 27, log), opened in a new window. The window
   "Goodnight Inn" that is open now holds publish 7 **without** the fixes; a `.pbix` saved from it is publish 7.
3. Bjorn publishes (the eighth), then the gate and the walkthrough on the link.
4. `final-check-publish7/` describes publish 7 and is left as it is; captures 16 to 21 and 05 to 08 of its
   walkthrough would be the ones to replace.

---

## 6 · Log

- **15 Nov, evening.** Docs 28 and 29 read from `main`. Branch `fix/publish7-visual-fixes` cut from
  `rebuild-finalv3` at `a86e4ef`.
- **Fix 1, three tries in the throwaway copy.** (1) Chart 172 px high with the minimum row at 16: eight rows at
  21 px and the scrollbar again, so the floor of 20 px is real. (2) The tile 64 px higher, the chart 224 px: ten
  rows, but the last name's descenders cut at the chart's foot in the eight-move view. (3) A quarter row of outer
  padding and 234 px: every name whole. The positions first lived as an offset in the generator; `a11y_check.py`
  reads the tile from the slot map and failed on the tab order, so they moved into the slot map, where they belong.
- **Fix 2.** Rendered at x 1256, 1272 and 1260; 1260 kept.
- **The renders.** Desktop slowed down after some forty reloads (a capture took 33 s, one process held 6.5 GB), and
  captures began to miss visuals; the throwaway window was closed and the copy opened again. The session's screen
  turned between tall and wide during the round, which breaks a strip render halfway. `fix29/shoot.py` now holds the
  two sizes of every strip against each other, captures again where they differ, and stops when the canvas changed
  under it. One render that still lost a line of text (the footer "Picked: 3 moves") was caught by eye and redone
  with a stricter limit.
- **Close-out.** Report and model regenerated (`opzet_report.py`, `sketch_model.py --submission`, cultures removed):
  the model is equal to `a86e4ef`. All checks green (section 3). The throwaway window closed without saving; the
  window "Goodnight Inn" (publish 7) was not touched. Committed and pushed on the fix branch. No merge, no pull
  request, no publish.
