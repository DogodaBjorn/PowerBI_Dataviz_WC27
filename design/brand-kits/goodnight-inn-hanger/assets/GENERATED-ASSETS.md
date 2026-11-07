# Generated brand assets (imagery-studio)

Assets in this folder that were generated, not drawn by hand. Each entry records its source and date
(08-verbeterplan-ronde-3.md V5: a generated asset is a recorded step, embedded by the generator, never pasted in Desktop).

| File | What | Source | Date | Used in |
|---|---|---|---|---|
| `goodnight-inn-door-asleep@2x.png` | The hotel door at night, closed, the hanger asleep on the handle ("Do not disturb") | Google Gemini image generation, model `gemini-3.1-flash-image`, via `scripts/imagery/render_image.mjs`; spec `project/deliverables/imagery/_specs/masthead_p1_asleep.json`, candidate c2 of 3 (raw file `project/deliverables/imagery/im_masthead_p1-brand-review.png`); style anchors: the kit's own hanger and lockup PNGs | 2026-11-07 | P1 masthead vignette, 160 x 160 px |
| `goodnight-inn-door-awake@2x.png` | The same door in the morning, open, light on the floor, towels ready, the hanger awake ("Please make up the room") | Same model and renderer; spec `masthead_p2_awake.json`, candidate c1 of 3 (raw `im_masthead_p2-investment-strategy.png`) | 2026-11-07 | P2 masthead vignette, 160 x 160 px |

Post-processing (both): cropped square around the hanger (P1: door edge, hanger and wall lamp; P2: open door, hanger and towel trolley), resized to 320 x 320
(2x of the slot) and given 12 px rounded corners with a transparent outside, in Python/PIL. Contact sheet of all six
candidates: `project/deliverables/imagery/_contact_sheet.png`; the rejected candidates stay in `candidates/`.

Why these two: the only pair with the same door in both states (closed and asleep on P1, open and awake on P2), so the
two pages read as one story, the brand's "from asleep to awake" (brand-guide.md section 2). Both have one raspberry
element only (the hanger), no text, no moon or stars, as the imagery profile requires. The hanger's slit is simplified
by the model; the mark itself stays the vector logo in the lockup next to it.

Rights: generated for this entry from the kit's own original marks; no third-party images, people or brands in the prompt.
The contest asks for original work and our own images (`project/contest/official-rules-digest.md` §6), and the starter
file explicitly allows AI-assisted design tools.
