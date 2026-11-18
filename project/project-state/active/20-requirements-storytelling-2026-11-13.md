# 20 · Requirements: the storytelling rebuild (13 Nov 2026)

**For:** the build planner (turns this into a phased build plan) and then the builder (`pbir-operator`, through
the generators). **Status:** approved by Bjorn on 13 Nov. He accepted the target in doc 19 and all six decisions
(D1–D6) as recommended there. This document is the contract. Deviations go back to Bjorn; they are not decided in
the build.
**Amended 13 Nov:** five construction points from `21-powerbi-build-guideline-2026-11-13.md` (section 2.2,
N-1 to N-5), approved by Bjorn. Each is marked **Amendment** at its requirement and listed in the section
"Amendments" near the end. Where this document and doc 21 differ on construction, doc 21 decides.
**Source:** `19-review-dataviz-storytelling-2026-11-13.md` (the why). It absorbs `19-jury-review`,
`19-review-ui-ux`, `19-investor-review` and `19-review-clarity-newcomer`. Each requirement lists the IDs it closes.
**Deadline:** submission is planned for 17 Nov (contest closes 18 Nov). Section 1 sets the cut line.

**How to read a requirement.** Each one has these parts:

- **What:** the outcome, not the implementation. The builder chooses how.
- **Copy:** exact text, where the wording matters. Copy marked *(Expected)* is the Expected-case version. If the
  visual follows the scenario slicer, the builder writes the Low and High variants in the same grammar.
- **Data:** the values the result must show (Expected unless stated), for acceptance. Every value is re-derived in
  the model. Never type a number in by hand (invariant 5).
- **Done when:** the acceptance check, judged on a fresh render.
- **Closes:** the review IDs it resolves.

**Build context (unchanged rules):**

- The generators are the source of truth: `tools/opzet_report.py`, `tools/sketch_model.py`,
  `design-prototypes/opzet-layout.json`, `opzet-layering.json`, `tools/build_selector_spec.py`.
- No Desktop saves. Commit before opening Desktop, and close every window without saving (memory:
  `desktop-afsluiten-aan-het-eind`).
- Renders use the throwaway-copy method. Delete `PillowKey.SemanticModel/definition/cultures` after every
  `opzet_report.py` run.
- Every new measure gets a docstring, a display folder and a format string. A new KPI-like metric (the yield, the
  ledger values) gets a metric contract (invariant 4).
- Canvas: 1920 × 1080 on every page. The rest of the design system (8 px grid, one radius system, one card style per
  page) stays as it is.

---

## 0 · Facts established on 13 Nov (the evidence behind the copy)

Reproducible: `analysis/50_storytelling_checks.py <PillowKey_Dataset.xlsx>` → `analysis/output/storytelling_checks.txt`.
Package figures come from `analysis/output/packages.csv` / `packages.txt`.

| # | Fact | Value |
|---|---|---|
| E1 | The kiosk hotels (GI-02) are exactly the 20 highest-occupancy hotels of 2025 | lowest kiosk hotel 81.4 %; the 21st (Nashville) 81.0 %. All seven F4 hotels are in the set. The data itself names the project "Self check-in kiosks - 20 busiest hotels" |
| E2 | Check-in complaints per 1,000 room nights, 2021 → 2025 | kiosk 20: 0.88 → **1.26** (+43 %); other 30: 0.88 → 0.98 |
| E3 | Room-condition complaints, 2021 → 2025 | rising in both groups: 1.53 → 1.78 and 1.54 → 1.81; the largest category |
| E4 | ADR growth 2023 → 2025, fullest 20 vs the other 30 | +2.9 % vs +2.6 %. **The "full but not pricing like it" idea is NOT supported. Do not use it.** RMS stays filed under F1 |
| E5 | Months at or above 90 % occupancy, 2024–2025 | Toronto 17 of 24 · Gatwick 14 · Montréal 13 · Kingston 0 (61.2 % for 2025) |
| E6 | Margin after commissions, 2023 → 2025 | 36.45 % → 33.73 % = **−2.72 pt**: operations −1.8 pt (staff cost +1.3 pt of revenue), commissions −1.0 pt. Since 2021 the commission take grew 8.4 → 10.6 % of revenue |
| E7 | Direct vs agency, one room night 2025 (already on P1) | the guest pays $111.56 direct vs $109.31 via an agency (+$2.25); Goodnight Inn keeps $107.10 vs $89.63 (+$17.47) |
| E8 | Renovation | spend since 2018: $1.0M per Goodnight Inn hotel vs $5.9M–$7.9M at the sister brands. No renovation has started since Dec 2020. The seven hotels renovated in 2021: NPS 6.4 → 6.3 (2021 → 2025); the rest of the brand 8.9 → 2.7 (`crosscheck.txt`, `gi.txt`) |
| E9 | Profit a year by 2032 ÷ capex (Expected) | App 47.0 % · RMS 32.0 % · Kiosks 20.5 % · Breakfast 19.8 % · Gatwick +40 15.8 % · Energy 11.8 % · Toronto +40 11.5 % · Kingston +40 8.2 % · Boston 8.1 % · Refresh 7.9 %. Package A 37.5 %; tranche 2 (Gatwick + Toronto) 13.8 % on $12.4M |
| E10 | Package A | capex $9.4M; NPV through 2032 L/E/H −$5.5M / +$3.3M / +$12.7M; a year by 2032 L/E/H +$1.0M / +$3.5M / +$6.2M; the app alone is +$3.4M NPV (E) |
| E11 | The 2032 ledger (2025 brand + A at full effect, 2025 dollars) | margin after commissions 33.7 % → L 34.1 / **E 35.1** / H 36.1 %. Distribution cost, % of room revenue: 11.3 % → L 10.7 / **E 10.1** / H 9.5 %. The app's commission saving: L $1.2M / **E $2.4M** / H $3.6M a year |
| E12 | Running costs ($0.6M app, $0.3M RMS) are netted in `AnnualOperatingProfitImpactUSD` | GI-10 reconciles to the dollar (768,141 vs 768,000). Answer to INV-CA-5: "included" |
| E13 | Each point of room revenue moved from agencies to the website or app | ≈ $0.28M a year (`gi.txt`) |

**Check item C0 (before any copy changes):** P1 says the margin after commissions fell **2.8** points since 2023
(KPI subline and F1 title). Unrounded, it is **2.72**. Find out whether the model's measure differs from E6 or the
canvas subtracts two rounded values. Then use one correct number everywhere (2.7 if E6 holds).
**C0 resolved (13 Nov, doc 21 N-2; Bjorn: only true data, nothing made up): 2.8.** The canvas subtracts the two
shown values (36.5 % and 33.7 %), and the two parts are real values rounded to one decimal (operations 1.77,
commissions 0.97, shown as 1.8 and 1.0). Nothing is adjusted to fit. The exact fall stays 2.72 (E6).

---

## 1 · Priorities and the cut line

| Tier | Meaning | Requirements |
|---|---|---|
| **T1** | Must ship. Without these the report can't reach 9: rule gap, contradictions, hygiene | R-G1–G4, R-P1-3/4/5/6/8, R-P2-1, R-P2-2 (position), R-P2-4/5/6/10/12, the gate copy of R-P2-7, R-W-2 (copy), R-B-3, R-TT-1, R-X-1/2/3 |
| **T2** | Should ship. Makes P2 a decision page | R-P1-1/2/7, R-P2-2 (styling), R-P2-3, R-P2-7 (charts), R-P2-8/9, R-W-1/3, R-B-1/2, R-TT-2 |
| **T3** | Polish | R-P1-9, R-P2-11, R-W-4, R-B-4, R-TT-3/4 |

**Cut line:** if R-P2-3 (the two-lens hero) can't be built and verified by the evening of 15 Nov, fall back to
**R-P2-3-FB**: the 456 scatter stays as the hero in Recommended, and everything else in this document still applies.
Every other T2 item is independent of the hero.

**Suggested order:** model measures (yield, ledger, gate text, formats) → P1 copy and colour → P2 Recommended →
What waits → Build → tooltips → accessibility pass → render set → Publish to Web gate.

---

## 2 · Global requirements (both pages)

### R-G1 · Number grammar, locale-proof (T1)

- **What:** one notation everywhere a judge can see a number.
  - **Money:** `$` + one decimal + `M` ($9.4M, +$3.3M, −$0.6M). Two decimals only below $1M. No "$11.65M", no
    "$3.28M", including in tooltips.
  - **Changes** carry a sign (+ or −, true minus sign).
  - **Ranges** carry the unit on both ends: "−$5.5M to +$12.7M".
  - **Percentages:** one decimal with a space before % only where the house style already does so. Keep the
    current style ("79.4%"), but use it consistently.
  - **Points:** "pt".
- **No locale leakage:** no "Totaal" and no decimal comma on any visual, whatever the viewer's locale.
- **Done when:**
  - The nl-NL Desktop render of every page, state and tooltip shows decimal points only and no Dutch word.
  - A Publish to Web check in an nl or de browser shows the same.
  - A text search of all text measures finds no 2-decimal $M value ≥ $1M.
- **Closes:** J-VE-1, J-VE-7, UX-11, CL-33, J-AC-7, INV §5.

### R-G2 · One word per idea (T1)

- **What:** use exactly these terms in titles, notes, tiles, tooltips and alt text.

  | Idea | Term | Never |
  |---|---|---|
  | NPV through 2032 ≥ 0 | "pays back by 2032" | "broken even" for NPV |
  | cumulative undiscounted net ≥ 0 | "cash positive from [year]" | "break-even" as a verb, "positive from" |
  | the ten options | "moves" | "initiatives" (allowed only in the source line) |
  | a set of moves | "package" | "plan" (except "your plan" in Build) |
  | `[2032 Run-rate]` | "a year by 2032" | "run-rate" (allowed only in the glossary), "profit a year by 2032" |
  | run-rate ÷ capex | "a year on cost" | ROI, IRR, yield (allowed only in the glossary) |
  | F1–F4 | "findings" | "facts" |
  | GI-07 | "the refresh" | "renovate" (for the move) |
  | tranche 1/2/3 | "tranche" | "phase", "wave" |
  | the mid-2028 decision | "the 2028 gate" | "trigger", "revisit" |

  The chart line "Break-even" at $0M on cumulative charts becomes "Cash positive above this line".
- **Done when:** a text search of the report definition and the text measures finds none of the "Never" words in a
  visible string.
- **Closes:** CL-04, CL-05, CL-28, CL-32, CL-22 (with R-TT-3).

### R-G3 · Colour roles: one meaning per colour (T1 for "your plan", T2 for the rest)

| Colour | The only meaning | Changes |
|---|---|---|
| Goodnight blue | "us / our choice": Goodnight Inn on P1; package A and its three moves on P2 | F4 no longer uses blue for "airport" (R-P1-7) |
| Grey | context: peers, other packages, unselected cases, moves not funded | — |
| Night | text, finding codes, controls "on", gated moves (tranche 2/3), "your plan" | the F-code kickers move from Tangerine to Night; "your plan" moves from orange to Night (line solid, dot as a hollow ring) |
| Tangerine / Burnt Tangerine | something is wrong: negative values, the Low-case downside, over budget | no longer used for: F-codes, the Low-case *line*, package C's *line*, "your plan", the hover pill fills |

- **Hover tags (D5):** white or Ice pill with a hairline and Night text. The ⓘ glyph may keep Tangerine as the one
  link to the orange tooltip band. This replaces the doc-18 Tangerine pill. Bjorn approved the change on 13 Nov via
  doc 19.
- **Done when:** on every render, every orange mark is either a negative/warning value or an ⓘ glyph.
- **Closes:** UX-02, CL-12, CL-13, J-VE-8.

### R-G4 · Hover adds depth; it never carries the argument (T1)

- **What:** everything a Board member needs to vote is static on the canvas. Tooltips stay, as depth only.
  - The P2 findings are covered by the ledger (R-P2-5).
  - Package contents are covered by the hero and the tile (R-P2-3/4).
  - The glossary terms used in a title are defined at first use in a subtitle (R-P2-1).
- **Done when:** with every tooltip disabled, a reader can state the recommendation, its cost and return, what it
  does to F1–F4, what happens to the other $50.6M and when, and the worst case.
- **Closes:** J-AC-1, J-AC-2 (partly; keyboard pass in R-X-1), INV §5, CL-30.

---

## 3 · Page 1, The Brand Review

### R-P1-1 · Masthead: page count and audience (T2)

- **Copy:**
  - Eyebrow: "1 / 2 · THE WAKE-UP CALL · THE BRAND REVIEW".
  - Subtitle: "Goodnight Inn in 2025, against the three other Pillow & Key Group brands. For the Board: what is
    wrong, before page 2 says what to fund."
- **Keep:** the headline, word for word.
- **Closes:** CL-01, UX-01 (part).

### R-P1-2 · KPI row as the index of the findings (T2)

- **What:** each KPI shows the code of its finding card, in the same chip style as the card kickers (Night, R-G3).
  - Occupancy → F4, Margin → F1, Agencies → F2, NPS → F3.
  - The NPS label carries its scale.
- **Copy:** NPS label: "Guest quality: net promoter score (−100 to +100)". The margin subline uses the C0-checked
  number.
- **Done when:** a reader can match every KPI to a card without reading the cards.
- **Closes:** CL-02, CL-20.

### R-P1-3 · F1 The margin: show the wedge, split the fall honestly (T1 copy, T2 chart)

- **Chart (T2):** the commission take is visible as a band.
  - Preferred: a stacked area of "after commissions" with "commissions" on top. The top edge equals "before
    commissions".
  - Allowed: the two current lines with the band between them shaded.
  - Both series are labelled directly, with no legend. The band is labelled "Commissions".
- **Copy (T1):**
  - Title: "After commissions, the margin fell 2.8 points since 2023" (C0 resolved: 2.8, the difference of the
    two shown values).
  - Note: "Commissions took 1.0 of those points and running costs 1.8 (staff rose from 26.9% to 28.3% of revenue).
    Room rates rose 2.7%, in line with the other brands, so no price premium absorbs it."
- **Forward link (T1):** a last line in the note, in the forward-link style (R-P1-8): "→ Page 2: revenue
  management and the kiosks."
- **Data:** E6.
- **Done when:** the note's numbers add up to the title's number, and title and note use the same base year.
- **Closes:** CL-18, CL-26; also corrects doc 19 DS-02 (its proposed title overstated the commission share).

### R-P1-4 · F2 The middleman: the folio becomes the bridge to member rates (T1)

- **Copy:**
  - Note: "Booked direct, the guest pays $2.25 more and we keep $17.47 more. Nothing rewards the guest for booking
    direct; member rates change that. At the 2021 channel mix, 2025 commissions would be $4.8M lower."
  - **Delete** "Our reading: … not by loyalty schemes."
  - Forward link: "→ Page 2: the booking app with member rates."
- **Chart:** no y axis. End labels on the Goodnight Inn line ("33%" at 2021, "50%" at 2025) and one end label on the
  peer line. Use the vertical space this frees to give the line chart room. No collision between a y tick and the x
  axis.
- **Data:** E7.
- **Done when:** no sentence on P1 contradicts the app's member rates, and the chart's end labels match the title.
- **Closes:** INV-DE-1, CL-19, CL-23, UX-15, J-VE-3.

### R-P1-5 · F3 The fading welcome: the cause, and the honest count (T1)

- **Chart:** keep the three band bars. Under the axis or in the note: "44 of 50 hotels; 6 have no renovation date."
- **Copy:**
  - Note: "Since 2018 Goodnight Inn spent $1.0M per hotel on renovation; the other brands spent $5.9M to $7.9M.
    None has started since 2020. Older hotels lose guest loyalty before they lose rooms: an association, not proof
    of cause."
  - Forward link: "→ Page 2: the refresh waits for the 2028 gate, and why."
- **Data:** E8.
- **Done when:** the bands' hotel counts plus the six named exclusions add up to 50.
- **Closes:** J-AQ-3, INV-DE-4, J-IN-3 (with R-P2-5), CL-20 (with R-P1-2).

### R-P1-6 · F4 Where we are full: the implication in the title (T1 copy)

- **Copy:**
  - Title: "Our airports run full: Toronto topped 90% occupancy in 17 of the last 24 months".
  - Note or subtitle line: "Gatwick did in 14, Montréal in 13; Kingston, the third extension on offer, in none."
  - Forward link: "→ Page 2: kiosks at the 20 busiest hotels; extensions decided at the 2028 gate."
- **Data:** E5. ("Topped 90%" means the month's average occupancy was at or above 90%. The tooltip or the glossary
  says so.)
- **Closes:** J-IN-6, INV-DE-3, CL-02.

### R-P1-7 · F4 chart: all 50 hotels as dots, three rows (T2)

- **What:** replace the three big numbers (`c_f4_types`) and the seven column stubs (`ch_f4_fullest`) with one chart
  across the card.
  - **Layout:** rows Airport / City / Highway. X = occupancy 2025 (axis about 60% to 95%). Each dot is a hotel.
  - **Row averages:** each row's average is a labelled tick (82.0% / 79.1% / 77.5%).
  - **Highlights:** the seven fullest hotels are labelled by short name; the 90% line is labelled "90%".
  - **Colour:** dots grey; the seven highlighted dots in Night. Blue is reserved (R-G3). Location type is carried
    by the row, not by colour.
  - **Hover:** the hotel tooltip (`tt-f4-hotel`) stays bound to the dots.
- **Done when:**
  - All 50 dots are present and the three row averages match the current KPIs.
  - "5 of the 7 fullest are airports" is visible without reading labels.
  - Kingston is visibly at the far left of its row.
  - No hotel name wraps.
- **Power BI:** a native scatter with a numeric row index plus text row labels, or the existing layered-scatter
  technique for the labelled seven. Deneb only if native fails.
- **Closes:** J-VE-2, UX-08, CL-13.

### R-P1-8 · Forward links and the route to page 2 (T1)

- **What:**
  - Each F card ends with its "→ Page 2: …" line (copy in R-P1-3 to R-P1-6), in one forward-link style: small,
    Night, not a button.
  - The footer gets a **page-navigation button** to P2, left of Definitions, in the control style of R-P2-2.
- **Copy:** "Next: what we fund, and why →".
- **Done when:** the button navigates in Desktop and in Publish to Web, and it is in the tab order after F4.
- **Closes:** UX-01, CL-02.

### R-P1-9 · P1 polish (T3)

- The KPI good-news subline stays blue (it is Goodnight Inn's own rank). No other changes.
- The smallest text on the page is ≥ 12 px at the 1920 canvas (J-AC-6).

---

## 4 · Page 2, The Investment Strategy: shared frame (all three states)

### R-P2-1 · Masthead: the ask, the return, the plan for the rest (T1)

- **Copy:**
  - Eyebrow: "2 / 2 · ROOM TO INVEST · THE INVESTMENT STRATEGY", with "← The Brand Review" next to it as a
    page-navigation button (R-P2-2 style, small).
  - Headline: "Fix the middleman first: $9.4M now earns $3.5M a year by 2032."
  - Subtitle (two lines allowed inside the masthead): "The other $50.6M waits for one Board decision in mid-2028.
    Expected case. NPV through 2032 at 8% in 2025 dollars is the contest's rule and counts nothing after 2032, so
    we also show what each move earns a year once it is live."
  - The case word ("Expected case.") follows the scenario slicer.
- **Data:** E10.
- **Done when:** the headline fits on one line at the current headline size, the subtitle wraps to at most two
  lines, and the masthead height is unchanged.
- **Closes:** INV-TH-1/2, CL-09, CL-03, J-AQ-1 (the statement half; R-P2-3 is the visual half).

### R-P2-2 · One page-level control row, one control language (T1 position, T2 styling)

- **Position:**
  - The state tabs and the scenario switch sit **outside every card**, preferably in the right half of the masthead
    (x ≈ 1208–1888, beside the headline). The cards gain the vertical space.
  - Order: tabs first, then the scenario. Tab order: masthead → tabs → scenario → content.
- **Tab copy:** "Recommended: A" · "What waits, and why" · "Build your own". Scenario label "Scenario", pills "Low" ·
  "Expected" · "High".
- **One control language:** one segmented control in two sizes (large for the tabs; small for scenario and the
  P1/P2 navigation buttons). One radius, one "on" fill, one "off" outline, valid on the Night masthead (contrast ≥
  4.5:1 for the text in both states).
- **Stability:** the controls keep the same x/y in all three states.
- **Done when:** in every state no control sits inside a card; the three tabs and three pills share one component
  look; the keyboard reaches them before the hero.
- **Closes:** UX-03, UX-04, J-AC-5.

### R-P2-12 · Footer (T1)

- **What:**
  - Source line: "Source: Pillow & Key Group dataset and finance parameters (8% discount rate, 2025 dollars,
    horizon 2032). Parts are rounded to add up."
  - The Definitions chip stays.
  - **Remove** the "Revisit the facts" pill and the F1–F4 footer chips (`z_pill_facts`, `chip_f1`–`chip_f4`). The
    ledger replaces them (R-P2-5).
- **Closes:** UX-09, J-AC-1 (part).

---

## 5 · P2 state "Recommended: A"

### R-P2-4 · Layout of the Recommended state (T1 for the frame, T2 for the hero)

- **Target grid** (planner may adjust within ± 32 px):

  | Row | Left | Right |
  |---|---|---|
  | Top (≈ y 168–688) | **hero card** (≈ 1040 wide): R-P2-3 | **decision card** (≈ 800 wide): recommendation tile (R-P2-6) and the ledger (R-P2-5) below it |
  | Bottom (≈ y 704–1016) | **capital-plan card**, full width: R-P2-7 | |

  All three P2 states then share one skeleton: two cards on top, one full-width card below.
- **Retire from Recommended:** the 456-dot hero and its overlays (`hero_packages` and the hover layers), the view
  switch `sl_view`, the guide box (`c_guide_*`, the tint tile), the waterfall `ch_rec_waterfall`, and the
  `c_uncertainty` line (its content moves into the tile).
- **Done when:** the Recommended render shows exactly three cards, one control row and the footer.
- **Closes:** J-VE-9, J-CI-1.

### R-P2-3 · The hero: ten moves, two lenses (T2)

- **What:** one row per move (10 rows), with a fixed order sorted by the Expected "a year on cost", high to low.
  The order does not change with the scenario. Two aligned panels share the rows:
  - **Left panel, "A year on cost":** bars, a reference line at **8%** labelled "8%: our cost of money", and value
    labels.
  - **Right panel, "NPV through 2032":** diverging bars around a **0** line labelled "pays back by 2032 →", with
    value labels.
  - **Row label:** move name · finding code, plus "growth" where `GrowthInitiative = Yes`. For example: "Booking app
    & member rates · F2 · growth".
  - **Status:** colour (R-G3: A = blue, gated = Night, not now = grey) **plus a text status** per row ("A",
    "2028 gate", "not now"). Status is never carried by colour alone.
  - **Scenario:** all values follow the scenario slicer.
- **Copy:**
  - Title *(Expected)*: "Two moves pass both tests; the kiosks earn 20.5% a year on cost but pay back after 2032".
  - Caption line: "A year on cost = what a move adds to operating profit in 2032 ÷ what it costs. Late moves are still
    ramping up in 2032."
- **Data (Expected):**

  | Order | Move | Finding | Status | Capex | A year on cost | NPV through 2032 |
  |---|---|---|---|---|---|---|
  | 1 | Booking app & member rates | F2 · growth | A | $5.0M | 47.0% | +$3.4M |
  | 2 | Revenue management | F1 · growth | A | $2.4M | 32.0% | +$0.5M |
  | 3 | Kiosks at the 20 busiest hotels | F4 | A | $2.0M | 20.5% | −$0.6M |
  | 4 | Breakfast upgrade | F3 · growth | not now | $4.3M | 19.8% | −$1.1M |
  | 5 | Gatwick +40 rooms | F4 · growth | 2028 gate | $6.6M | 15.8% | −$3.5M |
  | 6 | Energy programme | F1 | not now | $15.0M | 11.8% | −$12.2M |
  | 7 | Toronto +40 rooms | F4 · growth | 2028 gate | $5.8M | 11.5% | −$3.7M |
  | 8 | Kingston +40 rooms | F4 · growth | not now | $5.4M | 8.2% | −$3.9M |
  | 9 | Boston new hotel | F4 · growth | not now | $24.8M | 8.1% | −$18.3M |
  | 10 | Refresh, 10 oldest hotels | F3 | 2028 gate | $29.5M | 7.9% | −$27.3M |

- **Metric contract:** "A year on cost" = `[2032 Run-rate]` ÷ capex, per move and per package, scenario-aware.
  Document it as a derived ratio, "not a valuation".
- **Power BI:**
  - Preferred: two native bar charts with identical sort, row height and padding, the category axis shown on the
    left panel only, and the constant line from the analytics pane.
  - Allowed: one table with SVG bar measures, provided value text is also present for screen readers.
  - Keep the hover tooltip `tt-package` off this visual. The rows are moves, not packages.
- **Done when:**
  - The rows align to the pixel between the panels.
  - The order is the table above in all three scenarios.
  - A, gated and not-now are distinguishable in greyscale.
  - Labels never collide.
  - Dynamic alt text names the top three moves and the 8% line.
- **Closes:** INV-CA-1/2/3, J-AQ-1, J-AQ-2, J-AQ-5, J-VE-4, CL-06, CL-34, UX-06, J-IN-5.

### R-P2-3-FB · Fallback if the hero misses the cut line (T1 only when invoked)

- **What:**
  - Keep the 456 scatter as the hero.
  - Annotate A in the "All packages" view ("A · $9.4M, pays back by 2032").
  - Key glyphs equal the real marks; the guide panel gets a neutral tint instead of `#EAF2FB`.
  - The decision card's tile carries "37.5% a year on cost". The ledger and the capital plan still ship.
- **Closes:** UX-06, CL-16, CL-34 (part).

### R-P2-5 · The 2032 ledger: what A does to the four findings (T1)

- **What:** a static four-row block in the decision card, under the tile.
  - **Columns:** finding chip (F-code + name, Night) · measure · 2025 · 2032 with A · status word.
  - **Second line per row:** a small second line names the move(s) that act on it.
  - **Order:** F2, F1, F4, F3. Fixed first, then partly, then deferred.
  - **Scenario:** values follow the scenario slicer.
- **Copy and data (Expected; Low/High from E11):**

  | Chip | Measure | 2025 | 2032 with A | Status | Second line |
  |---|---|---|---|---|---|
  | F2 The middleman | distribution cost, % of room revenue | 11.3% | 10.1% | half the rise since 2021 undone | booking app with member rates |
  | F1 The margin | operating margin after commissions | 33.7% | 35.1% | half the fall since 2023 recovered | app + revenue management + kiosks |
  | F4 Where we are full | self check-in at the 20 busiest hotels · rooms added | 0 of 20 · 0 | 20 of 20 · 0 | rooms decided at the 2028 gate | kiosks live Apr 2028; guest score +0.25 there (dataset units) |
  | F3 The fading welcome | refresh of the 10 oldest hotels | not started | not started | deferred to the 2028 gate | why: R-W-2 |

- **Rules:**
  - "2032 with A" = the 2025 brand plus A's annual impacts at full effect, in 2025 dollars (the dataset's base-year
    convention). Say so in one caption: "2025 brand plus A's full yearly effect, in 2025 dollars."
  - `SatisfactionChangePts` stays in dataset units: never summed, never shown as NPS (decision in doc 04).
  - Don't put channel share in 2032. The data models the app as distribution cost, not as share.
- **Done when:** the Expected render shows exactly the values above (re-derived), and Low/High show E11's values.
- **Closes:** J-IN-1 (the operational-impact rule), INV-AC-1/2, J-CI-3, CL-07, J-IN-2 (with R-W-1), J-IN-3.

### R-P2-6 · The recommendation tile: return, downside, concentration, urgency (T1)

- **Style:** the same flat card treatment as every other card. **No glow, no blue outline.** The emphasis comes
  from the title and the blue A chip.
- **Copy:**
  - Title: "Our recommendation: package A".
  - Mix line: "Booking app with member rates + Revenue management + Kiosks at the 20 busiest hotels".
  - Four numbers: "$9.4M" capex · "+$3.3M" NPV through 2032 · "+$3.5M" a year by 2032 · "37.5%" a year on cost.
  - Line 1, the downside *(Expected view; always shows Low)*: "Worst case (Low): −$5.5M through 2032, and still
    +$1.0M a year by 2032."
  - Line 2, the concentration and urgency *(Expected)*: "The app carries it: +$3.4M of the +$3.3M. Every year
    without it leaves about $2.4M with the agencies."
  - Remove the old note ("Each move answers… waits until all three are live in Apr 2028…").
- **Data:** E10, E11, E13.
- **Done when:** the tile reads the same at a glance in all three scenarios, and no release rule appears in it (the
  rule lives only in R-P2-7).
- **Closes:** INV-TH-1, INV-TH-2, INV-RK-2, INV-RK-4, CL-10, CL-11, UX-10, J-VE-7.

### R-P2-7 · The capital plan: $60M in three tranches, one gate (T2; the gate copy is T1)

- **Amendment (doc 21 N-5, approved 13 Nov):** the budget bar runs full width on top; below it the gate copy
  sits left and the cumulative chart right. Two full-width elements plus the gate copy do not fit the card.
- **What:** the full-width bottom card, with two stacked elements on one time story.
  - **The budget bar:** one horizontal bar of $60.0M in four segments, labelled inside or directly above:
    - **Tranche 1 · package A · $9.4M · 2027** (blue).
    - **Tranche 2 · Gatwick and Toronto +40 rooms · $12.4M · 2028 gate** (Night).
    - **Tranche 3 · the refresh · $29.5M · 2028 gate** (Night, lighter tint).
    - **Not needed · $8.7M** (grey).
    - Each gated segment shows "a year once live" and "a year on cost": T2 +$1.7M · 13.8%; T3 +$2.3M · 7.9%.
  - **The cumulative line of A**, 2027–2032:
    - The selected case thick and blue; the other two thin grey (Low dashed, High dotted).
    - Direct labels at the right end ("Low −$X", "Expected +$X", "High +$X"); no legend.
    - y ticks including one below zero; the zero line labelled "Cash positive above this line".
  - **A milestone strip** aligned to the chart's year axis: "RMS live Jul 2027 · App live Oct 2027 · Kiosks live
    Apr 2028 (they need the app) · The 2028 gate · Cash positive 2031 (Expected)".
- **Gate copy (T1, also used verbatim in R-W-2/R-W-3):** "The 2028 gate, once all three moves are live: the Board
  releases tranche 2 if distribution cost has fallen at least 0.6 points (the app's Low case) and Gatwick and
  Toronto still topped 90% in 6 of the last 12 months. The refresh comes back to the same meeting with a case that
  looks beyond 2032. A decision rule, not a forecast."
- **Title:** "The $60M plan: $9.4M now, two decisions in 2028".
- **Rules:**
  - Tranche 2 and 3 show **no NPV**. The dataset prices every move from a 2027 start, so a gated start isn't
    modelled. Only the start-independent yearly figures appear.
  - Remove every other release rule from the report: "until all three are live in Apr 2028", "once A has broken
    even", "if NPS falls below 0".
- **Data:** E9, E10; segment sums: 9.4 + 12.4 + 29.5 + 8.7 = 60.0.
- **Done when:**
  - The four segments add up to $60.0M.
  - A text search finds exactly one release rule.
  - The cumulative chart's title or label matches the line (Expected end-2030 −$0.2M, so "cash positive 2031").
- **Power BI:** the budget bar is a native stacked bar. Milestones are an aligned text strip; native X-axis markers
  only if verified under Publish to Web.
- **Closes:** INV-RK-1 (Blocker), INV-RK-3, J-IN-4, J-AQ-6, INV-CA-4 (with R-W-2), UX-07, J-VE-6, CL-14, CL-15.

### R-P2-8 · The invitation to Build your own (T2)

- **What:** one invitation line with a button in the Recommended state, at the foot of the decision card.
- **Copy:** "Think you can beat A? Build your own →". The button switches to the Build state.
- **Closes:** UX-05a, J-CI-2.

### R-P2-9 · Alt text and tab order, Recommended (T2)

- Dynamic alt text on the hero, the ledger, the capital bar and the cumulative chart, following the scenario.
- **Tab order:** masthead → tabs → scenario → hero → tile → ledger → invitation → capital plan → footer.
- Retired overlay visuals are removed, not hidden.
- **Closes:** J-AC-4, J-AC-5.

### R-P2-10 · Retire the duplicate rule texts and the old C-card trigger (T1)

- This is a part of R-P2-7, listed separately so the planner sees it as its own task: purge every measure and text
  box that carries an old release rule or the "Revisit … NPS falls below 0" sentence.
- **Closes:** INV-RK-1.

### R-P2-11 · Small chart polish, Recommended (T3)

- The hero and cumulative chart use the R-G1 notation in labels. The smallest text is ≥ 12 px.
- **Closes:** J-AC-6.

---

## 6 · P2 state "What waits, and why" (was "Considered: B and C")

### R-W-1 · Layout and the proof chart (T2)

- **Layout:** the current alts skeleton: the small scatter top left (`card_scatter_s`), the wide panel top right
  (`card_panel_w`), the comparison card at the bottom. The tabs have left the panel (R-P2-2), and the panel uses the
  freed space.
- **The proof chart** (the 456-package scatter, small):
  - Title: "We checked all 456 packages the rules allow: none beats A through 2032".
  - Subtitle: "Only 6 pay back by 2032, all under $15M. Each dot is a package."
  - Markers: the same lettered discs as before for A (blue), B and C (Night). The key matches the marks. The
    package tooltip stays.
- **Data:** A is the NPV maximum in all three scenarios (`packages.txt`, presets). This must hold in the model.
- **Closes:** J-CI-2, UX-13, CL-16.

### R-W-2 · Three cards, one grammar (T1 copy, T2 layout)

- **Amendment (doc 21 N-3, approved 13 Nov):** the three options are three rows of **one comparison table**
  (Option, The numbers, Why it's on the table, Why not now, When we decide), not three cards side by side:
  the copy below does not fit a 344 px card at 12 pt. Copy, data and the release-rule check are unchanged;
  "cards" below reads as "rows". The header chip becomes the first words of the Option cell.
- **What:** three cards side by side in the panel, in the same structure: **title · four numbers · "Why it's on the
  table" · "Why not now" · "When we decide"**.
  - One fixed gap between text blocks (no fixed slots with holes).
  - A meaningful header chip: the package letter or the tranche number. No placeholder key icon.
- **Copy:**
  - **B · Breakfast instead of kiosks**
    - Numbers: $11.7M capex · +$2.7M NPV through 2032 · +$4.0M a year by 2032 · −$6.9M to +$12.6M.
    - Why it's on the table: "Lifts guest scores in all 50 hotels instead of 20."
    - Why not now: "$2.3M more than A for $0.6M less through 2032, and it leaves the queues at the 20 busiest
      desks."
    - When we decide: "Not planned."
  - **Tranche 2 · Airport extensions, +80 rooms**
    - Numbers: $12.4M capex · +$1.7M a year once live · 13.8% a year on cost · no NPV shown (R-P2-7 rule).
    - Why it's on the table: "Toronto and Gatwick topped 90% in 17 and 14 of the last 24 months."
    - Why not now: "Neither pays back by 2032 (−$3.7M and −$3.5M)."
    - When we decide: the gate copy, short form: "At the 2028 gate, if the app delivers and the airports stay
      full." Last line: "Kingston (61% full) is not on the list."
  - **Tranche 3 · The refresh of the 10 oldest hotels (in package C)**
    - Numbers: $29.5M capex · +$2.3M a year once live · 7.9% a year on cost · package C (App + RMS + refresh)
      −$23.4M through 2032.
    - Why it's on the table: "Renovation works here: the seven hotels renovated in 2021 held their NPS near +6 while
      the rest of the brand fell to +2.7."
    - Why not now: "It earns 7.9% a year on cost, just under our 8% cost of money. The data does not price the cost
      of waiting, so this case is understated."
    - When we decide: "Back at the 2028 gate, with a case that looks beyond 2032."
- **Panel title:** "What waits, and why". Intro: "One alternative and two tranches, each weighed against A."
- **Data:** E5, E8, E9; package values from `packages.csv` (B = 01+09+10, C = 01+07+10).
- **Done when:** the three cards have identical structure and the same vertical rhythm, and no card carries a
  release rule other than the gate copy.
- **Closes:** UX-12, CL-27, INV-GR-1, INV-CA-3, INV-CA-4, J-IN-2, INV-RK-1 (with R-P2-7).

### R-W-3 · The comparison chart (T2)

- **What:** cumulative net impact of A, B and C, 2027–2032, following the scenario.
  - A blue; B Night; C grey dashed (no orange).
  - Direct labels at the line ends; no legend.
  - A tick below zero. The zero line labelled per R-G2.
- **Copy:** title *(Expected)*: "Cumulative net impact, $M: B ends within $1M of A by 2032; C is not cash positive
  by 2032".
- **Closes:** CL-12, UX-07.

### R-W-4 · Polish (T3)

- The scatter markers in the small scatter are identical to the hero's former lettered discs.
- **Closes:** UX-13.

---

## 7 · P2 state "Build your own"

### R-B-1 · Show both lenses for the plan (T2)

- **Amendment (doc 21 N-1, approved 13 Nov):** the selector is **native** (a multi-select button slicer
  beside a ten-row table), not Deneb. Columns, the "Answers" header, square check marks and the instruction
  stay as written here. Deneb remains only as the fallback if doc 21's spike S-3 fails.
- **Selector** (`dn_build_selector`):
  - Add a column "A year by 2032".
  - Header "Answers" stays. Kiosks now read **"F4"** (was F3). Every other mapping stays.
  - The rows use **square check marks** (multi-select), not radio circles.
  - The instruction reads "Click a move to add or remove it."
- **"Your plan" tile:** numbers are capex · NPV through 2032 · **a year by 2032** · **a year on cost**, then the
  range line (R-G1 notation) and the rules line.
- **Closes:** UX-05c/d, CL-31, INV §5 (the builder teaches both lenses).

### R-B-2 · Start from A, or a clean empty state (T2)

- **Amendment (doc 21 N-1):** with the native selector the preferred route is a saved slicer selection of
  A's three moves. The clean empty state stays mandatory (a viewer can deselect everything). There is no
  waterfall any more (doc 21 K-4).
- **Preferred:** the state opens with A's three moves picked **[verify: Deneb initial selection that also filters
  the model under Publish to Web]**.
- **Fallback (mandatory if not verified):** with no move picked, the tile and the comparison show no numbers, no
  waterfall and no "Totaal". Instead: "Pick at least three moves, one of them growth, within $60.0M. Your plan
  appears here and is compared with A below." "Nothing picked yet" appears at most once.
- **Closes:** UX-05b, CL-29.

### R-B-3 · "Your plan" in Night, never orange (T1)

- **What:** the plan dot in the small scatter is a Night hollow ring with a "You" label, offset so B stays readable.
  The plan line in the comparison chart is Night solid. A stays blue.
- **Exception:** over budget stays in Tangerine (it is a warning).
- **Closes:** UX-02 (core), UX-13, CL-12.

### R-B-4 · The build waterfall (T3)

- **What:** it follows R-G1 (no "Totaal", en-US labels). If the native total can't be relabelled locale-proof,
  replace the waterfall with a sorted bar of the picked moves' NPV, with the total in the tile.
- **Closes:** J-VE-1 (Build part).

---

## 8 · Tooltip pages

### R-TT-1 · tt-package: a sentence instead of the strip (T1)

- **What:** replace `tt_range_svg` with one line: "Low −$5.5M · Expected +$3.3M · High +$12.7M through 2032; it
  pays back by 2032 above zero."
  - The moves table is set at body size, with R-G1 notation (no $3.28M / $9.40M).
  - Trim the page height to the content.
- **Closes:** UX-14, CL-17, CL-33.

### R-TT-2 · tt-f3: no smaller than the card (T2)

- **Amendment (doc 21 N-4, approved 13 Nov): closed by removal.** R-P2-12 takes away the footer chips, the
  only things that opened tt-f1 to tt-f4. The four pages are deleted; the ledger carries the findings on P2.
- **What:** the band bars are at least as tall as on the P1 card, or the tooltip shows the three numbers only.
- **Closes:** UX-14.

### R-TT-3 · tt-glossary: the report's own words (T3)

- **What:** add these terms, in plain words:
  - move, package, growth (the dataset's `GrowthInitiative` flag; the rules require at least one);
  - a year by 2032 (run-rate), a year on cost;
  - tranche, the 2028 gate;
  - pays back by 2032 vs cash positive;
  - "topped 90%".
- **Remove:** "Case in view".
- **Closes:** CL-22, CL-21 (part).

### R-TT-4 · Tooltip colour (T3)

- **What:** the orange band stays as the tooltip skin. Inside the tooltips, the colour roles of R-G3 apply.
- **Closes:** UX-02 (tooltips).

---

## 9 · Cross-cutting acceptance

### R-X-1 · Accessibility pass (T1)

- **What:** a keyboard-only pass through both pages and all three states (Tab, Shift+Tab, Enter, Esc) and a Narrator
  pass over the dynamic alt texts. Record both in the bouwlog.
  - (Only if Deneb ships as the S-3 fallback, doc 21 N-1.) The Deneb selector's keyboard behaviour is documented. If it isn't operable by keyboard, the submission notes
    say so, and the Recommended and What-waits states carry the full argument without it.
  - `a11y_check.py` reports 0 errors. Contrast ≥ 4.5:1 for all text, including the masthead controls.
- **Closes:** J-AC-2, J-AC-3, J-AC-4, J-AC-5.

### R-X-2 · Contest compliance after the swaps (T1)

- Exactly two visible pages; tooltip pages hidden.
- At least four built-in visual types remain (line or area, column, bar, scatter, table).
- Three moves in A, of which two are growth, and the growth label is visible (hero row labels).
- Within budget.
- Financial **and** operational impact through 2032 on the canvas (the ledger).
- Provided data only (all E-facts derive from the workbook).
- Fonts are built in; images are embedded.

### R-X-3 · Render set and the Publish to Web gate (T1)

- **What:** a new numbered render set `screenshots/FinalV3/` covering:
  - P1;
  - P2 in Recommended × Low/Expected/High;
  - What waits;
  - Build (empty or A-preset, filled, over budget);
  - every tooltip page.
- **Then the Publish to Web gate:** Deneb rendering, tooltips, nl/de browser locale (R-G1), the page buttons,
  visual headers against the hover tags, tooltip scale at 1366 px, and one touch test. Bjorn publishes.

---

## 10 · What must not change

- P1 headline, the action-title pattern, the KPI peer-rank sublines, the folio table's numbers, the card anatomy,
  the masthead, the warm canvas, the tooltip skin, and "An association, not proof of cause."
- The exhaustive package search and its 456-dot chart: they move to What waits; they are not deleted.
- The Low case is shown unprompted (now as a bounded loss in the tile).
- Dynamic alt text by measure as the pattern for every new visual.

## 11 · Decisions recorded (13 Nov, Bjorn: "fully on board")

| # | Decision | Outcome |
|---|---|---|
| D1 | P2 hero | Ten moves on two lenses (R-P2-3); the 456 scatter moves to What waits; fallback R-P2-3-FB at the cut line |
| D2 | Growth | A only now; Gatwick and Toronto +40 as tranche 2 at the 2028 gate; Kingston explicitly not |
| D3 | Release rule | One gate in mid-2028 with two tests (R-P2-7 gate copy) |
| D4 | Finding-to-move mapping | F2 = app; F4 = kiosks (E1, E2) and the tranche-2 extensions; F1 = RMS and the outcome measure; F3 = the refresh, deferred |
| D5 | Hover tags | Night text on a light pill; only the ⓘ glyph may stay Tangerine (overrides doc 18's pill colour) |
| D6 | P2 headline | "Fix the middleman first: $9.4M now earns $3.5M a year by 2032." |

**Corrections to doc 19 found while writing this:**

- E4 refutes the "full but not pricing like it" angle (doc 19 DS-07 data check, INV-GR-2), so RMS stays under F1.
- E6 shows that since 2023 most of the margin fall is running costs, so F1's copy names both causes (R-P1-3).
- E1/E2 confirm the kiosk → F4 link with complaint data.

## Amendments (13 Nov, from doc 21 section 2.2, approved by Bjorn)

| # | Requirement | Was | Now |
|---|---|---|---|
| N-1 | R-B-1, R-B-2, R-X-1, R-X-3 | Deneb selector | Native button slicer beside a table; Deneb only if spike S-3 fails |
| N-2 | C0, R-P1-2, R-P1-3 | 2.7 points if E6 holds | 2.8 points: the difference of the two shown values, parts 1.0 + 1.8, all real rounded values |
| N-3 | R-W-2 | Three cards side by side | One comparison table with three rows, same copy |
| N-4 | R-TT-2, R-P2-12 | Improve tt-f3 | tt-f1 to tt-f4 deleted; R-TT-2 closed by removal |
| N-5 | R-P2-7 | Two stacked full-width elements | Budget bar on top; gate copy left and cumulative chart right below it |

## Open questions

- **C0:** resolved, 2.8 (see section 0 and the amendments above).
- **R-B-2:** replaced by doc 21 spike S-3 (native selector with a saved selection).
- **R-P2-7:** milestones are one text line plus one constant line at the 2028 gate (doc 21 K-6); the Publish to Web
  check of that line stays open.
- **R-P1-7:** native scatter vs Deneb for the 50-hotel strip (preference: native; doc 21 spike S-4).
