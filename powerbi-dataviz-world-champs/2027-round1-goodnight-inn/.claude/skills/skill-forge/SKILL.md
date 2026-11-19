---
name: skill-forge
description: Use when creating a new skill, editing an existing SKILL.md or its frontmatter description, folding a scout adoption into a skill, or auditing skill descriptions - before any skill text is written or changed.
---

# skill-forge

Skill authoring is TDD applied to process prose: no new skill, and no edit
to an existing one, without a witnessed failure first. If nobody watched an
agent fail without the skill, nobody knows the skill teaches the right
thing. (Discipline adapted from Jesse Vincent's superpowers
`writing-skills`, MIT; description-trigger evaluation owes Anthropic's
`skill-creator`, Apache-2.0 — see CREDITS.md.)

## The forge cycle

1. **Baseline — watch it fail.** Before writing a word, run the target
   scenario in a fresh subagent WITHOUT the skill: a realistic repo task
   with real files and a real gate, never a "what would you do" quiz.
   Capture the agent's failures and its rationalizations **verbatim** —
   the exact sentences ("I already validated it mentally", "the deadline
   justifies skipping the sweep") are the spec the skill must defeat.
   No baseline failure → nothing to fix → do not write the skill.
2. **Write against the failures.** Address the captured failures only; no
   guidance for hypothetical ones. Match the form to the failure type:
   rule skipped under pressure → prohibition + rationalization table;
   right rule but wrong-shaped output → positive recipe stating what the
   output IS; omitted element → required slot in the template; behavior
   that depends on a condition → rule keyed to an observable predicate.
   Detail in `references/forge-protocol.md`.
3. **Re-test under pressure.** Same scenario WITH the skill, pressures
   stacked (3+): deadline framing ("the demo is in 40 minutes"), the
   client in the room watching the screen, sunk cost ("the page is
   already built and looks fine"). The agent must comply *and cite the
   skill*. Each new rationalization gets an explicit counter; re-test
   until none appear.
4. **Regression-test against the fixture.** The standing PBIR fixture is
   `E:\PowerBI Set-up\hp-world-champs\project\pbip\second-build.Report`.
   Any skill that reads, shapes, or validates PBIR gets its procedure
   walked against this fixture, read-only — copy to the scratchpad first
   if a test must mutate. A skill edit that breaks on the fixture does
   not ship.
5. **Record.** Baseline transcript, rationalization list, and passing
   runs go to `research/log/<YYYY-MM-DD>-forge-<skill>.md` — the same
   durability bar as a scout entry: a future forge run can skip
   re-testing what is already on record.

## Description = triggers only

The frontmatter `description` states WHEN the skill fires — symptoms,
stage or gate, the phrasings a user would actually type — and never what
the skill does or how. A workflow summary in the description becomes a
shortcut: agents follow the summary and skip the body, so the body's
rules silently stop binding. Third person; router-matchable keywords;
comfortably under 500 characters. The cover test: hide everything below
the frontmatter — a router must still know exactly when to load the
skill, and learn nothing about how it works.

## Scout fold-ins

/scout step 6 (Decide & implement) implements adoptions "per repo
conventions: module pattern (manifest + README + guide + gated skill), or
targeted edits to the owning module/skill/doc". Whenever that step
creates or edits a SKILL.md, it invokes this skill: baseline first, then
write, then pressure- and fixture-test. An adoption whose skill was never
baseline-tested is incomplete, exactly like an adoption without its
credits.

## Rationalizations already met

| Excuse | Reality |
|---|---|
| "The change is a one-liner" | One-liners redirect agents too. Baseline it. |
| "It's obviously clear" | Clear to the author ≠ binding on a fresh agent. |
| "I'll test after shipping" | Then live client projects are the test bed. |
| "No time before the client call" | An untested skill taxes every later session. |

## Maintenance

Re-audit all frontmatter descriptions when routing misfires or on
request: score each against the trigger-only rule and write findings to
`research/skill-descriptions-audit.md` — suggestions only; the user
approves every rewrite before any skill is edited.
