# Review: Goodnight Inn report (P1 The Brand Review, P2 The Investment Strategy)

> **Checked against the model afterwards** (7 Nov, Power BI Modeling MCP on the open Desktop model and
> `project/analysis/output/packages.csv`). The review below is the independent reviewer's text, unchanged; this box
> records what the data says about the findings that depend on numbers.
> - **B1 confirmed.** No package has an NPV of at least 0 in Low (offline as well), so rule B is empty there.
>   `Plan Risk (text)` then returns "NPV in the Low case +M; ... positive in 2027".
> - **M6 confirmed.** B and C are rules, so the package changes with the scenario. B is 01+09+10 in Expected and
>   01+02+09+10 in High. C is 01+02+07 in Low, 01+07+10 in Expected and 01+02+07+10 in High.
> - **M3 confirmed.** The kiosks have an NPV of -$0.6M in Expected.
> - **M8, correction.** The $60M package costs exactly $60.0M
>   (5.0 + 2.0 + 15.0 + 6.6 + 24.75 + 4.25 + 2.4). The table rounds 24.75 to 24.8 and 4.25 to 4.3, so its rows add up
>   to 60.1. The other gaps (+2.7, 3.5, cents, -2.7 pt) are also display rounding; every underlying total reconciles.
>   The fix is to show capex to two decimals, not to derive totals from rounded parts (that would display $60.1M,
>   over the cap).
> - **M11, correction.** The package does comply. In the dataset, Booking app and Revenue management are
>   `GrowthInitiative = Yes`, so A has 2 growth initiatives. The finding stands as a visibility issue only.
> - **m8, explained.** Goodnight Inn has 50 hotels: 44 have a renovation date and 6 were never renovated. F3 shows
>   the 44, so it needs a caption; the numbers are not in conflict.
> - **p1, intentional.** The lockup sleeps on P1 and is awake on P2 (brand-kit decision).
> - The `detail/` crops and the `comp/` copies the reviewer used are not in the repo. The comp is in
>   `project/design-prototypes/reference_screenshots/`. What the reviewer was told is in `REVIEW-BRIEF.md`.

Independent review based only on the images in this folder (16 states, 13 live clicks, 2x crops, 3 comp images).
Coordinates are page pixels on the 1920 x 1080 renders, as (x, y). "detail" = the 2x crops.
Ignored as environment artefacts: the "CTRL+klik hier om volgen" tooltip, edit-mode selection frames and
visual-header icons, the mouse position. The nl-NL decimal comma is treated as one item (M7).
Where the image cannot settle a question, the finding says so.

Severity: **blocker** = must fix before submission; **major** = a judge or board member will notice, and it costs
credibility or meaning; **minor** = visible craft defect; **polish** = refinement.

Tally: 1 blocker, 11 major, 11 minor, 10 polish.

---

## Blocker

### B1. "Open the plan" for B in the Low case renders a broken page with a false claim
- **Files / where:** `15_P2_plan_B_Low.png` + `detail/15_..._panel@2x.png`, whole right panel (1090-1886, 185-1014).
  Reached from `14_P2_landing_focusB_Low.png`.
- **What is wrong:**
  - Header says "No package in focus" while the dropdown still says "B · Most hotels with a guest-score effect…".
  - Waterfall is empty: y-axis ticks "+$0,0M / +$0,0M / $0,0M" and a lone "$0,0M Totaal".
  - All 10 initiatives "Not funded". The cumulative chart is blank; only its title is left.
  - The ops tiles mix two different nulls: "--" rooms added, "0" rooms refreshed, "--" hotels.
  - Risks line: **"NPV in the Low case +M; the cumulative net turns positive in 2027 (Low)."** It's a broken string, and
    the claim is false: nothing is funded, so nothing turns positive.
  - The landing (14) gives no warning: B has no dot on the scatter, and the raspberry "Open the plan…" button is
    still offered.
- **Why it matters:** two clicks from the opening state (pick B, click Low, in either order) reach it. Any judge who
  tests the scenario switch will find it. A sentence that invents a payback year casts doubt on every other number.
- **Fix:** best option: freeze B and C as fixed initiative sets (see M6), so a package in focus always exists and the
  empty state disappears. Either way, guard every plan measure. The Risks measure returns no NPV fragment when NPV is blank
  (never "+M") and no payback-year fragment when nothing is funded. The header reads "B has no package in the Low case"
  instead of "No package in focus". The landing shows one line under the dropdown when the focus is empty. Do not
  render an empty waterfall with three identical zero ticks: place a message card over it, driven by a measure.

---

## Major

### M1. The Back button's label disappears on hover
- **Files / where:** `L3c_live_C_after-Open-the-plan.png`, `L4b_live_after-Open-the-plan-with-point-selected.png`;
  the button at (1112-1864, 968-1006).
- **What is wrong:** on hover/press the fill turns dark maroon (rgb 109,14,57) and the label stays plum-black
  (rgb 36,21,53). The measured contrast is **1.4:1**, so "← Back to the recommendation" is barely visible. "Open the plan"
  keeps white text on hover, at 11.9:1 (`L3d`), so only the Back button's hover text colour is wrong.
- **Why it matters:** it is the only way out of the plan state, and every viewer hovers it. It looks broken.
- **Fix:** Back button > Style > Hover and Press: white text, or keep a light hover fill (e.g. #F3E6EC) with
  plum-black text. Check all four button states on both buttons.

### M2. Scatter: the highlighted packages get lost or drawn under the cloud, and the $60M focus point is clipped
- **Files / where:** `02`-`07`, `14`, `16` and their `detail/*__scatter@2x.png`; `L3b`, `L4a`; compare
  `comp/opzet-p2-investment-strategy.png`. Left card (33-1071, 185-1014).
- **What is wrong:**
  - The grey dots are about 14 px across and mid-grey (rgb 149,141,155). The comp's dots are about 8 px and light
    (rgb 199,195,202). That is roughly 3x the area and much darker, so the cloud reads as a solid mass.
  - The plum-black B and C dots differ from the grey by only about 3.3:1. C (about $37M, −$23M) sits in the densest part
    of the cloud, and grey dots are painted **over** it. A zoom of `06` and `16` shows grey discs covering the
    enlarged focus dot. In Low (`03`, `14`) C is hard to find.
  - The $60M package in focus (`07`, at about 1028, 713) is cut in half by the plot edge and also covered by grey dots.
    Every dot at capex $60M is half-clipped along the right edge, in every state.
  - Nothing on the chart is labelled. The reader has to map "Raspberry: our recommendation A. Plum-black: B and C." from
    the subtitle. In Low the subtitle still promises B, but no B dot is drawn (`03`, `14`, `15`, `16`).
- **Why it matters:** the scatter is the page's proof that only small packages pay back. If the reader can't find B
  and C, the "considered, not recommended" text has no visual anchor. The comp got this right, so this is a regression.
- **Fix:** follow the comp: make the cloud smaller, lighter (#C9C3CC) and 40-50% transparent. Put the highlights on
  top: overlay a second scatter with a transparent background and the same fixed axes that plots only A, B, C and the
  package in focus, with data labels "A", "B", "C". Draw order inside one series is not reliably controllable. Set the
  x-axis end to about $62M (or the start to −$1M) so edge dots are not clipped. Build the subtitle from a measure that
  drops "B" when B has no package.

### M3. The P2 headline is contradicted by its own panel: "the three moves that pay"
- **Files / where:** every P2 state, title at (32-1130, 95-130). The kiosks row in the `08`/`09`/`10` table and
  waterfall. The landing "Not funded" sentence (1112, 768-790).
- **What is wrong:** "Kiosks at 20 desks" has an NPV of **−$0.6M (Expected), −$1.2M (Low), +$0.0M (High)**. It never
  pays back by 2032. Yet the title says "Fund the three moves that pay". The landing rules out five initiatives because
  "each has a negative NPV through 2032", which is the same test the kiosks fail. In Low (`03`, `09`, `14`-`16`) the
  title sits directly above "Low case", above "None of the 456 possible packages pays back by 2032", and next to A at
  −$5.5M.
- **Why it matters:** anyone who reads the waterfall (the orange −$0.6M bar right under the title) sees that the
  headline is false. A critic gets an easy line. The real argument is stronger and goes unstated: the package pays,
  and the kiosks are the cheapest answer to F3.
- **Fix:** use a title that is true in all three scenarios, e.g. "Fund one package of three moves: $9.4M now, $50.6M
  held back." Add one landing sentence: "Kiosks alone don't pay back by 2032 (−$0.6M); they are the cheapest move on F3,
  and the package still returns +$3.3M." Change the not-funded reason to what the selection actually tests, e.g. "each
  would lower the package NPV". When the scenario isn't Expected, add "recommendation set on the Expected case" to the
  subtitle.

### M4. The P1 headline overclaims against its own evidence
- **Files / where:** `01`, title (32-1560, 90-130); F3 note (1304, 736-760); KPI band.
- **What is wrong:** "…and is losing its guests." But occupancy is "best of 4" (79.4%). F3's own note says "age costs
  loyalty, **not yet rooms**. An association, not proof of cause." The evidence is a low NPS (last of 4, and −4.9 in
  the 10 oldest hotels), not lost guests.
- **Why it matters:** the headline is read first, and judges check it against the cards. A headline that the page
  itself qualifies looks careless or spun.
- **Fix:** e.g. "…pays the middleman, and its oldest hotels are losing goodwill." or "…and its welcome is fading."
  The second matches F3's own label.

### M5. Internal codes in board-facing text, and "Funded" shown under packages that are not recommended
- **Files / where:** plan header at (1112, 288-304) in `08`-`13`, `16`. The dropdown in `07`/`13`
  ("Package 01+02+03+05+08+09+10 ($60.0M)"). The open list in `L3a`.
- **What is wrong:**
  - The plan headers read "01+02+10 in focus…", "01+07+10 in focus…", "01+02+03+05+08+09+10 in focus…". The codes
    appear nowhere else (the table, waterfall and landing all use names), so a reader cannot decode them.
  - The dropdown lists A, B, C, then "Package 01+02+10 ($9.4M)", which is A again, then "Package 01+09+10 ($11.7M)",
    which is B in Expected again. The rest of the 456 are listed by code only.
  - In the plan for B or C, nothing says "B", "C" or "not recommended". The status column says **"Funded"** for, e.g.,
    "Refresh 10 oldest" (`12`), which reads like a decision.
- **Why it matters:** the brief is "an investor deck, not a playground". The codes are database residue. "Funded"
  under a rejected package contradicts the recommendation for anyone who opens C.
- **Fix:** build the plan header from a measure: "Package A (our recommendation): $9.4M on 3 initiatives, all live by
  Apr 2028" or "Package C (considered, not recommended): …". For a free pick, name the initiatives. Label the status
  "In package / Not in package" unless the focus is A. Limit the dropdown to A, B, C (plus "Full $60M" if a named
  comparator is wanted) and let the scatter tooltip cover the rest. If the 456 stay, label them by initiative names and
  remove the duplicates of A and B.

### M6. B and C change composition by scenario, so one name carries different numbers
- **Files / where:** landing C line at (1112, 696) in `02`/`03`/`04`. Plan headers and Risks in `12` vs `16`. `11`
  Risks vs `14`/`15`.
- **What is wrong:**
  - C is "01+07+10, $36.9M, NPV −$23.4M" in Expected, "01+02+07, $36.5M, NPV −$34.5M" in Low, and "$38.9M, NPV −$11.3M"
    in High. The landing text "With the refresh of the 10 oldest hotels" is identical in all three.
  - Plan C in Expected (`12`) Risks: "NPV in the Low case **−$34.8M**". The Low landing (`03`) and plan C in Low (`16`):
    C at **−$34.5M**. That is two different Low NPVs for "C".
  - Plan B in Expected (`11`) Risks: "NPV in the Low case **−$6.9M**". The Low landing (`03`/`14`): "no package with a
    guest-score effect pays back", and plan B in Low (`15`) is empty (B1).
  - B is "breakfast instead of the kiosks, $11.7M" in Expected and "A plus the breakfast upgrade, $13.7M" in High.
- **Why it matters:** judges check consistency by toggling scenarios. It reads as a calculation bug, even though it
  comes from the rule definition.
- **Fix:** freeze B and C as fixed initiative sets (defined on Expected, as the comp implies) and evaluate those
  fixed sets under Low and High. Then −$6.9M and −$34.8M become the Low values everywhere, and B1 disappears. If the
  rules must stay dynamic, say so in the landing line and the dropdown, e.g. "C = best package with the refresh in this
  scenario: Booking app + Kiosks + Refresh".

### M7. Locale: two number formats on the same card, and one that changes meaning
- **Files / where:** `01` (KPI band, F2 table, F3/F4 labels); all of P2 (KPI row, waterfall, table, ops tiles).
- **What is wrong:** numbers formatted by the visual use a decimal comma and DAX text uses a point, often side by side:
  - "79,4%" above "the others 64.7% to 72.9%";
  - "$9,4M … +$3,3M" next to "−5.5 to +12.7";
  - "$2,0M … −$0,6M" in the same table row as "+0.25 on 20";
  - the waterfall total says "Totaal".
  The worst case is plan C (`12`, `16`): **"1.180 rooms refreshed"** directly above "Risks: 15% of 1,180 rooms". In
  English, "1.180" reads as one point one eight.
- **Why it matters:** Publish to Web formats visuals by the viewer's browser locale, so any judge outside en-US gets
  this mix. It looks unfinished, and in one place it changes the meaning.
- **Fix:** take every displayed number from one source. Set the file to English (US). Render cards and KPIs as DAX text
  with FORMAT(…, "en-US"), the way the subtexts already are, so no visual-formatted number sits next to a DAX one.
  Replace the waterfall's automatic total with an explicit "Package" category, as in the comp. Check the published
  link in both an nl-NL and an en-US browser.

### M8. Parts don't add up to totals, including a package that appears to break the $60M cap
- **Files / where:** `13` (capex column and header), `11` (waterfall), `02` vs `08`, `01` (F2 table; F1 vs KPI).
- **What is wrong:**
  - $60M package (`13`): 5.0 + 24.8 + 4.3 + 15.0 + 6.6 + 2.0 + 2.4 = **$60.1M**, but the header and dropdown say
    $60.0M.
  - Plan B (`11`): +3.4 − 1.1 + 0.5 = +2.8, but the total bar says +$2.7M.
  - A in Expected: the landing says "+$3.5M profit a year by 2032", but the run-rates add up to 2.4 + 0.4 + 0.8 =
    $3.6M. Low and High add up exactly (1.0 and 6.2).
  - P1 F2 table: $109.31 − $19.68 = $89.63 (shown $89.64), and $111.56 − $4.46 = $107.10 (shown $107.09).
  - P1: F1 "fell from 36.5% to 33.7%" is 2.8 pt, but the KPI says "−2.7 pt since 2023".
- **Why it matters:** judges add up tables. $60.1M reads as a breach of the "package at most $60M" rule, and the other
  gaps erode trust in every figure. (The comp already has the −2.7 and cent mismatches, so following the comp won't fix
  them.)
- **Fix:** derive displayed totals from the rounded components, or show capex to two decimals. Compute the KPI delta
  from the displayed values. Either give "Run-rate" and "profit a year by 2032" the same name and definition, or state
  the difference.

### M9. The cumulative net impact chart can't be read
- **Files / where:** `08`-`13`, `16`, at (1112-1490, 830-900); compare `comp/opzet-p2-investment-strategy--plan.png`,
  which has a year axis.
- **What is wrong:** there is no x-axis and no years. Three raspberry lines carry no labels, and the y-axis has only two
  ticks. The chart is about 375 x 60 px (about 265 x 45 px at 1366 wide). The Risks line states payback years ("2031
  (Expected)", "after 2032 (Low)", "2029 (High)") that the chart cannot show. The thick line is the same middle line in
  Low, Expected and High (`08`/`09`/`10`), so the emphasis doesn't follow the scenario switch. In `15` the chart is
  blank.
- **Why it matters:** a core visual that only the text can explain doesn't earn its place, and judges count core
  visuals.
- **Fix:** add years 2027-2032 and a $0 line. Label the line ends Low / Expected / High, or colour the selected
  scenario's line with a measure. Give the chart more height: take it from the gap above the button, or drop the
  zero-value ops tiles. Or replace the chart with one line: "Pays back: 2029 (High), 2031 (Expected), after 2032 (Low)".

### M10. Legibility at 1366 wide
- **Files / where:** all files. Measured on the renders: almost all secondary text (axis labels, table cells, card
  notes, KPI captions, Risks, "Scenario", footers) has a 9 px cap height at 1920. That is about a 13 px font, which
  becomes about **9 px at 1366** (71% scale).
- **What is wrong:** at that size the P2 plan state packs a 10-row, 9-column table, a waterfall, a line chart, three
  tiles and a paragraph into about 9 px text. P1's card notes and axes are the same size.
- **Why it matters:** judges often review at laptop widths. 9 px is below comfortable reading, and it makes the plan
  state feel like a spreadsheet.
- **Fix:** raise the minimum to about 16 px at 1920 (11-12 px at 1366) for table, axis and note text. To make room in
  the plan state, show the funded rows plus the one or two nearest misses (move the rest to a tooltip), and hide the
  ops tiles when they are zero.

### M11. Compliance with the contest rules isn't visible (ambiguous)
- **Files / where:** `02` landing; `08` table and ops tiles ("0 rooms added").
- **What is wrong:** the rules require at least one growth initiative. Nothing on P2 says which of A's three moves is
  the growth initiative. The table has no type column, and the plan shows "0 rooms added". From the images I cannot tell
  whether the dataset classes the booking app or revenue management as growth.
- **Why it matters:** judges check the rules. If they equate growth with rooms, A appears to fail a rule the report
  never addresses.
- **Fix:** add a "Type" column to the table (Growth / Margin / Guest) and one compliance line on the landing: "Within
  the rules: 3 initiatives, 1 growth (…), $9.4M of $60M, impact through 2032."

---

## Minor

### m1. Dropdown labels are truncated
- `05`, `06`, `11`, `12`, `14`-`16` (1500-1858, 225-250) and the open list in `L3a`: "B · Most hotels with a
  guest-score effect, NPV a…" and "C · Highest NPV with the refresh of the 10 olde…". The ellipsis runs into the
  chevron, and the cut part is the condition that defines the rule. **Fix:** shorter labels, e.g. "B · Most hotels
  with a score lift, NPV > 0" and "C · Best package with the refresh", or a wider slicer.

### m2. Changing the focus gives almost no feedback on the landing
- `02` vs `05`/`06`/`07`; `14`. Choosing B, C or the $60M package only enlarges a dot. In `07` that dot is clipped,
  and in `14` there is no dot at all. The heading and KPIs stay A's (by design), and the button label is generic.
  **Fix:** build the button text from a measure ("Open the plan for package B →") and add a one-line focus summary
  under the dropdown ("In focus: B · $11.7M · NPV +$2.7M").

### m3. F2 uses a legend with three identical grey dots instead of the comp's direct labels
- `01` F2 (1130-1235, 405-490); compare the comp P1. P&K Select, Maison d'Or and Pebble & Pine get the same grey dot.
  The legend order doesn't match the line ends. "Goodnight Inn" happens to sit beside its line end, so the other three
  read as misplaced direct labels. **Fix:** turn off the legend and label the line ends (series labels or text boxes)
  as in the comp: raspberry "Goodnight Inn", grey "Pebble & Pine", "P&K Select / Maison d'Or". Or use a single grey
  label, "the other three brands".

### m4. F3 has no zero line and awkward category wraps
- `01` F3 (1304-1880, 400-710); detail F3; comp. The bars float with no baseline. The labels wrap as "5 years or
  less · 14 / hotels" and "10 years or more · / 10 hotels", leaving a dangling separator. **Fix:** add a constant line
  at 0 in the axis colour. Use one-line labels such as "≤5 years (14 hotels)", "6-9 years (20)", "10+ years (10)", or
  two stacked fields as in the comp.

### m5. Tables: sort arrows, header alignment, row order, emphasis, scrollbar
- `01` F2 table (▲ at 690, 624) and the plan table in `08`-`16` (▲ at 1161, 503).
  - A sort arrow hangs under "One room night, 2025" and under "Status".
  - Headers are left-aligned over right-aligned numbers ("Via an online agency", "Capex", "Run-rate", "NPV").
  - P1's "Goodnight Inn keeps" row isn't bold; the comp bolds it.
  - The not-funded rows are alphabetical (the comp sorts by NPV), so the nearest misses aren't on top.
  - "Funded" isn't emphasised (the comp uses raspberry bold).
  - A scrollbar shows at about x 1858: the table overflows its box by a few px.

  **Fix:** right-align numeric headers; bold the total row; sort by status, then NPV descending; colour "Funded";
  enlarge the table box or reduce row padding. For the arrow, sort by a rank column with a blank header at minimum
  width.

### m6. Waterfall details
- The title "Where the NPV comes from, $M through 2032" doesn't name the scenario; the comp adds "(Expected)".
- In `13`, a category label is cut to "Revenue managem…".
- In `08`, "+$3,4M" sits inside its bar in white while every other label sits outside.
- In `10`, "+$0,0M" labels an invisible bar.

**Fix:** put the scenario in the title via a measure; use short category names ("Revenue mgmt"); keep all labels
outside the bars; show "$0.0M" without a sign.

### m7. A scatter selection persists and removes the colour encoding
- `L4a`-`L4c`. Clicking A dims every other dot, including B and C (B turns plain grey). The dimmed state survives the
  Open/Back round trip. The images don't show whether clicking any other dot cross-filters the panel. **Fix:** have
  the Open/Back bookmarks clear the scatter selection (Data, Selected visuals: scatter only). Then test that a click on
  any dot leaves the panel's numbers unchanged.

### m8. Hotel counts may disagree across the pages (verify)
- `01` F3 covers 14 + 20 + 10 = 44 hotels across all renovation bands. P2 says "a guest-score effect in 50 hotels"
  (landing B line) and "50 hotels, score up" (`11`, `13`). If the brand has 44 hotels, a 50-hotel breakfast upgrade is
  impossible. It may be legitimate (F3 might exclude hotels without data), but nothing says so. **Fix:** correct the
  number, or caption F3 "44 of 50 hotels with a renovation date".

### m9. Names drift between the panel and the table
- The landing says "Toronto extension / Gatwick extension / Kingston extension"; the table says "Toronto +40 rooms" etc.
- The landing says "profit a year by 2032"; the table says "Run-rate".

**Fix:** use one name per thing on every surface.

### m10. The scenario control is the default tile slicer instead of the comp's pills
- All P2 states (1120-1460, 200-268). The unselected "Low" and "High" have no border or fill, so they read as labels,
  not buttons. The selected tile is Power BI default grey (rgb 51,51,51), not the brand plum-black. The tiles are 50 px
  tall next to a 26 px dropdown. There are three left edges: label at 1120, tiles at 1133, body text at 1112. The
  "Scenario: Expected" header repeats the selection. **Fix:** give unselected tiles a thin rounded outline, use
  plum-black for the selected one, match the dropdown height, align everything to x 1112, and use a plain "Scenario"
  header.

### m11. Two questions the P2 landing leaves open
- "Kiosks at 20 desks F3": F3 is about the 10 hotels renovated 10 or more years ago. Which 20 hotels get kiosks, and do
  they include those 10?
- "$50.6M held back": held back for what, and decided when?

A board will ask both. **Fix:** answer each in one clause on the landing, using only what the model supports.

---

## Polish

- **p1. The logo changes between pages.** P1 has closed eyes (◡◡); P2 has open dots (••), at (33-56, 33-70) in `01` vs
  `02`. The comp uses closed eyes on both. If intentional, no one will read it as meaning anything; if not, it's a
  mismatch.
- **p2. The header jumps on a page flip.** The P2 subtitle sits 7 px lower (rows 146-159 vs 139-153) and the title 2-3
  px lower. Align both pages to the same grid.
- **p3. Landing panel rhythm.** The gaps are uneven, with about 135 px of dead space between "Not funded…" and "Read
  with care" (y 790-925). "−5.5 to +12.7" ends about 25 px from "+$3,5M" while the other KPI gaps are about 115 px. The
  range is the only KPI without "$…M" in the value.
- **p4. F1 axes.** There is an unlabelled band between the 30% gridline and the year labels (y 640-690). The 2023 and
  2025 points that the title quotes (36.5%, 33.7%) aren't labelled. Set the axis to 30-50 or show 25%, and label the
  two points.
- **p5. F4.** There is no baseline under the bars, and no caption saying the bars are "the 7 fullest hotels, 2025".
  The three segment labels sit tight under their numbers.
- **p6. Scatter corner.** "−$60M" and "$0M" crowd the bottom-left corner (about 80-140, 950-970).
- **p7. P2 footer.** "FinanceParameters" is a table name, and "Package values are scenario logic" is unclear. Suggest:
  "…and its finance parameters (ramp-up, 8% discount rate, horizon 2032). Low, Expected and High are the dataset's
  scenarios."
- **p8. P1 KPI arrows.** "▼ highest of 4" uses ▼ to mean "bad", but beside "highest" it reads as "down". Use colour or
  a neutral marker.
- **p9. Zero ops tiles.** "0 rooms added / 0 rooms refreshed" take prime space for A and B. Hide a tile when it is zero.
- **p10. Visual headers.** In `07`, `L3b` and `L4` the edit-mode headers of the scatter and a text box overlap the
  scatter subtitle and the "Our recommendation" line. That is edit chrome, but it shows the boxes overlap. Turn header
  icons off for every visual before publishing, so hover icons can't cover text in Publish to Web.

---

## Story (10-second test)

- **P1 passes.** The headline and KPI band carry the point, and each of F1-F4 has an action title that the chart
  supports. Weak spots are the overclaiming headline (M4) and F2's undecodable grey legend (m3).
- **The P2 landing passes.** The title, A's four numbers and "6 of 456 … pay back" make a clear recommendation in 10
  seconds. That clarity breaks once the reader leaves the default state, through B1, M3, M5 and M6.
- **Elements that don't earn their place as built:**
  - the 456-entry coded dropdown (M5);
  - the cumulative chart without an axis (M9);
  - the zero ops tiles (p9);
  - the redundant "Scenario: Expected" header (m10).

## Deviations from the approved comp that make it worse

The scatter mark styling (M2); the cumulative chart's lost year axis (M9); F2's direct labels replaced by a legend (m3);
F3's lost baseline and clean two-line labels (m4); the table's lost bold total, NPV sort and "Funded" emphasis (m5); the
waterfall's "Package" total and "(Expected)" title (M7, m6); the pills replaced by default tiles (m10); the P2 logo
(p1).

Some problems are already in the comp, so following the comp won't fix them: the codes in the plan header (M5), "the
three moves that pay" (M3), "−2.7 pt" and the cent mismatches (M8), and "▼ highest" (p8).

---

## Overall verdict

**Not ready to submit.**

P1 is close to final. Its structure is clean, it has four honest findings and a strong KPI band. It needs a truthful
headline, the locale and rounding fixes, and the comp's F2/F3 details.

The P2 landing communicates the recommendation well. The interactive layer that a judge will click through is not
ready:
- a reachable broken state that states a false payback year;
- a Back button that loses its label on hover;
- a scatter that hides the packages the text discusses;
- rule-based B and C whose numbers shift between scenarios;
- database codes in board-facing text.

None of this needs a redesign. All of it is visible to a judge within a minute of clicking.

## Top 5 fixes, in order

1. **Freeze A, B and C as fixed initiative sets, and guard every plan measure against an empty package** (B1, M6).
   One change removes the broken state, the false "2027", and the drifting B/C numbers.
2. **Fix the Back button's hover and press text colour** (M1). A five-minute fix that every visitor would otherwise hit.
3. **Rebuild the scatter's marks to the comp** (M2): a lighter, smaller cloud; A, B, C and the focus package on a
   labelled overlay; x-axis headroom past $60M; a subtitle that matches what is drawn.
4. **Make the words true** (M3, M4, M5): a P2 title and not-funded reason that survive the kiosks' −$0.6M, a P1 headline
   that matches F3, names instead of codes, and "In package" instead of "Funded" for packages that are not recommended.
5. **Use one number system** (M7, M8): en-US throughout, totals that equal their displayed parts (above all the $60.0M
   package), and "Package" instead of "Totaal".

Next in line: the cumulative chart's axis and labels (M9), the minimum text size for 1366 (M10), and the rules line
(M11).
