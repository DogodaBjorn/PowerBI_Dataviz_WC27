<!-- Grounding references for adapter 'chart-grounding' in repo 'pbi-atelier (agent-driven Power BI report studio, PBIP/PBIR, 8-stage gated lifecycle)'.
     Producer: BookCompiler (E:\bookcompiler) · bundle: bundle_v2_data-visualization · canonical schema 1.0.0.
     Regenerate after bundle updates: .venv\Scripts\python.exe tools\ground_repo.py <this adapter.yaml>
     Contract: docs/INTEGRATION_CONTRACT.md - paraphrased canonical knowledge with page-level provenance; no source-book content. -->

# Canonical principles behind `chart-grounding`

Full operational detail and provenance for every principle this skill cites. Consult on demand; SKILL.md stays concise.

## [CP-051] Name the relationship first, then pick the chart form - a thesaurus, not a wizard

**Statement.** Before choosing any chart, write the reader's question in plain words and name the one relationship it asks about - magnitude, change over time, ranking, deviation, correlation, distribution, part-to-whole, spatial or flow; shortlist forms from that family, consider at least one alternative, and name what the chosen form gives up, adding a companion view if the decision needs it. Never start from a chart type, a habit or the software's suggestion.

**Why.** Charts show relationships, not numbers: the same county populations become a magnitude chart, a ranking, a deviation from the average or a map depending on the question asked of them, so the question - not the dataset - determines the form. The FT Visual Vocabulary's nine relationship families turn a chart request into a question plus a shortlist, but they are a thesaurus of candidate forms (some forms sit in two families; the list is deliberately not exhaustive), never an automatic picker. Every chart is a design compromise: emphasising one relationship sacrifices another, and naming the sacrifice is what makes the choice deliberate and shows when a second chart is needed. Moving commissioning conversations from "what do you want" to "what do you want to show" is what changed chart quality at the FT.

**Apply when**
- any new chart, report visual or dashboard tile
- a chart is technically correct but says nothing
- a requester asks to just show the numbers, or names a chart type before the question

**Do not apply when**
- the numbers belong in a sentence or a lookup table rather than a chart (see CP-052)
- a strong domain convention fixes the form for this audience, such as candlesticks for traders

**Rules**
- write the reader's question first in plain words (how big? how has it changed? who leads? how far from target? are they linked? how spread? what share? where? from where to where?) and map it to exactly one family
- family dispatch: magnitude (CP-054), change over time (CP-055), ranking (CP-056), deviation (CP-057), correlation (CP-058), distribution (CP-059), part-to-whole (CP-061), spatial (CP-062), flow (CP-063)
- when two relationships matter, encode the primary one in the main form and carry the secondary one through sorting, colour or a second chart
- shortlist at least two forms from the family before choosing; forms that sit in two families (slope chart, Marimekko, dot strip) are bridges between them
- for each chart write down one relationship it shows and one it sacrifices; if the decision needs the sacrificed one, add a companion view (overview plus zoom, map plus a totals bar) rather than overloading one chart
- run chart requests as conversations about what to show, not about which chart to make
- check the finished chart against the question; if it emphasises a different relationship, redesign it

**Heuristics**
- the verb you would put in the title often reveals the family - surges (time), overtakes (ranking), falls below (deviation), is correlated with (correlation)
- sorting can add a ranking relationship to a magnitude chart at no cost
- prefer two clear charts over one chart that shows several relationships equally

**Diagnostics**
- what single question should a reader answer from this chart in five seconds, and which family does it belong to?
- which relationship does the current chart actually emphasise?
- what can a reader no longer answer from this chart, and does the decision depend on it?

**Transformations**
- alphabetical bars of county populations → bars sorted by size (ranking) or bars measured from the county average (deviation), depending on the question
- election map expected to show the overall winner → map of who won where, paired with a stacked bar of total votes

**Anti-patterns**
- choosing the chart type before knowing the question
- letting the software's recommended chart decide
- believing one all-purpose chart exists and cramming every relationship into it
- treating the vocabulary as a wizard, or as a list of the only permitted forms

**Evaluation criteria**
- one sentence names the relationship the chart emphasises, and the title makes the same claim
- at least one alternative from the same family was considered, and the sacrificed relationship is irrelevant or covered by a companion view

**Support.** 1 independent source(s) · confidence: medium (One source; explicit and extracted at high confidence. The per-family form lists rely on the chapters' prose because three columns of the Visual Vocabulary poster extracted jumbled.)

**Provenance.**
- `HCW-003` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “2. Why charts matter”, pp. 31–34, 39, 41–42, 173–174, 240, 262
- `HCW-006` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “3. The Financial Times visual vocabulary”, pp. 34, 38–41, 46, 72, 75, 100, 120, 140, 160, 172, 184, 194, 200, 224
- `HCW-005` (reinforces) — *How Charts Work: Understand and Explain Data with Confidence*, “2. Why charts matter”, pp. 32–33, 88, 130, 161, 195–196, 219

## [CP-052] Sentence, table or chart - choose by what the reader must do with the numbers

**Statement.** Chart only what a reader learns more from seeing than from reading: put one striking comparison in a sentence, put values readers must look up or rank precisely in a table, and keep charts for patterns - trends, distributions, flows, many-item comparisons; publish fewer, better charts. Set tables for lookup: right-aligned tabular figures, one decimal precision per column, white space instead of heavy rules, rows of interest highlighted.

**Why.** A two-column chart of one memorable comparison (China's steel output in two years against the UK's since 1870) adds no geometry to its title, and near-equal columns are hard to tell apart. Tables let readers look up any value, including totals, quickly and precisely, but make pattern-finding a working-memory task; charts do the reverse. When text and charts are planned together, charts carry what and how much, the text carries why and so what, and weak charts are cut rather than decorated - the author's fewer-but-better mantra. Right-aligned fixed-width figures keep units aligned for scanning; consistent precision avoids false signals; white space alone can form rows and columns; highlighting top and bottom rows focuses attention.

**Apply when**
- a chart would show only two or three numbers
- readers will look up specific items or exact values, or a chart would need every value labelled
- a report or deck holds many charts of uneven value, or its text restates its charts

**Do not apply when**
- readers must see the evidence for a contested claim themselves - chart it even if a sentence could state it
- the message is a shape (trend, distribution, flow) that neither a sentence nor a table conveys at a glance

**Rules**
- before charting, ask what the chart's geometry adds beyond its title; if nothing, write the sentence
- route by task: lookup or rank position → table; pattern across many numbers → chart; both → the chart for the pattern plus the table for reference
- cut charts that cannot be made useful instead of dressing them up
- plan text and charts together - charts carry what and how much, the text carries why and so what
- set tables for scanning: right-aligned numbers in tabular lining figures, the same decimal places down a column, spacing rather than heavy gridlines, and the rows the story is about highlighted
- order table rows by rank for ranking tables, and alphabetically only when readers search for a known item

**Heuristics**
- a fact that is memorable as a sentence rarely needs a chart
- if a pie or bar chart needs every value printed on it, a table may have been the honest choice

**Diagnostics**
- what do I learn from the marks that I could not get from the title alone?
- will readers search for a value or scan for a pattern?
- which charts in this report would nobody miss?

**Transformations**
- two-column chart of a single comparison → one sentence carrying both numbers
- dense table used to argue a trend → a chart for the trend plus the table for reference
- left-aligned proportional figures with mixed decimals → right-aligned tabular figures at one precision

**Anti-patterns**
- charting every number because it is a number
- text that narrates a chart point by point
- mixed decimal precision in one column; heavy gridlines that overpower the numbers

**Evaluation criteria**
- every remaining chart shows something a sentence or table could not show as efficiently
- in tables, any value is found quickly and digits line up down each column

**Support.** 1 independent source(s) · confidence: medium (One source; both principles explicit and high confidence at source.)

**Provenance.**
- `HCW-012` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “4. Charts of magnitude”, pp. 51–52, 172, 177–178
- `HCW-037` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “9. Charts of ranking”, pp. 141–142, 165, 169–170, 230, 281, 287

## [CP-053] Encode precise comparisons as position or length on a shared baseline

**Statement.** When readers must judge how much bigger one value is than another, encode the values as position or length from a common baseline - bars, columns or dots on a shared axis, with ticks or light gridlines; use area only where bigger-versus-smaller is enough or the range is extreme; never encode quantities as volume or decorative 3D; and put the component that matters on a stack's baseline, because floating segments cannot be compared precisely.

**Why.** In the FT's online experiment (over 12,000 answers) fewer than one in five readers identified the third-largest segment in all five pie charts, while more than four in five did so from the same data as columns. Asked how many times bigger one shape was than another (always eight), readers were accurate and consistent for length, more scattered for area and most error-prone for volume. Components that do not share a baseline, as in stacks and Marimekkos, are hard to compare, and perception is context dependent, so marks judged in isolation mislead. This perceptual ordering is the evidence behind the bar default, the limits on pies and the case against 3D.

**Apply when**
- the reader's task is to compare close values or ratios
- a chart uses pies, bubbles, spheres or 3D shapes to compare quantities
- stacked or segmented elements must be compared across categories

**Do not apply when**
- only rough bigger-or-smaller judgements are needed, or values span orders of magnitude so area is the better compromise (see CP-054)
- the part-to-whole cue of a pie, or a Marimekko's whole-dataset overview, matters more than precise comparison (see CP-061)

**Rules**
- prefer bars, columns and dots on a shared axis for any comparison the decision depends on
- add axis ticks or light gridlines to support exact reading
- place the most important component on the baseline of a stack; only the baseline layer compares precisely
- remove 3D effects and volumetric shapes from every chart that carries quantities
- do not rely on printed values to rescue an imprecise encoding; if every value must be printed, question whether a table is the right form (see CP-052)

**Heuristics**
- the more complex the shape, the harder it is to compare values
- accuracy falls from length to area to volume; pie angles compare poorly

**Diagnostics**
- which visual property encodes the value - position, length, angle, area or volume?
- do the marks being compared share a baseline?
- would a reader get the ratio right without the labels?

**Transformations**
- five pies compared by eye → the same data as columns on one axis
- spheres sized by value → bars, or flat circles only where a rough sense of scale suffices

**Anti-patterns**
- 3D pies, columns or spheres
- comparing stacked segments that do not touch the baseline
- data labels used as a crutch for a weak encoding

**Failure modes**
- systematic underestimation of differences encoded by area and volume
- near-equal values misread, producing the wrong ranking

**Evaluation criteria**
- every comparison that matters is made along a common scale
- no quantity is encoded by volume or decorative depth

**Tensions / disagreements**
- Precision versus overview (within the source): common-baseline encoding is more accurate, yet the author keeps Marimekkos, proportional symbols, heatmaps and pies when seeing the whole, the range or the part-to-whole cue matters more than fine differences - resolved case by case, not by rule. The canon keeps this principle as the default and names the bounded exceptions in CP-054, CP-061 and CP-064.

**Support.** 1 independent source(s) · confidence: high (One source, but the claim rests on a reported reader experiment and cited studies rather than on the author's opinion, and was extracted at high confidence.)

**Provenance.**
- `HCW-011` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “13. The science behind good charts”, pp. 50, 59, 195, 207, 228–235
- `HCW-013` (contextualizes) — *How Charts Work: Understand and Explain Data with Confidence*, “4. Charts of magnitude”, pp. 52–54, 56–61
- `HCW-040` (contextualizes) — *How Charts Work: Understand and Explain Data with Confidence*, “11. Charts of part to whole”, pp. 184–188, 191–192, 229–230
- `HCW-042` (contextualizes) — *How Charts Work: Understand and Explain Data with Confidence*, “11. Charts of part to whole”, pp. 21–22, 193–196

## [CP-065] Plot the measure that answers the question - rates, gaps and ratios, not raw totals

**Statement.** Before charting, transform the raw figure into the measure the question is about: a rate per person or unit when groups differ in size, a difference from a named reference when the question is how far above or below, a single ratio with its break-even marked when two opposing quantities must be weighed - and keep the original units recoverable wherever readers need to quote them.

**Why.** Registered weapons by US state simply mirror population; the household ownership rate moves California from the top class to the bottom. Vaccine benefits and harms shown side by side need three wide charts, but one ratio - intensive-care admissions prevented per blood clot caused - combines every scenario and isolates the one where harm outweighs benefit. Actors' heights become meaningful as centimetres taller or shorter than one actor, and a parity index is about distance from one, not size. But a purely relative measure, such as a temperature anomaly, removes the actual values, so the original metric stays on the axis or in labels when readers must describe the underlying figures.

**Apply when**
- totals vary mainly because the underlying populations differ in size
- the question is about a gap, target or parity rather than size
- two related measures must be weighed against each other across many scenarios

**Do not apply when**
- readers genuinely need absolute totals, for example to plan capacity or budgets
- the derived measure would be unfamiliar and cannot be explained to this audience

**Rules**
- write the question first, then choose the denominator or reference that answers it
- use per-person or per-unit rates to compare areas or groups of different size, and state the denominator
- collapse opposing quantities into a ratio when a threshold such as one carries the meaning, and mark the threshold
- keep the original scale, labels or a companion figure when converting to deviations or indices

**Heuristics**
- a chart of counts about human activity is usually a population chart
- a ratio with a natural break-even lets one chart show where the balance tips

**Diagnostics**
- would the ranking change if I divided by population or another base?
- is the reader asking how big, or how different from something?
- what threshold would make this measure meaningful?

**Transformations**
- number of registered weapons by state → share of adults in households with a firearm
- benefits and harms in separate panels → one ratio chart with the break-even line marked
- absolute heights on a truncated axis → deviation from a named reference height

**Anti-patterns**
- comparing raw totals across units of very different size
- relative-only charts that hide figures readers must quote

**Failure modes**
- charts that restate population size or scale instead of the phenomenon of interest

**Evaluation criteria**
- the plotted measure maps directly onto the reader's question
- readers can still recover the original units where they matter

**Support.** 1 independent source(s) · confidence: medium (The anchoring source principle is medium confidence (an assembled generalisation), which caps this one.)

**Provenance.**
- `HCW-031` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “6. Charts of correlation”, pp. 115–117, 174, 178, 214–216, 240–242
- `HCW-044` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “12. Spatial is special”, pp. 202–204, 209–211, 214–216

## [CP-066] Set every scale deliberately - zero for bars, a benchmarked range for rates, log for relative change

**Statement.** Never accept the software's axis: start bar and column axes at zero, because length encodes magnitude; zoom line and dot charts of rates and indices to the plausible or target range with the benchmark marked; choose time windows long enough to judge the latest value; use a labelled, explained log scale for relative change or extreme ranges and linear for levels; and share one value axis across panels meant to be compared.

**Why.** Software guesses a scale from the minimum and maximum but knows nothing about what the data mean or why the chart exists, and there is no neutral chart. A column chart of actors' heights starting at 100 centimetres made one bar 30 per cent of another, implying a height of 61 centimetres. A zero-anchored line of a vaccination rate hid a dangerous fall below the herd-immunity target that an 80-100 per cent axis with the target marked revealed - the rate is not a counted magnitude, so its axis can act as a lens. An auto-scaled chart of women's share of parliamentary seats looks like a solved problem; scaled to 50 per cent the remaining distance becomes the story. On a log axis equal distances mean equal ratios, so a century of a stock index shows every bubble and crash; but log axes cannot start at zero, and many general readers misread them as flatter and more reassuring. Panels with independent axes give false impressions of relative size.

**Apply when**
- setting or reviewing any value axis, time window or scale type
- a chart's differences look surprisingly large or surprisingly small
- a target, threshold, parity point or maximum gives the data meaning

**Do not apply when**
- the zero rule does not apply to line or dot charts of rates and indices where zero lies far outside any plausible value
- zooming does not apply to bars - change the form or the measure instead of truncating
- log scales do not apply to data with zero or negative values, or to questions about levels

**Rules**
- bars and columns that encode magnitude start at zero, always; never truncate or break a bar axis
- for rates and indices drawn as lines or dots, set the range to the plausible or target band, and mark and label the benchmark
- when a zero-based bar chart flattens the story, convert to deviation from a reference or to dots (see CP-057)
- name the benchmark behind every range (target, parity, equality, maximum), and let empty space carry a distance-from-goal story
- choose the time window that gives context; when zooming into recent detail, add an inset of the full history
- log scales: use for growth rates, doublings and long financial histories, or when a few values squash the rest; label the axis as log, say what each main tick multiplies by, draw dots or lines never bars, and give general audiences a linear companion or toggle
- small multiples meant to be compared share one value axis
- if a zero-based overview and a zoomed detail are both useful, show both; if only one can inform the decision, use the one that reveals the problem

**Heuristics**
- many readers never look at axis labels, so the visual impression must be right on its own
- on a log scale a straight rising line means constant percentage growth
- the same data can be bent toward opposite stories - state which benchmark you used and why

**Diagnostics**
- who chose this axis range - me or the software?
- does the length of a mark encode the value, and if so does the axis start at zero?
- is the reader's question about how much, or about how fast relative to before?

**Transformations**
- auto-scaled line hitting the top corner → axis extended to the equality line with the remaining distance labelled
- zero-anchored line of a vaccination rate → 80-100 per cent axis with the target marked
- linear century-long index dominated by recent decades → log chart showing every crash and bubble

**Anti-patterns**
- truncated bar axes
- zero-anchored rate charts that bury a meaningful decline
- unlabelled log axes, or log scales used to answer questions about levels
- refusing to adjust an axis for fear of looking biased; min-max autoscale on a chart that informs a decision

**Evaluation criteria**
- bar lengths are proportional to values
- every range is justified by a named benchmark or purpose, and the visual impression matches what a careful reader of the numbers would conclude
- the scale type matches the question and is clearly labelled

**Tensions / disagreements**
- Zero versus zoom (within the source) looks like a contradiction and is resolved by the relationship being shown - magnitude bars need zero; rates and indices may be zoomed to a benchmarked range.
- Editorial freedom versus manipulation - the same levers that let a chart tell the truth (benchmarked ranges, rescaling) can mislead; the only safeguard the source offers is a stated, defensible benchmark tied to the decision being informed (see CP-019).
- Log scales - an LSE study found general readers misread log charts as flatter and more reassuring and recommended linear or both; the author counters that some test questions were level questions suited to linear scales. The canon keeps log scales for rate questions, with an explanation and a linear companion for general audiences; time-pressured operational displays remain underspecified.

**Support.** 1 independent source(s) · confidence: medium (One source; explicit, with two contrasting worked examples for the zero rule.)

**Provenance.**
- `HCW-016` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “14. Scales of justice; axes of evil”, pp. 72, 76, 111–112, 173, 245–247, 266
- `HCW-047` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “14. Scales of justice; axes of evil”, pp. 53, 59, 68, 239–244
- `HCW-048` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “14. Scales of justice; axes of evil”, pp. 53–54, 108, 116, 130, 247–254, 261
- `HCW-020` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “5. Charts of change over time”, pp. 79–80, 113–114

## [CP-067] Write the chart - headline title first, metadata subtitle, annotations, source

**Statement.** Give every chart meant for others the words to stand alone: a narrative title drafted before building and kept as the yardstick - the finding, with an active verb that names the relationship, accurate enough to survive a fact-check; a subtitle stating what is measured, units, universe and period; short annotations tied to the key moments, targets and outliers; footnotes for definitions; and the source.

**Why.** Research by Borkin, Bylinskii and colleagues found that people spend most time on the text in a visualisation, especially the title, and that text aids recognition and recall; fifteen extra words of title and annotation turned a plain share-price chart into a memorable micro-story. Charts travel without their article, deck or report, so they must work alone. The FT's headline criteria: makes you want to look, stands alone, carries scan and search keywords, is accurate, uses an active verb, and makes a promise the graphic keeps. The subtitle is the one-stop shop for metadata, footnotes keep definitions out of the reading path, and a cited source makes the chart accountable. The annotation layer is where the insight lives: leaving a chart unannotated is not more neutral, because the decision to make the chart was already editorial.

**Apply when**
- any chart that may be read on its own - shared, exported, screenshotted or skimmed

**Do not apply when**
- exploratory charts for the analyst alone
- formal contexts that mandate descriptive titles (statistical tables, neutral reference visuals users explore themselves) - move the finding to the subtitle or a caption
- the finding is genuinely uncertain - the title must not claim more than the data and intervals support (see CP-070)

**Rules**
- draft the title as the finding before choosing or building the chart, revise it as the chart evolves, and check that the chart's most prominent feature proves it
- title: an active verb that echoes the relationship (rises, overtakes, falls below, is correlated with), the keywords readers scan or search for, no puns for international readers; How or Why to open an explainer; a coloured key word can double as the legend
- subtitle checklist: data series, units, geography or universe, time period - the dataset's name lives here, not in the title
- annotations: one short sentence each, attached by arrow, leader line or proximity, on targets, turning points, outliers and the events behind changes; numbered when order matters; never covering the data
- definitions, exclusions and method notes go in footnotes; the source goes at the foot of the chart, linked when the data are online; units in subtitle, axis and labels must agree
- test the chart cold - show it without its surrounding text and ask what it says

**Heuristics**
- it takes few words to turn a chart from numbers into a story
- without annotation a chart says here it is, work it out yourself
- an active title and a metadata subtitle make alt text almost write itself (see CP-043)

**Diagnostics**
- if this chart were forwarded alone, would the recipient understand it?
- does the title tell me what to see, or only what the data are?
- which two or three features would I point at if presenting this chart in person?

**Transformations**
- dataset name as title → the finding as title, the dataset name moved to the subtitle
- passive descriptive title → active narrative title (English homes are being eyed by overseas buyers → overseas buyers eye English homes)
- unexplained dip and recovery in a series → annotations marking the events behind both

**Anti-patterns**
- titles that merely name the dataset, or that overclaim relative to the data
- paragraph-length annotations, or annotations floating far from their data
- charts without units or sources; technical detail crowding the top of the chart

**Evaluation criteria**
- title and visual emphasis point at the same single finding
- series, units, universe, period and source are all present
- the chart's message is clear with no external context

**Tensions / disagreements**
- Narrative confidence versus uncertainty (within the source) - active headline titles can overclaim what intervals and missing variables allow; the title criteria demand accuracy, but the source gives no rule for titling an uncertain finding. Working resolution consistent with CP-019 and CP-070 - state the finding at the size the evidence allows and let the subtitle or an annotation carry the bounds.
- Editorial versus neutral titles - the source rejects the idea that unannotated, descriptive charts are more neutral, yet its own context is a newspaper; official-statistics and audit contexts may mandate descriptive titles, which the do-not-apply bound accommodates by moving the finding into the subtitle or caption.

**Support.** 1 independent source(s) · confidence: medium (One source for the chart-specific package; the title-first and payload-first behaviour is independently corroborated through CP-003 and CP-026.)

**Provenance.**
- `HCW-049` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “15. The best charts are well written”, pp. 124, 173, 256–258
- `HCW-050` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “15. The best charts are well written”, pp. 168, 247, 259–263, 281
- `HCW-051` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “15. The best charts are well written”, pp. 176, 264
- `HCW-052` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “15. The best charts are well written”, pp. 63, 93, 175, 258, 260, 266–267

## [CP-068] Label the data directly - legends are a fallback

**Statement.** Put series and segment names on or beside the data - at line ends, next to bar ends, inside or beside segments, in the series colour - so readers never shuttle between marks and a legend and meaning never rests on colour alone; keep a legend only for encodings that apply to every mark (colour ramps, size keys), or as a back-up placed next to the data or written as coloured words in the title.

**Why.** Playfair's eighteenth-century line charts had no legend: text that closely tracked the lines removed ambiguity and the burden on working memory. A many-line chart with a legend turns reading into constant scanning between key and marks. Direct labels also stop meaning from depending on colour alone, which helps colour-blind readers, and treemaps that label every segment read more easily than sunbursts that need leader lines. Labels placed close to what they label are grouped with it by proximity, the same Gestalt mechanism that makes white space do the grouping.

**Apply when**
- a chart has more than one series or segment
- colour is the only link between marks and their meaning

**Do not apply when**
- marks are too small or too dense to carry labels - label a highlighted subset or use interaction
- the legend explains an encoding shared by every mark, such as a colour ramp or a symbol size key

**Rules**
- label each line at its end or alongside it, in the line's colour
- label pie, donut and treemap segments directly, and keep segments few enough to label
- if a legend remains, place it close to the data or turn it into coloured words in the title
- place every label nearer its own mark than any neighbouring mark

**Heuristics**
- every glance away to a legend is a working-memory cost
- labels that track the data double as a check that the reader's eye is on the right series

**Diagnostics**
- how many times must a reader look away from the data to decode it?
- would the chart still work for someone who cannot tell its colours apart?

**Transformations**
- line chart with a legend box of four countries → each line labelled at its right-hand end
- sunburst with leader lines → treemap with every segment labelled

**Anti-patterns**
- legends listing many colours for many lines
- relying on hue alone to identify series

**Failure modes**
- readers attach the wrong label to a line, especially where lines cross

**Evaluation criteria**
- every series can be identified without consulting a legend
- identification survives greyscale printing

**Support.** 1 independent source(s) · confidence: medium (One source; explicit, high confidence at source.)

**Provenance.**
- `HCW-017` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “15. The best charts are well written”, pp. 74, 98, 188, 190, 262, 265
- `HCW-055` (contextualizes) — *How Charts Work: Understand and Explain Data with Confidence*, “16. Designing for charts”, pp. 276–281, 283

## [CP-069] Choose chart colour by its job - scheme by data type, saturation for the story

**Statement.** Decide what colour is doing before picking it: encoding an ordered quantity (sequential - one hue, light to dark), a deviation from a meaningful centre (diverging - two hues around a neutral midpoint), categories (qualitative - distinct hues, no implied order), or highlighting (one saturated colour on the story, grey context). Make lightness, not hue alone, carry every distinction, and build these sets into a functional chart palette.

**Why.** The three functional families map onto data relationships - sequential ramps for magnitude or order (as on choropleths), diverging schemes for deviation in two directions, qualitative palettes for categories - while highlighting is a fourth job in which saturation does the work. In the HSL model hue is the colour wheel, saturation drives highlighting and lowlighting, and lightness guarantees contrast regardless of hue; multi-hue palettes without lightness contrast collapse for readers with red-green colour blindness. Colour associations are often local (red for luck or danger) or recent stereotypes (pink and blue), though a few stable ones, such as party colours, help readers tune in. Corporate palettes were rarely designed for data, highlighting or colour blindness; the fix is to extend the brand's hues with lightness and saturation steps agreed with the design team and save the result as defaults.

**Apply when**
- choosing or reviewing colours for any chart, map, heatmap or theme
- a brand palette is mandated for charts

**Do not apply when**
- a strong, stable convention that readers expect fixes the colours (party colours, a team's home kit) - follow it

**Rules**
- ordered quantities or ranks: a sequential palette, light to dark within one hue family
- deviation from a meaningful centre (zero, target, parity): a diverging palette with a neutral midpoint
- categories: a qualitative palette of distinct hues with no implied order, few enough to tell apart
- highlighting: one saturated colour (two only for two distinct reasons) on the items the title names, everything else desaturated grey (see CP-038)
- vary lightness between neighbouring colours, and check the palette in greyscale and with a colour-blindness simulation
- audit a corporate palette for sequential, diverging, categorical, highlight and grey-context needs; extend brand hues with lightness and saturation steps agreed with the brand team, and store the sets as reusable chart defaults (see CP-042)
- avoid culture-specific or stereotyped colour associations; use stable ones when they help readers tune in

**Heuristics**
- when in doubt about a distinction, convert to greyscale and look again
- perceived colour depends on its surroundings - test colours in place, not in a swatch
- saturated colour everywhere is the visual equivalent of shouting in capitals

**Diagnostics**
- is the data ordered, centred on a reference or categorical - or is colour only highlighting?
- do adjacent colours differ in lightness as well as hue?
- can the brand palette produce a light-to-dark ramp, a diverging pair and a grey context colour?

**Transformations**
- rainbow palette on ordered data → single-hue sequential ramp
- every bar in saturated corporate red → grey bars with colour only on the items that miss the target
- red and green of equal lightness → colours that differ clearly in lightness

**Anti-patterns**
- qualitative palettes on ordered data
- distinctions carried by hue alone
- the brand colour on every element because it is the brand; gendered colour stereotypes

**Evaluation criteria**
- the scheme family matches the data type, or colour is used only to highlight
- every needed distinction survives greyscale and colour-blindness simulation
- a documented, reusable chart palette serves all three scheme types plus highlight and grey context

**Support.** 1 independent source(s) · confidence: medium (One source; explicit, with the colour-blindness demonstration a figure whose lesson is stated in prose.)

**Provenance.**
- `HCW-053` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “16. Designing for charts”, pp. 234, 271–274
- `HCW-054` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “16. Designing for charts”, pp. 173, 275–276, 302
- `HCW-010` (contextualizes) — *How Charts Work: Understand and Explain Data with Confidence*, “16. Designing for charts”, pp. 48, 86–87, 150, 161, 168, 173, 175, 262, 272–273, 298

## [CP-054] Magnitude - sorted bars by default; dots, log scales or symbols when bars fail

**Statement.** For size comparisons use bars or columns from zero, sorted by value, with the story's item highlighted - horizontal bars when labels are long or categories many. Switch form when bars fail: connected dot plots for two or more series per category, log-scale dots, snakeplots or proportional symbols when values span orders of magnitude, and countable pictograms or grouped symbols when units are naturally countable or memorability matters.

**Why.** Bars ask readers to judge one dimension against a common baseline, so more than four in five readers rank columns correctly; they are the worthy-but-boring default because they are overused, not because they are weak. Paired bars interrupt the reading of each series and spend most of their ink on what is not different, while a dot plot makes the gap itself visible and, encoding position rather than length, tolerates a zoomed axis. One giant value flattens every other bar (the Sun-and-Pluto problem); log-scale dots, snakeplots or proportional symbols - with only part of a swamping symbol drawn - keep the whole range comparable at some cost in precision. Pictograms that encode data carry no user cost and some benefit (Haroz, Kosara and Franconeri, 2015): they make units countable and comparisons memorable.

**Apply when**
- comparing the size of a handful to a few dozen categories - counts, money, volumes, rates or percentages
- two or more values per category, or values spanning orders of magnitude

**Do not apply when**
- one comparison that a sentence states better (see CP-052)
- the interest is distance from a reference (deviation, CP-057) or that the parts form a whole (CP-061)
- position in the list matters more than the value (ranking, CP-056)

**Rules**
- default: bars or columns from a zero baseline with ticks or light gridlines; columns for few categories with short labels, horizontal bars for long labels or many categories - never rotated labels
- sort by value and give the item the story is about the highlight colour
- two or three series per category across many categories: a connected dot plot - one dot per series, a thin line joining them, rows sorted by the series of interest; a zoomed axis is acceptable because position, not length, encodes the value
- extreme ranges: dots on a log axis for audiences who can read one (explain the ticks), a snakeplot that wraps over-long bars into rows of equal length, or proportional symbols sized by area with only part of a swamping symbol drawn and its value labelled; never break or truncate a bar axis
- countable units or general audiences: pictograms, grouped symbols or gridplots with one fixed unit per symbol, stated in the subtitle or key, arranged in regular rows
- keep imagery only if it measures or makes the data faster to read; imagery that would look the same with different data is decoration (see CP-001)
- stacked bars: sort by total and put the component the story is about on the baseline

**Heuristics**
- if you cannot name the fifth-largest item without counting, sort
- most of a paired bar chart's ink describes what is not different
- area sacrifices precision for range; accept it only when the full range matters more than exact ratios

**Diagnostics**
- do readers need fine differences, or only bigger and smaller?
- can the smallest values still be compared with each other?
- does each icon stand for a stated quantity, or is it decoration?

**Transformations**
- column chart with steeply angled place names → horizontal bars, sorted, key item highlighted
- alphabetical paired bars of two survey questions → dot plot sorted by one question, the two dots connected
- bar chart dominated by one giant → proportional circles with only an arc of the giant drawn

**Anti-patterns**
- rotated labels; paired bars in alphabetical order; more than two bar series per category
- breaking or truncating a bar axis to fit an outlier
- icons of varying size or spacing, or unstated symbol units

**Evaluation criteria**
- a reader ranks and roughly quantifies every category without data labels
- comparisons remain possible across the full range, and every symbol unit is stated

**Support.** 1 independent source(s) · confidence: medium (One source; explicit prose and examples, although how well individual illustrations work is partly judged from figures.)

**Provenance.**
- `HCW-008` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “4. Charts of magnitude”, pp. 46–50, 52, 173, 230–231
- `HCW-015` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “4. Charts of magnitude”, pp. 65–68, 165–166
- `HCW-013` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “4. Charts of magnitude”, pp. 52–54, 56–61
- `HCW-014` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “4. Charts of magnitude”, pp. 62–65, 68–70, 192, 217

## [CP-055] Change over time - lines by default, with a fitted form for each special case

**Statement.** Show change over time with lines by default, over a window long enough to judge the latest value, and switch form when the question demands it: a few highlighted series over grey context for many lines, slope charts for two points, re-indexed lines or shared-axis small multiples for episodes at different times, stacked areas for changing composition, timelines for durations and discrete events, and vertical timelines on phones.

**Why.** Lines are the heavy lifters because so much interest in data is about how it has changed. Each recurring failure has a known fix. Spaghetti: promote the series the story is about and grey the rest, or replace a peer group with a shaded high-low band. Two time points: a slope chart lets every line be labelled and shows ranks in both periods. Episodes separated by long gaps: small multiples sharing one value axis, or alignment on age or time since start. Composition: stacked area when values must be read, streamgraph when only the shifting pattern matters. Durations: bars on a true time axis; discrete irregular events: circles on the axis; open-high-low-close data: candlesticks. Two measures co-evolving: a connected scatterplot, sparingly. On portrait phones the longest dimension of the data should run vertically, and animation needs a memory line because fast change is hard to remember.

**Apply when**
- the question is how something changed, when, or how fast

**Do not apply when**
- only the totals at one moment matter (see CP-054)
- the sign or distance from a reference matters as much as the level - treat it as deviation (see CP-057)

**Rules**
- default: a line, with the time window chosen for context, and a small inset of the full history when the main chart zooms into recent detail (see CP-066)
- many series: colour and directly label the one to three series the title discusses, draw the rest thin and grey, or replace the peer group with a shaded highest-to-lowest band (see CP-038)
- two time points, or ranks that must be visible in both periods: a slope chart with every line labelled at both ends and risers and fallers coloured differently
- episodes at different times: re-index each to a common start, align cohorts on age or time since start, or split into small multiples that share one value axis
- parts of a changing whole: stacked area with a value axis when shares or totals must be read, streamgraph only when the shifting pattern is the message; contrasted layers adjacent, the most important on the baseline, every layer labelled directly
- durations: bars on a true time axis (Priestley timeline); discrete irregular events of varying size: circles on the time axis with notable ones annotated; open-high-low-close data for trading audiences: candlesticks
- two measures in different units moving together over time: a connected scatterplot with the start marked, dated points, direction arrows and annotated turns - only for a few trails
- many series where pattern matters more than exact values: a calendar heatmap with rows sorted by rank (see CP-064)
- columns only for sparse, ideally single series; never several column series competing over time
- portrait phones: run time vertically with annotations alongside; animate only when time has no axis of its own, always keeping a memory line of an earlier state and a static fallback or filmstrip
- projections: a central line inside scenario or probability bands, with actuals and earlier forecasts kept (see CP-070)

**Heuristics**
- grey lines are context, not clutter - they show what normal looks like
- if the dates appear only as text labels, time is not really on the chart
- equal time steps make a connected-scatter trail's length a visual measure of speed

**Diagnostics**
- which one to three lines does the title talk about?
- does the reader need the journey, or only the start and the end?
- is the reader comparing calendar timing, or the shape and size of each episode?
- where, and on what device, will most readers see this chart?

**Transformations**
- nine coloured and textured lines → two labelled focus lines over grey context, or a streamgraph if composition is the story
- paired bars of two periods → slope chart showing both values and both ranks
- one long timeline with decades of empty space → small multiples sharing one y-axis
- wide annotated line squeezed onto a phone → vertical timeline with annotations beside it

**Anti-patterns**
- a distinct colour or dash pattern for every one of many lines
- separate panels with independent y-axes for episodes meant to be compared
- streamgraphs used where readers are expected to read values
- animations whose earlier states vanish without trace; shrinking a desktop chart onto a phone

**Evaluation criteria**
- the focus series can be followed end to end, and the latest value can be judged against enough history
- every comparison the title makes (episodes, periods, ranks) is directly visible on a shared scale

**Support.** 1 independent source(s) · confidence: medium (One source. Two contributing principles (aligning episodes, stacked areas) are medium at source because their sections are brief and partly figure-dependent, which caps this one.)

**Provenance.**
- `HCW-006` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “3. The Financial Times visual vocabulary”, pp. 34, 38–41, 46, 72, 75, 100, 120, 140, 160, 172, 184, 194, 200, 224
- `HCW-019` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “5. Charts of change over time”, pp. 75, 86–87, 161
- `HCW-023` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “9. Charts of ranking”, pp. 87–88, 166–167
- `HCW-020` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “5. Charts of change over time”, pp. 79–80, 113–114
- `HCW-027` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “5. Charts of change over time”, pp. 96–98
- `HCW-025` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “5. Charts of change over time”, pp. 90–92, 94–95
- `HCW-026` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “5. Charts of change over time”, pp. 92–93, 112–114
- `HCW-022` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “5. Charts of change over time”, pp. 83–86, 109–110, 122, 124, 128, 150, 196, 218–219, 254

## [CP-056] Ranking - sort by value, then show rank alone or rank with values

**Statement.** Order categories by the value that matters, not the alphabet, wherever they have no inherent order; when position itself is the story, chart rank explicitly - a bump chart when only changing position matters, sorted bars or a dot strip when the gaps behind the ranks matter, a slope chart for two periods, a ranked table for lookup - and highlight the extremes the title discusses.

**Why.** Alphabetical order produces jagged shapes that hide rank and turn finding the seventh-largest item into counting; sorting by value adds a ranking relationship for free and makes gaps and outliers stand out - a significant reward for something as simple as sorting. No number is inherently big or small: ranking answers compared with what, through relative performance. Bump charts show changes of position very clearly but hide the values, so a club climbing to sixth may still be far behind the leader; a dot strip shows rank and gaps together. Interest in rankings usually lies at the extremes, so highlighting them, with a title that says the same, removes ambiguity.

**Apply when**
- categories have no natural order of their own (countries, products, teams, branches)
- the story is about winners, losers or positions, or about positions changing over time

**Do not apply when**
- the categories have an inherent order such as time, age bands, ordinal scales or process steps
- a lookup table in which readers search for a known item - alphabetical order helps there
- the size of the gaps matters more than the order - use a sorted magnitude chart (see CP-054)

**Rules**
- sort descending by the measure of interest; in two-series charts sort by the series the story is about, stacked bars by total, diverging and spine charts by the side the story focuses on
- in grids and heatmaps sort both rows and columns by rank so strong rows and columns cluster
- position over time only: a bump chart with the series of interest in the foreground and the rest grey
- rank plus values: sorted bars or a dot strip plot; ranks within groups: one strip row per group
- two periods: a slope chart; exact lookup: a ranked table (see CP-052)
- highlight the top or bottom positions the story discusses and make the title say the same

**Heuristics**
- if you cannot name the fifth-largest item without counting, the chart needs sorting
- a bump chart can make a small change in value look like a dramatic change in position - check the values before writing the headline

**Diagnostics**
- what order are these categories in right now, and did anyone choose it?
- compared with what - time, place or rivals?
- does the reader need the values behind the ranks, or only the positions?

**Transformations**
- alphabetical club revenue bars → bars sorted by revenue with the clubs of interest highlighted
- bump chart of a club rising to sixth → dot strip showing it is still far behind the leader
- map-like matrix of banks and cities in arbitrary order → grid sorted by presence in rows and columns

**Anti-patterns**
- accepting the software's or the source table's default order
- alphabetical order in a chart meant for comparison
- ranking charts that colour every item equally

**Evaluation criteria**
- the top and bottom items can be identified at a glance
- where values matter, the gaps between ranks are visible

**Support.** 1 independent source(s) · confidence: medium (One source; explicit, with parts of the ranking chapter's extracted text noisy but unambiguous.)

**Provenance.**
- `HCW-004` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “9. Charts of ranking”, pp. 31, 66–67, 163–165, 181, 222
- `HCW-038` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “9. Charts of ranking”, pp. 160–163, 168
- `HCW-023` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “9. Charts of ranking”, pp. 87–88, 166–167

## [CP-057] Deviation - anchor the chart to a meaningful reference, not the default axis

**Statement.** When the story is how far values sit above or below a reference - zero, target, budget, average, parity - draw bars from that reference in opposite directions, name what each direction means, shade any target band, colour only the items that miss it and keep the original metric recoverable; for opposing survey sentiment use a spine chart with don't-knows set aside; for series that cross zero over time, fill above and below or use diverging columns.

**Why.** A UNESCO chart of a gender parity index drew bars on a software-default axis with rotated labels and saturated red throughout; because the index means parity at one, the relevant relationship is deviation, not magnitude. Re-anchoring the bars at one, rotating the chart for readable labels, naming the two directions, colouring only the countries off target, restoring the target band and writing a clear title turned an unusable chart into a story. Any number can anchor a deviation chart if it is a contextual one. Purely relative charts hide the actual values. Spine charts set don't-knows aside and suit Likert scales. Filling above and below zero, inherited from Playfair's trade balance, makes contractions shout where a plain line does not; diverging columns do the same for sparse, single series.

**Apply when**
- the measure has a natural or agreed reference (zero, target, budget, parity, average)
- the question is how much above or below rather than how big
- a series changes sign and readers care whether it grew or shrank

**Do not apply when**
- readers need the absolute magnitudes and the reference adds little
- the reference is arbitrary or contested and would mislead

**Rules**
- name the reference and draw the bars from it in opposite directions; horizontal bars when labels are long
- label each direction in words (for example more girls enrolling versus more boys enrolling), with arrows if helpful
- show target or tolerance bands as labelled shaded areas and colour only the items outside them (diverging scheme, see CP-069)
- keep the original metric on the axis or in labels so the underlying figures can still be quoted
- sentiment: a spine (diverging stacked) chart with neutral and don't-know answers set to one side, sorted by one side of the divergence
- over time: fill between the line and zero, or between two lines, in contrasting colours; diverging columns only for sparse, ideally single series, with negative values highlighted
- when a zero-based magnitude chart flattens a story about differences, reframe it as deviation from a named reference (see CP-066)

**Heuristics**
- a software-default axis is often the first sign that the relationship was never chosen
- shading between two lines turns two variables into three - the gap becomes visible

**Diagnostics**
- what value represents normal, target or balance for this measure?
- can the reader tell immediately which direction is good or bad?
- is the target visible on the chart?

**Transformations**
- index bars on a default axis with rotated labels → horizontal bars diverging from parity, target band shaded, off-target countries highlighted
- stacked yes, no and don't-know bars → spine chart sorted by the share saying no, don't-knows set aside
- line of annual GDP growth → diverging columns with contractions highlighted

**Anti-patterns**
- plotting a parity or ratio index as magnitude
- saturated colour on every bar
- several column series competing over time

**Evaluation criteria**
- the reference value and the meaning of each direction are labelled
- the items outside target are identifiable at a glance

**Support.** 1 independent source(s) · confidence: medium (One source; explicit, high confidence at source.)

**Provenance.**
- `HCW-039` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “10. Charts of deviation”, pp. 172–181, 240–242
- `HCW-018` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “5. Charts of change over time”, pp. 74, 76–79, 179

## [CP-058] Correlation - scatterplot conventions, a causation warning, dual axes only with care

**Statement.** Show how two numeric measures move together with a scatterplot - explanatory variable on x, outcome on y, story points labelled, a trend line only if it helps - and say explicitly whether the link is causal, associative or unknown, because most readers assume causation; check subgroups before publishing. Use a dual-axis chart only for audiences fluent in it, each series tied visibly to its axis and both scales chosen for a stated, defensible reason.

**Why.** Scatterplots reveal aggregate patterns across thousands of points without inspecting each one; empty regions can be as telling as the cloud. Unless told otherwise, many readers assume a correlation shows cause and effect, yet a link may be causal, driven by an unseen third variable or spurious. Dual-axis charts are criticised because two axes are hard to read and arbitrary scaling of either can manufacture a relationship; the source treats this as grounds for scepticism rather than prohibition - colour and mark type tie each series to its axis, market analysts read them daily, and they work best when the two series mirror each other.

**Apply when**
- showing whether and how strongly two numeric measures move together
- a stakeholder asks whether one metric drives another
- two series in different units share a time axis

**Do not apply when**
- one of the variables is categorical - use a dot plot or categorical heatmap
- points are so dense they form a blob - use an XY heatmap (see CP-064)
- the joint path over time is the story - use a connected scatterplot (see CP-055)

**Rules**
- put the explanatory (presumed cause) variable on x and the outcome on y, even when causality is not claimed
- add a regression line and correlation figure only if they help readers judge strength and direction
- state in the title, subtitle or an annotation whether the relationship is causal, associative or unknown; never let a title's verb imply causation the evidence lacks
- before publishing a pooled correlation, colour or split the points by plausible grouping variables and check that the trend holds within groups (see CP-060)
- label the points that carry the story
- dual axes: only for audiences who read them routinely; colour each axis like its series, use different mark types, state why each range was chosen, and for general audiences index both series to a common base on one axis instead
- extra layers - colour for groups, size for magnitude, motion for time - only on a sound base, one channel at a time, each keyed (see CP-072)

**Heuristics**
- if moving one axis's range would change the story of a dual-axis chart, the chart is fragile
- empty regions of a scatterplot can be as telling as the cloud

**Diagnostics**
- would a reader infer that x causes y from this chart, and is that justified?
- could a third variable explain both?
- would the apparent dual-axis relationship survive a different but equally reasonable scaling?

**Transformations**
- scatterplot titled as if x drives y → title stating the association and its limits
- one national scatterplot with a trend line → points coloured by region, with within-group trends
- two similar-coloured lines on two unlabelled axes → columns and a line, each coloured like its own axis

**Anti-patterns**
- implying causation through titles or regression lines when only association is shown
- rescaling one axis until two unrelated series appear to track each other

**Evaluation criteria**
- the chart's wording matches the strength of the causal evidence
- in a dual-axis chart each series is unambiguously linked to its axis and the scaling is defensible

**Tensions / disagreements**
- Dual-axis charts: many practitioners advise against them outright because arbitrary scaling manufactures relationships; Smith keeps them for fluent audiences and mirroring series. The canon keeps his bounded permission and defaults general audiences to one indexed axis.

**Support.** 1 independent source(s) · confidence: medium (One source; the dual-axis principle is medium at source.)

**Provenance.**
- `HCW-029` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “6. Charts of correlation”, pp. 27–28, 39, 100–103
- `HCW-032` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “6. Charts of correlation”, pp. 117–118

## [CP-059] Distribution - choose the display by data volume, purpose and shape

**Statement.** Show how values spread with a histogram when one distribution's shape is the point; plot every observation (dot strip, barcode, beeswarm) when individuals must be found and the points are few enough to see; switch to boxplots sorted by median for many groups or very many points, stating the whisker convention; and use a Lorenz curve when the story is how unequally a total is shared.

**Why.** A histogram summarises, and its shape tells you how far a single average can be trusted; the number and width of bins shape the view. Plotting every point in a dot strip, with minimum, median and maximum marked, lets individual items be highlighted and finer patterns seen; barcode plots keep tightly clustered values from hiding one another; beeswarms show an item's broad position at a cost in precision. With thousands of points raw displays become dense noise, and horizontal boxplots - compact, easy to label, sortable by median - compare many distributions well, though they cannot reveal two peaks. A Lorenz curve makes concentration visible as a bow away from the line of equality: the top 5 per cent of US healthcare spenders account for half of all spending.

**Apply when**
- showing how values are spread within or across groups
- one item's position within a distribution is the story
- a total may be concentrated in a few units

**Do not apply when**
- a comparison of summaries is the entire story - a summary dot plot or bars may do
- the audience needs only one typical value and the distribution is known to be symmetric and stable

**Rules**
- one distribution's shape: a histogram with deliberately chosen, equal bins unless the source dictates otherwise, showing open-ended categories rather than dropping them
- few points and named items: a dot strip with the items of interest highlighted and minimum, median and maximum marked; tightly clustered values: a barcode plot
- many points where shape and broad position matter: a beeswarm, without asking readers to read values off it
- many groups or thousands of points: horizontal boxplots sorted by median, with a key stating what the whiskers show (minimum and maximum, 5th and 95th percentiles, or 1.5 times the interquartile range); check for multiple peaks first, because boxplots hide them
- concentration or inequality: a Lorenz curve - units sorted lowest to highest, cumulative share of units on x and of the total on y, both 0 to 100 per cent, the equality diagonal drawn and labelled, one or two telling readings annotated
- add a short reading key for boxplots, beeswarms, population pyramids and Lorenz curves when the audience is new to them (see CP-071)

**Heuristics**
- sorting boxplots by median adds a ranking relationship for free
- boxplot rows can be time periods, turning a distribution chart into one about change as well
- the more a Lorenz curve bows, the higher the concentration

**Diagnostics**
- does the reader need to find individual items, or compare whole spreads?
- how many points per group - can they all be seen without overlapping?
- could the data have two or more peaks that a boxplot would conceal?

**Transformations**
- 8,000 ward-level dots by region → horizontal boxplots sorted by median swing
- summary dot plot of minimum, median and maximum → dot strip of every country with the summaries overlaid
- average spending per person → Lorenz curve with the top 5 per cent's share annotated

**Anti-patterns**
- reading precise values off a jittered beeswarm
- unlabelled boxplots for an audience that has never seen one
- summarising a heavily concentrated quantity by its mean

**Evaluation criteria**
- readers can locate the items of interest or compare group spreads, as the story requires
- whisker conventions and the equality line are stated wherever those forms are used

**Support.** 1 independent source(s) · confidence: medium (One source; explicit, high confidence at source.)

**Provenance.**
- `HCW-034` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “7. Charts of distribution”, pp. 129–137
- `HCW-033` (reinforces) — *How Charts Work: Understand and Explain Data with Confidence*, “7. Charts of distribution”, pp. 120–121, 124–127, 139
- `HCW-035` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “7. Charts of distribution”, pp. 138–139

## [CP-061] Part-to-whole - pies only within strict limits, otherwise the form that fits the data

**Statement.** Use a pie or donut only to show that a few parts make one complete, meaningful whole: slices sum to 100 per cent, stay few, are labelled directly, and are never 3D, exploded, zero or negative. Otherwise choose the fitting form - stacked bars to compare several wholes, gridplots for countable shares, a waterfall when parts subtract, a treemap for hierarchy, a Marimekko when totals and their mixes must be seen at once, sorted bars if only part sizes matter.

**Why.** More than any other chart a pie signals that the components form a meaningful whole - a cue so strong that a broadcaster's pie summing to 193 per cent caused outrage. But readers compare its segments poorly (the FT test; Skau and Kosara found angle the weakest cue and arc length the strongest, donuts read as accurately as pies, exploded slices worse), so most pies carry printed values, and several pies side by side force readers to remember segments across charts. No pie can show a zero or negative part, whereas a waterfall can; a gridplot makes every percentage point countable; stacked bars use a conventional axis; treemaps label their rectangles where sunbursts need leader lines. The Marimekko, in both the magnitude and part-to-whole families, shows several totals and their composition in one memorable image at a cost in precision.

**Apply when**
- components add up to a meaningful total and that composition is the message

**Do not apply when**
- only the sizes of the components matter - use sorted bars (see CP-054)
- categories overlap, so the parts do not sum to the whole
- the change of composition over time is the story - use a stacked area or streamgraph (see CP-055)

**Rules**
- pie or donut: a complete set summing to 100 per cent within rounding, few segments, each labelled directly, the total or universe stated in a donut's centre; never 3D, exploded, zero or negative segments, and never several pies side by side
- several wholes: stacked bars (absolute or 100 per cent) on one shared axis, sorted by total, with the story's component on the baseline
- countable shares or several small compositions: a gridplot with one cell per unit, laid out ten by ten or five by twenty
- negative components or a bridge between two totals: a waterfall with start, steps and end
- hierarchy: a treemap with every rectangle labelled, rather than a sunburst with leader lines
- several totals of very different size plus their mixes in one view: a Marimekko with columns ordered by total, totals and key segments labelled, and a reading note for new audiences; split it into conventional charts when precise component comparison matters more

**Heuristics**
- if every segment needs a printed value to be understood, a bar chart or table would serve better
- whenever several pies stand side by side, ask how hard readers must work to compare segments

**Diagnostics**
- is the main message that these parts make one whole, and do they sum to 100 per cent of a complete set?
- are there several wholes, negative parts or nested categories?
- do readers need the big picture of size and composition, or exact component values?

**Transformations**
- three pies side by side → one gridplot or a set of stacked bars
- pie impossible because of losses → waterfall of gains and losses ending in the net result
- 100 per cent bars with footnoted absolute amounts → Marimekko with each total as a column width

**Anti-patterns**
- pies whose segments exceed 100 per cent because categories overlap
- many thin slices with leader lines
- percentage geometry with absolute labels reconciled in a footnote

**Evaluation criteria**
- the chosen form handles every value in the data, including negatives and hierarchy
- the parts form a real whole and every segment is labelled and distinguishable

**Tensions / disagreements**
- Pies keep a place for their unique whole-cue although the source's own reader test shows their segments are compared poorly (see CP-053); the Marimekko is kept for its overview although Stephen Few, whom the author cites and partly agrees with, argues for separate conventional charts. Both are resolved by task - when composition is the message some imprecision is acceptable; when component comparison drives the decision it is not.

**Support.** 1 independent source(s) · confidence: medium (One source; explicit rules backed by cited research and the FT reader experiment.)

**Provenance.**
- `HCW-040` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “11. Charts of part to whole”, pp. 184–188, 191–192, 229–230
- `HCW-041` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “11. Charts of part to whole”, pp. 184, 188–193
- `HCW-042` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “11. Charts of part to whole”, pp. 21–22, 193–196

## [CP-062] Map only when place is the point - rates on choropleths, counts as symbols

**Statement.** Map only when locations or geographic patterns matter to the reader more than anything else; otherwise use a sorted grid or chart, with colour for regional grouping. On choropleths map rates, ratios or ranks, never raw counts, choose classes after viewing the distribution, and beware large empty areas. Show counts as proportional or countable symbols, as cartograms on small screens, and pair any map with a chart of the totals it cannot show.

**Why.** Maps attract and contextualise like no other form and are quick to produce, which makes the discipline of when to use them more important. A draft map of banks' presence in eight European cities made cities easy to compare but banks very hard, because maps emphasise locations and distances that were irrelevant to the story; a grid sorted in both directions read easily. Choropleths of counts about people mostly reproduce population - registered weapons highlight the most populous states, while the household ownership rate reverses the picture - and the largest areas often hold the fewest people. Classes act like histogram bins: equal intervals, quantiles and Jenks natural breaks can give opposite impressions of the same data (the share of Welsh speakers). Proportional symbols and countable gridplots show counts where there is a spatial pattern, and an equal-unit cartogram keeps small, populous areas legible on phones.

**Apply when**
- the data carry a location field and a map is being considered or requested

**Do not apply when**
- the entities merely happen to have places and the comparison is between entities - use a sorted grid or chart (see CP-064)
- the quantity is everywhere and shows no spatial pattern

**Rules**
- before mapping, write down whether location, distance or a geographic cluster or gradient is the main point; if not, choose another family's chart (see CP-051)
- choropleths: map a rate per person or unit, a ratio or a rank, with the denominator stated; if the map looks like a population map, change the measure (see CP-065)
- classes: look at a histogram of the mapped values, start from Jenks natural breaks, audition equal-interval and quantile versions, move a break onto any meaningful threshold, keep the classes few, and show in the legend how values spread across them
- where large low-density areas dominate the eye, colour only populated or built-up land if the scale allows, or note the distortion
- counts: proportional symbols sized by area with a size key, or countable unit squares when exact counts matter; on crowded or phone layouts, an equal-unit cartogram with clear area codes
- pair any map with a simple chart of totals when readers will ask about the overall result
- use a sequential scheme for rates and ranks, and a diverging one only around a meaningful midpoint (see CP-069)

**Heuristics**
- a choropleth of counts about people is usually a population map in disguise
- the presence of a location column is not a reason to map
- big areas attract the eye regardless of how many people live there

**Diagnostics**
- would the story change if the places were moved around?
- is the mapped value a count or a rate, and would a population map look almost identical?
- does a different classification change the story?

**Transformations**
- map with a block per bank in each city → bank-by-city grid sorted by presence in rows and columns
- registered weapons per state → share of adults living in a household with a firearm
- default quantile classes on long-tailed data → Jenks breaks with a histogram legend

**Anti-patterns**
- mapping because the data contain geography
- raw totals on a choropleth
- accepting the software's default classification unexamined
- global maps of large circles once a phenomenon is everywhere

**Evaluation criteria**
- the map's main message depends on geography; otherwise a non-map form is used
- the mapped measure, its denominator and its classification are stated and defensible
- counts are readable at the target screen size

**Support.** 1 independent source(s) · confidence: medium (One source; explicit prose, with class-break values readable only in figures and not relied on.)

**Provenance.**
- `HCW-043` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “12. Spatial is special”, pp. 33, 108, 200–202, 217, 219–224
- `HCW-044` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “12. Spatial is special”, pp. 202–204, 209–211, 214–216
- `HCW-045` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “12. Spatial is special”, pp. 204–208
- `HCW-046` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “12. Spatial is special”, pp. 216–219

## [CP-063] Flow - draw movement with Sankey, chord, network or waterfall, never pies or snapshots

**Statement.** For movement between stages, states, places or parties - origin-destination tables, voter or customer transitions, funnels, budget bridges, connections between actors - use a Sankey for ordered stages, a chord diagram for two-way flows among many parties, a network graph when the existence of clusters is the point, and a waterfall for additions and subtractions to a running total; never split flows across arrays of pies or side-by-side snapshots.

**Why.** A pie can slice only one row or column of an origin-destination table; sixteen pies to cover inward, outward and total flows would be harder to read than the table itself, whereas a chord diagram shows all 64 values of a seven-region matrix at once. Two snapshot charts of successive elections cannot show what happened between them; a Sankey keeps both sets of totals and adds the flows between candidates, and copes with many stages. A network graph's value lies in revealing clusters - the pattern, not the number. Flow charts take longer to read but tell more, so they are published with reading instructions and restrained colour.

**Apply when**
- the data are an origin-destination matrix or a transition table
- the question is where things came from and where they went, or how stages feed a total
- relationships or co-occurrences between entities form clusters

**Do not apply when**
- only the totals at one point in time matter (see CP-054)
- readers must look up exact pairwise values - keep a table alongside or instead (see CP-052)

**Rules**
- ordered stages or before-and-after states: a Sankey with flow widths proportional to volume
- two-way flows among many parties: a chord diagram, chords coloured by the dominant partner, colour restricted to the part of the story that matters
- connections and clusters: a network graph with line thickness for the strength of each tie
- components adding and subtracting to a total: a waterfall with start, steps and end
- publish unfamiliar flow diagrams with step-by-step reading instructions, and plan to reuse the form (see CP-071)

**Heuristics**
- if the chart is an array of pies or two snapshots side by side, the flows are missing
- flow diagrams ask for more reading time; make sure the reward justifies it

**Diagnostics**
- is the story about states at a point in time, or about movement between them?
- are the stages ordered (Sankey) or are the flows mutual among peers (chord)?
- does the reader need quantities, or only to see that clusters exist (network)?

**Transformations**
- two column charts of successive first-round results → a Sankey of how each candidate's voters moved
- a set of pies, one per region → a chord diagram of all regional flows

**Anti-patterns**
- arrays of pie charts for matrix data
- side-by-side snapshots used to imply flows

**Failure modes**
- readers carry dozens of numbers in working memory and still miss the pattern

**Evaluation criteria**
- the origin, destination and size of the main flows can be read from one view

**Support.** 1 independent source(s) · confidence: medium (One source; explicit, high confidence at source.)

**Provenance.**
- `HCW-036` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “8. Charts of flow”, pp. 140–143, 145, 147, 150, 152–158, 188

## [CP-064] Heatmaps trade exact values for pattern - sort, bin, and print values when they matter

**Statement.** Use a heatmap - a calendar heatmap for many series over time, a sorted category-by-category grid, or a binned XY heatmap for a scatterplot too dense to read - when the pattern across many cells matters more than individual values: bin into few classes, sort rows and columns by rank or a meaningful grouping, explain what rows, columns and tints are, and print the values in the cells whenever their magnitudes matter.

**Why.** A calendar heatmap of fifteen countries' scores is far easier to read than fifteen tangled lines, but readers lose the ability to quantify individual values; it works best for binned data or simple integer indices, and sorting rows by broad rank reveals shared trends. For tens of thousands of scatter points, transparency helps only a little; tessellating the plot and colouring cells by count shows the strength and direction of the relationship at the cost of the individual points. In categorical grids, cells in the same tint can differ materially, so printing the numbers turns the heatmap into an enhanced table. A bank-by-city grid sorted in both directions read far better than the same data on a map.

**Apply when**
- many series over time would produce spaghetti
- a scatterplot's points merge into a blob
- the data form a two-way table and the pattern is the story
- entities are compared across places and the relationship is not spatial

**Do not apply when**
- readers must compare exact values and you cannot print them in the cells
- individual outliers are the story and aggregation would hide them
- fine continuous gradations would be flattened by a few colour classes

**Rules**
- bin continuous values into a small number of classes, or use data that are already simple integer indices
- sort rows, and columns where possible, by rank or a meaningful grouping so patterns cluster; never leave source or alphabetical order
- for dense scatterplots try lighter or outlined dots first; if the density persists, bin into hexagons or rectangles coloured by count
- write the values in the cells when the magnitudes matter, letting the tint carry the pattern
- add a short note on how to read the grid - what the rows, columns and tints represent
- use a sequential scheme for counts and levels, and a diverging one only around a meaningful midpoint (see CP-069)

**Heuristics**
- binning replaces individual points with aggregates, so interesting individuals can disappear
- sorting both axes by rank can turn an unreadable matrix into an obvious pattern

**Diagnostics**
- does the reader need values, or the overall pattern?
- are two cells with the same tint actually similar in value?
- have the rows been ordered to reveal structure, or are they alphabetical?

**Transformations**
- fifteen-line chart of political rights scores → calendar heatmap with rows sorted by score
- a scatterplot of tens of thousands of points → hexagonal XY heatmap coloured by count
- tinted categorical grid → the same grid with each cell's value printed

**Anti-patterns**
- unsorted heatmaps in source order
- expecting readers to decode precise values from tints alone

**Evaluation criteria**
- the intended pattern is visible at a glance
- wherever exact values matter, they are printed

**Support.** 1 independent source(s) · confidence: medium (One source; explicit, high confidence at source.)

**Provenance.**
- `HCW-024` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “6. Charts of correlation”, pp. 88–89, 103–105, 114–115, 222–223
- `HCW-043` (contextualizes) — *How Charts Work: Understand and Explain Data with Confidence*, “12. Spatial is special”, pp. 33, 108, 200–202, 217, 219–224

## [CP-060] Look beneath the summary - shape, hidden groups and what the chart leaves out

**Statement.** Before reporting an average or a pooled pattern, look beneath it: let the distribution's shape pick the summary (mean if symmetric, median if skewed, none if multi-peaked - find the grouping), split pooled correlations by plausible groups in case the trend reverses, open every catch-all category, footnote and unit, keep inconvenient categories rather than hiding them, and show or state the limitations that remain.

**Why.** The shape of a distribution decides how far a single summary can be trusted: in skewed data mean and median part, and the median resists outliers; a two-peaked exam distribution means no single figure describes the class and signals an unseen grouping (students who revised and those who did not, with medians of 47 and 82). A national scatterplot of party vote against religious make-up shows a positive trend that reverses within both east and west once points are coloured by region (Simpson's paradox). A survey's catch-all Other can hide the very group of interest, and an asterisked footnote can hide labels measured in a different unit from the axis. Dropping an open-ended top income bin would have misrepresented the whole dataset. Chart literacy comes as much from the variables not shown as from those that are.

**Apply when**
- a report, KPI or headline uses an average
- a correlation or pooled trend is presented as a finding
- a chart has an Other category, asterisks, footnotes or more than one peak

**Do not apply when**
- quick exploratory views for the analyst alone, where a lighter check suffices
- distributions known to be close to symmetric and stable, where a mean suffices

**Rules**
- plot a histogram or dot strip before choosing a summary statistic, and name the statistic used
- report the median, not the mean, for skewed data; with two or more peaks, identify and separate the groups before summarising
- split or colour pooled correlations by region, segment or type and check that the trend holds within groups
- check what each catch-all category contains and whether a group of interest is hidden inside it
- read every footnote and asterisk, and confirm that every label shares the axis unit
- show every category the source provides, including open-ended ones, and explain why they look different
- make the limitations that remain visible on the chart, in its subtitle or in a footnote

**Heuristics**
- trends that appear within groups can reverse when the groups are combined
- in skewed data, averages are relied upon at your peril
- a footnote on a data label can be the most important element of a chart

**Diagnostics**
- is the distribution symmetric, skewed or multi-peaked, and would mean and median tell different stories?
- which group, variable or category is absent, and would the trend survive a split?
- does every value label use the same unit as the axis?

**Transformations**
- class average exam score → two medians, for those who revised and those who did not
- one national scatterplot with a trend line → points coloured by region, with within-group trends shown
- mean household income → median plus a histogram of the full distribution

**Anti-patterns**
- quoting a mean for heavily skewed data
- accepting a pooled correlation without checking subgroups
- dropping an inconvenient tail category to tidy a chart
- mixing percentages and absolute units in one chart and explaining it with an asterisk

**Failure modes**
- a single summary that describes nobody in a divided population
- a published conclusion that reverses at the level where decisions are made

**Evaluation criteria**
- the summary matches the distribution's shape and is named
- pooled trends have been checked within the main subgroups, and remaining limitations are visible

**Support.** 1 independent source(s) · confidence: medium (One source; explicit, high confidence at source.)

**Provenance.**
- `HCW-009` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “6. Charts of correlation”, pp. 47, 101, 105–107, 127, 193–194
- `HCW-033` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “7. Charts of distribution”, pp. 120–121, 124–127, 139
- `HCW-035` (contextualizes) — *How Charts Work: Understand and Explain Data with Confidence*, “7. Charts of distribution”, pp. 138–139

## [CP-070] Show uncertainty when it is material - and say what the bounds mean

**Statement.** Treat every estimate, sample and forecast as uncertain and decide explicitly whether that uncertainty is material to the message; when it is, show it - labelled intervals or error bars whose meaning and level are stated, gradient bands for general audiences, fan charts with actuals and past forecasts for projections - and never claim a difference, a rank or a certain future where intervals overlap or scenarios diverge.

**Why.** Data presented as a chart look so authoritative that readers forget to ask how far to trust them, yet errors can be systematic or random and estimates carry statistical uncertainty. Uncertainty is not a family of the Visual Vocabulary because it applies to every family; the questions are when and how to show it. Error bars are simple, but there is no universal convention for what bounds represent, so many charts fail by not saying. For general readers a gradient conveyed a decay of plausibility away from an estimate better than error bars, without statistical training. Forecasts open several pathways into the future: a fan chart with the central forecast emphasised, actuals and earlier forecasts kept, counters readers' poor intuition for probability, and a chart of successive forecasts against outcomes shows how often central forecasts miss.

**Apply when**
- the data are estimates from samples or models, or any projection
- conclusions rest on differences that might lie within the margin of error
- the uncertainty itself is part of the story, as when estimates are exceeded or forecasts missed

**Do not apply when**
- the uncertainty is negligible relative to the differences shown - state the source's precision instead of adding clutter

**Rules**
- decide and record whether uncertainty is material to this chart's message
- state what intervals or bars represent (standard deviation, standard error, confidence interval, range) and at what level
- do not claim or rank differences between values whose intervals overlap
- for general audiences prefer gradient or blurred bands that read intuitively as uncertain
- projections: shade the scenario or probability bands, draw the central forecast distinctly, state what the bands cover, keep actuals and earlier forecasts on the chart, and show the forecast track record where one exists
- highlight values that fall outside plausible bounds and title them actively

**Heuristics**
- charts make numbers look more certain than they are
- a single forecast line is read as a promise

**Diagnostics**
- how were these numbers produced, and how wrong could they be?
- would the main conclusion survive the uncertainty?
- does the chart say what its error bars or bands mean?

**Transformations**
- point estimates presented as exact → estimates with labelled intervals or a gradient band
- single projected line → central line inside shaded probability bands, actuals and the earlier forecast kept

**Anti-patterns**
- error bars without a stated definition
- ranking items whose intervals overlap as if they were clearly different
- presenting a central forecast as if it were certain

**Failure modes**
- false precision leading to decisions on differences that are just noise

**Evaluation criteria**
- where uncertainty matters it is visible, labelled and interpreted correctly
- no claim rests on a difference inside the noise

**Support.** 1 independent source(s) · confidence: medium (One source; the forecast principle is medium at source and the gradient-versus-error-bar judgement is partly figure-dependent.)

**Provenance.**
- `HCW-058` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “17. Visualising uncertainty - a case study”, pp. 81, 294–298
- `HCW-021` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “5. Charts of change over time”, pp. 80–82

## [CP-071] No chart is innately intuitive - extend the vocabulary, teach new forms on the chart, reuse them

**Statement.** Treat every chart form as learned, not intuitive: choose the form the relationship needs, and when it is unfamiliar to this audience pay the learning cost deliberately - a compact how-to-read key or step-by-step build on the chart, tested on fresh eyes - then reuse the form for recurring data so the investment pays off; and grow an organisation's shared, tool-independent chart vocabulary with templates rather than letting software menus set it.

**Why.** Line, bar and pie charts dominate only because they are the only charts taught universally, and even they had to be learned by their first readers. A narrow vocabulary produces look-alike charts that are then criticised as boring and decorated to compensate, while forms such as scatterplots, Marimekkos, chord and Sankey diagrams carry stories simpler charts cannot - only about two in three general readers could decode a scatterplot, yet one was the FT's best-performing tweet of 2016. Playfair and Nightingale gave their first readers directions; the FT published its chord diagram of M&A flows with reading instructions (approving reactions outnumbered disapproving ones about 24 to 5) and chose a design it could reuse quarterly. At organisational scale, a visible vocabulary turned kiosk-style chart requests into conversations about what to show, and a BI team's vocabulary app replaced requirement documents and became its style guide; starting from a tool means accepting its limits.

**Apply when**
- a less familiar form (boxplot, Sankey, chord, Marimekko, population pyramid, connected scatterplot, log scale) shows what a familiar chart cannot
- the same few chart types keep producing look-alike graphics
- a stakeholder objects to a chart only because it is unfamiliar
- setting up chart standards or a template library for a team

**Do not apply when**
- the display must be read and acted on within seconds (operational tiles, status boards), where reading speed outranks depth
- the unfamiliar form shows nothing a familiar chart would not show equally well
- there is no space or channel to explain how the form is read
- the audience already reads the form daily, so instructions would patronise

**Rules**
- choose the form for the relationship first, then ask whether this audience can learn it - never the other way round
- add a compact reading key on the chart (what each mark, row, column, band or tick means) or annotate one worked reading, and give it real space
- test the key on a colleague who has not seen the chart (see CP-034)
- reuse the form and its key for recurring data rather than inventing a new chart each time
- judge an unfamiliar chart by whether most readers feel rewarded, not by whether a few call it complicated
- organisations: run chart requests as conversations about what to show, adapt the vocabulary to your audience and data, build a reusable template for every form you use in the tools you actually use, and keep the set as a living gallery and style guide

**Heuristics**
- graphicacy is a literacy gap, not a fixed ceiling; once learned, a chart is read without effort
- a narrow chart vocabulary produces look-alike charts that then get decorated to compensate

**Diagnostics**
- am I picking this form because it fits the relationship, or because everyone learned it at school?
- could someone who has never seen this chart type read it from the chart alone?
- will we publish this kind of data again, so the learning pays off?

**Transformations**
- sixteen pie charts sliced from an origin-destination table → one chord diagram with numbered reading steps, reused quarterly
- whatever charts the default software offers → a template library mirroring the chosen vocabulary

**Anti-patterns**
- vetoing a form solely because some readers have not met it before
- assuming readers will work out an unfamiliar encoding; using a novel form once and never again
- letting the software's chart menu define the organisation's visual language

**Evaluation criteria**
- a first-time reader extracts the main pattern using only the on-chart guidance
- chart requests and reviews are framed in terms of relationships to show, and templates exist for every form the team uses

**Tensions / disagreements**
- Extend the vocabulary (Smith) versus default to conventions (Krug, CP-031). Each accepts the other's boundary - Smith exempts displays read in seconds and forms that add nothing; Krug lets a departure stand when it repays its learning curve - but they differ on default posture and on how much learning is acceptable. Smith accepts substantial learning when it is taught on the chart, tested and reused; Krug's bar is a small curve. Resolve by display mode - explanatory charts for a rewarded audience extend the vocabulary; glance-speed operational displays stay conventional.
- Richness versus comprehension (within the source) - a cited LSE study found general readers misread log scales, and dashboards are read under time pressure; the source's answer (explain, offer both views, measure reader reward) leaves time-pressured operational displays underspecified.

**Support.** 1 independent source(s) · confidence: medium (One source; explicit across several chapters, high confidence at source.)

**Provenance.**
- `HCW-001` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “2. Why charts matter”, pp. 22–23, 28, 30–31, 140–141, 149, 186
- `HCW-028` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “8. Charts of flow”, pp. 30, 98–99, 128, 135, 143–145, 149, 223–224, 252, 254
- `HCW-007` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “18. Using the FT Visual Vocabulary in your own organisation”, pp. 20, 41–42, 178, 300–303, 306–307, 309–311

## [CP-072] Enrich rather than dumb down - layer secondary relationships onto one clear primary

**Statement.** When the audience is engaged and the base chart is sound, add information instead of stripping the data until nothing interesting remains: layer one secondary relationship at a time through its own channel - colour for groups, size for magnitude, motion for time - key every added encoding, keep the primary relationship the first thing seen, stop when a layer no longer changes what the reader understands, and move a competing layer to a companion chart.

**Why.** Hans Rosling's bubble charts began as ordinary scatterplots of income and life expectancy; colour by world region added a spatial relationship, bubble size added population and a sense of distribution, and animation added change over time - five of the nine relationships in one graphic - and generated broad public interest by adding information, not dumbing it down. Beeswarms can likewise take colour for category and size for magnitude. Complexity is not the enemy; unexplained complexity is. The source's own counterweight is that a chart showing several relationships equally becomes unreadable, so one relationship stays primary and anything that competes with it gets its own chart.

**Apply when**
- the base chart is sound and the audience is ready for more depth
- a secondary relationship (group, size, time) explains the main pattern

**Do not apply when**
- the chart must be read at a glance, as in operational dashboards and status tiles
- the added layers would compete with the main relationship rather than explain it
- colour is already doing another job, or there are too many categories to distinguish

**Rules**
- start from one clear primary relationship; add one layer at a time, each in a different visual channel
- provide a key for every added encoding
- stop adding when a layer no longer changes what the reader understands
- when a needed relationship would compete with the primary one, give it a companion chart instead (see CP-051)

**Heuristics**
- complexity is not the enemy; unexplained complexity is
- each added variable must earn its place by changing what the reader understands

**Diagnostics**
- what does each added layer let the reader understand that they could not before?
- is the primary relationship still the first thing seen?

**Transformations**
- plain scatterplot of income and life expectancy → the same plot coloured by region, sized by population, animated over time

**Anti-patterns**
- dumbing down data for a supposedly simple audience
- piling on encodings without keys

**Failure modes**
- layered charts that become unreadable because no layer is primary

**Evaluation criteria**
- each encoding is keyed and contributes to the story
- viewers can describe more than one relationship after viewing

**Tensions / disagreements**
- Enrich (Smith, via Rosling) versus cut every element that does no work (CP-001 - Zinsser, Krug, Handley). Both demand that every element earn its place, so they agree about decoration; they diverge on information layers. CP-001's default is subtraction for a busy, scanning audience ("cut half, then half again"); this principle's default is addition for an engaged one. Resolve by audience mode - glance-speed and scanning contexts follow CP-001; engaged, explanatory contexts may layer, each layer keyed and checked for whether it changes understanding.
- Within the source - adding layers versus preferring two clear charts over one that shows several relationships equally, and reducing clutter through foreground and background hierarchy; reconciled by one primary relationship plus decodable layers.

**Support.** 1 independent source(s) · confidence: medium (One source; explicit as the key takeaway of a section, high confidence at source.)

**Provenance.**
- `HCW-030` (supports) — *How Charts Work: Understand and Explain Data with Confidence*, “6. Charts of correlation”, pp. 107–111, 118, 137
- `HCW-005` (contextualizes) — *How Charts Work: Understand and Explain Data with Confidence*, “2. Why charts matter”, pp. 32–33, 88, 130, 161, 195–196, 219

## [CP-038] Rank first, then style - hierarchy is deliberate de-emphasis

**Statement.** Before styling anything, explicitly rank the elements (primary, secondary, tertiary), then make prominence express the ranks - mostly by actively de-emphasizing the non-primary (weight, color, contrast) rather than shouting the primary louder; make visual relationships portray actual relationships (related things look related, nested things look contained), and break every page into regions a viewer could name at a glance.

**Why.** When everything is emphasized nothing is; shouting is the symptom of an unmade ranking decision. Both design sources state the same two-step - decide importance, then let appearance preprocess the page - and both make de-emphasis the workhorse. Data journalism arrives at the same mechanism for charts: colour as a highlighter on what the title names, everything else pushed into desaturated grey context, so all the data stay visible but only the story competes for attention.

**Apply when**
- designing or critiquing any visual surface; a page feels busy or flat
- a chart has more series or categories than its story discusses

**Do not apply when**
- colour in a chart encodes a variable every reader must decode across all marks (a sequential or categorical scheme - see CP-069)

**Rules**
- one true primary action/element per surface; secondary and tertiary actively softened
- use weight and color before size for text emphasis; trade surface area against contrast to balance
- style actions by page-rank, not semantics; loud destructive styling belongs at the confirmation step
- group into nameable regions; give hierarchy a visible containment logic
- in charts: one saturated highlight on the items or series the title names (two only for two distinct reasons), everything else thin, light, desaturated grey; the highlight and the title point at the same thing
- give related chart items the same colour or shape and unrelated ones different ones; check for accidental groupings

**Diagnostics**
- blur test: what pops, in what order - and is that the intended ranking?
- can a viewer point at and name each region of this page?
- which marks does the chart's title actually discuss, and are they the ones that stand out?

**Transformations**
- everything bold and branded → one primary, the rest quietly legible
- nine coloured lines → one or two labelled focus lines over grey context

**Anti-patterns**
- emphasis inflation; shouting as unmade decisions; severity-styled buttons regardless of page role
- a rainbow of series colours with no hierarchy

**Evaluation criteria**
- the blur test returns the intended ranking; regions are nameable at a glance
- in a chart, a first-time reader looks first at the element the title is about

**Support.** 3 independent source(s) · confidence: high (Three independent sources with compatible tests.)

**Provenance.**
- `RUI-009` (supports) — *Refactoring UI*, “Hierarchy is Everything”, pp. 30–31
- `RUI-013` (specializes) — *Refactoring UI*, “Hierarchy is Everything”, pp. 39–40
- `RUI-010` (specializes) — *Refactoring UI*, “Hierarchy is Everything”, pp. 32–33
- `RUI-017` (specializes) — *Refactoring UI*, “Hierarchy is Everything”, pp. 48–51
- `RUI-018` (specializes) — *Refactoring UI*, “Hierarchy is Everything”, pp. 52–53
- `RUI-019` (specializes) — *Refactoring UI*, “Hierarchy is Everything”, p. 54
- `DMMT-013` (reinforces) — *Don't Make Me Think, Revisited*, “GUIDING PRINCIPLES”, pp. 44–47
- `DMMT-014` (reinforces) — *Don't Make Me Think, Revisited*, “GUIDING PRINCIPLES”, p. 47
- `HCW-010` (reinforces) — *How Charts Work: Understand and Explain Data with Confidence*, “16. Designing for charts”, pp. 48, 86–87, 150, 161, 168, 173, 175, 262, 272–273, 298
- `HCW-019` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “5. Charts of change over time”, pp. 75, 86–87, 161
- `HCW-055` (reinforces) — *How Charts Work: Understand and Explain Data with Confidence*, “16. Designing for charts”, pp. 276–281, 283

## [CP-040] Start with too much space - and let space do the grouping

**Statement.** Give every element far more breathing room than seems necessary, then remove space until satisfied - never add space until things stop looking cramped; keep more space around a group than inside it so proximity alone communicates belonging; give elements only the width their content needs; and prefer space (or background/shadow shifts) to borders as the separator.

**Why.** Cramped is the default failure; the subtract-from-generous direction produces calm layouts the add-when-cramped direction never reaches. Grouping-by-space is the visual version of the prose tradition's air-around-type: density repels, air invites. Data journalism grounds the same law in Gestalt perception - proximity and enclosure make readers see groups, rows and columns without extra ink - and applies it inside charts and tables, where white space can replace gridlines and boxes.

**Apply when**
- laying out anything; a design feels crowded or noisy
- a chart or table relies on gridlines, borders and boxes to show its structure

**Do not apply when**
- genuinely dense-by-purpose surfaces (data tables users came to scan) - keep their density, but still let alignment and spacing rather than heavy rules define rows and columns

**Rules**
- start roomy, subtract to taste; white space is removed, not added
- space-around-group > space-within-group, both axes
- content-driven widths; empty canvas is not a problem to fill
- separators in order: space, background change, shadow - border last
- in charts and tables, let proximity and white space form groups, rows and columns, drop gridlines and boxes that spacing can replace, and keep labels close to what they label

**Diagnostics**
- is any spacing inside a group larger than the spacing around it?
- what was added to this layout only because the canvas looked empty?
- could spacing replace any of the lines or boxes on this chart or table?

**Transformations**
- border-separated cramped panels → space-separated calm groups
- table boxed in by full gridlines → table structured by alignment and white space

**Anti-patterns**
- filling width because it exists; border-on-border separation; cramped-by-default forms
- heavy borders and gridlines doing work that spacing could do

**Evaluation criteria**
- groups read at a glance from proximity alone; nothing exists to fill space

**Support.** 4 independent source(s) · confidence: high (Four sources across disciplines.)

**Provenance.**
- `RUI-020` (supports) — *Refactoring UI*, “Layout and Spacing”, pp. 56–59
- `RUI-027` (specializes) — *Refactoring UI*, “Layout and Spacing”, pp. 83–86
- `RUI-022` (specializes) — *Refactoring UI*, “Layout and Spacing”, pp. 65–67, 71
- `RUI-058` (specializes) — *Refactoring UI*, “Finishing Touches”, pp. 206–209
- `DMMT-014` (reinforces) — *Don't Make Me Think, Revisited*, “GUIDING PRINCIPLES”, p. 47
- `OWW-031` (contextualizes) — *On Writing Well*, “Part II: Methods”, p. 47
- `HCW-055` (reinforces) — *How Charts Work: Understand and Explain Data with Confidence*, “16. Designing for charts”, pp. 276–281, 283

## [CP-042] Build color as a crafted system, not per-moment picks

**Statement.** Work in HSL, build the full palette in advance (8-10 greys, primaries and accents with 5-10 anchored-and-bisected shades each), raise saturation as lightness leaves 50%, rotate hue - never more than 20-30 degrees - to brighten or darken without draining intensity, and temperature-tint the greys instead of using pure neutral.

**Why.** On-the-fly color manipulation (lighten/darken functions, hex intuition) produces washed-out, incoherent palettes; the craft is in pre-built shade systems and perceptually honest adjustments. Data journalism converges on the same two moves - HSL as the working model, with saturation for highlighting and lightness for contrast, and a palette defined once and saved as defaults - and adds what a palette must provide once it carries data.

**Apply when**
- founding or auditing a product palette; shades keep being invented ad hoc
- a brand palette must serve charts and dashboards

**Rules**
- HSL as the working model; anchor base/darkest/lightest per color, bisect the gaps
- saturation compensates lightness extremes; hue rotation (≤20-30°) toward bright/dark hues adjusts brightness without greying
- saturate greys slightly toward the design's temperature
- a palette that will carry data must also supply sequential ramps, a diverging pair, categorical hues that differ in lightness, a highlight and a grey context colour - extend the brand hues with lightness and saturation steps agreed with the brand team rather than inventing unrelated colours (see CP-069)

**Diagnostics**
- do the light and dark shades still look like the same color, at full intensity?
- can this palette produce a light-to-dark ramp, a diverging pair and a grey context colour?

**Transformations**
- lighten(brand, 20%) sprinkled in code → the predefined shade scale
- five saturated brand hues used on every chart → brand hues plus tints and a neutral grey, defined as sequential, diverging and categorical sets

**Anti-patterns**
- five-color palette generators for real UIs; white-at-opacity as de-emphasis on colored grounds
- solving the same chart colour problems anew for every chart

**Evaluation criteria**
- every used color resolves to a palette member; extremes hold intensity; greys carry the temperature

**Support.** 2 independent source(s) · confidence: medium (The system approach now has two sources, but the statement's numeric specifics rest on one source and partly on figures not fully visible in extraction.)

**Provenance.**
- `RUI-037` (supports) — *Refactoring UI*, “Working with Color”, pp. 119–122
- `RUI-038` (specializes) — *Refactoring UI*, “Working with Color”, pp. 123–128
- `RUI-039` (specializes) — *Refactoring UI*, “Working with Color”, pp. 129–132
- `RUI-040` (specializes) — *Refactoring UI*, “Working with Color”, pp. 133–134
- `RUI-041` (specializes) — *Refactoring UI*, “Working with Color”, pp. 134–138
- `RUI-042` (specializes) — *Refactoring UI*, “Working with Color”, pp. 139–141
- `HCW-053` (reinforces) — *How Charts Work: Understand and Explain Data with Confidence*, “16. Designing for charts”, pp. 234, 271–274
- `HCW-054` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “16. Designing for charts”, pp. 173, 275–276, 302

## [CP-026] Front-load the payload - in headings, sentences and pages

**Statement.** Put the most important words and information first at every level: headings open with their key words and say plainly what the reader gets; sentences open with actor and action; the top of a page confirms the reader is in the right place and carries what most of the audience came for; headlines are 90% clear before they are 10% clever.

**Why.** Scanners decide from openings; front-loading is how content survives the F-pattern, the search results page and the feed. Curiosity-gap headings and back-loaded sentences tax exactly the attention the audience hasn't granted yet. Charts obey the same rule: readers spend most of their time on a chart's text, especially its title, so the title carries the finding and the dataset's name drops to the subtitle.

**Apply when**
- writing any heading, headline, page opening, chart title or scannable unit

**Do not apply when**
- deliberately literary openings for committed-reading contexts (see CP-012's tension)

**Rules**
- key words first in every heading; the heading states what the reader can get or do
- the page top: confirm right place + deliver what ~80% came for; the rest findable below
- open sentences with subject and verb; move framing clauses behind them
- headline: understandable alone, the reader inside it, specific about the payoff
- chart titles: the finding as an active-verb headline with the keywords readers scan for and no puns; the dataset name goes in the subtitle (see CP-067)

**Diagnostics**
- truncate each heading after three words - does the payload survive?
- what fraction of the audience finds their answer above the fold?

**Transformations**
- 'Everything you need to know about X' → the actual answer/promise, keyworded first
- chart titled with the dataset's name → the finding as title, the dataset name in the subtitle

**Anti-patterns**
- teaser headings; joke-first labels; context paragraphs before the point; buried subjects

**Evaluation criteria**
- headings scan as promises kept; first lines carry actors and payloads

**Support.** 3 independent source(s) · confidence: high (Three independent sources, mechanically compatible.)

**Provenance.**
- `CDE-032` (supports) — *Content Design*, “Design”, pp. 196–198
- `CDE-033` (supports) — *Content Design*, “Design”, pp. 198–199
- `EWR-022` (reinforces) — *Everybody writes*, “Part I Writing Rules”, pp. 96–98
- `EWR-062` (specializes) — *Everybody writes*, “Part VI 20 Things Marketers Write”, pp. 339–344
- `HCW-050` (reinforces) — *How Charts Work: Understand and Explain Data with Confidence*, “15. The best charts are well written”, pp. 168, 247, 259–263, 281

## [CP-034] Watch real people use it - early, small, recurring

**Statement.** Test with real people from before you design (on competitors or the thing you're replacing) through every artifact after: small qualitative rounds on a fixed recurring cadence beat one big late study; recruit loosely and grade on a curve; facilitate neutrally with think-aloud; fill the observation room; debrief the same day and fix the worst problems first - expecting behavioral patterns from about five participants, and never filing access needs as outliers.

**Why.** Watching one real person beats any argument about what users would do; more rounds beat more rigor because each round's fixes change what the next round can find. Observation is also the persuasion mechanism - watching is what changes teams. Makers quickly lose the ability to see their own work as a newcomer would, which is why even a single chart benefits from a cold read by someone who did not make it.

**Apply when**
- any point in making something people must use - including before design starts
- a chart uses an unfamiliar form or will inform an important decision

**Do not apply when**
- questions of appeal/desirability (that's what planning research and focus-group-style methods are for - not a substitute in either direction)

**Rules**
- fixed recurring test day; roughly three participants; decide fixes before the next round
- tasks worded so participants can act, with details they can supply themselves
- neutral facilitation - think aloud, no leading, no rescue; probes saved for the end
- same-day debrief, collective list, worst-ten ranked, owners and dates assigned, then stop
- when a participant stumbles, ask: would our real users hit this too?
- for one-off artifacts such as charts, at minimum a cold read-back: ask someone uninvolved what it says, compare with the intended message, and fix the gap - often with a clearer title, a reading key or a different form

**Diagnostics**
- when did a real outsider last try this in front of the team?
- has anyone other than the maker read this chart cold, and what did they say it shows?

**Transformations**
- one late big study → a morning a month, forever
- maker's private judgement of a chart → a quick read-back by an uninvolved colleague before publication

**Anti-patterns**
- focus groups standing in for usability tests; easy-fix cherry-picking at debrief; testing only your own finished thing
- publishing novel chart designs untested

**Evaluation criteria**
- a standing cadence exists; each round's top problems are fixed before the next; observers attend
- an uninvolved reader states a chart's intended message unprompted

**Support.** 3 independent source(s) · confidence: high (Three independent sources; the method cluster is the first source's core teaching.)

**Provenance.**
- `DMMT-034` (supports) — *Don't Make Me Think, Revisited*, “MAKING SURE YOU GOT THEM RIGHT”, pp. 125–126, 128–130, 152
- `DMMT-033` (contextualizes) — *Don't Make Me Think, Revisited*, “MAKING SURE YOU GOT THEM RIGHT”, pp. 123–124
- `DMMT-036` (specializes) — *Don't Make Me Think, Revisited*, “MAKING SURE YOU GOT THEM RIGHT”, pp. 131–132, 151
- `DMMT-037` (specializes) — *Don't Make Me Think, Revisited*, “MAKING SURE YOU GOT THEM RIGHT”, pp. 133, 136–137, 139–140, 143, 146
- `DMMT-038` (specializes) — *Don't Make Me Think, Revisited*, “MAKING SURE YOU GOT THEM RIGHT”, pp. 135–136
- `DMMT-039` (specializes) — *Don't Make Me Think, Revisited*, “MAKING SURE YOU GOT THEM RIGHT”, pp. 148–150
- `DMMT-035` (specializes) — *Don't Make Me Think, Revisited*, “MAKING SURE YOU GOT THEM RIGHT”, pp. 126, 134, 149
- `CDE-026` (reinforces) — *Content Design*, “Preparation”, p. 164
- `HCW-059` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “17. Visualising uncertainty - a case study”, pp. 12, 41, 223, 299, 306

## [CP-019] Never overstate - credibility is a one-strike asset

**Statement.** Keep every claim at the size of the truth - including what a chart's scale, geometry and title imply: no inflated incidents, manufactured intensities, unearned superlatives or false precision; verify names, figures, dates and arithmetic against primary sources before publishing; correct errors visibly - because one statement the audience catches as bogus poisons everything after it, and commercial content is suspected before it is read.

**Why.** Credibility is fragile and non-renewable within a piece; exaggeration also numbs. Handley extends Zinsser's rule into infrastructure (fact-checking, primary sourcing, visible corrections, publisher standards stricter than a newsroom's) because a commercial motive raises the burden of proof; content design adds that visible quality - down to spelling - is a condition of being trusted at all. Data journalism extends the rule to what a chart claims without words: a truncated bar axis can misstate a ratio several times over, and point estimates without their uncertainty claim a precision the data lack.

**Apply when**
- drafting anything tempted toward exaggeration; reviewing claim-heavy copy; publishing under a brand
- publishing a chart or a number that will inform a decision

**Do not apply when**
- declared satire/parody where heightening is the visible device, kept under control

**Rules**
- report incidents at actual size; cut fabricated intensities
- every factual claim must survive the challenge: really? - and trace to its original source
- cite while you write; correct visibly when wrong
- in charts: bar lengths proportional to values, every axis range tied to a stated benchmark, uncertainty shown where it is material, and titles and verbs no stronger than the data and intervals allow (see CP-066, CP-070)
- before publishing a pattern, check that it survives a split by the main subgroups and that nothing decisive hides in a catch-all category or footnote (see CP-060)

**Diagnostics**
- which sentence would I not defend as literally true or clearly figurative?
- which claims have I actually traced to a primary source?
- would this chart's visual impression match what a careful reader of the numbers concludes?

**Transformations**
- hyperbolic scene → the actual odd detail (stranger and funnier)
- column chart starting at 100 → zero-based bars, or deviation from a named reference

**Anti-patterns**
- superlative stacking; sourcing from whoever reposted it; silent corrections
- truncated bar axes; point estimates presented as exact; differences claimed inside overlapping intervals

**Evaluation criteria**
- claims all survive scrutiny and sourcing; effects land without volume

**Support.** 4 independent source(s) · confidence: high (Four independent sources.)

**Provenance.**
- `OWW-029` (supports) — *On Writing Well*, “Part II: Methods”, pp. 45–46
- `EWR-056` (reinforces) — *Everybody writes*, “Part V Publishing Rules”, pp. 274–275, 278–286, 346–347
- `EWR-049` (reinforces) — *Everybody writes*, “Part V Publishing Rules”, pp. 245–247
- `CDE-004` (contextualizes) — *Content Design*, “Preparation”, pp. 52–54
- `HCW-047` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “14. Scales of justice; axes of evil”, pp. 53, 59, 68, 239–244
- `HCW-058` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “17. Visualising uncertainty - a case study”, pp. 81, 294–298
- `HCW-009` (reinforces) — *How Charts Work: Understand and Explain Data with Confidence*, “6. Charts of correlation”, pp. 47, 101, 105–107, 127, 193–194
- `HCW-016` (contextualizes) — *How Charts Work: Understand and Explain Data with Confidence*, “14. Scales of justice; axes of evil”, pp. 72, 76, 111–112, 173, 245–247, 266

## [CP-043] Accessibility is a design constraint, not a compliance garnish

**Statement.** Build access in as a first-class constraint: meet contrast minimums (4.5:1 normal, 3:1 large text) by design moves that keep the design good (flip to dark-on-light, rotate hue) rather than by wrecking it; never let color be the only carrier of meaning; give every non-text element a genuine text alternative matched to intent; never classify disabled people as research outliers; and sequence the work - fix what confuses everyone, then the assistive-tech specifics.

**Why.** Three sources independently refuse the garnish model: visual design supplies craft-compatible techniques, content design the research ethics and alternatives discipline, usability the sequencing insight that guidelines applied to a confusing design fix nothing. Data journalism adds the chart-specific package: contrast for data as well as text, legible type, distinctions carried by lightness rather than hue, alt text written from the chart's own title and subtitle, and the underlying data on offer.

**Apply when**
- any visual or content decision; planning research; auditing products
- publishing any chart, especially online

**Rules**
- contrast minimums met creatively (invert, rotate hue) - not by abandoning the palette
- every meaning carried by color gets a second channel (icon, label, contrast)
- every non-text element: would someone who cannot see or load it still get the meaning? alt text matches intent
- access needs are patterns to serve, never exceptions to file
- charts: test data marks and text against contrast requirements; keep on-screen text at roughly 16px minimum in relative units, sans-serif labels and tabular figures; let lightness, not hue alone, carry every distinction; write alt text as [chart type] of [subtitle] that shows [title], then the trend, a few key figures and the source; offer the data as a table or download where feasible

**Diagnostics**
- greyscale the design - what meaning disappears?
- can someone who cannot see this chart get its message from the alt text alone?

**Transformations**
- white text darkened-background hack → dark colored text on light colored background
- chart image published without alt text → alt text built from chart type, subtitle and title, plus trend, key figures and source

**Anti-patterns**
- contrast fixed by ugliness (then reverted); decorative alt text; accessibility deferred to a final audit
- low-contrast pastel chart text; images of charts published without alt text

**Evaluation criteria**
- contrast passes; greyscale test loses nothing; alt text conveys intent; research includes access needs by default

**Support.** 4 independent source(s) · confidence: high (Four independent sources.)

**Provenance.**
- `RUI-043` (supports) — *Refactoring UI*, “Working with Color”, pp. 142–145
- `RUI-044` (supports) — *Refactoring UI*, “Working with Color”, pp. 146–148
- `CDE-040` (reinforces) — *Content Design*, “Design”, pp. 209–211
- `CDE-026` (reinforces) — *Content Design*, “Preparation”, p. 164
- `DMMT-047` (contextualizes) — *Don't Make Me Think, Revisited*, “LARGER CONCERNS AND OUTSIDE INFLUENCES”, pp. 184, 189–192
- `HCW-056` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “16. Designing for charts”, pp. 284–289
- `HCW-053` (reinforces) — *How Charts Work: Understand and Explain Data with Confidence*, “16. Designing for charts”, pp. 234, 271–274

## [CP-001] Cut every element that does no work

**Statement.** Remove every element - word, sentence, paragraph, interface component or chart element - that does not add something the audience needs: functionless words, long words with short equivalents, inflated phrases, repetition, happy talk, decorative page furniture, chart ornament, whole charts that add nothing beyond their title, and anything the audience already knows or can infer.

**Why.** Attention is the scarce resource. Element strength is inversely proportional to the noise around it; unread words and unused elements still make the artifact look daunting and bury what matters. Five of six corpus sources arrive at this rule independently, for prose, for interface copy, for whole screens and for charts - where data journalism adds a bound: imagery that encodes the data is not decoration.

**Apply when**
- revising any draft, page, screen or chart
- an artifact feels padded, busy, official or important-sounding

**Do not apply when**
- removal would cost facts the audience needs to understand, decide or act
- the density IS the content (reference tables, data pages people came to scan)
- imagery that itself encodes the data, such as countable pictograms or illustrations on a common scale
- information layers an engaged audience needs to understand the data (see CP-072 and the tension below)

**Rules**
- delete what loses nothing by its absence
- replace laborious phrases with their short equivalents
- start with the worst offenders: welcome blurbs, self-congratulation, filler that only makes a page look full
- in charts: delete 3D and any ornament that would look the same whatever the data said; fix a dull chart with a better-matched form, a sharper title or a highlighted finding, never with adornment
- cut whole charts whose marks add nothing beyond their title, and write the sentence instead (see CP-052)

**Diagnostics**
- is every element doing new work?
- what exactly would the audience miss if this vanished?
- would this graphic element still be there if the data were completely different? If so, it is decoration

**Transformations**
- inflated official phrasing → the plain fact it hides
- welcome/self-praise paragraph → deleted entirely, its one real fact moved into a heading
- chart decorated to look less dull → plain chart with a better-matched form, a narrative title and one highlighted finding

**Anti-patterns**
- throat-clearing frames; euphemism; fad vocabulary; happy talk; filling space because a sparse page looks empty
- chartjunk added to make thin data look exciting; 3D effects on quantities

**Evaluation criteria**
- the revision is materially shorter/leaner with zero information loss
- every visible chart element encodes data or helps the reader decode it

**Tensions / disagreements**
- Cut (Zinsser, Krug, Handley) versus enrich (Smith, CP-072). Both require every element to earn its place and both reject decoration, but they diverge on information layers in data displays - this principle's default is subtraction for a busy, scanning audience; Smith's is addition for an engaged one, each added layer keyed and tested for whether it changes understanding. Resolve by audience mode - glance-speed and scanning contexts cut; engaged, explanatory charts may layer.

**Support.** 5 independent source(s) · confidence: high (Multi-source, operationally identical advice with independent rationales.)

**Provenance.**
- `OWW-003` (supports) — *On Writing Well*, “Part I: Principles”, pp. 11, 15–17
- `OWW-007` (specializes) — *On Writing Well*, “Part I: Principles / Part II: Methods”, pp. 16, 41, 84–85, 114–115
- `DMMT-019` (reinforces) — *Don't Make Me Think, Revisited*, “GUIDING PRINCIPLES”, pp. 60–61
- `DMMT-015` (specializes) — *Don't Make Me Think, Revisited*, “GUIDING PRINCIPLES”, pp. 49–50, 148
- `EWR-012` (supports) — *Everybody writes*, “Part I Writing Rules”, pp. 71–72, 77
- `EWR-013` (specializes) — *Everybody writes*, “Parts I and II”, pp. 72–73, 171–172
- `CDE-036` (contextualizes) — *Content Design*, “Design”, pp. 202–203
- `HCW-002` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “2. Why charts matter”, pp. 25–27, 124–125, 233
- `HCW-012` (specializes) — *How Charts Work: Understand and Explain Data with Confidence*, “4. Charts of magnitude”, pp. 51–52, 172, 177–178
- `HCW-014` (contextualizes) — *How Charts Work: Understand and Explain Data with Confidence*, “4. Charts of magnitude”, pp. 62–65, 68–70, 192, 217
- `HCW-030` (**contradicts**) — *How Charts Work: Understand and Explain Data with Confidence*: Smith urges adding information rather than stripping it away - layering colour for groups, size for magnitude and motion for time onto a sound chart for an engaged audience, against dumbing data down. Bounded - he keeps one primary relationship, keys every layer and stops when a layer no longer changes understanding, and exempts charts read at a glance - so the disagreement is about the default direction for information layers (subtract for scanners, add for engaged readers), not about decoration, which both reject.

<!-- rendered by bookcompiler skill compiler v1.0.0 -->
