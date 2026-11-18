# 36 · Package A at a glance, one colour per decision, steps for tranches (16 Nov 2026, late evening)

**For:** Bjorn, and the agent that picks the project up after him.
**Asked by Bjorn on 16 Nov, with a screenshot of page 2:** "it's not clear within one single glance what is the selected
package A. I know it's the light blue, but it's not distinguishable enough. The right plan A is connected to the top 3
actions on the left and the first part of the bar chart, but it's not clear, not at all." His ideas: show plan A first
and then the optional additions, or more distinct colouring. Also: everything of tranche 3 one colour, plan A, tranche 2
and tranche 3 distinguishable, and he dislikes the word tranche. He asked what I think.
**Base:** his own Desktop save of 20:50 (the eyebrow of page 1 at x 1400 and 480 wide, page 2's 480 wide, the report
opens on page 1). Commit `718963e` holds it untouched.
**Branch:** `final/package-a-at-a-glance`, moved into `rebuild-finalv3`. `main` untouched. **Not published.**

---

## 1 · What was wrong

Package A showed in three places with three different, small signals: a letter "A" in the Status column and three
blue bars in the table, a title on the card at the right, and the first segment of the plan bar. Nothing said these
are the same thing. And the refresh was Night in the table (as the airport rooms) but slate in the plan bar.

## 2 · The edit (`project/tools/final_edit/f7_package_a.py <.Report dir> <.SemanticModel dir>`, can be run again)

| What | Was | Is |
|---|---|---|
| The three rows of package A in the table | white, as every row | a light blue ground (`#EAF2FB`) across all seven columns: one block |
| Status of those rows | "A" | "package A", in Deep Coffee |
| The card "Our recommendation: package A" | a white card as the others | the same card with an outline in Coffee Blue (2 px), "package A" in Deep Coffee |
| The label over the plan bar's first segment | "Tranche 1 · package A", Night | "Step 1 · package A", Deep Coffee |
| The refresh's bar in the table | Night (as the airport rooms) | slate `#717B8B`, the colour of its segment in the plan bar |
| Status of the gated rows | "2028 gate" three times | "step 2 · 2028" (Gatwick, Toronto), "step 3 · 2028" (the refresh, in Dusk) |
| The word | Tranche 1, 2, 3 | Step 1, 2, 3: plan labels, the gate rule ("It releases step 2 if"), What waits ("Step 2 · Airport extensions, +80 rooms", "Step 3 · Refresh, 10 oldest hotels", "One alternative and two later steps"), Definitions ("Step", "the next step"), two alt texts, the plan bar's series names |
| Column widths of the table | Move 280, Status 96 | Move 264, Status 112: "step 2 · 2028" fits; the bar columns and their covers stay where they are |

So one colour is one decision, the same in the table and in the plan bar: Coffee Blue is package A (now), Night is
step 2 (the airport rooms), slate is step 3 (the refresh), Warm Grey is not in the plan. Colour is not the only signal:
the status says it in words.

**Not done, and why.** "Show plan A first, then the optional additions" as a switch would hide the seven other moves,
and they are the proof ("Two moves pass both tests"). The tinted block gives the same reading order without a click.

**A second variant was rendered and not chosen:** the whole recommendation card on the light blue ground
(`--card tint`). The link with the rows is stronger, but the table inside the card stays white and the card looks
patched. `page2-variant-tinted-card.png` shows it; switching is one run of the script.

**The model** (341 measures, was 340): new `Move Row Tint`; changed `Move Status Color`, `Move Status Ink`,
`Move Status (text)`, `Plan T1/T2/T3 L1 (text)`, `Gate Rule (text)`, `Alt Plan Bar (text)`, `Alt Definitions (text)`;
the calculated table `WaitOption` (two titles). Measure and column names keep "Tranche" (nobody sees them, and a
rename breaks bindings). `sketch_model.py` and `opzet_report.py` say the same; `number_checks.py` knows the new status
words; `rebuild-v10-spec.json` was rewritten for the 18 changed lines (each read first: all were the intended words).

## 3 · Checks

On the final copy's own model (open in Desktop): texts against the spec 130 of 130, numbers 765 of 765, alt texts
0 flags. On `GoodnightInn-final.Report`: a11y 0 failures, strip check 0, `pbir_detect` 0 unwaived, `validate` 0 errors.
Text on the tint, computed: Dusk 6.8:1, Burnt Tangerine 5.6:1, Deep Coffee 5.5:1.
The final copy on disk equals the repo's report file for file; the two models are equal measure for measure.

Evidence: `project/deliverables/final-room-to-invest/package-a/` (`page2-before.png`, `page2-after-outline.png`,
`page2-variant-tinted-card.png` from the throwaway copy, `final-copy-page2.png` from the final copy, `checks/`).
The gallery's `report-page2.png` and `cover-b.png` were made again from the new page.

## 4 · How the open window was brought up to date

`project/tools/final_edit/f7_push_model.ps1 -DesktopPid -Port -Model` (Windows PowerShell 5.1): the measures, the
lineage tag of the new one, the two titles of `WaitOption` and a recalculation of that table; then the report reloaded
in the window. Tried on the throwaway window first. Before the reload both pages of Bjorn's window were compared with
the captures taken after his last save: nothing unsaved was showing (he had only zoomed out).

## 5 · Known, and left

- **Seen in the Recommended view only.** What waits and Build your own were not rendered again; the new titles of What
  waits were read from the model. First thing to click on the new link.
- Low and High were not rendered: the tint, the colours and the words do not follow the case; the numbers beside them do.
- Slate (step 3) and Warm Grey (not in the plan) are close (1.2:1). In the table the status word tells them apart, in
  the plan bar the white seam and the labels. A stronger step 3 colour is one constant (`STEP3` in `sketch_model.py`,
  and the plan bar's third fill).
- "Step" is my choice for the word; "Phase" or "Now, Next, Later" are one search and replace in the two scripts.
- A PowerShell lesson: `$model` and the parameter `-Model` are one variable (names ignore case).
- The tint's contrast is not in `a11y_check.py` (it reads card frames, not a measure's colour); computed by hand above.

## 6 · Open

1. Bjorn looks at it in the window "Goodnight Inn - Room to Invest" and says keep, change or revert (the state before
   is commit `718963e`).
2. He publishes and makes the Publish to Web link; then the gate and the walkthrough (`step12/gate.py`,
   `walkthrough/walk.py`): What waits and Build your own first, then a year in the cash chart, Low and High, a bar in
   the hero table, a hotel in card IV, Back.
3. Then File > Save as `.pbix`, the phone check, the post (doc 35), 17 Nov.

## Log

- 16 Nov late evening: the 20:50 save read and committed as it was; generators edited and the model regenerated; the
  edit tried on a throwaway copy in two variants; applied to the final copy and to the open window's model; checks on
  its own model; pushed.
- 16 Nov 21:30: Bjorn keeps the outlined version ("I like the looks of it so let's make that one definitive"). His
  Desktop window had gone strange (the canvas zoomed in, after the edits on disk and the reloads), and he asked for a
  save and a restart: the window was closed with Opslaan in its save dialog (the dialog is an embedded browser control;
  read and clicked through its HTML document), and the final copy opened again. The save equals the repo value for value;
  only the active page differs (page 2; the landing page is still page 1). Taken into `GoodnightInn-final.Report`
  untouched. The reopened window's model answers with the new words (Step 2, Step 3, package A's tint, 456 packages).
