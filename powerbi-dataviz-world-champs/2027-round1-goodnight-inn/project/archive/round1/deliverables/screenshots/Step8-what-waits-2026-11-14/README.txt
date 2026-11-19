Build step 8 of doc 23: the What-waits state against the comp (14 Nov 2026)
Desktop 2.159, Windows culture nl-NL, throwaway copy of the project (never the project itself).

01-waits-expected-stitched-page-pixels.png  Page 2, What waits, and why, Expected case, rendered by Power BI Desktop:
                                            stitched from four strip captures of 480 x 1080 and scaled to 1920 x 1080
                                            (tools/desktop_shots/tiles, mk_tiles.py --rows 1). The strip pages draw the
                                            Night header zone as a plain rectangle; the night-glow artwork and the hanger
                                            are not on them.
02-waits-low-stitched-page-pixels.png       The same in the Low case (no package pays back; the axis runs -$50M to +$10M).
03-waits-high-stitched-page-pixels.png      The same in the High case (57 packages pay back; Tranche 3 reads "but does not
                                            pay back by 2032"; the table ends 5 px above its slot's bottom edge).
04-waits-expected-overlay-on-comp.png       Render 01 over the comp: comp ink red, render ink cyan; where they agree the
                                            ink is dark.
05-comp-waits-expected.png                  The comp (rebuild-comp-v10.html#alts) at page pixels, Expected.
06-comp-waits-low.png, 07-comp-waits-high.png  The comp in Low and High (a scratch copy that reads ?scen=).

Seams between strips (page x 480, 960, 1440) can show as a hairline or a 1 to 2 px step in a table row or a line; they
are not in the report. There is no horizontal seam any more: every y in these renders is measured within one strip.

Render minus comp, in all three cases: every text row of the proof card, the panel and the table within 2 px, and the
same line wraps as the comp in all fifteen cells; the table's rules within 0.5 px; the scatter's band, zero line and
gridlines within 1.3 px; the comparison chart's gridlines, zero line and line ends within 1 px in Expected and High.
Outside 2 px, all listed in doc 23 (log of step 8, deviations):
  - the table's header words stand 8.7 px higher (a native header is taller than the comp's; its rule is on the comp's line);
  - both charts show a tick every $20M where the comp shows one every $10M (Power BI picks the ticks);
  - the scatter's capex ticks and axis title stand 4 to 5 px higher, the comparison chart's year labels 4 px higher;
  - A's end label stands 4.6 to 6.5 px higher above its line end than the comp draws it;
  - "Cash positive above this line" starts 16 px further left, and the zero line and the gridlines run to the plot's
    right edge (the comp ends them at 2032); the value-axis labels end 12 px further left;
  - in Low only, the comparison chart's plot starts 3 px higher (no tick at the axis end), so its zero line is 3.3 px high;
  - A's disc is Deep Coffee (#1763A8) under its white letter, not the comp's Coffee Blue (#2589D8): contrast 6.2:1
    instead of 3.7:1 (open question 7 of doc 23).
