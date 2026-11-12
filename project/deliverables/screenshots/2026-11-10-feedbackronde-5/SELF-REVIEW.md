# Self-review, feedback round 5 (10 November 2026, Björn's second look at round 4)

Rendered in Power BI Desktop 2.159 through the WebView2 DevTools port (`project/tools/desktop_shots/cdp.mjs`), page
clipped at 1920 x 1080. The session's RDP window was detached for most of this round, so the WebView only painted a
frame right after a viewport change: every shot is preceded by a `metrics` nudge and checked for a blank frame (a white
capture is a capture error, not the report; the failed ones were deleted, not kept). Edit-mode chrome (the "CTRL+klik"
tip, the selection frame) is Desktop's. Desktop prints chart labels in nl-NL ("+$3,4M", "Totaal").

## Björn's five points against the pixels

| Point | Shot | Verdict |
|---|---|---|
| A, B and C placed properly on the scatter | 02 (full), 05 (small) | Full scatter: the letters sit centred inside 22 px dots (`Named Point Size` 5.8 / 5.3 at multiplier -40; A and B no longer overlap). Small scatter: Power BI puts the letters UNDER the dots whatever their size in that plot (16, 23 and 29 px tried; at -40 it caps the dots at 10 px), so the small layer labels each dot with a Night tag under it: A, B, C in white on Night, legible on the Ice band, the white card and the cloud. |
| B: not picked purely on the capex-to-NPV mix, A simply better; C: a strategic investment, not the risk to take now | 05 | B why-not: "Not picked purely on the capex-to-NPV mix: $2.25M more capex for an NPV $0.6M lower, so A is simply the better deal." (gap from the shown figures, so it matches the cards; guarded for a scenario where B is higher). C why: "Considered as a strategic investment: the refresh of the 10 oldest hotels is the move that targets NPS head-on (F3)." C why-not: "Not the financial risk to take now: NPV −$23.4M, below zero in every case, even High (−$11.4M). One to revisit once A has broken even, or if NPS drops below 0 and growth is at risk." Why-not slots 96 px (three lines). |
| How to read: 456 combinations within the budget | 02 | "Each dot is one of 456 possible packages: a combination of the 10 moves on offer that stays within the $60.0M budget (at least 3 moves, 1 of them growth). Capex across, NPV through 2032 up; above the line it pays back by 2032. Hover a dot to see what it includes, what it does not, and what each move costs and returns." Guide tile 136 px, three lines; counts and budget from the model. |
| Build your own: a big alarm when the selection passes the budget | 08, 09, 10, 07 | The your-plan title row is the alarm: over the budget it turns into a Tangerine band with white 18 pt text "Over the $60.0M budget by $16.65M" (WCAG large text, 4.2:1; the a11y check pairs the text and fill measures branch for branch), and the Deneb selector's new footer reads "Over budget by $16.65M: $76.65M picked, the cap is $60.0M" in Burnt Tangerine bold under the hand that clicks. Within the budget the band is the plain title ("Your plan: 3 moves, live by Jul 2028") and the footer the running total ("Picked: 3 moves, $22.4M of $60.0M"). The rules line now says "over the budget". Empty state unchanged (07). |
| Tooltip: design elements, the same number of decimals | 14 | Night header band with the chip, the name and the case tag (the canvas's own header), the figures on white, the moves table on an Ice tile, "Not in it" in up to three lines (canvas 480 x 552). NPV and capex both carry two decimals everywhere in the tooltip ("−$23.44M" over "$36.90M"; the table "$5.00M / +$3.37M"), the move NPVs rounded at $0.01M so they still add up to the package. The rounded base card is drawn, but Desktop's tooltip container keeps square corners of its own (known). |

Also checked: the tab bar, the scenario toggle, the comparers and the "You" dot still behave as in round 4 (09, 10);
static gates after the last generator run: validate_tmdl 0, schema_check 134 files / 0 failing, a11y_check 0 failures.

## Not captured this round

- A tooltip on B and on a cloud dot: the hover landed on A or beside the dot in the detached session; the page is the
  same for every dot (shot 14 on C, round 4's shots 12 and 14 on A and the cloud).
- Low and High in the three states, and 1366 wide: unchanged since round 4 (no layout change outside the slots named
  above); Björn's zoom check stands.

## Known limitations (carried and new)

- Small scatter: letters as tags under the dots, not inside (Power BI's label placement in that plot size).
- Desktop's tooltip container is square-cornered; the page's rounded base card only shows where the host allows it.
- The Deneb selector has no keyboard toggling; the empty build waterfall draws a $0 total; nl-NL chart labels in Desktop.
