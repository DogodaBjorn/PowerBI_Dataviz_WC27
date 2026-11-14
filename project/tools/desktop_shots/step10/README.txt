Build step 10 of doc 23 (14 Nov 2026): tooltip renders, and the keyboard and screen-reader passes by script

Everything here works on the THROWAWAY copy (never the project; doc 23 rule 6).

  tt_pages.py <copy dir>                         the copy's report refreshed from project/pbip, plus one ordinary page
                                                 r_<view> per tooltip view: the tooltip page's visuals with the hover's
                                                 context as page filters (package A, B, C, a package of eight moves,
                                                 the year 2030, the oldest band, Gatwick, the glossary)
  crop_page.py <out dir> <capture>=<width> ...   a bridge capture cut to the page (the window is 540 px wide: Night
                                                 margin above and under the page, the Filters pane at the right)
  a11y_pass.ps1 -ProcId <pid> -Do names -Page "<page name>" -Out <dump.txt>
                                                 the accessibility tree of Desktop with the page open: every named or
                                                 focusable element, its role and its name (what a screen reader is given)
  a11y_pass.ps1 -ProcId <pid> -Do canvaswalk -Page "<page name>" -Keys "+{TAB}" -Count <n>
                                                 real key presses: Ctrl+F6 until the canvas has the focus, then the key
                                                 n times, the focused element printed after each
  spoken.py <dump.txt> [--cells]                 the page's visuals from a dump, one line each; --cells adds the rows and
                                                 cells of tables and the tiles of slicers

One round:
  python ..\throwaway_copy.py project\pbip <copy>; set PBI_DESKTOP_PATH; powerbi-desktop open <copy>\THROWAWAY.pbip
  powershell -File project\tools\refresh_desktop_model.ps1                    (once; it prints the AS port)
  python tt_pages.py <copy>; powerbi-desktop reload --pid <pid>; wait 8 s
  node ..\cap.mjs <pid> r_pkg_a_expected 3 <out>\pkg_a_expected.png; python crop_page.py <crops> <out>\pkg_a_expected.png=480
  a state of page 2: python project\tools\opzet_report.py --out <gen> --state=alts, copy <gen>\*.Report\definition and
      StaticResources over the copy's, reload, then a11y_pass.ps1 -Do names
  python project\tools\alt_texts.py --port <AS port>                          every alt text in Low, Expected and High
  end: Stop-Process on the copy's pid (accepted for the throwaway only)

What was learned (doc 23, log of step 10):
  - Tab runs from the HIGHEST tabOrder to the lowest. Ctrl+F6 puts the focus on the first stop of the page.
  - Desktop shows edit mode only: visuals that are out of the tab order take the focus too (they have no name), and
    Tab on an image or a shape falls into its header button ("Meer opties") and stays there. Walk with Shift+Tab
    ("+{TAB}") and read the list from the bottom up.
  - In edit mode Desktop marks every visual focusable, so a dump cannot tell a stop from a decorative visual; an
    element without a name is one the generator took out of the tab order.
  - The report view must be the open view ('Rapportweergave'), and the WebView's elements appear only after one
    full walk of the tree; -Do names does both.
