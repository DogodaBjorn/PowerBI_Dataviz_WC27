# The best-in-class dashboard canon - reference

Re-derived in this repo's own words from the research synthesis of
2026-11-05 (three independent research runs - Claude, ChatGPT, Gemini - 
merged, cross-checked and corrected; see
`research/log/2026-11-05-dataviz-best-in-class-canon.md`). Nothing here is
copied; every idea names the person or paper it comes from (CREDITS.md).
Each principle carries an id `DC-nnn` so skills and audits can cite it.

Scope: the *dashboard and report* level - what makes a whole page or
report best in class. Chart-level judgment (form, scale, words) lives in
`chart-grounding`; the finishing moves live in `dataviz-polish`; token
values in the brand kit and `design-hard-rules.md`. Where this canon and a
local doc disagree, flag both sides to the user; never silently override.

---

## 1. The thesis

**DC-001 Best in class is a set of habits, not a look.** Across the whole
canon (Tufte, Few, Cairo, Knaflic, Wexler/Shaffer/Cotgreave, IBCS, the
dashboard research of Sarikaya et al. and Bach et al.) the gap between
basic and excellent is: a named decision, a functional hierarchy
(overview → filter → detail), honest encodings, grey-plus-one-accent
color, context on every number, and trust signals underneath. Polish is
last and only in service of those.

**DC-002 Three tiers, three questions.** A report is judged on all three;
basic reports fail Meaning and System and try to compensate in Cognition
with styling.

| Tier | Question | Best-in-class criterion |
|---|---|---|
| Meaning | Which decision, for whom, at what cadence? | Every KPI, visual and interaction has a demonstrable decision function; KPIs are defined, owned, targeted and directional. |
| Cognition | Can the reader see the right thing fast and correctly? | Hierarchy, perceptually honest encodings, disciplined color and text, extraneous cognitive load near zero. |
| System | Does it stay fast, trustworthy and maintainable at scale? | Shared semantic model, consistent semantics, security, lifecycle as code, performance budgets, usage evidence, AI-ready metadata. |

**DC-003 Maturity ladder.** basic (visuals work) → professional (visuals,
metrics and interaction consistent) → enterprise (model, security,
lifecycle standardized) → high-end (continuously improved from usage,
performance data and decision impact). The last rung makes a dashboard a
product cycle, not a one-off design exercise.

**DC-004 Useful before beautiful** (Kurt Buhler, SQLBI, 2024). Two
versions of one report: the prettier one answered the core question more
slowly. The objective is a useful report; beauty is a trust and adoption
multiplier on top.

---

## 2. Theory behind the rules

### Perception
**DC-010** Cleveland & McGill (1984), replicated by Heer & Bostock (2010):
position on a common scale > position on non-aligned scales > length >
angle/slope > area > volume > color. Mackinlay (1986) re-ranked channels
per data type (hue is good for categories, poor for quantity). This is the
scientific reason sorted bars beat pies, lines beat area stacks, and 2-D
beats 3-D.

**DC-011** Bertin's visual variables, Ware's pre-attentive attributes
(hue, intensity, size, orientation, enclosure) and the Gestalt principles
(proximity, similarity, enclosure, closure, continuity) explain grouping,
alignment, whitespace-instead-of-borders, and "grey plus one accent".

### Cognition
**DC-012 Cognitive Load Theory** (Sweller). Working memory is a fixed
budget: *intrinsic* load (the data's real complexity - sequence it, never
delete it), *extraneous* load (clutter, cryptic icons, 3-D, legends far
from marks - drive to zero), *germane* load (schema-building - the only
load you want). The **split-attention effect** is the formal reason direct
labels beat legends and annotations beat footnotes.

**DC-013 Biometric evidence.** Eye-tracking studies show information load
and layout steer fixations; long fixations (> ~1 s) with fewer saccades
signal strain. One 2023 learning-analytics study reported overload around
nine or more information modules; an IEEE 2025 study (60 participants,
1,216 dashboards) confirmed object type and layout drive gaze. Treat the
"nine" as one study's finding, not a cap. The robust conclusion: more
tiles ≠ more insight.

**DC-014 The chartjunk debate.** Bateman et al. (CHI 2010) and Borkin et
al. (TVCG 2013) found embellishment can raise memorability; Few's rebuttal:
a memorable picture is not memorable data. Resolution: minimal for
monitoring displays, purposeful annotation and imagery for editorial or
communication pieces. Showpiece ≠ clutter.

### Task and requirements
**DC-015** Brehmer & Munzner's task typology (why → how → what) and
Munzner's nested model are the requirements method: before any visual is
named, know whether the reader searches, compares, monitors, discovers,
verifies or presents.

**DC-016** Shneiderman: overview first, zoom and filter, details on
demand. Operationalized for Power BI as SQLBI's **3-30-300 rule** (~3 s
overview, ~30 s filter and zoom, ~300 s detail; approximate, works across
pages via drillthrough).

**DC-017 Name the display type** (Nick Desbarats; Few vs the Big Book of
Dashboards). Few's definition - the most important information to reach
objectives, on one screen, monitored at a glance - fits *monitoring*
displays. Analytical and communication displays are different artefacts
with different rules. Most "dashboard" arguments are two people talking
about two display types.

**DC-018 Capability ladder** (Gartner): descriptive (what happened: KPIs,
trends) → diagnostic (why: drill paths, variance, anomaly) → predictive
(ranges, bands, scenarios) → prescriptive (recommendations, what-if).
Classify what a page is *for*; it decides the visual grammar.

### Dashboard research
**DC-019** Sarikaya, Correll, Bartram, Tory & Fisher (TVCG 2019): a
dashboard design space and seven genres; readers differ in visualization
literacy, data literacy and decision agency; "simplify, simplify,
simplify". Bach et al. (TVCG 2023): eight pattern groups from 144
dashboards - a vocabulary for design reviews.

**DC-020 Uncertainty** (Hullman, Kay, Padilla). Hypothetical outcome plots
beat error bars for ordering judgments; readers misread forecast error
bars as highs/lows (deterministic construal error); inferential error
bars make people overestimate effects. Show outcome variability as labeled
bands; state what any error bar means.

### KPI and data-quality theory
**DC-021 KPI anatomy.** A KPI is not a number that sounds important. The
minimum record: definition, formula, grain, time period, owner, source,
target or reference, desired direction, interpretation rule. Test: two
analysts independently compute the same figure. (This is what the
atelier's `metric.contract.yaml` exists for.)

**DC-022 Balance outcomes and drivers** (Kaplan & Norton): leading vs
lagging indicators; a KPI hierarchy headline → drivers → detail.

**DC-023 Data quality is a UX property** (Wang & Strong 1996): intrinsic
(accuracy), contextual (timeliness, completeness, relevance),
representational (consistency, interpretability), accessibility. A
correct number that is stale, undefined or hard to reach is still a bad
dashboard.

---

## 3. Design - what separates basic from best

**DC-030 Purpose and audience first.** Requirements run process → outcomes
→ users → decisions → questions → data. The failure mode is the Excel
lift-and-shift: full-page matrices treating Power BI like a spreadsheet
(Buhler, "We need this report in Power BI").

**DC-031 Information architecture.** 3-30-300; reading order top-left to
bottom-right; grid, consistent gutters, alignment; whitespace instead of
borders; conservative container styling (Van de Voorde). A working page
template: narrow header with *question + time context + refresh date* →
3–5 KPIs each with a comparison → one dominant trend/variance visual → a
few explanatory visuals → detail or drillthrough entry at the bottom. A
heuristic, not a law.

**DC-032 The 5-second test and its counterpoint.** For monitoring pages,
show the page briefly and ask what the reader took away. Alan Smith (FT)
warns against the idea that every chart must be understood in five
seconds - rich charts reward attention. Monitoring = fast; editorial =
rich; a contest page is editorial *and* must survive a five-second judge
glance.

**DC-033 Chart choice is relationship-first** (FT Visual Vocabulary / Alan
Smith): magnitude, ranking, change over time, deviation, part-to-whole,
distribution, correlation, flow, spatial - then the form. Defaults that
rarely fail: sorted horizontal bars; lines for time; bullet graphs for
actual-vs-target (Few's gauge replacement); IBCS variance bars and pins;
slope charts for two periods; small multiples instead of spaghetti;
waterfalls for bridges; tables for lookup.

**DC-034 Uniform scaling across small multiples.** Locally auto-scaled
axes destroy integrity: a $10k bar can stand as tall as a $1M bar next
door. Any side-by-side comparison shares one scale, or says loudly that
it does not.

**DC-035 Use with care:** pies and donuts (2–3 shares at most - Few would
avoid; Microsoft allows < 8 categories; SQLBI calls the rule "shades of
grey"); dual axes (invite false correlation - prefer two aligned charts or
indexed lines); log scales (right for growth rates, must be labeled);
gauges (low density); 3-D (always distorts).

**DC-036 Tables are first-class.** Right-aligned numbers, consistent
decimals, units in headers, subtle or no banding, embedded sparklines and
bars, layered headers (Few, Wong; `tb-tables` is the operational owner).

**DC-037 Color.** Grey is the most important color (Lisa Charlotte Muth,
Datawrapper): make everything grey except what matters. One accent for
emphasis. Semantic and consistent across the whole report. Good/bad only
for good/bad and never alone (pair with sign, arrow, label). Scale types:
categorical (few hues), sequential (one hue, lightness ramp), diverging
(two hues around a meaningful light-grey midpoint). Never a rainbow for
quantity. IBCS scenario notation: AC solid dark, PY light grey, PL
outlined, FC hatched; positive variance green, negative red. WCAG 2.2 AA:
4.5:1 text, 3:1 large text and meaningful graphics.

**DC-038 Typography and numbers.** Hierarchy page title → message →
visual title → labels → annotations; ≤ 2 families; thousands separators;
sensible rounding (€1.2M on a card, not 1,234,567.89); units once;
consistent decimals per column; locale-correct formats (Dutch: comma
decimal, dd-mm-yyyy); direct labels over legends; never both a labeled
axis and data labels when one suffices.

**DC-039 Message and context.** Titles are takeaways, DAX-driven so they
stay true under filtering. Every number carries target / prior / trend /
benchmark. IBCS *SAY*: a page without a message is a data dump.
Desbarats on flags: Good/Satisfactory/Poor bands and "% deviation from
target" produce false alarms and hidden problems - use evidence-based
thresholds and test them with readers.

**DC-040 Interaction.** Progressive disclosure: status → deviation →
cause → detail → action. Tooltip pages for context, drillthrough for
detail, field parameters for *controlled* flexibility. Make state
visible: no hidden visual-level filters, no self-filtering KPIs (an
on-time-% card on a page with an is-on-time slicer), no mixed
cross-highlight/cross-filter without explanation; predictable navigation
with a way back. Nothing essential lives only in hover or a click.

**DC-041 Trust signals.** Refresh timestamp, definitions reachable in one
step, data-quality flags, consistent metric semantics ("revenue" means one
thing everywhere), certified or endorsed content, a named owner.

**DC-042 Accessibility.** Alt text on every meaningful object, tab order,
accessible themes, "Show data" table checked, WCAG contrast, no jargon
titles. Few's "a dashboard accessible to the blind is a contradiction" is
a reminder to provide alternative formats, not an exemption. NL public
sector: DigiToegankelijk and the Dutch WCAG 2.2 translation.

**DC-043 Localization and mobile.** Design for translation from the start
(labels grow ~30 %; metadata translations in the model); build the mobile
layout deliberately; test on a real device.

**DC-044 Anti-patterns to name on sight.** Dashboard sprawl; the Christmas
tree (color everywhere); the rainbow effect; KPIs without comparison;
vanity metrics; slicer walls; gauges and 3-D; inconsistent color across
pages; legends far from marks; unlabeled axes and units; truncated axes;
dual-axis false correlation; hidden filters; report-only business logic
scattered across visuals; "beautiful but slow"; Excel lift-and-shift;
custom-visual sprawl.

**DC-045 Design system, bill of materials.** JSON theme; desktop + mobile
page templates; grid and spacing rules; title/subtitle patterns; standard
KPI component; permitted color semantics (incl. AC/PL/FC/PY); tooltip and
drillthrough patterns; measure naming and display folders; number-format
standards; accessibility checklist; performance budget; security matrix;
QA checklist; PBIP/TMDL structure; Dev/Test/Prod; central KPI dictionary;
custom-visual allow-list with owners and exit strategy. Mock up first,
test with users, iterate.

---

## 4. Power BI implementation layer

### Report layer
**DC-050** Themes carry the design system (colors, fonts, padding, visual
defaults) - never visual-by-visual formatting. PBIR + TMDL make design
governance code: lint colors, fonts and visual counts; diff reviews; bulk
fixes.

**DC-051** KPI cards: new card with reference labels; value + comparison +
trend; elaborate custom cards cost disproportionate maintenance (Van de
Voorde). Button slicer and field parameters for fewer, clearer controls.
Visual calculations for presentation math (running sums, % of parent) - 
business logic stays in the model.

**DC-052 Deneb.** Keeps filter context, tooltips, cross-filtering and
bookmarks (R/Python visuals do not). Vega-Lite for most needs (concise,
layered composition: bars + moving average + target rule on shared axes);
full Vega only for signals, event-driven interaction, Gantt-like layouts
or animation. Specs are code: template, document, version.

**DC-053 SVG-in-DAX budget.** A data-URI text measure with Data Category
Image URL renders per visible row in the Formula Engine (500 rows × 12
points = 6,000 evaluations for one column). Budget ~12 points per
sparkline, avoid > 24; avoid in DirectQuery. The limit is 32,766
characters per *column* text value; measures can go far larger
(CONCATENATEX ≈ 2.1 M chars - Chris Webb). "2,000 characters" is a myth.

**DC-054 Known limitations and workarounds.** Limited typography/spacing
control (improving); no native bullet or variance chart (error bars,
reference lines, SVG, Deneb, IBCS visuals); MacGyvered hacks (hidden
visuals, transparent buttons, bookmark forests) are fragile - document
and isolate report-specific objects (Buhler).

### Semantic-model layer - the consistency engine
**DC-055** Star schema; thin facts, wide dimensions; remove unneeded
columns; reduce cardinality; pre-aggregate where fitting.

**DC-056 Calculation groups** collapse fifty hard-coded measures into ten
base measures and one time-intelligence group. `SELECTEDMEASURE()`,
`SELECTEDMEASURENAME()`, `ISSELECTEDMEASURE()` (guardrails),
`SELECTEDMEASUREFORMATSTRING()`. **Dynamic format strings** keep currency
vs percentage correct when readers switch measures - the single most
useful consistency device for agent-built reports. **Precedence:** the
lowest integer evaluates innermost (scale and currency conversions first,
ratios last) or results corrupt silently (SQLBI).

**DC-057** Field parameters are built on `NAMEOF()` → rename-proof.

**DC-058** Storage mode is an architectural choice: Import (baseline),
DirectQuery (fresh or large; query reduction, aggregations), Composite,
Direct Lake (watch DirectQuery fallback). Incremental refresh for large
facts; query folding for refresh performance.

**DC-059 Performance workflow.** Performance Analyzer → render or query? →
DAX Studio server timings → Formula vs Storage Engine → VertiPaq Analyzer →
re-benchmark (cold/warm cache). DAX rules with Microsoft backing: boolean
filter arguments in CALCULATE over row-by-row FILTER; variables;
SELECTEDVALUE.

### Security, governance, lifecycle
**DC-060** RLS for rows, OLS for tables/columns; OLS does not bind
workspace Admin/Member/Contributor - consumers who need data restriction
get the Viewer role; test by impersonation per persona; think about
export paths. Purview labels travel to Excel.

**DC-061** Shared certified semantic model + thin reports (managed
self-service). Lifecycle: PBIP/TMDL in Git → Best Practice Analyzer → DAX
and data tests → performance tests → accessibility/UX review → Dev →
Test/UAT → Prod → usage monitoring. Microsoft's test categories:
functionality, data accuracy, performance, security, effectiveness,
accessibility.

**DC-062 Custom-visual policy.** Native first; certified where possible
(certification = code/test requirements and no external calls, not a
quality guarantee); security/privacy review; owner and licence recorded;
export, mobile and accessibility tested; exit strategy. The ABN AMRO
customer story: custom-visual sprawl became unmanageable until the
portfolio was rationalized - visual governance is architecture.

---

## 5. AI, Copilot and the "dashboards are dead" debate

**DC-070** Microsoft's documented Copilot limits (2026): no custom
visuals, no styling or formatting changes, needs Q&A and implicit
measures, needs a prepared model ("without preparation … generic or
inaccurate results"; "AI behavior is nondeterministic"). Prep-data-for-AI
(schemas, verified answers, instructions) lives on the semantic model.

**DC-071** Independent critique (Buhler; SQLBI 2025): generated reports
remain underwhelming - core visuals, little formatting variation. Simon
Späti: agents cannot *see* dashboards, so metrics, semantics and
governance matter more. Benn Stancil: BI splits into a governance layer
and a consumption layer. IDC's "dashboards are dead" is vendor
positioning.

**DC-072 Position.** AI moves excellence into the semantic model. Best in
class = (a) an AI-ready, governed model (explicit measures, calculation
groups, format strings, descriptions, verified answers) and (b) a
deliberately designed human monitoring layer. The main risk of generated
reports is fast proliferation of chartjunk, bad scaling and hallucinated
metrics on an ungoverned model.

---

## 6. Where experts disagree (teach the disagreement, take a stance)

| Debate | A | B | Stance |
|---|---|---|---|
| Minimalism vs embellishment | Tufte, Few | Bateman, Borkin | Minimal for monitoring; purposeful annotation and imagery for communication and contests |
| Beautiful vs useful | Showcase culture | SQLBI | Useful first; beauty multiplies trust and adoption |
| Single screen | Few | Big Book | Single screen for monitoring; pages and apps for analysis |
| Pies and gauges | Few, IBCS: eliminate | Microsoft (< 8), SQLBI | Bars and bullets by default; pies for 2–3 shares |
| IBCS strictness | Uniform notation | Brand flexibility | Strict for finance/management reporting; ISO 24896:2026 gives it formal weight |
| Native vs custom | Governance, Copilot | Deneb/IBCS expressiveness | Native by default; certified custom where analytic value is real |
| Interactivity | Rich self-service | Static simplicity | Interaction serves the 30/300 layers only |
| Dark mode | Wall displays, showpieces | Contrast, printing | Light by default; dark only with measured contrast |
| Accessibility | Few | Microsoft, WCAG | Design accessibly *and* provide alternatives |
| Flag thresholds | Traffic lights | Desbarats | Evidence-based flags, reader-tested |
| Visual calcs, SVG, Deneb | Fast, expressive | Logic fragmentation, performance, maintenance | Model-first; report-local only for presentation logic, documented |

---

## 7. Reliability notes (verify before teaching or enforcing)

| Claim | Status |
|---|---|
| ISO 24896:2026 "Notation for Business Reporting" | Verified published 11 June 2026 (IBCS Association press release); IBCS-led, aligned with IBCS 3.0 |
| SVG data-URI "~2,000 character" limit | Wrong - 32,766 chars per column text value; measures larger (Chris Webb) |
| 12-point sweet spot / 24-point max for SVG sparklines | Vendor-blog heuristic; treat as a budget to test with Performance Analyzer |
| "Overload at ≥ 9 modules"; IEEE 2025 (60 ppl, 1,216 dashboards) | Study-specific; cite as "a study found" |
| Gartner "76 % fail" | About logistics transformations - not applicable to dashboards |
| "Bateman, Borgo and Hullman" | Mis-citation; Useful Junk = Bateman et al. 2010 |
| Tool "20 % faster", "40–50 % cheaper" | Low-quality sources - not carried |
| PBIR default dates | Sources differ (Mar/Jul/Sep 2026) - verify on Microsoft Learn |
| Individual views of listed community experts | Leads, not findings, unless cited by article |

---

## 8. Sources (consult and cite; never copy)

Books: Tufte, *The Visual Display of Quantitative Information*; Few,
*Information Dashboard Design*, *Show Me the Numbers*; Cairo, *How Charts
Lie*; Knaflic, *Storytelling with Data*; Schwabish, *Better Data
Visualizations*; Wilke, *Fundamentals of Data Visualization* (free
online); Kirk, *Data Visualisation*; Wexler, Shaffer & Cotgreave, *The Big
Book of Dashboards* and *Dashboards That Deliver* (2025, with Makulec);
Desbarats, *Practical Charts* / *Practical Dashboards*; Wong, *WSJ Guide
to Information Graphics*; Alan Smith, *How Charts Work*; Munzner,
*Visualization Analysis and Design*; Ware, *Information Visualization*.

Papers: Cleveland & McGill 1984; Heer & Bostock 2010; Mackinlay 1986;
Shneiderman 1996; Brehmer & Munzner 2013; Sweller 1988; Sarikaya et al.
2019; Bach et al. 2023; Bateman et al. 2010; Borkin et al. 2013; Hullman,
Resnick & Adar 2015; Padilla, Kay & Hullman (review); Hofman, Goldstein &
Hullman 2020; Kaplan & Norton 1992; Wang & Strong 1996.

Standards and docs: IBCS Standards and ISO 24896:2026; WCAG 2.2 (+ Dutch
translation, DigiToegankelijk); Microsoft Learn - report design tips,
optimization guide, accessibility, mobile, Copilot and Prep-data-for-AI,
implementation planning, RLS/OLS, incremental refresh, query folding.

Power BI practitioners: SQLBI (3-30-300; pie charts; calculation-group
precedence; dynamic format strings; AI in Power BI); Data Goblins / Kurt
Buhler (report requirements, reporting layer, Copilot critique,
macguyver toolbox, svg-visuals skill); Tabular Editor / Ruben Van de
Voorde (data-visualization best practices 2026); Kerry Kolosko (SVG
templates); Daniel Marsh-Patrick (Deneb); Miguel Myers (core visuals
vision board); Reid Havens; Chris Webb (large images in datasets; Copilot
AI instructions); Datawrapper / Lisa Charlotte Muth (color).

Future of BI: Benn Stancil ("BI is dead"); Simon Späti ("BI is not dead",
2026).
