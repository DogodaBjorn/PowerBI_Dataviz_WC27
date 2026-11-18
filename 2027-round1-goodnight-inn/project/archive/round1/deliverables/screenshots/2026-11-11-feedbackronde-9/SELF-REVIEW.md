# Self-review, feedback round 9 (11 November 2026: V9, the final build)

Rendered in Power BI Desktop 2.159 through the WebView2 DevTools port (`project/tools/desktop_shots/cdp.mjs`), the page
clipped at 1920 x 1080, one viewport nudge per shot; Desktop restarted from disk on `GoodnightInn-opzet.pbip` for every build.
The shots of this round are the complete set `project/deliverables/screenshots/screenshots-v8/` (28 files, the v6/v7 numbering
plus the year tooltip and the Desktop windows at 45 %).

## What Björn asked (11 Nov, after his own Desktop save)

1. Port his Desktop changes: the scene visual deleted on P1 and P2 (the Fit background works for him), the header rows higher.
2. A review with the taste skill, UI/UX Pro and a "hallmark" skill: AI tells, placement and white space, declutter.
3. Orange tooltip scenes with the faded door card in orange, layout unchanged, so tooltip and page differ by colour.
4. Every default tooltip off, or a designed tooltip page where it adds to the report.
   His two answers: new pages only where valuable; the eyebrow as a hotel pun with the page name as tagline.

## What was built

- **Port.** `SCENE_VISUAL_TOOLTIP`: no `z_canvas` on the report pages, kept on the tooltip pages. Header on both pages: logo y 16,
  eyebrow and masthead y 24, headline y 64, subtitle y 112, P2 chips y 56; the first card row stays at 168. `report.json` carries
  `useEnhancedTooltips: false`. Desktop's other rewriting (z/tab renumbering, schema 2.14.0, the build state with Low) discarded.
- **Review findings applied** (design-taste-frontend section 9, ui-ux-pro-max, dataviz-canon, dashboard-audit, humanizer; no
  "hallmark" skill exists on this machine): section numbers out of the eyebrows ("THE WAKE-UP CALL · THE BRAND REVIEW", "ROOM TO
  INVEST · THE INVESTMENT STRATEGY"); the middle dot rationed to one per line (P2 subtitle, band and hotel headers, brand lines,
  weakest scores, room nights, KPI sublines, the range bar's keyboard twin); F1, F2, F3 and the recommendation note as plain
  sentences; "page-1 finding" became "a finding on The Brand Review page"; the folio table 112 px; the reading guide two lines
  and the scatter 24 px taller; the chip tooltip title 72 px; the F4 chip tooltip as horizontal bars with full names (200 px,
  page 424); categorical year axes on the small F1/F2 charts.
- **Orange scenes.** `brand_canvas_v3.tooltip(palette="orange")`: band Burnt Tangerine darkening to the right, Tangerine light,
  hairline and faded door card (`hanger_mask` at tooltip scale, 8 %) in signal tint and Tangerine; kicker in `TT_KICKER`
  (#FCE6DB), title white. Waiver recorded in `brand.yaml` (`depth.tooltip_orange`) and `status.yaml`.
- **Tooltips.** `finish()` turns Power BI's tooltip off on every visual without a page binding (the keyboard cloud layer excepted:
  its Tooltips well is the package card's text twin). New `tt-year` (560 x 376) on the three cumulative charts: the hovered
  year, A in Low/Expected/High, then A, B, C and "your plan" in the case in view ("none yet" before a pick). 14 measures (452).

## Against the ask (every item looked at in the pixels)

| Item | Shot (screenshots-v8) | Verdict |
|---|---|---|
| Header as Björn moved it, both pages alike | 01, 10 | Brand row at y 24, headline 64, subtitle 112; the chips 8 px under the masthead. |
| Scene on the report pages: background only | 00, 09 (Desktop at 45 %) | The banner reaches the strip above the page; horizon 64 px under the KPI card (the Desktop drift Björn accepted). |
| Eyebrow pun plus page name | 01, 10 | "THE WAKE-UP CALL · THE BRAND REVIEW" in eyebrow blue and muted white; one middle dot in the line. |
| One middle dot per line | 02, 03, 11, 12 | Band and hotel headers, brand lines, scores, room nights and the Low/High subtitles use commas and full stops. |
| Notes as sentences | 01, 21, 22, 23 | F1, F2 (with "Our reading:"), F3 (three sentences) and the recommendation note. |
| Folio table without a scrollbar | 01 | Header and three rows in 112 px. |
| Orange tooltips, legible | 02, 03, 14 to 17, 21 to 24 | Burnt Tangerine band with the Tangerine light and the faded door card; kicker in signal tint, title white; a11y_check 0. |
| F4 chip tooltip: seven full names | 24 | Horizontal bars, Toronto Pearson Airport to Orlando Airport, values at the end. |
| F1/F2 small charts: every year | 21, 22 | 2021 to 2025 labelled. |
| Chip tooltip title on two lines | 24 | "The airports are the fullest at 82.0%, and 5 of the 7 fullest hotels are airports" complete. |
| Year tooltip on the three cumulative charts | 18, 31, 42 | 2030 on the recommendation (A −$0.2M Expected), 2029 on Considered (B −$5.1M, C −$35.5M), 2031 on Build your own (your plan +$3.3M = A). |
| Default tooltips off | 04 (KPI hover), 19 of the check set (waterfall hover) | Nothing appears on hover; only Desktop's visual header shows. |
| P2 states and scenarios on the new rhythm | 11, 12, 13, 30, 40, 41, 43, 44 | Low, High, zoom, Considered, Build your own (empty, A rebuilt, over budget), back to Recommended. |
| Gates | static | validate_tmdl 34 files 0 errors, schema_check 193 files 0 failing, a11y_check 0 failures, 0 notes. |

## Decisions made while building

- The empty build waterfall keeps its $0 total bar: a visual-level filter on the picked count cannot blank a waterfall (Power BI
  draws the total whatever the row filter says, render 11 Nov). The card's title "Nothing picked yet" carries the state.
- The three equal F cards on P1 stay (three findings of equal weight; F4 breaks the rhythm as a full-width band). The taste
  skill's ban targets landing pages.
- "Totaal" on the waterfalls is Desktop's nl-NL; Publish to Web renders the viewer's locale and the label cannot be renamed.
- The year tooltip's first label reads "A, recommended" (the longer "A, our recommendation" truncated at 18 pt in a 124 px column).
- The F4 chip tooltip grew to 424 px for seven 24 px bars (160 px scrolled the seventh off); the page height follows the card.

## Known limitations

- Desktop-only: the scene on the report pages sits a few pixels high (the Fit background in Desktop's taller display area);
  the Service aligns exactly. Desktop also shows the slicer's selection frame after a click (edit mode).
- The round-5 to round-8 limitations stand (Deneb selector keyboard, hover-only tooltips with text twins, the moves card sized
  for 8 moves, nl-NL figures in Desktop).

## Addendum (11 Nov, evening, Björn's second look): the flashy orange, and the scene pixel-exact again

"It has become the dark orange, not the flashy one" and "no overlay of the top visuals on the banner, and the text is too low."
The band is now the flashy Tangerine (#E86C36 to #E6662F, a light-orange glow, the door card and hairline in the signal tint).
White text on it is 3.4:1, under the 12 pt floor, so the kicker and the title are Night (4.7:1 on the band's darkest pixel; the
tooltip shows two Night lines on orange, the white cards under it unchanged). The second remark was Desktop's Fit drift at his
zoom: the scene is again the lowest visual on every page (`SCENE_VISUAL`), so the cards hang 64 px into the banner in every host;
the Fit background only fills the strip Desktop paints above the page, and the two coincide on the page. The header rows take
his own Desktop positions (logo 12, eyebrow and masthead 20, headline 60, subtitle 108, chips 48; `pbir_lib.visual` now accepts a
4 px grid). The whole v8 set was recaptured on this build (28 shots): shots 00 and 09 show the overlap in Desktop at 45 %;
02, 03, 14 to 18, 21 to 24, 31 and 42 the orange banners with Night text. Gates: schema_check 195 files 0 failing, a11y_check
0 failures.
