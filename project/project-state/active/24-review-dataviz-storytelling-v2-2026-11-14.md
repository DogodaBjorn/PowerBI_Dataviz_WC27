# 24 · Dataviz and storytelling review v2: FinalV3 as published (14 Nov 2026)

**Role:** the same dataviz and storytelling consultant as doc 19, with the same objective: does the report tell one
story, does every chart earn its place, and where does the data offer a better story? This round also checks
whether doc 19 and doc 20 (the requirements) were carried through.
**Scope:** taste and target state. This review says *what* should still change and gives exact copy where words are
the fix. It does not say how to build it. It is written to go to the build planner and the builder like doc 20.
**Version reviewed:** branch `rebuild-finalv3`, commit `71a5abb` (the fourth publish, Publish to Web gate passed).
Evidence, in this order of weight:

- `deliverables/screenshots/PublishToWeb-2026-11-14/`: what a judge sees, header artwork included. Used renders:
  20 P1, 21/22 Recommended Expected/Low, 24 What waits, 25 Build, 29 the package tooltip, 31 at 1366 px, 35 P1 in a
  Dutch browser.
- `deliverables/screenshots/FinalV3/`: the states the publish set doesn't cover (10 over budget, 11 nothing picked).
- Zooms of the hero and the capital-plan chart from render 21 (scratch only).

**Decisions taken since doc 20 that this review does not reopen:**

- From doc 21: N-1 native selector, N-2 "2.8 stays", N-3 What waits as one table, N-4 the finding tooltips deleted,
  N-5 the capital-plan layout.
- From doc 23: Bjorn's answers of 14 Nov, including 20.6 %, the dropped caption sentence, and leaving the
  "Click here to follow" bubble as it is.

**IDs:** `DS2-nn`. Each item names the doc-19 or doc-20 item it continues. Priority:

- **T1:** costs trust with a numerate judge.
- **T2:** lifts the score.
- **T3:** polish.

Effort: **C** = copy or colour only (measures and text, no layout), **L** = touches layout.

---

## 0 · Verdict

**The story now closes.** It's a different report from the one reviewed on 13 Nov:

- Page 1 sets up four findings with their evidence.
- Page 2 opens with the ask and the return.
- The hero shows why these three moves on two lenses.
- The ledger says what A does to each finding by 2032.
- The capital plan turns "$50.6M held back" into two tranches and one gate.
- Every contradiction doc 19 listed is gone: the loyalty sentence, three release rules, kiosks answering F3,
  the hover-only findings, "Totaal" and the decimal commas.
- The Dutch-browser render (35) shows decimal points everywhere.

**Score, same lenses as 13 Nov (my estimate):**

| Lens | 13 Nov | Now | What moved it |
|---|---:|---:|---|
| Jury: Analytical quality | 8.0 | 9.0 | Two lenses, the honest margin split in F1, ~~check-in complaints behind the kiosks~~, the 44 of 50 count |
| Jury: Insightfulness | 7.5 | 9.0 | The ledger closes the operational-impact rule; F4 leads to kiosks and the gate |
| Jury: Visual effectiveness | 7.0 | 8.3 | Clean hero, one control row, Night plan colour. Held back by text density on P2 and a few label details |
| Jury: Creativity and innovation | 8.5 | 8.7 | Less "over-engineered" (all native); the 456-package proof and the builder are kept |
| Jury: Accessibility | 7.0 | 8.8 | Static content, tab order in reading order, locale-proof numbers, a keyboard-usable selector |
| **Jury total** | **38.0 / 50** | **≈ 43.8 / 50 (8.8)** | |
| Investor committee | 6.0 | ≈ 8.4 | One release rule, bounded downside, a 2032 ledger, growth answered at a gate. It would now approve the strategy with tranche 1 funded |

> **Crossed off, 14 Nov (check against the published report):** "check-in complaints behind the kiosks" is not in
> this version. The word "complaint" is on no page and in no alt text of the fourth publish
> (`screenshots/Committee-walkthrough-2026-11-14/texts/`), and no visual in `project/pbip` carries it. The queues are
> stated, not shown: that is the investor's INV-DE-2, which stands. The 9.0 was given with this credit in it.

**What still keeps it from 9.5.** It's no longer the story. It's three smaller things:

1. **Two money measures for one thing, side by side, without a bridge** (DS2-01). This is the only remaining trust
   risk.
2. **Page 2 asks a lot of reading.** The What-waits table is a wall of prose. The Recommended state carries roughly
   350 words (DS2-05, DS2-06, DS2-10).
3. **A handful of label and consistency seams** that a careful judge collects: the F4 title vs its chart, three names
   for the kiosks, a builder's note leaking into the UI, and lines hidden under their labels.

**Expected result:** all T1 and T2 items below are copy and colour (C), except DS2-06. Done in one round with one
republish, they should take the report to about 9.3. The last 0.2 is density (DS2-10): fewer words, not more
features.

**Cost reminder:** the Publish to Web gate is passed. Every change below means one more publish and a `gate.py` run.
Batch them into **one** round, copy and colour first, and avoid layout changes unless the item says L.

---

## 1 · Doc 19 / doc 20, carried through?

| Doc 19 item | Status | Note |
|---|---|---|
| DS-01 KPI row as index, NPS scale, page count, audience | ✅ Done | Reads well; the F-codes make the row a table of contents |
| DS-02 F1 wedge, honest split | ✅ Done | Band between the lines; the note's 1.0 + 1.8 = 2.8 adds up to the title (N-2) |
| DS-06 F2 bridge to member rates | ✅ Done | The strongest card on P1. The loyalty sentence is gone |
| DS-04 F3 cause and count | ✅ Done | "44 of 50 hotels; 6 have no renovation date" sits tight under the axis (DS2-12) |
| DS-07 F4 as all 50 hotels | ✅ Done, one new issue | The title claims what the chart can't show (DS2-03) |
| DS-08 / DS-31 navigation | ✅ Done | The Night "Next" button is the right weight |
| DS-10 two-lens hero | ✅ Done (as a bar table, better than the scatter I sketched) | Colour weight in the NPV panel (DS2-04) |
| DS-11 What waits | ✅ Done (as a table, N-3) | Too much prose; a builder note leaks (DS2-05, DS2-06) |
| DS-20 ledger | ✅ Done | One cryptic cell; text only (DS2-07) |
| DS-21 capital plan | ✅ Done | Its chart has no title and shows a different measure from the tile (DS2-01, DS2-08) |
| DS-22 tile | ✅ Done | Flat card, return, downside, concentration, urgency all present. Low view repeats itself (DS2-09) |
| DS-23 headline | ✅ Done | Scenario-aware ("$1.0M a year" in Low): good |
| DS-24 Build your own | ✅ Done | Opens on A, square checks, both lenses, Night plan, clean empty state |
| DS-30 hover depth only | ✅ Done | Nothing the Board needs sits behind hover |
| DS-32 / DS-33 controls | ✅ Done | One row in the masthead, one control language |
| DS-40 number grammar | ✅ Done | Proven in a Dutch browser (render 35) |
| DS-41 one word per idea | ⚠ Mostly | Move names drift between visuals (DS2-02) |
| DS-42 the horizon in plain words | ✅ Done | In the P2 subtitle |
| DS-43 colour roles | ✅ Done | Orange now means "wrong" only; the ⓘ glyph in Burnt Tangerine is accepted |

---

## 2 · Findings

### DS2-01 · Two money measures for one thing, with no bridge (T1, C)

*Continues CL-05 and doc 20 R-G2.*

- **What I see:**
  - On Recommended, the tile says **"Worst case (Low): −$5.5M through 2032"** and **"+$3.3M NPV"**. Forty
    pixels lower, the capital-plan chart ends at **"Low −$4.6M"** and **"Expected +$6.8M"**.
  - On What waits, the table says package C is **"−$23.4M through 2032"**. The chart under it ends at
    **"C −$19.2M"**.
  - The chart on Recommended has no title at all. The What-waits chart is titled "Cumulative net impact, $M" without
    saying the money is not discounted.
- **Why it matters:** the numbers are both right (NPV is discounted; the line is cumulative cash, not discounted).
  But a finance judge sees two values for "A's worst case" on one screen and starts auditing instead of reading.
  It's the last credibility seam in an otherwise very careful entry.
- **Ideal:** every cumulative chart says, in its title or its value axis, that it shows **cash, not discounted**.
  Where it sits next to an NPV, one clause says why the numbers differ.
- **Copy:**
  - **Recommended (capital-plan chart), new chart title:** "Package A, cumulative cash, $M (not discounted, so it
    ends above NPV)".
  - **What waits, chart title:** "Cumulative cash, not discounted, $M: B ends level with A by 2032; C is not cash
    positive by 2032".
  - **Build, chart title:** "Your plan against A, cumulative cash, not discounted, $M (Expected case): …" (the
    dynamic tail stays).
  - **Glossary, new term or extended entry:** "Cumulative cash: the yearly net impact added up, not discounted.
    It ends higher than NPV, which discounts each year at 8%."
- **Done when:** no cumulative value appears on a page without the words "cash" and "not discounted" on its chart.
- **Option, not recommended this close to submission:** switch the three charts to *discounted* cumulative impact.
  Their end points would then equal NPV (+$3.3M, −$5.5M, −$23.4M), and "pays back by 2032" would mean one thing
  everywhere. It's cleaner, but it is model work, a full recheck and a new gate run.

### DS2-02 · One name per move, everywhere (T1, C)

*Continues R-G2.*

- **What I see:** the same move goes by different names:

  | Hero | Selector, Build bars, package tooltip |
  |---|---|
  | "Kiosks at the 20 busiest hotels" | "Kiosks at 20 desks" |
  | "Booking app & member rates" | "Booking app" |
  | "Refresh, 10 oldest hotels" | "Refresh 10 oldest" |

  "20 desks" vs "20 busiest hotels" is the one that matters. The whole F4 → kiosks argument rests on *busiest
  hotels*.
- **Ideal:** a two-form name register. Long form in the hero, tile, ledger and What waits; short form only where
  width forces it (selector, Build bars, tooltip table). Both forms use the same nouns.

  | Long | Short |
  |---|---|
  | Booking app & member rates | Booking app & rates |
  | Revenue management | Revenue management |
  | Kiosks at the 20 busiest hotels | Kiosks, 20 busiest |
  | Breakfast upgrade | Breakfast upgrade |
  | Gatwick +40 rooms | Gatwick +40 rooms |
  | Energy programme | Energy programme |
  | Toronto +40 rooms | Toronto +40 rooms |
  | Kingston +40 rooms | Kingston +40 rooms |
  | Boston new hotel | Boston new hotel |
  | Refresh, 10 oldest hotels | Refresh, 10 oldest |

- **Done when:** a text search finds "desks" nowhere, and every short name begins with its long name's first noun.

### DS2-03 · F4: the title claims what the chart doesn't show (T1, C)

*Continues R-P1-6. I'm correcting my own copy here.*

- **What I see:**
  - The title says "Toronto topped 90% occupancy in 17 of the last 24 months". The chart shows each hotel's
    *annual* 2025 occupancy.
  - The reader looks for the 17 months and can't find them.
  - The chart's real message is a different one: the airport row sits furthest right, and five of the seven labelled
    dots are airports.
- **Copy:**
  - **Title:** "Our airports run fullest: five of the seven fullest hotels are airports".
  - **Note** (replaces the current first sentence): "Toronto topped 90% in 17 of the last 24 months, Gatwick in 14,
    Montréal in 13; Kingston, the third extension on offer, in none."
  - The forward link stays.
- **Also (T3, C):** the row averages are drawn as diamonds that nothing explains. Add "◆ average" after the row
  labels, or to the note.
- **Done when:** every number in the F4 title can be checked on the F4 chart.

### DS2-04 · Hero: the heaviest mark is the worst loser (T2, C)

*Continues DS-10.*

- **What I see** (zoom of render 21):
  - In the NPV panel the refresh's −$27.3M is a long Night bar: the darkest, largest mark on the decision page.
    The eye lands on what we are *not* doing.
  - The status colour (Night = "2028 gate") is repeated in both panels. In the right panel it adds weight without
    adding information, since the Status column already says it.
  - The "8%: our cost of money" label starts at the 8% line but sits in the header band, above "A year on cost".
    It reads as a second column header rather than as the label of the thin line inside the bars.
- **Ideal:**
  - **NPV panel:** package A's three bars in blue, all other bars in the light grey. Status stays in the Status
    column and the left panel's colours. The eye now goes to the three blue bars, the ones that matter.
  - **8% line:** its label sits on the line, or the header becomes "A year on cost (line: 8%, our cost of money)"
    and the floating label goes.
- **Done when:** in a greyscale copy of render 21, the three A rows are the darkest marks in the NPV panel.

### DS2-05 · What waits: a builder's note leaks into the table (T1, C)

*Continues R-W-2.*

- **What I see:** Tranche 2's "The numbers" cell ends with **"no NPV shown"**. That is my requirement's
  instruction (doc 20: "no NPV shown (R-P2-7 rule)") printed as copy. A judge reads it as "they hid the NPV".
- **Copy:** replace it with "NPV not shown: the data prices a 2027 start". Or drop the line, because tranche 3's cell
  shows the package-C NPV and tranche 2's "Why not now" already gives both NPVs (−$3.7M and −$3.5M). **Preferred:**
  drop it.
- **Done when:** no cell reads like an instruction to the builder.

### DS2-06 · What waits: from memo to table (T2, C; L only if row heights change)

*Continues R-W-2 / N-3.*

- **What I see:** 3 rows × 5 columns of prose. About 230 words at body size, in cells of four to six lines. It is
  correct and well argued, but it is the least visual element in the report. A judge skims it.
- **Ideal:** the same table with roughly 35 % fewer words. Every cell is one idea. "When we decide" holds only the
  decision; Kingston moves to "Why not now".
- **Copy:**

  | Option | The numbers | Why it's on the table | Why not now | When we decide |
  |---|---|---|---|---|
  | B · Breakfast instead of kiosks | $11.7M capex · +$2.7M through 2032 · +$4.0M a year by 2032 · −$6.9M to +$12.6M | Guest scores in all 50 hotels, not 20 | $2.3M more than A for $0.6M less through 2032, and the queues at the 20 busiest hotels stay | Not planned |
  | Tranche 2 · Airport extensions, +80 rooms | $12.4M capex · +$1.7M a year once live · 13.8% a year on cost | Toronto topped 90% in 17 of the last 24 months, Gatwick in 14 | Neither pays back by 2032 (−$3.7M, −$3.5M). Kingston (61% full) is not on the list | 2028 gate: if the app delivers and both stay full |
  | Tranche 3 · Refresh, 10 oldest hotels | $29.5M capex · +$2.3M a year once live · 7.9% a year on cost · in package C: −$23.4M through 2032 | Renovation works: the 2021 renovations held NPS near +6 while the rest fell to +2.7 | 7.9% a year on cost, under our 8%. The data can't price the cost of waiting, so this case is understated | 2028 gate, with a case that looks beyond 2032 |

- The number cells keep their line breaks (one figure per line) where the table allows it. The "·" above stands
  for a line break.
- **Done when:** no cell runs past four lines at 1920 px.

### DS2-07 · Ledger: one cryptic cell, and a missed chance to show the change (T2, C)

*Continues DS-20.*

- **What I see:**
  - The F4 row reads "0 of 20 · 0 → 20 of 20 · 0". Two measures are packed into one cell with a "·", and the
    reader has to decode the column header to parse it.
  - The finding chips wrap ("F2 The / middleman").
  - The ledger is the emotional pay-off of the whole report (P1's problems coming back fixed), but it is set as a
    plain table of numbers.
- **Copy:**
  - **F4 row:** "What we track" = "the 20 busiest hotels with self check-in"; 2025 "0"; 2032 with A "20"; Status
    "no rooms added now; up to 80 at the 2028 gate".
  - **Chips:** the F-code alone in the first column ("F2"); the finding's name moves to the start of the "What we
    track" line ("The middleman: distribution cost, % of room revenue"). If that doesn't fit, keep the chip but stop
    the wrap by giving the column the width of "F3 The fading welcome".
- **Ideal, T3 if there is time:** an arrow between the two values ("11.3% → 10.1%"), in one column, so the change
  reads as a change. That is a copy change in the value measure, not a new visual.
- **Done when:** no ledger cell contains two measures, and no chip wraps.

### DS2-08 · Capital-plan chart: lines hidden under their labels, and the crossing (T2, C)

*Continues R-P2-7, CL-15.*

- **What I see** (zoom):
  - The white boxes behind "High +$19.2M" and "Low −$4.6M" cover the last stretch of those two lines, so they
    seem to stop before 2032.
  - The Expected line crosses zero just after 2030, but the strip says "Cash positive 2031 (Expected)". A reader who
    trusts their eye sees 2030.
  - The value axis has +$20M and $0M only, and the Low line runs below zero without a tick.
- **Ideal:**
  - Labels without a background box, or placed where they don't sit on a line.
  - The milestone strip says what the eye sees and what the number means: "Cash positive during 2031 (end of 2030:
    −$0.2M)". Or the end-of-2030 point carries its value.
  - One tick below zero ("−$10M").
- **Done when:** all three lines visibly reach 2032, and the strip's year agrees with the crossing.

### DS2-09 · The Low view repeats itself, and its hero title picks the wrong hero (T2, C)

*Continues R-P2-3, R-P2-6.*

- **What I see** (render 22):
  - In Low, the tile's four numbers already show −$5.5M and +$1.0M, and the next line repeats them ("Worst case
    (Low): −$5.5M … +$1.0M").
  - The hero title says "the booking app earns 12.1% a year on cost", but Gatwick (13.3%) earns more in Low. A judge
    toggling Low will ask "then why not Gatwick?"
- **Copy:**
  - **Tile, line 1 in the Low view:** "Expected case: +$3.3M through 2032 and +$3.5M a year by 2032." (In High:
    "Worst case (Low): …" as now.)
  - **Hero title, Low:** "In the Low case no move pays back by 2032; package A still loses least of all 456
    packages".
  - **Data:** A is the NPV maximum in all three cases (`packages.txt`, presets). Re-verify in the model before the
    copy ships.
- **Done when:** in each scenario, the tile's lines add information that its four numbers don't already show.

### DS2-10 · Page 2 reading load (T2, C)

*New. This is the remaining step to 9.5.*

- **What I see:** the Recommended state reads well, but it reads *long*. These text blocks each sit at body size or
  larger:
  - a two-line subtitle;
  - two tile sentences;
  - a ledger of four two-line rows;
  - a four-line gate paragraph;
  - a milestone strip;
  - the hero caption.

  In total that is around 350 words. The headline and the hero title pass the 3-second test. The 3-minute trust is
  there. The middle (30 seconds, "what's the plan?") is where a judge drops off.
- **Ideal:** cut words, not elements.
- **Copy:**
  - **Subtitle:** "The other $50.6M waits for one Board decision in mid-2028. Expected case; NPV counts nothing after
    2032, so we also show what each move earns a year once live." (One line shorter. "In 2025 dollars at 8%" is
    already in the source line.)
  - **Gate paragraph:** "The 2028 gate, once all three moves are live. Tranche 2 goes ahead if distribution cost
    is down at least 0.6 points (the app's Low case) and Gatwick and Toronto topped 90% in 6 of the last 12 months.
    The refresh returns with a case beyond 2032. A decision rule, not a forecast."
  - **Ledger status words** at most five words each: "half the rise undone", "half the fall recovered", "rooms at
    the 2028 gate", "deferred to the 2028 gate".
- **Done when:** the Recommended state carries at most about 280 words. Count with `build_checks.py` text
  extraction.

### DS2-11 · Package tooltip: one awkward sentence, empty foot (T3, C)

*Continues R-TT-1.*

- **What I see** (render 29): "Low −$5.5M · Expected +$3.3M · High +$12.7M through 2032; it pays back by 2032 above
  zero." The tail is my requirement's wording and reads like a rule, not a sentence. Under a three-move package
  there are about 150 px of white space (the page is 616 px high for the eight-move case; accepted in Q9d).
- **Copy:** "Low −$5.5M · Expected +$3.3M · High +$12.7M through 2032." End of sentence.
- **Kept as accepted:** the empty foot (Q9d).

### DS2-12 · Small P1 and P2 seams (T3)

| # | Where | What | Fix (C unless noted) |
|---|---|---|---|
| a | P1 F3 | "44 of 50 hotels; 6 have no renovation date." sits tight under the bar labels and reads as a fourth axis label | 8 px more space above it, or start the note with it |
| b | P1 F4 | The label "Orlando" stands 20 px from its dot, closer to Phoenix's; "Gatwick, Montréal" is one label for two dots | Orlando's label to the left of its dot; the joint label is fine |
| c | What waits | The scatter title wraps to two lines and runs into "Hover a dot" | "None of the 456 packages beats A through 2032" (one line) |
| d | P2 masthead | "← The Brand Review" floats between the eyebrow and the tabs | Accept; or move it 16 px after the eyebrow's end so it reads as part of it (L, tiny) |
| e | Build, empty state | "Picked: 0 moves, $0.0M of $60.0M" under the selector while the tile says "Nothing picked yet" | Hide the picked line at zero, or "Nothing picked: $60.0M to spend" |

---

## 3 · A story point for the record, not a change

**P1's headline vs F1's own note.** The headline says "a slipping margin: Goodnight Inn pays the middleman". F1's
note now shows, honestly, that since 2023 running costs took 1.8 of the 2.8 points and commissions 1.0. Both are
true, and the headline doesn't claim the middleman is the only cause. A sharp judge may still notice that the bigger
part of the slip (staff, +1.3 points of revenue) is not what page 2 fixes first. The ledger answers that half of the
fall is recovered by A, the kiosks being the one move that cuts running costs.

My advice is to leave it. The honesty in F1 is worth more than a tighter headline, and changing the headline now
would ripple through both pages. If a juror raises it, the answer is on the page.

---

## 4 · The fix list, in one round

| Order | ID | Tier | Effort | Where |
|---|---|---|---|---|
| 1 | DS2-01 cash vs NPV, chart titles and glossary | T1 | C | P2 all states, glossary |
| 2 | DS2-05 "no NPV shown" | T1 | C | What waits |
| 3 | DS2-02 one name per move | T1 | C | selector, Build bars, tooltip |
| 4 | DS2-03 F4 title and note | T1 | C | P1 |
| 5 | DS2-04 NPV-panel colours, 8% label | T2 | C | P2 hero |
| 6 | DS2-07 ledger F4 cell and chips | T2 | C | P2 ledger |
| 7 | DS2-08 capital chart labels, crossing, tick | T2 | C | P2 capital plan |
| 8 | DS2-09 Low view tile line and hero title | T2 | C | P2 |
| 9 | DS2-06 What-waits copy | T2 | C | What waits |
| 10 | DS2-10 P2 word count | T2 | C | P2 |
| 11 | DS2-11, DS2-12 | T3 | C | various |

**Then:** regenerate, run `build_checks.py` and `number_checks.py` (every new number is an existing measure value),
render the FinalV3 views that changed, publish once, run `gate.py`, and take a Dutch-browser shot of P2 (only P1
was shot in Dutch).

**Cut line:** items 1–4 are the ones I'd ship even on the 16th. Items 5–10 only together, in the same publish.

## 5 · Keep, whatever else changes

- P1 as a whole. It's the best page in the round I'd expect.
- The hero as a two-lens bar table. Better than the scatter I proposed: no label collisions, keyboard-readable.
- The ledger's existence and its order (F2, F1, F4, F3).
- The capital bar and the single gate copy.
- Build your own opening on package A.
- The Night plan colour and Tangerine only for "wrong".
- The Low case shown unprompted.

## Open questions

- DS2-01 option: discounted cumulative charts instead of cash. Recommended: no, not before the submission.
- DS2-10: is about 280 words the right target for Recommended, or does Bjorn want the gate paragraph kept in full?
