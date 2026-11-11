# Self-review, feedback round 7 (11 November 2026: the tooltips as the page in miniature; a leaner package tooltip)

Rendered in Power BI Desktop 2.159 through the WebView2 DevTools port (`project/tools/desktop_shots/cdp.mjs`), page
clipped at 1920 x 1080, one viewport nudge per shot (the detached-session rule from round 5). Desktop prints chart labels
and card figures in nl-NL ("+6,8", "$80,47"); Publish to Web shows the viewer's locale. Desktop was started three times
this round (Björn had it open without the DevTools port, and later closed it); every start loaded the generator's files
from disk, so what is shown is what is on disk.

## What Björn asked (11 Nov, on the round-6 package tooltip)

1. A tooltip-specific design: the midnight banner with a title in the page's own design language, then the visuals in
   cards with the page's pop-out shadow, as a miniature of the page with sensible proportions; for all tooltips.
2. The scatter's package tooltip trimmed: information overload; the highlighted squares (the move grid) are noisy.

## What was built

- **One scene per tooltip page** (`brand_canvas_v3.tooltip`): the Night-to-navy band to a horizon 24 px under the
  first card, the Coffee Blue light at the right, the hairline on the horizon, the Oat page with its soft glow below; no
  hanger (a stamp at this size). The scene sits on the page as `z_canvas` and, 20 px taller, as the page's background
  image, so the strip the tooltip host paints above the page is banner too (the round-6 page fix, applied to tooltips).
- **Banner:** the kicker at y 16 in the page's eyebrow style (ZONE_EYEBROW on Night: `F3 · THE FADING WELCOME`,
  `PACKAGE C · EXPECTED CASE`), the title at y 40 in white Segoe UI Semibold (14 pt, two lines for the finding headlines).
- **Cards:** white, radius 12, the page's card shadow, 16 px margins, 16 px padding, hanging 24 px into the banner like
  the page's cards hang 64 px into its night zone. Layout v7 in `opzet-layout.json`; the 8 px grid, the card bounds and
  the page height (last card + 16) are asserted by the layout script.
- **Package tooltip, leaner (560 x 536):** banner (kicker, title); card 1 = NPV, capex, the verdict over the three cases,
  the range bar on the shared axis (Low-High band, Expected dot, break-even line, A/B/C ticks, Low and High numbers);
  card 2 = "In this package: n moves" and the list Move | Capex | NPV with a totals row. Gone: the hanger chip, the case
  tag (now in the kicker), the histogram strip, the Answers column, the waterfall bars, the move grid and its caption.
  Model: `TT Kicker (text)` new; `TT Chip`, `TT Case (text)`, `TT Mix (text)`, `TT Move Grid (svg)`, `TT Grid Label (text)`
  removed (438 measures).
- **Finding pages (560 x 448, F4 384):** banner, one card with the P1 chart and the note (F4: the three occupancy figures
  and the top-7 bars). **Detail pages (560 x 560):** banner with the band or hotel as title; a card with the three
  figures and the brand's figures; a card with the titled two-line chart and the closing line. The F4 month axis shows
  one letter per month (`Date[Month Letter]`, sorted by month number): at 496 px the three-letter names rotated.
- `a11y_check.py`: text outside a card on a tooltip page is checked against its own scene's pixels (the banner), as on
  the page's night zone.

## Against the ask (every item looked at in the pixels)

| Item | Shot | Verdict |
|---|---|---|
| Banner starts at the very top of the tooltip, no strip | 11, 12, 13, 23, 25, 26 | OK: the tooltip's first pixels are Night; the host's strip above the page is painted with the taller twin image. |
| Kicker and title in the page's design language | all | Kicker in the eyebrow blue, title in white Semibold, the Coffee Blue light at the right of the band, the hairline on the horizon. |
| Cards with the page's shadow, sensible proportions | all | 528 px cards on the Oat page, 16 px rhythm, the first card hanging into the banner. |
| Package tooltip trimmed | 11 (C), 12 (cloud dot), 13 (A) | Two cards: return (NPV, capex, verdict, range bar) and moves (list with total). The list adds up to the headline (C: 3.37 + 0.50 − 27.31 = −23.44; cloud: −3.74 − 12.18 − 27.31 = −43.23). No grid, no bars, no histogram. |
| Chip tooltip (F3) | 23 | Banner with kicker and headline; the chart card; the note complete on three lines (88 px). |
| F3 band hover | 25 | "5 years or less · 14 hotels · 1,835 rooms" as the title; figures, the brand line on two lines (64 px); NPS by year; weakest scores. |
| F4 hotel hover | 26 | "Toronto Pearson Airport · airport · 150 rooms"; figures, brand line; occupancy by month with J F M A M J J A S O N D; room nights complete. |
| Pages unchanged | 01, 20 | P1 and P2 as in round 6. |
| Gates | static | validate_tmdl 0, schema_check 185 files 0 failing, a11y_check 0 failures (incl. the SVG 16 px rule and the banner contrast). |

## Decisions made while building

- A cardVisual with 12 pt text needs 64 px for two lines and 88 px for three; at 56 and 72 px it truncates with an
  ellipsis instead of wrapping (seen on the brand line and the F4 footer). The layout gives those slots that room; the
  detail chart gave up 8 px for it.
- The moves card keeps room for the largest package (8 moves: header + 8 rows + total at 20 px = 200 px), so a 3-move
  package leaves the lower half of that card empty. A fixed layout cannot grow with the package; the alternative
  (smaller rows) saves little and costs legibility.
- The round-6 "apply external changes" bar in Desktop re-saved the MODEL folder (`cultures/en-US.tmdl`, `ref cultureInfo`)
  on every apply: the model was regenerated from `sketch_model.py` before this review, the report never needed it
  (its schema version stayed the generator's 2.11.0). After the second apply the bar stayed behind a native dialog, so
  Desktop was restarted from disk instead.

## Known limitations

- The F3 band tooltip (560 px tall) opens above a bar at y 505: Power BI places it against the top of the page, and in
  Desktop the top rows sit in the display strip (shot 25 shows the banner from the title down). The Service keeps the
  tooltip inside the viewport. The round-6 limit stands: tooltip pages above 568 px clipped over A.
- Report-page tooltips are hover-only and not read by screen readers: every SVG fact keeps its text twin (`TT Range
  (text)`, `TT Moves (text)`, the alt texts), the kicker is out of the tab order and the title carries the words.
- The round-5 and round-6 limitations stand (Deneb selector keyboard, empty build waterfall total, small-scatter letters
  under the dots, nl-NL in Desktop, chip labels at 12 pt in a 160 px pill).

## Addendum (11 Nov, Björn's second look): the background image is gone

"The background seems doubled, remove the overlay." A page background image at Normal scaling is drawn at actual size
while the canvas visual scales with the page, so at any zoom but 100 % (Björn's Desktop stood at 33 %) the scene showed
twice. The background image left every page (report and tooltip); the scene is the `z_canvas` visual only, the page colour
is Night, so Desktop's 20 px strip above a page and the tooltip host's strip above a tooltip show plain Night over the
banner's dark top. The complete set after this change is `project/deliverables/screenshots/screenshots-v6/` (20 shots:
both pages, the F3/F4 hovers, the three scenarios, the zoom, the package tooltip on A, B, C and a cloud dot, the four
chips, the Considered and Build-your-own states). The shots in this folder predate the change; the only visible
difference is that strip.
