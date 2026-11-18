# Desktop screenshots, 7 Nov 2026 (build v2, commit 2a3e6ae)

**Review of these screenshots: [REVIEW.md](REVIEW.md)** (independent reviewer: 1 blocker, 11 major, 11 minor, 10 polish; the data-dependent findings checked against the model at the top). What the reviewer was told: [REVIEW-BRIEF.md](REVIEW-BRIEF.md).

Rendered by Power BI Desktop itself (2.159, Store app) at exactly 1920 x 1080: the size a 1920-wide
Publish-to-Web viewer sees. Unlike `project/design-prototypes/reference_screenshots/`, which shows the HTML comp,
these show the real report.

## How they were made
- Desktop was started with a local WebView2 DevTools port for that one launch. Through it the canvas viewport was set
  so that the fit-to-page page is exactly 1920 px wide, then captured page by page.
- **01-16** are fixed states. The report's own stored bookmark (`bm_p2_shortlist` / `bm_p2_plan`) and slicer values
  were applied to a throwaway copy, reloaded through the Desktop Bridge and captured.
- **L1a-L4c** are real clicks on the canvas, in order. Desktop needs Ctrl+click to fire a button in edit mode.

Desktop runs with a Dutch (nl-NL) locale here, so numbers formatted by a visual show a decimal comma (79,4%) and the
waterfall total reads "Totaal". Text measures are en-US. In the L-series the mouse stays where it clicked, so hover
states, visual header icons and the tooltip "CTRL+klik hier om volgen" are Desktop edit-mode chrome.

## Files
| File | Page | State | Package in focus | Scenario |
|---|---|---|---|---|
| [01_P1_brand-review](01_P1_brand-review.png) | P1 | | | |
| [02_P2_landing_A_Expected](02_P2_landing_A_Expected.png) | P2 | landing (how the page opens) | A | Expected |
| [03_P2_landing_A_Low](03_P2_landing_A_Low.png) | P2 | landing | A | Low |
| [04_P2_landing_A_High](04_P2_landing_A_High.png) | P2 | landing | A | High |
| [05_P2_landing_focusB_Expected](05_P2_landing_focusB_Expected.png) | P2 | landing | B | Expected |
| [06_P2_landing_focusC_Expected](06_P2_landing_focusC_Expected.png) | P2 | landing | C | Expected |
| [07_P2_landing_focusX-60M_Expected](07_P2_landing_focusX-60M_Expected.png) | P2 | landing | 01+02+03+05+08+09+10 ($60.0M) | Expected |
| [08_P2_plan_A_Expected](08_P2_plan_A_Expected.png) | P2 | plan | A | Expected |
| [09_P2_plan_A_Low](09_P2_plan_A_Low.png) | P2 | plan | A | Low |
| [10_P2_plan_A_High](10_P2_plan_A_High.png) | P2 | plan | A | High |
| [11_P2_plan_B_Expected](11_P2_plan_B_Expected.png) | P2 | plan | B | Expected |
| [12_P2_plan_C_Expected](12_P2_plan_C_Expected.png) | P2 | plan | C | Expected |
| [13_P2_plan_X-60M_Expected](13_P2_plan_X-60M_Expected.png) | P2 | plan | 01+02+03+05+08+09+10 ($60.0M) | Expected |
| [14_P2_landing_focusB_Low](14_P2_landing_focusB_Low.png) | P2 | landing | B (no package meets rule B in Low) | Low |
| [15_P2_plan_B_Low](15_P2_plan_B_Low.png) | P2 | plan | B (no package meets rule B in Low) | Low |
| [16_P2_plan_C_Low](16_P2_plan_C_Low.png) | P2 | plan | C (01+02+07 in Low) | Low |

Live click sequence (starts from 02):

| File | Action |
|---|---|
| [L1a](L1a_live_landing_A_before-click.png) [L1b](L1b_live_after-ctrl-click-Open-the-plan.png) [L1c](L1c_live_after-ctrl-click-Back.png) | before; Ctrl+click "Open the plan"; Ctrl+click "Back" |
| [L2a](L2a_live_clicked-High-tile.png) [L2b](L2b_live_High_after-Open-the-plan.png) [L2c](L2c_live_High_after-Back.png) | click the High tile; Ctrl+click "Open the plan"; Ctrl+click "Back" |
| [L3a](L3a_live_dropdown-open.png) [L3b](L3b_live_picked-C-in-dropdown.png) [L3c](L3c_live_C_after-Open-the-plan.png) [L3d](L3d_live_C_after-Back.png) | open the dropdown; pick C; Ctrl+click "Open the plan"; Ctrl+click "Back" |
| [L4a](L4a_live_clicked-scatter-point-A.png) [L4b](L4b_live_after-Open-the-plan-with-point-selected.png) [L4c](L4c_live_after-Back.png) | click the raspberry scatter point (A); Ctrl+click "Open the plan"; Ctrl+click "Back" |

## Checked alongside
- The focus-swap wiring in the report files: 17/17 checks pass. Each button points to an existing bookmark; the
  bookmarks apply to the selected visuals only, with data and page off; the slicers and the scatter stay outside the
  bookmarks; each panel visual is hidden in exactly one state; nothing overlaps.
- The numbers, via the Power BI Modeling MCP on the open model, for A, B, C and the $60M package in all three scenarios.
  The package capex, the package NPV, the waterfall total and the funded rows of the initiative table agree. Capex, NPV,
  cumulative net 2032, rooms added, hotels rated and A's run-rate match `project/analysis/output/packages.csv`
  (0 mismatches).
- Found: with B in focus in the Low scenario no package qualifies, and the plan's risk line reads "NPV in the Low case
  +M; the cumulative net turns positive in 2027" (screenshot 15). To fix in `sketch_model.py`.
