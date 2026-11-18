Build step 12 of doc 23 (14 Nov 2026): the Publish to Web gate

The published report is checked in headless Edge, signed out, with a fresh profile per run (never Bjorn's browser).

  web.mjs <url> <steps.json> [--lang nl-NL] [--w 1920] [--h 1080] [--dsf 1] [--touch]
      opens the link in the given browser locale and window, then runs the steps: ready, pshot, pmove (hover),
      pclick, ptap (one touch), key, focus, texts. Page coordinates are the report's own 1920 x 1080.
  locale_scan.py <texts.txt> ...
      reads the texts web.mjs collected for a decimal comma or a Dutch or German word (R-G1).

  gate.py <url> <out dir> [--ref <earlier out dir>] [--only hit,clicks,...]
      the whole gate in one run (sixteen browser runs, four at a time, about 6 minutes) and one summary: which report
      the link shows, the mouse at 1920 and 1366 px, what a click changes, nl and de against en, the Tab order, and
      every page capture against an earlier run. The tooltips' and the pages' look is judged by eye on the captures.
  plan.py <out dir> <run> [tag]      the step files gate.py runs (p1, p2, states, more, clicks, tips, keys, keys2, touch)
                                     keys2 (review round 2, J-AC-8 and J-AC-4): Tab through page 1 and page 2's three
                                     states, then Enter, arrows and Esc inside the hero table and the selector; gate.py
                                     prints the stops per part and how many have no spoken name (none may), the whole
                                     list goes to <out dir>\keys2_walk.txt. Tried on publish 4 on 15 Nov: 0 nameless
  hit_test.js, hit_report.py         who gets the mouse, measured in the published page (see ..\..\strip_check.py for
                                     the same question answered from the report files, before a publish)

A republish reaches the link late: Publish to Web serves a cached copy (on 14 Nov a republish of 18:13 UTC was not
on the link 15 minutes later). `meta` shows the last publish time the link serves; wait until it moves.

The publish copy (the project is never opened or saved in Desktop, doc 23 rule 6):
  python ..\throwaway_copy.py project\pbip ..\GoodnightInn-publish --name "Goodnight Inn"
  set PBI_DESKTOP_PATH; powerbi-desktop open "..\GoodnightInn-publish\Goodnight Inn.pbip"; wait 30 s
  powershell -File project\tools\refresh_desktop_model.ps1          (data in about 6 s)
  Bjorn: Publish (Desktop asks to save: yes, it is the copy), then in the service File > Embed report >
  Publish to web (public). After a fix in the generators: write the copy again, open, refresh, Bjorn publishes
  over the same report (the link stays).

Start every run with {"op":"ready"},{"op":"meta"}: meta prints the report's name in the service, its last publish
time and its pages. The first link of 14 Nov was the old report "GoodnightInn-opzet" (13 Nov), not the new one.
In a 1920 x 1180 window the service gives .displayArea 1920 x 1100 at y 10 (the page plus a 20 px strip).

What was learned:
  - Edge's --lang and --accept-lang leave navigator.languages on the Windows list (a de-DE run answered "nl").
    Emulation.setUserAgentOverride with acceptLanguage sets the header and navigator.language(s);
    Emulation.setLocaleOverride sets Intl. web.mjs does both and prints navigator.language at "open" and "ready".
