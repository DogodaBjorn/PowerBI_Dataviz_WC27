# 37 · Grounds for step 2 and step 3, and the same grounds over the plan bar (16 Nov 2026, night)

**For:** Bjorn, and the agent that picks the project up after him.
**Asked by Bjorn on 16 Nov, on doc 36:** "the way we highlight with light blue the top 3 of package A, can we also do
that for step 2 and step 3, but then a lighter grade of their respective colours? And would it be possible and look ok
if we have the highlight colours on the stacked bar chart (the 60M plan) that sits below, adding the background colour
there too."
**Base:** his own Desktop save of 21:48. Commit `7569ef6` holds it untouched.
**Branch:** `final/step-tints`, moved into `rebuild-finalv3`. `main` untouched. **Not published.**

---

## 1 · What Bjorn changed in Desktop at 21:48 (read from his save, not changed back)

- Page 1: the titles of cards I to III 9 px lower (y 336), their notes at y 670, the subtitle at x 38, y 120; the line
  "44 of 50 hotels; 6 have no renovation date." under card III's chart (`c_f3_count`) removed.
- Both pages: an orange dot (Tangerine `#E05A22`) between the two parts of the eyebrow.
- Page 2: the tables of What waits and Build your own set to auto-size their columns (fit to content).

## 2 · The edit (`project/tools/final_edit/f8_step_tints.py <.Report dir> <.SemanticModel dir>`, can be run again)

| What | Was | Is |
|---|---|---|
| Rows of step 2 in the table (Gatwick, Toronto) | white | a light Night `#DEE0E4` (Night at 14 % on white) |
| Row of step 3 (the refresh) | white | a light slate `#E8EAEC` (the plan's slate at 16 % on white) |
| NPV bar of those three rows | the light neutral, as every move outside A | the step's own colour (Night, slate), as their bar of "a year on cost": the light bar faded on a ground |
| Over the plan bar (new: `plan_tint_1`, `_2`, `_3`) | the labels on the white card | each step's labels on the ground of its rows (light blue, light Night, light slate), as wide as its segment and standing on it. "Not needed" has none: it is not a step |
| The labels of the three steps | on their segment's left edge | 10 px inside their ground |

The grounds over the bar are rectangles under the labels: shown with the plan bar and hidden in the two other views
(bookmarks), out of the tab order, "no filter" from every chart. Their edges are the segments' as Desktop draws them
(measured: 52.7 to 337.0, 340.3 to 711.6, 715.8 to 1603.9; the bar's top at y 795.3); capex does not follow the case,
so they do not move.

**Does it look ok?** Yes for the plan bar: label and segment now read as one column per step, in the colour family
of its rows above. In the table the two new grounds are neutral greys (a tint of Night and of slate cannot be
anything else), lighter than one would want for telling step 2 from step 3 by the ground alone; the bars in full
colour and the status word do that. A stronger ground costs text contrast: on `#DEE0E4` the Burnt Tangerine of a
negative NPV is at 4.8:1, and 4.5:1 is the floor.

**The model** (341 measures, none new): `Move Row Tint` and `Move NPV Bar Color` changed. `sketch_model.py` says the
same (`STEP2_TINT`, `STEP3_TINT`); `number_checks.py` knows the new bar colours. The generator's report
(`opzet_report.py`) does not have the three rectangles: it is not what is submitted (as the covers of doc 33).
New: `project/tools/final_edit/model_sync.py`, the measure sync the edit scripts share from here on.

## 3 · Checks

On the final copy's own model (open in Desktop): texts against the spec 130 of 130, numbers 765 of 765, alt texts
0 flags. On `GoodnightInn-final.Report`: strip check 0, `validate` 0 errors, `pbir_detect` 0 unwaived.
**`a11y_check`: 4 failures, all four the orange dot of 21:48** (`#E05A22` on the banner: 3.2:1 and 2.2:1, where text
needs 4.5:1). The dot is a separator, not a word; left as Bjorn made it, and named to him.
Text on the three grounds, computed: Night 11.9:1 or more, Dusk 5.8:1 or more, Deep Coffee 4.7:1 or more, Burnt
Tangerine 4.8:1 or more; the slate bar on its ground 3.5:1.

**One waiver entered by the agent** (`plan-step-grounds` in `pbir-detect-waivers.yaml`): the three hexes of the
rectangles are not in the theme. They are the values of `Move Row Tint`; a shape has no row to read the measure from.
Under Bjorn's rule of 14 Nov (a waiver only where quality and accessibility are not at stake); his to confirm.

Evidence: `project/deliverables/final-room-to-invest/step-tints/` (`page2-before.png`, `page2-recommended.png`,
`page2-what-waits.png`, `page2-build-your-own.png`, `page1-as-saved-21h48.png`, all from a throwaway copy; `checks/`).
What waits and Build your own were rendered this round (they were not in doc 36): the new titles stand, the grounds are
hidden there, and Bjorn's auto-sized tables hold their layout. The gallery's two page images and `cover-b.png` were
made again.

## 4 · The open window

The measures went into the open window's model (`sync_measures_to_desktop.ps1`) and the report was reloaded in it,
twice (the second time for the interaction entries). Before that the window was compared with a render of the 21:48
save: nothing unsaved was showing. **The window was not captured after the reloads**: one capture of it came back as a
tiled picture of the whole Desktop window, and the view going strange earlier that evening followed a capture during a
reload. Its model was read instead (the grounds and bar colours answer as built).

## 5 · Known, and left

- Not seen in Bjorn's own window by the agent (see 4); seen on the throwaway copy, which holds the same files.
- Low and High were not rendered: grounds and colours do not follow the case.
- The orange dot's contrast (section 3). The logo's own orange `#FF783D` would reach 4.7:1 on the darker part of the
  banner and 3.2:1 on the lighter part.
- The removed line "44 of 50 hotels; 6 have no renovation date." was one of the caveats the reviewers of round 3 named
  as carrying trust; card III's chart now shows 44 hotels without saying so. Bjorn's choice; named to him.
- The bridge capture of a zoomed-out window can come back tiled; capture throwaway windows only.

## 6 · Open

1. Bjorn looks at it in the window "Goodnight Inn - Room to Invest": keep, change or revert (the state before is
   commit `7569ef6`).
2. He publishes and makes the Publish to Web link; then the gate and the walkthrough (`step12/gate.py`,
   `walkthrough/walk.py`).
3. Then File > Save as `.pbix`, the phone check, the post (doc 35), 17 Nov.

## Log

- 16 Nov night: the 21:48 save read and committed as it was; generators edited and the model regenerated; the edit
  tried on a throwaway copy in the three views; applied to the final copy and to the open window's model; checks on
  its own model; pushed.
