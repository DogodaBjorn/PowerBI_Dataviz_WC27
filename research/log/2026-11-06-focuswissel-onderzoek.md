# Scout: focus swap on the P2 investment page (bookmarks, Deneb, HTML Content) - 2026-11-06

**Trigger:** Björn asked (6 Nov) how the P2 package scatter should move between an
overview and a plan state - whether a smooth morph is possible - and supplied two
external research reports (a WhatsApp PDF at 16:13 and a ZIP with report plus
proof pack at 16:17) to check against our own findings. Decision output:
`project/project-state/active/02-focuswissel-methode.md`, test gate in
`03-focuswissel-testplan.md`, execution pattern in `.claude/skills/fx-focus/`.

**Sources consulted (fetched and read 6 Nov 2026):**

- Microsoft Learn, report bookmarks:
  https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-bookmarks
- Microsoft Fabric Community thread 3466549 (bookmark clears cross-selection,
  answer cites the same Learn page):
  https://community.fabric.microsoft.com/discussions/power-bi-designer/data-changes-as-a-result-of-switching-between-bookmarks-even-though-data-is-not-/3466549
- Vega porting guide (Vega 2 to 3):
  https://vega.github.io/vega/docs/porting-guide/
- Vega-Lite issue 9590, "Enable linear interpolated animations" (open, 2025-04):
  https://github.com/vega/vega-lite/issues/9590
- Deneb 1.1 performance docs (SVG default, canvas optional):
  https://deneb-viz.github.io/1.1/performance
- Deneb PR 683 (data-reduction window 10,000 to 30,000, merged):
  https://github.com/deneb-viz/deneb/pull/683
- Deneb issue 374 (Continuous View / Data Patching in 2.0, closed 2026-08):
  https://github.com/deneb-viz/deneb/issues/374
- HTML Content docs, interactivity and sanitization:
  https://html-content.com/docs/interactivity and
  https://html-content.com/docs/sanitization
- Round 1 blog post (no page limit stated; "at least four built-in visuals" is):
  https://community.fabric.microsoft.com/blog/community_blog/power-bi-dataviz-world-champs-2027--round-1/5390883
- Two external research reports supplied by Björn (6 Nov): the first overclaimed
  (a built-in Deneb/Vega morph; "HTML Content Secure has no interaction"); the
  second (ZIP, with sources) confirmed our line and is the origin of the
  claim-status framing below. Neither overrides owner documentation.

## Findings: claim status

| Claim | Status | Basis |
|---|---|---|
| Bookmarks capture filters, slicers, visibility, spotlight; Data / Display / Current page / Selected visuals options exist | confirmed | Learn desktop-bookmarks |
| Applying a bookmark clears previous cross-filters and cross-highlights ("by design") | confirmed | community 3466549 answer, citing Learn |
| A native morph or animated transition between bookmarks/layout states exists | not found, not documented | no such feature in Learn docs |
| Vega has a built-in interpolation/transition engine | refuted for Vega >= 3.0 ("Animated transitions are not currently supported") | porting guide |
| Vega-Lite supports linear interpolated animation | not available; animation is discrete frame animation; linear interpolation is an open enhancement | vega-lite 9590 |
| Deneb offers a canvas renderer and handles hundreds of points within its data window | confirmed (SVG default, canvas option; categorical window 30,000 rows) | Deneb 1.1 performance docs, PR 683 |
| Deneb 2.0 Continuous View / Data Patching patches data updates without a full redraw | confirmed ("prevents redraw on data changes (including cross-filtering)"); it is not animation | Deneb 374 (dm-p, closed 2026-08-18) |
| HTML Content Secure blocks all interaction | refuted; scripts are sanitized but row selection styling, tooltips and restricted SMIL/CSS animation are supported | html-content.com interactivity + sanitization docs |
| HTML Content Regular scripting is formally supported | refuted by the maker's own docs; animations stay inside the visual's frame | html-content.com docs |
| A custom visual can resize neighbouring native visuals | no supported method found | Power BI visual API surface (no host-layout write access) |
| Power BI Embedded customLayout can reposition visuals | confirmed, but unavailable under Publish-to-Web, so not a contest route | Embedded docs (via second external report) |
| The Round 1 blog limits the entry to two pages | not stated there; the starter Read Me is the source (`project/contest/page-count-ruling.md`) | blog 5390883 |

## Decision

Route A (native, display bookmarks, disconnected single-select selector,
highlight-by-measure) is the base; route B (one persistent Deneb visual with an
internal focus state) is a parked upgrade behind a real test; route C (HTML
Content Regular as architecture) is on hold. No morph is promised anywhere. The
method is recorded in `project/project-state/active/02-focuswissel-methode.md`
and becomes proven only through `03-focuswissel-testplan.md`.

## Ring moves (radar updated 2026-11-06)

- **trial:** focus swap via display-only bookmarks + disconnected selector +
  highlight-by-measure (owner: fx-focus skill; first project use decides).
- **assess:** Deneb 2.0 Continuous View / Data Patching for one persistent
  custom visual (route B spike in the test plan).
- **hold:** native morph between bookmarks (not a documented feature); HTML
  Content Regular as page architecture (own-frame animation, scripting not
  formally supported, certification/export risk).
