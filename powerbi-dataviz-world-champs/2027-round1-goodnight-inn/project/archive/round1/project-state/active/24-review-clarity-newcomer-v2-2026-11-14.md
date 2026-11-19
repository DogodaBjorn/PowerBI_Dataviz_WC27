# 24 · Clarity review v2: a newcomer with no background, FinalV3 as published (14 Nov 2026)

**Role and question:** the same as doc 19 (`19-review-clarity-newcomer-2026-11-13.md`). A random viewer who follows the
Dataviz World Champs and opens the entry out of interest. No knowledge of the brief, the dataset or the build. The
question is accessibility as *clarity*: can someone with no background follow the report, and where is the content, or
the layout plus the content, unclear, and why?
**Scope:** awareness only, no fixes. Part 1 gives the status of every finding of doc 19 (CL-01 to CL-34). Part 2 lists
what is new in this version (CL-35 onward). Same severity scale as doc 19:

- **S1 · loses the thread.** A wrong conclusion, or the reader cannot say what the page is telling them.
- **S2 · has to work for it.** They get there by decoding, cross-reading or hovering elsewhere.
- **S3 · friction.** A small stumble.

**Version reviewed:** branch `rebuild-finalv3` at `71a5abb`, the report "Goodnight Inn" as published to the web
(fourth publish, 14 Nov 2026, 20:45 UTC). The report files have not changed since that publish (last report commit
`ca9b086`, before the publish), so the gate's captures are the current version and no new render was needed.
Evidence, all existing:

| Source | Used for |
|---|---|
| `deliverables/screenshots/PublishToWeb-2026-11-14/20` | Page 1 in the browser |
| `.../21`, `22`, `24`, `25` | Page 2: Recommended (Expected, Low), What waits and why, Build your own |
| `.../26` to `30` | Tooltips: F3 band, F4 hotel, Definitions, package A, year |
| `deliverables/screenshots/FinalV3/09`, `10` | Build your own with six moves, and over the budget (Desktop, step 11) |

---

## Summary

**No finding left that makes a newcomer lose the thread.** Every S1 of doc 19 is fixed. A newcomer now knows who the
report is for, that page 1 leads to a decision on page 2, and why most moves look like losses (the 2032 rule). They can
also see why a money-losing move sits in package A. Orange now means only "bad".

| Status of the 34 findings of doc 19 | Count |
|---|---|
| Resolved | 19 |
| Improved, something left | 12 |
| Unchanged | 2 |
| Kept on purpose (the puns) | 1 |

**Unchanged:**

- **The chart crossing (CL-15).** The Expected line meets zero at the 2030 tick, yet the caption below says cash
  positive in 2031.
- **The F codes (CL-32).** "F" is still never written out as "finding", and the KPI row now runs F4, F1, F2, F3.

**New, and harder for a newcomer.** The extra detail on page 2 caused these:

- **Recommended screen (CL-35).** It is very full, and after the headline there is no obvious place to look next.
- **"Two moves pass both tests" (CL-36).** The title never says what the two tests are.
- **The ledger (CL-37).** Its F4 row and its footnote can't be read: "0 of 20 · 0", "(dataset units)".
- **Package C and tranche 3 (CL-39).** On "What waits, and why", the table weighs tranche 3 while the chart weighs
  package C, and their numbers differ.

Two earlier findings still need work at that level. The "Commissions" label in F1 can be read as naming the top line
(CL-18). Several things also have more than one name, such as "commissions" and "distribution cost", or "Revenue
management" and "RMS" (CL-28).

Eight smaller items are listed too, including a garbled sentence in the package tooltip (CL-41). The busy screen is a
trade-off: that density is what fixed the biggest earlier problems (see the merge notes).

**Not checked this time:** the builder with nothing picked, the High case, and a real phone.

| New in this version | S1 | S2 | S3 |
|---|---|---|---|
| CL-35 to CL-46 | 0 | 4 | 8 |

---

## Part 1 · The findings of doc 19, one by one

| ID | Doc 19 in one line | Status | What the newcomer sees now |
|---|---|---|---|
| CL-01 | No audience, no decision | **Resolved** | "For the Board: what is wrong, before page 2 says what to fund." and "1 / 2", "2 / 2" in the eyebrows |
| CL-02 | P1 does not lead to P2; F4 a dead end | **Resolved** | Each finding ends with "→ Page 2: ...", a "Next: what we fund, and why →" button; F4's title and link give it a purpose (busiest hotels, extensions at the 2028 gate) |
| CL-03 | The 2032 horizon makes most moves look like losses | **Resolved** | The subtitle says the rule and why a second lens exists; every move shows "a year on cost" next to its NPV |
| CL-04 | "Pays back" meant two things | **Resolved** | "Pays back by 2032" = NPV zero or more; "Cash positive" = the undiscounted running total; both in the glossary, the charts say "Cash positive above this line" |
| CL-05 | Two money measures, two answers for A | **Improved** | The two now have different names and the glossary says "undiscounted". Residual: the same tile and chart still show A at +$3.3M (NPV) and +$6.8M (cash), and the worst case at −$5.5M (tile) and −$4.6M (chart label); nothing on the page links the pairs |
| CL-06 | A money-losing move in A, no reason | **Resolved** | The table title: "the kiosks earn 20.6% a year on cost but pay back after 2032" |
| CL-07 | Move-to-finding link implied by order | **Resolved** | The "Answers" column and the ledger name the finding per move; the kiosks now answer F4 (the busiest hotels), which reads naturally |
| CL-08 | The rules arrive without a source; "growth" undefined | **Improved** | "Growth" is in the glossary. Residual: "We checked all 456 packages the rules allow" (What waits) never says what the rules are; they surface only as "Within the rules: 3 moves, 2 growth, $9.4M of $60.0M" in the builder. S3 |
| CL-09 | Headline used undefined words | **Resolved** | "Fix the middleman first: $9.4M now earns $3.5M a year by 2032. The other $50.6M waits for one Board decision in mid-2028." |
| CL-10 | Profit a year larger than total value | **Resolved** | The subtitle explains why both are shown; "a year by 2032" and "through 2032" are now visibly different lenses |
| CL-11 | The downside stated, not weighed | **Resolved** | "Worst case (Low): −$5.5M through 2032, and still +$1.0M a year by 2032. The app carries it." |
| CL-12 | Orange changed meaning between states | **Resolved** | Orange = bad throughout (negative, over budget, the KPI that moves the wrong way); "Your plan" is Night and turns orange only over budget, which reads as an alarm; C is a grey dashed line |
| CL-13 | Blue meant something else in every card | **Improved** | Blue is now A, Goodnight Inn and "after commissions", and F4 names its dots. Residual in CL-42 (F4's marks) |
| CL-14 | Four legend entries for three cases | **Resolved** | Direct labels at the line ends ("High +$19.2M", "Expected +$6.8M", "Low −$4.6M") |
| CL-15 | Title and line disagree by eye | **Open** | The Expected line still meets the zero line at the 2030 tick, and the caption under the chart now prints "Cash positive 2031 (Expected)" right below it; the year tooltip confirms the convention (year-end values), the eye does not. Seen in the Recommended chart and the builder's chart. S3 |
| CL-16 | Legend ring vs filled dots | **Resolved** | No legend; "Each dot is a package." |
| CL-17 | Range strip without an axis | **Resolved** | The package tooltip states Low, Expected and High in words. A new copy slip in that sentence: CL-41 |
| CL-18 | F1's note described the gap without naming it | **Improved** | The gap is now a shaded wedge labelled "Commissions", and the note splits the 2.8-point fall into commissions (1.0) and running costs (1.8). Residual: the top line has no label of its own, and "Commissions" sits at the end of the top line at about 45%, so it can be read as "commissions are 45%"; the 1.8 points of running costs are not visible as such (they are the fall of the top line). S2 |
| CL-19 | Guest pays more direct; unexplained | **Resolved** | "Booked direct, the guest pays $2.25 more and we keep $17.47 more. Nothing rewards the guest for booking direct; member rates change that." (The $4.46 "commission and fees" on a direct booking is still unexplained; S3, folded into CL-45) |
| CL-20 | NPS without a scale | **Resolved** | "net promoter score (−100 to +100)" in the KPI row |
| CL-21 | Jargon before help | **Improved** | Inline now: "8%: our cost of money", "A year on cost = what a move adds to operating profit in 2032 ÷ what it costs", the NPS scale. Residual: "pt", "RMS", "distribution cost", "tranche", "the 2028 gate" on page 1, "(dataset units)"; see CL-37, CL-38 |
| CL-22 | Glossary missed the report's own words | **Resolved** | Move, package, growth, tranche, the 2028 gate, scenarios, topped 90%, a year by 2032, a year on cost. Not in it: RMS and distribution cost |
| CL-23 | F2's "Our reading" could not be followed | **Resolved** | The sentence is gone; the note now leads to member rates, which page 2 funds |
| CL-24 | Puns need decoding | **Decided** | Kept on purpose (round 9, Bjorn). The "1 / 2" and the literal titles below each eyebrow keep the cost small |
| CL-25 | Who is "we"? | **Improved** | "For the Board" makes the voice management talking to its board. Residual: the same voice cites "the contest's rule" and "the organisers' rate"; see CL-40 |
| CL-26 | Two baselines in F1; "depressed base year" unexplained | **Improved** | F1 speaks of 2023 only. Residual: the footnote "2021 is a depressed base year" is still unexplained, and page 2's ledger measures F2 from 2021 ("half the rise since 2021 undone"). S3 |
| CL-27 | C's contents hidden | **Resolved** | "package C (App + RMS + refresh)" in the What waits table. A new confusion between C and tranche 3: CL-39 |
| CL-28 | Many words for one idea | **Improved** | Pays back and cash positive are now two defined ideas. Residual, new synonym sets: commissions / distribution cost / "with the agencies"; Revenue management / RMS; Booking app / Booking app & member rates / Booking app with member rates / the app; Kiosks at the 20 busiest hotels / Kiosks at 20 desks; Refresh, 10 oldest hotels / Refresh 10 oldest / the refresh / renovation; 8%: our cost of money / the contest's rule / the organisers' rate. S2 |
| CL-29 | Empty builder looked broken | **Resolved** | The builder opens on package A ("Your plan: 3 moves, live by Apr 2028"); over the budget it says so in a band. The nothing-picked state was not re-read for this review |
| CL-30 | Help arrives after the confusion | **Improved** | The key terms are explained in place (see CL-21). Residual: Definitions is still bottom right and hover-only, and the open glossary covers the chart the reader came from. S3 |
| CL-31 | Hover versus tap | **Improved** | "Click a move", and every button and tile works by tap (gate, touch at 1366 px). Residual: the "Hover a ..." tags and all tooltips still need a mouse; the phone check is Bjorn's. S3 |
| CL-32 | "F" never spelled out | **Open** | Still never written as "finding", and the KPI row now reads F4, F1, F2, F3 from left to right, which invites the question whether the codes are a ranking. S3 |
| CL-33 | Precision and units jump | **Improved** | One decimal almost everywhere; ranges carry "$" and "M". Residual: the builder tile's range ("−$5.5M to +$12.7M", "−$16.1M to +$5.7M") has no label saying it runs from Low to High. S3 |
| CL-34 | The point of the scatter in a corner | **Improved** | The scatter is now proof in What waits and Build your own, with a title that says what to see ("none beats A through 2032"). Residual: A and B still touch in the top-left corner. S3 |

---

## Part 2 · New in this version

### At a glance

| ID | Category | Where | In one line | Sev |
|---|---|---|---|---|
| CL-35 | A Context | P2 Recommended | A very full screen: two lenses on ten moves, a ledger, a three-tranche plan, a decision rule and a chart; no clear first place to look after the headline | S2 |
| CL-36 | B Vocabulary | P2 Recommended | "Two moves pass both tests": the two tests are only implied by the column headers | S2 |
| CL-37 | E Chart | P2 Recommended, ledger | The F4 row and the footnote cannot be read: "0 of 20 · 0", "(dataset units)", "2025 brand plus A's full yearly effect" | S2 |
| CL-38 | B Vocabulary | P1 forward links | "The 2028 gate" appears on page 1 twice, before anything explains it | S3 |
| CL-39 | F Logic | P2 What waits | The table weighs tranche 3 (the refresh), the chart below weighs package C (app + RMS + refresh); the newcomer reads them as one thing with two sets of numbers | S2 |
| CL-40 | G Decoding | P2 subtitle, glossary | A board report that cites "the contest's rule" and "the organisers' rate" next to "our cost of money" | S3 |
| CL-41 | G Decoding | Package tooltip | "it pays back by 2032 above zero" does not parse | S3 |
| CL-42 | E Chart | P1 F4 | Unexplained diamond marks; labels that could belong to more than one dot | S3 |
| CL-43 | F Logic | P2 Recommended, Low | "No moves pass both tests", yet A is still "Our recommendation"; the reason sits in the tile, not next to the claim | S3 |
| CL-44 | C Terms | P2 | "A year on cost" (a %) and "A year by 2032" (dollars) are near-identical names for different units, in different tables | S3 |
| CL-45 | G Decoding | P1, P2 | Small sentences that need a second read (listed) | S3 |
| CL-46 | H Interaction | P2 tabs, service | The service's "Click here to follow" bubble over a tab reads like the report's own instruction | S3 |

### Details

**CL-35 · The Recommended state is a very full screen (S2).**
Where: page 2 as it opens. Below a two-line subtitle: a ten-row table with two bar lenses, the recommendation tile
with four KPIs, a worst-case paragraph and a five-column ledger, the $60M plan bar with three tranches and their
numbers, the gate rule paragraph, and a three-line chart with a milestone caption. A newcomer reads the headline and
then has no obvious second stop: the table on the left and the tile on the right both start at the same height and
both open with a sentence that needs the other one ("Two moves pass both tests"; "Our recommendation: package A"). Each
part is clear on its own; together they ask for more working memory than a casual viewer brings. Page 1 does not have
this problem.

**CL-36 · "Both tests" are never named (S2).**
Where: the table title "Two moves pass both tests; the kiosks earn 20.6% a year on cost but pay back after 2032" (Low:
"No moves pass both tests"). The tests are a year on cost above 8% and an NPV of zero or more by 2032. The reader has to
find them in two small markers above the bars, "8%: our cost of money" and "pays back by 2032 →", and work out that a
bar must cross each marker. The arrow in "pays back by 2032 →" points right, but the zero line it refers to sits in the
middle of the NPV column, not at its right edge.

**CL-37 · The ledger's F4 row and footnote (S2).**
Where: the recommendation tile. Row F4: "self check-in hotels · rooms added", then "0 of 20 · 0" and "20 of 20 · 0",
with "kiosks live Apr 2028; guest score +0.25 there (dataset units)". Two measures share one cell, split by a dot, and one
of them is zero in both years. "(dataset units)" tells the reader the unit is unknown, which raises more doubt than it
removes. Row F2 measures "distribution cost", a word page 1 never used (page 1 says commissions). The footnote "2025
brand plus A's full yearly effect, in 2025 dollars" explains the method in words a newcomer cannot unpack. The ledger is
the most direct answer to "what does A fix?", so the newcomer reads it closely.

**CL-38 · "The 2028 gate" on page 1 (S3).**
Where: F3 "→ Page 2: the refresh waits for the 2028 gate, and why." and F4 "→ Page 2: ... extensions decided at the
2028 gate." The phrase reads as a teaser, and page 2 explains it, so the cost is small. But on page 1 it looks like a
known term the reader is expected to have.

**CL-39 · Package C and tranche 3 look like one thing (S2).**
Where: What waits, and why. The table's rows are B (an alternative package), tranche 2 (the airport extensions) and
tranche 3 ("the refresh of the 10 oldest hotels (in package C)"). The scatter above and the chart below compare packages
A, B and C ("C is not cash positive by 2032", "C −$19.2M"). The newcomer maps C in the chart onto the third table row and
then finds numbers that do not match: tranche 3 is $29.5M capex, C is the refresh plus the app and RMS with −$23.4M
NPV, and C in the chart ends at −$19.2M in cash. The table also mixes two kinds of object (one alternative package, two
tranches of the plan) under one header, "Option".

**CL-40 · Whose rule is 8%? (S3).**
Where: the page 2 subtitle ("NPV through 2032 at 8% in 2025 dollars is the contest's rule"), the glossary ("at the
organisers' rate", "the organisers' three scenarios") and the table marker ("8%: our cost of money"). One number gets
three owners. The page also speaks as management to the Board (CL-01), so "the contest's rule" steps out of that frame
in the middle of the subtitle.

**CL-41 · The package tooltip's last sentence (S3).**
Where: the tooltip on A's dot: "Low −$5.5M · Expected +$3.3M · High +$12.7M through 2032; it pays back by 2032 above
zero." The last clause does not parse; it reads like a definition that lost its subject.

**CL-42 · F4's marks and labels (S3).**
Where: the F4 dot chart. Three diamond marks (one per row, near 82%, 79% and 77.5%) are not explained; the row labels
"Airport 82.0%", "City 79.1%", "Highway 77.5%" suggest they are the averages, but nothing says so. In the busy right
half, labels sit between dots: "Gatwick, Montréal" is one label for two dots, and "Orlando", "Phoenix" and "Kuala
Lumpur" are each close to more than one dot. The dashed line carries only "90%"; "topped 90%" is defined in the
glossary, not at the line.

**CL-43 · Recommending A when nothing passes (S3).**
Where: Recommended, Low case. The table title says "No moves pass both tests; the booking app earns 12.1% a year on
cost but pays back after 2032", and the tile next to it still says "Our recommendation: package A" with an orange
−$5.5M. The reason (A still earns +$1.0M a year, and no package beats it) is in the tile's worst-case line and on the What
waits page, not next to the claim that nothing passes. The worst-case line also repeats the case already in view.

**CL-44 · Two "a year" measures (S3).**
Where: the Recommended table's "A year on cost" (a percentage) and the builder's "A year by 2032" (dollars). The names
differ by two words, the units by everything. The glossary separates them; the tables do not.

**CL-45 · Sentences that need a second read (S3).**
- F3 note: "None has started since 2020." (None of what? Renovations.)
- Recommendation tile: "The app carries it: +$3.4M of the +$3.3M." (A part larger than the whole; true because the
  kiosks are negative, but the newcomer stops.)
- What waits, tranche 3: "The data does not price the cost of waiting, so this case is understated."
- What waits, tranche 2: "no NPV shown" (why not is not said).
- The gate rule: "(the app's Low case)" as the source of the 0.6-point threshold.
- F2 table: "Commission and fees −$4.46" on a direct booking (which fees?).

**CL-46 · The "Click here to follow" bubble (S3).**
Where: page 2 in the service, above the active tab button (captures 24, 25). It is Power BI's own hint for a button
with an action, but it sits in the report's banner and reads like the report telling the viewer to click. Bjorn decided
on 14 Nov to leave it (doc 23); recorded so the merge does not lose it.

---

## What works for a newcomer now (keep)

- **The audience line and the page count** ("For the Board: ...", "1 / 2"): one sentence and two characters that set
  the scene.
- **The forward links on page 1** and the Next and back buttons: the two pages now read as one argument.
- **The page 2 headline**: a verb, an amount and a return, and the rest of the budget in one sentence.
- **The subtitle's honesty about the 2032 rule**, and the second lens it introduces: this is what turned the "everything
  loses money" reading around.
- **"A year on cost = ..."** written under the table, and **"8%: our cost of money"** at the bar: definitions where the
  eye is.
- **The worst-case line** ("still +$1.0M a year by 2032") and **"A decision rule, not a forecast."**
- **The What waits table's columns** (the numbers, why it's on the table, why not now, when we decide): the clearest
  structure in the report.
- **Orange as one meaning** (bad), and "Your plan" turning orange only over the budget.
- **Direct labels on the line charts**, and "Cash positive above this line".
- **The glossary's content**: it now holds the report's own words.
- **The builder opening on package A**: the newcomer starts from something that works and changes it.

## Merge notes for the improvement plan

- **No S1 is left.** The four S2 items (CL-35, CL-36, CL-37, CL-39) all sit on page 2, and three of them in the
  Recommended state. Two of the residuals are S2 too: CL-18 (F1's wedge label) and CL-28 (the new synonym sets).
- **The cheapest wins** are words, not layout: name the two tests (CL-36), one word per idea for the synonym sets
  (CL-28), the two copy slips (CL-41, CL-45), and the F-code order in the KPI row (CL-32).
- **CL-35 is a trade-off, not a defect.** The density is what closed CL-03, CL-06, CL-07 and CL-11. The merge should
  weigh it against the jury's and the investor's need for the same numbers, not remove content on clarity grounds alone.
- **Decided items** stay decided unless the merge reopens them: the puns (CL-24) and the service bubble (CL-46).
- **CL-15 has now survived two rounds.** It is small, but a careful newcomer who sees the line meet zero at 2030 and
  reads "2031" right below it may distrust the rest.

## Not verified in this review

- **A real newcomer.** Still a simulated cold read by someone who knows the build history.
- **A phone.** The touch checks of the gate ran at 1366 px in emulation; press and hold on a real phone is Bjorn's
  check (doc 23).
- **The builder's nothing-picked state and the High case** were not re-read; the Low and Expected cases and the
  six-move and over-budget builder states were.
- **The F3 band and F4 hotel tooltips** were looked at only in passing; they appear unchanged since doc 19 and raised
  nothing new.
