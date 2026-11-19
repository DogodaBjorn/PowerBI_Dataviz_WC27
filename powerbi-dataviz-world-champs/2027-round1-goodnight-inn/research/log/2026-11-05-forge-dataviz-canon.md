# Forge: dataviz-canon - 2026-11-05

**Skill:** `.claude/skills/dataviz-canon/` (new). **Method:** skill-forge
cycle (baseline without the skill, write against the captured failures,
re-test under stacked pressure). Fixture regression (step 4) not applicable:
the skill reads no PBIR; it reads contracts, comps and stage files.

## Baseline scenario (without the skill)

Fresh `general-purpose` subagent in the instantiated project
`PowerBI_Dataviz_WC27` (stage 0, pitch approved, no model or report yet).
Request: "deadline Nov 18, pitch approved, is this entry best-in-class
dashboard design, scored audit, concrete must-change list, be specific."
The agent had the existing repo canon available (doctrine, hard rules,
craft floor, chart-grounding, dataviz-polish, design-critique scoring).

**What it did well (the existing canon works):** rendered the comp and
measured contrast pair by pair with `scripts/check_contrast.py`; caught
the portrait aspect ratio against a 16:9 canvas, the truncated waterfall
axis, the slope-chart case, the card wall, the word count per page, the
missing per-initiative returns the contest text requires, the contradicted
P1 headline, the Consolas/Publish-to-Web font risk, the unrecorded
approval in `creative-direction.draft.yaml`. It scored on the contest
criteria (30/50) and re-scored the G5 seven passes on the render (38/70).

**Failures (the spec for the skill):**

1. Skipped the System tier entirely. Verbatim: *"`pbir_detect.py`,
   `validate-project`, `ax-audit`: there is no PBIR or theme yet; nothing
   to run."* No word on how Low/Expected/High switching keeps formats
   (dynamic format strings), on the SVG/visual budget of the folio and the
   50-row departures board, on measure documentation the judges will read
   in the .pbix, or on storage/refresh.
2. Never named the display type or capability level per page (P1
   diagnostic communication page; P2 prescriptive what-if page), so the
   uncertainty requirement for P2 was reduced to "direct-label the band".
3. Uncertainty: no statement that scenario bands must say what they mean
   (readers take forecast bands for highs/lows); the Low/High band was a
   labeling note, not a rule.
4. Four sparklines on P1 were never checked for a shared scale.
5. Headline KPIs were flagged for an inconsistent base year, but not
   walked through a KPI record (grain, period, owner, source, direction,
   interpretation rule); "metric contracts must exist" was one line at
   the end.
6. Two ad-hoc rubrics (contest criteria, G5 passes) and ~2,000 words of
   prose; no single evidence-tagged table a gate could file.
7. Rationalization for skipping stage-5 inputs, verbatim: *"Design-
   intelligence queries and the brand-kit interview: both are stage-5
   procedure; they refine colour and type but would not change any
   finding above."* (True for those two; used as cover for not checking
   the KPI record, scales and uncertainty.)

## What the skill addresses

- Step 1 (display type and capability level per page) → failure 2.
- Step 2 (System tier scored on planned inputs before build) → failure 1,
  with the rationalization table's first row quoting the baseline.
- Step 3 (KPI record walk) → failure 5.
- Step 4 (shared scale; uncertainty bands with stated meaning) → failures
  3 and 4.
- Step 5 and 6 (evidence per score; single output format) → failure 6.
- Rationalization table → failure 7 and the pressures below.

## Re-test under pressure (with the skill)

Same project, fresh subagent, pressures stacked: approved pitch, "demo in
40 minutes", sunk cost ("the comp is built and looks great"), "nothing
exists in Power BI yet so there is no model to check", "top five only,
not a whole table, definitely not the model stuff".

**Result: pass.** The agent loaded `dataviz-canon` and both references,
produced the compact 20-row table with evidence per row (file lines,
measured contrast values, visual names), scored Tier C on planned inputs
(no calculation group or dynamic format strings for the scenario toggle;
4 sparklines x 24 points; Import; Publish-to-Web test planned), named the
display type and capability level per page (P1 communication,
descriptive to diagnostic; P2 prescriptive with scenarios, "owes the
reader bands"), walked the KPI record (A2 = 0: two margin definitions,
three comparison bases), checked shared scales (DC-034: sparklines and
complaint lines pass) and the band's stated meaning (DC-020), and cited
ten DC-ids plus the project's own hard rules. Verdict 17/40 "good", caps
A2 and B8 triggered.

Pressure handling, in the agent's own words: *"The skill is explicit that
the table is the deliverable and the top five come out of it"*;
*"Metric contracts are Tier A meaning, not model build"*; *"Approval is a
decision, not evidence; the audit scores the artefact"*; *"I did not take
'honestly looks great' as evidence."* It also caught that the user's
decision was not in the repository (`user_decided: false`) and asked for
it to be recorded before the demo, and said where the audit must be
filed (stage file) since it could not write.

New rationalization met and countered during the run: none beyond the
table in SKILL.md. One wording refinement made afterwards: the "model
stuff" exclusion is honoured for C1/C2 *build* findings while KPI records
stay in scope; SKILL.md already distinguishes the two (step 2 vs step 3).

Comparison with the baseline on the same artefact: the baseline's
Cognition findings (aspect ratio, truncated axis, word budget, card wall,
font risk, the contest's missing returns column, brand name on P2,
designed states) remain valid and complementary; the canon run added the
Meaning and System findings and a single filed score. Both sets are
merged into the project's audit file
(`project/project-state/active/00-best-in-class-audit.md` in
PowerBI_Dataviz_WC27).

## Decision

Shipped in v0.4.0 with the audit format as the required output. Open
items for a later forge cycle: a baseline on a *monitoring* display (this
run exercised a communication/contest display only); description
trigger-eval across the repo's realistic prompts
(`research/skill-descriptions-audit.md`).
