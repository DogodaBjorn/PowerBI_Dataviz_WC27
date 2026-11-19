Review round 2, step C of doc 25 (15 Nov 2026): the plan chart's end labels as cards, its caption, the tag on the chart

The spike and the build were one round in the THROWAWAY copy (never the project; doc 23 rule 6), with the scripts of
step 9: the generator's report goes into the copy per view, so a constant changed in opzet_report.py is on screen two
minutes later.

  python ..\step9\round.py copy <copy>; python ..\step9\round.py view <copy> rec Expected
  set PBI_DESKTOP_PATH; powerbi-desktop open <copy>\THROWAWAY.pbip; wait 25 s
  the port: a second Desktop window was open (the fourth publish), so refresh_desktop_model.ps1 without -Port could
      pick the wrong model. Take the msmdsrv that started with the copy:
      (Get-NetTCPConnection -OwningProcess <msmdsrv pid> -State Listen)[0].LocalPort, then -Port <port> everywhere
  powershell -File project\tools\refresh_desktop_model.ps1 -Port <port>        (6 s; GuestComplaints came back, so a fresh copy)
  python project\tools\number_checks.py --port <port>; build_checks.py --port <port>; alt_texts.py --port <port>
  per case: python ..\step9\round.py view <copy> rec <Low|Expected|High>; python ..\step9\round.py shoot <pid> <out>\<name> rec_<case>
  python plan_measure.py <out>\<name>\rec_<case>.png          the x scale, the gridlines' reach, the label boxes
  python plan_sheet.py <sheet.png> <the three renders>        the three cases under one another
  end: Stop-Process on the copy's pid (the throwaway only; the other window stays as it is)

What the spike found.
  - With the axis ending on 2032 a line chart still draws its gridlines 9 px past the first and the last year, and
    centres the last year's label on the year. At a visual width of 940 the years stood 170.5 px apart; 943 gives the
    comp's 171 (2027 at 864.1, 2032 at 1719.7).
  - A cardVisual with an empty text measure draws nothing, so two cards can share one spot (the quiet and the
    emphasised label of a case); both are out of the tab order.
  - The label cards start 14 px right of the line's end, not the comp's 8: at 8 the first letter touched the end of
    the gridline at +$20M.
  - The caption is a text box that ends 8 px into the chart's rect: mouse_order() then still counts it as standing
    above the chart and puts it over the chart, clear of the band a clicked chart keeps in its header strip.
  - The tag stands inside the chart's rect and goes under the chart (mouse_order(), rule 1): the chart has no fill, so
    the tag shows, and the year tooltip opens over it as anywhere else in the plot.
  - In the strip render the chart stood 2 px higher than on the fourth publish (zero line at 913.2 against 915.25), the
    known snap. The labels' heights are computed from the published zero line, so here they read 2 px low; on publish 5
    they should sit on the line ends. That is one of the things to look at on publish 5.
