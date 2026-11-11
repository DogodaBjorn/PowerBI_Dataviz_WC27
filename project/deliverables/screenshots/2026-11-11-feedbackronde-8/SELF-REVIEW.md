# Self-review, feedback round 8 (11 November 2026: the banner and the titles; the scene pixel-exact; more air)

Rendered in Power BI Desktop 2.159 through the WebView2 DevTools port (`project/tools/desktop_shots/cdp.mjs`), the page
clipped at 1920 x 1080, one viewport nudge per shot. Desktop was restarted from disk for every build (`GoodnightInn-opzet.pbip`
by name: the folder also holds the D1/D2/D3 sketches, and the first start opened D1). The shots of this round are the
complete set `project/deliverables/screenshots/screenshots-v7/` (24 files, the v6 numbering plus `00_` and `09_`).

## What Björn asked (11 Nov, on the round-7 correction)

1. "The header banner and the placement of the title and subtitle are off."
2. "Put the titles higher and place the top layer of visuals slightly over the banner blue so that it overlays, and via
   that we gain some canvas space that allows for a bit more white space everywhere."

## What was found and built

- **Why the banner was off.** A page background image with 'Fit' is fitted into the host's display area. Desktop's area
  is taller than the page, so the scene drifted up: 14 px at 100 % zoom, 38 px at 60 % (the horizon above the KPI card
  instead of 64 px under its top). The Service's area is the page itself, so there it was right; Björn reviews in Desktop.
- **The scene pixel-exact.** A visual is placed in page pixels in every host, so the scene is again the lowest visual
  (`z_canvas`, z 0, out of the tab order; `SCENE_VISUAL` in `opzet_report.py`). The page background keeps the same scene
  with Fit, for the strip Desktop paints above a page (round 6: banner there, not plain Night). With Fit the background
  scales with the page, so no second scene shows at any zoom (round 7's doubling came from 'Normal', actual size).
- **Layout v8.** Headline y 80, subtitle y 128 (24 px slot), P2's chips y 72; the first card row y 168 and the horizon
  232 (first row + 64, `brand_canvas_v3`), so the top cards hang 64 px into the banner as before. The 16 px gained go
  into air: 24 px vertical gutters on P1, the F4 card 8 px taller, the notes ending 8 px above the card edge; on P2 the
  panel and scatter content 16 px up, the scatter and the cumulative chart 16 px taller, the compare card with a 24 px
  gutter and an 8 px taller chart. Footer 1032/48. Tooltip pages unchanged (v7).

## Against the ask (every item looked at in the pixels)

| Item | Shot (screenshots-v7) | Verdict |
|---|---|---|
| Banner aligned with the cards at full size | 01, 10, 30, 40 | OK: the horizon 64 px under the KPI card's top (P1) and the two cards' top (P2); hairline on the horizon. |
| Banner aligned at Björn's zoom | 00_P1_desktop_45pct_desktop, 09_P2_desktop_45pct_desktop | OK at 45 %: the same overlap; the strip above the page shows banner, no plain Night, no second scene. |
| Titles higher | 01, 10 | Headline 8 px under the brand row, subtitle directly under it; the P2 chips 8 px under the masthead. |
| More air | 01 | 24 px between the KPI card and the F cards and between the F cards and F4; F4's chart with 16 px under it. |
| P2 states on the new rhythm | 10, 11, 12, 13, 30, 40, 41, 42, 43 | Scenario buttons, zoom, Considered, Build your own (empty, A rebuilt = $9.4M / +$3.3M, over budget by $18.65M), back to Recommended. |
| Tooltips unchanged | 02, 03, 14 to 17, 21 to 24 | The package tooltip on A, B, C and a cloud dot, the four chips, the F3 band and F4 hotel hovers as in round 7. |
| Gates | static | validate_tmdl 34 files 0 errors, schema_check 185 files 0 failing, a11y_check 0 failures, 0 notes. |

## Decisions made while building

- The horizon rule stays "first card row + 64": Björn's "slightly over the banner" is read as the existing overlap moved
  up with the cards, not a deeper one. A deeper overlap (horizon 248 with the cards at 168) is one number in
  `brand_canvas_v3.py` if he wants it.
- The gained space went to gutters and bottom padding rather than larger charts: his words were "white space".
- The Deneb selector rows toggled only after an Escape and with unsettled clicks (the round-5 recipe); the v6 capture
  script's plain clicks selected the visual instead. Documented in the build log.

## Known limitations

- Desktop-only: the strip above the page shows the background's top (Fit, centred), which is the banner's near-uniform
  top; at other zooms it is a different slice of that top. The page itself is exact everywhere.
- The round-5 to round-7 limitations stand (Deneb selector keyboard, hover-only tooltips with text twins, the moves card
  sized for 8 moves, nl-NL figures in Desktop).
