---
name: design-critique
description: Run the scored divergence-critique-convergence process for report design - produce three genuinely different creative directions, score each 0-10 across seven passes against the design doctrine, and after the build run the dual-isolated fidelity review with the /40 health score and fix queue. Used inside stage 5 and again at the stage 6 gate.
---

# design-critique

Two jobs: force real creative divergence before stage 5 converges, and check
fidelity after stage 6 builds. Scoring method adapted from gstack's rated
review passes (MIT) and impeccable's dual-assessment critique (Apache-2.0) —
see CREDITS.md.

## Divergence (stage 5)

Produce three directions in `creative-direction.contract.yaml`. A direction
is a *stance*, not a palette:

- **Organizing concept** — the metaphor or editorial frame that makes the
  report memorable (a briefing, a control room, a ledger, a field report…).
- **Visual language** — type feel, color temperature, density, and the one
  signature layout move that follows from the concept.
- **Signature moment** — the single element a reader would describe to a
  colleague afterward.
- **Risk** — every direction has one; naming it is part of the work.

Divergence test: if two directions could swap accent colors and be the same
report, they are one direction — replace one. Anchor each in the audience:
a daily operational crew and a quarterly board read differently.

## Critique (stage 5, before the user chooses)

Argue each direction against `design/design-doctrine.md`, scored: rate every
direction 0-10 on the **seven passes** in `references/scoring.md` — read that
file first, don't run the passes from memory. Per pass: the score, one line
on the gap, with the pass's what-a-10 line as the measure. Score honestly —
most comps land 5-7; a 9 needs an argument, not enthusiasm.

1. Reading path (first/second/third read of the page)
2. State coverage (no-data, all-slicers-cleared, longest labels)
3. Slop risk
4. Brand alignment
5. Accessibility
6. Dial fit (declared DENSITY/VARIANCE vs what the comp actually does)
7. Signature-moment strength

Present the 7×3 score table and each direction's biggest gap. Recommend one,
with its risks — but **the user decides**; scores inform the choice, they do
not make it. Record `chosen_because` in the user's words and write the
fidelity checklist — the 3-5 elements that define the direction and must
survive the build.

Close with an **unresolved-decisions table** (`decision needed | if deferred,
what happens` — e.g. "empty-state look? → operator ships a blank canvas").
G5 does not close until the table is empty or the user has acknowledged every
row in writing; acknowledged deferrals go into the handoff as accepted risks.

## Fidelity review (stage 6 gate)

Two assessments, strictly isolated — the designer's eye must not be anchored
by tool output. Run A to completion and write its findings down **before**
collecting or reading any of B.

**Assessment A — design director.** The `report-designer` eye (never
`pbir-operator` reviewing its own build) walks the built PBIR against the
comp/handoff and the fidelity checklist, page by page, with no script output
in context: hero where the contract says? chrome identical across pages?
polish moves present? does each page still carry the direction's signature?

**Assessment B — scripted evidence**, collected separately:

- `python scripts/pbir_detect.py` — taste-lint over the PBIR (if the script
  is absent, record "detector unavailable" in the evidence; never fake it)
- `python scripts/check_contrast.py` against the active theme
- the full `validate-project` sweep
- px-prototype enabled: the ±2px diff of every built `position` against
  `layout.json`, plus the reference-screenshot comparison

**Synthesize** only after both are complete: weave, don't concatenate —
where A and B agree, what B caught that A missed, which B hits are false
positives. Score the ten fidelity dimensions in `references/scoring.md`
0-4 each → **health score /40**, and triage every finding **high** (first
impression, trust, or contract breach) / **medium** (felt subconsciously) /
**polish** (good-to-great). Record the score table and triage in
`06-build.md` as gate evidence.

**Findings out, fixes in.** Every deviation becomes a `review-finding`
contract (dimension: design) — fixed, or accepted by the user in writing;
"close enough" is a finding, not a verdict. Also write the machine queue
`project/project-state/fix-tasks.jsonl`, one JSON object per finding with
`id, priority, page, finding, verify` (schema in `references/scoring.md`).
`pbir-operator` consumes the queue in priority order: one finding = one
single-concern diff, then re-validate (hooks plus the finding's own `verify`
command) before taking the next. When the queue drains, re-score — the gate
reads the trend, not just the number.
