# 01 — Requirements & story angles

Audiences and traced requirements: `active/requirements.contract.yaml`.
The judges score four criteria in minutes; every requirement maps to a
scoring decision. The round theme (**Using data responsibly**) is the story,
not a constraint on it.

## What the model offers (verified schema, unverified contents)

One row per movie: Title, Release Date, Budget, Revenue, Runtime,
Vote Average, Vote Count, Popularity, Status, Adult, Original Language —
bridged to Genres, Keywords, Production Companies; day-grain Date table;
7 relationships; one starter measure (`Profit`), which is naive on this data.

Known-by-reputation, to verify by profiling (Q2): Budget/Revenue widely
zero-filled; Vote Count heavily right-skewed (most movies have almost no
votes); Popularity is an undocumented internal score; duplicates and
future-dated rows exist.

## Three candidate story angles (pick one — Q1, blocks G1)

### Angle 1 — "Anatomy of a misleading number"
The Profit trap as the spine. Act 1 (landing): the seductive chart everyone
makes — profit/ROI by year or genre, computed naively over all rows — shown
*as the trap*. Act 2: the coverage funnel (1M movies → the sliver with real
financials), the honest recompute on credible rows, outliers named (the
blockbusters that drag means), median-not-mean. Key Takeaway states what we
can honestly claim about movie economics — and what we refuse to.
*Strengths:* razor-focused, self-demonstrating, the starter's own measure is
the villain. *Risk:* financial focus uses a small slice of the data.

### Angle 2 — "The confidence of crowds"
Uncertainty as the spine, via ratings. A 9.2-rated movie with 11 votes vs a
7.8 with 30,000: which is "better"? Funnel of Vote Average vs Vote Count
(variance visibly shrinking with sample size), shrunk/weighted ratings vs
raw ones, genre comparisons with honest spread, budget-vs-rating scatter
that shows a correlation and explicitly refuses the causal reading.
Key Takeaway about when a rating deserves belief.
*Strengths:* probability/uncertainty made visual (the theme's hardest ask,
done natively); uses the whole dataset. *Risk:* needs careful design to stay
instantly readable for a minutes-long judge pass.

### Angle 3 — "Three seductive lies about the movies"
The fusion. One act per lie, each seductive chart shown small and struck
through, the responsible read beside it: (1) "The industry loses money" —
zero-filled financials; (2) "This obscure film beats The Godfather" —
tiny-sample ratings; (3) "Popularity says what's good" — an opaque score
nobody can define. Landing page carries the Key Takeaway as the moral:
*the data is not wrong — the reading is.*
*Strengths:* contest-shaped (creative structure, punchy landing, natural
signature moment; covers outliers + uncertainty + correlation/causation
across the lies). *Risk:* three acts in limited time — scope must stay
one-page-per-lie disciplined, or one dense landing + one detail page.

## Recommendation

Angle 3 for the win conditions (Creativity + Insightfulness scoring), with
Angle 1's coverage funnel and Angle 2's vote-count funnel absorbed as its
acts — they are the same material, arranged as a story. If time collapses,
Angle 1 alone is the safe, complete entry.
