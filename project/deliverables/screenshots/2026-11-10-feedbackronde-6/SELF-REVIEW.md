# Self-review, feedback round 6 (10 November 2026: footer, the package tooltip as an evidence card, F1–F4 chips, F3/F4 hover detail)

Rendered in Power BI Desktop 2.159 through the WebView2 DevTools port (`project/tools/desktop_shots/cdp.mjs`), page
clipped at 1920 x 1080, one viewport nudge per shot (the detached-session rule from round 5); blank captures were
retried, never kept. Desktop prints chart labels and card figures in nl-NL ("+6,8", "$80,47"); Publish to Web shows the
viewer's locale. Desktop was restarted this round (it closed itself during a reload), so a fresh AS port and a fresh
DevTools session; the model was re-synced from the TMDL after every generator run.

## Against the plan (every item looked at in the pixels)

| Item | Shot | Verdict |
|---|---|---|
| Footer without the scoping line | 01, 20 | OK on both pages: source plus the two real caveats (P1), source plus parameters and rounding (P2). |
| Verdict over the three cases | 11, 12, 13 | "Does not pay back by 2032, not even in the High case" on C and the cloud dot; "Pays back by 2032 except in Low; cash positive from 2031" on A. One line, bold, Burnt Tangerine when the case in view does not pay back. |
| Range bar on a shared axis | 11, 12, 13 | One fixed axis (−$50M to +$15M, rounded to $5M) for every package; the cloud as a grey histogram strip; A (Deep Coffee), B and C (Night) ticks with their letters; the hovered band with its Expected dot; the break-even line named top left; Low and High numbers under the band ends. The dot sits where the headline says. |
| Moves list with waterfall bars and a total | 11, 12, 13 | Positives first, the sinker last; capex and NPV two decimals; bars from running start to running end on one scale per package, Coffee Blue up, Tangerine down, the total from zero in Night. A: 3.37 + 0.51 − 0.60 = 3.28; C: 3.37 + 0.50 − 27.31 = −23.44; cloud: −3.74 − 12.18 − 27.31 = −43.23. The numbers equal the headline NPV. |
| Fixed move grid instead of "Not in it" | 11, 12, 13 | Ten chips in the selector's order, two columns; filled Night = in the package. A, C and the cloud dot compare by shape at a glance. |
| Tooltip fits on screen | 13 | 560 x 568; above A (near the top of the scatter) Power BI places it fully on the canvas. Desktop's tooltip container keeps square corners (known since round 5). |
| F1–F4 chips in the night banner | 20 | Four pills top right over the faded brand mark: code in the eyebrow blue, name in white, hairline border. Headline and subtitle shortened to 1176 px; nothing overlaps. |
| Chip tooltips | 21, 22, 23, 24 | Each opens the finding's page: night band "F# · name", the headline (two lines where needed), the same chart P1 draws (same builder: query, filters, colours, sort), the note (F4: the three occupancy figures above the bars). A card visual takes a report-page tooltip in Desktop: the spike passed, no fallback needed. |
| F3 band hover | 25 | "Last renovated 5 years or less ago · 14 hotels · 1,835 rooms"; NPS, occupancy, RevPAR 2025 with the brand's figures under them; NPS 2021–2025 band against brand; "Weakest guest scores 2025: amenities 7.3 · room comfort 7.4 (of 10)". |
| F4 hotel hover | 26 | "Toronto Pearson Airport · airport · 150 rooms"; occupancy, ADR, RevPAR 2025 with the brand's under them; occupancy by month 2025 (axis 50–100 %) against the brand; "Room nights 2025: leisure 39% · business travel 24% · family 22% · other 15%". |
| 12 pt / 16 px floor, alt text, reading order | static | `a11y_check.py` 0 failures over 191 files; new rule: every `font-size` inside an SVG-in-DAX measure is held to 16 px. |

## Decisions made while building (recorded, not in the plan)

- The moves table is one SVG, not a `tableEx` with an image column: the table squared its image cells to the column
  width (140 x 20 became 75 x 11 inside a 76 px tall row) and ignored the hidden sort key.
- `rows` and `top` are reserved words in DAX; variables renamed (`moveRows`, `top3`). A measure with a syntax error
  breaks every query on the model ("SYNTAXERROR"), which is how both were found.
- The SVG colour helper first shadowed the `PCT` format-string constant and gave two line measures a Python lambda as
  their format string; renamed to `HX`.
- Card width 560 (not 480): five columns of the moves list plus a bar need it, and the finding pages share the width.

## Known limitations

- Report-page tooltips are hover-only and not read by screen readers (Microsoft Learn): every SVG fact has a text twin
  (the verdict, `TT Range (text)` and `TT Moves (text)` in the keyboard layer's tooltip well, the chips' alt text is the
  finding's headline, the F3/F4 charts' alt texts say what a hover adds).
- Tooltip skin, final (Björn, 11 Nov, after two rejected attempts): a tooltip is a dashboard CARD, not a miniature of the page. White page (the host's strip above the page is painted in the page colour, so white merges), a kicker row in the finding's colours (the dashboard's own `kicker()`), the title, the content; the hanger chip is the only brand mark on the package card. No banner, no lockup, no night band, no inset frame. Re-rendered: 11, 13, 23, 25, 26.
- The page background (Björn's screenshot, 11 Nov): Desktop paints the page background over a display area 20 px taller than the page, so the Oat colour showed as a bar above the banner. The report pages' background is now the night scene itself as an image (`canvas-night-page.jpg`, the same scene with 20 px of banner added above, anchored top-left at actual size), so the banner starts at the very top of what Desktop shows; the on-page canvas visual stays the exact 1920 x 1080 scene, aligned with the cards, in every host. Nothing on the canvas moved.
- Chip labels at 12 pt in a 160 px pill: "The fading welcome" fits with 4 px to spare; a longer name would need a wider pill.
- The round-5 limitations stand (Deneb selector keyboard, empty build waterfall total, small-scatter letters under the dots, nl-NL in Desktop).
