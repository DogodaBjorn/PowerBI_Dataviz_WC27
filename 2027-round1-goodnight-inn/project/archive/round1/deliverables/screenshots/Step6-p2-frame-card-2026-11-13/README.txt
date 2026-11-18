Build step 6 of doc 23: page 2 frame and the decision card against the comp (13 Nov 2026)
Desktop 2.159, Windows culture nl-NL, throwaway copy of the project (never the project itself).

01-rec-expected-stitched-page-pixels.png  Page 2, Recommended, Expected case, rendered by Power BI Desktop: stitched from
                                          16 tile captures and scaled to 1920 x 1080 (tools/desktop_shots/tiles). The
                                          tile pages draw the Night header zone as a plain rectangle, so the masthead
                                          text shows; the night-glow artwork and the hanger are not on them.
02-rec-low-stitched-page-pixels.png       The same in the Low case (NPV in Burnt Tangerine, the Low branch of line 2).
03-rec-high-stitched-page-pixels.png      The same in the High case (the longest ledger status words).
04-rec-expected-overlay-on-comp.png       Render 01 over the comp: comp ink red, render ink cyan; where they agree the
                                          ink is dark. The hero table and the capital plan are red only: step 7 builds
                                          them.
05-comp-rec-expected.png                  The comp (rebuild-comp-v10.html#rec, Expected) at page pixels.
06-rec-desktop-capture-narrow-window.png  One capture of the whole page in the 540 px wide session window (0.46 capture
                                          px per page px). Not a pixel reference: at this size Desktop lets the
                                          background image drift off the header. It shows the page whole.
07-what-waits-state-narrow-window.png     The What waits state, same kind of capture: the new frame, with the old small
                                          scatter and comparison chart in their v10 slots until step 8 rebuilds them.
08-build-state-narrow-window.png          The Build state, same: the frame, the old scatter, your-plan cards and
                                          comparison until step 9 rebuilds them.

A thin dashed line through the four numbers in 01 to 03 (page y 270) is a seam between two tiles, not in the report.

Measured with tools/desktop_shots/tiles/slotdiff.py on the stitched capture, render minus comp, in all three cases:
every text row of the frame and the decision card within 2 px in y and x (65 rows paired, the same line wraps as the
comp), except
  - the ledger: a native table sets every cell at the top of its row and its header is 34 px, not 28. The four row tops
    are on the comp's within 2 px; a cell with fewer lines than its row sits 10 to 20 px higher than the comp's centred
    cell, and the header words 8.5 px higher;
  - the three tab labels: Segoe UI Semibold as doc 21 P-2 says, 3 to 5 px wider than the comp's picture (the comp draws
    them in regular weight: its rule "#stage button {font: inherit}" outranks ".btn.lg {font-weight: 600}").
