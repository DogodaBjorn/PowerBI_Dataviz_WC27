---
name: copy-polish
description: Sweep every user-visible string and text deliverable for AI-writing tells, topic-only titles, and register drift. Use when polishing or reviewing report copy, before gate G6 (the s6 fidelity review invokes it), or whenever the user asks to check wording.
---

# copy-polish

Copy is part of the build contract: a report that reads like a chatbot wrote
it loses the trust the visuals earned. This skill sweeps everything a user
reads — in the report and in the text deliverables — for the writing tells
that mark machine-generated copy, and replaces vague labels with specific
claims. The s6 fidelity review runs this sweep before gate G6; it also runs
standalone on request. (Tell list distilled from Wikipedia's "Signs of AI
writing" via Siqi Chen's humanizer skill; specificity rule and sweep
discipline owe Corey Haines' marketing skills — both MIT, see CREDITS.md.)

## What gets swept

**Report strings** (edit via `pbir-cli` / `pbir-authoring`): visual titles
and subtitles, the composed sentences inside insight-title measures,
tooltip text and tooltip pages, textboxes, page display names, button
labels. **Text deliverables:** BUILD_LOG prose, `definities.nl.md`
(nl-definities output), `uat-testplan.nl.md` (nl-uat output).

**Hard guard — copy only, never contracts.** Never rename contracted ids,
measure names, or metric display names; never change a number, a period
convention, or a steward-owned definition (nl-definities content is
translated, never "improved" — that rule outranks this skill). In an
insight-title measure, edit the wording of the composed string, not the
logic or the measure name. If a contracted name itself is bad copy, raise a
review finding for the contract owner instead of editing it.

## Step 1 — voice calibration

If client documents were collected at s0-intake (intake contract sources
and `project_additions`: briefs, existing reports, style guides), read them
first and match their register: formality, the client's own terms for
metrics and business units, English loanwords vs Dutch equivalents,
capitalization habits. The client's register outranks every default below —
if their house style is Title Case, keep Title Case. Without client
documents: plain professional, sentence case; for Dutch projects, zakelijk
maar helder (same register as nl-uat).

## Step 2 — the tell sweep

The AI-writing tells that actually show up in report copy:

1. **Em/en dashes.** The most reliable tell. Replace with comma, colon, or
   a new sentence: "Omzet stijgt — vooral in Noord" → "Omzet stijgt,
   vooral in Noord". (Client register with genuine dash habits overrides.)
2. **Inflated significance.** "A pivotal quarter", "marking a shift",
   "een cruciale rol". A report shows significance with numbers; it never
   asserts it. Cut the ceremony, keep the claim.
3. **AI vocabulary.** delve, landscape, tapestry, robust, seamless,
   showcase, underscore, vibrant. In a title or tooltip these are dead
   weight; name the thing instead.
4. **Rule-of-three padding.** "Trends, drivers, and opportunities" as a
   subtitle when the page shows two things. Lists match what the page
   actually answers, not a rhythm.
5. **Title Case Abuse.** Sentence case for titles, labels, and buttons
   ("Omzet per regio", not "Omzet Per Regio") unless the client's own
   materials say otherwise.
6. **Hedging.** "Could potentially indicate", "zou mogelijk kunnen wijzen
   op". A report states what the measure shows or stays silent; open
   questions belong in the BUILD_LOG, not in a tooltip.
7. **-ing tack-ons.** "...highlighting the importance of data quality"
   glued to a sentence to fake depth. Cut the participle clause; if the
   point matters, give it its own plain sentence.
8. **Filler and send-offs.** "It is important to note that", "in order
   to", and generic upbeat closers ("the future looks bright") in
   BUILD_LOG and UAT prose. End on the last concrete fact.

Judge by clusters: one dash is a typo, dash + "pivotal" + a triad is a
rewrite. Don't flatten legitimate prose that merely sounds formal, and
never edit quoted requester words (the intake quote stays verbatim).

## Step 3 — the specificity rule

"Cut reporting from 4 hours to 15 minutes" beats "Reporting overview".
Every string carries the finding, not the topic:

- Titles: "Omzet +8% vs vorig jaar, gedreven door Noord" beats "Omzet per
  regio". Where the handoff specifies insight titles (dataviz-polish move
  1), the DAX composes this sentence; the sweep checks the composed
  wording reads like one.
- Buttons: name the destination or outcome. "Naar klantdetail" beats
  "Meer info".
- Tooltips: answer the reader's next question; never restate the number
  they are hovering over.
- BUILD_LOG: "Filtered 214 rows with null OrderDate" beats "cleaned the
  data".

If a string cannot be made specific, ask whether it should exist at all.

## The sweep checklist (10 items)

- [ ] No em or en dashes in any user-visible string or deliverable
- [ ] Titles state findings, not topics, wherever the handoff allows
- [ ] Sentence case throughout (unless the client register says otherwise)
- [ ] No AI vocabulary (delve/landscape/tapestry/robust/seamless/pivotal...)
- [ ] No rule-of-three padding; every list item is really on the page
- [ ] No hedging; claims are stated or omitted, open issues in BUILD_LOG
- [ ] Filler cut; deliverable prose ends on facts, not send-offs
- [ ] Every claim specific: number, period, unit, or driver named
- [ ] One name per metric, byte-identical to the contracts, on every page
      and in every deliverable
- [ ] Read-aloud test passes in the target language; Dutch prose uses
      Dutch number and date conventions

## Dutch projects

Most tells transfer directly to Dutch; sweep for the local forms too:

- **cruciaal / essentieel** as reflex intensifiers ("speelt een cruciale
  rol") — the inflated-significance tell.
- **onderstreept / benadrukt het belang van** — the underscores/highlights
  tell; state the fact, drop the framing.
- **duiken in** ("we duiken in de cijfers") — delve; Dutch report prose
  does not dive, it shows.
- **zou mogelijk kunnen** — stacked hedging; one modal at most, and only
  when the uncertainty is real.

The em-dash rule holds unchanged: Dutch business copy uses dashes even
less than English does.

## Done when

All ten checklist items pass on every page and every text deliverable, in
the client's register, with zero contracted names or definitions altered.
Record the sweep and any raised findings in the BUILD_LOG (stage 6) or the
conversation (standalone).
