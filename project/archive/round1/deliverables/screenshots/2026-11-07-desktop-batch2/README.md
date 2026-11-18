# Desktop screenshots, batch 2 (7 Nov 2026): after the review-v2 fixes

**Own review notes on this batch: [SELF-REVIEW.md](SELF-REVIEW.md).** It lists every item of the fix guide
(`project/project-state/active/07-fixgids-review-v2.md`) with its status and the screenshot that shows it, and what
is still open. Batch 1 with the independent review: [../2026-11-07-desktop/](../2026-11-07-desktop/README.md).

Rendered by Power BI Desktop itself (2.159, Store app) at exactly 1920 x 1080, the same way as batch 1:
- Desktop starts with a local WebView2 DevTools port for one launch. The canvas viewport is set so that the
  fit-to-page page is exactly 1920 px wide, then captured page by page.
- **01-16** are fixed states. The report's own stored bookmark (`bm_p2_shortlist` / `bm_p2_plan`) and slicer values
  (package in focus, scenario, scatter view) were applied to a throwaway copy, reloaded through the Desktop Bridge and
  captured.
- **L1a-L5b** are real clicks on the canvas, in order. Desktop needs Ctrl+click to fire a button in edit mode. Each
  sequence starts from a fresh reload of the stored state.

Desktop runs with a Dutch (nl-NL) locale here. Numbers that a chart formats itself (waterfall labels, F3 and F4 bar
labels) show a decimal comma, and the waterfall total reads "Totaal". All cards, KPI values, tables and text are DAX
text now. In the L-series the mouse stays where it clicked: hover states, edit-mode selection frames and the tooltip
"CTRL+klik hier om volgen" are Desktop edit-mode chrome.

## Files
| File | Page | State | Package in focus | Scenario | Scatter |
|---|---|---|---|---|---|
| [01_P1_brand-review](01_P1_brand-review.png) | P1 | | | | |
| [02_P2_landing_A_Expected](02_P2_landing_A_Expected.png) | P2 | landing (how the page opens) | A | Expected | all |
| [03_P2_landing_A_Low](03_P2_landing_A_Low.png) | P2 | landing | A | Low | all |
| [04_P2_landing_A_High](04_P2_landing_A_High.png) | P2 | landing | A | High | all |
| [05_P2_landing_focusB_Expected](05_P2_landing_focusB_Expected.png) | P2 | landing | B | Expected | all |
| [06_P2_landing_focusC_Expected](06_P2_landing_focusC_Expected.png) | P2 | landing | C | Expected | all |
| [07_P2_landing_A_Expected_zoom](07_P2_landing_A_Expected_zoom.png) | P2 | landing | A | Expected | zoom |
| [08_P2_plan_A_Expected](08_P2_plan_A_Expected.png) | P2 | plan | A | Expected | all |
| [09_P2_plan_A_Low](09_P2_plan_A_Low.png) | P2 | plan | A | Low | all |
| [10_P2_plan_A_High](10_P2_plan_A_High.png) | P2 | plan | A | High | all |
| [11_P2_plan_B_Expected](11_P2_plan_B_Expected.png) | P2 | plan | B | Expected | all |
| [12_P2_plan_C_Expected](12_P2_plan_C_Expected.png) | P2 | plan | C | Expected | all |
| [13_P2_plan_B_Low](13_P2_plan_B_Low.png) | P2 | plan (batch 1: the broken state) | B | Low | all |
| [14_P2_plan_C_Low](14_P2_plan_C_Low.png) | P2 | plan | C | Low | all |
| [15_P2_landing_focusB_Low](15_P2_landing_focusB_Low.png) | P2 | landing | B | Low | all |
| [16_P2_landing_focusC_Low_zoom](16_P2_landing_focusC_Low_zoom.png) | P2 | landing | C | Low | zoom |

Live click sequence (each starts from 02, freshly reloaded):

| File | Action |
|---|---|
| [L1a](L1a_live_landing_A_before-click.png) [L1b](L1b_live_after-ctrl-click-Open-the-plan.png) [L1c](L1c_live_after-ctrl-click-Back.png) | before; Ctrl+click "Open the plan"; Ctrl+click "Back" |
| [L2a](L2a_live_clicked-High-tile.png) [L2b](L2b_live_High_after-Open-the-plan.png) [L2c](L2c_live_High_after-Back.png) | click the High tile; Ctrl+click "Open the plan"; Ctrl+click "Back" |
| [L3a](L3a_live_dropdown-open.png) [L3b](L3b_live_picked-C-in-dropdown.png) [L3c](L3c_live_C_after-Open-the-plan.png) [L3d](L3d_live_C_after-Back.png) | open the dropdown; pick C; Ctrl+click "Open the plan"; Ctrl+click "Back" |
| [L4a](L4a_live_clicked-scatter-point-A.png) [L4b](L4b_live_after-Open-the-plan-with-point-selected.png) [L4c](L4c_live_after-Back.png) | click the raspberry A dot; Ctrl+click "Open the plan"; Ctrl+click "Back" |
| [L5a](L5a_live_clicked-Zoom-on-A-B-C.png) [L5b](L5b_live_clicked-All-packages.png) | click "Zoom on A, B, C"; click "All packages" |

## Checked alongside
- **Offline:** `validate_tmdl` 32 files 0 errors; `validate_json` 80/0; MS JSON schema 80/0; `pbir_detect` PASS;
  `pbir validate` valid.
- **In Desktop (Power BI Modeling MCP):** 0 measure errors and 0 partition errors.
  - A, B and C resolve to 01+02+10, 01+09+10 and 01+07+10 in every scenario.
  - Axis ends: all packages $0-62M by -$60M to +$20M; zoom $0-40M by -$40M to +$20M.
  - For A, B and C in Low, Expected and High (9 combinations), the waterfall bars and the funded table rows add up
    exactly to the shown package NPV, and the profit-a-year rows to the shown package profit.
- **Focus-swap wiring in the report files:** both buttons point to existing bookmarks, and the bookmarks are
  display-only for the selected visuals; the slicers and both scatter layers stay outside the bookmarks.
