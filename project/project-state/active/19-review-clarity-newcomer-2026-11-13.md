# 19 · Clarity review: a newcomer with no background (13 Nov 2026)

**Role:** a random viewer who follows the Dataviz World Champs and opens this entry out of interest. Not a judge, not a
designer, not a hotel or finance person. No knowledge of the brief, the dataset or the earlier rounds.
**Question:** accessibility as *clarity*. Can someone with no background follow the report? Where is the content, or
the layout plus the content, unclear, and why?
**Scope:** awareness only. Every item says where, what the newcomer sees or asks, and why it is unclear. There are no
fixes in this file; the merge with the other role reviews (jury, UI/UX) turns them into one improvement plan. IDs are
`CL-nn`.

**Version reviewed:** commit `cf50fcc` on `claude/relaxed-noether-nwhfs9` (pbip identical to `6ec5b58`, doc 18 hover
cues, Bjorn's hand check). Rendered fresh on 13 Nov from a throwaway copy in Power BI Desktop (nl-NL Desktop, so native
labels show a decimal comma; that is the accepted M3 notation and not part of this review). Evidence in
`project/deliverables/screenshots/Clarity-review-2026-11-13/`:

| File | What |
|---|---|
| 01_p1-brand-review.png | Page 1 as it opens |
| 02_p2-recommended-A.png | Page 2, "Recommended: A", Expected |
| 03_p2-considered-B-C.png | Page 2, "Considered: B and C" |
| 04_p2-build-your-own-empty.png | Page 2, "Build your own", nothing picked |
| 10 to 18 | Tooltip pages F2, F3, F4, band (10 years or more), hotel (Toronto Pearson), year (2030), Definitions, package A, package C |

**Severity scale** (for the merge, about the reader, not about the craft):

- **S1 · loses the thread.** The newcomer draws a wrong conclusion, or cannot say what the page is telling them.
- **S2 · has to work for it.** They get there, but only by decoding, cross-reading or hovering somewhere else.
- **S3 · friction.** A small stumble; it adds up but does not block.

---

## At a glance

| ID | Category | Where | In one line | Sev |
|---|---|---|---|---|
| CL-01 | A Context | P1, P2 banner | Nothing says who this is for, who decides, or what decision the report supports | S1 |
| CL-02 | A Context | P1 | P1 does not say that a decision follows on P2, and F4 has no visible purpose on P1 | S2 |
| CL-03 | F Logic | P2 all states | The 2032 horizon makes almost every move lose money; the page never says this is the horizon, not the moves | S1 |
| CL-04 | C Terms | P2, Definitions | "Pays back" means NPV above zero on the scatter but undiscounted cash above zero in the glossary and line chart | S1 |
| CL-05 | C Terms | P2 | Two money measures (NPV, cumulative net impact) give different numbers for A; nothing on the page says why | S1 |
| CL-06 | F Logic | P2 Recommended | A contains a move that loses money (Kiosks, −$0.6M); the card does not say why it is in | S1 |
| CL-07 | F Logic | P2 Recommended | Which move answers which finding is only implied by order ("F2, F3, F1"); Kiosks answering "the fading welcome" is counter-intuitive | S2 |
| CL-08 | F Logic | P2 | The rules (at least 3 moves, 1 of them growth, $60M) appear without source; "growth" is never defined | S2 |
| CL-09 | B Vocabulary | P2 headline | The headline uses "package" and "move" before anything defines them; the $60M has to be added up by the reader | S2 |
| CL-10 | F Logic | P2 Recommended | "+$3.5M profit a year by 2032" is larger than the "+$3.3M NPV through 2032"; looks contradictory without ramp-up and discounting | S2 |
| CL-11 | F Logic | P2 Recommended | "Low case: A ends at −$5.5M": the downside of the recommendation is stated but not weighed | S2 |
| CL-12 | D Colour | P2 three states | Orange dashed means "Low case" in one state and "package C" in the next; solid orange means "Your plan" in the third | S1 |
| CL-13 | D Colour | P1 to P2 | Blue means a different thing in nearly every card; F4's blue and grey have no key | S2 |
| CL-14 | E Chart | P2 cumulative chart | Four legend entries for three cases ("Case in view" repeats one of them) | S2 |
| CL-15 | E Chart | P2 cumulative chart | The title says "positive from 2031", the line visibly touches zero at 2030 | S3 |
| CL-16 | E Chart | P2 scatter | Legend shows a hollow ring for "every other package", the chart draws filled grey dots | S3 |
| CL-17 | E Chart | Package tooltip | The range strip has letters and ticks but no axis; "break-even" is printed at the far left, away from the zero tick | S2 |
| CL-18 | E Chart | P1 F1 | The note's numbers (8.4 to 10.6 points) are the gap between the two lines, but the note does not say so | S2 |
| CL-19 | E Chart | P1 F2 | The per-night table shows the guest paying *more* direct than via an agency, and fees on direct bookings; unexplained | S2 |
| CL-20 | B Vocabulary | P1 KPI row, F3 | NPS has no scale; a newcomer cannot judge whether +3.3 or −4.9 is good or bad | S2 |
| CL-21 | B Vocabulary | P1, P2 | Jargon used before the glossary is in reach: capex, NPV, run-rate, ADR, RevPAR, "pt", "take", "8%" | S2 |
| CL-22 | B Vocabulary | Definitions | The glossary misses the report's own words: package, move, growth, scenario drivers, "Case in view" | S2 |
| CL-23 | G Decoding | P1 F2 | "Our reading: the fullest brand ... grows by reach and direct rebooking, not by loyalty schemes" cannot be followed | S1 |
| CL-24 | G Decoding | P1, P2 | Eyebrow puns and metaphors need decoding (wake-up call, middleman, fading welcome, room to invest, "lose rooms") | S3 |
| CL-25 | G Decoding | P1, P2 | Who is speaking? "our recommendation", "our reading", "where we are full" | S3 |
| CL-26 | A Context | P1 F1, footer | Two baselines in one card (since 2023 in the title, since 2021 in the note); "2021 is a depressed base year" is not explained | S2 |
| CL-27 | F Logic | P2 Considered | C's contents are only in its tooltip; the card names one of its three moves | S2 |
| CL-28 | C Terms | P2 | Synonyms for one idea: pays back, break-even, broken even, cash positive, positive from; renovate and refresh | S2 |
| CL-29 | H Interaction | P2 Build empty | The empty state shows zeros, "+0.0 to +0.0", "$0,0M", "Totaal" and "Nothing picked yet" twice; it reads as broken | S2 |
| CL-30 | H Interaction | P1, P2 | "Definitions" sits bottom right, after the jargon; it cannot be open while reading the term it explains | S2 |
| CL-31 | H Interaction | P2 | "Hover" in the tags, "Tap" in the builder; hover does not exist on a phone or tablet | S3 |
| CL-32 | C Terms | P1, P2 footer | "F" is never spelled out; P1 calls them findings by implication, the P2 footer calls them "facts" | S3 |
| CL-33 | I Numbers | P2 | Precision jumps between neighbours: $9.4M and $9.40M, +$3.3M and +$3.28M, $11.65M beside $9.4M; ranges lose their $ and M | S3 |
| CL-34 | E Chart | P2 scatter | The six packages that matter sit in a tiny corner, A and B labels overlap; the eye goes to the cloud of losers | S2 |

---

## A · Context and framing: who, what, why

**CL-01 · Nothing says who this is for or what decision it supports (S1).**
Where: the banner of both pages. The newcomer reads "goodnight inn. THE WAKE-UP CALL · THE BRAND REVIEW" and
"Goodnight Inn in 2025, against the three other Pillow & Key Group brands." They can work out that Goodnight Inn is one
of four brands in a group. They cannot work out who is reading (management? the group board? investors?), who wrote it,
or that there is a budget to spend and a choice to make. The line that did this ("FOR THE BOARD OF PILLOW & KEY GROUP")
was removed in the header round of 12 Nov because it "said nothing". To a newcomer it was the only sentence that set the
scene. *Merge note: tension with Bjorn's decision of 12 Nov; the function was real, the form may not have been.*

**CL-02 · P1 does not lead to P2, and F4 looks like a dead end (S2).**
Where: P1 as a whole, and F4. P1 ends on the source line. Nothing says "these four findings feed an investment choice on
the next page". F4 ("The airports are the fullest at 82.0%") is the only finding that is not a problem; a newcomer
asks "so what?". Its purpose (the +40-room moves on P2) only shows on P2, in the builder's "Answers" column, and there
those moves all lose money (see CL-03), which makes F4 look pointless in hindsight.

**CL-26 · Two baselines in one card, and an unexplained "depressed base year" (S2).**
Where: F1 and the P1 source line. F1's title measures "since 2023", its note "since 2021". The source line says "2021 is
a depressed base year" without saying why (presumably the pandemic). The newcomer does not connect the footnote to the
choice of 2023 in the title, so the two baselines look inconsistent or cherry-picked.

## B · Vocabulary and jargon

**CL-09 · The P2 headline uses words the page has not defined yet (S2).**
Where: "Fund one package of three moves: $9.4M now, $50.6M held back." "Package" and "move" are defined in the reading
guide below the scatter, which the eye reaches later. "$50.6M held back" assumes the reader knows there is a $60M
budget; the sum is left to them. "Held back" for what, and until when, is answered in the recommendation card, not near
the headline.

**CL-20 · NPS has no scale (S2).**
Where: the KPI row ("+3.3, still positive, but falling every year, last of 4"), F3 (+6.8, +3.8, −4.9) and the band
tooltip. The glossary says "promoters minus detractors" but not that the scale runs from −100 to +100, or what a
typical hotel scores. A newcomer cannot tell whether +3.3 is a crisis or a rounding error, so F3's −4.9 loses its
weight.

**CL-21 · Jargon is met before help is in reach (S2).**
Where and which words:
- KPI row: "pt" in "−2.8 pt since 2023" (percentage points or per cent?).
- F1 note: "the booking channels' take", "points", "no price premium absorbs it".
- P2 subtitle: "in 2025 dollars at 8%" (a discount rate; the newcomer does not know money is being discounted).
- P2: capex, NPV, "NPV range", "profit a year" (the glossary's "run-rate"), Low / Expected / High.
- Hotel tooltip: ADR, RevPAR.
The glossary covers most of these, but see CL-30 for why that does not help in the moment.

**CL-22 · The glossary misses the report's own vocabulary (S2).**
Where: the Definitions tooltip. It explains the industry words (NPV, capex, NPS, ADR, RevPAR, OTA) but not the words
this report invented or relies on: *package*, *move*, *growth* (as in "at least 1 of them growth"), what drives the
Low / Expected / High cases, and what "Case in view" means. Those are the words a newcomer actually stumbles on.

## C · Terminology consistency: one idea, several words; one word, several ideas

**CL-04 · "Pays back" means two different things (S1).**
Where: the scatter ("Only 6 of 456 packages pay back by 2032"; the reading guide: "NPV through 2032 up; above the line
it pays back by 2032") versus the glossary ("Pays back, break-even: the first year the cumulative net impact,
undiscounted, is above zero") and the cumulative chart's "Break-even" line. On the scatter "pays back" means NPV above
zero (discounted). In the glossary and the line chart it means undiscounted cash above zero. A careful newcomer who reads
the glossary will find the scatter's headline is using the word differently.

**CL-05 · Two money measures, two answers for A, no explanation on the page (S1).**
Where: P2 Recommended. The card says A is "+$3.3M NPV through 2032". The cumulative line for A, in the same case, ends
by eye around +$7M in 2032. Both are "the value of A by 2032" to a newcomer. The difference (discounting) is only in the
glossary, and the year tooltip's kicker that said "undiscounted" was removed on 12 Nov as "adding nothing". For a
newcomer it was the one word that explained the gap. *Merge note: tension with Bjorn's 12 Nov decision; the word had a
function, the reader just could not see which.*

**CL-28 · Many words for one idea (S2).**
Where: P2 and its tooltips. "Pays back by 2032", "break-even", "broken even", "cash positive from 2031", "positive from
2031", "never breaks even", "Not cash positive by 2032". Also "renovate" (C's title) and "refresh" (C's text and the
move "Refresh 10 oldest"). A newcomer assumes different words mean different things and starts looking for the
difference.

**CL-32 · What does "F" stand for? (S3).**
Where: F1 to F4 on P1, "Revisit the facts F1 ..." on P2, the builder's "Answers" column. "Finding" is never written out.
P2 calls them "facts". Small, but it is the key that ties the two pages together.

## D · Colour and encoding

**CL-12 · Orange changes meaning between the three states of one page (S1).**
Where: P2. In "Recommended: A" the orange dashed line is the Low case. Click "Considered: B and C" and an orange dashed
line of the same style is package C. Click "Build your own" and a solid orange line is "Your plan". Orange also marks
negative numbers, the "Hover" tags, the F-labels and the tooltip header band. A newcomer who learned "orange dashed =
the bad case" in the first state reads package C as a scenario.

**CL-13 · Blue means something else in nearly every card (S2).**
Where: P1 and P2. Blue is "After commissions" (F1), "Goodnight Inn" (F2, band tooltip), "airport" (F4), "A, our
recommendation" (P2), and "a positive bar" (waterfall). In F4 the blue and grey bars have no key at all: the newcomer has
to infer from the title that blue = airport, and does not learn what grey is (city? highway?).

## E · Reading individual charts

**CL-14 · Four lines in the legend, three cases in the chart (S2).**
Where: P2 Recommended, cumulative chart: "Low · Expected · High · Case in view". The newcomer counts three lines in the
plot, four in the legend, and looks for the missing one. That "Case in view" is the selected case drawn on top of its
twin is not said.

**CL-15 · The title and the line disagree by eye (S3).**
Where: same chart. Title: "positive from 2031 in the Expected case". The blue line touches the zero line at the 2030
tick (the year tooltip confirms −$0.2M at the end of 2030, so the title is right). A newcomer sees the crossing at 2030.

**CL-16 · Legend symbol does not match the marks (S3).**
Where: the scatter's reading guide: "○ every other package" (a hollow ring) against filled grey dots in the chart.

**CL-17 · The range strip in the package tooltip has no axis (S2).**
Where: tooltip pages for A and C. A grey bar with a dot, letters A, B, C above and below, small ticks, and "break-even"
printed at the far left with its own tick, while the actual zero line sits elsewhere (next to A). Without an axis the
newcomer cannot tell what the horizontal position means or which tick is break-even.

**CL-18 · F1's note describes the gap without naming it (S2).**
Where: F1. "The booking channels' take grew from 8.4 to 10.6 points since 2021." Those numbers are the space between the
grey and the blue line. The note does not say "the gap between the lines", so the newcomer looks for 8.4 and 10.6 on
the axis and does not find them.

**CL-19 · The per-night table raises a question it does not answer (S2).**
Where: F2. "The guest pays $109.31 via an online agency, $111.56 direct." Why does a guest pay more direct? And
"Commission and fees −$4.46" on a direct booking: which fees? The table is the most concrete thing on P1, so the
newcomer reads it closely and gets stuck on exactly these two cells.

**CL-34 · The point of the scatter is in a corner (S2).**
Where: P2 scatter, "All packages". The six packages that pay back, A and B among them, sit in the top-left corner, with
the A and B labels touching. The eye goes to the big cloud of losing packages. The zoom toggle exists, but a newcomer
does not know they should use it. (In the B/C and builder states the labels A and B overlap the dots as well.)

## F · The logic of the recommendation: the "why" gaps

**CL-03 · The horizon, not the moves, makes most options lose money (S1).**
Where: P2, all states. The scatter is a cloud of packages losing up to $60M; in the builder 8 of the 10 moves have a
negative NPV, including every "+40 rooms" move and the new Boston hotel. The subtitle says "nothing after 2032 is
counted", but never draws the consequence: anything that takes years to earn back looks like a loss by design. A
newcomer concludes "investing in this brand destroys value", or "F4 (the airports are full) was a dead end", which is
not the story.

**CL-06 · Why is a money-losing move in the recommendation? (S1).**
Where: the waterfall under "Our recommendation: package A". Booking app +$3.4M, Kiosks −$0.6M (orange), Revenue
management +$0.5M. The newcomer's first question is "why fund the one that loses money?". The answer (the rules require
three moves; Kiosks is the cheapest third move and the one aimed at guest scores) is spread over the builder's rule line,
the "Answers" column and B's card. It is not on A's card.

**CL-07 · The move-to-finding link is implied by order (S2).**
Where: A's card: "Each move answers a finding on The Brand Review page (F2, F3, F1)." The reader has to map the three
codes onto the three moves by position. Kiosks then answers F3, "The fading welcome", which reads backwards to a
newcomer (a machine at the desk as the answer to a fading welcome). B's card explains it ("a guest-score effect"), A's
does not.

**CL-08 · The rules arrive without a source, and "growth" is undefined (S2).**
Where: the reading guide ("within the $60.0M budget (at least 3 moves, 1 of them growth)") and the builder. The
newcomer does not know these are the competition's / the group's constraints, so they read like the author's own
preferences. "Growth" is a tag in the builder (Booking app is growth, Kiosks is not, Breakfast upgrade is) with no rule
for what makes a move "growth".

**CL-10 · Profit a year bigger than total value (S2).**
Where: A's card: "+$3.3M NPV through 2032" next to "+$3.5M profit a year by 2032". A yearly profit larger than the
total value over seven years looks like an error unless the reader knows about ramp-up and discounting.

**CL-11 · The downside is stated, not weighed (S2).**
Where: P2 Recommended: "−5.5 to +12.7, NPV range, $M" and "Low case: no package pays back by 2032; A ends at −$5.5M"
in orange. The newcomer reads "the recommendation can lose $5.5M" and finds no sentence about why that risk is
acceptable (for example, that every option is worse in the Low case). The range itself does not say it runs from the
Low to the High case.

**CL-27 · Package C's contents are hidden (S2).**
Where: "Considered: B and C". A's card lists its three moves; B's card describes a swap against A; C's card mentions
only "the refresh of the 10 oldest hotels". That C also holds the booking app and revenue management is only in C's
tooltip. The title "C · Why not renovate?" is a question, and the answer is spread over two text blocks.

## G · Text that needs decoding

**CL-23 · F2's "Our reading" cannot be followed (S1).**
Where: F2 on P1 and its tooltip: "Our reading: the fullest brand of the four grows by reach and direct rebooking, not by
loyalty schemes." Nothing on the page mentions loyalty schemes or rebooking. "Grows by reach" is unclear (reach through
the agencies?). And "direct rebooking" sounds like a fact about growth, while the chart shows direct bookings shrinking.
This is the one sentence on P1 a newcomer reads twice and still cannot paraphrase. *Merge note: "Our reading:" as a
label was kept on purpose (plan 09 R5); this item is about the sentence after it, not the label.*

**CL-24 · Puns and metaphors need decoding (S3).**
Where: "The wake-up call", "The middleman", "The fading welcome", "Where we are full", "Room to invest", and in F3
"Older hotels lose guest loyalty before they lose rooms" ("lose rooms" = lose occupancy). Each works once you know the
answer. A newcomer reads the eyebrow before the title, so the pun arrives first and the meaning second. *Merge note:
the puns were kept on purpose (round 9, Bjorn). Recorded for completeness; the cost is small because the titles below
are literal.*

**CL-25 · Who is "we"? (S3).**
Where: "Our recommendation", "Our reading", "Where we are full". Elsewhere the text says "Goodnight Inn" in the third
person. The newcomer cannot tell whether the voice is the brand's management, a consultant, or the report's author. This
links to CL-01.

## H · Interaction and empty states

**CL-29 · The builder's empty state looks broken (S2).**
Where: "Build your own", nothing picked. "$0.0M capex, $0.0M NPV through 2032, +0.0 to +0.0 NPV range", a lone "$0,0M"
floating over the word "Totaal" where the waterfall will be, and "Nothing picked yet" twice (tile title and under the
list). The line "Pick moves on the left; your plan appears here." is there, but the zeros around it make the newcomer
think something failed to load.

**CL-30 · Help arrives after the confusion (S2).**
Where: "Definitions" in the bottom-right corner of both pages. The jargon starts in the top-left KPI row. A
left-to-right, top-to-bottom reader meets "net promoter score", "operating margin after commissions" and "NPV" long
before they see the Definitions link. And because the glossary is a hover tooltip, it disappears the moment the mouse
moves back to the term it explains; it cannot be read side by side with the chart.

**CL-31 · Hover versus tap (S3).**
Where: the "Hover a bar / hotel / dot / year" tags and the builder's "Tap a move to add or remove it". On a phone or
tablet (Publish to Web links get shared on social media) there is no hover, so every tooltip, the glossary and the F1 to
F4 recap are out of reach. The two verbs also suggest two different devices.

## I · Number display

**CL-33 · Precision and units jump between neighbours (S3).**
Where: P2 and the package tooltip. "$9.4M" on the card, "$9.40M" in the tooltip; "+$3.3M" and "+$3.28M"; B's card
"$11.65M" beside A's "$9.4M"; NPV ranges written "−5.5 to +12.7" with "$M" moved to the label while the neighbours
carry "$" and "M" in the number. A newcomer wonders whether the numbers are different, not just rounded differently.

---

## What already works for a newcomer (keep; do not "fix")

- **The KPI row's comparison lines** ("best of 4, the others 64.7% to 72.9%", "highest of 4, 33.0% in 2021"): they
  answer "is that good?" without any background. NPS is the exception (CL-20).
- **Titles written as sentences** on every card: the newcomer can read the page by titles alone.
- **F2's per-room-night table**: the most concrete explanation of the middleman problem in the report (once CL-19 is
  answered).
- **F3's honesty line** "An association, not proof of cause."
- **The reading guide above the scatter**: the right idea in the right place; its content is what CL-08 and CL-09 build
  on.
- **The builder's table with the "Answers" column**: it is the clearest place in the report where moves meet findings.
  CL-07 is about bringing that clarity to A's card.
- **B's "Not picked" line**: one sentence, two numbers, a clear reason.
- **The "Hover a ..." tags**: they say exactly what to do and where.
- **The year tooltip** ("At the end of 2030", A in the three cases, then A, B, C and your plan): it answers the
  question the line chart raises.
- **The glossary's content**: short, plain, one line each. Its gaps are the report's own words (CL-22) and its
  placement (CL-30), not its writing.

## Merge notes for the improvement plan

- **Three items push against decisions already made.** CL-01 (the audience line removed on 12 Nov), CL-05 ("undiscounted"
  removed on 12 Nov) and CL-24 (the puns kept in round 9). From the newcomer's chair the first two removed words that
  carried meaning. The merge should decide these knowingly, not by drift.
- **Likely overlaps with the other roles:** colour semantics (CL-12, CL-13) with the UI/UX review's colour section;
  the horizon effect (CL-03) and the money-losing move in A (CL-06) with the jury's analytical-quality and
  insightfulness points; the empty builder (CL-29) and the hover-only content (CL-30, CL-31) with UX controls and the
  jury's accessibility criterion.
- **Clusters that would move the most for the least:** the three S1 logic gaps (CL-03, CL-04/05, CL-06) are each about
  one missing sentence or word in a place the reader already looks; CL-12 is a colour assignment; CL-23 is one
  sentence.
- **CL-15 and CL-16 are small** but they are the kind of mismatch a careful newcomer notices and then distrusts the
  rest.

## Not verified in this review

- **A real newcomer.** This is a simulated cold read by someone who has seen the build history; a five-minute test with
  one person who has never seen the report would confirm or kill the S1 items.
- **Tooltips in place.** The tooltip pages were rendered standalone; how they read floating over the hovered card was not
  checked.
- **Publish to Web, a browser at 1366 px, a phone.** Not available until Bjorn publishes; CL-31 is reasoned, not
  observed.
- **The filled builder states** (picks, over budget): the clarity of the plan tile and the rules line after clicks is
  taken from ScreenshotsFinalV2 05 to 08, not re-rendered.
