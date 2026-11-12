# ScreenshotsFinalV2 — GoodnightInn-opzet, FinalV2 (12 Nov 2026)

Renders of `project/pbip/GoodnightInn-opzet.pbip` after the FinalV2 build (plan 15: M1, M2, S1 to S6, N1 to N6) and the
fixes from verification 17 (short bar labels in the build waterfall, proven up to all ten moves; renders 05 to 08 after
real clicks), captured through the Desktop Bridge at scale 2 and cropped to the page. The page renders 01 to 08 were
all remade on 12 Nov (evening) from the committed tree, in a 1920 x 1080 Desktop window: 1920 x 1080 logical px, here
2940 px wide. The tooltip pages (10 to 18, unchanged since the morning set) are 480 px wide (here 1440 px, k = 3.0).
Later that evening, on Björn's go: the hover signifier (a 16 px Tangerine ring-i at the top right of every visual that
opens a page tooltip), the footer-row hint "hover for more" and the Definitions chip with its tooltip page tt-glossary.
Renders 01 to 04 were remade for that round and 19 is new; 05 to 08 are from the round before and differ only in the
footer row (five chips, the hint) and the badges.

## Desktop set

| File | What it shows | Evidence for |
|---|---|---|
| 01_p1-brand-review.png | Page 1, The Brand Review, as it opens | M2 (masthead clear of the hanger's hole), S1 (F2 legend on top, Goodnight Inn against the other three brands as one line), S5 (F1 title "fell 2.8 points since 2023"), N4 (2 px zero line under F3); the badge on the F3 and F4 cards (the two with hover detail) and nowhere else, the footer row with the hint and the Definitions chip |
| 02_p2-investment-strategy_recommended-A.png | Page 2, bookmark "Recommended: A", scenario Expected, all packages | M2 (the hanger free in the banner), S2 (short label "NPV range, $M"); the badge on the scatter card (right of the zoom toggle) and on the cumulative chart, the footer row: source line, hint, five chips each with its badge |
| 03_p2-investment-strategy_considered-B-C.png | Page 2, bookmark "Considered: B and C" | S4 (comparer title "B ends within $1M of A by 2032; C never breaks even"); the badge on the small scatter card and on the comparer |
| 04_p2-investment-strategy_build-your-own-empty.png | Page 2, bookmark "Build your own", nothing picked | S2 (short label, the muted note "Pick moves on the left; your plan appears here." as the waterfall's title); the badge on the small scatter card and on the comparer, none on the selector or the plan tile (no tooltip there) |
| 05_p2-investment-strategy_build-your-own-filled.png | The same state after three real clicks in the selector (Booking app, Revenue management, Toronto +40 rooms) | the working click chain: three ticked rows, the selector footer "Picked: 3 moves, $13.2M of $60.0M", the plan tile "Your plan: 3 moves, live by May 2028", the rules line "Within the rules", the waterfall with its own title and the bars "App", "Rev. mgmt", "Toronto +40" (verification 17: no ellipsis); the plan dot in Tangerine on the scatter; N1 (selector capex at one decimal) |
| 06_p2-investment-strategy_build-your-own-over-budget.png | The same state after three real clicks over the budget (Energy programme, Boston new hotel, Refresh 10 oldest: $69.25M) | the budget alarm from a click: three ticked rows, the selector footer in Tangerine "Over budget by $9.25M: $69.25M picked, the cap is $60.0M", the Tangerine band "Over the $60.0M budget by $9.25M", "Not yet within the rules: over the budget."; the bars "Energy", "Boston", "Refresh 10" |
| 07_p2-investment-strategy_build-your-own-eight-moves.png | Eight real clicks, the first eight rows ($46.45M, within budget) | the waterfall with eight bars and the total: Desktop rotates the labels and every one reads in full ("App", "Rev. mgmt", "Kiosks", "Breakfast", "Gatwick +40", "Toronto +40", "Kingston +40", "Energy", "Totaal"); "Your plan: 8 moves, live by Jul 2028", "Within the rules: 8 moves, 6 growth, $46.45M of $60.0M"; the comparison chart's title "yours ends behind A by $21.5M in 2032 and is not cash positive by 2032" |
| 08_p2-investment-strategy_build-your-own-all-ten.png | All ten rows clicked ($100.7M, over the budget by $40.7M) | the worst case for the axis: ten bars plus the total, all labels in full; the alarm band "Over the $60.0M budget by $40.7M", footer "Over budget by $40.7M: $100.7M picked, the cap is $60.0M"; the plan dot is beyond the scatter's capex axis ($62M) and so not drawn, as designed |
| 10_tt-f1.png … 13_tt-f4.png | The four finding tooltips (hover a finding card on page 1 or a chip on page 2) | N5 (chart and note centred in the card, F1 to F3) |
| 14_tt-f3-band.png | Band tooltip, rendered for "10 years or more" | S3 (Goodnight Inn line in Coffee Blue, the band in Night), N2 (brand line "RevPAR $84.80" on the KPI's decimals) |
| 15_tt-f4-hotel.png | Hotel tooltip, rendered for Toronto Pearson Airport | S3, N2 ("ADR $106.82, RevPAR $84.80"), N6 (room-nights line gone, the page 64 px shorter), the value axis 60 to 100 % back |
| 16_tt-package-A.png | Package tooltip on package A, Expected | M1: A above the band, B under it with its own tick, C clear, the Low and High numbers on their own row |
| 17_tt-package-C.png | Package tooltip on package C, Expected | M1 on C: the band left of break-even, A and B clear at the right |
| 18_tt-year.png | Year tooltip, rendered for 2030 | N3 (title "To the end of 2030: where the four options stand") |
| 19_tt-glossary.png | The definitions tooltip (hover the Definitions chip in the footer row of either page); 480 x 544, here 988 px wide (k = 2.06, a Desktop capture at a 1920 window) | the nine one-line definitions (NPV, capex, run-rate, pays back / break-even, Low / Expected / High, NPS, ADR, RevPAR, OTA) in the orange tooltip skin; needs no hovered context, so it comes straight from the copy |

## How the renders were made

- **05 to 08 are real clicks.** The copy was opened in Desktop in the "Build your own" state with nothing picked and
  no filter of any kind; each row was then clicked by posting the mouse messages (move, button down, button up) to
  the report view, the same path a mouse takes. The Deneb selector did the rest: the ticks, its footer, the plan tile,
  the rules line, the waterfall and the chart below all follow the clicks. Nothing in 05 to 08 comes from a filter.
  Between two renders the copy was reloaded, so every one starts from an empty plan.
- **03, 04 and 14 to 18 come from a throwaway copy** of the project with the bookmark's visibility applied (03, 04)
  or a temporary page filter for the hovered context (14 to 18: package A or C, band "10 years or more", hotel
  Toronto Pearson Airport, year 2030). The committed project has no such filters. In the report the tooltips follow
  the hovered data point, and the report setting `useScaledTooltips` scales them with the canvas (tooltip pages are
  480 px wide against a 1920 px page).
- **Build waterfall labels (verification 17).** The bars carry the column `BuildMove[Waterfall Label]`; the selector,
  the tooltips and the A waterfall keep the full Short Name. Up to about four bars the labels sit horizontally and wrap;
  from five bars on Desktop rotates them and clips at about 75 px of text, and the first label is clipped earlier
  because it runs out of the visual's left edge. The names were measured against that: "App" for the first bar (always
  Booking app, sort order 1), "Rev. mgmt", "Boston", and the widest kept name "Kingston +40". Renders 05 (three
  bars), 07 (eight) and 08 (ten) show every label in full. The axis property `maxMarginFactor` was tried at 40 and
  made it worse, so the axis stays at its default. Known and accepted: with eight or more bars the first data label
  ("+$3,4M") touches its bar; that is Power BI's automatic label placement in a 160 px high visual.
- **The hover signifier (12 Nov, evening).** Power BI gives no cursor change over a visual with a report-page tooltip,
  so the page says it: `Info Badge SVG`, a 16 px Tangerine ring-i drawn without text (the same under Publish to Web and
  on a Mac), at the top right of every visual that opens a page tooltip and nowhere else; under a chip it sits below
  the chip, so the chip keeps the hover. The hint in the footer row (`Info Hint SVG`, "hover for more", 16 px) names it
  once per page. The Definitions chip is the same pill as F1 to F4; its alt text carries the glossary in one breath for
  keyboard and screen-reader users (hover itself is not keyboard-reachable). Measured: a 152 px chip clipped "The
  fading welcome", so the five chips are 160 px and the source line 864 px.
- **"Totaal"** under the last bar (04 to 06) is Desktop's nl-NL label for the waterfall's total; in an en-US browser
  it reads "Total" (M3, accepted).

## Not rendered here: what only the published report can show

- **Publish-to-Web set, 20 to 28** (`20_p2w-p1-1366.png` to `28_p2w-mac-fonts.png`, plan 15 section 7, phase 5):
  these need the report in the Power BI service with Publish to Web on. Publishing is Björn's action (rule
  `mutation-safety.md`) and he renders this set by hand after publication. Open until then: the Deneb selector after
  a click in the browser (22), scaled tooltips at 1366 and 1920, the package tooltip on dot A high in the cloud, the
  background at 45 % and 100 % zoom, en-US notation in the browser, one nl-NL session for the known mix (26), fonts
  on a Mac, and the keyboard round.
- **Keyboard round in the service** (plan 15, phase 5 step 7): not run. Known from Desktop (BUILD_LOG, 9 Nov): the tab
  bar and the slicers are reachable and named; the Deneb selector cannot be operated with the keyboard (known
  limitation for the submission notes).
- **A tooltip hovering in place.** The tooltip pages are rendered standalone (10 to 18); a capture of the tooltip
  floating over the hovered card, chip or dot on page 1 or 2 is not in this set. Desktop evidence that the bindings
  hold: the chips and cards point at tt-f1 to tt-f4 in the PBIR, and the pages render at 480 px.
- **Page 1 and 2 in a browser at 1366 px** (the jury's likely laptop width): a Desktop capture cannot show the
  service's scaling; see 20 and 21 of the Publish-to-Web set.

## Notation (M3)

Accepted as decided in plan 15, phase 4: native labels follow the viewer's locale (here nl-NL Desktop: "+6,8",
"91,9%", "$84,99", "Totaal"), text measures and SVGs are en-US. Under an en-US browser everything shows points; the
nl-NL screenshot for the submission notes is item 26 of the Publish-to-Web set.
