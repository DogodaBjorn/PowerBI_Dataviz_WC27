# Scout: what turns basic dashboarding into best-in-class - 2026-11-05

**Trigger:** user request to research everything about data visualization
and dashboard design, "what makes best in class", with a Power BI
application layer and an emphasis on third-party verified experts; three
independent deep-research runs (Claude, ChatGPT, Gemini Pro) merged and
cross-checked, then turned into (1) standalone skills, (2) this repo's
`dataviz-canon` skill, (3) preparation of the PowerBI_Dataviz_WC27 entry.

**Sources consulted (cited, nothing copied):**

- Stephen Few - *Information Dashboard Design*; Perceptual Edge blog
  (dashboard definition; critiques of memorability research; accessibility
  position) - https://www.perceptualedge.com/blog/
- Edward Tufte - data-ink, chartjunk, sparklines, small multiples
- Alberto Cairo - *The Functional Art*, *How Charts Lie*
- Cole Nussbaumer Knaflic - *Storytelling with Data*
- Jonathan Schwabish - *Better Data Visualizations*; Claus Wilke - 
  *Fundamentals of Data Visualization*; Andy Kirk - *Data Visualisation*
- Nick Desbarats - display taxonomy, *Practical Dashboards* - 
  https://www.practicalreporting.com/
- Wexler, Shaffer, Cotgreave (+ Makulec) - *The Big Book of Dashboards*,
  *Dashboards That Deliver* (Wiley 2025)
- Dona Wong - *WSJ Guide to Information Graphics*
- Alan Smith / FT - Visual Vocabulary, *How Charts Work*
- Lisa Charlotte Muth / Datawrapper - color guidance - 
  https://www.datawrapper.de/blog/category/color-in-data-vis
- IBCS Association - standards; ISO 24896:2026 press release - 
  https://www.ibcs.com/iso-24896-press-release/
- Cleveland & McGill 1984; Heer & Bostock 2010; Mackinlay 1986; Bertin;
  Ware; Munzner; Brehmer & Munzner 2013; Shneiderman 1996; Sweller (CLT)
- Sarikaya et al., TVCG 2019 - https://alper.datav.is/publications/dashboards/
- Bach et al., TVCG 2023 - https://arxiv.org/abs/2205.00757
- Bateman et al. 2010; Borkin et al. 2013; Hullman/Kay/Padilla on
  uncertainty - https://users.eecs.northwestern.edu/~jhullman/hops_jobs_pfs.pdf
- Kaplan & Norton (Balanced Scorecard); Wang & Strong 1996 (data quality)
- SQLBI - 3-30-300 rule (Buhler) - https://www.sqlbi.com/articles/introducing-the-3-30-300-rule-for-better-reports/ ;
  pie charts; calculation-group precedence; dynamic format strings; AI in
  Power BI
- Data Goblins (Kurt Buhler) - report requirements, reporting layer,
  Copilot critique, macguyver toolbox - https://data-goblins.com/
- Tabular Editor blog (Ruben Van de Voorde) - data-visualization best
  practices 2026 - https://tabulareditor.com/blog/data-visualization-best-practices-for-power-bi-reports
- Kerry Kolosko - SVG templates - https://kerrykolosko.com/
- Chris Webb - storing large images (32,766-char fact) - 
  https://blog.crossjoin.co.uk/2019/05/19/storing-large-images-in-power-bi-datasets/ ;
  Copilot AI instructions
- Microsoft Learn - dashboard design tips, optimization guide,
  accessibility, mobile, Copilot, Prep data for AI, implementation
  planning, PBIR; Core Visuals Vision Board (Miguel Myers)
- Benn Stancil - "BI is dead" - https://benn.substack.com/p/bi-is-dead ;
  Simon Späti - "BI is not dead 2026" - https://www.ssp.sh/blog/bi-is-not-dead-2026/
- Gartner - analytics capability model; D&A predictions 2026 (via Gemini
  run; the "76 % fail" statistic was found to concern logistics
  transformations and was dropped)

## Findings

Three runs agreed on the thesis: best in class is a set of habits, not a
look - purpose-first, overview→filter→detail hierarchy, honest encodings,
grey-plus-accent color, context on every number, trust underneath. They
differed in *which layer they saw*: Claude covered the expert canon and
Power BI craft; ChatGPT added the enterprise **System** tier (KPI anatomy,
data quality as UX, RLS/OLS, lifecycle, custom-visual governance, Dutch
accessibility/localization); Gemini added the cognitive mechanism
(Sweller's Cognitive Load Theory, split-attention) and the semantic-model
consistency engine (calculation groups, dynamic format strings,
precedence; Deneb Vega vs Vega-Lite; SVG-in-DAX budgets).

Cross-checks changed the record: ISO 24896 is published (11 June 2026),
not a work item; the "2,000-character SVG limit" is false (32,766 per
column text value); a Gartner statistic and a paper citation in the
Gemini run were wrong and were dropped. Full merged synthesis with a
reliability table: `.claude/skills/dataviz-canon/references/canon.md`.

What the repo already had: the doctrine (3-second/3-minute), hard rules,
`chart-grounding` (chart level), `dataviz-polish` (finishing moves),
`design-critique` (G5 /70, G6 /40). What it lacked: a *dashboard-level*
canon with the three tiers, the KPI anatomy as an explicit input, the
cognitive-load budget, uniform scaling across multiples, uncertainty
display, trust/data-quality signals, the semantic-model consistency
devices, the AI-readiness position, the expert disagreements, and a
distance-from-best-in-class audit usable at G7 and for contests.

## Shortlist

| Candidate | Source(s) | Improves | Classification | Impact/effort |
|---|---|---|---|---|
| `dataviz-canon` skill (canon + 20-dimension audit, DC-ids) | all of the above | dashboard-level judgment layer; contest/G7 audit | new core skill (pattern: chart-grounding) | high / medium |
| KPI anatomy fields as required slots | Desbarats, Kaplan & Norton, Van de Voorde | s2 metric contracts complete before build | extension of s2 / metric contract (proposal) | high / low |
| Uniform scaling across small multiples as a hard check | Gemini run, IBCS | integrity of comparisons | extension of dataviz-polish move 6 (already "synced axes") - note only | medium / low |
| Dynamic format strings via calculation groups | SQLBI | consistency for agent-built reports | extension of dax-patterns (proposal) | medium / low |
| SVG-in-DAX performance budget | vendor heuristic + Chris Webb | avoids slow tables | extension of icon-studio/table-studio guides (proposal) | medium / low |
| Performance tooling (Performance Analyzer → DAX Studio) | Microsoft, SQLBI | C2 of the audit | stays **hold** per radar (different skillset); audit asks for evidence only | - |
| AI-readiness (Prep data for AI, Copilot limits) | Microsoft, Buhler, SQLBI | C7 of the audit | assess - fold into tmdl-patterns docstring guidance later | medium / low |

## Decision

2026-11-05: user asked for three layers - standalone skills, this repo,
and the WC27 entry. Implemented in this repo: the `dataviz-canon` skill
(SKILL.md + references/canon.md + references/audit.md), credits and
source-register additions, radar update, routing lines in CLAUDE.md and
design-doctrine. Forge record: `research/log/2026-11-05-forge-dataviz-canon.md`.
The extension proposals (s2 KPI anatomy slots, dax-patterns format
strings, SVG budget) are listed as *assess* on the radar for the user to
pick; not auto-adopted.
