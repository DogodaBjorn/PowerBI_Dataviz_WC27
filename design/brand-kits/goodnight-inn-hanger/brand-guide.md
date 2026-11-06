# Goodnight Inn, option 2: the door hanger

Companion to `brand.yaml`. Option 1 (`../goodnight-inn/`) was designed by a
dataviz editor: a Board briefing on paper at night. This option is the same
brand read by a dataviz specialist who came from brand marketing. It starts
where a marketer starts, with what the brand promises and who it is for, and
only then picks colors and shapes. Same data, same model, same contest pages;
a different brand in front of them.

Credits for the thinking used here (also in CREDITS.md): Jenni Romaniuk
(distinctive brand assets, category entry points), Byron Sharp (mental
availability), Kevin Lane Keller (customer-based brand equity), Margaret Mark
and Carol S. Pearson (brand archetypes), April Dunford (positioning
components), Theodore Levitt (sell the outcome), Paul Rand and Chermayeff &
Geismar & Haviv (logo principles). Type: Vincent Connare (Trebuchet MS),
Matthew Carter (Verdana), Lexend by Bonnie Shaver-Troup, Thomas Jockin et al.
(OFL-1.1, outlined in the wordmark).

## 1. The marketer's read of the data

Every number below is from the mission's evidence pack, re-derived in the
sketch model (`project/pbip/SKETCHES.md`).

- **The promise is broken.** The brand positioned as "affordable" now has the
  lowest value-for-money score of the four brands (7.66), after raising its
  average rate 14.6 % since 2021 (E19). Price went up, perceived value went
  down: in marketing terms that is the brand promise failing at the moment
  of payment.
- **Someone else owns the guest.** Online travel agencies took 33 % of room
  revenue in 2021 and 50 % in 2025; direct web and app fell from 31 % to
  23 % (E5). Commission is a customer-acquisition cost, and the brand pays
  $18.1M of it a year to meet guests it used to meet itself (E6).
- **The product is tired.** No renovation started since December 2020;
  $0.98M per hotel since 2018 against $5.9M to $7.9M at the sister brands
  (E17). Room comfort tracks renovation age at r = -0.92. NPS fell from +8.5
  to +3.3.
- **Who stays.** Leisure 38 % of room nights, business travel 24 % and
  growing, family 23 %, groups and long stays about 8 % each (E15). The
  places they arrive: airports (82 % occupancy, the fullest), highways,
  cities (E13).

The marketer's conclusion: this is not three operations problems, it is one
brand problem with three symptoms. The plan in the mission already answers
it (buy the guest back, fix the welcome, build where we're full); option 2
makes the report say so in the brand's own voice.

## 2. Brand platform

**Positioning** (Dunford's components):
- *For:* leisure, family and business travellers who need a good night on
  the way to somewhere else.
- *Category:* the budget inn at the airport, the highway exit and the city
  edge.
- *Unique value:* sleep and price you can count on.
- *Proof:* the honest rate, booked with us.

**Promise:** *A good night. A fair price.* Two halves, and the data checks
each one: comfort, cleanliness and NPS check the night; value for money
against the rate checks the price.

**Archetype: the Everyman** (Mark and Pearson). It belongs, it doesn't
pretend, it says things plainly and with a little warmth. It is never luxury
and never cute.

**Sell the outcome** (Levitt): guests don't buy a room, they buy waking up
rested and not feeling overcharged. The brand's visual story runs from
asleep to awake.

**Category entry points** (Romaniuk, Sharp): the moments a traveller thinks
"I need a bed".
- "A room near the airport tonight." The airport hotels are the fullest,
  which is why "build where we're full" is a brand move as well as a
  capacity move.
- "A cheap stop on a long drive." That's the highway hotels.
- "Somewhere simple in town." That's the city hotels.

**Brand health, the Keller way:** read it as a ladder from salience to
resonance.
- *Salience* (do they find us directly?): direct share.
- *Performance* (is the room good?): comfort and cleanliness.
- *Judgment* (is it worth it?): value for money.
- *Resonance* (would they recommend us?): NPS.

The P1 scorecard can be read as this ladder from bottom to top.

## 3. Distinctive assets (the Romaniuk test: unique, famous, ownable)

| Asset | What it is | Why it earns its place |
|---|---|---|
| Color | Raspberry `#B5175F` | The hotel category speaks navy and gold; the design-intelligence layer's own default for "hotel hospitality" is navy plus gold. Raspberry is unused by the category, survives AA as text (5.8:1) and reads as a highlighter, not a warning. |
| Shape | The door hanger | The one object every hotel guest has held. Tall, pillow-soft (radius 12), with the handle hole and slit. |
| Character | The hanger's face | Two closed eyes (sleeping, "do not disturb"), two open eyes (awake, "make up the room"). The face only ever shows a state; it is not a mascot. |
| Phrase | "Do not disturb" / "Please make up the room" | Words every guest already knows. They become the page headlines (section 5). |

## 4. Logo (Rand: simple, works small, works in one color)

| File | Use |
|---|---|
| `assets/goodnight-inn-lockup.svg` / `@2x.png` | Masthead on both pages, 40 px tall at 1920x1080 |
| `assets/goodnight-inn-lockup-reversed.svg` / `@2x.png` | On plum-black surfaces: the "How we calculated this" overlay |
| `assets/goodnight-inn-hanger.svg` / `@2x.png` | The mark, asleep: P1 masthead state, gallery thumbnail, not-funded chips |
| `assets/goodnight-inn-hanger-awake.svg` / `@2x.png` | The mark, awake: P2 masthead state, funded chips |
| `assets/goodnight-inn-hanger-mono.svg` / `@2x.png` | One-color uses and print |
| `assets/goodnight-inn-hanger-awake-on-accent.svg` / `@2x.png` | White awake hanger for raspberry surfaces: the funded chip |

Construction: a 56 x 96 rounded tile (radius 14) with a 10-unit handle hole
and a slit to the right edge, cut by a mask so the background shows through.
The wordmark is lowercase *goodnight inn* in Lexend SemiBold, converted to
outlines with HarfBuzz shaping, so it needs no installed font and renders the
same in an embedded PNG.

Tests run on 2026-11-06:
- *Silhouette:* holds at 16 px; the eyes need 24 px, so 24 px is the minimum
  height.
- *One color:* passes (the mono file).
- *Reverse:* passes (white hanger with plum face).
- *Greyscale:* asleep and awake still read by shape alone.

Never recolor beyond the files, never place on a chart, never animate the
face.

## 5. How option 2 changes the report

The analytical content stays the same; the brand changes how it is said.

**Page 1, The Brand Review.**
- *Headline:* "Do not disturb, since 2020."
- *Subtitle:* "No renovation started since December 2020. Guests noticed:
  comfort down, value for money now the lowest of the four brands."
- *Masthead:* the sleeping hanger.
- *The promise scorecard:* three cards for "A good night", "A fair price"
  and "Booked with us". Each card shows a number, its comparison, and a
  verdict word in Ember with a down arrow, so the verdict never relies on
  color.
- The middleman and folio analysis sit below, unchanged in substance.

**Page 2, The Investment Strategy.**
- *Headline:* "Please make up the room."
- *Subtitle:* a DAX sentence, for example "$51.3M of $60.0M on six projects:
  buy the guest back, fix the welcome, build where we're full", which
  changes with the plan builder.
- *Masthead:* the awake hanger.
- *Plan-builder chips:* the hanger icon, awake for a funded initiative and
  asleep for one that isn't. The state is carried by shape and color
  together.

**Discipline.** The wordplay is used exactly twice (the two headlines). The
chips carry the face; nothing else does. Insight titles on every visual stay
in plain analytical English.

## 6. Components

- **Promise card:** Sheet surface, Seam hairline, radius 12.
  - Label in Trebuchet MS 13 pt plum-black.
  - Figure in Verdana Bold 26 pt plum-black.
  - Comparison in Verdana 11 pt: Harbour or Ember with an arrow and a word,
    for example "▼ lowest of four brands".
- **Insight title:** Trebuchet MS Bold 13 pt plum-black; subtitle Verdana
  10 pt plum-grey with unit and period.
- **State chip:** 32 px pill with a 24 px hanger icon (the logo's minimum
  size).
  - *Funded:* raspberry fill, white text, white awake hanger
    (`goodnight-inn-hanger-awake-on-accent`).
  - *Not funded:* Sheet fill, Seam border, plum-grey text, sleeping hanger
    icon.
- **Scenario toggle:** a segmented pill on Sheet. The selected option is
  plum-black with white text; Expected is the default.
- **Folio:** a Sheet receipt; figures right-aligned in Verdana; the line the
  inn keeps in plum-black; the commission line in Ember with a minus sign.
- **Scenario band:**
  - Low to High: raspberry at 15 % opacity between two raspberry hairlines.
  - Expected: a 2 px raspberry line.
  - Do-nothing baseline: a 2 px plum-slate line.
  - One printed sentence says what the band is.

## 7. Icon language

Rounded line icons, 2 px stroke, 20 px grid, round caps, plum-black by
default: hanger (asleep / awake), key fob, pillow, plane, road, city block,
calendar, receipt, warning triangle, check, reset arrow. Raspberry only when
the icon marks the story state. No moons, stars or "Zzz" (category clichés,
and option 1's territory). To be produced with `ic-icons` from these
descriptions.

## 8. Accessibility contract

- Every text pair >= 4.5:1; every meaning-bearing mark >= 3:1
  (`scripts/check_contrast.py --kit`, 10/10 on 2026-11-06).
- Blue-orange good/bad separates for protan, deutan and tritan readers
  (deltaE 91 / 104 / 87). It is still never shown without a sign, arrow or
  word.
- Trebuchet MS and Verdana were drawn for screen legibility and ship with
  both Windows and macOS, so a Mac judge sees the designed fonts without
  depending on Power BI web fonts.
- Alt text per visual at stage 5; tab order headline > scorecard > hero >
  supports > chrome; keyboard walk of the plan builder before G7.

## 9. Risks (the honest part)

- **Raspberry could read as consumer-marketing to a Board.** Mitigation:
  one accent, lots of Pillowcase, analytical titles everywhere but the two
  headlines.
- **The face could tip into cute.** Mitigation: states only, chrome only,
  never animated.
- **Verdana's width costs space.** Mitigation: the 1920 canvas, the 11 pt
  body, and the visual budget from the canon audit.
- **This option diverges from the pitched D1 look.** If D1 stays the
  direction, option 1 is the natural kit. Option 2 suits D1's structure with
  a different skin, or D2's "fifty keys" wall, where each hotel can carry a
  hanger state.

## 10. Hand-off

Activate with `brand_kit: goodnight-inn-hanger` in `project/project.yaml`,
then `theme-from-brand-kit` compiles the theme at stage 5. `ca-canvas` draws
the masthead and card furniture, `ic-icons` produces the icon set and
`ax-audit` proves the contract at the gates. The logo files are regenerated
by `project/tools/brand_logos.py`.
