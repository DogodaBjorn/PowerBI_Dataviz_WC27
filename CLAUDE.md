# PowerBI_Dataviz_WC27 — project context (read first)

This repository is a **pbi-atelier project** (not the template): `project/project.yaml`
exists, the lifecycle is at stage 0, and all work serves the Power BI Dataviz World
Champs 2027 Round 1 entry for **Goodnight Inn**. Deadline **November 18, 2026**;
plan to submit November 17.

- Stage-0 source of truth: `project/MISSION-goodnight-inn.md` (kickoff prompt at the
  bottom). Dataset mechanics and the four-brand comparison: `project/SCOUT-pillowkey-round1.md`.
  Three creative directions with scores: `project/PITCH-goodnight-inn-directions.md`
  and the browsable version `project/deliverables/pitch/goodnight-inn-three-ways.html`.
  Pre-filled stage-5 contract draft: `project/creative-direction.draft.yaml`.
- Contest rules as blocker-severity: one brand, exactly two visible pages, ≥ 4 core
  visuals, ≤ $60 M, ≥ 3 initiatives with ≥ 1 growth, impact through 2032, provided
  data only, accessibility scored, **must render under Publish-to-Web** (built-in
  fonts only, embedded images only).
- Every number in the mission and pitch is a hypothesis from an offline decode of the
  starter `.pbix` (`project/analysis/`, reproducible); re-derive in the model before
  it lands in a visual.
- Contest data lives in `project/data/` (gitignored): the starter `.pbix` and the
  blog page. The dataset itself loads from the organisers' public blob via the
  model's `DataFile` parameter.
- Vendored third-party skills sit beside the atelier's own in `.claude/skills/`;
  see `.claude/skills/VENDORED.md` and `CREDITS.md`.

---

# pbi-atelier — operating contract

You are working in **pbi-atelier**, an agent-driven studio for building premium
Power BI reports through a gated lifecycle. This file is a router: deep knowledge
lives in skills, rules, and `design/` — load it when a stage needs it, not before.

## What this repository is

- A **template** (no `project/project.yaml` filled in yet): you may improve the
  framework itself. Run `/project-init` to start a project.
- A **project** (`project/project.yaml` exists): all work serves that project.
  Framework files (`.claude/`, `lifecycle/`, `contracts/`, `design/`, `scripts/`)
  are read-only reference; changes to them belong in the template repo.

## The lifecycle

State lives in `project/project-state/status.yaml` (schema:
`lifecycle/status.schema.yaml`; definitions: `lifecycle/lifecycle.md`).
The daily driver is `/next` — it reads the state, reports gate status, and routes.

| # | Stage | Skill | Primary agent |
|---|---|---|---|
| 0 | Intake | `/s0-intake` | requirements-analyst |
| 1 | Requirements | `/s1-requirements` | requirements-analyst |
| 2 | Metric architecture | `/s2-metrics` | definition-steward |
| 3 | Model design | `/s3-model-design` | model-auditor |
| 4 | Model build | `/s4-model-build` | pbir-operator |
| 5 | Creative direction & design contract | `/s5-design` | report-designer |
| 6 | Report build | `/s6-report-build` | pbir-operator |
| 7 | Validation & delivery | `/s7-deliver` | qa-reviewer |

## Eleven invariants

1. **The durable truth is the repository, not the chat.** Every decision lands in
   `project/project-state/active/`; update `status.yaml` at every gate; never
   advance a stage silently.
2. **Research first.** Never trust memory for TMDL/PBIR schema fields, enum values,
   or theme properties — verify against the file's `$schema` URL or Microsoft Learn
   before writing.
3. **Declare grain first.** No fact table, measure, or relationship before its grain
   is written in the model blueprint.
4. **One metric, one contract.** Every KPI has a filled `contracts/metric.contract.yaml`
   before implementation. Same-name metrics may still be different metrics.
5. **Do not fabricate.** Metrics not derivable from the sources go on the
   "not available" list; scenario logic (targets, composite scores) is labeled as such.
6. **Only `pbir-operator` mutates `project/pbip/`**, in small single-concern diffs,
   validating after every change.
7. **Design is contracted.** Stage 6 builds exactly what the stage-5 design contract
   specifies; deviations go back through the contract, not into the report.
8. **3-second clarity, 3-minute trust.** Every page states one message at a glance
   and withstands scrutiny on drill-down. Never default Power BI styling.
9. **No machine-specific paths, no client-identifiable content** in anything that
   could leave the project repo. Data sources are parameterized.
10. **Guidance persuades, enforcement decides.** Skills and rules shape reasoning;
    hooks, validators, and `settings.json` scopes are the hard floor. Never work
    around a failing hook — fix the cause.
11. **Credit where it is due — no negotiations.** Every adopted idea carries a
    named credit in the implementing file and in `CREDITS.md`; removing an
    attribution is a blocker-severity defect (rule: `attribution.md`).

## Routing beyond the lifecycle

| Need | Go to |
|---|---|
| TMDL / DAX / PBIR conventions | skills `tmdl-patterns`, `dax-patterns`, `pbir-authoring` |
| Visual choice, page layout, polish | `design/` docs + skills `design-critique`, `dataviz-polish`, `chart-grounding` (canon judgment layer for chart choice, scales and chart words) |
| Is this report best in class? (audit, contest prep, KPI anatomy, what the canon says) | skill `dataviz-canon` (dashboard-level canon with DC-ids + the 20-dimension audit) |
| Brand kit → theme | skill `theme-from-brand-kit` (kits in `design/brand-kits/`) |
| Driving the `pbir` CLI / MS plugin | adapter skills `pbir-cli`, `ms-authoring` |
| Full validation sweep | skill `validate-project` |
| Build documentation | skill `build-log` |
| Add-on modules (brand kit, custom visuals, NL, icons, nav, Deneb, tables, tooltips, canvas, a11y, imagery, pixel comps) | `modules/README.md`; module skills are prefixed `bk-`, `cv-`, `nl-`, `ic-`, `nv-`, `dn-`, `tb-`, `tt-`, `ca-`, `ax-`, `im-`, `px-` |
| P2 focus swap (package selector, bookmark states, Deneb/HTML route gates) | skill `fx-focus` + `project/project-state/active/02-focuswissel-methode.md` |
| Screenshot review v2 op de opzet (fixgids met acceptatiechecks, volgorde tot 18 nov) | `project/project-state/active/07-fixgids-review-v2.md` + `research/log/2026-11-07-screenshot-review-v2.md` |
| Keep the toolkit first-in-class (research any subject) | skill `scout` + `research/radar.md` |

## Environment notes

- Windows-first: hooks run under Git Bash; scripts are stdlib-only Python ≥ 3.11.
- External tools are pinned in `DEPENDENCIES.md`. The `pbir` CLI has a
  **non-commercial license** — see that file before paid use; direct JSON editing
  is the documented fallback.
