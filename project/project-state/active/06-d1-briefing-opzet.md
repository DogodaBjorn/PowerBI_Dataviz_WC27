# 06 - Back to D1: the briefing, stripped (comp v2)

**Date:** 2026-11-07 · **Decided by:** Björn ("Dit is een investor deck geen speeltuin ... terug naar een
simpel doeltreffend rapport. Geen onnodig poespas.") · **Stage:** 0, pre-gate opzet pass. This file
supersedes the P1 page map of `05-doorlichting-nieuwe-opzet.md` §2 and closes its open question 1.

## Decisions

1. **Basis: pitch D1 "Wake-up call", stripped.** P1 is a Board briefing: a message headline, four
   benchmarked KPIs, three findings with one chart each, and where we are full. No plan builder, no
   promise-ladder table, no overlays, no signature ornaments. D2 is dropped (an operations wall, not an
   investor deck); D3 lends nothing but its stance on stated uncertainty.
2. **Recommendation (closes 05 open question 1): package A, "fund the three moves that pay".**
   01+02+10 (booking app, kiosks at 20 desks, revenue management), $9.4 M, NPV through 2032
   +$3.3 M Expected (Low -$5.5 M, High +$12.7 M), +$3.5 M operating profit a year by 2032.
   The other $50.6 M is held back. B and C are shown as "considered, not recommended".
3. **P2 keeps the package scatter and the focus swap** (Björn, 7 Nov: "houden zoals bedacht"). The
   scatter gets one fixed Y axis for all three scenarios, a "pays back by 2032" zone, light dots, and
   labels only on A, B and C. The shortlist state becomes one recommendation block plus the alternatives.
   No tile shapes on top of content (the cause of the empty preset boxes in Desktop on 6 Nov).

## Page messages

- **P1:** "Full rooms, a slipping margin: Goodnight Inn pays the middleman and is losing its guests."
  - F1 margin before vs after commissions; the gap grew every year.
  - F2 OTA share plus the folio: one room night, the guest pays the same, the inn keeps $89.64 vs $107.09.
  - F3 NPS by years since the last renovation.
  - F4 airports are the fullest.
- **P2:** "Fund the three moves that pay: $9.4M now, $50.6M held back."

## Facts added (project/analysis/41_opzet_facts.py, regenerated from the starter .pbix)

- **Folio 2025 (MISSION E8):** both channels reproduce E8 exactly.
  - OTA: the guest pays $109.31, fees are $19.68, the inn keeps $89.64.
  - Direct web and app: the guest pays $111.56, fees are $4.46, the inn keeps $107.09.
- **Channel-mix counterfactual (E7):** $4.81 M more distribution cost in 2025 than at the 2021 mix.
- **NPS by years since the last renovation (E10):** dated hotels only, weighted by SurveyResponses
  (the project convention).
  - Results: +6.8 for 14 hotels / +3.8 for 20 / -4.9 for 10.
  - E10 recorded +6.8 / +4.0 / -4.6. The 6-9 and 10+ bands differ by 0.2-0.3 points, which is
    attributed to the weighting; the canvas uses the weighted figures.
  - Occupancy is 79-80 % in every band.
- **Unchanged facts:** every existing key in `opzet-data.json` reproduces within float noise from the
  .pbix export.

## Text budget (per page)

- **Titles:** findings with a verb, one line.
- **Subtitles:** one line.
- **Footer:** one source line.
- **Uncertainty:** stays on the canvas as one sentence.

## Status (7 Nov, night)

- **Approval:** Björn approved the comp ("Yes go ahead and build. With precision").
- **Built:** the model, the report and the comp. The comp now follows the report one to one: no point labels on the
  scatter, no pays-back zone, and texts word for word from the measures. See `project/deliverables/BUILD_LOG.md` for
  the item list.
- **Verified in Desktop:**
  - The model loads with 0 partition errors.
  - Every number on both pages equals the offline facts.
  - Both pages and the P2 plan state rendered.
- **Found and fixed in Desktop:**
  1. NPS rank shown as "3rd of 4". Floating-point noise counted Goodnight Inn as better than itself; it is now
     excluded from its own count.
  2. `FORMAT()` with `,,` scaling did not scale. Text measures now divide explicitly.
  3. `USDM1` / `SUSDM` used the wrong comma position for .NET scaling.
  4. Axis display units doubled the scaling ("$0MM").
  5. Button text did not render. `show` now sits outside the state selector.
  6. Card visuals drew white fills of their own.
  7. The background image drifted off the visuals when Desktop scaled the canvas non-uniformly. Cards and logo are
     visuals now.
  8. A stale background was copied because Edge wrote its PNG late.
  9. The plan table's chips were too tall.
- **Still owed (Björn):**
  - The focus-swap click test (`03-focuswissel-testplan.md`).
  - A full-size review on a normal screen.
  - Publish to Web at 1920 and 1366 wide.
