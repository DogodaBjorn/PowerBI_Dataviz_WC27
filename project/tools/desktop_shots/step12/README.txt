Build step 12 of doc 23 (14 Nov 2026): the Publish to Web gate

The published report is checked in headless Edge, signed out, with a fresh profile per run (never Bjorn's browser).

  web.mjs <url> <steps.json> [--lang nl-NL] [--w 1920] [--h 1080] [--dsf 1] [--touch]
      opens the link in the given browser locale and window, then runs the steps: ready, pshot, pmove (hover),
      pclick, ptap (one touch), key, focus, texts. Page coordinates are the report's own 1920 x 1080.
  locale_scan.py <texts.txt> ...
      reads the texts web.mjs collected for a decimal comma or a Dutch or German word (R-G1).

The publish copy (the project is never opened or saved in Desktop, doc 23 rule 6):
  python ..\throwaway_copy.py project\pbip ..\GoodnightInn-publish --name "Goodnight Inn"
  set PBI_DESKTOP_PATH; powerbi-desktop open "..\GoodnightInn-publish\Goodnight Inn.pbip"; wait 30 s
  powershell -File project\tools\refresh_desktop_model.ps1          (data in about 6 s)
  Bjorn: Publish (Desktop asks to save: yes, it is the copy), then in the service File > Embed report >
  Publish to web (public). After a fix in the generators: write the copy again, open, refresh, Bjorn publishes
  over the same report (the link stays).

What was learned:
  - Edge's --lang and --accept-lang leave navigator.languages on the Windows list (a de-DE run answered "nl").
    Emulation.setUserAgentOverride with acceptLanguage sets the header and navigator.language(s);
    Emulation.setLocaleOverride sets Intl. web.mjs does both and prints navigator.language at "open" and "ready".
