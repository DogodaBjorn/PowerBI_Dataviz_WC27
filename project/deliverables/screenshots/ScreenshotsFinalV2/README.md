# ScreenshotsFinalV2 — GoodnightInn-opzet, FinalV2 (12 Nov 2026)

Renders of `project/pbip/GoodnightInn-opzet.pbip` after the FinalV2 build (plan 15: M1, M2, S1 to S6, N1 to N6),
captured through the Desktop Bridge at scale 2 and cropped to the page. Page 1 and 2 are 1920 x 1080 logical px
(here 2494 px wide); the tooltip pages are 480 px wide (here 1440 px, k = 3.0).

## Desktop set

| File | What it shows | Evidence for |
|---|---|---|
| 01_p1-brand-review.png | Page 1, The Brand Review, as it opens | M2 (masthead clear of the hanger's hole), S1 (F2 legend on top, Goodnight Inn against the other three brands as one line), S5 (F1 title "fell 2.8 points since 2023"), N4 (2 px zero line under F3) |
| 02_p2-investment-strategy_recommended-A.png | Page 2, bookmark "Recommended: A", scenario Expected, all packages | M2 (the four F-chips in the footer row, the hanger free in the banner), S2 (short label "NPV range, $M") |
| 03_p2-investment-strategy_considered-B-C.png | Page 2, bookmark "Considered: B and C" | S4 (comparer title "B ends within $1M of A by 2032; C never breaks even") |
| 04_p2-investment-strategy_build-your-own-empty.png | Page 2, bookmark "Build your own", nothing picked | S2 (short label, the muted note "Pick moves on the left; your plan appears here." as the waterfall's title) |
| 05_p2-investment-strategy_build-your-own-filled.png | The same state with three valid moves (Booking app, Toronto +40 rooms, Revenue management) | the filled build waterfall with its own title, N1 (selector capex at one decimal: $4.3M, $24.8M), the rules line |
| 06_p2-investment-strategy_build-your-own-over-budget.png | The same state over the budget (Refresh 10 oldest, Boston new hotel, Energy programme: $69.25M) | the budget alarm (Tangerine band, "Not yet within the rules") |
| 10_tt-f1.png … 13_tt-f4.png | The four finding tooltips (hover a finding card on page 1 or a chip on page 2) | N5 (chart and note centred in the card, F1 to F3) |
| 14_tt-f3-band.png | Band tooltip, rendered for "10 years or more" | S3 (Goodnight Inn line in Coffee Blue, the band in Night), N2 (brand line "RevPAR $84.80" on the KPI's decimals) |
| 15_tt-f4-hotel.png | Hotel tooltip, rendered for Toronto Pearson Airport | S3, N2 ("ADR $106.82, RevPAR $84.80"), N6 (room-nights line gone, the page 64 px shorter), the value axis 60 to 100 % back |
| 16_tt-package-A.png | Package tooltip on package A, Expected | M1: A above the band, B under it with its own tick, C clear, the Low and High numbers on their own row |
| 17_tt-package-C.png | Package tooltip on package C, Expected | M1 on C: the band left of break-even, A and B clear at the right |
| 18_tt-year.png | Year tooltip, rendered for 2030 | N3 (title "To the end of 2030: where the four options stand") |

The context-dependent tooltip pages (14 to 18) and the five page-2 states (03 to 06) were rendered from a throwaway
copy of the project with a temporary page filter, the bookmark's visibility or a visual-level filter on the build
targets applied; the committed project has no such filters. Two consequences of that method, visible in 05 and 06: the
Deneb selector itself is not filtered, so its rows show no picked state and its footer still reads "Nothing picked
yet"; in the report a click on a row does both. In the report the tooltips follow the hovered data point, and the
report setting `useScaledTooltips` scales them with the canvas (tooltip pages are 480 px wide against a 1920 px page).

## Publish-to-Web set (20 to 28): NOT RENDERED

The files `20_p2w-p1-1366.png` to `28_p2w-mac-fonts.png` of plan 15, section 7, are not in this set. They need the
report published to the Power BI service with Publish to Web switched on (phase 5 of the plan), which only Björn can
do: publishing is the user's action (rule `mutation-safety.md`), and no service link exists yet. The gate's eight
checks (Deneb selector after a click, scaled tooltips at 1366 and 1920, the package tooltip on dot A high in the cloud,
the background at 45 % and 100 % zoom, en-US notation, one nl-NL session for the known mix, fonts on a Mac, the
keyboard round) stay open until then. Desktop evidence that stands in for part of them: the tooltips render at 480 px
with `useScaledTooltips` on (16 to 18), and the Deneb selector drives the numbers in Desktop (05, 06, via the
cross-filter stand-in described above).

Keyboard round (plan 15, phase 5 step 7): not run in the service. Known from Desktop (BUILD_LOG, 9 Nov): the tab
bar and the slicers are reachable and named; the Deneb selector cannot be operated with the keyboard (known
limitation for the submission notes).

## Notation (M3)

Accepted as decided in plan 15, phase 4: native labels follow the viewer's locale (here nl-NL Desktop: "+6,8",
"91,9%", "$84,99"), text measures and SVGs are en-US. Under an en-US browser everything shows points; the nl-NL
screenshot for the submission notes is item 26 of the Publish-to-Web set.
