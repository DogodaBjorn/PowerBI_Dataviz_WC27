# Ruling: how many pages the Round 1 entry may have

Question raised 2026-11-06: the Dutch review of 4 Nov sketches a five-page report; the
mission says exactly two. Which is right? This note quotes every official source
verbatim so the ruling can be checked by anyone without opening the files.

## The three sources, verbatim

**1. The Round 1 blog post** (`round-1-brief.txt`, community.fabric.microsoft.com article
5390883). It frames the task as two questions and lists five "things to remember". It
says nothing about pages:

> Choose one brand and build a Power BI report that helps the Board make smart
> investment decisions. Your report should answer two big questions: 1. The Brand
> Review … 2. The Investment Strategy …
>
> A few things to remember: Choose one brand. Use only the provided data. Include at
> least four built-in Power BI visuals. Design for your audience: the Board of
> Directors. Make accessibility part of your design.

**2. The Official Rules** (`official-rules-ATL-2027.pdf`, 5 pages). Dates, eligibility,
entry mechanics, judging criteria, prizes, legal terms. The word "page" does not occur
in a report sense; there is no page or visual rule.

**3. The starter file** (`PillowKey_Starter.pbix`, hidden page "Read Me", text box
`4a1d31d79ea7053d474d`, extracted from the report definition). This is the only source
that states a page count, and it is explicit:

> **Your Task**
> Page 1 – The Brand Review: Which brand do you lead, and where does it stand today?
> Page 2 – The Investment Strategy: How should the brand invest its budget up to the
> end of 2032, and why is this the right choice?
>
> **Submission Requirements**
> One brand only
> Power BI (.pbix) only
> **Exactly two visible report pages (hidden tooltip pages are allowed).**
> At least four core (built-in) visuals
> Meet accessibility expectations: labels, alt text, contrast, tab order

The same page also says, under "What You Can Do": *"Create measures, calculated tables,
and scenario parameters … Add helper tables (e.g., derived tables, indexes, field
parameters) … Use custom visuals, images, icons, themes, and AI-assisted design
tools."*

## Ruling

**Two visible report pages, named by the organisers as the Brand Review and the
Investment Strategy. Hidden tooltip pages are allowed.** The blog post and the rules
do not loosen this; they are silent, and the starter file is the organisers' own
instruction bundled with the challenge, which is what a judge will open.

What follows from it:

| Device | Allowed? | Basis |
|---|---|---|
| Two visible pages | required, exactly | starter Read Me |
| Hidden pages marked as **tooltip** pages | yes | starter Read Me, explicit |
| Hidden pages that are not tooltip pages (drill-through targets, "method" pages) | not mentioned; treat as **not allowed** | the only allowance named is tooltip pages; a hidden drill-through page is still a report page |
| Bookmark states, overlays and panels **within** a page | yes | not pages; a bookmark changes the state of a page |
| Slicers, buttons, field parameters, what-if (scenario) parameters | yes | starter "What You Can Do" |
| The starter's own hidden pages (Read Me, Judging Criteria, Overview) | delete before submission | they are not tooltip pages; leaving them hidden invites a count dispute |
| Page size | free (the starter is 1920 × 1080) | no rule |

The three direction sketches in `project/pbip/` (`D1-wake-up-call`, `D2-fifty-keys`,
`D3-two-futures`, 6 Nov) each have exactly two pages and comply; the merged direction
D4 (`PITCH-D4-what-if-merged.md`) is designed to the same rule, with tooltip pages
for depth.

The Dutch review's five-page sketch is a **narrative sequence**, not a compliant
layout. Its content survives the ruling: its pages 1–3 (paradox, cause, which hotels)
are the Brand Review; its pages 4–5 (the money, the plan) are the Investment Strategy.
Depth that does not fit goes into tooltip pages and in-page bookmark overlays.

## If any doubt remains

The blog post accepts comments; a one-line question there ("Are hidden drill-through
pages treated like hidden tooltip pages?") is the only way to get an authoritative
answer on the one grey area. Until answered, the build uses tooltip pages only.

*Prepared 2026-11-06. Sources filed in `project/contest/` and `project/data/`.*
