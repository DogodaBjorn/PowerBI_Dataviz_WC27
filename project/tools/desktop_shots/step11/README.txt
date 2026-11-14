Build step 11 of doc 23 (14 Nov 2026): the FinalV3 render set and its sheet against the comp

Everything here works on the THROWAWAY copy (never the project; doc 23 rule 6).

  slot_sheet.py <render png> <comp png> <page> [state]   every slot of the view from the slot map, render minus comp:
                                                         text rows, max dy, left and right edge; text slots within 2 px
                                                         are counted, the others listed; charts and tables apart

The round that made project/deliverables/screenshots/FinalV3 (about 25 minutes, one Desktop window):
  python ..\throwaway_copy.py project\pbip <copy>; set PBI_DESKTOP_PATH; powerbi-desktop open <copy>\THROWAWAY.pbip; wait 30 s
  powershell -File project\tools\refresh_desktop_model.ps1                 (once; prints the AS port)
  python project\tools\number_checks.py --port <port>; build_checks.py --port <port>; alt_texts.py --port <port>
  page 2, per view:  python ..\step9\round.py view <copy> <rec|alts|build> <Low|Expected|High> [picked short names | -]
                     python ..\step9\round.py shoot <pid> <out>\<name> <name>
  page 1:            python project\tools\opzet_report.py --out <gen>; copy <gen>\*.Report\definition and StaticResources
                     over the copy's; python ..\tiles\mk_tiles.py <copy>\THROWAWAY.Report --page p1-brand-review --mast 168
                     --rows 1; then round.py shoot as above
  the comp per view: the method of ..\step9\comp_shots.py (a scratch copy of the comp that reads ?scen= and ?picked=;
                     #p1, #rec, #alts, #build), cropped at (16, 94) to 1920 x 1080
  tooltips, last:    empty the copy's report folders (the strip pages must not stay behind), python ..\step10\tt_pages.py
                     <copy>, reload, node ..\cap.mjs <pid> r_<view> 3 <png> (twice), python ..\step10\crop_page.py
  end:               Stop-Process on the copy's pid (accepted for the throwaway only)

Views of the set: rec x Low, Expected, High; alts x Low, Expected, High; build with package A (the saved selection),
with six moves ("Booking app,Revenue management,Kiosks at 20 desks,Breakfast upgrade,Gatwick +40 rooms,Toronto +40
rooms"), over the budget ("Energy programme,Refresh 10 oldest,Boston new hotel") and with nothing picked ("-").

What was learned:
  - A render of a view is byte for byte repeatable across sessions when nothing changed (three Build views and all
    nine tooltip views equalled their step 9 and step 10 renders): `cmp` against the last set is a cheap regression test.
  - The first tooltip capture after a reload can come back without its visuals (66 KB instead of 179 KB) even on the
    second pass: compare file sizes with the last set and capture again.
  - A whole-page capture in the 540 px window puts the background image off the header; the header's look cannot be
    judged in this session.
