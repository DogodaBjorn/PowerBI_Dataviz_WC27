# The last check: checklist

Work top to bottom. Part A is pass or fail; one failure there is a no-go. Parts B to E are "as expected" or "differs":
for every difference, name the view and quote what you see. Part F is the submission post.

Sources for each part: the live report where you have the link, otherwise the captures in `walkthrough/` (their
README lists the 23 views) and the text files in `walkthrough/texts/` (every visible text and every alt text of a
view, one per line).

## A · The contest's hard rules (a failure here is a no-go)

| # | Rule (Round 1 brief, `project/contest/round-1-brief.txt`) | Where to look | Expected |
|---|---|---|---|
| A1 | One brand | both pages | Goodnight Inn only |
| A2 | Two visible pages, answering "The Brand Review" and "The Investment Strategy" | the page list of the report | "1 of 2" and "2 of 2"; no third page reachable |
| A3 | At least three initiatives recommended | page 2, the recommendation tile | Booking app with member rates + Revenue management + Kiosks at the 20 busiest hotels |
| A4 | At least one growth initiative | page 2, column "Answers" | "F2 · growth" and "F1 · growth" among package A's three |
| A5 | Within the brand's budget ($60M) | page 2, the plan title and bar | $9.4M + $12.4M + $29.5M + $8.7M not needed = $60.0M |
| A6 | Financial and operational impact through 2032 | page 2, the four numbers and the "What we track" table | NPV through 2032, a year by 2032, a 2025 and a "2032 with A" value per finding |
| A7 | Choices, risks and trade-offs explained | page 2: Low case, What waits, the gate rule | a Low case on every number; a row per option that waits; one release rule |
| A8 | Provided data only | the source lines at the foot of both pages | "Pillow & Key Group dataset" |
| A9 | At least four built-in Power BI visuals | both pages | line, area, column, table, scatter, bar, cards, slicer; no custom visual |
| A10 | Renders in the published link, signed out | open the link in a private window | both pages draw, with data, no sign-in prompt, no error tile |
| A11 | Accessibility is part of the design | `gate/gate-summary.txt` | the keyboard walk has 0 stops without a name on all four views |

## B · The seven lines of publish 7

`CHANGES-publish7.md` has each line as it must read, per case.

- [ ] B1 The tile's second line reads "The app alone: ..." in Low, Expected and High, on one line, not cut off.
- [ ] B2 What waits, row B, "Why not now": the new sentence in all three cases, with the two percentages.
- [ ] B3 Status column: "package B" for the Breakfast upgrade, "not full" for Kingston +40 rooms, the other eight
      unchanged.
- [ ] B4 Tranche 3's label: "$29.5M · 2028 gate, only with a case beyond 2032".
- [ ] B5 "Low −$6.9M · High +$12.6M" in row B; "Low −$5.5M · High +$12.7M" under "Your plan" as Build opens.
- [ ] B6 The table's two value columns are headed "≥ 8%" and "≥ $0".
- [ ] B7 "whose renovation finished in 2021" in the tranche 3 row.
- [ ] B8 None of these old strings is left on any view: "carries it", "test 1", "test 2", "last renovated in 2021",
      " to +$12.6M", " to +$12.7M".
- [ ] B9 No text ends in "..." or is cut at a card's edge; the What waits table ends inside its white card in all
      three cases.

## C · Numbers that must agree between views (Expected case unless said)

- [ ] C1 Package A is $9.4M capex, +$3.3M NPV through 2032, +$3.5M a year by 2032, 37.5% a year on cost: the same in
      the headline, the tile, the package tooltip on A and Build as it opens.
- [ ] C2 A's three moves in the table: +$3.4M, +$0.5M, −$0.6M NPV (sum +$3.3M).
- [ ] C3 Low: A is −$5.5M and +$1.0M a year; High: +$12.7M and +$6.2M a year. The tile's first line and the headline
      follow.
- [ ] C4 B: $11.7M capex; +$2.7M NPV and +$4.0M a year (Expected); −$6.9M and +$1.3M (Low); +$12.6M and +$6.7M
      (High). The new sentence's differences follow from these: 11.7 − 9.4 = 2.3; 4.0 − 3.5 = 0.5; 3.3 − 2.7 = 0.6.
- [ ] C5 "None of the 456 packages beats A through 2032" in all three cases; "Only 6 pay back by 2032, all under
      $15M" (Expected), "None pays back by 2032" (Low), "Only 57 ... all under $35M" (High).
- [ ] C6 Page 1, F1: commissions 1.0 + running costs 1.8 = the 2.8-point fall. Page 2: 33.7% to 35.1% is "half the
      fall recovered".
- [ ] C7 The gate rule's "0.6 points" is half of 11.3% to 10.1%.
- [ ] C8 "Cash positive during 2031 (Expected)"; the year tooltip gives −$0.2M at the end of 2030 and +$3.3M at the
      end of 2031.
- [ ] C9 Toronto topped 90% in 17 of the last 24 months and Gatwick in 14: the same on page 1 and in What waits.

## D · Nothing that was fixed has come back

- [ ] D1 No bubble "Click here to follow" when the mouse rests on a tab or a button (`gate/`, the two tab-rest
      captures; live: rest the mouse on a tab for three seconds).
- [ ] D2 The scenario pills and the three tabs answer the mouse in a 1366 px wide window (`gate/gate-summary.txt`,
      the mouse test at 1366 px: clear on all four views).
- [ ] D3 A click on a chart or a table row changes nothing outside that visual.
- [ ] D4 None of these words is on any page: "desks", "RMS", "dataset units", "no NPV shown", "contest".
- [ ] D5 "cash" and "not discounted" stand on all three cumulative charts.
- [ ] D6 Against publish 6, pixel for pixel, only the places named in `CHANGES-publish7.md` differ
      (`gate/gate-summary.txt`, the comparison with the earlier run).

## E · A fresh eye (ten minutes, as a judge who opens the link for the first time)

- [ ] E1 Can you say after page 1 what is wrong with the brand, and after page 2's first screen what to fund?
- [ ] E2 Anything that reads as a mistake: a number that contradicts another, a sentence you have to read twice, a
      label on the wrong mark. Check `CHANGES-publish7.md`, "Known and accepted", before reporting it.
- [ ] E3 Spelling and grammar in the seven new lines.

## F · The submission post (Bjorn posts; check his draft against this)

- [ ] F1 An image of the report.
- [ ] F2 A short description that names the brand, Goodnight Inn (`DESCRIPTION-draft.md`).
- [ ] F3 The Publish to Web link, or the `.pbix` saved from the window publish 7 came from.
- [ ] F4 The official contest tag, taken from the Contests Gallery when posting.
- [ ] F5 Posted before the round closes: 18 Nov 2026, 11:59 p.m. Pacific (19 Nov, 08:59 in the Netherlands). The
      plan is 17 Nov.
- [ ] F6 Every number in the description is on the published report.

## The report back

One message to Bjorn: **go** or **no-go** first; then the failures of part A (if any); then every "differs" of parts
B to D with the view's name and what you saw; then at most five remarks from part E. Say for each part whether you
checked it on the live report or on the captures.
