# Goodnight Inn 3.1: the boardroom edition, night header

Companion to `brand.yaml` (version 3, revision 3.1). Björn's brief for 3.0: hip, modern and
businesslike; a basis for a Board report and an investor deck, not a poster.
The analysis of the current build (`opzet`) does not change; 3.0 changes how
it looks and how it is said.

## 0. Why 2.0 was replaced

2.0 made the door hanger a character (Hank) and pushed the chrome toward riso
print, paper grain and illustration. The AI images it produced were honest
results of those prompts, and they showed the problem: picture-book and
café-poster cues read as consumer and playful, not as an international hotel
group talking to its Board. 3.0 keeps what was sound (the palette, the
two-meaning color logic, the measured weights, the numbered findings) and
removes everything decorative from the entry. Hank, the poster wordmark and
the prompt pack stay in the repo, parked for guest-facing use.

## 1. Principles

1. **The data is the image.** No illustrations, characters or textures. Large
   exact figures, clean charts, hairlines and space carry the page.
2. **Goodnight Inn is always Coffee Blue; everyone else is Warm Grey.** The
   reader learns it once on P1 and never has to look for the brand again.
3. **Tangerine only signals.** A cost, a risk, a "last of four". Never a brand,
   never decoration, never without ▲ ▼ or a word.
4. **One argument per page, sized by importance.** P1's scorecard and P2's
   package scatter are the largest cards; everything else supports them.
5. **Say it, then show it.** A short declarative headline, a subtitle with the
   numbers, and card titles that state their finding.

## 2. Color

| Token | Hex | Contrast | Role |
|---|---|---|---|
| canvas · Oat Light | `#F3F1EA` | | page |
| surface · White | `#FFFFFF` | | cards |
| ink · Night | `#12233D` | 13.9 / 15.8 | text, masthead band, totals |
| ink_secondary · Dusk | `#4B5466` | 6.7 / 7.6 | labels, axes, captions |
| hairline · Seam | `#E3DFD3` | | borders, rules |
| oat · Oat Cream | `#E9E5D6` | 12.5 on Night | masthead text, neutral fills |
| accent · Deep Coffee | `#1763A8` | 5.5 / 6.2 | blue text, the recommendation, ▲ |
| accent_mark · Coffee Blue | `#2589D8` | 3.3 / 3.7 | Goodnight Inn's series |
| accent_tint · Ice | `#EAF2FB` | ink 13.9 | Goodnight Inn column, selected card |
| signal · Burnt Tangerine | `#A63F0E` | 5.6 / 6.3 | signal text, ▼ |
| signal_mark · Tangerine | `#E05A22` | 3.3 / 3.7 | signal marks (a cost, the Low case) |
| signal_tint | `#FCE6DB` | Burnt 5.2 | "Last of 4", risk chips |
| neutral_data · Warm Grey | `#8E897D` | 3.1 / 3.5 | sister brands, context |

`scripts/check_contrast.py --kit`: 10/10. Coffee Blue against Tangerine stays
far apart for every color-vision type (ΔE 94 / 111 / 112).

## 3. Type

Segoe UI throughout: Semibold for the headline (30 pt, 40 px on 1920), card
titles (14 pt) and figures; Regular for body text. Eyebrows in letter-spaced
Semibold capitals, Deep Coffee. Tabular figures.

**Floor: 12 pt (16 px on 1920)** for every table, axis, label and tooltip text,
per plan 08 item R4 (11-12 px once Publish-to-Web scales the page to a 1366
laptop). The comps draw some labels at 11-13 px for density; they show the
look, not the final sizes.

Segoe UI is Power BI's own default and the reason the page reads as modern.
It ships with Windows only: whether a Mac judge sees it under Publish-to-Web
is unverified. Test in a browser without Segoe UI before stage 6; the
fallback is Arial, with the layout re-measured. The comps use Open Sans, the
closest open stand-in, so they render the same everywhere.

## 4. Logo

The door hanger stays as the symbol, without a face: a Coffee Blue hanger with
its handle hole and slit. The wordmark is lowercase **goodnight inn.**,
outlined from Plus Jakarta Sans ExtraBold (OFL-1.1), with a Tangerine full
stop that closes it the way the promise closes ("A good night. A fair price.").

| File (`assets/`) | Use |
|---|---|
| `gi-lockup-reversed.svg` | Masthead on the Night band, 34 px tall |
| `gi-lockup.svg` | On light backgrounds: decks, documents |
| `gi-mark.svg` | Gallery icon, favicon, deck footer |
| `gi-mark-mono-night.svg`, `gi-mark-mono-oat.svg` | One color |
| `gi-wordmark.svg` | Wordmark alone |

Generator: `project/tools/brand_logos_v3.py`.

## 5. Page anatomy (1920 × 1080)

- **Band, 64 px, Night:** lockup, page tabs `01 Brand review` and
  `02 Investment strategy` (the active one in an Oat pill), context on the
  right in letter-spaced capitals.
- **Head:** eyebrow, headline, one-line subtitle with the numbers.
- **Body:** bento of white cards, radius 12, 20 px gutters, 32 px margins.
- **Foot:** data source and method note on the left, `goodnight inn. · 01 / 02`
  on the right.

**P1, The Brand Review.** Headline *Full rooms, fading guests.* The scorecard
(the four brands, Goodnight Inn in an Ice column, rank chips, change since
2023) carries the page; F4 geography sits beside it (region × type heat
table, the seven fullest hotels with airports in blue); three trend cards
below (margin after commissions, OTA share, NPS), Goodnight Inn in blue and
labelled, sisters in grey.

**P2, The Investment Strategy.** Headline *Fix the booking before the
building.* The package scatter carries the page (blue without the refresh,
grey with it, the "worth its cost" zone in Ice, A, B and C marked). Beside it:
the Low / Expected / High switch, three plan cards (A Recommended, B
Alternative, C Comparator: "Why not renovate everything?"), the waterfall of
A's NPV, A's cumulative net with the Low to High band, and the ten initiatives
with status, the P1 finding each answers, capex, go-live, run-rate and NPV.

Comps: `comps/p1-brand-review.html` and `comps/p2-investment-strategy.html`
(and `.png`), generated by `project/tools/comps_v3.py` from
`opzet-data.json`. Every figure is re-derived from the model before it ships.

## 5a. Depth: the night header (3.1)

Björn asked for more punch on 9 November ("the background can be turned to live
somehow, adding some 3D or shadowing"). Three depth levels were rendered on P1
(lift, light, night); he chose **night**. Real 3D stays out: 3D charts distort
values and are a hard-rule violation. The depth lives in the frame, never in the
data.

- **The zone.** A flat Night rectangle from the top of the page to the
  *horizon*: the top of the first card row + 128 px (y 312 in
  `opzet-layout.json`). Logo, masthead line, headline and subtitle sit in it.
- **The overlap.** The first card row starts inside the zone and hangs over
  the horizon. That layering is where the punch comes from.
- **One card style.** No hairline; one shadow on every top-level card: Night
  at 10 %, y 8, blur 24. P2's inner tiles keep their canvas fill and hairline
  and get no shadow (a shadow inside a card reads as a second layer).
- **Text on the zone.** Headline `zone_text` #F7F5EE (14.4:1), masthead line
  and subtitle `zone_text_muted` #C9D0DC (10.2:1), eyebrow `zone_eyebrow`
  #A9CDF0 (9.5:1).
- **The faded hanger.** In the zone, top right: the faceless hanger, Oat at
  6 %, large, tilted 10 degrees and cut off by the horizon. It is the one
  piece of brand theatre on the page, and it stays in the frame. Björn asked
  to keep it (9 November), which waives hard rule 6 (decorative images) and
  the canvas-guide "no logos in the background" rule for the header zone only.
  Text over it keeps 8.3:1 or better.
- **Where it is built.** Zone and shadows are drawn into the page background
  image by `project/tools/opzet_backgrounds.mjs` (canvas-studio: furniture
  only). No visual gets a shadow property, and `shape.shadow` stays `none`.
- **Optional, needs a waiver: night-glow.** A Night-to-navy gradient, a Coffee
  Blue glow, a stronger hero shadow and a blue glow under the recommended
  plan. It bends hard rule 6 for gradients and lock 9 (one card style), so it
  ships only with Björn's recorded waiver.

Comps (`comps/`): `*-night` is the spec, `*-night-glow` the optional variant,
`*-flat` the 3.0 baseline. The HTML comps are generated by
`project/tools/comps_v3.py`; the night-glow canvas by
`project/tools/brand_canvas_v3.py`.

## 6. Components

- **Chips** (pill, 11 px Semibold): `▲ Best of 4` Ice/Deep Coffee,
  `▼ Last of 4` tint/Burnt, `2nd of 4` neutral, `Funded` Ice, `Not funded`
  plain Dusk, `Recommended` / `Alternative` / `Comparator`, `Risk`.
- **Segmented control:** white pill track, the active option Night with Oat
  text.
- **Plan card:** letter, role chip, name, contents, NPV as the hero figure
  (Deep Coffee or Burnt by sign), one line of capex and timing. Selected:
  2 px Coffee Blue border on Ice.
- **Table:** Night rule under the header, Seam rules between rows, Goodnight
  Inn column in Ice, change column colored by direction with ▲ ▼.
- **Line chart:** Goodnight Inn 3 px Coffee Blue with an end dot and a bold
  end label; sisters 1.5 px Warm Grey with end labels; no legend.

## 7. Voice

Plain, exact, a little confident. Headlines are short declaratives; card
titles carry their number ("The airports are the fullest: 82.0% occupancy,
against 77.5% on the highway"). No wordplay beyond the two headlines.

## 8. Risks

- **Segoe UI on Mac under Publish-to-Web** (section 3). Test before stage 6.
- **Blue means Goodnight Inn and also "better".** Mitigated by never coloring
  a change without ▲ ▼, and by the change column using Deep Coffee text, not
  the series blue.
- **Density on P2.** The right column holds four components; if it feels
  crowded at 1366 px, the initiatives table moves to a drill-through tooltip.
- **Brand decision.** Option 2 is the recorded decision
  (`project/project-state/active/00-brand-decision.md`); `project.yaml` changes
  only when Björn picks this kit.

## 9. Hand-off

The full build plan, item by item with file and line references, is
`project/project-state/active/10-design-rebuild.md`, part B of the rebuild
package with plan 09 (content). In short:

Activate with `brand_kit: goodnight-inn-wakeup` in `project/project.yaml`,
compile the theme (`project/tools/compile_theme.py`; map `accent_mark` to
dataColors[0] and `neutral_data` to dataColors[1]), re-run
`check_contrast.py --theme`, and port the comps into `opzet_report.py`
through the px-prototype flow.
