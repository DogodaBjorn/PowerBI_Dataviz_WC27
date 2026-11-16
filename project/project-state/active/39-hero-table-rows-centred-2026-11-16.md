# 39 · The hero table's text in the middle of its row (16 Nov 2026, night)

**For:** Bjorn, and the agent that picks the project up after him.
**Asked by Bjorn on 16 Nov, on doc 38:** "the text in the table is aligned to the top of the row instead of the middle;
this makes the highlight look a bit odd. Can we middle the text or is that impossible? And double check: are we still
able to call this native visuals only?"
**Base:** the report as doc 38 left it (he had not saved since 21:48).
**Branch:** `final/rows-centred`, moved into `rebuild-finalv3`. `main` untouched. **Not published.**

---

## 1 · The answer to both questions

**Vertical alignment.** A native table has no such setting: Microsoft's formatting catalog
(`powerbi-report-author formatting describe-object tableEx values | grid | columnFormatting | columnHeaders`) lists
`alignment` (left, centre, right) and nothing for top, middle, bottom. What a table has is **row padding**: the same
space above and under the text puts the text in the middle. That is what this edit uses.

**Native visuals only: yes.** The report holds no custom visual (no `publicCustomVisuals`, no visual type outside
Power BI's own: table, line, bar, column, area and scatter chart, card, slicer, button, shape, image, text box). The
bars in the table are images that DAX measures write and the native table shows; that was so before this edit.

## 2 · The edit (`project/tools/final_edit/f10_rows_centred.py <.Report dir> <.SemanticModel dir>`, can be run again)

| What | Was | Is |
|---|---|---|
| `tbl_hero` row padding | 0 | 5 px above and under the text |
| The bar images | 34 px high, as the row | 23 px: the row minus its padding. The bar (18 px) in the image's middle |
| A row | 34 px, the text on its top | 33 px, text and bar in its middle |
| The two reference lines (8 %, NPV 0) | one unbroken line down the ten rows | one stroke of 23 px in every row, 10 px apart: a dashed line |
| The table | y 224, 374 high | y 219.5, 378 high: the header takes the padding too (41.9 px, was 33.5), its words stay at their height |
| The ten rows | y 257.5 to 597.5 | y 261.4 to 592.4 |
| `cover_hero_yield`, `cover_hero_npv` (doc 33) | over the old rows | over the new ones |

**Why the lines are dashed now.** A line ran unbroken because its image was as high as its row. With padding an image
ends 5 px from the row's edge, so each row keeps its own stroke.

**Tried and dropped: two rectangles over the table for an unbroken line.** Desktop places a shape on whole screen
pixels; at the zoom of the test window that is a grid of 2 page px, and the line stood up to 1.7 px beside the point
where the NPV bars begin. Inside the image the line cannot leave the bars, at any zoom. The script removes the two
rectangles (`hero_line_8`, `hero_line_0`) if a copy still has them.

**Padding 5 and not 6.** With 6 the text's box is in the middle, but its capitals sit about 1 px low; with 5 the
capitals are within a quarter of a pixel of the row's middle, and the stroke is 2 px longer.

**The model** (341 measures, none new): `Hero Yield Bar SVG`, `Hero NPV Bar SVG`. `sketch_model.py` (`HERO_PAD`,
`HERO_IMG_H`), `opzet_report.py` (the grid) and `number_checks.py` (the image's height, the bar's place) say the same.

## 3 · Checks

On the final copy's own model (open in Desktop): texts against the spec 130 of 130, numbers 765 of 765, alt texts
0 flags. On `GoodnightInn-final.Report`: strip check 0, `pbir_detect` 0 unwaived, `validate` 0 errors; `a11y_check`
4 failures, the orange dot of Bjorn's save of 21:48, nothing of this edit.
Measured on a throwaway copy: a row 33.1 px, the header rule at y 260.7, the first row from 261.4; no scroll bar.

Evidence: `project/deliverables/final-room-to-invest/rows-centred/` (`table-before.png`, `table-after.png`,
`table-tried-unbroken-line.png`, `page2-recommended.png`, `checks/`). The gallery's `report-page2.png` and
`cover-b.png` were made again.

## 4 · The open window

Two measures synced into the open window's model and the report reloaded in it once. Not captured (doc 37 section 4);
seen on the throwaway copy, which holds the same files.

## 5 · Known, and left

- **The hover text of doc 33 was not tried again.** The covers are over the new rows by measurement; whether an image
  cell still overflows with padding was not measured. First thing to hover on the new link.
- Rendered in the Recommended view; the table is in no other view. Low and High not rendered (the bars' lengths
  follow the case, their place in the row does not).
- The generator's report has the same grid and images; it was not rendered.

## 6 · Open

1. Bjorn looks at it in the window "Goodnight Inn - Room to Invest": keep, or back to rows without padding (commit
   `ba793c6`).
2. He publishes and makes the Publish to Web link; then the gate and the walkthrough (a bar in the hero table first).
3. Then File > Save as `.pbix`, the phone check, the post (doc 35), 17 Nov.

## Log

- 16 Nov night: the catalog read; row padding tried on a throwaway copy; an unbroken line over the table tried,
  measured and dropped; the dashed line inside the images built, applied to the final copy and the open window's
  model; checks; pushed.
