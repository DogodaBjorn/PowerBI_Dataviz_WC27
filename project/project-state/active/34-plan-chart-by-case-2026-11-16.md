# 34 · The capital plan's cash chart, by case (16 Nov 2026, afternoon)

**For:** Bjorn, and the agent that picks the project up after him.
**Asked by Bjorn on 16 Nov, after doc 33:** the cash chart at the foot of page 2 is "too much grey: the gridlines, the
two different scenario lines and the cash positive line all the same colour". His idea: High dark blue, Low Burnt
Tangerine, or something that makes the cash positive line stand out. He asked what I suggest.
**Base:** the final copy as doc 33 left it (he had not saved since; the copy on disk equalled the repo).
**Branch:** `final/plan-chart-colours`, moved into `rebuild-finalv3`. `main` untouched. **Not published.**

---

## 1 · What was wrong

The chart had one colour with a meaning: Coffee Blue, 3 px, for the case in view. Everything else was a grey of about
the same weight: the two other cases Warm Grey 1.5 px (one dashed, one dotted), the zero line Dusk 1 px, the gridlines
a hairline. The zero line is what the chart is about (when does package A turn cash positive) and it read as one more
gridline.

## 2 · The edit (`project/tools/final_edit/f6_plan_cases.py <.Report dir> <.SemanticModel dir>`, can be run again)

| What | Was | Is |
|---|---|---|
| Low line and its end label | Warm Grey, dashed | Burnt Tangerine `#A63F0E`, dashed. The report's colour for "bad", on the one line that ends under zero |
| Expected line and its end label | Warm Grey, solid (Coffee Blue when in view) | Coffee Blue `#2589D8`, solid; the label Deep Coffee `#1763A8` |
| High line and its end label | Warm Grey, dotted | Night `#12233D`, dotted |
| The case in view | one Coffee Blue line of 3 px, whichever case | the case's own line at 3.5 px, in its own colour and dash; its label semibold, as it was |
| The two other cases | 1.5 px | 2 px: a thin dotted line was hard to follow |
| Zero line | Dusk, 1 px | Night, 1.5 px, its name in Night |
| Under the zero line | nothing | a light shade (Tangerine, 93 % transparent): under water is an area, not a line to find |
| Gridlines, the gate line, axis, caption, milestones | | unchanged |

Colour is never the only signal: every line keeps its dash, and its name and amount stand at its end in the same
colour.

**Why three measures.** A series has one colour. The thick line was one series (`Preset A Cumulative Net (sel)`), so it
could not follow the case's colour. Now there is one thick series per case: `A Cumulative In View (Low | Expected |
High)`, the case's line while it is in view and blank otherwise. 340 measures (were 337). `Preset A Cumulative Net
(sel)` stays in the model: the comparison charts and the year tooltip read it.

**The generators say the same.** `sketch_model.py` has the three measures, `opzet_report.py` builds the chart this way
(`PLAN_CASE`, `PLAN_SHADE`), and the generated chart equals the edited one object for object. `number_checks.py` checks
the new measures (6 checks more: 765).

## 3 · Checks

On the final copy's own model (open in Desktop): texts 138 of 138, numbers 765 of 765, alt texts 0 flags.
On `GoodnightInn-final.Report`: a11y 0 failures, strip check 0, `pbir_detect` 0 unwaived, `validate` 0 errors.
Rendered on a throwaway copy in the three cases (the scenario slicer set in the file, then reload):
`chart-expected.png`, `chart-low.png`, `chart-high.png`; `chart-before.png` is the same crop before the edit;
`final-copy-page2.png` is page 2 from the final copy.

Evidence: `project/deliverables/final-room-to-invest/plan-chart/` (with `checks/`).

## 4 · How the open window was brought up to date

The final copy was open in Desktop (the window of doc 33). The three measures went into its model over the engine port
(`sync_measures_to_desktop.ps1`, then the lineage tags of the files), and the report was reloaded in that window. Before
the reload both pages of the window were compared with the captures of doc 33: nothing unsaved was showing.

## 5 · Known, and left

- **The hover on a year was not tried.** The tooltip binding is unchanged (page `tt-year`), but the chart has six
  series where it had four. It is the first thing to hover on the new link.
- In the Low and the High view the thick line is dashed or dotted. That keeps one dash per case; a solid thick line
  for whichever case is in view is one line in the script (`CASES`).
- Expected ends 2030 at −$0.2M and 2031 at +$3.3M, so "cash positive during 2031" is right, but on the darker zero
  line the eye now sees the line touch zero at 2030.
- A second Desktop started with the DevTools option hangs on its splash screen while another Desktop is open (they
  share one WebView2 profile). Start the throwaway without it, or close the other window first.
- `E:\_throwaway_f5` (the test copy) is still on disk; it can go.

## 6 · Open

1. Bjorn publishes from the window "Goodnight Inn - Room to Invest" and makes the Publish to Web link. Desktop asks
   to save first; that save is his.
2. The gate and the walkthrough on that link (`step12/gate.py`, `walkthrough/walk.py`): hover a year in this chart and
   click Low and High first, then a bar in the hero table, a hotel in card IV, Back on page 2.
3. Then File > Save as `.pbix`, the phone check, the description, the submission on 17 Nov.

## Log

- 16 Nov afternoon: the design tried on the throwaway copy in the three cases; generators brought in line; applied to
  the final copy and to the open window's model; checks on its own model; pushed.
