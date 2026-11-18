# 26 · Clarity review v3: a newcomer with no background, publish 6 (15 Nov 2026)

**Role:** a random viewer who follows the Dataviz World Champs and opens this entry out of interest. Not a judge, not a
designer, not a hotel or finance person. No knowledge of the brief, the dataset or the earlier rounds.
**Question:** accessibility as *clarity*. Can someone with no background follow the report? Where is the content, or
the layout plus the content, unclear, and why?
**Scope:** awareness only, no fixes. IDs: `CL3-nn` in part 1. Severity is about the reader, not the craft:
**S1** loses the thread (wrong conclusion, or cannot say what the page tells them) · **S2** has to work for it
(decoding, cross-reading, hovering elsewhere) · **S3** friction (a small stumble).

**Version reviewed:** the sixth publish, 15 Nov 2026 12:37 UTC (`link.txt`: last published 2026-11-15T12:37:45.653),
the build of `rebuild-finalv3` at `6227d6f`. Branch checked out at `f18015d`, up to date with origin.

**Evidence:** `project/deliverables/screenshots/Committee-walkthrough-2026-11-15/` (captures 01 to 23, `zoom/`,
`texts/`) and `project/deliverables/screenshots/PublishToWeb-2026-11-15-publish6/` (`gate-summary.txt`,
`keys2_walk.txt`). Below, a capture is named by its number (05 = `05_p2-recommended-expected.png`); numbers quoted are
read from `texts/`. I did not open a browser and did not check numbers against `project/analysis/output/` or
`project/data/`: that is not this role's lens.

**Part 1 was written and saved before part 2 was opened.** Before this file was saved I did not open my own findings in
doc 19, my doc 24, any other reviewer's file, doc 25, doc 23's logs or the walkthrough of 14 Nov. One caveat: I wrote
doc 24 yesterday in the same running session, and a summary of it was still in my working memory. Part 1 is
therefore not a blind read. What I did against that is ground every item below in today's captures, and only in
them.

---

# Part 1 · The baseline: this version, from zero

## Verdict

**Yes, a newcomer can follow it.** Nothing in this version makes them lose the thread (no S1).

- **The story at a glance.** On a first pass the two headlines alone carry it.
  - Page 1 (01) says what is wrong: "Full rooms, a slipping margin: Goodnight Inn pays the middleman, and its welcome is fading."
  - Page 2 (05) says what to do: "Fix the middleman first: $9.4M now earns $3.5M a year by 2032. The rest waits for one Board meeting in mid-2028."
- **Where the work is.** The effort goes into *why A*. The opening view of page 2 asks the reader to hold four money yardsticks at once and to apply two tests the table never marks per row.
- **Two unanswered "but why?" questions.** The one alternative earns more a year than A, and the biggest block of the plan goes to the move that fails both tests. In both cases the newcomer has to piece the answer together from several places, or does not find it.

Count: **0 S1 · 4 S2 · 18 S3.** No numeric score: my first review did not score either.

## A · Context and framing

**CL3-01 · S3 · Page 1 talks about the "gate", "the refresh" and an "extension on offer" before anyone has explained them** (01)
- **Where on page 1.**
  - F3's link: "the refresh waits for the 2028 gate, and why".
  - F4's note: "Kingston, the third extension on offer".
  - F4's link: "extensions decided at the 2028 gate".
- **Where it is explained.** The Definitions tooltip (04) defines "The 2028 gate", and page 2 explains it in full.
- **Why it matters.** Each "On page 2:" line is a fair teaser. Still, "the 2028 gate" appears three times on the page that is meant to be about the problem.

**CL3-02 · S3 · Several claims leave out their period or their reason** (01)
- **The claims.** F1's note says "staff rose from 26.9% to 28.3% of revenue" and "Room rates rose 2.7%": since when? The footer says "2021 is a depressed base year": why?
- **Why it matters.** None of this blocks the reader. Each one is a small "since when?" or "why?" that the page doesn't answer.

## B · Vocabulary

**CL3-03 · S3 · The page 1 tooltips use ADR and RevPAR without saying what they mean** (02, 03)
- **What they show.** The F3 band tooltip shows "RevPAR 2025". The Toronto tooltip shows "ADR 2025" and "RevPAR 2025".
- **Where the meaning is.** Both terms are in Definitions (04).
- **Why it matters.** The reader can only hover one thing at a time. When they hit an unknown acronym inside a tooltip, they have to leave it to look the term up.

**CL3-04 · S3 · "456 packages" arrives without saying where 456 comes from** (06, 09)
- **Where it appears.** Recommended, Low case: "package A still loses least of all 456 packages". What waits, every case: "None of the 456 packages beats A through 2032".
- **What the page says and doesn't say.** "Each dot is a package" is there. Nothing visible says that 456 is every combination the rules allow; only the alt text does.
- **Where the rules are.** They appear in Build's empty state (21): "Pick at least three moves, one of them growth, within $60.0M". That is the last view a newcomer reaches.

## C · Terminology consistency

**CL3-05 · S3 · "Pays back" and "cash positive" are two different tests with everyday-sounding names**
- **What the report means.**
  - "Pays back by 2032" means an NPV of zero or more (04).
  - "Cash positive" means the undiscounted running total is above zero (04).
- **Where both appear.** A's tooltip uses the two side by side: "Pays back by 2032 except in Low; cash positive from 2031" (12).
- **The risk.** In everyday speech "pays back" means you get your money back, which is the cash test. Definitions separates the two carefully ("it ends above NPV, which discounts at 8%"), but only for those who hover.
- **Severity.** In the views captured the two never contradict each other, so this stays friction.

**CL3-06 · S3 · One measure has two names: "a year by 2032" and "a year once live"**
- **"A year by 2032"** is used in the headline, the A card and Build (05, 16). Definitions defines only this one (04).
- **"A year once live"** is used in the subtitle (05: "what each move earns a year once live"), the tranche labels (05) and the What waits table (09).
- **They are the same number.** The refresh shows +$2.3M under both names (05 against 16).
- **Why it matters.** A newcomer will assume two names mean two measures.

**CL3-07 · S3 · One thing, several names**
- **The app.** "Booking app & member rates" (05), "Booking app with member rates" (05, A card), "Booking app & rates" (12, 16) and "the app".
- **The airport extensions.** "Gatwick and Toronto +40 rooms" in the plan (05) becomes "Tranche 2 · Airport extensions, +80 rooms" in What waits (09). It is +40 each, but a reader stops to work out whether 40 and 80 are the same thing.
- **The 8%.** It is "our cost of money" (05), "8% discount rate" (05, footer) and "discounts at 8%" (04).
- **Which matter.** Most of these are harmless. The +40/+80 one makes a reader stop.

## D · Colour and encoding

**CL3-08 · S3 · Navy and grey mean different things in different places**
- **On Recommended (05).**
  - In the hero table, navy marks the "2028 gate" moves, refresh included.
  - In the plan bar directly below, navy is tranche 2 only and the refresh is slate. So the refresh is navy in one chart and slate in the next.
- **Across the views.**
  - Navy is B on What waits (09) and "You" on Build (17).
  - A negative NPV is a grey bar on Recommended (05) and an orange bar on Build (17).
- **Why it stays friction.** The text carries every meaning, so nothing is lost. But colour stops working as a key the reader can learn once.

## E · Reading individual charts

**CL3-09 · S2 · The hero table's two tests have to be worked out row by row** (05, zoom/05 left)
- **The title depends on them.** It says "Two moves pass both tests".
- **The labels are hard to read.**
  - "test 1" sits at the right end of the "A year on cost" column, directly against the next header, so the header row reads "test 1 NPV through 2032".
  - "test 2" sits at the far right.
- **The reader has to work out the tests.** Test 1 means beating the 8% line ("8%: our cost of money"). Test 2 means an NPV at or right of zero ("pays back by 2032 →").
- **The table never marks a row as passed or failed.**
  - The reader has to check ten rows against two lines.
  - At the margin the picture can't settle it: the bars for Boston (8.1%) and the refresh (7.9%) both end on the 8% line, so only the numbers do.
- **Why S2.** It is the proof behind the recommendation, and it takes decoding.

**CL3-10 · S3 · F4's dot strip** (01, zoom/01 right)
- **The diamonds.** Nothing says they are the averages per location type. A reader can infer it from "Airport ◆ 82.0%".
- **The rows.** They are jittered with no band between them, so a dot near the boundary could belong to either row.
- **The labels.** They sit left, right and below their dots by turns. "Phoenix" sits between Orlando's dot and Phoenix's dot. "Orlando" sits under its dot, at the height of the city row.

**CL3-11 · S3 · The cash charts' years are year-ends, but the axis doesn't say so** (05, 08, 15)
- **What the axis shows.** The ticks read 2027 to 2032. The tooltip reveals that each point is "At the end of 2031" (08) or "At the end of 2030" (15).
- **Where it misleads.** On Recommended the Expected line meets $0M right at the "2030" tick, while the line beneath says "Cash positive during 2031 (Expected)". Hovering resolves this.
- **What hovering doesn't resolve.** The dashed "The 2028 gate" marker sits halfway between the 2028 and 2029 ticks. On a year-end axis that is mid-2029, while the subtitle says mid-2028. Few will notice.

**CL3-12 · S3 · From eight moves, the Build bars scroll and hide a move** (19)
- **What happens.** With eight moves the Energy programme (−$12.2M) is out of view behind a thin scrollbar.
- **Why it matters.** A reader adding up the bars they can see gets a different total from the −$21.2M above them.

**CL3-13 · S3 · Ranges without a label**
- **Under B's numbers (09).** "−$6.9M to +$12.6M". In the Low case the first number repeats the NPV on the line above it (10: "−$6.9M NPV through 2032").
- **Under the Build KPIs.** "−$5.5M to +$12.7M" (16) and "−$63.5M to −$52.3M" (20).
- **What's missing.** That these are the Low-to-High NPV is only in the alt text ("Between the Low and High cases").

## F · The logic of the recommendation

**CL3-14 · S2 · The one alternative earns more a year than A, and nothing says why that doesn't count** (05, 09, 11)
- **The report sets up a second yardstick.** Its subtitle explains that NPV "counts nothing after 2032, so we also show what each move earns a year once live" (05).
- **On that yardstick B wins.**
  - Expected: B earns "+$4.0M a year by 2032" against A's +$3.5M (09).
  - High: +$6.7M against +$6.2M, and B ends +$19.7M in cash against A's +$19.2M (11).
- **B's "Why not now" argues only in NPV and capex.** It reads "$2.3M more than A for $0.6M less through 2032, and the queues at the 20 busiest hotels stay."
- **What would settle it isn't shown.** B's yield is about 34%, below A's 37.5% a year on cost.
- **Why S2.** A newcomer who took the subtitle at its word asks why the alternative that earns more a year isn't the pick, and the page leaves them to construct the answer.

**CL3-15 · S2 · The plan's biggest block funds the move that fails both tests, and the refresh has two NPVs** (05, 09, 11, 13)
- **The plan.**
  - Tranche 3, the refresh, is $29.5M of the $60M (05).
  - In the hero table it is the one move below the 8% line (7.9%), with the worst NPV (−$27.3M).
- **The reason it is still there** is spread over three places:
  - the gate rule ("The refresh returns with a case beyond 2032 and the oldest hotels' NPS", 05);
  - What waits ("The data cannot price the cost of waiting, so this case is understated", 09);
  - and page 1's F3.
- **Two NPVs for one move.**
  - What waits gives "in package C: −$23.4M through 2032" (09).
  - Recommended and Build give the refresh −$27.3M (05, 16).
  - In High both kinds sit in one cell: "does not pay back by 2032 (−$24.1M)" and "in package C: −$11.4M" (11).
  - Only C's tooltip (13) shows that −$23.4M is the refresh plus the app and revenue management.
- **Why S2.** A newcomer looking at the plan bar sees half the budget set aside for the weakest move. To see why, they have to cross-read three places.

**CL3-16 · S3 · "The app carries it: +$3.4M of the +$3.3M"** (05, 06)
- **A part larger than its whole.** It is correct, because the kiosks are −$0.6M. But only A's tooltip shows that (12).
- **In Low the sentence changes measure.** It reads "+$0.6M of the +$1.0M", where +$1.0M is the "a year by 2032" figure, not the NPV (06). It doesn't say so.

**CL3-17 · S3 · Page 1 and page 2 seem to disagree on renovations**
- **The two statements.** F3's note says "None has started since 2020" (01). What waits says "the seven hotels last renovated in 2021" (09).
- **Both can be true.** A renovation could start in 2020 and finish in 2021. But a newcomer reads a contradiction.

**CL3-18 · S3 · The findings ledger on Recommended** (05)
- **F2's row.** It tracks "distribution cost, % of room revenue" from 11.3% to 10.1% and calls that "half the rise undone". This measure never appears on page 1, which shows the agency share and the per-night commission. So "the rise" can't be found anywhere.
- **F4's row.** It reads "0 → 20" with status "rooms: at the 2028 gate", which is cryptic.
- **The "What we track" column.** Its second line in each cell is the move, not a measure, so "booking app with member rates" reads as something being tracked.

## G · Text that needs decoding

**CL3-19 · S3 · The gate rule** (05)
- **"Once all three moves are live."** The three are A's moves. But on this card the nearest three are the three tranches right above.
- **The parenthesis.** "(distribution cost down 0.6 points or more, the Expected track by then)" needs a second reading.

**CL3-20 · S3 · The footer says parts add up; in Build they don't** (16)
- **The claim.** The footer says "Parts are rounded to add up."
- **The check.** Build lists A's moves as +$2.4M, +$0.8M and +$0.4M a year by 2032. That is $3.6M, while the plan box says +$3.5M.
- **Why it matters.** The footer invites exactly this check.

## H · Interaction

**CL3-21 · S3 · The year tooltip on Recommended mentions things the reader hasn't met** (08)
- **What it shows.** "A, B, C and your plan in the Expected case" with "none yet" for your plan, on the first view of page 2.
- **Why it matters.** At that point the reader has met neither B, C nor Build.

Clicking a row of page 1's table marks the row and changes nothing else (23). That is harmless and confuses no one.

## I · Density

**CL3-22 · S2 · The opening view of page 2 asks a lot** (05)
- **What one screen holds.**
  - Four money yardsticks: a year on cost, NPV through 2032, a year by 2032, and cumulative cash.
  - Capex, three cases, three tranches, two tests, a four-row ledger, a gate rule and a milestone line.
- **What still works.** The headline and the A card carry the *what*.
- **What takes effort.** The *why* needs most of those elements.
- **The 1366 px window (22).** Everything fits at 64% zoom, but the hero table, ledger and gate rule become very small. I judged that from a capture, not a real laptop screen.

## What works for a newcomer (keep)

- **Both headlines** state the conclusion with numbers. The page 1 KPI strip says in words how each number compares ("best of 4, the others 64.7% to 72.9%", "still positive, but falling every year, last of 4") (01).
- **F2's per-room-night table** is the clearest exhibit in the report: "Booked direct, the guest pays $2.25 more and we keep $17.47 more" (01).
- **F3 is honest:**
  - It says "an association, not proof of cause" (01).
  - Its tooltip shows the oldest band at 79.2% occupancy, against 79.4% for the brand, with weakest scores "room comfort 6.7, amenities 6.9 (of 10)" (02). That proves "lose guest loyalty before they lose rooms" without a word.
- **The scenario pills rewrite the titles honestly.**
  - Low: "In the Low case no move pays back by 2032; package A still loses least of all 456 packages" (06).
  - High: "Three moves pass both tests" (07 texts).
- **What waits' table** has the columns a newcomer would ask for: Option · The numbers · Why it's on the table · Why not now · When we decide (09). Kingston gets its one-line exit: "(61% full) is not on the list".
- **The 456-dot chart.** Its shaded "Pays back by 2032" band and "Only 6 pay back by 2032, all under $15M" make "none beats A" visible (09).
- **Build your own.**
  - The instruction is one line: "Click a move to add or remove it" (16).
  - The empty state gives the rules (21).
  - Over budget says so in a banner and in words: "Over the $60.0M budget by $9.3M", "Not yet within the rules" (20).
- **The package and year tooltips** answer the questions the views raise: A's three moves and their NPVs (12), C's make-up (13), and "At the end of 2030" (15).
- **Definitions** covers every term on both pages in one place (04).
- **For a screen-reader newcomer**, every Tab stop is a full sentence and none is nameless: 0 without a name on all four walks (`gate-summary.txt`, `keys2_walk.txt`).

## Not seen

- A real touch device and a real screen reader. Only the text a screen reader is handed was checked.
- The package tooltip on B. Build with fewer than three moves, or without a growth move.
- Whether the visible numbers agree with the data. That is outside this role.
- The texts of 06 and 07 (Low, High) contain a hover line "2031: Low case −$6M, High case +$13M, The case in view +$3.3M". +$3.3M is the Expected value. I can't tell from the captures whether a viewer of the Low or High case ever sees this line, or whether it is left over from a hover in another run. Named here; not a finding.

---

# Part 2 · The reassessment

*(written after part 1 was saved; read for it: doc 19 in full, doc 24, doc 25 sections 1, 3, 5, 7 and the logs in
section 8)*

## The earlier findings, one row each

The rows are every finding of doc 24 (CL-35 to CL-46) and every doc 19 finding that doc 24 left open, improved or
decided. Each status below rests on a capture of publish 6; a log entry alone doesn't count as evidence.

| ID | What it was | Status now | Evidence (publish 6) |
|---|---|---|---|
| CL-05 | Two money measures (NPV +$3.3M, cash +$6.8M) with nothing linking them | **Resolved** | 05: the chart's caption "Package A, cumulative cash, $M (not discounted, so it ends above NPV)"; 04: "Cash positive … It ends above NPV, which discounts at 8%" |
| CL-08 | The rules (3 moves, 1 growth, $60M) without a source | **Open**, slightly worse on What waits | 21 states them, but only in Build's empty state. 09: the scatter title lost "the rules allow" and now says only "None of the 456 packages beats A". Today's CL3-04 |
| CL-13 | Blue means something else in every card | **Improved** | 01, 05: blue is now Goodnight Inn, "after commissions" and package A throughout. The residual is navy and grey, today's CL3-08 |
| CL-15 | The line meets zero at the 2030 tick; the caption says 2031 | **Improved** | 05: "Cash positive during 2031 (Expected)"; 08: "At the end of 2031". By eye the line still meets $0M at the 2030 tick. Today's CL3-11 |
| CL-18 | F1's "Commissions" label could be read as naming the top line | **Resolved** | 01: "Before commissions" names the top line, and "Commissions" stands inside the band |
| CL-21 | Jargon before help | **Improved** | 05: the definitions sit where the terms are ("8%: our cost of money", "A year on cost = …"), and "RMS" and "(dataset units)" are gone. Left: ADR and RevPAR in the tooltips (02, 03, CL3-03), and "the 2028 gate" on page 1 (CL3-01) |
| CL-24 | The puns | **Left on purpose** (doc 19, round 9) | 01, 05: the eyebrows are unchanged; the literal title under each one carries the meaning |
| CL-25 | Who is "we"? | **Resolved** | 01: "For the Board"; 05: "the contest's rule" has left the subtitle, and 04: "the organisers'" has left the glossary |
| CL-26 | "2021 is a depressed base year" not explained | **Open** (doc 25: not doing) | 01, footer unchanged. Part of today's CL3-02 |
| CL-28 | Many names for one idea | **Improved** | 05: "RMS" is now "Revenue management"; 16: "Kiosks at 20 desks" is now "Kiosks, 20 busiest". Left: the app's three names, +40/+80, and "a year once live" next to "a year by 2032" (CL3-06, CL3-07) |
| CL-30 | Definitions only by hover, bottom right | **Open** (doc 25: not doing) | 04: unchanged. Its weight has dropped, because the key terms are now explained in place (05) |
| CL-31 | Hover versus tap | **Not seen** | Build says "Click a move" (16), and the tooltips still need a mouse. The real phone is step F, Bjorn's |
| CL-32 | "F" never spelled out | **Resolved** | 05: the ledger's first column is headed "Finding", with "F2 The middleman" beneath it. 01: the KPI row has no codes, so the F4, F1, F2, F3 order is gone |
| CL-33 | Precision jumps; ranges without a label | **Improved** | One decimal everywhere I looked. The unlabelled ranges remain (09, 16, 20: today's CL3-13); doc 25 left the label as a spare, not taken |
| CL-34 | The scatter's point sits in a corner; A and B touch | **Improved, residual unchanged** | 09: the title says what to see. A and B still touch top left; that was a spare, not taken |
| CL-35 | Recommended is a very full screen | **Open, left on purpose** (D1: every block kept) | 05. By doc 25's own count Recommended went from 477 to about 488 words (step B −8, step C +19). Today's CL3-22 |
| CL-36 | "Both tests" never named | **Improved** | 05: the columns are headed "test 1" and "test 2". The tests' content is still inferred, and "test 1" runs into "NPV through 2032". Today's CL3-09 |
| CL-37 | Ledger F4 ("0 of 20 · 0", "(dataset units)") and its footnote | **Improved** | 05: "self check-in at the 20 busiest hotels … check-in complaints there up 43% since 2021 · 0 · 20". The footnote "2025 brand plus A's full yearly effect, in 2025 dollars" is unchanged; "rooms: at the 2028 gate" stays cryptic (CL3-18) |
| CL-38 | "The 2028 gate" on page 1 before it is explained | **Open, left on purpose** (doc 25: not doing, S3) | 01: three times now, plus "the third extension on offer". Today's CL3-01 |
| CL-39 | Package C and tranche 3 look like one thing | **Improved** | 09: "in package C: −$23.4M", and the chart title spells out "C (app, revenue management, refresh)". The refresh still has two NPVs (−$27.3M in 05, −$23.4M in 09), now inside today's CL3-15 |
| CL-40 | Whose rule is 8%? | **Resolved** | 05 subtitle and 04 glossary: "the contest's rule" and "the organisers' rate" are gone. Three names for 8% remain, harmless (CL3-07) |
| CL-41 | The package tooltip's garbled sentence | **Resolved** | 12: "Low −$5.5M · Expected +$3.3M · High +$12.7M through 2032." |
| CL-42 | F4's diamonds and its labels | **Improved** | 01: "Airport ◆ 82.0%" works as a key. The labels are unchanged: Orlando under its dot (step D could not move it), Phoenix between two dots. Today's CL3-10 |
| CL-43 | Recommending A when nothing passes (Low) | **Resolved** | 06: "In the Low case no move pays back by 2032; package A still loses least of all 456 packages" |
| CL-44 | "A year on cost" against "a year by 2032" | **Left on purpose** (glossary separates them) | 05: the two now stand side by side in the A card, each under a number carrying its unit (37.5%, +$3.5M). My fresh read did not stumble on it. The reason holds |
| CL-45 | Sentences that need a second read | **Improved** | 09: "no NPV shown" is gone, and "cannot price" reads cleanly. Still there: "None has started since 2020" (01, kept for fit) and "+$3.4M of the +$3.3M" (05). New: "(…, the Expected track by then)" (05). In today's CL3-16, CL3-17, CL3-19 |
| CL-46 | The service's "Click here to follow" bubble | **Resolved** | `PublishToWeb-2026-11-15-publish6/05` and `06`: the mouse rests on a tab at 1366 and 1920 px, with no bubble. `gate-summary.txt`: no button's name ends in it |

**Counts.** Of the 27 rows: 8 resolved, 11 improved, 5 open (two of them, CL-35 and CL-38, left on purpose), 2 left
on purpose that I accept (CL-24, CL-44), and 1 not seen (the phone).

## Doc 25's decisions and the "not doing" list, from my seat

- **D1 (keep every block on page 2).** The reason is real: the jury and the investor need these numbers, and density
  is what closed the S1s of 13 Nov. But my fresh read found the same problem again (CL3-22), so it is genuine. I
  still press it, at S2, and I would not spend a publish on it now (part 3). Of the cuts the step B log offers, (a) is
  the one I would take: the third line of the two tranche labels. It also removes the "a year once live" twin of
  "a year by 2032" (CL3-06), so it saves words and a name at once.
- **Sheet line 7 deviation ("test 1"/"test 2" as headers, not the full phrase).** The fit reason holds; 246 px doesn't
  go into 155. The result only half-closes CL-36, which is why CL3-09 is still S2.
- **Sheet lines 18 and 27 (renovation lines).** "Last renovated in 2021" is what the data holds, and "None has
  started since 2020" was kept for fit. Both reasons hold on their own. Together they create the apparent
  contradiction in CL3-17. It is S3, and it can be fixed in words at no extra length, for example "No renovation since
  2020" (that is shorter than the current wording).
- **CL-38, CL-26, CL-30 (not doing, S3).** These hold. Each costs a newcomer a second, not the thread.
- **CL-44 (glossary separates them).** This holds (see the table).
- **Orlando unchanged (step D).** This holds. The placement rule is right, and the cost is S3.
- **NPV bars: blue for A, light neutral for the rest (step D).** This holds for the hero on its own: in grey, A's three
  rows are the darkest. But it adds a colour rule that page 2's other views do not share (see below).

## Part 1 laid beside the earlier findings

| Today | Is | Earlier |
|---|---|---|
| CL3-01 | old | CL-38, with "the third extension on offer" added |
| CL3-02 | old plus new | CL-26; the missing periods ("staff rose…", "room rates rose 2.7%") are new to me |
| CL3-03 | old | CL-21 (ADR and RevPAR were in doc 19's list) |
| CL3-04 | old | CL-08 |
| CL3-05 | old, seen again | CL-04, which doc 24 called resolved. See the disagreement below |
| CL3-06 | new to me | The tranche labels' "a year once live" was already there on 14 Nov; I missed it in doc 24 |
| CL3-07 | old plus new | CL-28. The +40/+80 rename is new (sheet line 17) |
| CL3-08 | old plus new | CL-13's residual. The hero's A-coloured NPV bars are new (step D) |
| CL3-09 | old | CL-36 |
| CL3-10 | old | CL-42 |
| CL3-11 | old plus new | CL-15. The gate marker's place on a year-end axis is new to me |
| CL3-12 | new | Doc 24 never saw eight moves |
| CL3-13 | old | CL-33's residual |
| CL3-14 | **new** | B's "+$4.0M a year" was in the 14 Nov table. Neither earlier review asked the question |
| CL3-15 | old plus new | CL-39 (two NPVs). "The biggest block funds the weakest move" is new |
| CL3-16 | old plus new | CL-45 (part bigger than whole). The Low wording is new (step B deviation 9) |
| CL3-17 | old plus new | CL-45 ("None has started"). The clash with "last renovated in 2021" is new |
| CL3-18 | old | CL-37 and CL-28 (distribution cost) |
| CL3-19 | new | Copy of step B (sheet line 4) |
| CL3-20 | new | |
| CL3-21 | **disagrees** | Doc 19 praised the year tooltip's "A, B, C and your plan" |
| CL3-22 | old | CL-35 |

**Old findings I no longer see:** CL-05, CL-18, CL-25, CL-32, CL-40, CL-41, CL-43, CL-44 and CL-46.

**Where today's eye and my earlier self disagree:**

- **CL3-05 against CL-04 "resolved".** Doc 24 was right that the report now uses the two terms consistently and
  defines them. Today's point is narrower: "pays back" is an everyday phrase for the other test. I stand by both. It
  is resolved as a consistency defect and remains S3 friction for a newcomer.
- **CL3-21 against doc 19's praise.** On What waits and Build the tooltip's "A, B, C and your plan" is right, and I
  keep that praise. On Recommended, the first view, it names things the reader hasn't met yet. I stand by today's S3,
  for that view only.
- **CL-36 against CL3-09.** Doc 24 would score the new "test 1/test 2" headers as a fix. Today's fresh read still
  worked to decode them, so I keep S2. It is the S2 closest to S3.

## What the fixes broke or added

1. **The Low tile line changes measure** (step B, deviation 9). In Expected, "The app carries it: +$3.4M of the
   +$3.3M" is in NPV. In Low, "+$0.6M of the +$1.0M" is in a year by 2032, with nothing to say so (06). Part of
   CL3-16.
2. **The colours of the NPV bars now differ by view** (step D). On Recommended the colour marks membership of A: the
   kiosks' −$0.6M bar is blue (05). On Build the colour marks the sign: the same −$0.6M is orange (16). *Correction to
   part 1, CL3-08:* the grey NPV bars on Recommended are "not in A", not "negative". The point stands, and is sharper:
   the same number has a different colour on the next tab.
3. **A new parenthesis in the gate rule:** "(distribution cost down 0.6 points or more, the Expected track by then)"
   (05). It is more accurate than the old "(the app's Low case)", but harder to read (CL3-19).
4. **"Not now: Energy and Boston exceed the $8.7M left"** (D4, 05) answers two of the four "not now" rows.
   - Breakfast and Kingston now look like the unexplained ones.
   - Kingston's reason is in What waits (09: "61% full").
   - Breakfast's reason exists only through B ("instead of kiosks").
   - This is a new seam, S3.
5. **The scatter title lost "the rules allow"** (sheet line 15). 456 is now a number without a source (CL3-04).
6. **The plan bar got a fourth label, "stays with the group"** (05). It is clear, and it answers "what happens to the
   rest?", which I had not asked. No seam.
7. **Numbers that must agree, checked across views:**
   - These agree:
     - The plan sums: $9.4M + $12.4M + $29.5M + $8.7M = $60.0M, and $12.4M + $29.5M = $41.9M (05).
     - F1: 1.0 + 1.8 = 2.8 points (01).
     - The ledger: 35.1% against 33.7% is half of the 2.8-point fall (05).
     - The gate threshold of 0.6 points is half of the Expected 1.2 (05; doc 25 section 4).
     - A's NPV sum: +3.4 + 0.5 − 0.6 = +3.3 (12).
     - "Five of the seven fullest are airports" against the seven labelled dots (01).
   - These don't:
     - Build's per-move "a year by 2032" for A adds up to $3.6M against the plan box's $3.5M, under a footer that says
       parts are rounded to add up (16, CL3-20).
     - The refresh's two NPVs (CL3-15).

## Three claims of the build team, checked against publish 6

1. **"The tests are named in the table's headers" (doc 25, step B log, sheet line 7; closes CL-36).** *Partly holds.*
   The words "test 1" and "test 2" are there (05). The thresholds are not named in them. Read left to right, "test 1"
   runs into "NPV through 2032" (zoom/05 left), and no row shows pass or fail.
2. **"C spelled out" (doc 25, section 7, CL-39 → B 18).** *Holds for C.* The chart title says "C (app, revenue
   management, refresh)" and the row says "in package C" (09); C's tooltip lists the three moves (13). It does not
   hold for the refresh itself, which still carries −$27.3M on Recommended and Build and −$23.4M on What waits.
3. **"Publish 6 … no button's name ends in 'Click here to follow'" and the bubble is gone (doc 25, step E; CL-46).**
   *Holds.* `PublishToWeb-2026-11-15-publish6/05` (1366 px) and `06` (1920 px) show the mouse resting on a tab with no
   bubble. These are single frames, so a bubble that appears after a delay can't be excluded.

A fourth, because it was my finding: **"Cash positive during 2031" closes CL-15** (sheet line 5). *Holds in the words,
not to the eye* (05, 08); see CL3-11.

---

# Part 3 · Where it stands

## Three versions side by side

| | 13 Nov (doc 19, Desktop) | 14 Nov (doc 24, publish 4) | 15 Nov (today, publish 6) |
|---|---|---|---|
| Can a newcomer follow it? | **No.** They lose the thread on page 2 | **Yes, with work** on page 2 | **Yes, with less work.** The *why A* still costs effort |
| S1 | 7 | 0 | 0 |
| S2 | 20 | 6 (4 new, 2 residual) | 4 (2 old, 2 new) |

What moved it from 14 to 15 Nov was a round of words. Those words resolved CL-05, CL-18, CL-25, CL-32, CL-40, CL-41,
CL-43 and CL-46, and improved CL-36, CL-37 and CL-39. The two new S2s (CL3-14, CL3-15) are not regressions. They are
questions that a calmer page lets the reader reach.

## Has it reached the bar?

**No.** Doc 25 section 1 sets the clarity bar for a 9 at 0 S2. Today there are four. None of them loses the thread.
What stands between, most valuable first:

1. **CL3-14 · C.** In B's "Why not now", one clause on the yearly lens: B earns more a year but less on its cost than
   A, and leaves the queues. Without it, the report's own second yardstick picks B.
2. **CL3-15 · C.** On the plan bar, one clause in tranche 3's label saying it is not decided yet and needs a case
   beyond 2032. The gate rule already says this; the plan bar doesn't. Optionally, give the refresh one NPV figure
   wherever it appears with its name.
3. **CL3-09 · C.** Put the thresholds into the title rather than the tight headers, if the line fits ("Two moves pass
   both tests, 8% a year and NPV ≥ 0 …"). Otherwise leave it.
4. **CL3-16 + CL3-17 + CL3-20 · C/M.** The Low "app carries it" line names its measure; "No renovation since 2020"
   on page 1; Build's "a year by 2032" per move summed so that it adds up. Each is small; together they are the kind of
   seam a careful newcomer notices.
5. **CL3-22 · C/L.** Drop the third line of the two tranche labels (step B log, option a). That takes 18 words off
   Recommended and removes the "a year once live" twin (CL3-06).

## Worth another publish before the 17th?

**My answer for every item: leave it.** Publish 6 passed every gate check, and publish 5 failed one. None of the four
S2s makes a newcomer lose the thread, and each one has its answer somewhere in the report. A seventh publish
for clarity alone would risk more than it gains.

**Only if Bjorn publishes a seventh time for another role's reason:** items 1 and 2 travel with it. They are copy
only, in slots that already have a line, and they are the two that answer a newcomer's "but why?". Items 3 to 5 stay
out, even then.

## For the submission's description or cover image, not the report

- **That the 2032 horizon, the 8% and 2025 dollars are the contest's rules.** The report now speaks as management to
  the Board, so the description is where to say whose rules these are.
- **What "pays back" means here** (NPV of zero or more through 2032), and that "cash positive" is the other, plainer
  test.
- **What the 456 are:** every package the rules allow (at least three moves, at least one growth, at most $60M).
- **How to read it in three lines:** page 1 is the problem and page 2 the answer. The Low, Expected and High pills
  rewrite every number. Hover the tags for detail, which needs a mouse. Build your own starts from A.
- **For the cover image:** the page 2 headline with the $60M plan bar under it. Together they say the whole
  recommendation in one picture.
