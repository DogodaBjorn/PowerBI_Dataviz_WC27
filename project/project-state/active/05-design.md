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

## Round-2 comp build record (2026-08-04 — three comps, both toggle states each)

All three verified free of non-reproducible ingredients. Author resolutions:
- **D4:** two-line SVG title at 36pt; billing block as condensed SVG text
  (authentic squish) with stacked nav buttons; **a11y flag for s6: cream
  inside-bar label on #78716C measures ~4.2:1 (< 4.5 floor) — move label
  outside the bar or re-ink at build (D5's comp already exteriorized its
  equivalent label); naive-state dimming intentionally sub-floor** (paired
  full-contrast counterpart state — same rationale as D6).
- **D5:** frame values 20pt treated as the one sanctioned scale exception
  (spec-internal contradiction resolved; log in handoff if D5 wins); 13.1%
  label exteriorized above the bar; grease marks as imperfect two-arc
  ellipses / overshooting X-es with per-frame variation.
- **D6:** aligned 8-dot leader columns across bands; footer centered in the
  space left of the buttons; trailer-state dimming to #6B6558 (~3.2:1)
  documented as de-emphasis with full-contrast counterpart; rank-strip ✓/✕
  kept monochrome per that visual's own "never colored" contract.

## ROUND 3 (2026-08-04) — the entrant authored the concept

D4–D6 rejected ("Still not sold on any"). The entrant supplied the direction
(verbatim, binding brief — taste key trilogy-concept-entrant):

> "What if we make the concept all around it being a movie on itself. A
> trilogy even.. The Seductive Lies I II and III. Each telling the story of
> how Data used irresponsibly leads to a wrong conclusion about the best
> movie.. rated on profitability in movie I, on viewer ratings on II and
> then in the end everything is working out well because movie III makes
> the necessary adjustments and shows the viewer the weighted best selling
> and rated movie on a good scatter plot animation. [...] something like a
> movie posters front page or three movie tickets and then clicking on
> either of three, ripping off the entrance bit and then entering the
> screenplay page where the plain naive conclusion is shown, the critique
> is appearing and the new conclusion is drawn."

Plus hard requirements: mockups must be dynamic/realistic (static artboards
below the bar); Deneb + extended-HTML visuals are a hard wish; movie assets
(posters) in tooltips; "can't be a flat dashboard... remarkable, usable,
accessible and most of all fun to engage with"; final chance at the finals.

Feasibility verified this session:
- Deneb + HTML Content visuals are championship-legitimate (an interactive
  HTML visual was highlighted at the Champs); rule: ≥1 core PBI visual must
  remain. Sources in the s5 research trail.
- Movies[Poster Path] carries real TMDB paths (seen at Q2 profiling) —
  poster imagery is DATA, not decoration; base-URL mechanics verified at
  build (research-first).
- "Scatter plot animation" has a native mechanism: scatter-chart PLAY AXIS
  over Release Year — real animation, core visual, and the home of the
  entrant's over-time seed.
- Story restructure: Acts I (profit lie) + II (ratings lie) + III "The
  Corrected Cut" (resolution; M-007 popularity folded in as a refusal beat)
  — metric contracts unchanged, staging only. Key Takeaway stays on cover.

D7 ("The Seductive Lies: A Trilogy") convergence commissioned from
report-designer: architecture + replacement page contracts + mechanism map
(every effect names its PBI mechanism: ticket click→page nav, stub tear→CSS
animation in HTML Content w/ pre-torn fallback, beats→bookmarks, scatter→
play axis, posters→Image URL) + interactive-prototype build spec + critique.

## D7 converged design (2026-08-04) — summary

Full spec in the designer's round-3 output; contracts live in
`active/pages/` (5 pages + tt-movie-poster tooltip) and the D7 block in the
creative-direction contract. Critique: **52/70**, honest lows on state
coverage (6) and accessibility-of-interactivity (6) — the 50% eligibility
gate is winnable but must be BUILT. Ranked risks: (1) scope vs deadline —
ordered cut list contracted (tear→pre-torn; dn_rating_fall→paired bars;
3 beats→2; tooltip posters→table only; credits joke→free); (2) trap-first
SC.1 openings — M-003 equivalent marking non-negotiable; (3) a11y of the
interaction surface — the package is contract, not aspiration.

Architecture: p0 Box Office (night; marquee Key Takeaway; 3 tickets = nav) →
p1/p2 screenplay acts (paper; 3 bookmark beats: SEDUCTION → NOTES →
CORRECTED CUT; shared template) → p3 Premiere (night; native play-axis
scatter over Release Year, credible ∧ votes≥100; refusal beat = M-007;
no-date chip = the over-time seed's disclosure) → p9 End Credits (method as
credits roll; static). Mechanism map: every effect names its PBI mechanism
with fallback (HTML Content tear = VERIFY, pre-torn fallback; 2 Deneb with
native fallbacks; posters = Image URL from Poster Path; ≥1 core visual rule
satisfied by the scatter).

## D7 prototype build record (2026-08-04)

`project/design-prototypes/d7-trilogy.html` (51 KB, self-contained, system
fonts, UTF-8 no BOM). Full five-page flow simulation: tearable tickets
(translate + 8° rotate + fade, 380 ms) → two screenplay acts with cumulative
scene bookmarks → premiere with an 8-keyframe year sweep (opens resolved;
PLAY re-runs) → static credits → floating 320×420 tooltip. Keyboard loop
complete in DOM order, Enter activates every control, Escape dismisses the
tooltip, `prefers-reduced-motion` honored. **14 mechanism chips verified**,
incl. "HTML Content tear — VERIFY; fallback pre-torn stub", both Deneb
fallbacks, and "native scatter play axis (core visual)". Conformance scan
clean: no gradients/blur/shadow/blend/parallax/elastic easing/external refs
(only the SVG namespace string, not a network call).

Builder deviations worth carrying to the handoff:
- **Strike fades in, never "draws"** — a width-draw is outside the honest
  motion vocabulary; a fade is what a bookmark-toggled line shape actually
  does. (Same discipline applied to every effect.)
- **Do-not-fabricate held**: dumbbell rows 3–4 and the tooltip's year/rank
  render as marked placeholders rather than invented film names.
- Waffle mini-tickets 36×14 (grid step 18) — 16 px overflowed the card by
  ~11 px; p3 beat rail defined (SC.1/SC.2 dim the scatter and spotlight the
  adjustments/refusal cards, SC.3 restores the premiere); Act II gained an
  action line + smash-cut slug for screenplay-grammar symmetry; credits
  source/closing lines moved to a centered closing block for roll rhythm.
- Torn stubs reset on return to the Box Office (demo replay); the real
  report's fallback is a static pre-torn stub, already disclosed on the chip.

## Ack table (entrant, at prototype approval — defaults recommended)

| # | Decision | Default |
|---|---|---|
| 1 | 5 pages + tooltip (credits as own page) | yes |
| 2 | Cover = ticket booth, not poster wall (no AI key art) | yes |
| 3 | Acts I/II open on SC.1 (naive, marked); Act III opens on SC.3 | yes |
| 4 | M-007 = Act III refusal beat | yes |
| 5 | Tear = HTML Content VERIFY; pre-torn fallback accepted | yes |
| 6 | Scatter population = credible financials ∧ votes ≥ 100; X = Revenue log | yes |
| 7 | No act tints — single ticket-red accent | yes |
| 8 | Posters only where they carry data (Act II leaderboard + tooltip) | yes |
| 9 | Cut-list order pre-approved (see risks) | yes |
| 10 | Carried: sign-variant headline, placeholder batch, locked Adult filter, coverage basis, credits joke line | — |

## ENTRANT DECISION 2026-08-05 — D7 approved with one change

- **Approved with changes** → the change is per-act tints (below). All other
  ack-table defaults accepted as recommended.
- **Cover = tickets** confirmed (poster wall declined; real TMDB posters stay
  where they carry data — Act II leaderboard + tooltip).
- **Act tints granted** — documented exception to consistency lock 7,
  bounded by a scope rule so hard rule 3 (direction encoding) stays intact:

| Act | Tint | Paper | Night | Ratios | Reading |
|---|---|---|---|---|---|
| I | Ledger Indigo | `#2E4A7D` | `#7FA8DD` | 7.84 / 7.43 | the money act, shot cold |
| II | Awards Brass | `#8A6516` | `#D9A441` | 4.74 / 8.12 | the applause act, shot warm |
| III | Velvet Plum | `#5B3E8E` | `#B79BE8` | 7.43 / 7.71 | the corrected cut, house curtain |

All six variants computed against the WCAG formula 2026-08-05: every one
passes AA for text and non-text. **Scope rule (G6-checkable): the tint
touches chrome only** — act numeral, ticket rule + serial, beat-rail current
fill, header rule, verdict rule. Data never wears the tint: traps stay
trap-red + strike + word, honest stays good-green + ✓ + word, identically on
every page. A tinted data mark is a defect. Hue budget per page stays at 4
families; p9 credits carry no tint.

## G5 CLOSE-OUT (2026-08-05)

**Quartet complete** in `project/deliverables/`: design-handoff.md (68 KB —
149 role-prefixed visual ids with rects read from the prototype, per-beat
bookmark visibility, the M-003 marking as four simultaneous carriers, the
a11y package with enumerated tab orders, verbatim copy, a 56-row
asset-fidelity inventory with **nothing unmapped**, and the 5-step cut
list), data-model.md (blueprint §7 verbatim, byte-identical; 12-row
placeholder batch naming the resolving measure for each), measures.dax
(8 stub replacements + 50 new; colour measures paired with glyph/word
measures), theme.json (validates 0 errors against reportThemeSchema-2.156).

**Measured truth**: `layout.json` (8 screens at exact canvas sizes) +
`reference_screenshots/` @2x — the stage-6 fidelity targets.

**Rendered review before close** (screenshots read, not assumed) caught the
reserved-red inversions now contracted; the quartet compiler independently
found the same three, plus five more fixes (chip overflow, measure
miscount, paper tokens unreachable from a single-background theme → added
as documented chrome-only dataColors zones 7–16).

**Documented comp-vs-build drift** (not a defect — resolved deliberately):
ack #1 defaulted to the filter-true basis, so the build binds 84,036 /
13.2% live via measures while the prototype PNGs still print 85,394 /
13.1%. "87%" survives the rounding either way. 85,394 remains only on the
credits' LISTINGS PER SOURCE row. Fidelity review compares *rects*, not
these strings.

### Two blockers stage 6 must clear BEFORE the relevant work

1. **Attribution (rule 5 — blocker severity).** The dynamic-alt-text
   technique comes from the entrant-supplied community post, whose author
   is unretrievable behind the 403 wall that blocks agents. The author must
   be identified in a browser and added to `contracts/source-register.yaml`
   AND `CREDITS.md` **before** the `Alt ·` measure family is implemented.
   If the name cannot be obtained, the technique is not used.
2. **TMDB image base URL** for `Image · Poster URL` — retrieve from TMDB's
   image-configuration docs at build and log it. If unverifiable, posters
   drop wholesale; the design reads without them.

### Gate G5 checklist

- [x] Every page has a purpose contract with a written 3-second message and 3-minute path (5 contracts + tooltip)
- [x] Design intelligence queried before directions drafted; cited as used/overruled; judge intel folded in
- [x] Directions documented with Design Read + dials; three rounds, honest critique; entrant chose D7 (their own concept) — comps existed at every approval point
- [x] Asset-fidelity inventory complete — 56 rows, nothing unmapped, fallbacks contracted
- [x] Quartet complete and internally consistent (same tokens in brief/theme/handoff; same ids in handoff/measures)
- [x] Fidelity checklist written (creative-direction contract; stage 6 judged against it)

## After the pick (contracted next steps)

px-prototype: reference screenshots + rect extraction from the winning comp →
`layout.json` + `reference_screenshots/`. Then the handoff quartet
(design-handoff.md with asset-fidelity inventory, data-model.md, measures.dax,
theme.json via theme-from-brand-kit — bespoke mini-kit from the winner per
mission Day 2), fidelity checklist, G5 close.
