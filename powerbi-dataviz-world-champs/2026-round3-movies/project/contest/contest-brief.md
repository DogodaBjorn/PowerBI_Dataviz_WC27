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

## ⚠ CORRECTED 2026-08-05 — the facts below supersede everything above

The table in the original draft was assembled from search snippets and an in-session
relay, and **four of its rows were wrong**. Corrected against the Round 1/2/3
announcement pages and the judging explainer (retrieved 2026-08-05). The
"Using data responsibly" quote above is genuine but describes the **Responsible Data
Use criterion**, not the round's question. **The question the entry must answer is
"What makes a movie successful?"**

## Hard facts (verified 2026-08-05)

| Fact | Value | Source |
|---|---|---|
| **Round question** | **"What makes a movie successful?"** on the TMDB data | Round 3 announcement |
| **Window** | July 28 → **closes 9 August 2026** (was recorded as Aug 7 — WRONG) | Round 3 announcement |
| **Judging** | **SIX** criteria, not four: Insightfulness · Visual Effectiveness · **Storytelling and Communication** · Creativity and Innovation · Accessibility · **Responsible Data Use** | Round 3 announcement |
| **Core visuals** | **"Include at least three core Power BI visuals"** — a hard rule, stated identically in rounds 1, 2 and 3 (was recorded as "one" — WRONG) | Rounds 1–3 announcements |
| **Pages** | **Maximum 5**; hidden tooltip pages are allowed and do not count | Round 3 announcement |
| **Key Takeaway** | Visible, **≤50 words**, on the landing page | Round 3 announcement |
| **Accessibility** | ~25% of score; **entries under a 50% accessibility score are INELIGIBLE** to win or be a judge's favourite; a dedicated judge tests **tab order, alt text and colour contrast by hand** | "How are Fabric Community Dataviz Contests Judged" |
| **Custom visuals** | **Explicitly allowed** — Deneb is named in the FAQ. Images and visual assets allowed; all external assets must be cited in the report | EU-edition FAQ, Round 3 "You CAN" list |
| **External data** | **PROHIBITED** — no external datasets, no joins to IMDb / Wikipedia / Rotten Tomatoes / Box Office Mojo / the TMDB API, no web scraping. (Earlier draft said these joins were ALLOWED — **WRONG**, and the inverse of the truth.) | Round 3 announcement |
| Entries | One per round, per person | rules PDF |
| Submission | "Submit to contest" in the Fabric Community Contests gallery | rules PDF |
| Dataset | TMDB movies, embedded in the starter pbix; the entrant's own Kaggle download is a **newer snapshot** (84,510 non-adult listings in partition) | contest repo + s6 reconciliation |
| **Judges' stated anti-goal** | *"We are not rewarding: the most complex model, the flashiest visuals, the densest pages."* | Round 1 announcement |

Sources (403 to agents; opened via search retrieval):
[Round 1](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Dataviz-World-Champs-Barcelona-Round-1/ba-p/5206333) ·
[Round 2](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Dataviz-World-Champs-Barcelona-Round-2/ba-p/5272049) ·
[Round 3](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Dataviz-World-Champs-Round-3/ba-p/5323477) ·
[How judged](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/How-are-Fabric-Community-Dataviz-Contests-Judged/ba-p/4781653) ·
challenge hub https://aka.ms/pbidvwc26

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
