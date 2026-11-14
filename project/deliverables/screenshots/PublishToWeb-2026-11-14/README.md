# Publish to Web gate · the published report, 14 Nov 2026 (build step 12)

The entry as a judge gets it: the Publish to Web link of the report "Goodnight Inn", fourth publish
(14 Nov 2026, 20:45 UTC), opened signed out in headless Edge with a fresh profile. Captures 20 to 25 and 32, 33, 35
are the report page (1920 x 1080); the others are the whole browser window with the service's bar.
The run that made them: `project/tools/desktop_shots/step12/gate.py` (its summary: [gate-summary.txt](gate-summary.txt)).
The log of the step, with the four publishes and what each one showed: doc 23, "Step 12".

| File | What it shows |
|---|---|
| [20_p1-brand-review](20_p1-brand-review.png) | Page 1, The Brand Review |
| [21_p2-recommended-expected](21_p2-recommended-expected.png) | Page 2 as it opens through the Next button: Recommended, Expected case |
| [22_p2-recommended-low](22_p2-recommended-low.png) | Recommended after a click on the scenario pill Low |
| [23_p2-recommended-high](23_p2-recommended-high.png) | Recommended after a click on High |
| [24_p2-what-waits](24_p2-what-waits.png) | What waits, and why, through its tab |
| [25_p2-build-your-own](25_p2-build-your-own.png) | Build your own, through its tab (package A is the saved selection) |
| [26_tooltip-f3-band](26_tooltip-f3-band.png) | The mouse on F3's oldest band: `tt-f3-band` |
| [27_tooltip-f4-toronto](27_tooltip-f4-toronto.png) | The mouse on Toronto's dot: `tt-f4-hotel` (blind on the first publish) |
| [28_tooltip-glossary](28_tooltip-glossary.png) | The mouse on the Definitions chip: `tt-glossary` |
| [29_tooltip-package-a](29_tooltip-package-a.png) | The mouse on A's disc: `tt-package` |
| [30_tooltip-year](30_tooltip-year.png) | The mouse on the plan chart: `tt-year` |
| [31_p2-recommended-1366px](31_p2-recommended-1366px.png) | Recommended in a 1366 x 768 window |
| [32_p1-folio-row-clicked](32_p1-folio-row-clicked.png) | Page 1 after a click on a row of the folio table: only that table marks the row; the years of the chart above it stay readable |
| [33_p2-ledger-row-clicked](33_p2-ledger-row-clicked.png) | Recommended after a click on a row of the ledger: nothing else changes, the line above the ledger stays whole |
| [34_p2-what-waits-by-tap-1366px](34_p2-what-waits-by-tap-1366px.png) | What waits reached by taps only (touch emulation, 1366 px) |
| [35_p1-dutch-browser](35_p1-dutch-browser.png) | Page 1 in an nl-NL browser: pixel for pixel the English capture |

## What the gate checked, and the result

| Check | Result |
|---|---|
| The link shows the right report | "Goodnight Inn", seven pages (two visible, five tooltip pages) |
| SVG cells in the hero table, the A chip, the header artwork | render |
| Tooltips | all five tooltip pages open, at 1920 and at 1366 px, and scale with the page |
| Buttons, tabs, scenario pills, selector tiles | work by click and by tap, also from the middle of a tab at 1366 px |
| The mouse reaches every live visual (`hit_test.js`) | clear at 1920 and 1366 px: 54 + 6 + 461 + 461 marks |
| A click on a mark or a row | changes nothing outside the clicked visual |
| The band of a clicked visual | the line above it is unchanged in nine places |
| nl-NL and de-DE browser (R-G1) | every page and tooltip capture equal to the English one; no decimal comma, no Dutch or German word of the report's own |
| Tab key | after Ctrl+Enter: logo, eyebrow, headline, subtitle, the four KPIs, F1: the reading order |
| Visual headers against the hover tags | nothing meets |

## Known, and left as it is

- While the mouse rests on a button, Power BI shows its own bubble "Click here to follow" in the browser's language;
  at 1366 px it hangs over the scenario pills after a click on a tab until the mouse moves (doc 23, open question 11:
  Bjorn, leave it). The mouse test at 1366 px reports the pills as partly covered in What waits and Build for that reason.
- A tap on a dot opens no tooltip in the touch emulation; on a touch screen Power BI opens a tooltip on press and
  hold. To be tried once on a phone (Bjorn).
- The clicked visual marks its own selection (Power BI's), and its two header icons can lie under the text card above it.
