# Design handoff — World Champs BCN 26 — Round 3

Direction: **D7 "The Seductive Lies: A Trilogy"** (creative-direction contract, chosen
and authored by the entrant; approved with one change on 2026-08-05 — per-act tints)
Design Read: A marquee stating the takeaway over three tickets — you already know the
thesis before you choose which lie to watch fall.
Dials: DENSITY **balanced** · VARIANCE **expressive**
Canvas: **1280 × 720**, identical on every page · Theme: `theme.json` · Brand kit:
none (bespoke D7 mini-kit compiled into `theme.json`)
Measurement source: `project/design-prototypes/d7-trilogy.html` — the approved
interactive prototype. Its rect ledger and its CSS are the layout truth; every rect
below is read from it. (No `layout.json` / `reference_screenshots/` were produced this
round; the prototype's own ledger is the contracted substitute and is authoritative.)

## Reading me

- Visual ids follow `design/naming-conventions.md` and match `measures.dax`.
- "Polish" entries reference the numbered moves in the `dataviz-polish` skill.
- Rects are `x, y, w, h` in canvas px, top-left origin. Stage 6 builds them verbatim;
  the fidelity review measures against them at ±2 px.
- Anything not specified here defaults to `theme.json`. Visual-level overrides below
  are exceptions and each carries its reason.
- Where the prototype and this document differ, **this document wins** — every
  difference is listed under *Corrections applied to the prototype*, with its reason.

### Page-contract slot → built objects

The five page-purpose contracts name **slots**. A slot is a design idea; PBIR needs
objects. This is the reconciliation — every slot in `project-state/active/pages/*.yaml`
maps here, and no slot is dropped.

| Slot (page contract) | Page | Built as |
|---|---|---|
| `hero_takeaway` | p0 | `hero_takeaway` (unchanged) |
| `btn_ticket_act1/2/3` | p0 | `btn_ticket_actN` + `z_ticketN_body` / `_rule` / `_perf` / `_act` / `_hr` / `_title` / `_tease` / `_stub_art` |
| `html_ticket_tear` | p0 | **not built** — the contracted pre-torn fallback `z_ticketN_stub_art` ships instead (cut-list item 1) |
| `z_billing` | p0 | `z_billing_method` + `z_billing_caveats` (two lines, two measures) |
| `kpi_profit_naive` (+ `c_strike_act1`) | p1 | `kpi_profit_naive` / `kpi_profit_naive_corrected` + `z_kpi_profit_card` / `c_kpi_profit_kicker` / `c_kpi_profit_label` / `z_kpi_profit_strike` / `c_kpi_profit_misread` |
| `c_script_body` | p1, p2 | `c_pN_slug_naive` · `_action` · `_cue_naive` · `_dlg_naive` · `_note_*` (+ rules) · `_trans` · `_slug_honest` · `_cue_honest` · `_dlg_honest` |
| `dn_ticket_waffle` | p1 | `dn_ticket_waffle` + `z_waffle_card` / `c_waffle_kicker` / `c_waffle_title` / `c_waffle_cap` / `c_waffle_foot` |
| `c_verdict_act1/2/3` | p1–p3 | unchanged, plus `z_pN_verdict_rule` |
| `sl_beat_rail` | p1–p3 | `btn_beat_1` · `btn_beat_2` · `btn_beat_3` · `btn_next_scene` |
| `tbl_perfect_tens` | p2 | `tbl_perfect_tens` + `z_lb_card` / `c_lb_kicker` / `c_lb_more` |
| `dn_rating_fall` | p2 | `dn_rating_fall` + `z_fall_card` / `c_fall_kicker` / `c_fall_title` |
| `hero_premiere_scatter` | p3 | `hero_premiere_scatter` + `c_scatter_population` / `z_p3_scrim` / `c_winner_label` |
| `c_adjustments` | p3 | `z_adjustments_card` (+ `_lit`) · `z_adj_chip_*` ×4 · `c_adj_floor` / `_revenue` / `_m` / `_c` |
| `c_refusal_popularity` | p3 | `z_refusal_card` (+ `_lit`) · `c_refusal_title` · `c_refusal_why` · `tbl_refusal_ranks` |
| `c_nodate_chip` | p3 | `c_nodate_chip` + `z_nodate_card` |
| `hero_reconciliation` | p9 | `tbl_production_counts` (+ `c_cr_h_counts`) |
| `c_cast` | p9 | `c_cr_cast` (+ `c_cr_h_cast`) |
| `c_params` | p9 | `tbl_disclosed_params` (+ `c_cr_h_params`) |
| `c_glossary` | p9 | `c_cr_glossary` (+ `c_cr_h_glossary`) |
| `c_refusals` | p9 | `c_cr_refusals` (+ `c_cr_h_refusals`) |
| `c_credits_tmdb` | p9 | `c_cr_close_src` (+ `c_cr_close_last`) |

---

## Tokens (identical in `theme.json`, in the act-tint block, and here)

| Role | Paper surface | Night surface |
|---|---|---|
| Canvas | `#F5F2E9` | `#171418` |
| Card / surface | `#FFFFFF` | `#1D1A20` |
| Hairline border | `#D8D4C8` | `#2E2933` |
| Ink (primary text) | `#211E1A` | `#F2EFE6` |
| Ink secondary | `#57534E` | `#B5AFA0` |
| Trap / lie | `#B3402E` (5.08:1) | `#E8705F` (6.01:1) |
| Honest / corrected | `#2F6B4F` (5.62:1) | `#4ECBA0` (9.02:1) |
| Neutral data | `#78716C` | `#B5AFA0` |

**Act tints — CHROME ONLY** (entrant-approved 2026-08-05; documented exception to
consistency lock 7, bounded by the scope rule):

| Act | Tint | Paper | Night | Ratios | Reading |
|---|---|---|---|---|---|
| I | Ledger Indigo | `#2E4A7D` | `#7FA8DD` | 7.84 / 7.43 | the money act, shot cold |
| II | Awards Brass | `#8A6516` | `#D9A441` | 4.74 / 8.12 | the applause act, shot warm |
| III | Velvet Plum | `#5B3E8E` | `#B79BE8` | 7.43 / 7.71 | the corrected cut, house curtain |

**Scope rule (G6-checkable).** The tint touches exactly five chrome elements and
nothing else: the **act numeral** (the tinted run in the page header title), the
**ticket rule + serial** (p0 and the ADMIT ONE glyph on act pages), the **beat-rail
current-state fill**, the **page header rule**, the **verdict rule**. **Data never
wears the tint** — traps stay trap-red + strike + word, honest stays good-green + ✓ +
word, identically on every page. Any tinted data mark is a G6 defect. p9 carries no
tint. `measures.dax` deliberately contains no tint-returning measure.

**Hue budget per page** (≤ 6 families required; all pages carry 4 or fewer):
p0 = 3 act tints + warm neutrals (no data) · p1 = Act I tint + trap + honest +
neutrals · p2 = Act II tint + trap + honest + neutrals · p3 = Act III tint + trap +
honest + neutrals · p9 = trap + honest + neutrals (no tint).

**Structure.** Corner radius is a documented **2-step scale** (consistency lock 8):
**0 px on every surface, card, rule and chart**; **8 px on tickets and chips only**
(p0 ticket bodies, p3 adjustment chips, p3 no-date chip). **No shadows anywhere** —
`dropShadow.show = false` globally in the theme, no exceptions.

**Type scale** — 10 / 12 / 14 / 20 / 28 pt, plus two **granted exceptions**
(unresolved decision #7, default granted): **36 pt** ticket act numeral, **40 pt**
marquee title. Roles: **Bahnschrift SemiCondensed** display and chrome caps ·
**Consolas** screenplay body, numerals and credits · **Georgia Italic** verdicts and
the Key Takeaway · **Segoe UI** micro-UI (buttons, chart labels, table values).
**Nothing renders below 10 pt anywhere in the report** — see *Accessibility package*.

### Theme notes (JSON cannot carry comments — they live here)

- `theme.json` validates with **0 errors** against
  `reportThemeSchema-2.156.json` (microsoft/powerbi-desktop-samples, the latest
  schema in that repo as of 2026-08-05), checked with a Draft-7 validator. The
  `$schema` value is the repo's raw URL and was confirmed to resolve (HTTP 200).
- Card/property names were additionally cross-checked against Microsoft's own
  `Fluent2-CY26SU05.json` base theme, which ships inside this report's
  `StaticResources/SharedResources/BaseThemes/`.
- **Properties omitted because their effect could not be verified** (research-first:
  never emit an unverified property):
  - `accent` — present in the schema and in Fluent2, but undocumented on Microsoft
    Learn. Effect unknown → omitted rather than guessed.
  - `dataTitle` text class — in the 2.156 schema, absent from the Learn text-class
    table → omitted.
  - `mapPushpin`, `foregroundButton`, `foregroundSelected`, `foregroundDark`,
    `foregroundLight`, `foregroundNeutralSecondaryAlt`,
    `foregroundNeutralSecondaryAlt2`, `foregroundNeutralTertiaryAlt`, `icons`,
    `baseTheme` — schema-valid but unused by any D7 visual → omitted.
  - `cardVisual` visual-style block — no Microsoft-authored example of its card names
    was reachable, so **card formatting is specified per visual in this document**
    instead of in the theme.
  - Filter-pane styling (`outspacePane`, `filterCard`) is deliberately left at the
    base theme: the filter pane is *visible* because it carries the locked Adult
    filter, and it should read as a genuine Power BI control, not as disguised chrome.
- `smallDataLabel` **is** emitted at 10 pt although Learn does not document it —
  raising a font size can only help the 10 pt floor. Spot-check in Desktop.
- **`dataColors` is the token register, and it is zoned.** A Power BI theme carries
  one structural surface, so the night surface is in the structural slots and the
  paper surface lives in `dataColors` — that is how a builder picks a theme colour
  for a shape fill or a text run, so nothing in this report needs an ad-hoc hex.
  Positions **1–6 are data semantics** (trap paper/night, honest paper/night, neutral
  paper/night) and are the only ones a data mark may use. Positions **7–12 are the
  act tints** and **13–16 are the paper-surface structural tokens**
  (`#F5F2E9` canvas, `#211E1A` ink, `#FFFFFF` card, `#D8D4C8` hairline) — both zones
  are **CHROME ONLY**. Binding any of positions 7–16 to a data mark is a G6 defect.
- **PBIR property names.** `position.x / y / z / height / width / tabOrder` are
  verified against this report's own `visual.json` files (visualContainer schema
  2.11.0). The **alt-text property path could not be verified** — the visualContainer
  `$schema` URL returned 404 from this machine. Stage 6 must verify it against the
  `$schema` declared in the file it is editing before writing alt text.

---

## Page chrome

### Night pages (p0 · p3 · p9) — one background treatment for the archetype
Canvas `#171418`; cards `#1D1A20` with a 1 px `#2E2933` hairline, radius 0; every
card on a page uses the identical style (consistency lock 9). Visual headers off,
visual titles off (see *Titles*), padding 0.

### Paper pages (p1 · p2) — one background treatment for the archetype
Canvas `#F5F2E9`; cards `#FFFFFF` with a 1 px `#D8D4C8` hairline, radius 0. Because
`theme.json` is authored for the night surface, **every visual on p1, p2 and the
tooltip page carries the documented paper override**: card background `#FFFFFF`,
border `#D8D4C8`, text `#211E1A` / secondary `#57534E`, chart neutral `#78716C`.
That is one rule with one reason (a single theme cannot serve two surfaces); it is
not a per-visual improvisation.

### Titles — the recorded decision
**Every visual's built-in title is hidden report-wide** (`title.show = false` in the
theme). The design carries headings as on-canvas typography instead: screenplay
slugs, card kickers (`INSERT — …`), and section heads. This is the deliberate,
recorded decision required by the `pbir-style` rule — not a default left unset. Every
data visual compensates with an **alt-text measure carrying live numbers** (see
*Accessibility package*), so the heading survives for screen-reader users.

### Shared chrome per act page (p1 · p2 · p3)

| Element | Id | Spec |
|---|---|---|
| Header title | `z_pN_header_title` | textbox `24, 36, 830, 32`, Consolas 12 pt; three runs — `"THE SEDUCTIVE LIES — "` in ink, the **act numeral run** (`"ACT I"` / `"ACT II"` / `"ACT III"`) in the act tint, then `": ‘…’"` in ink. Background off, border off. |
| Header rule | `z_pN_header_rule` | basicShape `24, 80, 1232, 1`, fill = act tint, no border, radius 0 |
| Home button | `btn_home` | actionButton `866, 32, 130, 32`, text `⌂ BOX OFFICE`, → `p0-box-office` |
| Credits button | `btn_credits` | actionButton `1006, 32, 120, 32`, text `CREDITS ▸`, → `p9-end-credits` |
| ADMIT ONE glyph | `z_pN_admit_svg` | ca-canvas SVG image `1136, 32, 120, 40`; perforated ticket outline, stroke = **act tint** 1.5 px, fill `#FFFFFF` (paper) / `#241F28` (night), inner text `ADMIT ONE` in ink at 10 pt tracked. Decorative → hidden from tab order, empty alt text. |
| Beat rail | `sl_beat_rail` | three actionButtons + one advance button, see *Bookmarks* |
| Verdict rule | `z_pN_verdict_rule` | basicShape `24, 624, 1232, 1`, fill = act tint |
| Verdict | `c_verdict_actN` | textbox `24, 636, 1040, 56`, Georgia Italic 14 pt / 20 px, ink |

Beat-rail geometry, identical on all three act pages:

| Id | Rect | Text (p1/p2) | Text (p3) |
|---|---|---|---|
| `btn_beat_1` | `24, 100, 172, 32` | `SC.1 — THE SEDUCTION` | `SC.1 — THE ADJUSTMENTS` |
| `btn_beat_2` | `206, 100, 148, 32` | `SC.2 — THE NOTES` | `SC.2 — THE REFUSAL` |
| `btn_beat_3` | `364, 100, 200, 32` | `SC.3 — THE CORRECTED CUT` | `SC.3 — THE PREMIERE` |
| `btn_next_scene` | `1106, 100, 150, 32` | `NEXT SCENE ▸` | `NEXT SCENE ▸` (disabled at SC.3) |

Beat button properties: 10 pt Bahnschrift SemiCondensed, tracking 0.1 em, fill off,
1 px outline in ink, radius 0. **Current state:** fill = the page's **act tint**, text
`#F5F2E9` (paper pages) / `#171418` (p3), 3 px bottom rule in ink, and a leading `●`
glyph — so the current beat is marked by fill, by rule, **and** by a glyph, never by
colour alone. Each button's accessible name is `"Scene N of 3 — <title>"`.

---

## Live-number binding — one mechanism, decided once

Prose that contains a number is bound to a `Copy · …` / `Label · …` / `Title · …`
measure from `measures.dax`. Preferred mechanism: **a textbox with a dynamic-value
run** bound to the named measure — **VERIFY-AT-BUILD** that the installed Desktop
build serialises this into PBIR, and record the verdict in `BUILD_LOG.md`.
If it does not: **fallback A** — a `cardVisual` bound to the measure with the callout
styled as body text (loses inline mixed-run styling, keeps the live number);
**fallback B**, last resort — a static string typed from the value read out of the
model at build, with the value, the measure and the date recorded in `BUILD_LOG.md`.
Typing a number from this document, from the prototype, or from memory is a G6
defect in every case.

---

## Page p0 — `p0-box-office` (overview, night)

**Question:** What is this report's one claim, and how do I enter its three acts?
**3-second message:** The data is not wrong — the reading is: a trilogy in three acts,
three tickets, the takeaway on the marquee.
**Layout:** marquee band 24–136 · takeaway band 152–224 · three 384×312 tickets on a
424 px pitch at y 248 · billing block 592–648 · footer 664–696. Page margin 24, 8 px
grid throughout.

| Id | Visual | Intent | Data | Polish | Explicit properties |
|---|---|---|---|---|---|
| `z_marquee_frame` | basicShape rect | chrome | — | — | `24, 24, 1232, 112`; fill none; border 2 px `#F2EFE6`; radius 0; no title |
| `z_marquee_frame_inner` | basicShape rect | chrome | — | — | `28, 28, 1224, 104`; fill none; border 1 px `#F2EFE6`; radius 0 |
| `z_marquee_title` | textbox | report identity | — | — | `40, 44, 1200, 56`; Bahnschrift SemiCondensed 40 pt semibold, tracking 0.14 em, `#F2EFE6`, centred; **granted scale exception** |
| `z_marquee_sub` | textbox | framing | — | — | `40, 104, 1200, 22`; Bahnschrift 12 pt, tracking 0.32 em, `#B5AFA0`, centred |
| `hero_takeaway` | textbox (dynamic value) | S1 editorial framing — the mandated Key Takeaway | `[Title · Landing]` | 1 | `24, 152, 1232, 72`; Georgia Italic 14 pt / 22 px, `#F2EFE6`, centred, max text width 1180; background off; border off |
| `z_ticket1_body` | basicShape rect | chrome | — | — | `24, 248, 384, 312`; fill `#F5F2E9`; border none; **radius 8** |
| `z_ticket1_rule` | basicShape rect | chrome (tint carrier) | — | — | `30, 254, 372, 300`; fill none; border 2 px **`#2E4A7D`**; radius 0 |
| `z_ticket1_perf` | basicShape line | chrome | — | — | `316, 248, 1, 312`; 1 px dashed `#9A9284`; **VERIFY** dashed line style, fallback = the stub SVG draws it |
| `z_ticket1_act` | textbox | chrome | — | — | `54, 286, 238, 50`; Bahnschrift 36 pt semibold, `#211E1A`; **granted scale exception** |
| `z_ticket1_hr` | basicShape rect | chrome | — | — | `54, 348, 34, 1`; fill `#211E1A` |
| `z_ticket1_title` | textbox | chrome | — | — | `54, 362, 238, 60`; Bahnschrift 20 pt semibold, tracking 0.03 em, `#211E1A` |
| `z_ticket1_tease` | textbox | teaser | — | — | `54, 432, 238, 44`; Georgia Italic 12 pt, `#57534E` |
| `z_ticket1_stub_art` | **ca-canvas SVG** image | chrome (tint carrier) | — | — | `316, 248, 92, 312`; vertical `ADMIT ONE` 10 pt tracked ink + vertical serial `TMDB·2026·07·24` 10 pt in **`#2E4A7D`**; this art is also the contracted **pre-torn stub**; decorative → empty alt text, out of tab order |
| `btn_ticket_act1` | actionButton | **nv navigation** — the ticket IS the nav | teaser stat `[Financial coverage %]` in its alt text | 10 | `24, 248, 384, 312`; topmost z; fill off; outline off (default) / 2 px `#2E4A7D` (hover); text off; action = page navigation → `p1-act-i-profit` |
| `z_ticket2_*` / `btn_ticket_act2` | as above | — | `[Median votes]` | — | identical geometry at **x = 448**; tint `#8A6516`; → `p2-act-ii-ratings` |
| `z_ticket3_*` / `btn_ticket_act3` | as above | — | popularity refusal phrase | — | identical geometry at **x = 872**; tint `#5B3E8E`; → `p3-act-iii-corrected-cut` |
| `z_billing_method` | cardVisual | S1 scope stamp | `[Label · Method]` | 1 | `24, 592, 1232, 28`; callout Bahnschrift 10 pt, tracking 0.03 em, `#B5AFA0`, centred, wrap on; label off; background off; border off |
| `z_billing_caveats` | cardVisual | S1 scope stamp | `[Label · Caveats]` | 1 | `24, 620, 1232, 28`; same styling |
| `z_footer_credit` | textbox | attribution | — | — | `24, 664, 900, 32`; Segoe UI 10 pt, tracking 0.04 em, `#B5AFA0` |
| `btn_credits` | actionButton | navigation | — | — | `1106, 664, 150, 32`; text `END CREDITS ▸` Segoe UI 10 pt `#F2EFE6`; 1 px outline `#F2EFE6`; radius 0; → `p9-end-credits` |

Ticket 2 and 3 inner rects: add 424 / 848 to every ticket-1 x value.

**Interactions:** ticket click → native page navigation (never dependent on the tear).
Report-level filter `Movies[Adult] = FALSE` is **visible and locked**. No slicers.
**Leaves out:** any data visual, AI-generated key art, the tear animation (see
*Asset-fidelity inventory*).

---

## Page p1 — `p1-act-i-profit` (drivers, paper) · tint `#2E4A7D`

**Question:** Does the movie business really lose money — or does the dataset lose data?
**3-second message:** The "industry loses money" conclusion is an artifact — only a
13.2 % sliver of listings can support a money claim at all.
**Layout:** header band 24–80 · rule at 80 · beat rail 96–136 · screenplay column
24–784 (text column 524 wide, margin-note gutter at x 568) · insert column 800–1256 ·
verdict 624–696.

| Id | Visual | Intent | Data | Beats | Explicit properties |
|---|---|---|---|---|---|
| `c_p1_slug_naive` | textbox | S2 annotation + **M-003 marking** | — | 1·2·3 | `34, 162, 500, 20`; Consolas 12 pt `#211E1A` uppercase; second run `[naive cut]` at 10 pt in **`#B3402E`** |
| `c_p1_action` | textbox (dynamic) | S2 | `[Copy · Act I · action]` | 1·2·3 | `34, 195, 470, 40`; Consolas 12 pt / 19 px |
| `c_p1_cue_naive` | textbox | S2 | — | 1·2·3 | `34, 251, 470, 20`; Consolas 12 pt, centred in the 470 column |
| `c_p1_dlg_naive` | textbox (dynamic) | S2 — the lie in its own words | `[Copy · Act I · naive read]` | 1·2·3 | `129, 270, 315, 40`; Consolas 12 pt / 19 px |
| `c_p1_note_zeros` | textbox (dynamic) | S2 script-doctor note | `[Copy · Act I · note zeros]` | 2·3 | `568, 196, 206, 44`; Consolas 10 pt / 14 px `#B3402E`; paired rule `z_p1_note_rule_1` basicShape `568, 196, 2, 44` fill `#B3402E`; text inset 8 px |
| `c_p1_note_budget` | textbox | S2 | — | 2·3 | `576, 278, 198, 44`; rule `z_p1_note_rule_2` `568, 278, 2, 44` |
| `c_p1_note_negrev` | textbox | S2 | — | 2·3 | `576, 374, 198, 30`; rule `z_p1_note_rule_3` `568, 374, 2, 30` |
| `c_p1_trans` | textbox | S2 | — | 3 | `34, 328, 470, 20`; Consolas 12 pt, right-aligned, uppercase |
| `c_p1_slug_honest` | textbox | S2 | — | 3 | `34, 361, 500, 20` |
| `c_p1_cue_honest` | textbox | S2 | — | 3 | `34, 398, 470, 20`; centred |
| `c_p1_dlg_honest` | textbox (dynamic) | S2 — the honest counterpart | `[Copy · Act I · responsible read]` | 3 | `129, 417, 315, 116` |
| `z_kpi_profit_card` | basicShape rect | chrome | — | 1·2·3 | `800, 152, 456, 144`; fill `#FFFFFF`; border 1 px `#D8D4C8`; radius 0 |
| `c_kpi_profit_kicker` | textbox | label | — | 1·2·3 | `816, 166, 424, 16`; Consolas 10 pt tracking 0.14 em `#57534E`; text `INSERT — THE NAIVE NUMBER` |
| `c_kpi_profit_label` | textbox (dynamic) | label | `[Copy · Act I · kpi label]` | 1·2·3 | `816, 190, 424, 18`; Segoe UI 10 pt `#57534E` |
| `kpi_profit_naive` | cardVisual | **1 Magnitude — trap exhibit** | `[Profit (naive)]` | 1·2 | `816, 210, 424, 50`; callout Consolas 28 pt `#211E1A`; label off; background off; border off; alt `[Alt · kpi_profit_naive · SC1]` |
| `kpi_profit_naive_corrected` | cardVisual | same value, corrected state | `[Profit (naive)]` | 3 | identical rect and styling; alt `[Alt · kpi_profit_naive · SC3]` — the paired-variant pattern, because alt text must change with the state |
| `z_kpi_profit_strike` | basicShape rect | correction | — | 3 | `810, 236, 436, 2`; fill `#B3402E`; fades in via the bookmark tween (a fade, never a width-draw) |
| `c_kpi_profit_misread` | textbox | correction label | — | 3 | `816, 264, 424, 16`; Segoe UI 10 pt tracking 0.08 em `#B3402E`; text `MISREAD — see notes` |
| `z_waffle_card` | basicShape rect | chrome | — | 3 | `800, 312, 456, 296`; fill `#FFFFFF`; border 1 px `#D8D4C8` |
| `c_waffle_kicker` | textbox | label | — | 3 | `816, 324, 424, 16`; `INSERT — THE TICKET AUDIT` |
| `c_waffle_title` | textbox (dynamic) | insight title | `[Copy · Act I · waffle title]` | 3 | `816, 346, 424, 22`; Segoe UI 12 pt semibold `#211E1A` |
| `c_waffle_cap` | textbox | legend | — | 3 | `816, 370, 424, 16`; Segoe UI 10 pt `#57534E` |
| `dn_ticket_waffle` | **Deneb** (fallback: `hundredPercentStackedBarChart`) | **hero — 1 Magnitude, felt proportion** | `[Financial coverage %]`, `[Movies (credible financials)]`, `[Movies]` | 3 | `816, 390, 424, 176`; 100 cells, 10 × 10, cell 36 × 14, x-step 43, y-step 18, corner 2; **valid cells fill `#2F6B4F`** with two white punch dots (r 2.2); remainder outline 1 px `#78716C`, no fill; background off; alt `[Alt · dn_ticket_waffle]` |
| `c_waffle_foot` | textbox (dynamic) | caveat | `[Copy · Act I · waffle foot]` | 3 | `816, 574, 424, 26`; Segoe UI 10 pt `#57534E` |
| `c_verdict_act1` | textbox (dynamic) | S1 editorial framing | `[Copy · Act I · verdict]` | 1·2·3 | `24, 636, 1040, 56`; Georgia Italic 14 pt / 20 px `#211E1A`; trailing run at 11 pt: `(USD as recorded; gross gap, not P&L.)` |
| `btn_next_act` | actionButton | navigation | — | 1·2·3 | `1106, 648, 150, 32`; text `NEXT ACT ▸`; 1 px outline `#211E1A`; text `#211E1A`; → `p2-act-ii-ratings` |

Plus the shared chrome row: `z_p1_header_title`, `z_p1_header_rule`, `btn_home`,
`btn_credits`, `z_p1_admit_svg`, `btn_beat_1..3`, `btn_next_scene`,
`z_p1_verdict_rule`.

**Interactions:** beat rail drives `bm_p1_b1/b2/b3` (native tween only). Default beat
= **SC.1** (ack table row 3).
**Leaves out:** coverage-by-year (Act III owns over-time), genre splits, and any
unmarked appearance of `Profit (naive)`.

---

## Page p2 — `p2-act-ii-ratings` (drivers, paper) · tint `#8A6516`

**Question:** Is a perfect 10.0 the best film ever — or just the least-rated?
**3-second message:** A 10.0 on 2 votes is not a rating — weighted by evidence the
"best film ever" reads about 7.02.
**Layout:** identical template to p1; the insert column changes.

| Id | Visual | Intent | Data | Beats | Explicit properties |
|---|---|---|---|---|---|
| `c_p2_slug_naive` | textbox | S2 + **M-003-equivalent marking** | — | 1·2·3 | `34, 162, 500, 20`; second run `[naive cut]` 10 pt `#B3402E` |
| `c_p2_action` | textbox | S2 | — | 1·2·3 | `34, 195, 470, 20` |
| `c_p2_cue_naive` | textbox | S2 | — | 1·2·3 | `34, 232, 470, 20`; centred |
| `c_p2_dlg_naive` | textbox | S2 — the lie in its own words | film name is Q2-verified (M-006), **confirm at build** | 1·2·3 | `129, 251, 315, 40` |
| `c_p2_note_twovotes` | textbox | S2 | — | 2·3 | `576, 196, 198, 16`; rule `z_p2_note_rule_1` `568, 196, 2, 16` |
| `c_p2_note_median` | textbox (dynamic) | S2 | `[Copy · Act II · note median]` | 2·3 | `576, 248, 198, 44`; rule `z_p2_note_rule_2` `568, 248, 2, 44` |
| `c_p2_note_twenty` | textbox | S2 | — | 2·3 | `576, 352, 198, 44`; rule `z_p2_note_rule_3` `568, 352, 2, 44` |
| `c_p2_trans` | textbox | S2 | — | 3 | `34, 309, 470, 20`; right-aligned |
| `c_p2_slug_honest` | textbox | S2 | — | 3 | `34, 342, 500, 20` |
| `c_p2_cue_honest` | textbox | S2 | — | 3 | `34, 379, 470, 20`; centred |
| `c_p2_dlg_honest` | textbox (dynamic) | S2 | `[Copy · Act II · responsible read]` | 3 | `129, 398, 315, 80` |
| `z_lb_card` | basicShape rect | chrome | — | 1·2·3 | `800, 152, 456, 200`; `#FFFFFF` / 1 px `#D8D4C8` |
| `c_lb_kicker` | textbox | label | — | 1·2·3 | `816, 160, 424, 16`; `INSERT — THE PERFECT TENS` |
| `tbl_perfect_tens` | tableEx | **4 Ranking — the trap leaderboard** | `[Image · Poster URL]` (Image URL column, 32 × 44), `Movies[Title]`, `[Rating (raw)]`, `[Votes]`, `[Mark · Rating verdict]`, colour by `[Color · Rating verdict]` | 1·2·3 | `816, 180, 424, 150`; filter `[Rating (raw)] = 10`, top 3 ascending by `[Votes]`; column headers hidden; row height 48; horizontal gridline 1 px `#EBE7DC`, no vertical grid; values Segoe UI 12 pt `#211E1A`; score column Consolas 12 pt bold **`#B3402E`**; votes column Segoe UI 10 pt `#57534E` right-aligned, width 74; background off; alt `[Alt · tbl_perfect_tens]` |
| `c_lb_more` | textbox | scope | — | 1·2·3 | `816, 329, 424, 18`; Georgia Italic 10 pt `#57534E` |
| `z_fall_card` | basicShape rect | chrome | — | 3 | `800, 368, 456, 248` |
| `c_fall_kicker` | textbox | label | — | 3 | `820, 378, 420, 16`; `INSERT — THE CORRECTION` |
| `c_fall_title` | textbox | insight title | — | 3 | `820, 398, 420, 22`; Segoe UI 12 pt semibold |
| `dn_rating_fall` | **Deneb** (fallback: `clusteredBarChart`, paired bars) | **hero — the fall from applause to evidence** | `Movies[Title]`, `[Rating (raw)]`, `[Rating (evidence-weighted)]`, `[Rating C (disclosed)]` | 3 | `812, 422, 432, 172`; x scale 0–10, plot inset 18 px, row pitch 32, first row baseline y 40; raw dot r 5 **`#B3402E`** labelled `10.0 raw`; weighted dot r 5 **`#2F6B4F`** labelled `✓ N.NN weighted`; connector 1.5 px `#78716C`; C reference line dashed `#78716C` with a `C = 6.96` cap label; tick labels 0/2/4/6/8/10 at 10 pt `#78716C`; alt `[Alt · dn_rating_fall]` |
| `c_verdict_act2` | textbox (dynamic) | S1 | `[Copy · Act II · verdict]` | 1·2·3 | `24, 636, 1040, 56` |
| `btn_next_act` | actionButton | navigation | — | 1·2·3 | `1106, 648, 150, 32`; text `THE PREMIERE ▸`; → `p3-act-iii-corrected-cut` |

**Interactions:** beat rail → `bm_p2_b1/b2/b3`, default **SC.1**. `tbl_perfect_tens`
rows open the `tt-movie-poster` tooltip page — the poster is enhancement only; the
name, the rating and the vote count are always printed.
**Leaves out:** the full votes-vs-rating scatter (Act III owns it) and any average of
averages.

---

## Page p3 — `p3-act-iii-corrected-cut` (comparison, night) · tint `#B79BE8`

**Question:** With the adjustments applied — and one refused — which films actually
earn "best", and how does that evolve by release year?
**3-second message:** Adjust honestly, refuse what cannot be defined, and the truly
best-selling **and** best-rated films emerge — year by year.
**Layout:** header 24–80 · beat rail 96–136 · scatter 24–920 × 152–616 · right rail
936–1256 in three stacked cards · verdict 624–696.

| Id | Visual | Intent | Data | Beats | Explicit properties |
|---|---|---|---|---|---|
| `hero_premiere_scatter` | **native scatterChart** | **hero — correlation over time; the ≥1 core-visual rule** | X `Movies[Revenue]` **log scale**; Y `[Rating (evidence-weighted)]`; Details `Movies[Title]`; **Play axis** `'Release Year'[Year Label]` (sorted by `Year Sort`); mark colour `[Color · Scatter mark]` | 1·2·3 | `24, 152, 896, 464`; background `#1D1A20`; border 1 px `#2E2933`; legend off; category-axis title `Revenue (USD, log) — credible set`, value-axis title `Rating (evidence-weighted)`, both 10 pt `#B5AFA0`; value-axis gridlines 1 px `#241F28`, category gridlines off; **constant line** at 6.96 (Analytics pane), dashed `#6E6960`, label `C = 6.96` 10 pt `#B5AFA0`; marker size small; population filter and sentinel exclusions per `data-model.md`; play-axis default position = **latest year** (nothing essential is in motion); alt `[Alt · hero_premiere_scatter]` |
| `c_scatter_population` | textbox (dynamic) | scope on canvas | `[Label · Population]` | 1·2·3 | `40, 164, 500, 18`; Segoe UI 10 pt `#B5AFA0` |
| `z_p3_scrim` | basicShape rect | de-emphasis | — | 1·2 | `24, 152, 896, 464`; fill `#171418` at 65 % transparency, no border; the bookmark mechanism for "dim the scatter"; hidden from tab order, decorative |
| `c_winner_label` | textbox (dynamic) | annotation | `[Copy · Act III · winner label]` | 3 | `498, 248, 336, 50`; Segoe UI 10 pt / 15 px `#F2EFE6`, right-aligned; the leading `✓` is the non-colour carrier |
| `z_adjustments_card` | basicShape rect | chrome | — | 1·2·3 | `936, 152, 320, 136`; fill `#1D1A20`; border 1 px `#2E2933`; radius 0 |
| `z_adjustments_card_lit` | basicShape rect | spotlight variant | — | 1 | identical rect; fill `#282331`; border 1 px `#B5AFA0` — shown instead of the plain card at SC.1 (paired-variant pattern) |
| `z_adj_chip_floor` / `_revenue` / `_m` / `_c` | basicShape rects | chrome | — | 1·2·3 | `952, 167, 132, 22` · `952, 195, 132, 22` · `952, 223, 104, 22` · `952, 251, 104, 22`; fill none; border 1 px `#3A3441`; **radius 8** |
| `c_adj_floor` | textbox (dynamic) | disclosed parameter | `[Label · Chip floor]` | 1·2·3 | `964, 169, 110, 18`; Segoe UI 10 pt `#F2EFE6`, leading `✓` run in `#4ECBA0` |
| `c_adj_revenue` | textbox | disclosed parameter | — | 1·2·3 | `964, 197, 110, 18`; text `✓ Revenue > 0` |
| `c_adj_m` | textbox (dynamic) | disclosed parameter | `[Label · Chip m]` | 1·2·3 | `964, 225, 82, 18` |
| `c_adj_c` | textbox (dynamic) | disclosed parameter | `[Label · Chip C]` | 1·2·3 | `964, 253, 82, 18` |
| `z_refusal_card` | basicShape rect | chrome | — | 1·2·3 | `936, 304, 320, 152`; fill `#1D1A20`; **border 2 px `#E8705F`**; radius 0 — the one place trap red frames chrome, because the card *is* a refusal |
| `z_refusal_card_lit` | basicShape rect | spotlight variant | — | 2 | identical rect; fill `#282331`; border 2 px `#E8705F` |
| `c_refusal_title` | textbox | S1 | — | 1·2·3 | `952, 318, 288, 20`; Segoe UI 12 pt `#E8705F`, tracking 0.04 em; `ADJUSTMENT REFUSED — POPULARITY` |
| `c_refusal_why` | textbox | **M-007 disclosure** | — | 1·2·3 | `952, 342, 288, 32`; Segoe UI 10 pt / 14 px `#B5AFA0` |
| `tbl_refusal_ranks` | tableEx | **4 Ranking — rank divergence** | `Movies[Title]`, `[Rank · Popularity]`, `[Rank · Rating (weighted)]`, `[Rank · Revenue]` | 1·2·3 | `952, 378, 288, 52`; filter `[Rank · Popularity] <= 3`, sorted ascending; headers hidden; values Consolas 10 pt `#F2EFE6`; divergence flag column prints `✕` in `#E8705F` where the popularity rank and the weighted-rating rank differ by more than 100 places, blank otherwise; **popularity is never good/bad-coloured**; background off; alt `[Alt · c_refusal_popularity]` |
| `z_nodate_card` | basicShape rect | chrome | — | 1·2·3 | `936, 472, 320, 144`; fill `#1D1A20`; border 1 px `#2E2933`; **radius 8** |
| `c_nodate_chip` | cardVisual | **1 Magnitude — the labelled unknown** | `[Label · No date]` | 1·2·3 | `952, 486, 288, 116`; callout Segoe UI 10.5 pt / 17 px `#B5AFA0`, wrap on, label off, background off, border off; alt `[Alt · c_nodate_chip]` |
| `c_verdict_act3` | textbox (dynamic) | S1 — "THE END" | `[Copy · Act III · verdict]` | 1·2·3 | `24, 636, 1040, 56`; Georgia Italic 14 pt / 20 px `#F2EFE6` |
| `btn_roll` | actionButton | navigation | — | 1·2·3 | `1106, 648, 150, 32`; text `ROLL CREDITS ▸`; outline 1 px `#F2EFE6`; → `p9-end-credits` |

**Interactions:** beat rail → `bm_p3_b1/b2/b3`, **default SC.3** (ack table row 3).
Scatter points open `tt-movie-poster`. The play axis is enhancement, never the only
path to the finding.
**Leaves out:** any popularity aggregation or good/bad colouring; silently dropped
dateless rows (they are counted, visibly); causal claims.

---

## Page p9 — `p9-end-credits` (definitions, night, static, no tint)

**Question:** What exactly did I read — definitions, parameters, reconciliation, and
the claims this report refuses?
**3-second message:** Every number states its scope: the cast of lies, the production
counts, the disclosed parameters, the scenes deleted.
**Layout:** title band 24–88 · two 360 px columns at x 240 and x 680, both 104–592 ·
centred closing block 598–648 · home button 664–696.

| Id | Visual | Intent | Data | Explicit properties |
|---|---|---|---|---|
| `z_cr_title` | textbox | chrome | — | `24, 24, 1232, 64`; Bahnschrift 20 pt, tracking 0.3 em, `#F2EFE6`, centred |
| `c_cr_h_cast` | textbox | section head | — | `240, 104, 360, 18`; Bahnschrift 10 pt tracking 0.28 em `#B5AFA0`; `CAST` |
| `c_cr_cast` | textbox | S1 editorial framing — the three lies named | — | `240, 126, 360, 114`; Consolas 12 pt / 19 px `#F2EFE6`; dot leaders as literal ` . . . . ` runs in `#57534E`; each attribution on its own line |
| `c_cr_h_counts` | textbox | section head | — | `240, 256, 360, 18`; `PRODUCTION COUNTS` |
| `tbl_production_counts` | tableEx | **hero — the cross-foot** | `[Movies (all listings incl. adult)]`, `[Adult listings excluded]`, `[Movies]`, `[Duplicate listings]`, `[Duplicate Movie IDs]`, `[Movies (undated)]`, `[Movies (future-dated)]`, negative-revenue count | `240, 278, 360, 152`; headers hidden; label column left, value column right; Consolas 12 pt `#F2EFE6`; horizontal gridline 1 px `#57534E` (**dotted VERIFY** — solid is the accepted fallback, it is the dot-leader stand-in); BASIS row carries `✓ kept` in `#4ECBA0`; background off; alt `[Alt · tbl_production_counts]` |
| `c_cr_h_params` | textbox | section head | — | `680, 104, 360, 18`; `DISCLOSED PARAMETERS` |
| `tbl_disclosed_params` | tableEx | 10 Detail lookup | `[Financial floor (disclosed)]`, `[Rating m (disclosed)]`, `[Rating C (disclosed)]`, `[Snapshot anchor (disclosed)]` | `680, 126, 360, 96`; same styling as the counts table; robustness and derivation notes printed in the value column |
| `c_cr_h_glossary` | textbox | section head | — | `680, 237, 360, 18`; `THE GLOSSARY` |
| `c_cr_glossary` | textbox | 10 Detail lookup — M-001…M-007 | — | `680, 259, 360, 119`; Consolas 11 pt / 17 px `#F2EFE6`; tag runs: `[TRAP]` `#E8705F`, `[HONEST]` `#4ECBA0`, `[OPAQUE]` `#B5AFA0` — tag word plus colour, never colour alone |
| `c_cr_h_refusals` | textbox | section head | — | `680, 394, 360, 18`; `SCENES DELETED — CLAIMS WE REFUSE` |
| `c_cr_refusals` | textbox | the not-available list | — | `680, 416, 360, 40`; Consolas 11 pt / 17 px `#F2EFE6`; every row of `data-model.md` → *Metrics NOT available* must be traceable here |
| `c_cr_close_src` | textbox | attribution | — | `24, 598, 1232, 18`; Bahnschrift 10 pt tracking 0.24 em `#B5AFA0`, centred |
| `c_cr_close_last` | textbox | S1 sign-off | — | `24, 622, 1232, 26`; Georgia Italic 14 pt `#F2EFE6`, centred |
| `btn_home` | actionButton | navigation | — | `24, 664, 150, 32`; text `⌂ BOX OFFICE`; → `p0-box-office` |

**Interactions:** `btn_home` only. Static page — a credits *roll* in Power BI is
composed, never animated, and nothing here promises auto-scroll.
**Leaves out:** charts, DAX dumps, interactive filtering.

---

## Tooltip page — `tt-movie-poster` (320 × 420, paper, hidden)

| Id | Visual | Intent | Data | Explicit properties |
|---|---|---|---|---|
| `z_tt_bg` | basicShape rect | chrome | — | `0, 0, 320, 420`; fill `#FFFFFF`; border 1 px `#211E1A`; radius 0 |
| `img_tt_poster` | image | identification (data, not decoration) | `[Image · Poster URL]` | `75, 18, 170, 240`; scaling `Fit`; background off; border 1 px `#C8C3B4`; **omitted entirely if the base URL cannot be verified** — the card reads without it |
| `c_tt_name` | textbox | identification | `Movies[Title]` | `16, 268, 288, 24`; Bahnschrift 14 pt `#211E1A`, centred |
| `c_tt_year` | textbox | scope | `'Release Year'[Year Label]` | `16, 294, 288, 18`; Consolas 10 pt `#57534E`, centred |
| `tbl_tt_rows` | tableEx | 10 Detail lookup | `[Votes]`, `[Rating (raw)]`, `[Rating (evidence-weighted)]`, `[Rank · Popularity]` | `16, 318, 288, 72`; headers hidden; Consolas 10 pt; raw rating `#B3402E`; weighted rating `#2F6B4F` prefixed by `[Mark · Rating verdict]`; horizontal gridline 1 px `#C8C3B4`; alt `[Alt · tt_movie_poster]` |
| `c_tt_foot` | textbox | **M-007 disclosure** | — | `16, 396, 288, 16`; Segoe UI 10 pt `#57534E` |

Page settings: page type **Tooltip**, canvas 320 × 420 Custom, background `#FFFFFF`,
`displayArea.verticalAlignment = Top`. Bound as the tooltip of `tbl_perfect_tens`
rows and of `hero_premiere_scatter` points.

---

## Bookmarks — three beats per act page

Nine bookmarks: `bm_p1_b1`, `bm_p1_b2`, `bm_p1_b3`, `bm_p2_b1`, `bm_p2_b2`,
`bm_p2_b3`, `bm_p3_b1`, `bm_p3_b2`, `bm_p3_b3`.
Capture settings for all nine: **Data OFF · Display ON · Current page ON · All
visuals** (not "selected visuals" — the whole page state is the beat). Transition =
the native bookmark tween; **no custom animation exists in Power BI and none is
promised**. Reveals are fades; the Act I strike **fades in, it never draws** — a
width-draw is outside the honest motion vocabulary (prototype build record).

| Bookmark | Visible | Hidden |
|---|---|---|
| `bm_p1_b1` **(default)** | all chrome · `c_p1_slug_naive` · `c_p1_action` · `c_p1_cue_naive` · `c_p1_dlg_naive` · `z_kpi_profit_card` · `c_kpi_profit_kicker` · `c_kpi_profit_label` · `kpi_profit_naive` · `c_verdict_act1` · `btn_next_act` | the three notes + their rules · `c_p1_trans` · `c_p1_slug_honest` · `c_p1_cue_honest` · `c_p1_dlg_honest` · `kpi_profit_naive_corrected` · `z_kpi_profit_strike` · `c_kpi_profit_misread` · the whole waffle block |
| `bm_p1_b2` | everything in b1 **plus** `c_p1_note_zeros` · `c_p1_note_budget` · `c_p1_note_negrev` and their three rules | as b1 minus the notes |
| `bm_p1_b3` | everything in b2 **plus** `c_p1_trans` · `c_p1_slug_honest` · `c_p1_cue_honest` · `c_p1_dlg_honest` · `kpi_profit_naive_corrected` · `z_kpi_profit_strike` · `c_kpi_profit_misread` · `z_waffle_card` · `c_waffle_kicker` · `c_waffle_title` · `c_waffle_cap` · `dn_ticket_waffle` · `c_waffle_foot` | `kpi_profit_naive` (replaced by its corrected variant) |
| `bm_p2_b1` **(default)** | all chrome · `c_p2_slug_naive` · `c_p2_action` · `c_p2_cue_naive` · `c_p2_dlg_naive` · `z_lb_card` · `c_lb_kicker` · `tbl_perfect_tens` · `c_lb_more` · `c_verdict_act2` · `btn_next_act` | the three notes + rules · `c_p2_trans` · `c_p2_slug_honest` · `c_p2_cue_honest` · `c_p2_dlg_honest` · the whole fall block |
| `bm_p2_b2` | b1 **plus** `c_p2_note_twovotes` · `c_p2_note_median` · `c_p2_note_twenty` and their rules | as b1 minus the notes |
| `bm_p2_b3` | b2 **plus** `c_p2_trans` · `c_p2_slug_honest` · `c_p2_cue_honest` · `c_p2_dlg_honest` · `z_fall_card` · `c_fall_kicker` · `c_fall_title` · `dn_rating_fall` | — |
| `bm_p3_b1` | all chrome · `hero_premiere_scatter` · `c_scatter_population` · **`z_p3_scrim`** · **`z_adjustments_card_lit`** · the four chips and their labels · `z_refusal_card` + its contents · `z_nodate_card` + `c_nodate_chip` · `c_verdict_act3` · `btn_roll` | `z_adjustments_card` (plain) · `z_refusal_card_lit` · `c_winner_label` |
| `bm_p3_b2` | as b1 but **`z_refusal_card_lit`** shown and `z_adjustments_card` plain | `z_adjustments_card_lit` · `c_winner_label` |
| `bm_p3_b3` **(default)** | everything plain **plus** `c_winner_label` | `z_p3_scrim` · `z_adjustments_card_lit` · `z_refusal_card_lit` |

Motion budget: exactly **one** story-state mechanism per page (the beat rail) plus the
native play axis on p3 — inside the `dataviz-polish` move-10 budget.

---

## The M-003 equivalent marking — non-negotiable

`Profit (naive)` (M-003) and the perfect-ten leaderboard (M-005 trap) may never appear
unaccompanied. On **every** SC.1 beat, four carriers are present simultaneously:

1. **Slug tag** — `[naive cut]` in trap red beside the scene heading
   (`c_p1_slug_naive`, `c_p2_slug_naive`).
2. **Beat rail** — `SC.1 — THE SEDUCTION` is the current state, and the button's
   accessible name reads `Scene 1 of 3`.
3. **Card kicker + label** — `INSERT — THE NAIVE NUMBER` above, and the label ends in
   the word `(naive)`; on p2, `Mark · Rating verdict` prints `✕ thin evidence` on
   every leaderboard row from SC.1 onward.
4. **Alt text** — `[Alt · kpi_profit_naive · SC1]` opens with the words
   `"Trap exhibit."`.

At SC.3 the correction lands: `z_kpi_profit_strike` fades in across the value and
`c_kpi_profit_misread` prints `MISREAD — see notes`. A build in which
`Profit (naive)` is visible without carriers 1, 3 and 4 fails G6 at blocker severity.

---

## Accessibility package

The contest's accessibility judge tests by hand, and an entry below 50 % accessibility
cannot win or be judge's favourite (05-design.md, judge intelligence finding 1). This
package is contract, not aspiration.

### Tab order (PBIR `position.tabOrder`; step 100 per stop)

Chrome that carries no information — frames, rules, card backgrounds, scrims, the
ADMIT ONE glyphs, ticket internals whose content is repeated in a button's alt text —
is **removed from the tab order** and given empty alt text. Everything below is a stop.

- **p0** — `z_marquee_title` → `z_marquee_sub` → `hero_takeaway` → `btn_ticket_act1`
  → `btn_ticket_act2` → `btn_ticket_act3` → `z_billing_method` →
  `z_billing_caveats` → `z_footer_credit` → `btn_credits` (10 stops).
- **p1** — `z_p1_header_title` → `btn_home` → `btn_credits` → `btn_beat_1` →
  `btn_beat_2` → `btn_beat_3` → `btn_next_scene` → `c_p1_slug_naive` →
  `c_p1_action` → `c_p1_cue_naive` → `c_p1_dlg_naive` → `kpi_profit_naive` /
  `kpi_profit_naive_corrected` → `c_p1_note_zeros` → `c_p1_note_budget` →
  `c_p1_note_negrev` → `c_p1_trans` → `c_p1_slug_honest` → `c_p1_cue_honest` →
  `c_p1_dlg_honest` → `dn_ticket_waffle` → `c_waffle_foot` → `c_verdict_act1` →
  `btn_next_act` (23 stops; hidden visuals drop out of the order automatically).
- **p2** — `z_p2_header_title` → `btn_home` → `btn_credits` → `btn_beat_1..3` →
  `btn_next_scene` → `c_p2_slug_naive` → `c_p2_action` → `c_p2_cue_naive` →
  `c_p2_dlg_naive` → `tbl_perfect_tens` → `c_lb_more` → `c_p2_note_twovotes` →
  `c_p2_note_median` → `c_p2_note_twenty` → `c_p2_trans` → `c_p2_slug_honest` →
  `c_p2_cue_honest` → `c_p2_dlg_honest` → `dn_rating_fall` → `c_verdict_act2` →
  `btn_next_act` (22 stops).
- **p3** — `z_p3_header_title` → `btn_home` → `btn_credits` → `btn_beat_1..3` →
  `btn_next_scene` → `c_scatter_population` → `hero_premiere_scatter` →
  `c_winner_label` → `c_adj_floor` → `c_adj_revenue` → `c_adj_m` → `c_adj_c` →
  `c_refusal_title` → `c_refusal_why` → `tbl_refusal_ranks` → `c_nodate_chip` →
  `c_verdict_act3` → `btn_roll` (20 stops).
- **p9** — `z_cr_title` → `c_cr_h_cast` → `c_cr_cast` → `c_cr_h_counts` →
  `tbl_production_counts` → `c_cr_h_params` → `tbl_disclosed_params` →
  `c_cr_h_glossary` → `c_cr_glossary` → `c_cr_h_refusals` → `c_cr_refusals` →
  `c_cr_close_src` → `c_cr_close_last` → `btn_home` (14 stops).
- **tt-movie-poster** — tooltip pages are not tab-navigable; the hovering row's own
  alt text plus `[Alt · tt_movie_poster]` carry the content.

### Alt text — state-specific, live-number

Every data visual binds its Alt text through **fx → Field value** to its measure in
`06 Display\Alt text`. Where the *meaning* of a visual changes with the beat, the
visual is split into paired variants so the alt text changes with it — that is the
only reason `kpi_profit_naive` / `kpi_profit_naive_corrected` exist as two objects.
Decorative chrome carries **empty** alt text and is out of the tab order; a
decorative object with narration is as much a defect as a data visual without it.

Two alt-text measures are named for a **page-contract slot** rather than for a single
visual id, because the slot is built from several objects. Their bindings are explicit
and are not a naming mismatch: `[Alt · c_refusal_popularity]` binds to
**`tbl_refusal_ranks`** (the data visual inside the `c_refusal_popularity` slot on
p3), and `[Alt · tt_movie_poster]` binds to **`tbl_tt_rows`** on the
**`tt-movie-poster`** tooltip page.

**Attribution blocker.** The dynamic-alt-text technique comes from the Fabric
Community post *"Accessibility in Action: Building Reusable Alternative Text Logic"*
supplied by the entrant. The author's name was not retrievable through the community
403 wall. Per attribution rule 5, the author **must** be retrieved in a browser and
added to `contracts/source-register.yaml` **and** `CREDITS.md` **before** this family
is implemented at stage 6. Building first and crediting later is a blocker-severity
defect.

### Focus, colour and size

- **Focus outline:** Power BI's native focus indicator is used and **never overridden
  or suppressed**; the design's own spec (matching the prototype) is a **2 px outline
  at 2 px offset** in the surface ink — `#F2EFE6` on night, `#211E1A` on paper.
  The a11y audit checks the rendered indicator against 3:1 on both surfaces; if the
  host indicator falls short, the finding is raised rather than worked around.
  Buttons additionally take a 1 px hover outline (`#B5AFA0` night / `#57534E` paper)
  so pointer users get feedback the keyboard user already has.
- **Colour is never the only carrier** (hard rule 3): trap red always travels with a
  strike, an `✕`, or the word `naive` / `MISREAD` / `thin evidence`; honest green
  always travels with a `✓` or the word `weighted` / `kept` / `HONEST`; the current
  beat carries a `●` and a bottom rule as well as its fill; the act tints carry no
  meaning at all and are always redundant with a printed act numeral.
- **10 pt floor, report-wide.** The theme raises `label`, `smallLabel`, `lightLabel`,
  `smallLightLabel` and `smallDataLabel` to 10 pt, and **no visual override drops
  below 10 pt anywhere**. Prototype sizes raised to meet the floor: card kickers
  9 → 10 pt · waffle caption 9 → 10 pt · `MISREAD` tag 9 → 10 pt · refusal rationale
  9.5 → 10 pt · tooltip footnote 8 → 10 pt · ticket serial 8 → 10 pt · the `ADMIT ONE`
  text inside the ticket glyphs ≈ 7 → 10 pt.
- **Contrast:** every pair in the token table is verified AA; the six act-tint
  variants were verified against the WCAG formula on 2026-08-05 (4.74:1 worst case,
  Act II on paper).

---

## Copy strings — verbatim

Every string below ships exactly as written. Strings marked **(measure)** are composed
by `measures.dax`; the text here is the shape they must take, with `‹…›` marking the
live part.

### p0
- `z_marquee_title`: `THE SEDUCTIVE LIES`
- `z_marquee_sub`: `A TRILOGY IN THREE ACTS  ·  A TMDB DATA STORY`
- `hero_takeaway` **(measure `Title · Landing`)**: `The data is not wrong — the reading is. ‹87%› of ‹84,036› listings have no credible financials, the median listing has zero votes, and “popularity” has no published formula. Every honest number here states what it excludes.`
- Ticket 1: `ACT I` / `THE PROFIT LIE` / `In which $0 is money`
- Ticket 2: `ACT II` / `THE RATINGS LIE` / `In which 2 votes crown a champion`
- Ticket 3: `ACT III` / `THE CORRECTED CUT` / `In which the fixes land — and one is refused`
- Ticket stubs: `ADMIT ONE` and the serial `TMDB·2026·07·24`
- `z_billing_method` **(measure `Label · Method`)**: `TMDB SNAPSHOT 2026·07·24 · BASIS ‹84,036› LISTINGS (ADULT ‹1,358› EXCLUDED OF ‹85,394›) · FINANCIAL FLOOR $10,000 · m=100 · C=6.96 · LISTINGS≠FILMS: ‹1,697› DUPLICATE (TITLE,DATE) PAIRS (‹2.0%›)`
- `z_billing_caveats` **(measure `Label · Caveats`)**: `USD AS RECORDED — NOT INFLATION-ADJUSTED · MEDIAN LISTING: 0 VOTES · POPULARITY: FORMULA NOT PUBLISHED`
- `z_footer_credit`: `SOURCE DATA BY TMDB — THIS PRODUCT USES TMDB DATA BUT IS NOT ENDORSED OR CERTIFIED BY TMDB`
- `btn_credits`: `END CREDITS ▸`

### p1
- `z_p1_header_title`: `THE SEDUCTIVE LIES — ACT I: ‘THE PROFIT LIE’`
- `c_p1_slug_naive`: `INT. THE NAIVE SCREENING ROOM — NIGHT` + `[naive cut]`
- `c_p1_action` **(measure)**: `The ANALYST sums profit across all ‹84,036› listings. No questions asked.`
- `c_p1_cue_naive`: `THE NAIVE READ`
- `c_p1_dlg_naive` **(measure, sign-variant)**: `The movie business loses money. Look: ‹$…›.` — the verb flips to `prints money` if the computed naive profit is positive
- `c_p1_note_zeros` **(measure)**: `NOTE: ‹67,436› revenues (‹79.0%›) are ZERO — unknowns counted as $0.`
- `c_p1_note_budget`: `NOTE: Budget is never 0 here. Unknowns arrive as junk: min $1, median $2,800.`
- `c_p1_note_negrev`: `NOTE: one listing books −$12 revenue.`
- `c_p1_trans`: `SMASH CUT TO:`
- `c_p1_slug_honest`: `INT. THE HONEST SCREENING ROOM — DAY`
- `c_p1_cue_honest`: `THE RESPONSIBLE READ`
- `c_p1_dlg_honest` **(measure)**: `Only ‹11,110› listings — ‹13.2%› — can support money claims (Budget ≥ $10,000 AND Revenue > 0). Median credible profit: ‹$…›. The mean, ‹$…›, is blockbuster-dragged.`
- `c_kpi_profit_kicker`: `INSERT — THE NAIVE NUMBER`
- `c_kpi_profit_label` **(measure)**: `Profit, all ‹84,036› listings (naive)`
- `c_kpi_profit_misread`: `MISREAD — see notes`
- `c_waffle_kicker`: `INSERT — THE TICKET AUDIT`
- `c_waffle_title` **(measure)**: `‹13.2%› hold a valid ticket (floor $10,000)`
- `c_waffle_cap`: `green ✓ = VALID (13) · outline = no credible financials (87)`
- `c_waffle_foot` **(measure)**: `median ‹$…› · mean ‹$…› · USD as recorded, gross gap not P&L`
- `c_verdict_act1` **(measure)**: `The industry doesn't lose money — the dataset loses data. Claim only the ‹13.2%› we can verify.` + 11 pt run `(USD as recorded; gross gap, not P&L.)`
- `btn_next_act`: `NEXT ACT ▸`

### p2
- `z_p2_header_title`: `THE SEDUCTIVE LIES — ACT II: ‘THE RATINGS LIE’`
- `c_p2_slug_naive`: `INT. THE AWARDS NIGHT — NIGHT` + `[naive cut]`
- `c_p2_action`: `The envelope opens. The ROOM leans in.`
- `c_p2_cue_naive`: `THE NAIVE READ`
- `c_p2_dlg_naive`: `The best film ever made? Las mujeres deciden. A perfect 10.0!` *(film name Q2-verified via M-006; re-confirm at build)*
- `c_p2_note_twovotes`: `NOTE: 2 votes.`
- `c_p2_note_median` **(measure)**: `NOTE: the MEDIAN listing has ‹0› votes; 75th percentile has ‹1›; ‹65.5%› have none.`
- `c_p2_note_twenty`: `NOTE: at least 20 films score a perfect 10.0 on 2–3 votes.`
- `c_p2_trans`: `SMASH CUT TO:`
- `c_p2_slug_honest`: `INT. THE RECOUNT — DAY`
- `c_p2_cue_honest`: `THE RESPONSIBLE READ`
- `c_p2_dlg_honest` **(measure)**: `Weighted by evidence (m=100, C=6.96), a 10.0 on 2 votes reads ‹7.02›. The Godfather reads ‹…›. Applause is not evidence.`
- `c_lb_kicker`: `INSERT — THE PERFECT TENS`
- `c_lb_more`: `+ at least 18 more perfect 10s`
- `c_fall_kicker`: `INSERT — THE CORRECTION`
- `c_fall_title`: `Raw applause → evidence-weighted`
- `c_verdict_act2` **(measure)**: `Applause is not evidence: 10.0 on 2 votes reads ‹7.02› with m=100, C=6.96.`
- `btn_next_act`: `THE PREMIERE ▸`

### p3
- `z_p3_header_title`: `THE SEDUCTIVE LIES — ACT III: ‘THE CORRECTED CUT’`
- `c_scatter_population` **(measure)**: `films with credible financials AND ≥ 100 votes · n = ‹…›`
- Axis titles: `Revenue (USD, log) — credible set` · `Rating (evidence-weighted)` · reference-line label `C = 6.96`
- Chips **(measures)**: `✓ floor $10,000` · `✓ Revenue > 0` · `✓ m = 100` · `✓ C = 6.96`
- `c_refusal_title`: `ADJUSTMENT REFUSED — POPULARITY`
- `c_refusal_why`: `formula not published. Ranked under protest, never colored, never averaged.`
- `c_winner_label` **(measure)**: `✓ ‹winner› — best-selling AND best-rated on evidence`
- `c_nodate_chip` **(measure)**: `‹26,166› listings (‹30.6%›) have no date — they never enter this animation · ‹320› future-dated flagged · sentinels 1800/2099 (‹…›) excluded from play`
- `c_verdict_act3` **(measure)**: `THE END — the best movie, read responsibly: ‹winner›, best-selling AND best-rated on evidence. Correlation shown; causation refused.`
- `btn_roll`: `ROLL CREDITS ▸`

### p9
- `z_cr_title`: `END CREDITS — METHOD & REFUSALS`
- `CAST`: `THE ZERO-FILLED FINANCIALS … as 'The Industry Loses Money'` · `THE TWO-VOTE PERFECT TEN … as 'Better Than The Godfather'` · `THE UNPUBLISHED FORMULA … as 'The People's Favorite'`
- `PRODUCTION COUNTS` rows: `LISTINGS PER SOURCE` · `ADULT TITLES EXCLUDED` · `BASIS` (with `✓ kept`) · `DUPLICATE (TITLE, DATE) PAIRS` · `DUPLICATE IDS` · `NO RELEASE DATE` · `FUTURE-DATED` · `NEGATIVE REVENUE`
- `DISCLOSED PARAMETERS` rows: `FINANCIAL FLOOR … $10,000 (13.1% vs 11.9% @ $100k)` · `m, EVIDENCE REQUIRED … 100 (Vote Count p90=106)` · `C, GLOBAL MEAN … 6.96` · `SNAPSHOT … 2026·07·24`
- `THE GLOSSARY`: `M-001 LISTINGS COUNT — rows, not films` · `M-002 COVERAGE — share of basis with a value` · `M-003 NAIVE PROFIT [TRAP] — counts $0 unknowns` · `M-004 MEDIAN CREDIBLE [HONEST] — floor $10k, Rev>0` · `M-005 RAW RATING — any votes, even 2` · `M-006 WEIGHTED RATING [HONEST] — m=100, C=6.96` · `M-007 POPULARITY [OPAQUE] — formula not published`
- `SCENES DELETED — CLAIMS WE REFUSE`: `inflation-adjusted money · true P&L · distinct-film counts · full-catalogue claims · popularity's meaning`
- `c_cr_close_src`: `SOURCE DATA BY TMDB — NOT ENDORSED OR CERTIFIED BY TMDB`
- `c_cr_close_last`: `No averages of averages were computed in the making of this report.`
- `btn_home`: `⌂ BOX OFFICE`

### tt-movie-poster
- Row labels: `VOTES` · `RATING (RAW)` · `RATING (WEIGHTED)` · `RANK · POPULARITY †`
- `c_tt_foot`: `† formula not published — ranked under protest`

---

## Asset-fidelity inventory

Every visual ingredient of the approved prototype, mapped to **exactly one**
implementation medium. Nothing is unmapped. Ingredients that PBIR cannot reproduce
were designed out of the shipped report rather than inventoried away after the fact,
and each carries the fallback that was contracted at the same time.

| # | Ingredient (from the prototype) | Page / slot | Medium | Notes |
|---|---|---|---|---|
| 1 | Marquee double-rule frame | p0 / chrome | native basicShape ×2 | 2 px outer + 1 px inner, radius 0 |
| 2 | Marquee 40 pt tracked title | p0 / chrome | native textbox | granted scale exception |
| 3 | Marquee tracked subtitle | p0 / chrome | native textbox | |
| 4 | Key Takeaway serif paragraph | p0 / `hero_takeaway` | native textbox + `[Title · Landing]` | live counts |
| 5 | Ticket body, cream, 8 px radius | p0 / ×3 | native basicShape | the only 8 px surfaces besides p3 chips |
| 6 | Ticket 2 px inner rule | p0 / ×3 | native basicShape | **act tint** (was trap red) |
| 7 | Ticket perforation, dashed | p0 / ×3 | native line shape | dashed style **VERIFY**; fallback = drawn inside #8 |
| 8 | Stub interior: vertical `ADMIT ONE` + serial | p0 / ×3 | **ca-canvas SVG** | doubles as the contracted **pre-torn stub** art |
| 9 | Ticket act numeral / title / teaser | p0 / ×3 | native textbox ×3 | |
| 10 | Ticket click → act page | p0 / ×3 | native actionButton | transparent, topmost, alt text carries the whole ticket |
| 11 | **Ticket tear** (translate + 8° rotate + fade) | p0 | **accepted omission** | no PBIR mechanism; HTML Content is VERIFY-only and is cut-list item 1. The pre-torn stub art (#8) is the shipped design. |
| 12 | 14 mechanism legend chips | all | **accepted omission** | prototype instrumentation, never report content |
| 13 | Billing block, two lines | p0 / `z_billing_*` | native cardVisual ×2 | live via display measures |
| 14 | TMDB credit line | p0, p9 | native textbox | |
| 15 | `END CREDITS ▸` button | p0 | native actionButton | |
| 16 | Screenplay header with tinted act run | p1·p2·p3 | native textbox, multi-run | the act-numeral tint carrier |
| 17 | `ADMIT ONE` ticket glyph 120 × 40 | p1·p2·p3 | **ca-canvas SVG** | stroke = act tint; decorative, empty alt |
| 18 | Header rule / verdict rule, 1 px | p1·p2·p3 | native basicShape ×2 per page | act tint |
| 19 | Beat rail, `●` marker + 3 px underline | p1·p2·p3 | native actionButton ×4 | drives the bookmarks |
| 20 | Screenplay slug / action / cue / dialogue / transition | p1·p2 | native textbox ×8 per page | numbers via `Copy · …` measures |
| 21 | `[naive cut]` tag | p1·p2 | native textbox run | the M-003 marking |
| 22 | Margin notes + 2 px left rules | p1·p2 | native textbox ×3 + basicShape ×3 | |
| 23 | Insert cards (KPI, waffle, leaderboard, fall) | p1·p2 | native basicShape ×4 | identical style per page (lock 9) |
| 24 | Naive-profit hero number | p1 / `kpi_profit_naive` | native cardVisual ×2 variants | paired variants so alt text is state-specific |
| 25 | Strike-through across the value | p1 | native basicShape + bookmark | fades in; never draws |
| 26 | `MISREAD — see notes` tag | p1 | native textbox + bookmark | |
| 27 | 100-ticket waffle with punch holes | p1 / `dn_ticket_waffle` | **dn-deneb** | **contracted fallback: native 100 % stacked bar** at the same rect |
| 28 | Perfect-tens leaderboard | p2 / `tbl_perfect_tens` | native tableEx | |
| 29 | Poster thumbnails 32 × 44 | p2 | native Image URL column + `[Image · Poster URL]` | real TMDB posters — data, not decoration; base URL **VERIFY-AT-BUILD** |
| 30 | Raw → weighted dumbbell + C line | p2 / `dn_rating_fall` | **dn-deneb** | **contracted fallback: native paired bars** (`clusteredBarChart`) |
| 31 | Premiere scatter, log X, C line | p3 / `hero_premiere_scatter` | **native scatterChart** | satisfies the ≥1 core-visual rule |
| 32 | Year-by-year population | p3 | **native scatter play axis** | the entrant's "scatter plot animation", real and native |
| 33 | 28 pt year readout | p3 | native (play-axis own label) | the custom textbox is an **accepted omission** — the native control renders it |
| 34 | `▶ PRESS PLAY` button | p3 | native play-axis control | custom button an **accepted omission** |
| 35 | Scatter dim at SC.1/SC.2 | p3 / `z_p3_scrim` | native basicShape at 65 % transparency + bookmark | PBIR has no visual-opacity property; a scrim is the honest mechanism |
| 36 | Winner ring | p3 | **replaced** — `[Color · Scatter mark]` + `c_winner_label` | a ring cannot be a static shape over a data-driven position |
| 37 | Four adjustment chips, 8 px radius | p3 | native basicShape ×4 + textbox ×4 | chip height 22 px (prototype's 24 overflowed the card by 9 px) |
| 38 | Refusal card, 2 px trap border | p3 | native basicShape | |
| 39 | Refusal rank rows with `✕` | p3 / `tbl_refusal_ranks` | native tableEx | live top-3 by popularity rank |
| 40 | Refusal `@ build` placeholder line | p3 | **accepted omission** | superseded by the live table (#39) |
| 41 | No-date chip, 8 px radius | p3 | native basicShape + cardVisual | |
| 42 | Verdict lines, Georgia italic | p1·p2·p3 | native textbox ×1 per page | |
| 43 | Credits cast rows with dot leaders | p9 / `c_cr_cast` | native textbox, literal dot-leader runs | no numbers → full fidelity |
| 44 | Credits counts + parameters with dot leaders | p9 | native tableEx ×2 | dotted gridline **VERIFY**; solid `#57534E` is the accepted fallback |
| 45 | Glossary with `[TRAP]`/`[HONEST]`/`[OPAQUE]` tags | p9 | native textbox, coloured runs | tag word + colour |
| 46 | `SCENES DELETED` list | p9 | native textbox | verbatim from the not-available list |
| 47 | Closing block (source + sign-off) | p9 | native textbox ×2 | |
| 48 | `⌂ BOX OFFICE` button | p9, act headers | native actionButton | |
| 49 | Tooltip card 320 × 420 | tooltip | native tooltip page | |
| 50 | Tooltip poster 170 × 240 | tooltip / `img_tt_poster` | native image + `[Image · Poster URL]` | omitted wholesale if the base URL cannot be verified |
| 51 | Tooltip dot-leader rows | tooltip / `tbl_tt_rows` | native tableEx | |
| 52 | Tooltip `†` footnote | tooltip | native textbox | |
| 53 | Page backgrounds (night / paper) | all | theme `page.background` + per-page override on p1/p2 | |
| 54 | Focus outlines | all | native Power BI focus indicator | never overridden; audited at G6 |
| 55 | `prefers-reduced-motion` honouring | all | native | the only motion is the bookmark tween and the play axis, both native; the play axis opens on its resolved state so nothing essential is in motion |
| 56 | Hover tint on tickets/buttons | p0, all | native actionButton hover state | 1 px outline, no fill change |

**Contracted fallbacks (not cuts — build these if the primary route fails):**
`html_ticket_tear` → pre-torn stub art (#8) · `dn_ticket_waffle` → 100 % stacked bar ·
`dn_rating_fall` → paired bars · dashed perforation → drawn inside the stub SVG ·
dotted credits gridline → solid `#57534E` · `[Image · Poster URL]` → no posters
anywhere.

**Pre-approved cut list, in order** (ack table row 9 — cut from the top when the clock
runs out; no re-litigation needed):

1. **The HTML Content tear** → the pre-torn stub (already the default; zero risk).
2. **`dn_rating_fall`** → native paired bars.
3. **Three beats → two** on p1 and p2 (merge SC.2's notes into SC.3; the M-003
   marking at SC.1 survives untouched — it is never cut).
4. **Tooltip and leaderboard posters** → table-only tooltip, no image column.
5. **The credits sign-off joke line** (`c_cr_close_last`) — free to cut.

---

## Corrections applied to the prototype

The prototype is the layout truth. Four semantic points are corrected here, each for a
stated rule; none of them moves a rect.

1. **Waffle "VALID" cells go green, not red.** The prototype fills the 13 valid
   tickets with trap red `#B3402E` and captions them `red = VALID`. Those 13 are the
   *honest* subset, so under hard rule 3 they must carry the honest token. Valid cells
   are now `#2F6B4F`, the caption reads `green ✓ = VALID (13)`, and the filled-vs-
   outline shape difference remains the non-colour carrier.
2. **Trap red is semantics-only; it is never chrome.** The prototype paints buttons
   (`.btn`), the night-page accent and the winner ring in `#B3402E` / `#E8705F`.
   Buttons and rails now use surface ink (`#211E1A` paper, `#F2EFE6` night). Trap red
   survives in exactly three places: the trap number's strike and tags, the `✕` marks,
   and the refusal card's border — all of which *are* refusals.
3. **The winner reads honest, not alarming.** The `#E8705F` ring becomes an honest
   `#4ECBA0` mark via `[Color · Scatter mark]`, plus a `✓` in `c_winner_label`.
4. **Act tints applied.** The prototype predates the entrant's 2026-08-05 tint
   decision. Ticket rules and serials, ADMIT ONE glyph strokes, beat-rail current
   fills, header rules, verdict rules and the act-numeral runs now carry the act tint;
   nothing else does.

Two numeric corrections, from unresolved decision #1 defaulting to the *filter-true*
basis: the denominator is **84,036**, not 85,394, and coverage reads **13.2 %**, not
13.1 %. Every affected string is bound live rather than typed (see the placeholder
batch in `data-model.md`); 85,394 survives only as the end-credits' `LISTINGS PER
SOURCE` row.

---

## Manual steps expected in Desktop

`BUILD_LOG.md` confirms or extends this list at stage 6.

- [ ] Import `theme.json` (View → Themes → Browse) and confirm no base-theme
      regression banner; verify the 10 pt text classes took.
- [ ] Set the report-level filter `Movies[Adult] = FALSE`, then **lock it and keep the
      filter pane visible**.
- [ ] Author the two Deneb specs (`dn_ticket_waffle`, `dn_rating_fall`) in the Deneb
      pane; PBIR can carry the container but not the Vega-Lite spec.
- [ ] Set the poster column's data category to **Image URL** and paste the
      **VERIFY-AT-BUILD** TMDB base URL into `[Image · Poster URL]`; record the URL
      and its source in `BUILD_LOG.md`.
- [ ] `hero_premiere_scatter`: put `'Release Year'[Year Label]` in the **Play axis**
      well, set the X axis to **logarithmic**, add the **constant line at 6.96** in
      the Analytics pane, and leave the play head on the latest year.
- [ ] Bind every alt text via **fx → Field value** to its `06 Display\Alt text`
      measure (after the attribution blocker is cleared).
- [ ] Capture the nine beat bookmarks with **Data OFF / Display ON / Current page ON**.
- [ ] Verify tab order in the Selection pane matches the enumerated order above.
- [ ] Confirm the dashed line style on `z_ticketN_perf` and the dotted horizontal
      gridline on the two credits tables; fall back as contracted if unavailable.
- [ ] Confirm Bahnschrift SemiCondensed, Consolas and Georgia render in the Service
      (web) as well as in Desktop; if any does not, the documented fallback stack
      applies and the substitution is logged.
- [ ] Verify at s6 entry: `Genres` and `Production Company` returned from the stage-4
      round-trip carrying `PBI_ResultType = Exception` annotations — confirm both
      tables have plausible row counts before building on them.

---

## Fidelity checklist (from the creative-direction contract)

- [ ] Key Takeaway verbatim on the p0 marquee; the three tickets are the only nav and
      each names its act and its teaser stat.
- [ ] Every SC.1 naive beat carries the M-003 equivalent marking (slug + "naive cut"
      tag + beat rail 1/3); strikes and corrections land at SC.3.
- [ ] Act III's hero is the **native play-axis scatter**, with population and
      parameters printed on canvas, the popularity refusal card present, and the
      no-date chip visible.
- [ ] End-credits method page: cross-foot 85,394 − 1,358 = 84,036, glossary with
      TRAP / HONEST / OPAQUE tags, SCENES DELETED refusals, TMDB credit.
- [ ] Per-act film-stock tints applied to **chrome only** per the scope rule (no
      tinted data marks); ≤ 6 hues per page; 0 px surfaces with 8 px tickets and
      chips; and the full accessibility package (tab orders, state-specific alt text,
      focus outlines) as contracted.

---

## Rejected paths

Recorded so no later session resurrects one as a fresh idea. Do not re-litigate
without new requirements.

- **D1 The Projection Room** (52/70) — rejected by the entrant: "don't look and feel
  movie related"; also the most crowded dark-cinema lane and a Deneb-dependent
  signature.
- **D2 The Working Papers** (54/70) — same rejection; its own failure mode was a
  Creativity ceiling: the signature is retold as an idea, not seen as an image.
- **D3 Front Page / Corrections** (49/70) — same rejection; structurally, the lie was
  typeset larger than the truth and compact blocks pressed the 10 pt floor.
- **D4 The One-Sheet** (55/70) — "still not sold on any"; the AI key-art slot risked
  cheapening the sheet and 320 px of chrome raised the insight burden.
- **D5 The Contact Sheet** (56/70) — same; two compression points against a manual
  accessibility judge, and one SVG chrome dependency per page.
- **D6 Main Titles / End Credits** (52/70) — same; landing insight density too low,
  and Lie 2 lost its scatter to a dumbbell.
- **A poster-wall cover for D7** — declined by the entrant on 2026-08-05: the cover is
  the ticket booth. Real TMDB posters stay only where they carry data (the Act II
  leaderboard and the tooltip).
- **A single ticket-red accent with no act tints** (D7 ack table row 7's original
  default) — superseded on 2026-08-05 by the entrant's approved act-tint exception.
