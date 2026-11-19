# Forge protocol — testing skills on agents

Load when running a forge cycle (SKILL.md steps 1-5). Methodology adapted
from Jesse Vincent's superpowers `writing-skills` /
`testing-skills-with-subagents` (MIT) and Anthropic's `skill-creator`
trigger-eval approach (Apache-2.0); re-expressed for this repo.

## Running a baseline (step 1)

- Fresh context, no skill loaded: a subagent via the Task tool, or
  `claude -p` from a clean directory. The agent must believe it is doing
  real work, not answering a quiz.
- Give a realistic repo task: real stage, real gate, real file paths
  (use the standing fixture, below). "You are at gate G6, the fidelity
  review is next, the user wrote: ..." beats "imagine a report".
- Force a decision. Open-ended prompts let the agent hedge; concrete
  options (A/B/C) or a task with a deliverable expose the actual choice.
- Run 3+ times. Single samples lie; patterns across runs are the signal.

## Pressure scenarios (steps 1 and 3)

The pressures that recur in this repo's real sessions:

| Pressure | pbi-atelier framing |
|---|---|
| Time | "Client demo at 15:00, it is 14:20" |
| Client in the room | "The client is watching the shared screen right now" |
| Sunk cost | "The page is already built and looks fine" |
| Authority | "The user said just ship it, skip the sweep" |
| Exhaustion | "Session context is nearly full, wrap up" |
| Social | "Re-running validation looks pedantic in front of the client" |

Combine 3+ pressures in a verify run. A skill that holds under one
pressure and folds under three is not done.

Scenario quality bar: concrete constraints (times, names, paths), an
explicit "act — do not describe what you would do", and no free exit
("I'd ask the user" only counts if asking is a listed option).

## Verbatim capture

Record the exact rationalization sentences, not paraphrases. "Agent
skipped validation" teaches nothing; "Given the deadline, a visual check
is sufficient here" is a counter you can write. Every distinct excuse
across all runs goes into the skill's rationalization table.

## Matching form to failure (step 2)

| Baseline failure | Right form | Wrong form |
|---|---|---|
| Knows the rule, skips it under pressure | Prohibition + rationalization table + red flags | Soft "prefer/consider" wording |
| Complies but output has the wrong shape | Positive recipe: what the output IS, parts in order | Prohibition list |
| Omits an element from output it already produces | REQUIRED slot in the template it fills | Prose reminder near the template |
| Behavior should depend on a condition | Conditional on an observable predicate | Unconditional rule + exemption clauses |

No nuance clauses ("don't X unless it matters" reopens the negotiation)
and no exemption clauses ("doesn't apply to Y" still suppresses Y —
restructure so the rule cannot reach Y instead).

## Closing loopholes (step 3)

For each new rationalization observed WITH the skill loaded, add all of:

1. an explicit negation in the rule ("delete means delete — not 'keep as
   reference', not 'adapt while testing'");
2. a rationalization-table row (excuse verbatim → reality);
3. a red-flag entry the agent can self-match mid-drift;
4. a description symptom, when the excuse marks being *about* to violate.

**Meta-test** when stuck: show the failing agent its own transcript and
ask how the skill should have been written so the right choice was
unambiguous. "The skill was clear, I ignored it" → add a foundational
principle (violating the letter is violating the spirit). "It should
have said X" → add X verbatim. "I didn't see section Y" → reorganize.

## Micro-testing wording

Before full pressure runs, verify a sentence binds at all: fresh-context
single-shot samples with the guidance embedded in its realistic home (the
full SKILL.md, not the sentence alone), a no-guidance control (if the
control does not fail, stop — there is nothing to fix), 5+ reps per
variant, every flagged match read manually, and variance as a metric —
five different interpretations across five reps means the form is wrong,
not the word count.

## Fixture regression (step 4)

Standing PBIR fixture:
`E:\PowerBI Set-up\hp-world-champs\project\pbip\second-build.Report`

- Walk the changed skill's procedure against the fixture end to end:
  every referenced file exists, every command runs, every claim about
  PBIR structure holds on real pages.
- Read-only. If a test must write, copy the fixture to the session
  scratchpad and point the test there. The fixture in place is never
  mutated — it is only useful while it stays representative.
- After the walk, the untouched fixture still passes `validate-project`'s
  sweep — proof the test itself left no residue.

## Description trigger rubric (SKILL.md "Description = triggers only")

Score a description by:

1. **Cover test** — frontmatter alone says when to fire, nothing of how.
2. **Router keywords** — the words a user or router would actually
   produce (stage names, gate ids, artifact names, "polish", "is
   everything valid", Dutch terms for Dutch skills).
3. **Third person, no first/second person.**
4. **No workflow narration** — step lists, scoring mechanics, and
   output inventories belong in the body; in the description they become
   the version agents follow.
5. **Symptom coverage** — include the states that mean the skill is
   *about* to be needed or violated, not only the happy-path request.

To evaluate empirically (adapted from skill-creator's eval loop): give a
fresh agent only the name + description among the repo's other skill
descriptions, feed it repo-realistic prompts that should and should not
fire, and count trigger/no-trigger over 5+ reps each. Fix misses by
generalizing the trigger category, never by appending the failing query.

## When a skill is done

Bulletproof: complies under maximum stacked pressure, cites the skill's
sections, acknowledges the temptation, fixture walk clean, and the forge
log records baseline + passes. Not done: new rationalizations still
appearing, "hybrid approach" proposals, or arguing the skill is wrong —
each of those restarts step 3.
