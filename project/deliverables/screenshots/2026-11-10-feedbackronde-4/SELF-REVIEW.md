# Self-review, feedback round 4 (10 November 2026)

Rendered in Power BI Desktop 2.159 through the WebView2 DevTools port (`project/tools/desktop_shots/cdp.mjs`), page
clipped at 1920 x 1080 (`metrics` 2356 x 1400) and at 1366 wide (`W1366*`). The report is the generated
`GoodnightInn-opzet` on branch `feedback-ronde-4`; model refreshed from the organisers' blob, measures synced after the
last generator run. Edit-mode chrome (the "CTRL+klik" tip, the selection frame round a slicer) is Desktop's, not the
report's. Desktop prints numbers in nl-NL on chart labels ("+$3,4M", "Totaal"); Publish to Web shows the viewer's locale.

## Checklist against the plan (every item looked at in the pixels)

| Item | Shot | Verdict |
|---|---|---|
| Copy diet: every note one sentence, no "…" at the end of a card | 01, 02, 05 | OK. F1, F2, F3 notes one sentence each; `Rec Note` two lines; B and C why / why-not one sentence each; footers one line. |
| NPS line "still positive, but falling every year · last of 4" | 01 | OK, in Burnt Tangerine (last of four and falling). |
| More orange within the kit roles | 01, 02, 05, 13 | OK. KPI context lines (margin, OTA, NPS) Burnt Tangerine, occupancy Deep Coffee; F-codes in the kickers; the uncertainty line; C dashed Tangerine and "Your plan" Tangerine in the comparers; the negative NPV and the "does not pay back" line in the tooltip. |
| Reading guide before the chart | 02 | OK: Ice tile with kicker, legend (three dot kinds) and two lines of guide text. |
| Scatter title one line | 02, 04 | OK ("Only 6 of 456 packages pay back by 2032, all under $15M"; in Low: "None of the 456 possible packages pays back by 2032 in the Low case"). |
| Tab bar: active tab filled, the dropdown gone | 02, 05, 07 | OK. |
| State rec: tile, waterfall, cumulative chart with year axis, uncertainty line | 02, 03, 04 | OK in Expected, High and Low; titles follow the scenario. |
| State alts: small scatter, B and C cards, comparer with A Coffee Blue | 05, 06 | OK. The cards show capex, NPV, range, why, why not, the payback line. Comparer title handles the level case ("B ends level with A by 2032; C never breaks even"). |
| State build: Deneb selector, plain click toggles, numbers / waterfall / comparer / dot follow | 07, 08, 09, 10 | OK. Empty state says "Nothing picked yet" and "The rules: …" (07); one move picked shows the rule shortfall (08); A plus the breakfast upgrade, four moves, "Within the rules" and "behind A by $0.3M" (09); A without the app flags the kiosk rule in Burnt Tangerine (10). A rebuilt from three clicks ($9.4M, +$3.3M) was seen in the spike run (session scratchpad), not kept in this batch. The Tangerine "You" dot appears on the small scatter. |
| Tooltip: case tag, NPV, capex, payback, range, moves table, "Not in it" | 12, 13 | OK on A and C. 480 x 520; the table has room for up to eight moves, so three-move packages leave white space above the "Not in it" line (accepted). |
| 1366 wide | W1366a-d | Everything fits; text scales with the page (12 pt at 1920 is about 8.5 pt at 1366, Björn's standing decision). |
| 12 pt floor, no responsive charts, alt text from the model | static | `a11y_check.py` 0 failures over the three states (tiles count as sub-cards in the reading order). |

## Known limitations recorded

- The Deneb selector is mouse and touch only: no keyboard toggling (Deneb has no keyboard selection). Everything it
  drives (the numbers, the waterfall, the comparer) is reachable by keyboard and screen reader; the plan itself is not.
  A native button slicer is one flag away (`--selector=native`) if this weighs heavier than the design.
- In the empty build state the waterfall still draws a "$0,0M Totaal" bar: a waterfall cannot hide its total.
- Publish to Web with the Deneb visual (AppSource-certified) is Björn's gate; not tested here.
- On the small scatter (alts and build) A and B draw as dots without their letters: the chart is too small for Power BI to place the category labels. A is still the Deep Coffee dot, the legend in the alt text and the comparer name it; the full-size scatter in the rec state carries the letters.
- The Deneb selection persists across a Desktop reload within one session; a fresh open starts empty.
- Shot 14 (a cloud dot) hovered an empty spot; the tooltip on cloud dots is the same page as on A and C (shots 12, 13).
