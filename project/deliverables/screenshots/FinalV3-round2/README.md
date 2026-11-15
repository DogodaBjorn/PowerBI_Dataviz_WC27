# FinalV3 after review round 2 · the renders that changed (15 Nov 2026, step E of doc 25)

Renders of `project/pbip/GoodnightInn-opzet.pbip` at commit `4d54cf8` on `rebuild-finalv3` (steps B, C and D of
doc 25 on top of the FinalV3 set of 14 Nov), on the submission model (26 tables, 339 measures). Power BI Desktop
2.159, a throwaway copy of the project (the project itself was not opened). This is what publish 5 will show; the
proof on the published report is `gate.py` and `walk.py` after the publish.

**Later the same day:** the published report is publish 6 (`6227d6f`), three small things on from these renders: the
buttons' bubble is gone, the year tooltip's banner reads "CUMULATIVE CASH, $M · NOT DISCOUNTED", and F1's "Before
commissions" stands 2 px further left. The published views are in `../Committee-walkthrough-2026-11-15/`.

File names and views are those of `../FinalV3/` (its README has the table). Seventeen of the twenty changed:

| Files | What changed since FinalV3 |
|---|---|
| `01` page 1 | KPI labels without codes, F1's two names, F4's title, note and diamond key, the forward lines (steps B, D) |
| `02` to `04` Recommended | the copy round, the plan chart's end labels, caption and tag, the complaint fact in the ledger, the NPV panel's bar colours (steps B, C, D) |
| `05` to `07` What waits | the copy round: title, the three rows, the chart's title (step B) |
| `08` to `11` Build your own | the move names, the chart's title (step B) |
| `12` to `16` package tooltip | the move names, the last line without its tail (step B) |
| `20` Definitions | three entries reworded (step B) |

**Not here because nothing changed:** `17` (year tooltip), `18` (renovation band) and `19` (hotel) came out byte for
byte equal to the FinalV3 files (`cmp`), which is also the regression test of the render method.

## How they were made

As the FinalV3 set (`tools/desktop_shots/step11/README.txt`): page renders as four strips of 480 x 1080 stitched at
1.84 capture px per page px and scaled to 1920 x 1080; tooltip pages as ordinary pages with the hover's context as
page filters, 2.09 px per page px (the glossary 1.08). Two things were new this round:

- The session's screen turned between wide and tall several times. The strips only work on the tall screen; the
  renders here are all from strips (`tools/desktop_shots/round2d/README.txt` says how to tell and what to do).
- Picked moves whose names carry a comma ("Kiosks, 20 busiest") are passed with semicolons between the names
  (`mk_tiles.py --picked "a;b"`).

The limits of the FinalV3 set hold: no header artwork on a strip page, seams at page x 480, 960 and 1440, a tooltip
render is not a real hover. The comp pairs of FinalV3 were not remade: the comp still draws the copy of 14 Nov.
