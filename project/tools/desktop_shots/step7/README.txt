Build step 7 of doc 23 (14 Nov 2026): measuring a table or a chart when the Desktop window is narrow

A tile seam through a table, a bar or a chart is no pixel reference: at a fractional zoom Desktop snaps a visual by up to
1.6 page px and rounds each table row to a device pixel. These scripts put one visual whole on a 480 x 270 scratch page
of the THROWAWAY copy (never the project), with a Tangerine marker at y 4 to 8 to anchor the capture.

  hero_probe.py <copy .Report>             pages h_a, h_b (tbl_hero at y 20 and 22), h_c (its last rows), h_d (its bar columns)
  bar_probe.py <copy .Report>              pages b_a (ch_plan_bar, slot top at y 100) and b_b (ch_plan_cum, page y 828 at y 60)
  bar_measure.py <captures dir> <t_cal.txt>  the bar's rows and the chart's gridline, zero line and tick labels, in page px
  find_cal.py <t_cal.png> <t_cal.txt>      the calibration rectangle of a tile round (tiles/README.txt, step 4)
  scan_hero.py <page.png> ...              rule, reference line and bar rows of the hero in a stitched page
  scan_cum.py <page.png>                   gridline, zero line, gate line and line ends of the plan chart in a stitched page

After writing the pages: powerbi-desktop reload --pid <pid>, wait ten seconds, capture each page twice with
node cap.mjs <pid> <page> 3 <out.png> (the first capture after a reload can miss a visual).
