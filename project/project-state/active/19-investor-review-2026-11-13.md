# 19 · Investor review: the Board's investment committee reads the entry (13 Nov 2026)

**Role:** chair of the investment committee that has to approve or return Goodnight Inn's five-year plan.
**Lens:** Christopher J. Nassetta, President & CEO of Hilton (see "Why this lens"). The review applies the principles
he has stated in public. The wording and the verdict are mine. Nothing here is a quote from him unless it is cited.
**Scope:** awareness only, like the other role reviews (`19-jury-review`, `19-review-ui-ux`). It records where the
investment case convinces, where it doesn't, and what would have moved the decision to a full yes. It does not fix
anything. The merge round turns all the role reviews into one improvement plan.
**Version reviewed:** commit `cf50fcc`. No pbip changes since, so the 13 Nov renders are current:
`project/deliverables/screenshots/Jury-review-2026-11-13/01_p1-brand-review.png` and
`02_p2-investment-strategy_recommended-A.png`. Considered B/C, Build your own and the package tooltip come from
`ScreenshotsFinalV2/` (03, 05, 16). Their content is current; only their header row is out of date.
**Numbers in this review** that are not on the canvas come from the project's own evidence pipeline:
`project/analysis/output/project_economics.csv`, `packages.csv`, `packages.txt`, `gi.txt`. Run-rate = the
annual operating-profit impact in 2032, Expected case, unless stated otherwise.

**Item IDs** (`INV-TH-1` and so on) are stable for the merge. They cross-reference the jury IDs (`J-…`) where both
roles see the same gap from different sides.
Severity: **Blocker** (the committee would not approve the plan as presented), **Major** (a question the presenter
has to answer before approval), **Minor** (credibility detail).

---

## 0 · Why this lens

The report asks a hotel board to fund a plan. The reviewer should be someone who has made those calls at scale and
has commented in public on the exact issues in this report. Nassetta fits on all three themes:

| Theme in the report | Why his view is the relevant one |
|---|---|
| **F2, the middleman** (OTA share 33 % → 50 %) | He fought this fight in public. In 2015 he renegotiated Hilton's OTA contracts (no last-room availability, preferential member pricing, lower margins). In 2016 he launched "Stop Clicking Around", the industry's best-known direct-booking campaign, built on **member rates** in the Honors app |
| **$50.6M held back** | He runs Hilton capital-light and returns the cash it doesn't need to shareholders. He would respect discipline, but he would want to know where the money goes and why |
| **F4, where we are full** | His growth algorithm is net unit growth plus same-store growth. A brand that is full and adds no rooms would get his full attention |

He is widely regarded as one of the most successful hotel CEOs of his generation: he led Hilton through the
Blackstone era, the 2013 IPO and the 2017 spin-offs. And he talks about strategy in public, in interviews and on
earnings calls.

---

## 1 · How an investment committee scores a plan

A jury asks whether this is a good report. A committee asks whether to fund it. The criteria below are the ones a
board investment committee applies to any capital request. The weights reflect what decides a vote.

| # | Criterion | Weight | The question the committee asks |
|---|---|---:|---|
| 1 | Thesis and the ask | 15 % | In one sentence, what do you want from us, and why now? |
| 2 | Diagnosis and evidence | 15 % | Do you understand the business better than we do? |
| 3 | Capital allocation and returns | 25 % | Is this the best use of the $60M, judged the way we judge assets? |
| 4 | Growth and value creation | 15 % | Where is the brand bigger and more valuable in 2032? |
| 5 | Risk, downside and governance | 15 % | What can go wrong, how much can we lose, and when do we decide again? |
| 6 | Accountability | 15 % | Which operating numbers will you be held to, by when? |
| — | Experience (not scored) | | Did the document hold the room? Was it a pleasure to use? |

---

## 2 · Scorecard

| # | Criterion | Score | One line |
|---|---|---:|---|
| 1 | Thesis and the ask | **8.0** | The headline is a decision with numbers. Few board papers manage that |
| 2 | Diagnosis and evidence | **8.5** | P1 is a diagnosis I would want from my own strategy team. One sentence contradicts the cure |
| 3 | Capital allocation and returns | **5.5** | Rigorous, but on one lens only. That lens is the contest's 2032 cut-off, and it decides the answer |
| 4 | Growth and value creation | **4.5** | A full brand with pricing headroom, and the plan adds no rooms and claims little rate |
| 5 | Risk, downside and governance | **6.0** | Honest about the Low case. Thin on concentration, milestones and the rule for releasing the money |
| 6 | Accountability | **4.0** | No 2032 operating targets. I can't hold anyone to a number except NPV |
| | **Weighted total** | **6.0 / 10** | **Strong analyst, unfinished investment case** |

Experience: **P1 8.5 / 10** (a pleasure to read). **P2 6.5 / 10** (rewarding but hard work, and hover-dependent).

---

## 3 · Criterion by criterion

### 3.1 Thesis and the ask — 8.0

**Where it lands**

- "Fund one package of three moves: $9.4M now, $50.6M held back." That is an ask. The amount, the scope and the
  boldest choice are all in the headline. Most capital requests bury the number on page 4.
- P1's headline is the thesis in one breath: full rooms, slipping margin, paying the middleman, fading welcome.
  When I reach P2 I already know what the money is meant to fix.
- The package is named in plain language (Booking app, Kiosks at 20 desks, Revenue management), not in project
  codes.

**Where it falls short**

| ID | Sev. | Observation |
|---|---|---|
| INV-TH-1 | Major | **There is no "why now".** The cost of waiting is in the data but not on the page. Commissions grow by about $1–4M a year: the take rose from 8.9 % to 11.3 % of room revenue, and at the 2021 channel mix 2025 commissions would be $4.8M lower. NPS lost 1.7 points in 2025 alone. A committee funds urgency. The report has the evidence and doesn't make the case |
| INV-TH-2 | Minor | **The headline sells the restraint, not the return.** "$50.6M held back" is the most memorable phrase on P2, so the reader remembers what is *not* being done. The return of A (37 % yield on cost, see INV-CA-2) never reaches the headline or the rec tile |

### 3.2 Diagnosis and evidence — 8.5

**Where it lands**

- **The unit economics are the strongest single item in the report.** The F2 folio table shows one room night:
  $109.31 paid via an agency, $19.68 in fees, $89.63 kept, against $107.10 kept direct. Any hotel operator sees
  the problem in five seconds. This is how Nassetta argued the OTA case in public: what the commission costs the
  owner per stay.
- **Peer ranks on every KPI** ("best of 4", "2nd of 4", "last of 4") answer the committee's first reflex: compared
  to what?
- **Fact is kept apart from opinion.** "Our reading:" and "An association, not proof of cause" read as
  intellectual honesty, and committees reward that.
- **The counterfactual is in dollars:** $4.8M of 2025 commissions caused by the mix shift.

**Where it falls short**

| ID | Sev. | Observation |
|---|---|---|
| INV-DE-1 | **Major** | **The F2 note contradicts the recommended cure.** "Our reading: the fullest brand of the four grows by reach and direct rebooking, **not by loyalty schemes**." The move that carries the whole package is GI-01, *Direct booking app & **member rates***. Member rates *are* the loyalty lever. They are the core of the most famous direct-booking campaign in the industry. Someone with this lens stops reading at that sentence. Either the sentence or the framing of GI-01 has to change |
| INV-DE-2 | Major | **The kiosk evidence is in the data, but not on the page.** Goodnight Inn complaints per 1,000 room nights: *Check-in & waiting times* rose from 0.88 to 1.10 (+25 %, the second-fastest riser), and *Room condition* from 1.54 to 1.80 (the largest category, also rising). P1 ties F3 to renovation age only. So the kiosks look like an answer to a question nobody asked (cross-ref J-IN-3). A single complaint-category line on F3 would turn a weak link into an argued one |
| INV-DE-3 | Minor | **F4 is described, not interpreted.** "The airports are the fullest at 82.0 %" and F1's "room rates rose 2.7 %, in line with the other brands" together say *full, but not pricing like it*. That reading is the investor's insight, and it is the case for revenue management (see INV-GR-2). The report has both facts on one page and doesn't connect them (cross-ref J-IN-2, J-IN-6) |
| INV-DE-4 | Minor | F3 covers 44 of 50 hotels without saying so (cross-ref J-AQ-3). A committee member who adds it up starts to doubt the other numbers too |

### 3.3 Capital allocation and returns — 5.5

**Where it lands**

- **An exhaustive search, not three hand-picked options.** All 456 legal packages are evaluated under the finance
  rules. No board I know gets that level of option analysis.
- **Discipline over spending for its own sake.** Turning down 84 % of an allocated budget takes nerve. It is the
  capital-light instinct: don't deploy capital that doesn't earn its keep.
- **The alternatives carry reasons:** "B: $2.25M more capex than A for $0.6M less NPV". "C: below zero in every
  case, even High."
- **Build your own** lets a sceptical director test their own plan against A, live, within the rules. That is the
  most persuasive feature in the report. It turns an objection into a demonstration.

**Where it falls short**

| ID | Sev. | Observation |
|---|---|---|
| INV-CA-1 | **Blocker** | **One lens decides the answer, and it is the lens that is blind to long-life assets.** NPV through 2032 with no value after 2032 judges a 30-year hotel extension on four years of income. Your own scout file named this the *horizon trap* and said the entry "must show both the cumulative impact through 2032 *and* the 2032 run-rate … plus payback year". The page shows the run-rate for A only (+$3.5M) and no exit value for anything held back. To a committee, "Only 6 of 456 packages pay back by 2032, all under $15M" doesn't read as a finding about the business. It reads as a property of the method (cross-ref J-AQ-1) |
| INV-CA-2 | **Major** | **Under the lens investors actually use, the ranking changes in one place, and it is the place P1 points at.** Yield on cost = 2032 run-rate ÷ capex, Expected: App 47 % · RMS 32 % · **Kiosks 21 %** · Breakfast 20 % · **Gatwick +40 rooms 16 %** · Energy 12 % · Toronto +40 rooms 12 % · Boston 8 % · Kingston 8 % · Refresh 8 %. Two things follow. (a) **A gets stronger:** 37.5 % yield on cost as a package, and the "weak" kiosks are the third-best investment on the list. (b) **Gatwick clears an 8 % hurdle twice over.** It sits at a 90.4 % full hotel, and only the cut-off rejects it. A + Gatwick: $16.0M capex, NPV through 2032 −$0.25M instead of +$3.28M, run-rate +$4.57M a year instead of +$3.53M, plus 40 rooms. Most hotel investors would take that trade. You may still decide against it, but the committee needs to see that you weighed it |
| INV-CA-3 | **Major** | **"Why not renovate?" is argued with the weaker lens.** The refresh yields 7.9 % on cost, below the 8 % hurdle even with no cut-off at all. That is a far stronger reason to decline it than "NPV −$23.4M through 2032", which a critic can dismiss as horizon arithmetic. The report has the stronger argument and doesn't use it |
| INV-CA-4 | Major | **The cost of doing nothing is not priced, and the page doesn't say so.** The dataset's baseline doesn't decay old hotels. Deferring the refresh therefore looks free, while P1 says the welcome is fading. Deferred capex is a liability that grows. If the model can't price it, the page should say so in one line, so the committee knows the refresh case is understated, not settled |
| INV-CA-5 | Minor | Running costs: GI-01 ($0.6M/yr) and GI-10 ($0.3M/yr) appear to be netted in the operating-profit impact (MISSION reconciliation), but `04-p2-build-method` still says "unverified". If they are not netted, A's run-rate falls from $3.53M to $2.63M. The committee will ask. Make sure the answer is one word ("included") and true |

### 3.4 Growth and value creation — 4.5

**Where it lands**

- The rule is met: GI-01 and GI-10 carry the growth flag in the data.
- Margin recovery is a legitimate first move. Winning back $2.4M a year of commissions is worth more to a 44 %
  GOP brand than another 40 rooms in the wrong place.

**Where it falls short**

| ID | Sev. | Observation |
|---|---|---|
| INV-GR-1 | **Major** | **The brand is full, and the plan doesn't grow it.** P1 calls Goodnight Inn "best of 4" on occupancy (79.4 %), with airport hotels at 85–92 % and five of the seven fullest hotels at airports. P2 then holds back every room-adding move (Gatwick, Toronto, Boston). The "growth" in A is channel shift and pricing software: good business, but margin repair, not growth. A unit-growth mind reads P1 as a demand signal and P2 as ignoring it. The page needs either an extension or an explicit reason beyond the cut-off (cross-ref J-IN-2) |
| INV-GR-2 | Major | **Revenue management is filed under the wrong finding.** The rec note says RMS answers F1 (margin). Its real argument is F4 + F1: full hotels whose rates rose only 2.7 %, in line with brands that are 7–15 points emptier. That is money left on the table, and RMS ($2.4M, 32 % yield on cost) is the move that collects it. Re-filing RMS under F4 closes the "F4 leads nowhere" gap at no cost |
| INV-GR-3 | Minor | **Where the brand stands in 2032 is never shown.** No revenue, rooms or RevPAR line for 2032 against the do-nothing path. A committee approving a five-year plan wants to see the 2032 brand, not only the 2032 NPV |

### 3.5 Risk, downside and governance — 6.0

**Where it lands**

- **The downside is on the page, unprompted:** "Low case: no package pays back by 2032; A ends at −$5.5M." And
  "Pays back by 2032 except in Low" in the package tooltip. That is rare and builds trust.
- The NPV range sits on every card. The Low/Expected/High toggle reflows the whole page.
- A trigger exists for the held-back money, which shows governance thinking.

**Where it falls short**

| ID | Sev. | Observation |
|---|---|---|
| INV-RK-1 | **Blocker** | **Three different rules release the same $50.6M.** The rec note says it waits "until all three are live in Apr 2028". The C card says "revisit once A has broken even" (2031 on your own chart) "or if NPS falls below 0". And on the brand's own trend the NPS trigger fires first: 8.5 → 3.3 in four years, −1.7 in 2025 alone. That puts NPS below zero in 2027 or 2028, before A is even live. The plan's main capital decision is governed by a rule that contradicts itself and is likely to trigger by 2028. A committee will not approve that |
| INV-RK-2 | Major | **The whole package rests on one move.** The app is +$3.37M of A's +$3.28M NPV. RMS adds +$0.51M, kiosks −$0.60M. In Low the app alone is −$2.76M. So A is really "a bet on app adoption plus two supporting moves". The page should say so, and say what adoption means in operating terms (the share of room revenue that has to move from OTA to direct; each point is worth about $0.28M a year) |
| INV-RK-3 | Major | **No milestones, no kill criteria.** The data has the dates: RMS live Jul 2027, app Oct 2027, kiosks Apr 2028 (and the kiosks depend on the app). A committee funds in tranches against checkpoints: *if direct share hasn't moved X points by mid-2028, the kiosks don't start*. None of this is on the page (cross-ref J-AQ-6) |
| INV-RK-4 | Minor | **The downside is shown as a warning, not as a bounded loss.** In orange, "A ends at −$5.5M" reads like an alarm. The investor framing is: cash at risk $9.4M, worst case −$5.5M of value by 2032, and even then +$1.0M a year from 2032 onward. Same facts, but now the committee knows what it is signing up for |

### 3.6 Accountability — 4.0

| ID | Sev. | Observation |
|---|---|---|
| INV-AC-1 | **Blocker** | **No operating targets for 2032.** The brief asks for "financial *and operational* impact". A committee asks the same thing for a sharper reason: we pay for outcomes we can track. Distribution cost is at 11.3 % of room revenue against 7.5–8 % at the other brands. The app's driver (−1.2 pts) takes it to about 10.1 %, so even after A, about two-thirds of the gap remains. The committee needs to hear that from you, along with the 2032 target for margin after commissions, NPS (or the guest-score lift at the 20 kiosk hotels) and check-in complaints. All of it can be derived from the driver columns in `InvestmentScenarios` (cross-ref J-IN-1, J-CI-3) |
| INV-AC-2 | Major | **The P1 problems don't come back on P2.** Four findings open the case. P2 says "each move answers a finding (F2, F3, F1)" but never says *what happens* to each finding by 2032, or which one is consciously left open (room condition, F4 capacity). A short line per finding ("fixed by / partly / not now, because") would close the story. That is the moment a board says yes |

---

## 4 · Where the story and the numbers part ways

I read P1 and P2 as one argument. This is where the narrative and the numbers stop matching:

| P1 sets up… | …and P2 says | What the committee concludes |
|---|---|---|
| "Pays the middleman" (F2) | App + member rates, the largest NPV | ✅ **Matches.** The strongest thread in the report. Weakened only by "not loyalty schemes" (INV-DE-1) |
| "Its welcome is fading" (F3: renovation age → NPS) | Kiosks at 20 desks. Refresh declined | ⚠ **Different problem.** F3 points at rooms and P2 answers at the desk. Defensible with the complaint data (INV-DE-2), not as it stands |
| "The margin is slipping" (F1) | RMS, +$0.5M | ⚠ **Thin.** The margin story is mostly F2's commissions. RMS argues better from F4 (INV-GR-2) |
| "Where we are full" (F4) | Every room-adding move held back | ❌ **Contradiction.** A quarter of P1 builds a capacity story that P2 then rejects without a business reason (INV-GR-1) |
| Urgency (NPS falling every year) | $50.6M waits, with a release rule likely to fire by 2028 | ❌ **Contradiction** (INV-RK-1) |

---

## 5 · Experience: was it convincing, was it enjoyable?

**P1 — 8.5 / 10. Yes, enjoyable.** It reads like a well-written board memo that happens to be interactive. The
headline, the KPI row with peer ranks and the folio table carry the argument in under a minute. The eyebrow puns
("The wake-up call", "Room to invest") give it a voice without costing seriousness. I'd forward this page as it
stands.

**P2 — 6.5 / 10. Rewarding, but work.**
- The hero scatter is an analyst's proof, not a board's decision aid. About 450 grey dots argue *that* you searched.
  The committee needs *what you found*, and that sits in the small top-left corner where A and B overlap. It impresses
  the first time. The second time I look straight at the right-hand rec tile.
- **Build your own is the best moment in the report.** I added Toronto, watched the waterfall go orange and the line
  fall behind A, and understood the cut-off in ten seconds. That is persuasion by experience. But it shows only NPV,
  so it also teaches the committee the lens I'm challenging in INV-CA-1.
- **Board packs are read before the meeting, often as PDF or on a tablet.** Hover doesn't exist there. The package
  card, the year comparison, the four findings ("Revisit the facts") and the definitions sit behind tooltips, and a
  director reading the pre-read never sees them (cross-ref J-AC-1).
- **Number hygiene is a credibility signal in a financial paper.** "Totaal" on the waterfall, and decimal commas
  next to decimal points ("+$3,4M" under "+$3.3M") on the same screen (cross-ref J-VE-1). A finance director who
  notices that starts checking the arithmetic instead of the argument. Unit notation also mixes "$9.4M" and
  "−5.5 to +12.7, $M".

**How convincing:** it convinced me of the **problem** (9/10) and of **Tranche 1, package A** (7/10). It did **not**
convince me of the **five-year strategy** (4/10). The report answers "what should we fund first?" very well. It
doesn't yet answer the question the Board asked: "where should the $60M go?"

---

## 6 · Verdict: would I invest?

**In you: yes, without hesitation.** The rigour (an exhaustive search instead of opinion), the honesty (the Low case
on the page, "not proof of cause"), and the nerve to say "don't spend" are rare. They are what I look for in people
I'd put in charge of capital. The gap is one I've seen in many strong analysts: the method optimises the metric it
was given (NPV through 2032) instead of the business behind it. That is coachable. It is also exactly what
separates a strategist from an analyst.

**In package A: yes, approve as Tranche 1.** $9.4M, a 37.5 % yield on cost in the Expected case, a bounded
downside, and the move aimed straight at the brand's clearest problem.

**In the strategy as presented: not yet. Returned for one more round.** Three things stop approval:
1. The $50.6M has no coherent plan: three release rules, one of them likely to fire by 2028 (INV-RK-1).
2. Long-life assets are judged on four years of income, and the growth signal from P1 goes unanswered
   (INV-CA-1, INV-GR-1).
3. No 2032 operating targets to hold the plan to (INV-AC-1).

**Committee decision:** *Tranche 1 approved. Strategy to be re-presented with a staged capital plan and a 2032
scorecard.*

---

## 7 · What would have moved me to a full yes

In order of impact. Most of this reuses what is already in the model (`[2032 Run-rate]`, the driver columns, the
complaint table). These are the investor's asks, not a build plan; the merge round decides what fits before 18 Nov.

1. **Add the second lens next to NPV: 2032 run-rate and yield on cost per move and per package.** Keep NPV
   through 2032 as the contest's rule, and show what each move earns a year once it is built. Then A looks stronger
   (37.5 %), the kiosks become defensible (21 %), the refresh is declined for a better reason (7.9 % < 8 %), and the
   committee sees you didn't fall into your own horizon trap. *(INV-CA-1/2/3, J-AQ-1, J-AQ-5)*
2. **Turn "$50.6M held back" into a staged capital plan with one release rule.** For example: Tranche 1 = A
   (2027). Tranche 2 = the move the run-rate lens favours (Gatwick +40 rooms, if you agree) or an explicit "no,
   because…". Tranche 3 = the refresh, with a trigger that matches the NPS trend, plus the honest note that the data
   doesn't price the cost of waiting. One rule, one date, one owner. *(INV-RK-1, INV-CA-4, J-IN-4)*
3. **Put a 2032 scorecard on P2:** distribution cost % of room revenue (11.3 % → about 10.1 %), margin after
   commissions, NPS or the guest-score lift at the kiosk hotels, check-in complaints, rooms. Each with today's
   value and the 2032 value under A. *(INV-AC-1, J-IN-1)*
4. **Close the P1 loop in one line per finding:** F2 fixed by the app, F1 and F4 by RMS, F3 partly by kiosks with
   room condition knowingly deferred, capacity knowingly not added (or added). *(INV-AC-2, J-IN-2, J-CI-3)*
5. **Fix the credibility details:** the loyalty sentence (INV-DE-1), the complaint evidence for the kiosks
   (INV-DE-2), the bounded-downside framing (INV-RK-4), the app-concentration line (INV-RK-2), the locale and unit
   formatting (J-VE-1), the 44 of 50 hotels (J-AQ-3).
6. **Make the pre-read work without hover.** Whatever the Board must know to vote has to be static on the page.
   *(J-AC-1)*

If the report had done 1–4, my verdict would have been: **approve the strategy, fund Tranche 1 now, Tranche 2 on the
stated gate.** That is the outcome a Board paper is written for.

---

## 8 · Cross-cutting observations for the merge

1. **The investor and the jury see the same core gap:** P1's problems don't return on P2 as 2032 outcomes
   (INV-AC-1/2 ↔ J-IN-1, J-IN-2, J-CI-3). Two independent roles converging on this makes it the top item.
2. **The horizon issue is the investor's main objection and only a Major for the jury** (INV-CA-1 ↔ J-AQ-1). For a
   Board-facing entry, weigh it as the investor does: it decides whether 84 % of the budget is a judgment or an
   artefact.
3. **New items no other role has raised:** INV-DE-1 (loyalty contradiction), INV-RK-1 (conflicting release rules,
   NPS trigger about to fire), INV-CA-2 (the yield-on-cost ranking), INV-GR-2 (RMS belongs to F4), INV-DE-2
   (complaint evidence for kiosks).
4. **Hover dependence** costs the accessibility score with the jury and the pre-read with the Board
   (J-AC-1 ↔ section 5).

## 9 · Not verified in this review

- Whether `AnnualOperatingProfitImpactUSD` nets the running costs (INV-CA-5): the MISSION reconciliation says
  yes, `04-p2-build-method` says unverified.
- The NPS trajectory past 2025 is my linear reading of 2021–2025, not a model forecast. The dataset has no
  guest-score projection.
- Yield on cost uses the Expected 2032 run-rate, which still includes ramp-up for moves that go live late (Boston,
  Mar 2029). For those it understates the stabilised yield. Treat it as a ranking signal, not a valuation.
- Considered and Build-your-own were read from the 12 Nov renders (content unchanged since).

## Sources

- Project evidence: `project/analysis/output/project_economics.csv`, `packages.csv`, `packages.txt`, `gi.txt`;
  `project/SCOUT-pillowkey-round1.md` §2 (horizon trap) and §4.3; `project/MISSION-goodnight-inn.md`;
  `project/contest/round-1-brief.txt`.
- On the lens: [Skift, Hilton negotiated favorable concessions from online booking sites (2015)](https://skift.com/2015/12/01/hilton-negotiated-favorable-concessions-from-online-booking-sites) ·
  [Skift, Hotel CEOs won't back down on direct bookings (2016)](https://skift.com/2016/05/16/hotel-ceos-wont-back-down-when-it-comes-to-pushing-direct-bookings) ·
  [Skift, Hilton CEO believes direct booking campaign is key (2018)](https://skift.com/2018/02/14/hilton-ceo-believes-direct-booking-campaign-is-key-to-improved-guest-experience) ·
  [CoStar/HNN, Booking direct: CEOs on lower rates for loyalty members](https://www.costar.com/article/976382353/booking-direct-ceos-on-lower-rates-for-loyalty-members) ·
  [McKinsey, Hilton CEO Chris Nassetta on culture, strategy, and reinvention](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/hilton-president-and-ceo-chris-nassetta-on-culture-strategy-and-reinvention) ·
  [Hotel Investment Today, Why Hilton is confident about NUG growth](https://www.hotelinvestmenttoday.com/Financials/C-Corps/Why-Hilton-is-confident-about-NUG-growth)
