# ScreenshotsFinalV1 — GoodnightInn-opzet, final 1.0 (12 Nov 2026)

Renders of `project/pbip/GoodnightInn-opzet.pbip` as saved by Björn in Power BI Desktop on 12 Nov 2026, 06:54,
captured through the Desktop Bridge at scale 2 and cropped to the page. Page 1 and 2 are 1920 x 1080 logical px
(here 2537 px wide); the tooltip pages are 480 px wide (here 1440 px, k = 3.0).

| File | What it shows |
|---|---|
| 01_p1-brand-review.png | Page 1, The Brand Review, as it opens |
| 02_p2-investment-strategy_recommended-A.png | Page 2, bookmark "Recommended: A", scenario Expected, all packages |
| 03_p2-investment-strategy_considered-B-C.png | Page 2, bookmark "Considered: B and C" |
| 04_p2-investment-strategy_build-your-own.png | Page 2, bookmark "Build your own", nothing picked yet |
| 10_tt-f1.png … 13_tt-f4.png | Report-page tooltips of the four findings on page 1 (hover a finding card) |
| 14_tt-f3-band.png | Tooltip of a renovation band in F3, rendered for "10 years or more" |
| 15_tt-f4-hotel.png | Tooltip of a hotel bar in F4, rendered for Toronto Pearson Airport |
| 16_tt-package.png | Tooltip of a dot in the package scatter on page 2, rendered for package A, Expected case (bottom 16 px margin clipped by the capture) |
| 17_tt-year.png | Tooltip of a year in the cumulative chart on page 2, rendered for 2030 |

The context-dependent tooltip pages (14 to 17) and the two bookmark states (03, 04) were rendered from a throwaway
copy of the project with a temporary page filter or the bookmark's visibility applied; the committed project has
no such filters. In the report the tooltips follow the hovered data point, and the report setting
`useScaledTooltips` scales them with the canvas (tooltip pages are 480 px wide against a 1920 px page).
