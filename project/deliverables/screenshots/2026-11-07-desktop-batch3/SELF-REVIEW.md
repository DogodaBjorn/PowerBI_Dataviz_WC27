# Self-review, batch 3 (7 Nov 2026)

The builder (Claude Code) wrote this file; it is not an independent review. It does three things:
- it checks every point of `project/project-state/active/08-verbeterplan-ronde-3.md` against the batch-3 renders in
  this folder;
- it lists what I found myself while looking at them;
- it lists what is still open.

It is written so the next independent review can check each claim against a screenshot. File names refer to this
folder.

Status words: **fixed** = visible in the renders and checked in the model; **partly** = improved, with a stated rest;
**open** = not done in this round.

## Björn's new points (V1-V5)

| # | Point | Status | Where to see it | What changed |
|---|---|---|---|---|
| V1 | C framed as the answer to "why not renovate?" | **fixed** | 02, 06, 12, 13, L1c, L4a-c | Dropdown: "C · Why not renovate? For comparison". Scatter subtitle: "A: our recommendation · B: the alternative · C: why not renovate?". Landing: "C · Why not renovate? The refresh of the 10 oldest hotels instead of the kiosks at 20 desks: $36.9M, NPV −$23.4M. It answers F3 most directly, but it stays below zero through 2032 in every case (High −$11.4M)." Plan C, under its title "Package C (why not renovate?): …": "Shown to answer 'why not renovate?': it stays below zero through 2032 in every case, High included (−$11.4M)." The "every case" claim is computed from the model and drops out if it stops being true. B keeps "considered, not recommended". |
| V2 | Tooltip cards on the scatter | **fixed** (in Desktop; the browser check belongs to the P2W gate) | L1a-L1d | A native report-page tooltip (`tt-package`, 432 x 296), no custom visual. It shows the brand's chip (the hanger awake when the package pays back by 2032, asleep when not), the name (A, B, C by role, any other package as "A package of n moves"), NPV large in raspberry above zero or ember below, capex, the NPV in all three cases, "Pays back by 2032: cash positive from 2031" or "Does not pay back by 2032 in this case", and the moves by name. It works on the cloud too: a third, fully transparent scatter layer over all 456 packages carries the tooltip, and transparent markers still take the hover. So batch 2's N3 is closed. A click on that layer filters nothing. The answer "6 of 456 pay back by 2032" stays on the canvas, in the scatter title. |
| V3 | A quieter zero line | **fixed** | 02, 03, 04 | 1 px in plum-slate `#82798A` (was plum-grey at full weight). The band above it is shaded in a light raspberry tint and labelled "Pays back by 2032" at its right end, where no package sits. The line is still the first thing you find, but no longer the heaviest line on the page. A, B and C sit on top of it. |
| V4 | Canvas use of the scatter | **partly** | 02, 07, 15, W1366a | The axes now round to $5M with $1.5M of air (they were $10M). Capex starts at $5M instead of $0, because the cheapest package costs $9.4M. The empty band above zero is now the shaded "pays back" zone, so that space carries meaning. The scatter header is two lines (title and subtitle). **Zoom as the default was weighed and not taken:** Björn chose "All packages" on 7 Nov, and the title's "6 of 456" needs the whole cloud in view. The zoom stays one click away and now fills its frame better (L5a, 15: $5-42M by −$40M to +$15M, C in Low clear of the edge). Flipping the default is one value in `opzet_report.py`. |
| V5 | Brand recognition | **fixed** | 01, 02, L3a | Both pages now open with a brand row: the lockup at 56 px (was 40); the pay-off in raspberry, "Do not disturb, since 2020." on P1 and "Please make up the room." on P2; the masthead line; and a generated vignette. The vignette shows the same hotel door twice: closed at night with the hanger asleep on P1, open in the morning light with the hanger awake on P2. The scenario and view toggles are the kit's segmented pills (see S1). The funded chip sits next to "Our recommendation: package A", and the tooltip carries the chip as well. Colours and type: `pbir_detect` finds no hex outside the theme, and Trebuchet MS / Verdana are used throughout. **Asset step:** two Gemini renders, three candidates each, specs in `project/deliverables/imagery/_specs/`, chosen pair and crop recorded in `design/brand-kits/goodnight-inn-hanger/assets/GENERATED-ASSETS.md`. The generator embeds them as RegisteredResources; nothing was pasted in Desktop. |

## Open points from round 2

| # | Point | Status | Where | Notes |
|---|---|---|---|---|
| N8 | Proof that Back stays readable on hover | **fixed** | L2b, Z1, Z2, L2d | The mouse comes onto Back from outside: the seam-grey fill, with the plum-black label readable. The Desktop hint "CTRL+klik hier om volgen" belongs to the button and sits above it. With the mouse on the risk line (Z2) there is no hint and no hover state, only Desktop's edit frame around the text, so the risk line carries no stray button action. L2d shows the filled button's hover too: plum with a white label. |
| N9 | Risk line tautology in its own scenario | **fixed** | 08, 09, 10, 12, 13 | The case in view is now "this case": "Risks: in the Low case NPV falls to −$5.5M; in this case the cumulative net turns positive in 2031." In Low: "Risks: in this case it does not pay back by 2032." |
| N11 | No claims after 2032 | **fixed** | 09, 12, 13 | "turns positive after 2032" is gone: "in this case it does not pay back by 2032". The tooltip says "Does not pay back by 2032 in this case". It only names a cash year when the package pays back by the scatter's own rule (NPV at least zero), so it never contradicts the line. |
| R4 | Smallest text | **fixed** (the reviewer's 1366 check still owed) | W1366a-c, 01, 08 | 11 pt (15 px) is now the smallest text on the canvas: notes, axes, table cells, chart labels, slicers. At 1366 px that is 10.4 px. In Verdana, 11 pt reads like 12 pt Segoe UI (brand.yaml). The plan table now fits in 8 columns: the finding and the growth flag share one column ("F2 · growth"). Not done: the 16 px the plan suggested for 1920. That would need about a third less copy in the P2 panel. |
| S1 | Scenario tiles in the house style | **fixed** | 02, L3a, L3b | Both toggles are button slicers. Unselected: Sheet with a thin rounded outline. Selected: plum-black with white bold text. The tiles are 40 px tall like the dropdown and aligned at x 1112. |
| S10 | Which 20 hotels get kiosks; what the $50.6M is held back for | **fixed** | 02, 03, 04 | "The kiosks go to the 20 fullest hotels (9 airport, 7 highway, 4 city)". This is checked: they are exactly the 20 Goodnight Inn hotels with the highest 2025 occupancy, and the sentence only says "fullest" while that holds. "The other $50.6M is held back, to be decided again once all three moves are live, by Apr 2028: no other initiative pays back by 2032, even in the High case." |
| R6 / N10 | Publish to Web, both locales | **partly, Björn's** | [published report](https://app.powerbi.com/groups/me/reports/4888e342-dfcc-49d7-8df1-ad893b9789a0/p1-brand-review?experience=power-bi) | Björn published the round-3 build to the Power BI service on 7 Nov (link in the README). It is a workspace link that needs a sign-in, so it lets the reviewer check the live report in the service: tooltips, the button slicers and the embedded vignettes in a browser. The contest's gate is still open: the anonymous Publish-to-Web link (`view?r=...`), opened signed out in nl-NL and en-US, which settles the locale mix (chart labels "Totaal", "+6,8" in this nl-NL Desktop). The build stays P2W-proof: built-in fonts, embedded images, a native tooltip page, a native button slicer, no custom visuals. |

## Found while looking (new, N12-N17)

| # | Finding | Kind | Notes |
|---|---|---|---|
| N12 | Tooltip hover near A, B and C | small, accepted | The hover layer has a transparent dot under every package, so a mouse on the rim of B can hit a neighbouring cloud dot and show that package's card. Every card names its package, and the centre of A, B and C always gives their own card (L1a-L1c). |
| N13 | The cumulative chart in the plan state is small | taste | The 11 pt text took height, and the chart is now 112 px tall (W1366b). The three lines and the zero line still read, but the gap between Low and High is compressed. If the reviewer wants it back: drop the "In the hotels" line under A, or shorten the waterfall by 16 px. |
| N14 | The panel is still the densest part of the report | taste | The landing panel carries about 270 words at 11 pt. S10 added two answers. Each block is now one claim. A next round could cut "Within the rules" to the three ticks it needs. |
| N15 | The package dropdown is the classic slicer | small | It cannot take the pill shape. With its header off and a separate label it lines up with the tiles, but its box is the stock one. |
| N16 | The HTML comp is behind the build | process | `build_opzet_comp.py` still draws the v2 slots. The PBIP and these renders are the reference for round 3. |
| N17 | Gemini model | process | The key's config file selects `gemini-3.1-flash-image`, while DEPENDENCIES.md still names `gemini-2.5-flash-image` as the default. It is recorded in GENERATED-ASSETS.md and the BUILD_LOG. |

## What to look at first
1. **02** (the landing): the brand row, the pills, the shaded payback zone, and the panel with S10 and C's framing.
2. **L1a-L1d**: the tooltip on A, B, C and the cloud.
3. **01**: P1 with the brand row and the 11 pt notes.
4. **12 / 13**: plan C, the comparator role in its title and first line.
5. **W1366a-c**: legibility at laptop width.
