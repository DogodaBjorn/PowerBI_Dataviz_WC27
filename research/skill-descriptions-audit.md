# Skill descriptions audit — trigger-only rule

Date: 2026-08-04 · Auditor: skill-forge first audit (read-only) · Scope:
all 37 skills under `.claude/skills/` · **No skill files were edited** —
every rewrite below is a suggestion awaiting the user's review.

## Rule and scoring

Per skill-forge, a frontmatter `description` states WHEN the skill fires
(symptoms, stage/gate, phrasings a router would match) and never
summarizes what the skill does or how. A workflow summary in the
description is a shortcut agents follow instead of reading the body.

Verdicts:

- **ok** — trigger clause present; any "what" content is a keyword bag
  (router-matchable nouns), not actionable process. Low shortcut risk.
- **weak** — trigger clause present, but the description carries content
  or process detail an agent could act on without opening the body.
- **workflow-summary** — the description narrates steps, mechanics, or
  rules in order; it functions as a miniature (and lossy) skill.

House-style note: nearly every skill uses the hybrid "What it is - detail
list. Use when ..." shape. The trailing trigger clauses are mostly good;
the risk sits in the leading half. Keyword-bag lists (nv-navigation,
tb-tables) are harmless and aid routing; ordered pipelines and scoring
mechanics (px-prototype, design-critique) are the dangerous kind.

## Findings

| Skill | Verdict | Note |
|---|---|---|
| ax-audit | weak | Check-list of audit components could be executed from the description; trigger clause ("gates 6-7, accessibility in question") is good. |
| bk-brand-kit | weak | Narrates the process (interview → validate → write brand.yaml); triggers good, incl. the no-house-style case. |
| build-log | weak | Lists the file's required sections; strong trigger incl. anti-trigger "never retroactively from memory". |
| ca-canvas | weak | Slot maps / furniture-only rules are body content; trigger clause broad but serviceable. |
| copy-polish | ok | Short "what", strong triggers (gate G6, s6 invocation, "check wording"). |
| cv-custom-visual | workflow-summary | Four-step pipeline named in order (justification gate → scaffold → develop → package). Rewrite below. |
| dataviz-polish | workflow-summary | Names five of the ten moves — an agent may apply the named ones and skip the rest. Rewrite below. |
| dax-patterns | ok | Reference skill; topic list doubles as router keywords; clear trigger. |
| design-critique | workflow-summary | Scoring mechanics leak in (0-10, seven passes, /40 health score) — the exact trap: agents may score from the description. Worst offender. Rewrite below. |
| dn-deneb | workflow-summary | Five-step pipeline in order; trigger clause itself is excellent. Same fix pattern as cv-custom-visual. |
| fg-figma | weak | Long; three use cases narrated; the real trigger (Figma MCP connected + design should surface in Figma) arrives last. |
| ic-icons | ok | Keyword bag (icons, pictograms, state chips, accents) + clear trigger. |
| im-imagery | workflow-summary | A body rule ("always 2-3 candidates for user choice") leaked into the description. Rewrite below. |
| ms-authoring | weak | Dense, but triggers are concrete (tools installed, s4 ops, G7 DAX validation, screenshots); acceptable for an adapter. |
| next | weak | Workflow narration up front, but the trigger phrases ("next", "continue", "where are we") are the best in the repo. |
| nl-definities | ok | Dutch terms are router keywords for Dutch requests; clear stage trigger. |
| nl-uat | ok | Same pattern as nl-definities. |
| nv-navigation | ok | Keyword bag of UI forms + clear trigger. |
| pbir-authoring | ok | Reference skill; topics as keywords; precise trigger (report JSON under project/pbip/). |
| pbir-cli | ok | Adapter; trigger precise. |
| project-init | workflow-summary | Four setup steps named — an agent could init (incorrectly) from the description alone. Rewrite below. |
| px-prototype | workflow-summary | The full pipeline verbatim (capture → extract rects → build → verify ±2px). Rewrite below. |
| s0-intake | weak | Stage narration; low risk since /next routes stage skills by name, but the "Produces" clause is the only part that must stay. |
| s1-requirements | weak | Same pattern as s0. |
| s2-metrics | weak | Same pattern; "one contract per KPI" is body content. |
| s3-model-design | weak | Same pattern; grain-first and "do not fabricate" rules belong in the body. |
| s4-model-build | weak | Same pattern; names the operator and diff step. |
| s5-design | workflow-summary | Longest description in the repo; full stage pipeline narrated. Rewrite below. |
| s6-report-build | workflow-summary | Narrates operator duties, craft floor, sweeps, reviews. Rewrite below. |
| s7-deliver | weak | Step list, but each item is close to a keyword; triggers implicit via stage routing. |
| scout | weak | Flow narration ("research → shortlist → fold in"); trigger side thin — "Run any time, on any subject" matches nothing a router can key on beyond the examples. |
| skill-forge | ok | New; trigger-only by construction (this audit's rule). |
| tb-tables | ok | Keyword bag + "any table or matrix work". |
| theme-from-brand-kit | ok | What + three precise triggers. |
| tmdl-patterns | ok | Reference skill; topics as keywords; clear trigger. |
| tt-tooltips | ok | Keyword bag + clear trigger. |
| validate-project | ok | Sweep components read as keywords; "is everything valid" is a perfect router phrase. |

Totals: 17 ok · 12 weak · 8 workflow-summary.

## Suggested rewrites (worst 8)

Suggestions only — trigger-only form, keeping stage identity and the
"Produces" artifact statement where the repo relies on it. The user
approves before any edit; per skill-forge, each rewrite should then be
verified with a trigger check (does it still fire on the phrasings the
old description caught?).

**design-critique**

> Use inside stage 5 when the three creative directions are ready for
> critique or a winner must be converged on, at the stage 6 gate after
> the build, or whenever the user asks for a design critique, review, or
> scoring of directions or a built report.

**px-prototype**

> Use when a stage-5 creative direction has been approved as an HTML comp
> and stage 6 must reproduce it exactly, or when the user mentions
> pixel-perfect fidelity, reference screenshots, comp measurements, or
> measured layouts (px-prototype module).

**s5-design**

> Lifecycle stage 5 - creative direction and design contract. Use when
> the state machine stands at stage 5, /next routes here, or design
> directions, page-purpose contracts, or the design handoff need
> producing or revising. Produces 05-design.md, page-purpose contracts,
> and the handoff quartet in deliverables/.

**s6-report-build**

> Lifecycle stage 6 - report build. Use when the state machine stands at
> stage 6, /next routes here, or report pages must be built or corrected
> from the approved design handoff. Produces the report under
> project/pbip/ and 06-build.md.

**dataviz-polish**

> Use during stage 5 design specification and stage 6 build, when the
> user asks to polish, level up, or premium-ize a report, or when
> preparing a contest or executive showpiece submission.

**project-init**

> Use when starting a new project from this template, when the user asks
> to instantiate or initialize a project, or when project/project.yaml or
> the state machine is missing or broken and needs repair.

**im-imagery**

> Use when a design direction calls for cover heroes, section dividers,
> empty-state art, or subtle background textures, or when the user asks
> for illustrative imagery or on-brand artwork for report chrome
> (imagery-studio module).

**cv-custom-visual**

> Use when a contracted analytical intent cannot be served by native
> visuals, theming, polish, or a Deneb spec, and a pbiviz TypeScript
> custom visual is under consideration (custom-visual-studio module).

## Not rewritten but flagged

- **dn-deneb** — same ordered-pipeline pattern as cv-custom-visual; its
  trigger clause is already the strongest part and can stand alone.
- **scout** — needs *more* trigger, not less: add phrasings like
  "research", "what's new in Power BI", "should we adopt", "keep the
  toolkit current".
- **s0-s4, s7** — acceptable while /next is the only router into stage
  skills; if stage skills ever need to self-trigger from user phrasing,
  apply the s5/s6 rewrite pattern across the set.
