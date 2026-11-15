Review round 2, step D of doc 25 (15 Nov 2026): page 1's craft and the hero's NPV bars

Everything here works on the THROWAWAY copy (never the project; doc 23 rule 6).

The session's screen turned during this step (2248 x 1080, then 1080 x 2248: a remote screen that follows its device).
That is what earlier logs called "the narrow session window". Look before you render:
  [System.Windows.Forms.Screen]::AllScreens      wide  -> the page is drawn whole, 1.41 capture px per page px at scale 3
                                                 tall  -> 0.63 px per page px whole; use the strips (1.84 px per page px)

  wide screen   python round.py view <copy> [state] [scenario]; python round.py shoot <pid> <out> <name> [page] [card]
                page_crop.py finds the page in the capture through one white card (scale from its width; a card's
                shadow blurs its top and bottom edge, so its height is no scale)
  tall screen   page 1: python project\tools\opzet_report.py --out <gen>; copy <gen>\*.Report\definition and
                StaticResources over the copy's; python ..\tiles\mk_tiles.py <copy>\THROWAWAY.Report --page
                p1-brand-review --mast 168 --rows 1; python ..\step9\round.py shoot <pid> <out> p1
                page 2: python ..\step9\round.py view <copy> rec <Low|Expected|High>; ... shoot <pid> <out> <name>

  hero_grey.py <render of Recommended> [grey copy]   DS2-04's test: the bars of package A darker than every other bar
                                                     of the NPV panel, in grey (exit code 1 when not)
  contrast_probe.py <render> name,x,y,w,h ...        the contrast of text as drawn (a label under the chart's band, a
                                                     glyph from a fallback font): darkest pixel against the rectangle's
                                                     commonest colour
  ..\step11\slot_sheet.py <render> <FinalV3 comp> p1-brand-review     the regression: every slot that did not change
                                                     reads as in the FinalV3 sheet

The recovery banner. Desktop opens a new window with "Automatisch herstel bevat enkele herstelde bestanden" (the
throwaway windows of earlier sessions that were ended). It covers the top of a whole-page capture. Every view of the
window has its own banner; its close button is the Button named 'Uitvouwen' that follows the Button 'Herstelde
bestanden weergeven' in the UI Automation tree. Invoke that one (InvokePattern), in the report view; nothing is
recovered and nothing is opened.

What the round found.
  - A stacked area chart takes a per-series switch for its series labels (seriesLabels with a metadata selector, show
    false), as the line chart of F2 does: the band's label is off, the base series still names itself, and the plot
    keeps its width.
  - A text box that lies inside the chart's rect goes under the chart (mouse_order, rule 1). Under the band (Warm Grey
    at 30 %) Night text reads #384151 on #DDDBD8, 7.4:1 as drawn; Dusk would have been 4.3:1.
  - "◆" (U+25C6) is drawn 10 px wide at 16 px and close to what follows: the value card starts 17 px after the type's
    own width, not the 14.7 px the font metrics give.
  - A strip seam (page x 480, 960, 1440) moves a chart's own labels by up to 3 px against a text box beside them: the
    two F1 names were set level on the whole-page capture, not on the strips.
  - Orlando's name left of its dot does not fit: see doc 25, step D, deviations.
