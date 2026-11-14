# 25 · Action plan: from the V2 reviews to a 9 (15 Nov 2026)

**For:** Bjorn and the local Claude Code sessions that build the last round before the submission of 17 Nov.
**Sources:** the five V2 reviews of 14 Nov on the fourth publish (`24-jury-review-v2`, `24-investor-review-v2`,
`24-review-ui-ux-v2`, `24-review-clarity-newcomer-v2`, `24-review-dataviz-storytelling-v2`), the captures they can
be checked against (`deliverables/screenshots/Committee-walkthrough-2026-11-14/`), doc 20 section 0 (the facts) and
the analysis outputs.
**How to use:** one step per session, as doc 23. Say "Read project/build-steps/round2.txt and execute it". The rules
of doc 23 section 1 hold for every step (generators only, comp and spec first, checks green, Desktop in a throwaway
copy, never publish, close your own Desktop windows without saving).
**Approval:** Bjorn, 15 Nov: "Go ahead, apply your recommendations." The decisions of section 3 are settled that
way, and that instruction is the approval for the new wording in section 5. A line can still be vetoed before
publish 5: say which one.

---

## 0 · Progress (each session updates its own row)

| Step | Title | Status | Date | Commit | Note |
|---|---|---|---|---|---|
| A | Copy sheet and fact check | done | 15 Nov | (this commit) | Sections 4 and 5. Three facts confirmed in the data, two placements changed for fit (D4, D5) |
| B | The copy round | todo | | | |
| C | The plan chart, and the kiosk evidence | todo | | | |
| D | Page 1 and the hero | todo | | | |
| E | Proof and publish 5 (Bjorn publishes) | todo | | | |
| F | Submission (Bjorn) | todo | | | |

Status values as in doc 23: `todo`, `doing`, `done`, `blocked`.
**Already built on 14 Nov, waiting for publish 5:** the buttons' bubble off, the plan chart's four ticks (doc 23,
"After the gate").

---

## 1 · Where we stand, and what a 9 is

| Lens | Now | A 9 is | The gap |
|---|---|---|---|
| Jury (5 criteria × 10) | 41.5 / 50 | 45 / 50 | Visual effectiveness 7.5 (P2 reads like a memo); two analytical loose ends; accessibility proof |
| Investor | 8.3 | 9.0 | The 2028 gate's logic and wording; staff cost has no owner |
| Dataviz reviewer's estimate | 8.8 | 9.3 | Two money measures without a bridge; P2 reading load; label seams |
| UI/UX (5-point scale) | 3 to 4.5 | nothing under 4 | Legibility at 1366 px (3), hierarchy on P2 (3.5) |
| Clarity | 0 S1, 6 S2 | 0 S2 | Four S2 on P2, two residual |

All five say the rebuild worked: no blocker, no finding that loses a reader. A 9 is on the edge: the jury's Visual
Effectiveness must go from 7.5 to about 8.5, and that only moves when page 2 carries fewer words.

| Lens | Moves on (themes of section 2) | Expected |
|---|---|---|
| Jury · Visual effectiveness 7.5 | 2, 6, 8 | about 8.5 |
| Jury · Analytical quality 8.5 | 1, 4, 7 | 9 |
| Jury · Insightfulness 8.5 | 3, 4 | 9 |
| Jury · Accessibility 8.5 | 9, the bubble, shorter text | 9 |
| Jury · Creativity 8.5 | the cover image only | 8.5 |
| **Jury total** | | **about 44.5 to 45 of 50** |
| Investor 8.3 | 3, 4 | about 9 |

---

## 2 · The findings in nine themes

Effort: C = copy or colour (text measures, spec, comp), M = model and report work, L = touches layout.

| # | Theme | Findings | Effort | Step |
|---|---|---|---|---|
| 1 | **Two money measures, no bridge.** NPV +$3.3M beside a chart that ends at +$6.8M; the Recommended chart has no title | DS2-01 (T1), J-AQ-8 (Major), J-VE-12, CL-05 | C; the caption is M | B, C |
| 2 | **Page 2 reads like a memo** (about 350 words on Recommended; 9 to 10 px at 1366) | J-VE-10 (Major), UX-18, CL-35, DS2-10, DS2-06, UX-26, INV-EX-1, J-AC-6, UX-28 | C | B |
| 3 | **The 2028 gate's logic and wording** | INV-CA-6, INV-RK-5, INV-RK-6 (all Major), INV-AC-4, INV-CA-7, J-IN-8 | C | B |
| 4 | **Moves parked without a reason; the bigger cause without an owner** | J-AQ-7 (Major), J-IN-7 (Major), INV-AC-3 (Major), INV-DE-2 | C, one M | B, C |
| 5 | **One name per thing** | DS2-02 (T1), CL-28, J-VE-15, INV-DE-5, J-AQ-11 | C | B |
| 6 | **The plan chart on Recommended:** label boxes hide two line ends, the line meets zero at 2030 beside "Cash positive 2031", "Hover a year" sits on the bar | DS2-08, CL-15, UX-20 | M, spike | C |
| 7 | **Copy slips** | DS2-05 (T1), DS2-07, DS2-09, DS2-11, DS2-12e, CL-36, CL-37, CL-41, CL-43, J-AQ-9, INV-DE-6 | C | B |
| 8 | **Page 1 craft, and the hero's colours** | UX-19, CL-18, DS2-03 (T1), UX-21, CL-42, J-VE-11, UX-22, J-IN-10, CL-32, UX-17, DS2-04, J-VE-13 | C, small L | D |
| 9 | **Accessibility proof, not design** | J-AC-8, J-AC-4, J-AC-2 | scripts | E |

---

## 3 · Decisions (settled, see "Approval")

| # | Question | Built | Not chosen |
|---|---|---|---|
| D1 | Page 2 density | Cut words, keep every block: Recommended from about 350 to 280 words, What waits about a third shorter | Moving "What we track" out of the tile (UX-18): it is what meets the contest's operational-impact rule |
| D2 | Why tranche 2 waits for the app | Both conditions stay, with the reason: the first money must have worked before more is spent | Releasing the rooms on occupancy alone |
| D3 | A rule for tranche 3 | F3 gets a number: the oldest hotels' NPS (−4.9 in 2025) in "What we track", named in the gate sentence | "A case that looks beyond 2032" alone |
| D4 | Energy and Boston | One sentence under the hero table: they exceed the $8.7M left. **Placement changed in step A:** a fourth row does not fit What waits (its rows stay four lines high after the cut) | A fourth row of What waits |
| D5 | Staff cost | One line, no headline change. **Placement changed in step A:** the fourth line of F1's note on page 1, where the reader meets the 1.8 points; the ledger and its caption on page 2 have no line to spare | A line on page 2 |
| D6 | KPI codes F4, F1, F2, F3 | The F-codes leave the KPI row; the cards keep theirs | Renumbering the findings |
| D7 | "→ Page 2: …" lines | Reworded so they stop promising a click: "On page 2: …" | Four bookmark buttons |
| D8 | Ledger row F4 | "guest score +0.25 there (dataset units)" makes way for the complaint fact (+43 % since 2021) | Keeping it and stating the scale |

---

## 4 · Facts checked for this round (step A)

| Fact | Result | Where |
|---|---|---|
| Check-in complaints at the 20 kiosk hotels | 0.88 → 1.26 per 1,000 room nights, 2021 → 2025 (+43 %); the other 30: 0.88 → 0.98. Not on any page today | doc 20 E2; `storytelling_checks.txt` section 2 |
| INV-RK-5: 0.6 points is not the Low case at mid-2028 | **Holds.** Ramp-up is 50 / 85 / 100 % by year after completion (FinanceParameters); the app is live in Oct 2027, so at a mid-2028 meeting the Expected case stands at half of 1.2 points = 0.6, the Low case at 0.3 | `packages.txt` line 1; `40_package_matrix.py` |
| The kiosks and running costs | The dataset gives two moves an operating-expense cut: the kiosks (−0.8 % at their 20 hotels, Expected) and the energy programme (−1.5 % brand-wide). No move acts on staff cost by name | `proj.txt`, column OperatingExpenseChangePct |
| "Five of the seven fullest hotels are airports" (DS2-03) | **Holds.** 2025 occupancy: Toronto 91.9 %, Gatwick 90.4 %, Montréal 90.2 %, Phoenix 88.5 % (airports), Kansas City 87.4 % (highway), Kuala Lumpur 86.5 % (city), Orlando 85.2 % (airport) | `hotels.txt` |
| Energy and Boston against what is left | 60.0 − 9.4 − 12.4 − 29.5 = $8.7M; Energy $15.0M, Boston $24.8M. Through 2032 they lose $12.2M and $18.3M: the most after the refresh | doc 20 R-P2-3 table |
| INV-GR-2: revenue management under F4 | **Refuted** (doc 20 E4: the fullest 20 raised rates 2.9 % against 2.6 %). Stays under F1 | `storytelling_checks.txt` section 3 |
| INV-GR-4: what the extensions' wait costs | **Not in the data.** Every move is priced from a 2027 start (doc 20 R-P2-7) | |
| "Renovated in 2021" against "none started since 2020" | To confirm in step B from the renovation dates; if "finished in 2021" cannot be shown, the line reads "last renovated in 2021" | `gi.txt` line 150 |

---

## 5 · The copy sheet

Old lines are the published text (`Committee-walkthrough-2026-11-14/texts/`). Where a line follows the scenario, the
Expected wording is shown and the pattern holds for Low and High. "Fit" says what the builder must see in the render;
when a line does not fit, the fallback is used, never a smaller font.

### Page 2 · frame and Recommended (step B unless marked)

| # | Slot | Old | New | Closes | Fit |
|---|---|---|---|---|---|
| 1 | Subtitle | The other $50.6M waits for one Board decision in mid-2028. Expected case. NPV through 2032 at 8% in 2025 dollars is the contest's rule and counts nothing after 2032, so we also show what each move earns a year once it is live. | The rest waits for one Board meeting in mid-2028. Expected case. NPV counts nothing after 2032, so we also show what each move earns a year once live. | DS2-10, UX-28, J-IN-9, CL-40, J-IN-8 | one line |
| 2 | Plan title | The $60M plan: $9.4M now, two decisions in 2028 | The $60M plan: $9.4M now, $41.9M decided at one Board meeting in 2028, $8.7M not needed | J-IN-8 | one line, clear of the hover tag |
| 3 | Plan bar, fourth label | Not needed · $8.7M | Not needed · $8.7M / stays with the group (a second line) | INV-CA-7 | two lines over a 262 px segment; fallback: leave |
| 4 | Gate rule | The 2028 gate, once all three moves are live: the Board releases tranche 2 if distribution cost has fallen at least 0.6 points (the app's Low case) and Gatwick and Toronto still topped 90% in 6 of the last 12 months. The refresh comes back to the same meeting with a case that looks beyond 2032. A decision rule, not a forecast. | The 2028 gate, one Board meeting once all three moves are live. Tranche 2 goes ahead if the first money worked (distribution cost down 0.6 points or more, the Expected track by then) and Gatwick and Toronto topped 90% in 6 of the last 12 months. The refresh returns with a case beyond 2032 and the oldest hotels' NPS. A rule, not a forecast. | INV-CA-6, INV-RK-5, INV-RK-6, DS2-10 | four lines; fallback: drop "or more" |
| 5 | Milestones | RMS live Jul 2027 · App live Oct 2027 · Kiosks live Apr 2028 (they need the app) · Cash positive 2031 (Expected) | Revenue management live Jul 2027 · App live Oct 2027 · Kiosks live Apr 2028 (they need the app) · Cash positive during 2031 (Expected) | J-VE-15, CL-15, DS2-08 | one line |
| 6 | Hero caption | A year on cost = what a move adds to operating profit in 2032 ÷ what it costs. | A year on cost = what a move adds to operating profit in 2032 ÷ what it costs. Not now: Energy and Boston exceed the $8.7M left. | J-AQ-7 (D4) | one line (the dropped sentence of 14 Nov left the room) |
| 7 | Hero markers | 8%: our cost of money · pays back by 2032 → | test 1: above 8%, our cost of money · test 2: pays back by 2032 → | CL-36, DS2-04 | each in its own slot; fallback: "1 · …", "2 · …" |
| 8 | Hero title, Low case | No moves pass both tests; the booking app earns 12.1% a year on cost but pays back after 2032 | In the Low case no move pays back by 2032; package A still loses least of all 456 packages | DS2-09, CL-43 | one line. A is the NPV maximum in Low (doc 23, step 8): re-read in the engine |
| 9 | Tile line 1, Low case only | Worst case (Low): −$5.5M through 2032, and still +$1.0M a year by 2032. | Expected case: +$3.3M through 2032 and +$3.5M a year by 2032. | DS2-09 | one line |
| 10 | Ledger F2 | status: half the rise since 2021 undone | half the rise undone | DS2-10 | |
| 11 | Ledger F1 | status: half the fall since 2023 recovered | half the fall recovered | DS2-10 | |
| 12 | Ledger F4 | self check-in hotels · rooms added / kiosks live Apr 2028; guest score +0.25 there (dataset units) / 0 of 20 · 0 / 20 of 20 · 0 / rooms decided at the 2028 gate | self check-in at the 20 busiest hotels / kiosks live Apr 2028 (step C adds: "; check-in complaints there up 43% since 2021") / 0 / 20 / rooms: at the 2028 gate | DS2-07, CL-37, J-AQ-9, INV-AC-4, INV-DE-2 (D8) | the row stays three lines |
| 13 | Ledger F3 | refresh of the 10 oldest hotels / why: see What waits, and why / not started / not started / deferred to the 2028 gate | NPS, hotels renovated 10+ years ago / the refresh: see What waits, and why / −4.9 / not in A / decided at the 2028 gate | INV-RK-6, INV-AC-4 (D3) | the row stays two lines; −4.9 is F3's own measure |
| 14 | Recommended chart caption (step C) | none | Package A, cumulative cash, $M (not discounted, so it ends above NPV) | DS2-01, J-AQ-8, J-VE-12 | placed in the spike |

### Page 2 · What waits, Build, tooltips (step B)

| # | Slot | Old | New | Closes |
|---|---|---|---|---|
| 15 | Scatter title | We checked all 456 packages the rules allow: none beats A through 2032 | None of the 456 packages beats A through 2032 | DS2-12c, CL-08 |
| 16 | Row B | Lifts guest scores in all 50 hotels instead of 20. · $2.3M more than A for $0.6M less through 2032, and it leaves the queues at the 20 busiest desks. · Not planned. | Lifts guest scores in all 50 hotels, not 20. · $2.3M more than A for $0.6M less through 2032, and the queues at the 20 busiest hotels stay. · Not planned. | DS2-06, DS2-02 |
| 17 | Row tranche 2 | numbers end with "no NPV shown" · Toronto and Gatwick topped 90% in 17 and 14 of the last 24 months. · Neither pays back by 2032 (−$3.7M and −$3.5M). · At the 2028 gate, if the app delivers and the airports stay full. Kingston (61% full) is not on the list. | numbers without that line · Toronto topped 90% in 17 of the last 24 months, Gatwick in 14. · Neither pays back by 2032 (−$3.7M, −$3.5M). Kingston (61% full) is not on the list. · 2028 gate: if the first money worked and both stay full. | DS2-05, DS2-06, INV-DE-6, UX-26 |
| 18 | Row tranche 3 | Tranche 3 · The refresh of the 10 oldest hotels (in package C) · package C (App + RMS + refresh) −$23.4M through 2032 · Renovation works here: the seven hotels renovated in 2021 held their NPS near +6 while the rest of the brand fell to +2.7. · It earns 7.9% a year on cost, just under our 8% cost of money. The data does not price the cost of waiting, so this case is understated. · Back at the 2028 gate, with a case that looks beyond 2032. | Tranche 3 · Refresh, 10 oldest hotels · in package C (app, revenue management, refresh): −$23.4M through 2032 · Renovation works: the seven hotels whose renovation finished in 2021 held NPS near +6 while the rest fell to +2.7. · 7.9% a year on cost, under our 8%. The data cannot price the cost of waiting, so this case is understated. · 2028 gate, with a case beyond 2032. | DS2-06, CL-39, J-VE-15, INV-DE-5, J-AQ-11 |
| 19 | What waits chart title | Cumulative net impact, $M: B ends within $1M of A by 2032; C is not cash positive by 2032 | Cumulative cash, not discounted, $M: B ends within $1M of A by 2032; C is not cash positive by 2032 | DS2-01 |
| 20 | Build chart title | Your plan against A, $M (Expected case): yours ends level with A in 2032, cash positive from 2031 | Your plan against A, cumulative cash, not discounted, $M (Expected case): yours ends level with A in 2032, cash positive from 2031 | DS2-01 |
| 21 | Move names in the selector, the bars and the tooltip table | Booking app · Kiosks at 20 desks · Refresh 10 oldest | Booking app & rates · Kiosks, 20 busiest · Refresh, 10 oldest | DS2-02 |
| 22 | Selector footer with nothing picked | Picked: 0 moves, $0.0M of $60.0M | (empty) | DS2-12e |
| 23 | Package tooltip, last line | Low −$5.5M · Expected +$3.3M · High +$12.7M through 2032; it pays back by 2032 above zero. | Low −$5.5M · Expected +$3.3M · High +$12.7M through 2032. | DS2-11, CL-41 |
| 24 | Glossary: Cash positive | from that year on, the cumulative net impact, undiscounted, is above zero. | from that year on, cumulative cash (the yearly net impact added up, not discounted) is above zero. It ends above NPV, which discounts each year at 8%. | DS2-01 |
| 25 | Glossary: NPV; Low, Expected, High; A year by 2032 | …at the organisers' rate. · the organisers' three scenarios for every move… · …measured in 2032 (its run-rate). | …at 8%. · the three cases the investment data gives for every move… · …after its running costs, measured in 2032 (its run-rate). | CL-40, INV-CA-5 |

### Page 1 (step B for 26 and 27; step D for the rest)

| # | Slot | Old | New | Closes |
|---|---|---|---|---|
| 26 | F1 note | …so no price premium absorbs it. | …so no price premium absorbs it. Staff cost is an operating matter, outside the ten moves on page 2; of those, only the kiosks and the energy programme cut running costs. | INV-AC-3, J-IN-7 (D5). Fit: a fourth line, as F2's note has; fallback: end after "page 2." |
| 27 | F3 note | None has started since 2020. | No renovation has started since 2020. | CL-45, INV-DE-5 |
| 28 | KPI labels | F4 · Occupancy · F1 · Operating margin after commissions · F2 · Room revenue booked through online agencies · F3 · Guest quality: net promoter score (−100 to +100) | the same without the codes | UX-22, J-IN-10, CL-32 (D6) |
| 29 | Forward lines | → Page 2: revenue management and the kiosks. (and three more) | On page 2: revenue management and the kiosks. (and three more, same pattern) | UX-17 (D7) |
| 30 | F4 title and note | Our airports run full: Toronto topped 90% occupancy in 17 of the last 24 months · Gatwick did in 14, Montréal in 13; Kingston, the third extension on offer, in none. | Our airports run fullest: five of the seven fullest hotels are airports · Toronto topped 90% in 17 of the last 24 months, Gatwick in 14, Montréal in 13; Kingston, the third extension on offer, in none. | DS2-03. Fit: the note takes a third line, the forward line moves down with it |
| 31 | F4 row labels | Airport 82.0% | Airport ◆ 82.0% (the diamond is the average's own mark) | UX-21, CL-42, J-VE-11 |
| 32 | F1 chart labels | "Commissions" at the end of the top line | "Before commissions" names the top line; "Commissions" stands in the band | UX-19, CL-18 |

---

## 6 · The steps

**Step B · The copy round (C).** Sheet lines 1 to 13 and 15 to 27, in `sketch_model.py` (the text measures of
`TEXT_SLOTS`, `BuildMove` short names, `WaitOption`, the ledger), `rebuild-v10-spec.json` → `text`, the comp, and
the generator's typed strings (`A_MOVES`, `GLOSSARY`, `HERO_CAPTION`, `WAITS_HEAD`).
*Done when:* every file check green; `build_checks.py` with the engine: every text slot equals the new spec in Low,
Expected, High and the empty Build state; `number_checks.py` green; strip renders of Recommended (three cases),
What waits and Build show the comp's line counts; Recommended at or under 280 words; the page texts hold no "desks",
"RMS", "dataset units", "no NPV shown", "contest".

**Step C · The plan chart, and the kiosk evidence (M).** Spike first, in a throwaway copy: the three end labels as
cards right of the line ends (the comp's picture; bound to the end measures, the case in view in Deep Coffee
semibold), the chart's own data labels off; sheet line 14 as the chart's caption; "Hover a year" moved onto the
chart (UX-20). Then `GuestComplaints` back into the trimmed model for one measure and the clause of sheet line 12.
*Done when:* all three lines visibly reach 2032 in Low, Expected and High; no label box lies on a line; the caption
names the measure; `strip_check` 0; the complaint number equals `storytelling_checks.txt` (a number check);
`compliance_check` counts the sheet.

**Step D · Page 1 and the hero (C, small L).** Sheet lines 28 to 32; Orlando's label on the side of its own dot
(DS2-12b); in the hero's NPV panel A's three bars in blue and every other bar in the light grey, the status staying
in the Status column and the left panel (DS2-04, J-VE-13).
*Done when:* P1 strip render on the comp with the new lines; `a11y_check` 0 (the diamond and the band label keep
4.5:1); in a greyscale copy of Recommended the three A rows are the darkest marks of the NPV panel.

**Step E · Proof and publish 5.** Engine checks; the FinalV3 renders that changed; a fresh publish copy in a freshly
opened Desktop window (doc 23, lesson 6); close the old window "Goodnight Inn" without saving; **Bjorn publishes**;
then `gate.py` against publish 4, extended with a Tab, Enter and Esc walk through page 2's three states in the
published report (J-AC-8) and a check that the scatter's unnamed layers take no focus (J-AC-4); `walk.py` again.
*Done when:* the gate passes, and on the published report: no bubble over a tab at 1366 px; the two typed ticks in
line with Power BI's own; "cash" and "not discounted" on every cumulative chart; Recommended at or under 280 words.

**Step F · Submission (Bjorn).** Phone check; the `.pbix` from the new window; description and image. Two free wins:
"best viewed full screen" in the description (UX), and the 456-package chart in the cover image, so a judge meets
the entry's most original idea before clicking a tab (J-CI-4).

**Cut line.** Steps drop from the back: D first, then C. Step B alone, with the two fixes of 14 Nov, closes every T1
and Major except the plan chart's labels.
**Schedule.** Sun 15 Nov: B, C. Mon 16 Nov: D, E with publish 5 by midday, publish 6 in reserve. Tue 17 Nov: F.
**Spare, only if step D ends early:** UX-23 (one colour rule for negatives in Build), UX-27 (A and B overlap), UX-29
(Build tile seams), CL-33 (label the range "Low to High"), DS2-12a, UX-25 (the hotel tooltip's small chart).

---

## 7 · Every V2 finding, and where it goes

"B 4" = step B, sheet line 4. New findings first, then what was left open from round 1.

| Jury | Goes to | Investor | Goes to |
|---|---|---|---|
| J-AQ-7 | B 6 | INV-CA-6 | B 4 |
| J-AQ-8 | B 19, 20, 24; C 14 | INV-RK-5 | B 4 (fact confirmed) |
| J-AQ-9 | B 12 | INV-RK-6 | B 4, 13 |
| J-AQ-10 | B 7 (the tests named); the measure stays | INV-AC-3 | B 26 |
| J-AQ-11 | B 18, 27 | INV-AC-4 | B 12, 13 |
| J-IN-7 | B 26; the headline stays (doc 20 §10) | INV-GR-4 | not doing: not in the data |
| J-IN-8 | B 1, 2 | INV-CA-7 | B 3 |
| J-IN-9 | B 1 | INV-DE-5 | B 18, 27 |
| J-IN-10 | D 28 | INV-DE-6 | B 17 |
| J-VE-10 | B (D1) | INV-EX-1 | B (D1); "full screen" in F |
| J-VE-11 | D 31, Orlando | INV-DE-2 (partly) | C 12 |
| J-VE-12 | C 14 | INV-DE-3 (partly) | not doing: E4 refutes the pricing reading |
| J-VE-13 | D (hero colours) | INV-CA-5 (partly) | B 25 |
| J-VE-14 | done 14 Nov | INV-GR-1 (partly) | not doing: decision D2 of doc 20 |
| J-VE-15 | B 5, 18 | INV-GR-2 (open) | not doing: refuted (E4) |
| J-CI-4 | F (cover image) | INV-GR-3 (partly) | not doing: new content and layout |
| J-CI-5, J-CI-1 | not doing: by construction | INV-RK-3 (kiosk stop rule) | not doing |
| J-AC-8 | E | | |
| J-AC-9 | B 5, 12 (the two unexplained terms go) | | |
| J-AC-2, J-AC-4, J-AC-6 | F (phone), E, B (D1) | | |
| J-AQ-6 (partly) | not doing | | |

| UI/UX | Goes to | Clarity | Goes to | Dataviz | Goes to |
|---|---|---|---|---|---|
| UX-17 | D 29 | CL-35 | B (D1) | DS2-01 | B 19, 20, 24; C 14 |
| UX-18 | B (D1); the table stays | CL-36 | B 7 | DS2-02 | B 16, 21 |
| UX-19 | D 32 | CL-37 | B 12 | DS2-03 | D 30, 31 |
| UX-20 | C | CL-38 | not doing (S3) | DS2-04 | D; B 7 |
| UX-21 | D 31, Orlando | CL-39 | B 18 (C spelled out) | DS2-05 | B 17 |
| UX-22 | D 28 | CL-40 | B 1, 25 | DS2-06 | B 16 to 18 |
| UX-23 | spare | CL-41 | B 23 | DS2-07 | B 12 |
| UX-24 | done 14 Nov | CL-42 | D 31, Orlando | DS2-08 | C; ticks done 14 Nov |
| UX-25 | stands (foot); spare (hotel chart) | CL-43 | B 8, 9 | DS2-09 | B 8, 9 |
| UX-26 | B 16 to 18 | CL-44 | not doing: the glossary separates them | DS2-10 | B 1, 4, 10, 11 |
| UX-27 | spare | CL-45 | B 17, 18, 27 | DS2-11 | B 23; the foot stands |
| UX-28 | B 1 | CL-46 | done 14 Nov | DS2-12 | a spare, b D, c B 15, d not doing, e B 22 |
| UX-29 | spare | CL-05, CL-15 | B 19, 20, 24; C | | |
| UX-30 | done 14 Nov | CL-18, CL-32 | D 32, D 28 | | |
| UX-07, UX-13, UX-14 (partly) | C; spare; stands | CL-08, CL-21, CL-22, CL-25, CL-28 | B 15; B 5, 12; B 5; B 1; B 16, 21 | | |
| | | CL-26, CL-30, CL-31, CL-33, CL-34 | not doing; not doing; F (phone); spare; spare | | |

**Not doing, in one place:** INV-GR-2 and INV-DE-3 (refuted by E4), INV-GR-4 (not in the data), INV-GR-3 (new
content), J-IN-7's headline change (the headline is fixed, doc 20 §10), UX-18's removal of the tracking table (D1),
DS2-01's discounted charts (model work and a full recheck), J-CI-1 and J-CI-5 (by construction), the tooltip's foot
and the puns (checked on 14 Nov: stand).

---

## 8 · Logs

*(each step writes its log here: built · verified, with the render or check that proves it · deviations · open items)*

**Step A (Sun 15 Nov 2026).** The five reviews read in full and merged (sections 2 and 7); the facts of section 4
checked in doc 20 and the analysis outputs; the copy sheet written (section 5). Two placements differ from the plan
Bjorn approved, both for fit and both recorded in section 3: the Energy and Boston sentence stands under the hero
table (D4), the staff-cost line in F1's note on page 1 (D5). Nothing was built in this step.
