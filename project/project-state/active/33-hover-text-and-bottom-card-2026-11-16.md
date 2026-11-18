# 33 · Hover text in the hero table, and the bottom card on both pages (16 Nov 2026, afternoon)

**For:** Bjorn, and the agent that picks the project up after him.
**Asked by Bjorn on 16 Nov, after doc 32:** two hovers in the hero table of page 2 show "weird text" (screenshots:
`data:image/svg+xml;utf8,<svg ...`), and the bottom card should line up the same on both pages, preferably by making
page 1's a little longer, with its "Investment Option" line.
**Base:** his own Desktop save of 13:18 (he saved again after doc 32). Commit `e948786` holds it untouched.
**Branch:** `final/hover-align`, moved into `rebuild-finalv3`. `main` untouched. **Not published.**

---

## 1 · What Bjorn changed in Desktop at 13:18 (read from his save, not changed back)

- Both pages: the headline 8 px higher (y 42); the eyebrow to the top right corner, right-aligned (y 0, its box ends
  at the page edge, x 1920); the logo to the top edge (y 0).
- Page 1: the notes of cards I to III 14 px lower (y 662.7).
- Page 2: Back out of the header and into the footer row (x 1545, y 1045.9).
- Card IV: Highway no longer `#FF783D` but theme colour 3 (Tangerine `#E05A22`) at 25 % darker, about `#A8431A`,
  on the plot and on the key's mark alike. The bright orange is gone from the report, and with it the one a11y
  failure of doc 32 (the two waivers for `#FF783D` in `pbir-detect-waivers.yaml` now match nothing).
- Desktop's own renumbering of tab orders (same sequence).

## 2 · The hover text: cause

A bar in `tbl_hero` is an image cell as high as its row (34 px). An inline image stands on the text baseline, so the
cell's content is 38 px high in a cell of 34 (measured in Desktop 2.159: `scrollHeight` 38, `clientHeight` 34). A table
shows a tooltip with the cell's value when the content does not fit, and that tooltip does not listen to
"Tooltips: off" (`visualTooltip.show` is false on this table; `desktop.PivotTableVisuals`:
`shouldHideDefaultTooltip` compares the two heights, `getBodyTooltipInfo` then returns the cell's text). The value of an
image cell is its data URI. So every one of the 20 bar cells showed its SVG source on hover. Text cells fit and show
nothing.

What does not fix it: the alt-text setting for image columns (`accessibility.altTextColumns`) changes the image's
alt attribute, not the tooltip; row padding or a lower image leaves gaps in the two reference lines, which run
unbroken down the ten rows.

## 3 · The edit (`project/tools/final_edit/f5_hover_align.py <.Report dir>`, can be run again)

| What | Was | Is |
|---|---|---|
| `cover_hero_yield`, `cover_hero_npv` (page 2, new) | - | Two invisible rectangles over the ten body cells of the two bar columns (x 536 and 796, y 255, 198 and 186 wide, 342 high: the cells plus 1 px). A box on top takes the mouse, so the cells are never hovered. Hidden with the table in the two other views, out of the tab order, "no filter" from every chart |
| `z_card_card_f4` (page 1) | foot at y 1020 | foot at y 1025.7, the foot of page 2's `z_card_bottom`; left edge and width were already equal |
| `lnk_f4` | y 985.7 | y 991.4: the same distance to the card's foot as Bjorn gave it |
| `btn_back` (page 2) | layer 10000, tab order before the headline | layer 86500 and tab order 500 |

**Back was dead in the 13:18 save.** In the footer row it lay under the box of the source line (1697 px wide, layer
86000), and a box on top takes the click: tried in Desktop on the untouched save, a click on Back did nothing; after the
edit it goes to page 1. Its place in the tab order is now between the source line and Definitions, as Next on page 1.

What the covers cost: over the two bar columns the row no longer lights up on hover, and a click there does nothing
(it did nothing before either: the table filters nothing). In focus mode the table stands alone, without the covers,
and the hover text is back.

The picture of page 2 is unchanged. The generator (`opzet_report.py`) does not have the covers: its report is not
what is submitted (doc 32 section 0).

## 4 · Checks

On the final copy's own model (open in Desktop): texts 138 of 138, numbers 759 of 759, alt texts 0 flags.
On `GoodnightInn-final.Report`: a11y 0 failures, strip check 0, `pbir_detect` 0 unwaived, `validate` 0 errors.
Hover, in a throwaway copy driven over Desktop's DevTools port (`desktop_shots/cdp.mjs`, Desktop started with
`WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS=--remote-debugging-port=9333`): before the edit the SVG text on a bar cell;
after it nothing on either bar column, nothing on the Move column.
Card feet measured in the two captures: y 1025.5 on both pages.

Evidence: `project/deliverables/final-room-to-invest/hover-align/` (`page1.png`, `page2.png` from the throwaway,
`final-copy-page1.png`, `final-copy-page2.png` from the final copy, `checks/`).

## 5 · Known, and left

- **The covers are proven in Desktop, not in the service.** Whether the published report behaves the same is the
  first thing to hover on the new link.
- The eyebrow of both pages ends at the page edge (x 1920, no margin), where Bjorn put it; the cards end at x 1888.
  Not changed.
- `E:\_throwaway_f5` (the test copy) could not be removed by the agent; it can go.
- The title of the hotel tooltip page is still underlined (doc 32).

## 6 · Open

1. Bjorn publishes from the window "Goodnight Inn - Room to Invest" and makes the Publish to Web link. Desktop asks
   to save first; that save is his.
2. The gate and the walkthrough on that link (`step12/gate.py`, `walkthrough/walk.py`): hover a bar in the hero table
   first, then a hotel in card IV, then click Back on page 2.
3. Then File > Save as `.pbix`, the phone check, the description, the submission on 17 Nov.

## Log

- 16 Nov afternoon: the 13:18 save read and committed as it was; the cause measured in a throwaway copy; the edit built
  and tried there, then applied to the final copy; checks on its own model; the final copy open in Desktop for Bjorn;
  pushed.
