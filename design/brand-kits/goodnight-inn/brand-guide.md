# Goodnight Inn brand guide (design elements beyond the tokens)

Companion to `brand.yaml`, which holds every token value. This file says how
the tokens become a report: the logo, the chrome, the components, the icon
language, the states, and the accessibility contract. All original work for
the Power BI Dataviz World Champs 2027 entry (the brand is fictional; nothing
here imitates a real hotel chain). Credits: the design doctrine and hard rules
of pbi-atelier; the canon in `dataviz-canon` (Muth on grey, Few on bullets,
IBCS on scenario notation, WCAG 2.2); Leonxlnx's consistency locks via
CREDITS.md.

## 1. The idea

A budget inn at night: paper sheets, navy sky, one window still lit. The
report is plain-spoken (a Board briefing, not a brochure), warm (paper and
amber, never grey-on-white corporate), rested (airy margins, nothing
blinking). The one amber light is the story: whatever carries amber on a
page is the thing the Board must look at. Everything else is navy ink or
grey context.

## 2. Logo

| File | Use |
|---|---|
| `assets/goodnight-inn-lockup.svg` / `@2x.png` | Masthead, top-left of both pages, 36 px tall at 1920x1080 |
| `assets/goodnight-inn-lockup-reversed.svg` / `@2x.png` | On Night surfaces only: the "How we calculated this" overlay header |
| `assets/goodnight-inn-mark.svg` / `@2x.png` | Gallery thumbnail, tooltip-page corner, favicon-size uses (>= 24 px) |
| `assets/goodnight-inn-mark-mono.svg` / `@2x.png` | Single-color contexts and print |

Construction: a 96-unit Night tile, corner radius 10 (the report's 4 px
radius scaled), a Linen crescent at the upper right, a four-pane window in
Lamp at the lower left standing on a Linen sill. Wordmark "Goodnight Inn",
"Inn" italic, Night ink, outlined from Gelasio (Eben Sorkin, OFL-1.1, drawn
metric-compatible with Georgia) so the logo needs no installed font and the
embedded PNG renders the same everywhere. Clear space: half the tile on every side. Minimum size:
mark 24 px, lockup 120 px wide. Never recolor beyond the four files, never
place on a chart, never as a watermark, never with a drop shadow. Power BI
takes the PNGs (image visual, embedded), the SVGs are the source.

## 3. Page chrome (the `z_*` layer, identical on both pages)

- **Masthead**, 64 px band on Paper: lockup at left; page name at right in
  Georgia 20 pt Night ("The Brand Review" / "The Investment Strategy", the
  contest's names); under it the period in Segoe UI 12 pt Dusk ("2021 to
  2025, 50 hotels" / "2027 to 2032, Expected scenario").
- **Headline**, Georgia 28 pt Night, one sentence, DAX-driven on P2. The
  one place Lamp may appear in text: a single figure or phrase inside the
  headline, never the whole line.
- **Footer**, 32 px band, Segoe UI 10 pt Dusk, hairline Fold above it: data
  source and weighting rule at left, "scenario logic labelled where used"
  and the refresh stamp at right. Same text on both pages.
- **Hairlines** (Fold, 1 px) separate regions; no boxes around charts. Cards
  are Linen on Paper with a Fold hairline, radius 4, no shadow: one card
  style per page (lock 9).

## 4. Components

- **KPI card** (new card visual): value in Segoe UI Semibold 28 pt Night;
  reference label below in Segoe UI 12 pt Dusk with the comparison in Pine
  or Brick plus a sign ("+1.2 pts vs 2024", "-2.3 % vs 2024"); a 12-point
  sparkline in Slate with the last point in Lamp. One base period for the
  whole band (audit item 1).
- **Insight title** on every visual: Segoe UI Semibold 14 pt Night, the
  finding, not the topic. Subtitle Segoe UI 12 pt Dusk for unit and period.
- **The folio** (D1 signature): a Linen receipt with a Fold hairline, Segoe
  UI figures right-aligned, dotted leaders in Fold, the total in Lamp ink.
- **The lamp chip** (plan builder state): a 24 px pill; on = Lamp fill with
  Linen text and a filled-window icon; off = Paper fill, Fold border, Dusk
  text and an outline-window icon. The icon changes with the state, so
  color is never the only carrier (hard rule 3).
- **Scenario toggle** (Low / Expected / High): three segmented buttons on
  Paper; the selected one Night fill with Linen text, the others Paper
  with Dusk text. Expected is the default and the reset target.
- **Departures board** (matrix): row header Segoe UI 12 pt Night; figures
  Segoe UI tabular, right-aligned; status column as a word plus a lamp
  icon; Gantt bars in Slate with the funded ones in Lamp.
- **Scenario band** on the impact chart: Low to High as a Lamp fill at
  18 % opacity between two Lamp hairlines; Expected as a 2 px Lamp line;
  the do-nothing baseline as a 2 px Slate line; one printed sentence
  states what the band is (canon DC-020).

## 5. Icon language

Line icons, 1.5 px stroke, 20 px grid, Night by default, Lamp when they
mark the story state. The set the entry needs: window (lit / unlit), moon,
key, bed, door, plane (airport hotels), road (highway), city skyline,
calendar, receipt, warning triangle (risks), check (plan valid), reset
arrow. Generated with `ic-icons` from these descriptions; no third-party
icon fonts (Publish-to-Web and the contest licence).

## 6. Color rules in practice

- One accent: Lamp. Ink weight `#9E5407` for text and thin marks; mark
  weight `#C2690A` for fills and bars. Never both on one visual, never the
  mark weight as text.
- The brand's own series (direct web, the Board's own numbers) is Navy
  `#2F4470`, which is ink, not emphasis.
- Context is Slate, Mist or Sand, always labelled directly, never in a
  legend far from the mark.
- Good and bad are Pine and Brick, always with a sign, arrow or word.
- Sister-brand benchmarks are Slate marks with the brand name printed.
- IBCS scenario notation where finance reads it: actual solid Night, prior
  year Slate, plan outlined Night, forecast hatched Lamp.
- Heat: the Lamp sequential ramp; divergence: Brick through paper-grey to
  Pine.

## 7. Typography rules in practice

Georgia for words in display sizes only (headline, page name, wordmark).
Segoe UI for everything else; Segoe UI Semibold for every figure.
Correction (2026-11-06): Georgia and Arial ship with Windows and macOS,
Segoe UI with Windows only. Whether a Mac judge sees Segoe UI depends on the
Power BI service serving it as a web font, which is unverified. Before G7,
open the Publish-to-Web link in a browser without Segoe UI. If it falls
back, switch body and numbers to Arial or Tahoma and re-measure the comp
before `px-prototype` trusts its rects. Sizes at 1920x1080: 28 / 20 / 14 / 12 / 10 pt; nothing smaller, so the
1366-wide laptop test still reads.

## 8. Designed states

Empty plan builder (no lamp on): the P2 headline says "Pick at least three
initiatives, one of them growth, under $60.0 M" in Dusk, the impact chart
shows the baseline only. Invalid plan (over budget or no growth move): the
headline turns the offending number Brick with a word ("over budget by
$1.3 M"). Scenario cleared: a bookmark restores Expected. Long project
names: the slicer shows the short name, the full name in the tooltip.

## 9. Accessibility contract

- Every text pair >= 4.5:1, every meaning-bearing mark >= 3:1
  (`scripts/check_contrast.py --kit`, re-run after any tweak, plus the
  overlay state on Night).
- Color never alone: sign, icon or word beside every Pine, Brick or Lamp
  state.
- Alt text per visual written at stage 5 in the page-purpose contracts;
  tab order follows the reading order (headline, KPI band, hero, supports,
  detail, chrome last).
- Keyboard walk of the plan builder and scenario toggle before G7.
- Georgia and Arial on both platforms; Segoe UI tested on a Mac browser
  before G7; no R or Python visuals; images embedded.

## 10. Hand-off

`theme-from-brand-kit` compiles `brand.yaml` into `theme.json` and the
hard-rule token values at stage 5; `ca-canvas` draws the backgrounds in
these tokens; `ic-icons` produces the icon set; `ax-audit` proves the
contract at the gates. Activate with `brand_kit: goodnight-inn` in
`project/project.yaml`.
