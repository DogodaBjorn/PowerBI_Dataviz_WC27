# 32 · The last edit: card IV by location type, on the report as Bjorn saved it (16 Nov 2026)

**For:** Bjorn, and the agent that picks the project up after him.
**Asked by Bjorn on 16 Nov, after doc 31:** the key of card IV did not look like its plot. Give Airport blue, City
grey and Highway orange, each with its own mark, the same in the key as in the plot; the orange is the bright one of
the logo's full stop; the bar in card III becomes Burnt Tangerine, the darker colour for "bad". And: start from the
version he saved in Desktop at 11:32, because he moved visuals and text himself.
**Branch:** `final/f4-types`, moved into `rebuild-finalv3`. `main` untouched. **Not published.**

---

## 0 · What changes for whoever works on this next

**The report is hand-finished now.** Until 11:32 on 16 Nov the generator (`opzet_report.py`) wrote the report. Then
Bjorn finished it in Desktop and saved it. From here:

| | Where | What it is |
|---|---|---|
| The report that is submitted | `project/pbip/GoodnightInn-final.Report` (+ `GoodnightInn-final.pbip`) | Bjorn's save of 11:32 plus the edit of this doc. The same files as `E:\Goodnight Inn - Room to Invest`. |
| The generator's report | `project/pbip/GoodnightInn-opzet.Report` | Same design, texts and model bindings, but its own layout (doc 31's). Not what is submitted. |
| The model | `project/pbip/PillowKey.SemanticModel` | Still the generator's (`sketch_model.py --submission`), and equal to the final copy's model measure for measure (337). |
| An edit on the final report | `project/tools/final_edit/` | A script that edits the saved report in place and can be run again. Never regenerate over it. |

Commit `97927ff` holds Bjorn's save exactly as it was, before any edit.

## 1 · What Bjorn changed in Desktop (read from his save, not changed back)

- Page 1: the KPI row 6 px lower; card IV 16 px higher (to y 1020), its note narrower, its key 50 px to the left, the
  plot and its seven names 12 px up, its link line at the foot of the card; the three link lines of cards I to III
  at the foot of their cards; all four link lines start "Investment Option:" (were "Page 2:"); the footer row at
  y 1044.
- Page 2: the lines "Low case: ..." under the recommendation's numbers and the caption under the ledger are gone;
  the plan card is 22 px higher and its bar, gate paragraph, cash chart and milestones stand lower in it.
- Desktop's own rewrite, without effect on the picture: schema versions, layer and tab numbers (the same sequence
  as before, checked), the column setting of three tables, a sort entry on the ledger.

## 2 · The edit (`project/tools/final_edit/f4_types.py`)

| What | Was | Is |
|---|---|---|
| Hotels in card IV | Night circles for the seven fullest, Warm Grey circles for the rest | By location type: Airport a Coffee Blue circle (#2589D8), City a Warm Grey square (#8E897D), Highway a triangle in the logo's bright Tangerine (#FF783D) |
| The key | "Airport ◆ 82.0%": a Dusk diamond after the name | The type's own mark before its name, the same shape and colour as in the plot (a shape visual of 10 px, so no font decides how it looks) |
| The three average diamonds in the plot | Dusk, small | Not drawn. The number in the key is the average; the diamond was the mark the key showed while the eye saw circles |
| Marks in the plot | size −10 | size −5: a square and a triangle need a little more than a dot |
| The bar "10 years or more" in card III | Tangerine #E05A22 | Burnt Tangerine #A63F0E (measure `Age Band Color`) |
| `F4 Dot Color` | measure | removed, nothing binds it (337 measures) |

Put right in the saved file, none of it visible:

- **Scenario opens on Expected again.** The save carried High, the case clicked last; the bookmarks do not set it.
- The three typed link lines read "Page 2: ..." to a screen reader while they show "Investment Option: ...".
- The plot's top lies under the title's box since it moved up; a box on top takes the mouse, so the top row of
  hotels would lose its tooltip. The plot is one layer above the title now, the "Hover a hotel" chip above the plot.
- "No filter" entries from every chart to the three new marks; the two visuals taken out no longer stand in the
  bookmarks' target lists.

The generators and `number_checks.py` say the same (card IV, card III, the link lines), so the generated model
equals the final one and the text check reads the wording that is on the page.

## 3 · Checks

On the final copy's own model (open in Desktop): texts 138 of 138, numbers 759 of 759 (50 fewer than before: the
check of the dot colour per hotel left with the measure), alt texts 0 flags.
On `GoodnightInn-final.Report`: strip check 0, `pbir_detect` 0 unwaived, `powerbi-report-author validate` 0 errors,
tab sequence equal to the generator's on both pages. `schema_check.py` cannot read Desktop's newer schema versions
(404 at the source); on the generator's report it gives 211 files, 0 failing.

**One failure, by choice: the bright Tangerine is 2.6:1 on white; a mark needs 3:1.** Bjorn asked for the logo's
colour. The triangle and the row carry the type too, so the colour is not the only signal. `#F5692B` is the
nearest orange that reaches 3:1, if he wants it. Recorded as two waivers in `pbir-detect-waivers.yaml`.

`a11y_check.py` now reads the card frames from the report it checks (Bjorn resized two), not from the slot map.

## 4 · Known, and left

- A tooltip on a hotel was not tried by hand: Desktop's captures do not hover. The gate on the published link does.
- The title of the hotel tooltip page is underlined in the save (`tt-f4-hotel/ttd_head`); not changed.
- `final-room-to-invest/renders/` and `TEXT-before-after.md` show the state of doc 31, before Bjorn's own pass.

## 5 · Open

1. Bjorn publishes from the window "Goodnight Inn - Room to Invest" and makes the Publish to Web link.
2. The gate and the walkthrough on that link (`step12/gate.py`, `walkthrough/walk.py`): the hover on card IV first.
3. Then File > Save as `.pbix`, the phone check, the description, the submission on 17 Nov.

## Log

- 16 Nov: Bjorn's save read and committed as it was; the edit built and rendered on a throwaway copy, then applied to
  the final copy; checks on its own model; the final copy open in Desktop for Bjorn; pushed.
