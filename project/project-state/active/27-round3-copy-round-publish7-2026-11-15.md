# 27 · Review round 3: the last copy round, and publish 7 (15 Nov 2026)

**For:** Bjorn, and whoever checks the entry before the submission of 17 Nov.
**Sources:** the five V3 reviews of publish 6 (`26-jury-review-v3`, `26-investor-review-v3`, `26-review-ui-ux-v3`,
`26-review-clarity-newcomer-v3`, `26-review-dataviz-storytelling-v3`, all dated 15 Nov), the captures they read
(`deliverables/screenshots/Committee-walkthrough-2026-11-15/`) and the organisers' workbook.
**Approval:** Bjorn, 15 Nov, on the summary of those five reviews: "let's do one final update for the small bits ...
there's consensus on most, so let's go in and do one more publish."
**Rules:** doc 23 section 1, as in every round (generators only, checks green, Desktop in a throwaway copy, Bjorn
publishes, every Desktop window closed without saving).

---

## 0 · Progress

| Step | Status | Date | Note |
|---|---|---|---|
| The copy round | done | 15 Nov | Seven lines, all in slots that exist. Engine: 142 of 142 texts, 809 of 809 numbers, alt texts 0 flags. Rendered in Low, Expected and High |
| The publish copy | see the log | 15 Nov | |
| Publish 7 | Bjorn | | Replace the report "Goodnight Inn"; the link stays |
| The gate and the walkthrough on publish 7 | after the publish | | `gate.py` against publish 6, `walk.py` |
| The package for the last check | after the gate | | `deliverables/final-check-publish7/` |

---

## 1 · Where the five reviewers stood on publish 6

| Reviewer | Score | On one more publish |
|---|---|---|
| Jury | 42.0 of 50 (was 41.5) | "Submit this version, or one copy-only publish"; expects 42.5 to 43.0 |
| Dataviz and storytelling | 8.9 on the jury lens | One item is worth a publish: say the second lens out loud for B |
| Investor | 8.2 (was 8.3) | Not on its own; two items ride along |
| UI/UX | 35 of 40 (was 34) | Not on its own; the copy lines ride along |
| Clarity | 0 S1, 4 S2 | "Leave it"; two items ride along |

None asked for a new version. All five named a small set of sentences, and most of those are the same sentences.

---

## 2 · The seven lines

Old is publish 6 (`Committee-walkthrough-2026-11-15/texts/`). Where a line follows the scenario, the Expected wording
is shown.

| # | Slot | Old | New | Raised by | Fit, as rendered |
|---|---|---|---|---|---|
| 1 | Recommendation tile, line 2 | The app carries it: +$3.4M of the +$3.3M. Every year without it leaves about $2.4M with the agencies. | The app alone: +$3.4M through 2032. Every year ... (Low: "The app alone: +$0.6M a year by 2032.") | J3-03, UX3-11, CL3-16, DS3-01 | one line in all three cases; 24 px shorter than before |
| 2 | What waits, row B, "Why not now" | $2.3M more than A for $0.6M less through 2032, and the queues at the 20 busiest hotels stay. | $2.3M more than A for $0.5M more a year: 34.0% a year on cost against A's 37.5%, and $0.6M less through 2032. The queues at the 20 busiest hotels stay. | J3-02, INV3-02, CL3-14, DS3-03 | five lines (was three): row B is one line higher, the table still ends about 60 px above its card's edge in the High case |
| 3 | Hero table, Status | Breakfast upgrade: not now · Kingston +40 rooms: not now | package B · not full (Energy and Boston keep "not now": the caption says why) | J3-08, INV3-01, DS3-02, clarity part 2 | as wide as "2028 gate" |
| 4 | Capital plan, tranche 3, line 2 | $29.5M · 2028 gate | $29.5M · 2028 gate, only with a case beyond 2032 | J3-01, INV3-03, CL3-15 | 347 px in a segment of 881 |
| 5 | What waits, row B, last number line; Build, under "Your plan" | −$6.9M to +$12.6M · −$5.5M to +$12.7M | Low −$6.9M · High +$12.6M · Low −$5.5M · High +$12.7M | UX3-08, CL3-13, DS3-08 | one line each |
| 6 | Hero table, the two value columns' headers | test 1 · test 2 | ≥ 8% · ≥ $0 | UX3-04, CL3-09, DS3-07 | 37 and 33 px; the columns give their headers 54 and 64 |
| 7 | What waits, tranche 3, "Why it's on the table" | ... the seven hotels last renovated in 2021 held NPS near +6 ... | ... the seven hotels whose renovation finished in 2021 held NPS near +6 ... | J3-05, CL3-17, DS3-14 | five lines (was four); the row was five lines high already |

The alt text of the your-plan numbers follows line 5: "NPV by case: Low −$5.5M · High +$12.7M."

**What line 2 prints per case** (the engine): Low "$0.3M more a year: 10.8% a year on cost against A's 11.1%, and
$1.4M less through 2032"; High "$0.5M more a year: 57.6% ... against A's 66.0%, and $0.1M less through 2032". A is
ahead on "a year on cost" in all three cases.

**What line 3 reads from.** A move marked "not now" shows "package B" when package B holds it and package A does not,
and "not full" when it is an extension whose hotel topped 90% in none of the last 24 months. Both come from the model
(`Move Status (text)`); `MoveDecision[Status]` stays the key for the colours and the caption.

**Line 7 is proven in the workbook.** `Hotels[LastRenovationDate]` of the seven hotels equals their renovation's
`EndDate` in the Renovations sheet (April to August 2021; the works started August to December 2020). Page 1's "None
has started since 2020" and this line now say the same thing from both ends.

---

## 3 · Not built, and why

| Item | Raised by | Decision |
|---|---|---|
| F1's forward line, "the kiosks for running costs" | Investor: overstates (kiosks are about 0.2 of the 1.8 points) | **Left.** The jury gives this same line as the reason the headline-emphasis finding went from Major to Minor. Two reviewers pull opposite ways; the jury's lens is the one that scores |
| A's parts on Build add to $3.6M against $3.5M | J3-04, INV3-07, CL3-20 | **Left.** Showing the app at +$2.3M breaks "$2.4M with the agencies" on the tile; it is model work with a full recheck |
| "+$0.03M" for the kiosks in the High case | UX3-10, DS3-13 | **Left.** It is the formatter's rule (R-G1): two decimals only where one would print 0.0 for an amount that is not zero |
| Tranche 2 named "+40 rooms" on the plan and "+80 rooms" in What waits | Jury 2.4, CL3-07 | **Left.** Both are right (40 each); either rename costs a line in a slot that has none |
| The refresh navy in the hero table, slate in the plan bar | UX3-05, CL3-08, DS3-16 | **Left.** The hero's colour is the status (2028 gate), the plan bar's is the tranche; changing one adds a fourth colour without a key |
| "none yet" in the year tooltip | UX3-07 | **Left.** The words are fine; what runs together is two cells of the tooltip, which is layout |
| End labels of What waits' cash chart at their values | UX3-01, DS3-09 | **Left.** Layout: the same work as step C of round 2 on another chart |
| Build's bars scroll from eight moves | UX3-02, CL3-12 | **Left.** Layout |
| Page 2 at 1366 px (64%) | all five | **Left**, as every reviewer advises. "Best viewed full screen" goes in the description |
| The cash line meets zero at the 2030 tick; the gate marker's place | Jury 2.4, CL3-11, DS3-04 | **Left.** Model and chart work on a chart that passed the gate |
| Data points read raw numbers to a screen reader | J3-15, UX3-15 | **Left.** Format strings on six visuals' measures: model work with a full recheck |
| The whole plan added up; a threshold for tranche 3; an NPS target | Investor | **Description**, not the report (the investor's own advice for the first; the other two are new content) |

---

## 4 · Deviations from the reviewers' wording

| Reviewer's wording | Built | Why |
|---|---|---|
| "The app is the core: +$3.4M through 2032 on its own." (DS3-01) | "The app alone: +$3.4M through 2032." | The reviewer's line is 783 px in a slot of 752: a card value does not wrap, it ends in an ellipsis |
| "test: 8%", "test: $0" (DS3-07) | "≥ 8%", "≥ $0" | "test: 8%" is 54 px and its column gives its header 54. The thresholds say what each test is; the title keeps the word "tests" and the two markers above the header name them |
| "Low to High: −$6.9M to +$12.6M" (UX3-08, DS3-08) | "Low −$6.9M · High +$12.6M" | 232 px in a column that gives 214; it would wrap. The built form is the package tooltip's own grammar ("Low −$5.5M · Expected +$3.3M · High +$12.7M") |
| B: "... and 34% a year on cost against A's 37.5%" with a special sentence for Low, "where the two are equal (11.1%)" (DS3-03) | one pattern for all cases | They are not equal in Low: B earns 10.8% on its cost, A 11.1% (the engine and the workbook). The measure still carries a branch for equal values |
| Tranche 3: "not decided yet and needs a case beyond 2032" (CL3-15); one sentence that weighs the refresh against Energy (J3-01) | "2028 gate, only with a case beyond 2032" | The label takes the gate rule's own words. A sentence that weighs the refresh against the energy programme has no line on Recommended; it goes in the description |

---

## 5 · Verified

- **Files:** `schema_check` 208 files 0 failing, `a11y_check` 0, `strip_check` 0, `compliance_check` 5 of 5,
  `validate_tmdl --strict` 0 errors (7 expected warnings), `pbir_detect` 0 unwaived, `build_checks --static` 6 of 6.
  The regenerated project differs from publish 6's (`6227d6f`) in two files only: `tbl_hero/visual.json` (two header
  names) and `_Measures.tmdl` (eight measures).
- **Engine** (Desktop 2.159, a throwaway copy on its own port): `build_checks.py` 142 of 142 after the spec took the
  fifteen slot views that differ (each read against section 2 first), `number_checks.py` 809 of 809 (new: the hero's
  status word against the workbook and package B, the tile's second line names its measure), `alt_texts.py` 0 flags.
- **Renders** (throwaway copy; the session's screen turned twice, so one view whole-page and the rest in strips):
  Recommended in Low, Expected and High, What waits in Low, Expected and High, Build as it opens. No line ends in an
  ellipsis, no cell wraps beyond the count in section 2, the What waits table ends inside its card.

---

## 6 · Log

*(the publish copy, the publish, the gate and the package: written as they happen)*
