---
name: dataviz-canon
description: >-
  Dashboard-level canon and the distance-from-best-in-class audit. Use when the
  user asks whether a report, page, design contract or contest entry is best in
  class, championship-grade or "good enough"; when a design argument needs a
  named expert or standard behind it (Few, Tufte, IBCS/ISO 24896, Cleveland &
  McGill, Sweller, Hullman); at G1/G2 for KPI records, at G5 before build, at G7
  as delivery evidence; and whenever someone says the System tier "cannot be
  checked yet because nothing is built".
---

# dataviz-canon

Judgment layer for the *whole report*: what separates basic from best in
class and how far a given report is from it. `chart-grounding` judges the
chart, `dataviz-polish` finishes it, `design-critique` scores directions
(G5, /70) and fidelity (G6, /40); this skill scores distance from best in
class (/40, three tiers) and supplies the canon those judgments stand on.
Canon with ids: `references/canon.md` (cite `DC-nnn`). Rubric and output
format: `references/audit.md`. Read both before scoring; never run the
tiers from memory. Credits: CREDITS.md, "The dashboard canon".

## When invoked for an audit

1. **Name the display type and capability level first** (DC-017, DC-018),
   per page: monitoring / analytical / communication, and descriptive /
   diagnostic / predictive / prescriptive. A page whose type you cannot
   name scores A1 = 0, and that is finding one. Type decides grammar: a
   prescriptive page with scenarios owes the reader uncertainty bands
   (B7); a monitoring page owes a single screen.
2. **Score all three tiers, including System, before anything is built.**
   Tier C is not "the stuff you check after the PBIR exists". Before build
   it is scored on *planned inputs*: storage mode and refresh, how
   measures are documented, whether scenario or metric switching uses
   calculation groups with dynamic format strings (DC-056), the SVG-in-DAX
   and visual budget (DC-053), the custom-visual policy (DC-062), what a
   reviewer opening the .pbix or the model will read. A design that needs
   a 500-row SVG matrix or a Vega visual that drops filter context is a
   design finding now, not a build surprise later.
3. **Walk every headline number through the KPI record** (DC-021): name,
   definition, formula, grain, period, owner, source, reference, direction,
   interpretation rule. Missing slots are A2 findings even when the number
   is correct. Same name on two pages with two base years is an A2 and a
   C3 finding.
4. **Check scales and uncertainty explicitly.** Any set of small
   multiples, sparklines or side-by-side panels: one shared scale or a
   loud statement that scales differ (DC-034). Any forecast, scenario or
   projection: labeled band, stated meaning, no bare point line (DC-020).
5. **Score with evidence** per `references/audit.md`: a page, a visual, a
   measured number, a file path. "Looks fine" is not a score. State which
   tier you could not observe and why, instead of silently omitting it.
6. **Output the audit format** from `references/audit.md`: verdict,
   scored table, must-change list with an owner (stage, skill or person)
   and a verify step per row, accepted gaps. Prose outside that structure
   is the summary, one paragraph, not a second report.

## When invoked for design or explanation

- Quote the canon by id and name (DC-037 Muth: grey is the most important
  color; DC-010 Cleveland & McGill: position beats angle). A rule without
  its source is an opinion the next agent will relitigate.
- Where the canon and a local doc disagree (hard rules, polish, craft
  floor), present both sides and let the user decide; never silently
  override either. Known positions are in `references/canon.md` §6.
- Three tiers, in order, when the user asks "what makes it best in
  class": Meaning (decision, display type, KPI records), Cognition
  (hierarchy, load, encoding, color, words, interaction, uncertainty,
  accessibility), System (model, performance, trust, security, governance,
  lifecycle, AI readiness, adoption). Basic reports fail the first and the
  third and try to compensate in the second.

## Contest and showpiece entries

Map the judging criteria onto the tiers before scoring (template in
`references/audit.md`): insightfulness → A1 to A4 + B7; visual
effectiveness → B1 to B6; creativity → the signature moment constrained by
B2 to B4; accessibility → B8; analytical quality → A2, C1, C3 (judges open
the file and read measure names, descriptions and formats). Score hardest
where the judges score; say which dimensions they cannot see.

## Rationalizations this skill exists to refuse

| Said | Reality |
|---|---|
| "There is no PBIR or theme yet, nothing to run" | Tier C is scored on planned inputs before build (step 2). The decision to switch scenarios without format strings, or to draw a 50-row SVG board, is already made in the comp. |
| "The pitch is approved, the design is settled" | Approval is a decision, not evidence. The audit scores the artefact; the user decides what to do with the score. |
| "Design-intelligence and the brand-kit interview would not change any finding" | They do not; the KPI record, the shared-scale check and the uncertainty rule do, and those are this skill's steps 3 and 4, not stage-5 procedure. |
| "No time for the full table, give me the top five" | The table is the deliverable and takes the same time to score; cut the prose, not the dimensions. The top five come out of the table. |
| "Judges only see pages, skip Tier A" | A1 to A4 are what judges call insightfulness and analytical quality. |
| "We will fix accessibility at the end" | B8 = 0 caps the verdict at good; it is a design input. |

## Record

Audit results go to the stage file (`project/project-state/active/NN-*.md`)
as gate evidence, with the score table and the must-change list; findings
that will be fixed become `review-finding` contracts or fix-queue lines
exactly as `design-critique` does. Never leave the score only in the chat.
