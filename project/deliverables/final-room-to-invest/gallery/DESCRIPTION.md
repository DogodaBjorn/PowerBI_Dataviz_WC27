# The gallery post: texts and images (16 Nov 2026)

Everything Bjorn pastes into the Contests Gallery form. Every number below is on the report as it stands
(`rebuild-finalv3`, the copy in `E:\Goodnight Inn - Room to Invest`). The rest of the account is in doc 35.

## The form, field by field

| Field | What goes in |
|---|---|
| Title | `Goodnight Inn: Room to Invest` (long form, if the field takes it: `Goodnight Inn: Room to Invest. 456 ways to spend $60M, and the best one spends $9.4M`) |
| Thumbnail image | `cover-a.png` (recommended), `cover-b.png` or `cover-c.png`; `cover-a-1920x1440.png` if the form wants 4:3 |
| Description | "The description" below; the first image in it `report-page1.png`, the second `report-page2.png` |
| Publish to Web URL | the link of the last publish (not stored in this repository) |
| PBIX | `Goodnight Inn - Room to Invest.pbix`, saved from the Desktop window after the gate |
| Category or tag | the official contest tag as the form offers it (earlier rounds: a category such as "World Champs ATL"); it is in no document here |

Alt text for the thumbnail, if the form asks for it:

> Cover of the entry Room to Invest for Goodnight Inn. Headline: 456 ways to spend $60M, the best one spends $9.4M.
> Beside it a cloud of 456 dots, one per investment package, falling from left to right; six dots lie above the line
> "pays back by 2032" and package A, at $9.4M, is marked as the highest.

## The teaser (first lines, about 60 words)

> **Goodnight Inn has the fullest hotels in the Pillow & Key Group. So why is its margin slipping?**
>
> My brand is Goodnight Inn, the group's budget brand of 50 hotels. The Board has $60M for it. I computed all 456
> investment packages the rules allow. Six pay back by 2032. The best one spends $9.4M. Think you can beat it? Page 2
> lets you build your own.

## The description (about 430 words)

> **Goodnight Inn has the fullest hotels in the Pillow & Key Group. So why is its margin slipping?**
>
> My brand is Goodnight Inn, the group's budget brand of 50 hotels. The Board has $60M for it. I computed all 456
> investment packages the rules allow. Six pay back by 2032. The best one spends $9.4M. Think you can beat it? Page 2
> lets you build your own.
>
> **Page 1 · The Wake-up Call: where the brand stands**
>
> Four findings, each ending in the investment option it leads to.
>
> - **I. The margin.** Occupancy is 79.4%, the best of the four brands. The operating margin after commissions still
>   fell 2.8 points since 2023.
> - **II. The middleman.** Online agencies now book 50% of room revenue, up from 33% in 2021. Same room, same night:
>   Goodnight Inn keeps $17.47 more when the guest books direct.
> - **III. The fading welcome.** Hotels last renovated ten or more years ago score an NPS of −4.9, and no renovation
>   has started since 2020.
> - **IV. Where we are full.** Five of the seven fullest hotels are airports.
>
> **Page 2 · Room to Invest: where the money goes, and why**
>
> One recommendation: fix the middleman first. $9.4M now pays for a booking app with member rates, revenue management
> and self check-in kiosks at the 20 busiest hotels. Together they add $3.5M a year to operating profit by 2032
> (NPV +$3.3M through 2032). The rest waits for one Board meeting in mid-2028, with the rule written down: $12.4M for
> 40 extra rooms each at Gatwick and Toronto if the first money worked, and $29.5M for a refresh of the ten oldest
> hotels only with a case beyond 2032. $8.7M is not needed and stays with the group.
>
> **Three things to try**
>
> - Switch between Low, Expected and High. Every number, sentence and alt text follows the case.
> - Open "What waits, and why". Each dot is one of the 456 packages; hover one to see what is in it.
> - Open "Build your own". Pick your moves within the $60M and see your plan against the recommendation.
>
> **How it is built**
>
> - Two pages and five tooltip pages, in native Power BI visuals only. The bars inside the table are images written
>   by DAX measures.
> - Only the provided data. The three cases are the dataset's own Low, Expected and High assumptions.
> - Every title states its finding. Each finding names the move that answers it, and each move names its finding.
> - Two yardsticks: NPV through 2032 at 8% in 2025 dollars, and "a year on cost" (operating profit added in 2032
>   divided by capex), because NPV counts nothing after 2032.
>
> **Accessibility**
>
> Alt text on every visual, rewritten for the case in view. A keyboard path through both pages. Text contrast at
> WCAG AA. No meaning in colour alone: lines differ by dash, marks by shape, and every line is named at its end.
>
> Best viewed full screen. Hover the ⓘ tags for detail; on a touch screen, press and hold.
>
> Data: Pillow & Key Group dataset, Power BI Dataviz World Champs 2027. Thank you to the organisers and the Contest
> Advisory Committee.

## Optional line: how it was made (Bjorn decides)

> **How it was made.** I built the report as a Power BI Project (PBIR and TMDL), with an AI coding agent doing the
> file work under my direction. 765 automated checks compare the numbers on the pages with the workbook.

The starter file allows AI-assisted design tools. The line is true and speaks to Creativity and Innovation; whether it
goes in is Bjorn's choice.

## Lines to add if a reviewer asks (from the draft of 15 Nov, still true)

- **Why A and not B.** The alternative with the breakfast upgrade instead of the kiosks earns $0.5M more a year, but
  less on its cost (34.0% against 37.5%) and $0.6M less through 2032.
- **The worst case.** In the Low case package A ends 2032 at −$5.5M and is still the best of the 456.
- **Why the refresh keeps a step.** It does not pay back by 2032 and earns just under our 8%. It stays at the gate
  because it is the one move that answers the fading welcome, and the data cannot price what waiting costs.
