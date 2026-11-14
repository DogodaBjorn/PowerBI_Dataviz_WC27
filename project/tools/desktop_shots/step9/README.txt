Build step 9 of doc 23 (14 Nov 2026): rendering a state of page 2 with a selection, and measuring it against the comp

Everything here works in the THROWAWAY copy (never the project; doc 23 rule 6).

  round.py copy <copy dir>                              a fresh throwaway copy (tools/desktop_shots/throwaway_copy.py)
  round.py view <copy dir> <state> <scenario> [picked]  the generator's report in that state into the copy, cut into four
                                                        strips (tiles/mk_tiles.py --rows 1 --picked)
  round.py shoot <pid> <out dir> [name]                 reload, capture, stitch
  comp_shots.py <out dir> [view ...]                    the comp at page pixels per view: scenario and picked moves from the
                                                        query string of a scratch copy of the comp (headless Edge)
  marks.py <render> <comp> x,y,w,h hex[,tol] ...        coloured marks of a rectangle in both images: bars, boxes, the dot
  summary.py <renders dir> <comp dir> view ...          every Build slot of every view, render minus comp, one line each

One session, start to end:
  python round.py copy <copy>; python round.py view <copy> build Expected
  set PBI_DESKTOP_PATH to PBIDesktop.exe; powerbi-desktop open <copy>\THROWAWAY.pbip; wait 30 s
  powershell -File project\tools\refresh_desktop_model.ps1          (once per window; it prints the AS port)
  python round.py shoot <pid> <out>\f_build_Expected build_Expected
  python comp_shots.py <out>\comp; python summary.py <out> <out>\comp build_Expected
  a measure changed: sketch_model.py, then sync_measures_to_desktop.ps1 -Port <port>; a table changed: copy again, reopen
  a real toggle on the real page: spikes_step2\s3_keys.ps1 -ProcId <pid> -Do space -Tile "Breakfast upgrade"
      -Page "The Investment Strategy" (run it twice: the first run only opens the page tab), then cap.mjs on the page
  end: close the copy's window without saving (Stop-Process on the copy's pid is accepted for the throwaway only)

What the strips cannot tell (found in step 9). At this zoom Desktop snaps a visual to its device pixels: 1 px of a visual's
rect moved its marks by 0 or by about 3.3 px in the stitched render. To settle an edge, render at two rects one px apart and
take the position both readings allow (reading = true position within 1.6 px). The seam at page x 1440 runs through the
your-plan tile; text rows there measured as elsewhere.
