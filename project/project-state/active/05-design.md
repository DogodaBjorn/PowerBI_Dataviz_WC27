# 05 — Creative direction (stage 5, in progress 2026-08-04)

Report narrative, three page-purpose contracts (`active/pages/`), and three
divergent directions (`active/creative-direction.contract.yaml`) drafted by
report-designer per the design-critique process. Three 1280×720 HTML comps in
`project/design-prototypes/` — the single approval point. Entrant pick PENDING.

## The report in one sentence

A judge lands on a page that states the Key Takeaway — *"The data is not
wrong — the reading is"* — proves it three times (financials, ratings,
popularity), then earns trust with an over-time evidence page and a method
page where every exclusion, parameter, and refusal is on canvas.

## Page plan (3 pages, express scope)

| # | Page | Archetype | 3-second message |
|---|---|---|---|
| 1 | The Three Lies (landing, Key Takeaway mandated) | overview | Three seductive lies, struck through, each answered by an honest number that states what it excludes |
| 2 | Evidence Over Time | drivers | 30.6% of listings have no date; credible evidence exists only in recent decades (entrant's over-time seed) |
| 3 | Method & Refusals | definitions | Every number states its scope: reconciliation, glossary with TRAP/HONEST/OPAQUE badges, parameters, refusals |

Deliberately left out (do not re-add): per-lie deep-dive pages, genre/keyword/
company slicers, essential tooltip content, decomposition trees, Popularity
aggregation, claims about the ~930k full catalogue.

## The three directions (detail in the contract; comps are the approval surface)

| | D1 Projection Room | D2 Working Papers | D3 Front Page / Corrections |
|---|---|---|---|
| Metaphor | dark screening room, house lights on the truth | auditor's file, red pencil + signed opinion | tabloid that retracts itself |
| Dials | balanced · strict | airy · strict | compact · expressive |
| Signature | 100-seat house, 13 seats lit | cross-foot strip on every page | struck 44pt headline + yellow-barred correction |
| Critique /70 | 52 | 54 | 49 |
| Named risk | Deneb dependency; crowded dark-cinema lane | Creativity ceiling (quiet) | lie typeset larger than truth; 10pt floor pressure |

## Judge intelligence (entrant-supplied sources, 2026-08-04)

Sources (community pages 403 for agents; retrieved via web search):
[Round 1 winners](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Dataviz-World-Champs-Barcelona-Round-1-Winners/ba-p/5284184),
[Round 2 winners](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Dataviz-World-Champs-Barcelona-Round-2-Winners/ba-p/5332826),
[How contests are judged](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/How-are-Fabric-Community-Dataviz-Contests-Judged/ba-p/4781653),
[Alt-text logic post](http://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Accessibility-in-Action-Building-Reusable-Alternative-Text-Logic/bc-p/5296822#M8292),
plus three gallery entries (Round 1 ×2, Round 2 ×1).

Verified findings and their design consequences:

1. **Accessibility eligibility gate: entries below a 50% accessibility score
   cannot win or be judge's favorite.** A dedicated accessibility judge
   manually tests tab order, alt text, and color contrast. → ax-audit at s6/s7
   is existential, not polish (mission already treats it so); tab order and
   alt text are contracted per direction; add **dynamic alt-text measures**
   (Alt · <visual> family, 06 Display) at s6 so alt text carries live numbers.
   The entrant-linked alt-text post covers exactly this technique — **author
   name unretrievable through the 403 wall; if the technique is adopted at s6,
   retrieve the author in-browser and credit in source-register + CREDITS.md
   BEFORE implementation (attribution rule 5).**
2. **Round 1 winner (Gus Bavia) was praised for:** polish, thoughtful
   interactivity, clever bookmarks, beautiful color and layout consistency,
   "educational and incredibly usable" — unanimous judges. → our directions
   are deliberately static; one on-theme interaction is on the table at pick
   time (below). Layout/color consistency locks already bind (hard rules 7–9).
3. **Customization baseline:** default-looking reports are not shortlisted.
   → already doctrine (invariant 8).
4. **General bar:** "help people see something they didn't know" — beauty
   alone insufficient; analysis + design + memorable story. → the 87% /
   zero-votes / unpublished-formula trio is exactly this; keep numbers the
   heroes, chrome subordinate.
5. Round 2 winner specifics not retrievable by agent (403 + search-thin);
   titles suggest a story-led single-insight entry ("What makes LEGO stand
   [out]"). Entrant saw these pages in-browser — their read trumps this note.

**Option for the pick (from finding 2): one "thoughtful interaction".**
A single bookmark toggle on the landing page — **"Read naively / Read
responsibly"** — that swaps the three trap exhibits between full-color
seduction and struck-through correction. On-theme (the report performs its
own retraction), memorable, and exactly the "clever bookmarks" judges
rewarded. Cost: ~half a day at s6 + doubles the fidelity surface of p1.
Decision belongs to the entrant with the direction pick; default if
unaddressed: NOT included (deadline safety).

## Comp build record (2026-08-04 — three comps, one approval point)

All three comps verified free of non-PBIR-reproducible ingredients (no
gradients/blur/animation/shadows/blend/external refs). Comp-author
resolutions on record (measured rects at extraction are truth):
- **D1:** takeaway block runs ~10px past nominal height (no collision);
  redacted hero values set in Consolas; slope permutation fixed with two
  6-step divergences in gold; footer meta/pill duplication resolved.
- **D2:** hero quote 12pt (14pt cannot fit the 80px region); footer recon
  wraps to two lines (copy kept over "single line"); **spec contrast bug
  fixed by the comp author**: gray-segment inside label #78716C→#57534E
  (3.65:1 → passing) — carry into the handoff tokens.
- **D3:** one 4px strike per headline line; dumbbell dots honor the 0–10
  scale; "✕ WITHDRAWN" tag added so trap red never travels without ✕ + word.

## Unresolved decisions (block G5 until answered or defaulted at pick time)

| # | Decision | Default if unaddressed |
|---|---|---|
| 1 | Coverage headline basis: 13.1% (all listings) vs 13.2% (non-adult basis under the locked filter) | 13.2% everywhere (filter-true), comps re-annotated at handoff |
| 2 | Adult filter visible AND locked in view mode? | Locked (static copy stays true) |
| 3 | D1 only: Deneb approved (seat map + rank slope)? | Native fallbacks, signature demoted |
| 4 | D1 only: dim/lit two-card-state exception to lock 9? | Granted as a documented brief exception |
| 5 | Lie 1 headline sign variant (naive profit not yet computed) | Headline copy finalized at s6 from the computed sign |
| 6 | p2 axis window 1900–2030 with out-of-window counts disclosed | Accepted (full 1800–2099 axis is a slop finding) |
| 7 | Type-scale exceptions (D1 40pt numerals / D3 44pt headline) | Granted as documented brief exceptions |
| 8 | D3 only: Lie 2 as dumbbell (drops the scatter) | Acknowledged as D3's contracted trade-off |
| 9 | ~~"Read naively / Read responsibly" bookmark toggle~~ | DECIDED 2026-08-04: **YES** — entrant wants it "with animations"; contracted as native bookmark transition tweening only (no custom animation exists in PBI); two designed p1 states, responsible state default; both states in the asset-fidelity inventory |

`{PLACEHOLDER-AT-BUILD}` batch (not decisions — contracted s6 tasks, filled
from profiling, never memory): naive profit + sign, median/mean credible
profit, top-10 popularity film names, The Godfather weighted score, p2
out-of-window counts, dateless-bucket coverage.

## ROUND 2 (2026-08-04) — after full round-1 rejection

Entrant rejected D1–D3, verbatim: "I don't like either three.. they don't
look and feel movie related to be fair" — logged to taste memory (3 keys) and
applied as Prior Learning: cinema must be carried by ARTIFACT FORM, not
palette; every round-2 direction passes a grayscale test. Toggle DECIDED yes
("with animations") → contracted as native bookmark transition tween only;
p1 has two designed states, responsible = default; naive state carries M-003
equivalent marking (state banner + persistent naive tag). No Deneb this round.

| | D4 One-Sheet | D5 Contact Sheet | D6 Main Titles |
|---|---|---|---|
| Artifact | theatrical quad poster (billing block, rating plate, star-quotes) | sprocketed film strip + grease-pencil pass on a light table | title-sequence credits + end-credits method roll |
| Toggle skin | rating plate R / N | EDITOR'S PASS / AS SHOT | THE PICTURE / THE TRAILER |
| Dials | balanced · expressive | balanced · expressive | airy · strict |
| Critique /70 | 55 | 56 | 52 |
| Named risk | AI key-art slot could cheapen the sheet; 320px chrome column | small-text compression in dark frames/prints vs the manual a11y judge; 1 SVG chrome asset | landing insight density — analysis one click away |

New decisions (delta; full detail in the designer's round-2 spec):
- Naive-state M-003 equivalent marking (banner + tag, no strike) — needs ack.
- Toggle dim mechanism = paired bright/dim element variants (element count
  roughly doubles in affected zones) — build-cost ack.
- D4: im-imagery key-art route (duotone, no text, 2–3 candidates, entrant
  picks; typographic fallback in comp) + 320px chrome column ack.
- D5: sprocket chrome as one ca-canvas SVG per page (shape-built fallback).
- D6: Lie-2 scatter→dumbbell acknowledged deviation from p1 contract.
- Carried from round 1: coverage basis, sign-variant headline, axis window,
  locked filter, type-scale exceptions (36pt), placeholder batch (+ Godfather
  weighted score). Removed: all Deneb rows, ex-D1 card-state exception.
- px-prototype note: each p1 comp holds BOTH toggle states as two stacked
  1280×720 artboards — still three comps, one approval point.

## Open questions

- The entrant's direction pick (D4 / D5 / D6) + acks/answers on the round-2
  decisions delta above. Recorded to `chosen` / `chosen_because` in the
  creative-direction contract and to taste memory (learnings.py) on decision.

## After the pick (contracted next steps)

px-prototype: reference screenshots + rect extraction from the winning comp →
`layout.json` + `reference_screenshots/`. Then the handoff quartet
(design-handoff.md with asset-fidelity inventory, data-model.md, measures.dax,
theme.json via theme-from-brand-kit — bespoke mini-kit from the winner per
mission Day 2), fidelity checklist, G5 close.
