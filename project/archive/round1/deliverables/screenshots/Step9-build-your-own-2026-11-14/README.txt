Build step 9 of doc 23: the Build-your-own state against the comp (14 Nov 2026)
Desktop 2.159, Windows culture nl-NL, throwaway copy of the project (never the project itself).

Each state is a pair: the render and the comp at the same view (rebuild-comp-v10.html#build with the scenario and the
picked moves in the query string, tools/desktop_shots/step9/comp_shots.py).

01-build-low-...           Page 2, Build your own, Low case, package A picked (the state as it opens): rendered by Power BI
02-build-expected-...      Desktop, stitched from four strip captures of 480 x 1080 and scaled to 1920 x 1080
03-build-high-...          (tools/desktop_shots/tiles, mk_tiles.py --rows 1 --picked). The strip pages draw the Night header
                           zone as a plain rectangle; the night-glow artwork and the hanger are not on them. A slicer only
                           reaches its own page: the strips that hold the selector carry its selection, the others get the
                           same moves as a page filter.
04-build-nothing-picked    Expected, nothing picked: "Nothing picked yet", the rules sentence once, no numbers, no bars, no
                           plan dot; the chart shows A alone.
05-build-over-budget       Expected, Energy + Refresh + Boston ($69.3M): the alarm band, the Tangerine line. The plan lies
                           right of the proof chart's axis ($62M), so Power BI draws no dot there (the comp draws it outside
                           the chart, over the panel, and marks it red itself).
06-build-broken-rule-...   Expected, Kiosks + Breakfast + Revenue management: "the kiosks need the booking app" in Burnt
                           Tangerine; the plan dot in Night with its name above it.
07-real-page-after-space-on-breakfast-panel.png
                           The real page 2 of the copy (not a strip): the panel after Space on the tile "Breakfast upgrade"
                           (focus set through UI Automation, the key posted to the report). Four moves; title, numbers, range,
                           rules, bars and footer follow; the table keeps its ten rows. A full-page capture in the narrow
                           session window (0.52 px per page px): proof of the wiring, not a pixel reference.
08-real-page-after-reload-panel.png
                           The same panel after `powerbi-desktop reload`: the saved selection (package A) is back.
09-your-plan-six-moves-ten-moves-comp-six.png
                           The your-plan tile with six moves (left), ten moves (middle) and the comp with six (right): from
                           six moves on the rows share the plot; from eight on Power BI scrolls the bars.
10-build-over-budget-inside-the-chart-...
                           Expected, Refresh + Boston + Toronto ($60.1M, over the budget by $0.1M and inside the axis): the
                           plan dot in Tangerine, its name in Burnt Tangerine. No comp pair.
summary-render-minus-comp.txt
                           Per view and slot: the text rows in the render and in the comp, and the largest difference in y,
                           left edge and right edge (tools/desktop_shots/step9/summary.py). Outside 2 px: the header words of
                           tbl_moves (9.2 px high, a native header is taller than its rows) and the "A year by 2032" column
                           (3 px right, wider columns). A strip render moves by about 3 px for 1 px of a visual's rect
                           (Desktop snaps to device pixels at that zoom): trust a difference under 2 px no further than that.
