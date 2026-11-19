# 00 — Intake

**Classification:** new-build (contest entry, starter model provided).
**Deadline:** Aug 7, 2026, 11:59 p.m. PT — hard. Express lifecycle per
`project/MISSION-wc-round-3.md`; contract in `active/intake.contract.yaml`.

## The request, distilled

Build the Round 3 entry through the toolkit as its first full stress test.
Round theme (binding, from the organizers): **Using data responsibly** —
understand limitations, question assumptions, communicate uncertainty, avoid
misleading conclusions. Mark outliers; explain probability; correlation ≠
causation. The theme must *sing through* the report, not sit in a footnote.

## Feasibility and the big opportunity

The starter PBIP is already star-shaped (Movies + Date + Genres/Keywords/
Production Companies via bridges + _Measures) — stages 3–4 are light. The
theme is a direct hit on this toolkit's core doctrine: metric contracts,
do-not-fabricate lists, and evidence gates ARE responsible data use. The
report can demonstrate the discipline it preaches.

Concrete hook found at intake: the starter ships
`Profit = SUM(Revenue) − SUM(Budget)` — on TMDB data where Budget/Revenue
are widely zero-filled, that measure is *exactly the kind of misleading
conclusion the round warns about*. "The naive answer vs. the responsible
answer" is a candidate story spine for s1.

## Risks

1. **Time.** Three days. Mitigation: express gates, px-prototype comps for a
   fast visual decision, waivers recorded in the mission file.
2. **Theme done preachy.** A lecture about data ethics scores worse than a
   report that *shows* it (honest axes, visible uncertainty, labeled
   outliers, an unanswerable question answered with "the data cannot say").
   s5 doctrine must carry this.
3. **Unverified round details.** Key Takeaway requirement + external-join
   rules came via search snippets; the announcement post blocks agents.
   30-second browser check by the entrant closes this.
4. **Profiling depth.** Data lives in the model cache, not on disk. Real
   row-level profiling needs Desktop open + the Modeling MCP (installed), or
   the Kaggle CSV. Until then, claims about data quality stay hedged — which
   is itself on-theme.

## Open questions (block G1, not G0)

- Which story spine: (a) "the naive vs. responsible read" (Profit trap,
  vote-count reliability, popularity opacity), (b) "what makes a movie
  succeed — and what the data cannot tell you", or (c) another angle s1
  surfaces. Decide at s1 with profiling evidence.
- Any external join needed, or does the starter carry the story alone?
- Single landing page + detail page(s), or one dense page? (Starter has 2
  pages; no page-count rule found — verify none exists.)
