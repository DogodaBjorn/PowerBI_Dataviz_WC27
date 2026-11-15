# 26 · Dataviz and storytelling review v3: the sixth publish (15 Nov 2026)

**Role:** the dataviz and data-storytelling consultant hired for a last check before submission. I am not the jury
and this is not a build review. **Question (from doc 19, unchanged):** does the report tell one story? Does every
chart earn its place in that story? Where does the data offer a better story than the one on the canvas?
**Version reviewed:** the sixth Publish to Web publish, 15 Nov 2026 12:37 UTC. This is branch `rebuild-finalv3` at
`6227d6f`, the version that will be submitted.
**Evidence:**
- `project/deliverables/screenshots/Committee-walkthrough-2026-11-15/`: captures 01–23, `zoom/`, and `texts/` (every
  number quoted below is read from there).
- `../PublishToWeb-2026-11-15-publish6/`: `gate-summary.txt` and `keys2_walk.txt`.
- One data check of my own in `project/data/PillowKey_Dataset.xlsx` (Renovations sheet, see DS3-14).
- I had no browser and no link, so I saw nothing live.

**Order of work:** Part 1 was written and saved before Part 2's sources were opened: doc 19 beyond its top, doc 24
and doc 25. One caveat in fairness: I wrote docs 19 and 24 myself in this same working session, and I still carry a
summary of them. I judged every view below from the captures alone. Where my memory and a capture could disagree, the
capture decides.

**Item IDs:** `DS3-nn`. **Severity:** **High** = a judge or investor can stumble on it in the first three minutes;
**Medium** = it costs trust or a second read; **Low** = polish. The fix type comes in Part 3.

---

## Part 1 · The baseline: this report, read as if for the first time

### 1.1 Verdict on this version alone

The report tells one story, and tells it well. Page 1 says what is wrong in one headline: "Full rooms, a slipping
margin: Goodnight Inn pays the middleman, and its welcome is fading." Four numbered findings follow, and each one ends
by pointing to page 2 ("On page 2: …"). Page 2 opens with the answer, "Fix the middleman first: $9.4M now earns
$3.5M a year by 2032." Below it sit:
- a ranked table of all ten moves on two tests;
- a recommendation tile that says what package A does to each finding;
- a capital plan with one decision rule;
- a scatter of all 456 legal packages that proves none beats A through 2032.

Low and High do not just swap numbers. The words change too: "In the Low case no move pays back by 2032; package A
still loses least of all 456 packages". That is rare and it is the right instinct.

What keeps it short of the top band is reading work, not story structure:
- two cryptic column labels ("test 1", "test 2");
- a sentence where a part is bigger than its whole;
- price ranges with no label;
- one rival (package B) that beats A on the page's own second lens without the page saying so;
- a time axis whose ticks mean year-ends while one marker on it assumes year-starts.

None of these needs a new chart. Most are words.

**Would I put my name to it as is?** Yes. **Is it a 9.5?** Not yet. It is a confident 8.5–9, and the gap is a
handful of sentences.

### 1.2 Scores (0–10, the same overall scale as doc 19)

| Criterion | Score | Why |
|---|---|---|
| One story spine, page 1 → page 2 | 9.0 | Headline → four findings → "On page 2" lines → the answer → ledger → plan → gate. The only weak joint is F4 → the kiosks (DS3-05). |
| Each chart earns its place | 9.0 | The F1 wedge, the F2 line plus the room-night table, the F3 diverging bars, the F4 strip plot, the hero bar table, the 456-package scatter and the cash lines all carry a claim their title states. Nothing decorative. |
| The data's best stories are used | 9.0 | The margin split (1.0 commissions, 1.8 running costs), the $17.47 kept per direct night, the 20 fullest hotels, the 456 packages and the honest Low case are all there. One is missing: B's lead on yearly profit (DS3-03). |
| Words and number grammar | 8.0 | The titles are claims and the claims are true. Several reader-stoppers remain: "test 1/test 2", unlabelled ranges, "+$3.4M of the +$3.3M". Recommended carries about 640 visible words and figures. |
| Colour and encoding | 8.5 | Blue means A everywhere and orange means worse or negative everywhere. Two small mismatches: tranche 3's colour, and the F4 type markers. |
| Hover adds depth, never meaning | 9.0 | Every tooltip deepens a claim already on the canvas: the F3 band, the F4 hotel, the package, the year, the glossary. Nothing essential hides behind hover. |
| Trust: numbers agree, periods stated, terms defined | 8.0 | The glossary is complete and the scenario words adapt. One timing disagreement sits inside the cash chart (DS3-04). Two numbers lack an anchor (DS3-06, DS3-11). |
| **Overall** | **8.6** | A finished story with a reading tax. |

### 1.3 Page 1, The Brand Review (`01`, `zoom/01_*`, `texts/01`, tooltips `02`–`04`, click `23`)

- **Masthead and KPI row: right.** Each KPI has a context line in the colour of its direction: "best of 4, the others
  64.7% to 72.9%" and "still positive, but falling every year, last of 4". The NPS label carries its scale
  ("(−100 to +100)").
- **F1, the margin: right.** The wedge between "Before commissions" and "After commissions" is labelled
  "Commissions". The note splits the 2.8-point fall into 1.0 for commissions and 1.8 for running costs, and rules out
  price. One gap: "Room rates rose 2.7%" has no period (DS3-12).
- **F2, the middleman: the best device in the report.** The room-night table makes the claim in three rows: an agency
  guest pays $109.31 and the inn keeps $89.63; a direct guest pays $111.56 and the inn keeps $107.10. "Nothing rewards
  the guest for booking direct; member rates change that." That sentence sets up page 2's lead move better than any
  chart could. Small seams (DS3-13):
  - the "27%" end label sits on top of the "2025" axis label;
  - the card says both "we keep" and "Goodnight Inn keeps".
- **F3, the fading welcome: right.** The diverging bars put only the oldest band in orange (−4.9). The note says
  "an association, not proof of cause". The tooltip (`02`) adds occupancy, RevPAR, the NPS trend and the weakest guest
  scores: depth, not meaning. "44 of 50 hotels; 6 have no renovation date." sits 20 px under the band labels and reads
  like a fourth label (DS3-13).
- **F4, where we are full: the chart is right, the bridge is thin.** See DS3-05. The strip plot of 50 hotels with
  the seven fullest named works, and so does the 90% line. "Kingston, the third extension on offer, in none" is a
  strong sentence. The type averages (◆) sit in the dot rows and look like hotels; the left-hand legend rescues them
  (DS3-15). The Toronto tooltip (`03`) is right.
- **Definitions (`04`): right and complete.** It defines "Cash positive … ends above NPV, which discounts at 8%",
  which is exactly the bridge between the two money lenses.
- **Clicked row (`23`):** Power BI marks the row and nothing else moves. Harmless.

### 1.4 Page 2, Recommended (`05`–`08`, `zoom/05_*`, `texts/05`–`07`, `22`)

- **Headline and subtitle: right.** "NPV counts nothing after 2032, so we also show what each move earns a year once
  live" tells the reader why there are two lenses before they meet them.
- **The hero table: right in structure, cryptic in its labels.** Ten moves are ranked by "A year on cost" against an
  8% line, with "NPV through 2032" beside it, and the title names the outcome: "Two moves pass both tests; the kiosks
  earn 20.6% a year on cost but pay back after 2032". The tests themselves are named only by two floating captions
  above the header ("8%: our cost of money", "pays back by 2032 →"). The columns say "test 1" and "test 2". A fresh
  reader needs a few seconds to decode which test is which (DS3-07). The "not now" rows raise a question this view
  never answers (DS3-02).
- **The recommendation tile: the right content, one bad sentence.** "$9.4M capex · +$3.3M NPV through 2032 · +$3.5M
  a year by 2032 · 37.5% a year on cost", then the worst case, then the ledger. The ledger's statuses adapt by case:
  "half the rise undone" in Expected, "a quarter of the rise undone" in Low, "three quarters…" in High. Good writing.
  The bad sentence and the lens switch are DS3-01. The F2 row's metric has no anchor on page 1 (DS3-06).
- **The capital plan: right.** The plan reads in one line: "$9.4M now, $41.9M at the 2028 gate, $8.7M not needed".
  The tranche labels carry yearly profit and a year on cost. The gate rule is concrete: "distribution cost down 0.6
  points or more … Gatwick and Toronto topped 90% in 6 of the last 12 months", and it ends "A rule, not a forecast."
- **The cash chart: right idea, one timing seam.** See DS3-04.
- **Low (`06`) and High (`07`): right.** The titles, the tile's other-case line and the ledger statuses all follow the
  case. "+$0.03M" for the kiosks in High breaks the one-decimal grammar (DS3-13).
- **The 1366 px window (`22`):** the page fits, with body text at about 8 px. That works for a judge on a laptop who
  zooms, and is not great for one who doesn't. This is Power BI's fit-to-page, not a design fault. I note it and do
  not score it.

### 1.5 Page 2, What waits, and why (`09`–`15`, `zoom/09_*`, `texts/09`–`11`)

- **The 456-package scatter: the strongest chart on page 2.** "None of the 456 packages beats A through 2032. Only 6
  pay back by 2032, all under $15M." A, B and C are lettered discs and the pay-back zone is shaded. The subtitle adapts
  ("None pays back by 2032" in Low, "Only 57 … all under $35M" in High). The package tooltips (`12`–`14`) list the
  moves with their capex and NPV. A grey dot's tooltip (`14`) is as complete as A's.
- **The table: right in form.** Its columns are Option · The numbers · Why it's on the table · Why not now · When we
  decide. The writing is honest: "The data cannot price the cost of waiting, so this case is understated."
  Three issues:
  - B's yearly profit beats A's and the table doesn't say so (DS3-03).
  - The ranges have no label (DS3-08).
  - Two renovation sentences seem to contradict each other (DS3-14).
- **The cash chart: right idea, wrong label position.** See DS3-09. The year tooltip (`15`) fixes the convention: the
  "2030" tick is "At the end of 2030".

### 1.6 Page 2, Build your own (`16`–`21`, `zoom/16_*`, `texts/16`–`21`)

- **Right, and it now invites play.**
  - It opens with A ticked, so the "You" dot sits on A.
  - Adding moves moves the dot and the tile, and retitles the cash chart: "yours ends behind A by $6.4M in 2032, cash
    positive from 2032".
  - The rules are stated ("Within the rules: 6 moves, 5 growth, $26.1M of $60.0M").
  - Over budget is unmissable: the orange banner "Over the $60.0M budget by $9.3M" and an orange line.
  - The empty state says what to do.
- **A lesson left unsaid (DS3-10).** The six-move plan earns more a year (+$6.1M against +$3.5M) yet loses by 2032
  (−$5.1M NPV against +$3.3M). That is the second lens's whole argument, and the view shows both numbers without
  saying it.
- The tile's bars scroll from eight moves on (`19`). The scrollbar is visible, so this is acceptable.

### 1.7 Findings

| ID | Where | What I see | Why it matters | Severity |
|---|---|---|---|---|
| DS3-01 | `05`, `06`, `07`, tile | "The app carries it: +$3.4M of the +$3.3M." A part bigger than its whole reads as an error until you work out that the kiosks are negative. In Low the same sentence switches lens without saying so: "+$0.6M of the +$1.0M" is a year, not NPV. | It is the one sentence that sells the lead move, and a fresh reader stumbles on it. | High |
| DS3-02 | `05`, `07`, hero | The Breakfast upgrade is fourth by a year on cost (19.8%) and "not now". In High the hero title names it ("the breakfast upgrade earns 26.4% a year on cost but pays back after 2032"). Kingston is "not now" too. The footnote explains only Energy and Boston. The answer exists, but on another view (the B row of What waits). | The hero raises a question it never answers. An investor asks "why not breakfast?" and gets silence. | Medium |
| DS3-03 | `09`, `10`, `11`, B row | B ("Breakfast instead of kiosks") earns "+$4.0M a year by 2032" against A's +$3.5M (Expected), and +$6.7M against +$6.2M (High). The "Why not now" cell cites only NPV and the queues. B's a year on cost (4.0 ÷ 11.7 ≈ 34%) is below A's 37.5%. That is the honest reason, and it is unsaid. | The page promises a second lens and then stays silent where that lens favours the rival. A sharp judge finds it in a minute, and silence reads as hiding. | Medium–High |
| DS3-04 | `05`–`08`, `15`, cash chart | The tooltips say a tick is a year-end ("At the end of 2030": Expected −$0.2M). The caption says "Cash positive during 2031 (Expected)". But the eye reads the line crossing zero at the "2030" tick. The dashed "The 2028 gate" marker sits halfway between the 2028 and 2029 ticks. On a year-end axis that is mid-2029, not mid-2028. | Two elements of one chart assume different calendars, and either reading makes one of them wrong. Small, but it is a timing claim on the investment page. | Medium |
| DS3-05 | `01` F4 → `05` ledger | Page 1's F4 says "kiosks at the 20 busiest hotels", but its chart names the 7 fullest and does not mark the 20. The kiosks' actual evidence ("check-in complaints there up 43% since 2021") first appears in a ledger cell on page 2. F4's title says "fullest" and its link says "busiest". | The kiosks are a third of package A, and their case is the thinnest bridge between the pages. | Medium |
| DS3-06 | `05` ledger F2 row; gate text | The ledger tracks "distribution cost, % of room revenue: 11.3% → 10.1%", and the gate rule uses it ("down 0.6 points or more"). Page 1 never shows 11.3%: it shows the agency share (50.0%) and the $19.68 per night. | The number that releases $12.4M has no anchor on the page that diagnoses it. | Medium |
| DS3-07 | `05`, hero header | The columns read "test 1" and "test 2". The tests are named only by captions floating above ("8%: our cost of money", "pays back by 2032 →"). | Decoding work on the most important table; "test 1" says nothing on its own. | Medium |
| DS3-08 | `09`–`11` B row; `16`–`21` plan tile | Ranges with no label: "−$6.9M to +$12.6M" and "−$5.5M to +$12.7M". The reader must guess Low to High NPV. In Low, B's range starts with the number printed right above it. | An unlabelled number is a small trust leak, repeated on two views. | Low–Medium |
| DS3-09 | `09`, `11`, What waits cash chart | The "B +$6.8M" label sits on the $0M line, about $7M below where B's line ends. In High the labels say A +$19.2M and B +$19.7M, so B ends higher, yet B's label sits under A's. The title says "B ends within $1M of A". | The label position misreads B, and the title hedges where the labels are exact. | Low–Medium |
| DS3-10 | `17`, `19`, Build | Six moves: +$6.1M a year against A's +$3.5M, but −$5.1M NPV against +$3.3M. The cash title only says "behind A by $6.4M". | It is the clearest teaching moment for the two lenses, and the view leaves it to the reader. | Low |
| DS3-11 | `09`–`11` tranche 3 row | "the seven hotels last renovated in 2021 held NPS near +6 while the rest fell to +2.7". That is a fourth NPS cut, beside page 1's +6.8 / +3.8 / −4.9 and the brand's +3.3. | More numbers to reconcile, in a cell, on the most expensive tranche. | Low |
| DS3-12 | `01` F1 note | "Room rates rose 2.7%" with no period. "Since 2023" is implied by the title, not stated. | Periods explicit is the floor for trust. | Low |
| DS3-13 | various | Small seams: F2's "27%" label sits on the "2025" axis label (`zoom/01_right`). "we keep" and "Goodnight Inn keeps" share one card. F3's count line hugs the band labels. "+$0.03M" (`07`). "$60.0M" on Build against "$60M" elsewhere. The tooltip names ("Kiosks, 20 busiest", "Booking app & rates") are a fair short register. | Polish. | Low |
| DS3-14 | `01` F3 note against `09` tranche 3 row | Page 1: "None has started since 2020." What waits: "the seven hotels last renovated in 2021". Both are true: the Renovations sheet shows the last seven Goodnight Inn renovations started Aug–Dec 2020 and ended Apr–Aug 2021. Side by side, they read as a contradiction. | A reader who spots it doubts both. | Low |
| DS3-15 | `01` F4 | The three type averages (◆ 82.0 / 79.1 / 77.5) sit in the dot rows and look like hotels. Only the legend on the left explains them. | Minor encoding ambiguity. | Low |
| DS3-16 | `05` against `09` | The refresh bar in the hero is navy, like the other "2028 gate" moves. Tranche 3 in the plan bar is slate. | One status, two colours. | Low |

**What is right and should not be touched:**
- the two headlines;
- the KPI context lines;
- the F1 wedge;
- the F2 room-night table;
- the F3 orange-only band;
- F4's Kingston sentence;
- the adaptive titles across Low, Expected and High;
- the ledger's adaptive statuses;
- the plan's one-line title and its gate rule;
- the 456-package scatter;
- Build's opening state, rules line, over-budget banner and empty state;
- the glossary;
- the tooltips.

*Part 1 saved here, before Part 2's sources were opened.*

---

## Part 2 · The reassessment

Sources opened only now:
- doc 19, in full;
- doc 24, in full;
- doc 25, sections 3, 5 and 7, and the logs of steps A to E in section 8.

Every status below rests on a capture or a text file of publish 6, not on a log.

### 2.1 Status of every earlier finding

These are doc 24's DS2-01 to DS2-12, plus the doc-19 items that were still open on 14 Nov. Doc 24 section 1 marked
DS-41 and DS-07 as open; they continue as DS2-02 and DS2-03. It also left two notes: the kiosk evidence it had
"crossed off" and the story note of section 3.

| ID | What it was | Status now | Evidence (publish 6) |
|---|---|---|---|
| DS2-01 | Cash and NPV side by side with no bridge | **Resolved** | The three cumulative titles carry "cumulative cash, not discounted" (`texts/05`, `09`, `16`). Recommended adds "(not discounted, so it ends above NPV)". The glossary has "Cash positive … ends above NPV, which discounts at 8%" (`04`). The year tooltip's banner reads "CUMULATIVE CASH, $M · NOT DISCOUNTED" (`08`). |
| DS2-02 | One name per move ("20 desks") | **Resolved** | The short names "Booking app & rates", "Kiosks, 20 busiest" and "Refresh, 10 oldest" are used (`16`, `12`). "desks" is on no page (grep of `texts/`). A residue sits in DS3-05: F4's "fullest" against its link's "busiest". |
| DS2-03 | The F4 title claimed months its chart can't show | **Resolved** | "Our airports run fullest: five of the seven fullest hotels are airports". The months moved into the note (`01`). |
| DS2-03 (also) | Diamonds explained by nothing | **Improved** | The legend reads "Airport ◆ 82.0%" (`01`). In the plot the ◆ still sits among the dots (DS3-15). |
| DS2-04 | NPV panel: the heaviest mark is the worst loser; the 8% label floats | **Improved** | The NPV panel shows A's three bars in blue and the other seven in light neutral (`05`, `06`, `07`). The 8% label still floats above the header, and the columns are now headed "test 1" and "test 2" (DS3-07). |
| DS2-05 | "no NPV shown" leaks into the table | **Resolved** | The phrase is gone (`texts/09`). |
| DS2-06 | What waits as a wall of prose | **Improved** | The copy is near-verbatim mine. Spec count 371 → 318 words (−14%, not −35%). The tranche 3 numbers cell runs five lines, against the four-line done-when (`zoom/09_right`). It reads well now (Part 1, 1.5). |
| DS2-07 | Ledger: the F4 cell packs two measures; chips wrap | **Improved** | F4 reads "0" and "20" (`05`). The chips still wrap: "F2 The / middleman", "F4 Where we / are full", "F3 The fading / welcome" (`zoom/05_right`). |
| DS2-08 | Capital chart: labels hide line ends; crossing against "2031"; no tick below zero | **Improved** | The lines reach 2032 and the labels stand clear (`05`–`07`). The −$10M tick is there. The strip says "Cash positive during 2031 (Expected)", but the eye still sees the line cross at the "2030" tick; my "(end of 2030: −$0.2M)" was not taken. It continues as DS3-04, which adds the gate marker. |
| DS2-09 | Low view repeats itself; the wrong hero in its title | **Resolved** | Line 1 reads "Expected case: +$3.3M through 2032 and +$3.5M a year by 2032.", and the hero title is the doc-24 copy (`06`). The new line 2 brought its own seam (DS3-01). |
| DS2-10 | Recommended at about 280 words | **Open, left on purpose** | The build's own count is 477 → 469, plus 19 in step C (doc 25, step B open item 1, step E "not met"). Part 1 counts about 640 visible words and figures, numbers included. |
| DS2-11 | Package tooltip ends on a rule | **Resolved** | "Low −$5.5M · Expected +$3.3M · High +$12.7M through 2032." (`12`, `13`). |
| DS2-12a | F3's count line hugs the band labels | **Open** | Unchanged (`zoom/01_right`), now in DS3-13. |
| DS2-12b | Orlando's label sits far from its dot | **Left on purpose** | Unchanged (`01`). Doc 25 step D gives the reason. |
| DS2-12c | The scatter title wraps into "Hover a dot" | **Resolved** | One line (`09`). |
| DS2-12d | The back link floats | **Left on purpose** | Unchanged (`05`). |
| DS2-12e | "Picked: 0 moves" beside "Nothing picked yet" | **Left on purpose** | Unchanged (`21`). |
| Doc 24 §3 | The headline blames the middleman while F1 shows running costs took more | **Left on purpose, now better answered** | F1's note names staff ("26.9% to 28.3% of revenue"). The forward line says "the kiosks for running costs" (`01`). |
| Doc 24 crossed-off note | Check-in complaints behind the kiosks were not on the page | **Improved** | Ledger F4: "check-in complaints there up 43% since 2021" (`texts/05`). It is on page 2 only (DS3-05). |

### 2.2 Left on purpose: does the reason hold from my seat?

- **D1, cut words and keep every block; DS2-10 not met: holds.** My 280 was a proxy. My fresh read did not stall on
  length. It stalled on four sentences: DS3-01, DS3-02, DS3-07 and DS3-08. The words added since 14 Nov carry
  evidence (the complaint rise, the reason in the gate rule, the Energy and Boston sentence). **I withdraw 280 as a
  condition for a 9.** If Bjorn wants a block out after all, the tile's mix line ("Booking app with member rates +
  Revenue management + Kiosks at the 20 busiest hotels") is the cheapest, because the hero's three blue rows say the
  same. It is not worth a publish of its own.
- **D2, D3, D6, D7 and D8: hold.**
  - The gate rule reads as one rule with a reason.
  - F3 has a number to watch: −4.9.
  - The KPI row without codes reads cleaner. On 13 Nov (DS-01) I asked for the KPI row as an index of the findings;
    taking the codes off undoes that, and the cards carry the index instead. I accept the change.
  - The complaint fact is the best evidence the kiosks have.
- **D4, Energy and Boston under the hero: holds, but it is half the job.** The caption explains two of the four "not
  now" rows. Breakfast and Kingston stay unexplained on the view (DS3-02).
- **D5, staff cost; the F1 sentence not built (step B, line 26): holds.** The note already names staff, and the
  forward line names the kiosks for running costs.
- **Copy-sheet line 7, "test 1" and "test 2" as column headers (step B): I would still press this one.** The reason
  (a 246 px phrase in a 155 px slot) is real, but the fallback is the worst of the options: it names the tests by a
  number. Short headers fit the same slots: "test: 8%" and "test: $0". The floating markers can stay. See DS3-07.
- **Copy-sheet line 9, the Low tile's line 2: does not hold as built.** "+$0.6M of the +$1.0M" quietly switches from
  NPV to yearly profit. The Expected wording "+$3.4M of the +$3.3M" names a part bigger than its whole. Both are
  sound arithmetic, and both read as mistakes. See DS3-01.
- **Copy-sheet lines 18 and 27, the renovation wording: the reason does not hold.** Step B said "last renovated is
  what the data holds (no proof needed that works finished then)". The data does hold it: the Renovations sheet gives
  the seven an EndDate in Apr–Aug 2021, after starts in Aug–Dec 2020. "Whose renovation finished in 2021" is provable.
  It would also clear the clash with "None has started since 2020". Line 27 stays as is: changing it would push F3's
  causal caveat into an ellipsis, and that caveat matters more. Low severity; ride-along only (DS3-14).
- **Line 22, "Picked: 0 moves" kept so the card has a spoken name: holds.** "Nothing picked: $60.0M to spend" would
  have served both purposes. It is not worth touching now.
- **Line 25, the glossary entry unchanged for fit: holds.**
- **Orlando (step D) and the back link: hold.** I checked capture `01`: Orlando's name under its dot is unambiguous.
- **NEUTRAL_LIGHT for the other NPV bars (step D, open to Bjorn's veto): holds.** From the storytelling seat this is
  right. A's three bars now carry the panel, and every pale bar has its value printed beside it.
- **Section 7, "not doing":**
  - INV-GR-2 and INV-DE-3 were refuted by the data.
  - INV-GR-4 is not in the data.
  - INV-GR-3 would be new content.
  - J-IN-7's headline change: the headline is fixed.
  - UX-18 (the tracking table): it meets the operational-impact rule.
  - DS2-01's discounted charts: model work. I advised against them myself.

  All of these hold.

### 2.3 Part 1 against my earlier findings

**Old findings under a new ID:**
- DS3-04 continues DS2-08's crossing point and adds the gate marker.
- DS3-07 continues DS2-04's floating 8% label and CL-36. It is partly made by a fix: the "test 1" and "test 2"
  headers are new in this round.
- DS3-13 includes DS2-12a.
- DS3-15 is DS2-03's residue.
- DS3-14 is CL-45 and INV-DE-5 from the other reviewers, not mine before.

**New, and two of them are my own blind spots:**
- **DS3-03:** I wrote the B row's copy myself on 14 Nov, "+$4.0M a year by 2032" included, without seeing that it
  beats A's +$3.5M.
- **DS3-08:** I also wrote "−$6.9M to +$12.6M" without a label.

The fresh read is right on both. The other new findings are DS3-01, DS3-02, DS3-05, DS3-06, DS3-09, DS3-10, DS3-11,
DS3-12 and DS3-16.

**Old findings I no longer see:** DS2-01, DS2-02, DS2-03, DS2-05, DS2-09, DS2-11 and DS2-12c. Their fixes hold in
the captures.

**Where my fresh eye and my earlier self disagree:**
1. **The What-waits table.** On 14 Nov I called it "the least visual element in the report" and wanted 35% fewer
   words. Today, after 14%, it read as clear and honest. I stand by today.
2. **Recommended's reading load.** On 14 Nov it was the last step to 9.5. Today it is a tax, not a barrier, and the
   barrier is a handful of sentences. I stand by today.
3. **The ledger order (F2, F1, F4, F3).** On 14 Nov I asked to keep it. Today I noticed the order and let it pass.
   I still keep it: A's strongest effect comes first.

### 2.4 What the fixes broke or added

- **New terms:** "test 1" and "test 2" (DS3-07).
- **New seam:** the Low tile's switch of lens (DS3-01).
- **A new number on page 2 only:** "+43%" check-in complaints. It is good evidence, without a home on page 1
  (DS3-05).
- **More to read:** Recommended carries about 2% more words than on 14 Nov by the build's count. It is acceptable,
  as above.
- **A coincidence to know about, not a defect.** The year tooltip at the end of 2031 (`08`) shows A's Expected cash
  as "+$3.3M", the same figure as A's NPV through 2032 on the same screen. A judge might think the tooltip shows NPV.
  The banner ("CUMULATIVE CASH, $M · NOT DISCOUNTED") answers that.
- **Numbers that should agree, checked across views. All agree:**
  - Tranche 2's 13.8% matches the hero's Gatwick 15.8% and Toronto 11.5% weighted by capex.
  - A's 37.5% matches its three moves.
  - "$2.4M with the agencies" matches the app's yearly +$2.4M on Build.
  - The ledger's 11.3% → 10.1% matches the gate's 0.6 points (half of 1.2 at the first-year ramp-up, doc 25 §4).
  - "17 of the last 24 months" reads the same on page 1 and in What waits.
  - The kiosks' "+$0.03M" in High appears identically in the hero.

### 2.5 Three claims of the build team, checked

| Claim (doc 25) | Holds? | Evidence |
|---|---|---|
| Step E: "'cash' and 'not discounted' on the three cumulative charts; none of 'desks', 'RMS', 'dataset units', 'no NPV shown', 'contest' on any page" | **Holds** | A grep of all 12 `texts/` files finds none of the five words. All three chart titles carry both phrases. |
| Step C: "Ledger row F4 now reads 'kiosks live Apr 2028; check-in complaints there up 43% since 2021'", re-derived from the workbook (0.88 → 1.26) | **Holds** | The cell reads exactly that (`texts/05`), and 1.26 ÷ 0.88 − 1 = 43.2%. |
| Step D: "In grey, the three A rows are the darkest marks of the NPV panel", and step C: "the lines visibly reach 2032, no label box lies on a line" | **Holds** | In `05`, `06` and `07`, A's NPV bars are the only saturated marks in the panel. In all three cases the three cash lines run to the 2032 tick and their labels stand right of the line ends. |

---

## Part 3 · Where it stands

### 3.1 Three versions side by side

| | 13 Nov | 14 Nov | Today (publish 6) |
|---|---:|---:|---:|
| My overall score, jury-lens estimate (as doc 19 and doc 24) | 7.4 | 8.8 (≈ 43.8 / 50) | **8.9** (≈ 44.7 / 50) |
| Jury lenses, per lens: Analytical quality · Insight · Visual effectiveness · Creativity · Accessibility | 8.0 · 7.5 · 7.0 · 8.5 · 7.0 | 9.0 · 9.0 · 8.3 · 8.7 · 8.8 | 9.1 · 9.2 · 8.6 · 8.7 · 9.1 |
| My storytelling criteria (Part 1, fresh) | not scored | not scored | 8.6 |

**What moved it:**
- **13 → 14 Nov:** the story closed.
- **14 Nov → today:** the trust seams closed: cash against NPV, one name per move, F4's title, the leak.
- Kiosk evidence and the keyboard walk joined.
- The fresh read found a new, smaller layer of reading-stoppers. That is why the gain is small.

The 8.6 is stricter than the jury lens because it prices every sentence a reader must decode.

### 3.2 Has it reached the bar for a 9?

Doc 24 put "about 9.3" on the T1 and T2 copy round, with DS2-10 as the last 0.2.
- **The round itself has landed.** All four T1 items are resolved, and the T2 items are resolved or improved.
- **The 9.3 has not.** The fresh read found a layer doc 24 did not list, and two items of it were my own copy.

Like for like, it stands at **8.9: at the edge of a 9, not over it.** What stands between, most valuable first:

| # | Item | Fix | Type |
|---|---|---|---|
| 1 | **DS3-03 + DS3-01: say the second lens out loud where it matters.** | **B row, Why not now:** "$2.3M more than A: $0.5M more a year, but $0.6M less through 2032 and 34% a year on cost against A's 37.5%. The queues at the 20 busiest hotels stay." The figures follow the case, so it needs a text measure: in Low the two yields are equal (11.1%) and the clause must say so.<br>**Tile line 2:** "The app is the core: +$3.4M through 2032 on its own. Every year without it …" In Low: "The app is the core: +$0.6M a year on its own. …" | C |
| 2 | **DS3-02: answer every "not now" on the hero.** | In the Status column, Breakfast reads "package B" and Kingston "not full". Both are as short as "2028 gate". The caption's Energy and Boston sentence stays. | C |
| 3 | **DS3-07: name the tests in their headers.** | "test 1" → "test: 8%", "test 2" → "test: $0". The floating markers can stay. | C |
| 4 | **DS3-08: label the ranges.** | "Low to High: −$6.9M to +$12.6M" (B row) and "Low to High: −$5.5M to +$12.7M" (Build tile). Fallback if the B cell would grow a fifth line: "range −$6.9M to +$12.6M". | C |
| 5 | **DS3-04: one calendar for the cash chart.** | The ticks stay; the gate marker moves to halfway between the 2027 and 2028 points. Or the strip ends with "(end of 2030: −$0.2M)" if it fits. | M |

### 3.3 Worth one more publish?

The gate has passed on every check at both widths for the first time. Every publish so far has brought a surprise:
the bubble, a 25-minute cache. So:

- **Item 1: worth a publish, and the only one that is.** A judge who reads the subtitle's promise and then sees B's
  "+$4.0M a year by 2032" next to A's "+$3.5M" will ask why the page says nothing. The answer is in A's favour, but
  silence reads as hiding. These are two text measures, no layout. Check the fit in the B cell (four lines) and the
  tile (one line).
- **Items 2, 3 and 4: ride along only.** They are worth doing in the same publish if item 1 goes ahead. None is worth
  a publish of its own.
- **Item 5: leave it.** It is model or report work on a chart that passed the gate. Most judges read the ticks as
  year-starts, so to them the gate marker looks right and only the crossing looks a year early. The strip's "during
  2031" and the tooltip's "At the end of 2030: −$0.2M" give the truth to anyone who checks.
- **Ride-alongs if there is a publish, not worth one alone:**
  - DS3-14: "whose renovation finished in 2021" in the tranche 3 row.
  - DS3-13: "+$0.03M" written as "+$0.0M" or "break-even" in High.
- **If Bjorn would rather not publish again: leave everything.** The report is ready as it stands. Nothing here is
  wrong; it is unsaid or cryptic.

### 3.4 For the description or the cover image, not the report

- **The description:**
  - One sentence that names the two lenses up front: "NPV through 2032 is the contest's measure; because it counts
    nothing after 2032, every move also shows what it earns a year once live."
  - "Best viewed full screen" (the 1366 px window shrinks body text to about 8 px, `22`).
  - "All 456 packages the rules allow were computed; none beats A through 2032."
- **The cover image:** the 456-package scatter with A, B and C lettered, as doc 25 step F plans (J-CI-4). It is the
  single image that says "we checked everything". A crop of `09`'s left card at 2× from `zoom/09_left` is enough.
- **Not seen, so not judged:**
  - touch on a phone;
  - a real screen reader (only the text it is handed);
  - the package tooltip on B;
  - Build states other than the five captured;
  - the live report in a browser.

---

**Delivery:** written in the shared folder on Bjorn's machine and left uncommitted, as the prompt asks. No other file
in the repository was changed.
