Build step 7 of doc 23: the hero table and the capital plan of Recommended against the comp (14 Nov 2026)
Desktop 2.159, Windows culture nl-NL, throwaway copy of the project (never the project itself).

01-rec-expected-stitched-page-pixels.png  Page 2, Recommended, Expected case, rendered by Power BI Desktop: stitched from
                                          16 tile captures and scaled to 1920 x 1080 (tools/desktop_shots/tiles). The
                                          tile pages draw the Night header zone as a plain rectangle; the night-glow
                                          artwork and the hanger are not on them.
02-rec-low-stitched-page-pixels.png       The same in the Low case (no move passes both tests; Low is the blue line).
03-rec-high-stitched-page-pixels.png      The same in the High case ("+$0.03M", three moves pass).
04-rec-expected-overlay-on-comp.png       Render 01 over the comp: comp ink red, render ink cyan; where they agree the
                                          ink is dark.
05-comp-rec-expected.png                  The comp (rebuild-comp-v10.html#rec) at page pixels, Expected.
06-comp-rec-low.png, 07-comp-rec-high.png The comp in Low and High (a scratch copy that reads ?scen=).

Seams between tiles (page x 480, 960, 1440; y 270, 540, 810) can show as a hairline or a 1 to 2 px step in a table row
or a bar; they are not in the report. Measures of the table, the bar and the chart come from scratch pages that show
them whole (tools/desktop_shots/step7).

Render minus comp, in all three cases: every text row of the hero card and the capital plan within 2 px (the gate rule
up to 2.3), the same line wraps as the comp, bars and plan bar within 1 px. Outside 2 px, all listed in doc 23 (log of
step 7, deviations):
  - the chart's end labels stand above or under their line ends, not right of them (a line chart has no such position);
  - the chart shows two ticks (+$20M, $0M) where the comp shows four; tick and year labels sit 2 px higher;
  - the names of the zero line and the gate line are semibold;
  - the hero's header rule and its two reference lines are 4.5 px lower, so that text and bars are on the comp;
  - the hero table is 8 px wider (step 2): its NPV values end 6 px further right.
