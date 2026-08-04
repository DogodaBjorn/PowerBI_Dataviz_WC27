# Contest brief — Power BI Dataviz World Champs BCN 26, Round 3

Source of truth for stage 0. Facts verified 2026-08-04 against the official
rules PDF in this folder and the contest repo.

## Round theme (BINDING — from the organizers, relayed by the entrant 2026-08-04)

> "For Round 3, we're focusing on one of the most important skills a data
> professional can develop: **Using data responsibly.** The best analysts
> don't just create beautiful visuals. They understand the limitations of
> data, question assumptions, communicate uncertainty, and avoid misleading
> conclusions."

Practical translation for this build: mark outliers, communicate uncertainty
and probability honestly, show why correlation is not causation, name what
the data cannot say. The theme must be *shown* in the visuals and the story,
not lectured in a footnote. Every s2 metric contract's edge-case section and
the do-not-fabricate list are direct scoring assets this round.

## Hard facts

| Fact | Value | Source |
|---|---|---|
| Window | July 28 → **Aug 7, 2026, 11:59 p.m. PT** | rules PDF §schedule |
| Time left | ~3 days from kickoff (Aug 4) | — |
| Judging | 10 pts each: Insightfulness · Visual Effectiveness · Creativity & Innovation · **Accessibility** (40 total) | rules PDF §judging |
| Entries | One per round, per person | rules PDF |
| Submission | "Submit to contest" in the Fabric Community Contests gallery; challenge details at https://aka.ms/pbidvwc26 | rules PDF |
| Dataset | TMDB movies (~1M movies), embedded in the 54MB starter pbix (`World Champs BCN 26 - Round 3.pbix`, this folder) | contest repo |
| Kaggle original | https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies — only needed if reshaping in Power Query; no kaggle CLI on this machine (manual download) | round-3 post |
| External data | Joins to IMDb / Wikipedia / Rotten Tomatoes / Box Office Mojo / TMDB API **allowed**; enhancing the data itself is **not** | round-3 post (via search; verify at aka.ms/pbidvwc26) |
| Mandatory element | Visible **Key Takeaway statement on the landing page** — the headline of the story | round-3 post (via search; verify) |
| Announcement post (403s for agents — open in browser to re-verify the two rows above) | https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Dataviz-World-Champs-Round-3/ba-p/5323477 | — |

## Judging criteria → toolkit mapping

- **Insightfulness** → s1/s2 discipline: real questions, metric contracts, the
  Key Takeaway IS the story headline (copy-polish sweep applies).
- **Visual Effectiveness** → s5 three comps (px-prototype), craft floor,
  dataviz-polish showpiece tier, pbir_detect clean.
- **Creativity & Innovation** → signature moment per the design doctrine;
  deneb-studio for bespoke marks; imagery-studio for an on-theme cover.
- **Accessibility** → a11y-studio full audit (check_contrast core + ax-audit)
  is NOT optional here — it is 25% of the score.

## Round 2 lessons that bind here (from hp-world-champs)

1. Design in HTML first, then recreate pixel-perfect — never let s5 stay prose.
2. Deneb-first for pixel-critical charts.
3. Do-not-fabricate: TMDB data is messy (adult titles, zero-budget rows,
   duplicate titles) — profile before claiming anything.
4. Starter pbix → File > Save As > PBIP into `project/pbip/` is the first
   manual Desktop step (agents cannot open pbix).
