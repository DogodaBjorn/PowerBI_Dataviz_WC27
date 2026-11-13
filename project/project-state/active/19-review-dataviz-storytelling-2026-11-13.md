# 19 · Dataviz and storytelling review: from a 7.4 to a 9.5 (13 Nov 2026)

**Role:** the dataviz and data-storytelling consultant hired for a last check before submission. This is not the jury
and not a build review. **Question:** does the report tell one story, does every chart earn its place in that story,
and where does the data offer a better story than the one on the canvas?
**Scope:** taste and target state. This file says *what the ideal report looks like*. It does not say how to build it.
It turns the three role reviews of 13 Nov (`19-jury-review`, `19-review-ui-ux`, `19-investor-review`, plus
`19-review-clarity-newcomer`) into one storytelling direction. A Power BI specialist agent turns it into fixes.
**Constraint kept throughout:** this has to be built in Power BI and must render under Publish to Web. That means
exactly two visible pages, hidden tooltip pages, bookmarks, native visuals plus the existing Deneb selector, SVG
measures in tables and images, built-in fonts, and provided data only. Where an idea is at the edge of what Power BI
can do, it is marked **[verify]**.

**Version reviewed:** commit `cf50fcc`. `git status` shows no changes under `project/pbip` since then, so the 13 Nov
renders show the current report. I did not re-render. Evidence:
`project/deliverables/screenshots/Clarity-review-2026-11-13/` (01 P1, 02 P2 Recommended, 03 Considered, 04 Build empty,
10-18 tooltips), `UX-review-2026-11-13/03_tooltips-sheet.png`, and `ScreenshotsFinalV2/05` (Build filled).
**Data used for new story angles:** `project/analysis/output/` (`gi.txt`, `hotels.txt`, `crosscheck.txt`,
`project_economics.csv`, `price_index.txt`). These figures come from the offline decode. Per CLAUDE.md, re-derive each
one in the model before it reaches a visual.

**Item IDs:** `DS-nn` for critique and target design, `DS-Dn` for data opportunities. Each item lists the other
reviews' IDs it absorbs, so the merge can de-duplicate.
**Priority:** **T1** = without it the report cannot reach 9; **T2** = this lifts it to 9.5; **T3** = polish.

---

## 0 · The verdict in one page

**What works (keep it):** P1 is close to best in class. It has a one-sentence diagnosis as the headline, peer ranks on
every KPI, action titles on every chart, and the folio table (one room night, three numbers), which is the best single
artefact in the report. The visual system is calm and consistent. And the analytical ambition behind P2 (all 456 legal
packages evaluated) is something no other entry will have.

**What breaks it.** There are five things. None of them is about polish.

1. **The story doesn't come back.** P1 opens four problems. P2 answers in dollars only and never says what happens to
   those four problems by 2032. F4 ("where we are full") leads nowhere, F3 → kiosks looks like a non sequitur, and one
   sentence on P1 ("not by loyalty schemes") argues against the move that carries the whole package (member rates).
   *Every reviewer found this from a different angle. It is the top item.*
2. **The P2 hero chart is about the method, not about the business.** "Only 6 of 456 packages pay back by 2032" is
   a property of the 2032 cut-off. The biggest chart on the decision page shows the weakest part of the argument
   (the horizon artefact) and hides the answer in a 40 px corner.
3. **$50.6M, 84 % of the budget, has no plan.** It appears as "held back" in the headline and as a sub-clause in the
   tile, and three different release rules govern it.
4. **Meaning sits behind hover.** The findings on P2, the package contents, the year comparison and the definitions
   only exist as tooltips. A Board pre-read, a keyboard user or a touch user never sees them.
5. **Number and word hygiene.** "Totaal", decimal commas next to decimal points, $3.28M next to $3.3M, "pays back"
   with two meanings, and orange with six meanings. A financial reader who spots these starts checking arithmetic
   instead of following the argument.

**The path from 7.4 to 9.5** (my estimate; these weights are judgment, not measurement):

| Step | What changes | Expected effect |
|---|---|---|
| Today | | ~7.4 (jury 38/50, investor 6.0, UX ~3.4/5) |
| **T1 · close the story** | Finding-to-move mapping rebuilt on evidence (DS-01..04), a static "what A does to the four findings by 2032" ledger (DS-20), one release rule (DS-22), the loyalty sentence turned into the member-rate bridge (DS-06), number and word hygiene (DS-40..42) | → ~8.6. The operational-impact rule is met, the contradictions are gone, and the argument holds from page 1 to page 2 |
| **T2 · make P2 a decision page** | Two-lens hero (DS-10), the 456 scatter moved to the "what waits" state as proof (DS-11), the $60M capital plan (DS-21), F4 as a capacity chart (DS-07), page navigation and static versions of hover content (DS-30..32) | → ~9.3. The Board sees the answer, the reasoning and the plan without hovering |
| **T3 · polish** | Colour roles (DS-43), control system (DS-33), chart details (DS-50..58) | → 9.5+ |

---

## 1 · The story spine: as built, and as the data allows

### 1.1 As built

```
P1  Full rooms, a slipping margin: we pay the middleman, and the welcome is fading.
    F1 margin ─ F2 middleman ─ F3 welcome ─ F4 where we are full
P2  Fund one package of three moves: $9.4M now, $50.6M held back.
    A = App (→F2) + Kiosks (→F3) + RMS (→F1)        F4 → nothing
    proof = 456 packages, only 6 pay back by 2032
```

The arc breaks in three places. Kiosks answer a renovation finding with a check-in device. F4 is a quarter of P1
with no consequence. And the proof on P2 argues the cut-off, not the business.

### 1.2 What the data supports (verified in `analysis/output`, re-derive in the model)

The data contains a tighter story than the one on the canvas. Four findings that the report doesn't use change the
mapping:

- **DS-D1 · The kiosks go to exactly the 20 fullest hotels.** GI-02's 20 hotels are the brand's 20 highest-occupancy
  hotels in 2025 (81.4 % to 91.9 %; number 21, Nashville, is at 81.0 %). All seven hotels on the F4 card are among
  them. *The kiosks are an answer to F4 (where we are full: queues at the desk), not to F3.*
  (`hotels.txt` ranked by Occ2025, `gi.txt` "GI-02 properties")
- **DS-D2 · Today, booking direct costs the guest more.** The F2 folio table shows that the guest pays $111.56 direct
  against $109.31 through an agency. Nothing rewards the guest for booking direct. *That is the exact problem member
  rates solve.* The report has this number on the canvas and doesn't read it.
- **DS-D3 · The welcome is fading because the renovations stopped.** Goodnight Inn spent $48.8M on 18 renovations
  since 2018, $1.0M per hotel. The sister brands spent $5.9M to $7.9M per hotel. No Goodnight Inn renovation has
  started since Dec 2020. The seven hotels renovated in 2021 held their NPS at about +6 (6.4 → 6.3) while the rest of
  the brand fell from +8.9 to +2.7. Room-condition complaints are the largest category and the fastest riser
  (1.54 → 1.80 per 1,000 nights; +0.09 in 2025 alone). Check-in complaints rose from 0.88 to 1.10 by 2023 and have been
  flat since. (`crosscheck.txt`, `gi.txt`)
- **DS-D4 · Not every full hotel is equally full.** On monthly average occupancy in 2024 and 2025, Toronto was at or
  above 90 % in 17 of 24 months, Gatwick in 14 and Montréal in 13. Kingston, the third extension candidate, reached
  90 % in 0 of 24 months (61 % for the year). (`gi.txt`, the monthly lines at the end)
- **DS-D5 · The second lens** (operating profit a year in 2032 ÷ capex, Expected; a simple yield, not a valuation):
  App 47 % · RMS 32 % · Kiosks 21 % · Breakfast 20 % · Gatwick +40 16 % · Energy 12 % · Toronto +40 12 % ·
  Kingston +40 8 % · Boston 8 % · Refresh 7.9 %. Package A = **37.5 %** ($3.53M a year on $9.4M).
  (`project_economics.csv`, RunRate2032 ÷ Capex)
- **DS-D6 · The cost of waiting.** Distribution cost rose from 8.9 % to 11.3 % of room revenue. At the 2021 mix,
  2025 commissions would be $4.8M lower. Each point of room revenue moved from agencies to the website or app is worth
  about $0.28M a year. (`gi.txt`)

### 1.3 The target spine

```
P1  [same headline] Full rooms, a slipping margin: we pay the middleman, and the welcome is fading.
    F1 the margin (the symptom)        → measured on P2 as margin after commissions, 2025 → 2032
    F2 the middleman (cause 1)         → Booking app with MEMBER RATES (direct is dearer today, DS-D2)
    F3 the fading welcome (cause 2)    → knowingly deferred: refresh = tranche 3, with the evidence that it works (DS-D3)
    F4 where we are full (opportunity) → Kiosks at the 20 fullest desks (DS-D1) + RMS prices the full nights
                                         + extensions: decided at the 2028 gate (DS-D4)
P2  Fix the middleman first: $9.4M now earns $3.5M a year by 2032. The other $50.6M waits for one test in 2028.
    hero  = ten moves, two lenses (pays back by 2032 × earns its keep a year)
    then  = what A does to F1–F4 by 2032 (ledger)  →  the $60M plan in tranches  →  the downside, bounded
    proof = all 456 packages (in "What waits, and why")  ·  challenge = Build your own
```

Why this spine is better as a story, beyond fixing the gaps:

- **It has a hard choice in it.** "We know the refresh works. We are not funding it yet, and this is when we will."
  An honest trade-off persuades more than a clean sweep, and it is what the brief asks for ("choices, risks and
  trade-offs").
- **Every P1 card gets a consequence**, including the one that is deliberately not fixed.
- **The restraint becomes a plan**, not just a number.

---

## 2 · Page 1, The Brand Review: element by element

P1 needs the least work. The changes are about setting up page 2, not about rebuilding page 1.

### DS-01 · Masthead and KPI row: make the row the index of the findings (T2)

*Absorbs: CL-01, CL-02, CL-20, UX-01 (part).*

- **What I see:** the KPI order (occupancy, margin, agencies, NPS) follows the headline order. It maps to F4, F1, F2
  and F3, but nothing on the canvas shows that mapping. NPS +3.3 has no scale. The masthead doesn't say there is a
  page 2 or who decides.
- **Ideal:**
  - Each KPI carries the code of its finding card ("F4", "F1", "F2", "F3") in the same chip style as the card kicker.
    The KPI row then reads as the table of contents of the page.
  - NPS gets its scale in the label: "Net promoter score (−100 to +100)".
  - The eyebrow gets a page count and an audience: "1 / 2 · THE BRAND REVIEW". The subtitle gets one clause saying
    who decides and what follows, for example: "For the Pillow & Key Board: what is wrong, before page 2 says what to
    fund."
- **Keep:** the peer-rank sublines. They are the best KPI anatomy in the report.

### DS-02 · F1 The margin: show the wedge, name the cause (T3)

*Absorbs: CL-18, CL-26.*

- **What I see:** two lines, before and after commissions. The story is the *gap between them*, which widens from
  8.4 to 10.6 points, but the chart asks the reader to judge that gap by eye. The note gives the gap without naming
  it. The title counts from 2023 and the note from 2021.
- **Ideal:** the gap is the mark. Either a stacked area (margin after commissions at the bottom, with the commission
  take as a labelled band on top: "the middleman's share") or the two lines with the band between them shaded and
  labelled. Use one baseline year on the card: the title and the note both count from 2021, or both from 2023.
  2021 is the depressed base year, so 2023 is the safer choice. Suggested title: "Commissions took the gain: after
  them, the margin fell 2.8 points since 2023."
- **Power BI:** a stacked area from zero is native and honest. If the specialist keeps the lines, the shaded band
  is **[verify]** (error-bar or area tricks).

### DS-06 · F2 The middleman: turn the folio table into the bridge to the app (T1)

*Absorbs: INV-DE-1 (Blocker for the investor), CL-19, CL-23, UX-15.*

- **What I see:** the strongest artefact in the report, and a note that undercuts it. "Our reading: the fullest brand
  … grows by reach and direct rebooking, not by loyalty schemes." The recommended move is "Direct booking app & member
  rates". Member rates are the loyalty lever. The table also raises a question it never answers: why does the direct
  guest pay *more*?
- **Ideal:** the table's last insight becomes the card note: **"Booked direct, the guest pays $2.25 more and we keep
  $17.47 more. Nothing rewards the guest for booking direct, and that is what member rates change."** Delete the
  loyalty sentence. The line chart drops its y axis and labels the ends ("33 %" in 2021, "50 %" in 2025), matching the
  title. That frees the 100 px chart from its cramped two ticks.
- **Forward link:** a small line at the foot of the card: "→ Page 2: Booking app with member rates."

### DS-04 · F3 The fading welcome: give the cause, then defer it on purpose (T1)

*Absorbs: J-IN-3, INV-DE-2, J-AQ-3, INV-DE-4, CL-20.*

- **What I see:** a clean three-band bar chart (+6.8 / +3.8 / −4.9) with "an association, not proof of cause". The
  bands cover 44 of 50 hotels without saying so. The card says *that* old hotels score worse but not *why the brand
  has so many old hotels*, and P2 answers it with kiosks.
- **Ideal:**
  - Keep the band bars. They are Board-friendly and correct.
  - The note gives the cause (DS-D3) in one sentence: "Since 2018 Goodnight Inn spent $1.0M per hotel on renovation;
    the other brands spent $5.9M to $7.9M. None has started since 2020."
  - Add the count under the axis or in the note: "44 of 50 hotels; 6 have no renovation date."
  - Optional, and only if it fits: the in-brand evidence that renovation works ("the seven hotels renovated in 2021
    held NPS near +6 while the rest fell to +2.7"). It belongs on P2, in the refresh card (DS-11), more than here.
- **Forward link:** "→ Page 2: the refresh, deferred to tranche 3, and why."
- **Note:** this makes the case *for* renovation stronger, and P2 then defers it. That is deliberate. The trade-off
  is the story (§1.3). The specialist must not soften it into a recommendation the numbers don't support.

### DS-07 · F4 Where we are full: replace the stubs with a capacity chart that leads somewhere (T2)

*Absorbs: J-VE-2, UX-08, CL-13, J-IN-2, J-IN-6, INV-DE-3, INV-GR-1.*

- **What I see:** three big numbers (82.0 / 79.1 / 77.5) plus seven equal 40 px column stubs for 85.2 % to 91.9 %.
  The bars encode nothing. Blue and grey have no key. Hotel names wrap. The title states a fact without an
  implication. P2 then ignores the card.
- **Ideal:** one chart for the whole card: **all 50 hotels as dots on an occupancy axis, in three rows (Airport /
  City / Highway)**, with each row's average as a tick and labelled. The seven fullest are highlighted and named, and
  a 90 % reference line reads "effectively full". The three averages stop being separate KPIs and become the ticks.
  "5 of the 7 fullest are airports" becomes visible as the top end of the airport row. The 61 % Kingston dot sits
  visibly far left, which pre-empts the "why not extend Kingston" question.
- **Title with an implication:** "Our airports run full: Toronto was above 90 % in 17 of 24 months". Or, if the
  pricing check below holds, a pricing-headroom version.
- **Note and forward link:** "→ Page 2: kiosks at the 20 fullest desks; revenue management prices the full nights;
  extensions decided at the 2028 gate."
- **Opportunity to verify [data]:** do the fullest hotels raise their rate faster than the rest of the brand? If they
  don't, F4 + F1 ("full, but not pricing like it") is the real argument for RMS (INV-GR-2). Check the ADR growth
  2023–2025 of the top 20 against the rest before it goes on the canvas. Don't argue it from a brand average against
  a single hotel: country price levels distort that comparison.
- **Power BI:** a native scatter with a categorical row index on Y, or a strip plot. Labels only on the highlighted
  dots. Hover (the hotel tooltip) stays as extra depth.

### DS-08 · P1 footer: the route to page 2 (T1)

*Absorbs: UX-01, CL-02.*

The footer row gets a page-navigation button, bottom right before Definitions: **"Next: what we fund, and why →"**.
On P1 that matters more than any polish: a judge who reads P1 alone has read half the argument.

---

## 3 · Page 2, The Investment Strategy: the ideal decision page

### 3.1 Reading order of the ideal Recommended state

A Board member's eye should get answers in this order, and the layout should force that order:

1. **The ask** (headline): how much, for what, and what happens to the rest.
2. **Why these three** (hero): the ten moves on two lenses, with A visibly the best.
3. **What it fixes** (ledger): the four P1 findings in 2025 and in 2032 with A.
4. **The plan for the $60M** (capital strip): what is committed now, what is gated, and when the Board decides again.
5. **What can go wrong** (downside, bounded) and **how to challenge it** (the two other states).

### 3.2 Target layout, Recommended state (sketch, not a spec)

```
┌─ 2 / 2 · ROOM TO INVEST ───────────────────────────────────── ← The Brand Review ─┐
│ Fix the middleman first: $9.4M now earns $3.5M a year by 2032.                    │
│ The other $50.6M waits for one test in 2028.                                      │
│ Expected case · NPV through 2032 at 8 % (contest rule) · profit a year once live  │
├─ [ Recommended: A ][ What waits, and why ][ Build your own ]   Scenario [L|E|H] ──┤  ← one page-level control row
├──────────── 7 / 12 ────────────────────┬──────────── 5 / 12 ─────────────────────┤
│ HERO · Ten moves, two lenses           │ A · Booking app + RMS + Kiosks           │
│  y: profit a year by 2032 ÷ capex      │ $9.4M · NPV +$3.3M · +$3.5M a year ·     │
│  x: NPV through 2032                   │ 37 % a year on cost                      │
│  ── 8 % line ── 0 line ──              │ Worst case (Low): −$5.5M by 2032         │
│  A's three moves: blue, labelled       ├──────────────────────────────────────────┤
│  gated/deferred: ring, labelled        │ WHAT A DOES TO THE FOUR FINDINGS BY 2032 │
│  the rest: grey, labelled              │ F2 middleman   11.3 % → ~10.1 %  partly  │
│                                        │ F1 margin      33.7 % → x %      partly  │
│                                        │ F4 full        kiosks at 20 · +0 rooms   │
│                                        │ F3 welcome     deferred → tranche 3      │
├────────────────────────────────────────┴──────────────────────────────────────────┤
│ THE $60M PLAN  [■■ T1 $9.4M 2027 ][▒▒▒ T2 gate mid-2028 ][░░░░ T3 refresh, trigger ]│
│ cumulative of A, 2027–2032, Low / Expected / High, live dates and the gate marked  │
└─ Source · Definitions ────────────────────────────────────────────────────────────┘
```

What leaves the Recommended state: the "How to read this chart" guide box (the hero labels itself), the waterfall
(its message moves into the ledger and the move table), the four-key cumulative legend, the footer "Revisit the
facts" pill (the ledger shows the findings statically), and the 456-dot scatter (it moves to "What waits, and why").

### DS-10 · The hero: ten moves on two lenses (T2, the single biggest storytelling upgrade)

*Absorbs: INV-CA-1 (Blocker), INV-CA-2, INV-CA-3, J-AQ-1, J-AQ-2, J-AQ-5, J-VE-4, CL-03, CL-06, CL-34, UX-06.*

- **What I see:** 456 grey dots and the answer in a corner. The chart proves that the search was exhaustive. A Board
  doesn't need that as the first thing it sees. It needs to see why *these three moves*.
- **Ideal:** a scatter with **ten labelled dots, one per move**:
  - X = NPV through 2032, the contest rule, with a 0 line labelled "pays back by 2032".
  - Y = profit a year by 2032 ÷ capex, with an 8 % line labelled "earns more than our 8 % cost of money".
  - Optional: dot size = capex.
  - A's three moves are blue, the gated or deferred moves are rings, and the rest are grey.
- **What the reader sees at once:**
  - App and RMS: top right. They pass both tests.
  - Kiosks: just left of zero but high on the yield axis (21 %). *That is why it is in A* (J-AQ-2, CL-06), visible
    without a sentence.
  - Gatwick (16 %): above the 8 % line but left of zero, so "good business, wrong horizon". That is the honest growth
    conversation (INV-CA-2).
  - Refresh (7.9 %): under the 8 % line even without the cut-off. That is the stronger argument to decline it
    (INV-CA-3).
  - Kingston and Boston: on the line.
- **Title:** "Two moves pass both tests; the kiosks earn 21 % a year but pay back after 2032."
- **Rules for honesty:** call it "profit a year by 2032 ÷ capex", not ROI or IRR. Add one caveat line: "late moves
  are still ramping up in 2032". Both inputs are provided data (`AnnualOperatingProfitImpactUSD`/run-rate and capex).
  The derived ratio has to be documented in a metric contract (invariant 4).
- **Power BI:** a native scatter, ten points, with data labels by move name. Fully keyboard and screen-reader
  friendly, which the 456-dot layered scatter is not (J-AC-4).

### DS-11 · "Considered" becomes "What waits, and why" (T2)

*Absorbs: J-IN-4, CL-27, UX-12, J-CI-2, INV-GR-1, INV-CA-4.*

- **What I see:** B and C cards with uneven grammar ("Breakfast instead of kiosks" / "Why not renovate?"), fixed text
  slots with holes, a placeholder-looking icon, C's contents only in its tooltip, and a C card carrying a release rule
  that contradicts the rec tile.
- **Ideal:** this state answers the Board's second question, "and the other $50.6M?":
  - **Proof, left:** the 456-package scatter lives here, smaller, with A annotated directly. Title: "We checked all
    456 packages the rules allow: none beats A on NPV through 2032." This is where the innovation earns its keep,
    as evidence and not as the opening.
  - **Three cards, one grammar** ("X: what it is · why not now · when we decide"):
    - **B, the alternative:** "Breakfast instead of kiosks: $2.25M more for $0.6M less."
    - **The growth question:** "Gatwick +40 rooms: 16 % a year on cost, full 14 of 24 months; decided at the 2028
      gate."
    - **The refresh:** "The ten oldest hotels: deferred, not rejected." Include the evidence (DS-D3), the 7.9 %
      yield, and one honest line: "the data does not price the cost of waiting, so this case is understated."
  - The cumulative comparison chart stays, with direct labels at the line ends.
- **Tab name:** "What waits, and why" says what the reader will find. "Considered: B and C" is jargon.

### DS-20 · The 2032 ledger: what A does to the four findings (T1, closes the brief's operational-impact rule)

*Absorbs: J-IN-1 (rule gap), INV-AC-1 (Blocker), INV-AC-2, J-CI-3, CL-07, J-IN-5.*

- **Ideal:** a static table of four rows, one per P1 finding, in the same F-code chips as P1. Columns: *2025* ·
  *2032 with A* · *status* (fixed / partly / deferred / not now). Under each row, in small text, the move that drives
  it, with "growth" marked where it applies (this also settles J-IN-5).

  | Finding | Measure | 2025 | 2032 with A | Status |
  |---|---|---|---|---|
  | F2 middleman | distribution cost, % of room revenue | 11.3 % | ~10.1 % **[derive]** | partly: most of the gap to the other brands remains |
  | F1 margin | operating margin after commissions | 33.7 % | **[derive]** | partly |
  | F4 full | the 20 fullest hotels: kiosks live · rooms added | 0 · 0 | 20 · 0 | rooms decided at the 2028 gate |
  | F3 welcome | guest score at the 20 kiosk hotels / the 10 oldest | **[derive]** | +0.25 pts at the 20 / unchanged | deferred: refresh in tranche 3 |

- **Rules:** every 2032 value is derived from the `InvestmentScenarios` driver columns, never estimated.
  `SatisfactionChangePts` is on the guest-score scale. Do not convert it to NPS (invariant 5, do not fabricate).
  The ~10.1 % is the investor review's derivation. Re-derive it.
- **Why it matters for the story:** this is the moment the two pages become one argument. It is also the only place
  P2 needs to show the findings, so the hover-only "Revisit the facts" can go.

### DS-21 · The $60M plan in tranches (T2)

*Absorbs: INV-RK-1 (Blocker), INV-RK-3, INV-TH-2, J-IN-4, J-AQ-6.*

- **What I see:** "$50.6M held back" is the most memorable phrase on P2, so the reader remembers what is *not* being
  done. The release rule exists in three versions: "until all three are live in Apr 2028" (rec tile), "once A has
  broken even" (C card, which means 2031), and "if NPS falls below 0" (C card). On the trend, the NPS rule fires
  first, probably before A is live.
- **Ideal:** one horizontal bar of the $60M budget, in three segments:
  - **Tranche 1:** A, $9.4M, committed in 2027.
  - **Tranche 2:** gated mid-2028, sized to what it would fund (for example Gatwick +40, $6.6M), with its test.
  - **Tranche 3:** the refresh, $29.5M, with its trigger.
  - The remainder is labelled "not needed".
- Under the bar sits the cumulative line of A (Low / Expected / High), with the live dates (RMS Jul 2027, app
  Oct 2027, kiosks Apr 2028) and the gate marked on the same time axis. *One rule, one date, one owner.*
- **Governance text is a proposal, not a model output.** The gate's tests (for example "direct share up X points by
  mid-2028") are Bjorn's call (§6, D3), and the page says they are a decision rule, not a forecast.
- **Power BI:** a stacked bar is native. Milestone markers on the line are **[verify]**: X-axis reference lines on a
  line chart, or a marker series with custom data labels. The fallback is a one-row milestone strip of text under the
  chart.

### DS-22 · The recommendation tile: sell the return, bound the downside (T1)

*Absorbs: INV-TH-1, INV-TH-2, INV-RK-2, INV-RK-4, CL-10, CL-11, UX-10, J-VE-7.*

- **What I see:** $9.4M · +$3.3M · "−5.5 to +12.7" (the unit sits in the label) · +$3.5M a year. A glowing outline
  that no other card has. A note that carries the $50.6M rule. And the downside sits in orange under a different
  chart.
- **Ideal:** the same flat card style as every other card; emphasis comes from the title.
  - Four numbers: **$9.4M** capex · **+$3.3M** NPV through 2032 · **+$3.5M** a year by 2032 · **37 %** a year on
    cost.
  - Then two lines:
    - *The downside, as a bounded loss:* "Worst case (Low): −$5.5M by 2032, still +$X a year after" **[derive the Low
      run-rate]**.
    - *The concentration, said out loud:* "The app carries the package (+$3.4M of +$3.3M); each point of room revenue
      won back from the agencies is worth about $0.28M a year."
  - One "why now" clause, if room allows: "Every year at today's channel mix costs about $X in commissions"
    (INV-TH-1, DS-D6) **[derive]**.
  - The note explains why profit a year can exceed total NPV (ramp-up and discounting, CL-10) in one clause, or the
    Definitions do.
- **Moves table instead of the waterfall** (*absorbs J-VE-5, UX-11 "Totaal"*): three rows (move · answers · live ·
  capex · NPV through 2032 · a year by 2032) with an inline bar for NPV. It shows the concentration, why kiosks are in,
  and the milestones. It also removes the native waterfall, which carries the "Totaal" label and the comma labels.

### DS-23 · Headline and subtitle of P2 (T1)

*Absorbs: INV-TH-1/2, CL-09.*

- **Today:** "Fund one package of three moves: $9.4M now, $50.6M held back." It is a decision, but it sells the
  restraint and uses two undefined words (package, move).
- **Ideal:** the ask, the return and the plan for the rest. Suggestions (Bjorn picks, D6):
  - "Fix the middleman first: $9.4M now earns $3.5M a year by 2032. The other $50.6M waits for one test in 2028."
  - "Fund $9.4M now to win back the middleman's cut; decide on the other $50.6M in 2028."
- **Subtitle:** name both lenses and the rule, and define the unit once: "Three moves (a package) out of ten on offer.
  NPV through 2032 at 8 %, the contest rule; and the profit each move adds a year once it is live."

### DS-24 · Build your own: invite it, teach the second lens with it (T2)

*Absorbs: UX-05, UX-13, CL-29, CL-31, J-AC-3, J-CI-2, INV §5 ("the best moment in the report").*

- **What I see:** the best moment in the report (the investor added Toronto and understood the cut-off in ten
  seconds). But it sits behind a neutral third tab, opens on a page full of zeros with "$0,0M Totaal", uses radio
  circles for a multi-select, and says "Tap". The plan is orange, which P1 taught as "problem".
- **Ideal:**
  - **Invite it** from the Recommended state with one line next to the tile: "Think you can beat A? Build your own →".
  - **Open from A, not from zero** (the three A moves pre-picked) if the Deneb selection can start in a state
    **[verify]**. If it can't, the empty state shows the rules and one sentence, and no numbers.
  - **Show both lenses for the plan:** NPV and "a year by 2032", so the builder teaches the trade-off instead of only
    the cut-off. Add the column "a year by 2032" to the selector table.
  - **The same ledger for your plan** (what it does to F1–F4). This is optional and only if the measures allow it.
  - Square check marks, "Click a move", and the plan in Night with a hollow ring (DS-43).

---

## 4 · Across both pages

### DS-30 · Hover carries depth, never meaning (T1)

*Absorbs: J-AC-1, J-AC-2, INV §5 (pre-read), CL-30.*

A Board pre-read is often a PDF or a tablet. Test every tooltip with one question: *if this never opens, does the
argument still hold?*

| Tooltip | Holds without it? | Target |
|---|---|---|
| tt-f2 / tt-f3 / tt-f4 (the cards in miniature) | yes | keep as depth |
| tt-f3-band, tt-f4-hotel (detail per band or hotel) | yes | keep as depth |
| tt-package (contents, range) | **no** | the contents go into the moves table (DS-22); the range strip becomes a sentence |
| tt-year (A/B/C/plan per year) | yes, after DS-21 | keep |
| "Revisit the facts" (findings on P2) | **no** | replaced by the ledger (DS-20) |
| tt-glossary (Definitions) | partly | define each term at first use in a subtitle; keep the glossary as a reference |

### DS-31 · Navigation between the pages (T1)

*Absorbs: UX-01.* P1 gets "Next →" (DS-08). P2 gets "← The Brand Review" next to the eyebrow. Both eyebrows carry
"1 / 2" and "2 / 2".

### DS-32 · One page-level control row on P2 (T2)

*Absorbs: UX-04, J-AC-5.* The state tabs and the scenario switch change the whole page, so they sit in one row
across the page, under the masthead and above the cards. In tab order they come before the hero.

### DS-33 · One control language (T3)

*Absorbs: UX-03.* One segmented control in two sizes: large for the story tabs and small for scenario and zoom.
One radius, one "on" fill. The page switch must look like the most important control on the page, because it is.

---

## 5 · System rules: colour, numbers, words

### DS-40 · Number grammar (T1)

*Absorbs: J-VE-1, J-VE-7, UX-11, CL-33, J-AC-7, INV §5.*

- **One notation everywhere:** "$9.4M", one decimal in $M, two only below $1M; signs on every change ("+$3.3M",
  "−$0.6M"); ranges carry the unit ("−$5.5M to +$12.7M"). Exceptions to the one-decimal rule ($11.65M, $3.28M in the
  tooltip) go.
- **No locale leakage:** no "Totaal" and no decimal commas, whatever the viewer's browser locale. Every number a judge
  sees on a chart label is formatted as en-US text, or the visual doesn't use a locale-dependent native label. The
  Publish to Web check in an nl or de browser is the acceptance test (UX check 5).

### DS-41 · One word per idea (T1)

*Absorbs: CL-04, CL-05, CL-15, CL-22, CL-28, CL-32, J-VE-6.*

| Idea | The one word | Retire |
|---|---|---|
| NPV through 2032 ≥ 0 | **pays back by 2032** | "broken even" in the NPV sense |
| cumulative undiscounted cash ≥ 0 | **cash positive from [year]** | "break-even", "positive from" |
| the ten options | **moves** | initiatives (except in the source line) |
| a set of moves | **package** (defined in the P2 subtitle) | plan (keep "your plan" in Build only) |
| the 2032 annual effect | **a year by 2032** | run-rate (in the glossary only), "profit a year by 2032" (shorten) |
| F1–F4 | **findings** (spelled out once on P1) | "facts" |
| the refresh | **refresh** | renovate (keep "renovation" only for the past) |
| the selected scenario | **the case in view** (subtitle only) | "Case in view" as a legend key |

The cumulative chart's title has to match its line: if the line touches zero in 2030, the title says "cash positive
from 2030" or the line starts above zero in 2031 (CL-15).

### DS-42 · The 2032 horizon, said once and in plain words (T1)

*Absorbs: CL-03, J-AQ-1.*

One sentence, on P2 at the point of first use: "The contest counts nothing after 2032, so moves that take years to
earn back look worse than they are. That's why we also show what each move earns a year once it is live." With
DS-10 on the canvas, this sentence turns the horizon trap into a demonstration of judgment.

### DS-43 · Colour roles, one meaning each (T2)

*Absorbs: UX-02, CL-12, CL-13, J-VE-8.*

| Colour | One meaning | Leaves |
|---|---|---|
| Goodnight blue | "us / our choice": Goodnight Inn on P1, package A and its moves on P2 | F4's airport colouring (rows label the type instead, DS-07) |
| Grey | context: other brands, other packages, unselected cases | — |
| Tangerine | something is wrong: a negative value, the Low-case downside, over budget | F-codes (→ Night), "your plan" (→ Night ring), package C as a line (→ grey dashed), the Low case as a line style (→ grey dashed, labelled) |
| Night | text, finding codes, controls in the "on" state, "your plan" | — |

The hover tags in Tangerine were approved on 12 Nov (doc 18). My view as storyteller: they are the sixth orange
signal on a page where orange should mean "problem". This is a conflict with a decision already taken, so Bjorn
decides (D5). I don't overrule it here.

---

## 6 · Decisions only Bjorn can make (the merge should ask, not assume)

| # | Decision | Options | My recommendation |
|---|---|---|---|
| D1 | The P2 hero | (a) ten moves on two lenses, with the 456 scatter as proof in "What waits" · (b) keep the 456 scatter as hero, annotate A, and add the second lens only in the tile and moves table | **(a).** It is the only option that answers the horizon objection visually. (b) is the fallback if time runs out |
| D2 | The growth answer | (a) A only, with Gatwick named as the tranche-2 decision at the 2028 gate · (b) A + Gatwick now ($16.0M; NPV through 2032 −$0.25M, $4.57M a year, +40 rooms) | **(a).** It keeps "pays back by 2032" true for what is funded, and still answers F4. Note: the dataset prices Gatwick from a 2027 start. A 2028 decision is governance, not a modelled number, so the page must say so |
| D3 | The single release rule | the gate date (mid-2028, when all three moves are live) and its tests | Tests that the plan itself moves: direct share or distribution cost, and the full-hotel months. Not brand NPS < 0, which the trend fires first |
| D4 | The finding-to-move mapping | today F2/F3/F1 · target F2 = app, F4 = kiosks + RMS (+ the extension decision), F3 = deferred refresh, F1 = the outcome measure | The target. It is what the data supports (DS-D1, DS-D3) |
| D5 | Hover-tag colour | Tangerine (approved 12 Nov) · Night or outline | Night, but this is Bjorn's earlier call |
| D6 | P2 headline wording | the two options in DS-23, or the current one | "Fix the middleman first: …" |

---

## 7 · What to keep, whatever else changes

- **P1's headline**, the action titles on every card, the peer-rank sublines in the KPI row.
- **The F2 folio table.** Only its note changes.
- **"An association, not proof of cause"** and the separation of fact from reading.
- **The exhaustive search** as an idea: it moves, but it stays (DS-11).
- **Build your own:** it gets invited and taught, not replaced.
- **The Low case on the page, unprompted.** Reframed as a bounded loss, never hidden.
- **The card anatomy, the masthead, the warm canvas, the tooltip skin.**
- **Dynamic alt text by measure.** The new hero (DS-10) and the ledger (DS-20) need theirs too.

---

## 8 · Smaller chart notes (T3)

| ID | Where | Note | Absorbs |
|---|---|---|---|
| DS-50 | P2 cumulative (if it stays as is) | Three cases, the selected one thicker in blue, labels at the right end; no "Case in view" key; a −$10M tick | UX-07, J-VE-6, CL-14 |
| DS-51 | P2 scatter (if kept as hero, D1-b) | The key glyphs match the marks; the guide panel is not the same blue as the payback band; A labelled in the "All packages" view | UX-06, CL-16 |
| DS-52 | Small scatter (Considered/Build) | The same lettered discs as the large one; the plan dot is a ring labelled "You", offset so B stays readable | UX-13 |
| DS-53 | tt-package | Replace the range strip with a sentence ("Low −$5.5M · Expected +$3.3M · High +$12.7M"); the table at body size; trim the empty bottom | UX-14, CL-17 |
| DS-54 | tt-f3 | Taller bars or just the three numbers; the tooltip must not be smaller than the card it explains | UX-14 |
| DS-55 | Footer pill | Retire it on P2 (the ledger replaces it, DS-20). If it stays: a white fill, centred separators | UX-09 |
| DS-56 | Smallest text | Source lines, legends and footer at ≥ 12 px at the canvas's native size; check at "fit to page" on a 1366 px laptop | J-AC-6 |
| DS-57 | Layered scatters | Every overlay visual has alt text or is removed from the tab order | J-AC-4 |
| DS-58 | Eyebrow puns | Keep them; each eyebrow sits beside a plain label ("F3 · The fading welcome"), which already decodes it | CL-24 |

---

## 9 · Checks the specialist must run before anything lands

1. **Re-derive every DS-D figure in the model** (kiosk hotels = 20 fullest, renovation spend per hotel, the 2021
   cohort NPS, months ≥ 90 %, yield per move, $0.28M per point). These figures come from the offline decode.
2. **Check that running costs are in the operating-profit impact** (INV-CA-5). If they aren't, the yields and A's
   +$3.5M change.
3. **Check the brief's visual count after the swaps.** There must still be ≥ 4 built-in visual types after the
   waterfall goes and the F4 columns become a scatter. Lines, area or line, columns (F3), scatters and tables keep it
   well above 4.
4. **Publish to Web:** locale in an nl/de browser, Deneb selector rendering and keyboard use, tooltip scale at
   1366 px, visual-header icons against the hover tags, touch.
5. **Keyboard and screen-reader pass** over the new hero, ledger and capital strip.
6. **Desktop discipline** (project memory): commit before opening Desktop, close every window without saving.

---

## 10 · Merge map: every role-review ID and where it lands here

| Other review IDs | Lands in |
|---|---|
| J-IN-1, J-CI-3, INV-AC-1, INV-AC-2, CL-07 | DS-20 ledger |
| J-IN-2, J-IN-6, INV-GR-1, INV-GR-2, INV-DE-3, J-VE-2, UX-08, CL-13 | DS-07 F4 + DS-11 growth card + D2 |
| J-IN-3, INV-DE-2, J-AQ-3, INV-DE-4 | DS-04 F3 + DS-D1/D3 + D4 |
| INV-DE-1, CL-19, CL-23, UX-15 | DS-06 F2 bridge |
| J-AQ-1, J-AQ-2, J-AQ-5, INV-CA-1/2/3, CL-03, CL-06, CL-34, J-VE-4 | DS-10 hero + DS-42 |
| INV-RK-1, INV-RK-3, J-IN-4, J-AQ-6, INV-CA-4 | DS-21 capital plan + D3 |
| INV-TH-1/2, INV-RK-2/4, CL-09, CL-10, CL-11, UX-10, J-VE-5, J-VE-7 | DS-22 tile + moves table, DS-23 headline |
| UX-05, UX-13, UX-16, CL-29, CL-31, J-AC-3, J-CI-2 | DS-24 Build your own |
| J-AC-1, J-AC-2, CL-30 | DS-30 hover |
| UX-01, CL-01, CL-02 | DS-01, DS-08, DS-31 |
| UX-03, UX-04, J-AC-5 | DS-32, DS-33 |
| J-VE-1, UX-11, CL-33, J-AC-7 | DS-40 |
| CL-04, CL-05, CL-15, CL-22, CL-28, CL-32, J-VE-6, UX-07, CL-14 | DS-41, DS-50 |
| UX-02, CL-12, J-VE-8 | DS-43 + D5 |
| UX-06, UX-09, UX-12, UX-14, CL-16, CL-17, J-AC-4, J-AC-6, CL-24 | §8 |
| J-CI-1 (over-engineered) | addressed by subtraction: DS-10 swaps 456 dots for 10, and P2 loses the guide box, the waterfall, the footer pill and a legend |

## Open questions

- D1 to D6 (section 6).
- Does the Deneb selector support a pre-selected start state (DS-24)? **[verify]**
- Can the line chart carry date markers for the live dates and the gate under Publish to Web (DS-21)? **[verify]**
- Do the 20 kiosk hotels have higher check-in complaint rates than the other 30? If so, that is the clincher for
  DS-D1, and it belongs in the moves table. **[data]**
- Do the fullest hotels raise their rate more slowly than the rest (DS-07)? **[data]**

---

## Addendum (13 Nov, later): approved, and three data checks

Bjorn approved this target and decisions D1 to D6 as recommended. The build contract is
`20-requirements-storytelling-2026-11-13.md`. While writing it, three checks against the workbook
(`analysis/50_storytelling_checks.py`) changed details here:

- **DS-07's pricing angle is refuted.** The 20 fullest hotels raised their rate slightly faster than the other 30
  (+2.9 % vs +2.6 %, 2023 to 2025). Revenue management stays filed under F1, not F4.
- **DS-02's suggested title overstated the commission share.** Since 2023 the margin after commissions fell
  2.72 points: 1.8 from running costs (staff +1.3 points of revenue) and 1.0 from commissions. F1 now names both.
  The canvas says 2.8; doc 20 has a check item (C0) for this.
- **DS-D1 is confirmed with complaint data.** Check-in complaints at the 20 kiosk hotels rose from 0.88 to 1.26 per
  1,000 room nights; at the other 30, from 0.88 to 0.98.
