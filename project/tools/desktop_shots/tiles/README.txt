Tile render: a page-pixel render of a report page when the Desktop window is too narrow for one
(build step 5 of doc 23, 13 Nov 2026)

Why. The Desktop Bridge captures the report canvas as it is laid out in the window, at a scale of at most 3. In a
narrow session window (540 px wide on 13 Nov) a 1920 px page comes out at 0.46 capture px per page px: too coarse to
check 2 px, and text inside visuals reads several px off. A 480 x 270 page in the same window comes out at 1.84
capture px per page px. So the page is cut into 16 tile pages in the THROWAWAY copy, each holding the visuals that
touch its region, shifted so the region's corner is the page origin (Desktop draws visuals at negative positions and
clips them at the page edge). The 16 captures are stitched and scaled back to 1920 x 1080.

Steps (all in the throwaway copy, never in project/pbip; doc 23 rule 6):
  1. python throwaway_copy.py project/pbip <copy dir>; open the copy; refresh_desktop_model.ps1
  2. python tiles/mk_tiles.py <copy dir>/THROWAWAY.Report        # writes pages t_0_0 .. t_3_3 and t_cal (P1; change
                                                                   # the source page in the script for another page)
  3. powerbi-desktop reload --pid <pid>; wait a few seconds (a new page is unknown to the bridge right after a reload)
  4. node cap.mjs <pid> t_cal 3 t_cal.png; find the Tangerine rectangle in it and write "x0 x1 y0 y1" (capture px,
     x1 and y1 exclusive) to t_cal.txt: that is where every tile page sits in a capture
  5. node cap.mjs <pid> t_<r>_<c> 3 <dir>/t_<r>_<c>.png for the 16 tiles
  6. python tiles/stitch.py <dir> t_cal.txt page.png             # page.png (1.84x) and page_1920.png (page pixels)
  7. python tiles/overlay.py page_1920.png <comp page png> ov    # comp ink red, render ink cyan, agreement dark
     python tiles/bands.py page_1920.png <comp page png> name,x,y,w,h ...   # text rows of both, y centre in page px

The comp at page pixels: headless Edge with --window-size=1952,1300 on rebuild-comp-v10.html#p1 puts the page at
(16, 94) at scale 1; crop 1920 x 1080 from there.

Build step 6 (page 2): mk_tiles.py takes --page <folder>, --scenario <Low|Expected|High> (the tile with sl_scenario gets
the slicer set to that case, the other tiles get it as a page filter; the page's own filters are copied to every tile)
and --mast 168 (draws the Night header zone as a rectangle under the tile's visuals, so light text on it can be read and
measured). slotdiff.py <page.png> <comp page png> name,x,y,w,h ... prints the text rows and ink edges of a page
rectangle in both images and their differences, on any background; give it the stitched capture at its own resolution.
A card's line can read 1.5 px off in a tile depending on where the card's top falls on the capture's pixel grid: a 1 px
move of a card moved its text 3.3 px. Trust a difference under 2 px no further than that.
The comp in a scenario: a scratch copy of the comp with ST.scen read from ?scen=Low, headless Edge as below; Edge
returns before the PNG is written, wait for the file.

Limits. The page background image is not on the tile pages (they are Oat, or a plain Night rectangle with --mast), so
the night-glow artwork does not show; check the header's look in a normal capture. A full-page capture in a narrow window is not a pixel reference: Desktop
scaled x and y differently there (0.4594 and 0.4565) and the background image drifted.
