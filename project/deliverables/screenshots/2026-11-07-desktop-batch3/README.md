# Desktop screenshots, batch 3 (7 Nov 2026): after round 3

**Own review notes on this batch: [SELF-REVIEW.md](SELF-REVIEW.md).** It checks every point of the round-3 plan
(`project/project-state/active/08-verbeterplan-ronde-3.md`) against a screenshot (fixed / partly / open) and lists what
the builder found. Batch 2: [../2026-11-07-desktop-batch2/](../2026-11-07-desktop-batch2/README.md).

## Published report (Björn, 7 Nov)
**https://app.powerbi.com/groups/me/reports/4888e342-dfcc-49d7-8df1-ad893b9789a0/p1-brand-review?experience=power-bi**

Björn published the round-3 build to the Power BI service (his workspace, "My workspace"); the reviewer can check the
live report there next to these renders. This is a workspace link: it needs a sign-in with access to that workspace.
It is not yet the anonymous Publish-to-Web link (`app.powerbi.com/view?r=...`) the contest asks for, so the P2W gate
(R6/N10: the link in a clean browser, signed out, in nl-NL and en-US) is still open. The Desktop file it was published
from left a re-save in the working tree with the same 304 measures and the round-3 visuals (both door vignettes), so the
published report is the build these renders show.

## How these renders were made
Rendered by Power BI Desktop itself (2.159, Store app), the same way as batches 1 and 2:
- Desktop starts with a local WebView2 DevTools port for one launch. The canvas viewport is set so that the
  fit-to-page page is exactly 1920 px wide (and 1366 px for the W-series), then captured page by page.
- **01-15** are fixed states. The report's own stored bookmark (`bm_p2_shortlist` / `bm_p2_plan`) and slicer values
  (package in focus, scenario, scatter view) were applied to a throwaway copy, reloaded through the Desktop Bridge and
  captured.
- **L1a-L5b** are real mouse events on the canvas, in order: hovers (tooltips, button hover) and clicks. Desktop needs
  Ctrl+click to fire a button in edit mode. Each sequence starts from a fresh reload of state 02.
- **W1366a-c** are the landing, the plan state and P1 at 1366 px wide (R4).
- **Z1, Z2** are 1:1 crops of L2b and L2c (the Back button with the mouse on it, and with the mouse on the risk line).

Desktop runs with a Dutch (nl-NL) locale here. Numbers that a chart formats itself (waterfall labels, F3 and F4 bar
labels) show a decimal comma, and the waterfall total reads "Totaal" (N10, settled only by the Publish to Web test).
In the L-series the mouse stays where it was: hover states, edit-mode frames, the visual-header icons above a hovered
visual and the hint "CTRL+klik hier om volgen" are Desktop edit-mode chrome.

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
| [13_P2_plan_C_Low](13_P2_plan_C_Low.png) | P2 | plan | C | Low | all |
| [14_P2_plan_B_Low](14_P2_plan_B_Low.png) | P2 | plan | B | Low | all |
| [15_P2_landing_focusC_Low_zoom](15_P2_landing_focusC_Low_zoom.png) | P2 | landing | C | Low | zoom |

Live sequences (each from state 02, freshly reloaded):

| Files | Action |
|---|---|
| [L1a](L1a_hover-A.png) [L1b](L1b_hover-B.png) [L1c](L1c_hover-C.png) [L1d](L1d_hover-cloud-dot.png) | mouse on the A, B and C dots and on one cloud dot: the package tooltip (V2) |
| [L2a](L2a_ctrl-click-Open-the-plan.png) [L2b](L2b_mouse-on-Back.png) [L2c](L2c_mouse-on-risk-line.png) [L2d](L2d_ctrl-click-Back.png) | Ctrl+click "Open the plan"; mouse onto Back from outside (N8); mouse onto the risk line; Ctrl+click Back (the mouse then rests on "Open the plan": its hover state) |
| [L3a](L3a_clicked-High.png) [L3b](L3b_clicked-Low.png) | click the High tile; click the Low tile |
| [L4a](L4a_dropdown-open.png) [L4b](L4b_picked-C.png) [L4c](L4c_C_ctrl-click-Open-the-plan.png) | open the dropdown; pick C; Ctrl+click "Open the plan for package C" |
| [L5a](L5a_clicked-Zoom.png) [L5b](L5b_clicked-All.png) | click "Zoom on A, B, C"; click "All packages" |
| [W1366a](W1366a_P2_landing_A_Expected.png) [W1366b](W1366b_P2_plan_A_Expected.png) [W1366c](W1366c_P1_brand-review.png) | the landing, the plan state and P1 at 1366 px wide |
| [Z1](Z1_zoom_Back-on-hover.png) [Z2](Z2_zoom_risk-line-under-the-mouse.png) | 1:1 crops of L2b and L2c |

## Checked alongside
- **Offline:** `validate_tmdl` 32 files 0 errors; `validate_json` 98/0; MS JSON schema 98/0; `pbir_detect` 88 visuals,
  PASS; `pbir validate` valid (warnings only).
- **In Desktop (Power BI Modeling MCP):** 304 measures, 0 measure and 0 partition errors.
  - For A, B and C in Low, Expected and High (9 combinations) the waterfall parts add up exactly to the package NPV.
  - Axis ends: all packages $5-62M by -$60M to +$15M; zoom $5-42M by -$40M to +$15M.
  - Copy read back in all three scenarios: `Rec Answers`, `Rec Held`, `Alt C`, `Plan Risk` (A and C), `Plan Ops`
    (C), `Plan Title` (C); tooltip measures for A, B, C and three cloud packages (up to 8 moves).
- **Generated brand assets:** both vignettes are recorded with model, spec, candidate and crop in
  `design/brand-kits/goodnight-inn-hanger/assets/GENERATED-ASSETS.md`; all six candidates and the specs are in
  `project/deliverables/imagery/`.
