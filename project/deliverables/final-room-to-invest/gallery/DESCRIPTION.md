# The gallery post: texts and images (16 Nov 2026, night: the final cover and the native-visuals line)

Everything Bjorn pastes into the Contests Gallery form. Every number below is on the report as it stands
(`rebuild-finalv3`, the copy in `E:\Goodnight Inn - Room to Invest`). The account is in docs 35 and 40.

## The form, field by field

| Field | What goes in |
|---|---|
| Title | `Goodnight Inn: Room to Invest` (long form, if the field takes it: `Goodnight Inn: Room to Invest. 456 ways to spend $60M, built with 100% native Power BI visuals`) |
| Thumbnail image | `cover-final.png`; `cover-final-1920x1440.png` if the form wants 4:3 |
| Description | "The description" below; the first image in it `report-page1.png`, the second `report-page2.png` |
| Publish to Web URL | the link of the last publish (not stored in this repository) |
| PBIX | `Goodnight Inn - Room to Invest.pbix`, saved from the Desktop window after the gate |
| Category or tag | the official contest tag as the form offers it (earlier rounds: a category such as "World Champs ATL"); it is in no document here |

Alt text for the thumbnail, if the form asks for it:

> Cover of the entry Room to Invest for Goodnight Inn. Headline: 456 ways to spend $60M, the best one spends $9.4M.
> Under it a badge: 100% native Power BI visuals. Beside it two views of the report's second page: the 456 investment
> packages as a cloud of dots, and the recommended plan with its ten moves in a table and the $60M budget as one bar.

## The teaser (first lines, about 75 words)

> **Goodnight Inn has the fullest hotels in the Pillow & Key Group. So why is its margin slipping?**
>
> My brand is Goodnight Inn, the group's budget brand of 50 hotels. The Board has $60M for it. I computed all 456
> investment packages the rules allow. Six pay back by 2032. The best one spends $9.4M. Think you can beat it? Page 2
> lets you build your own.
>
> Built with 100% native Power BI visuals: no custom visuals, nothing to install.

## The description (about 510 words)

> **Goodnight Inn has the fullest hotels in the Pillow & Key Group. So why is its margin slipping?**
>
> My brand is Goodnight Inn, the group's budget brand of 50 hotels. The Board has $60M for it. I computed all 456
> investment packages the rules allow. Six pay back by 2032. The best one spends $9.4M. Think you can beat it? Page 2
> lets you build your own.
>
> Built with 100% native Power BI visuals: no custom visuals, nothing to install.
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
> **100% native Power BI visuals**
>
> Every one of the 194 visuals on the two pages and the five tooltip pages is Power BI's own: tables, line, bar, area
> and scatter charts, cards, slicers, buttons, shapes and text boxes. There is no custom visual in the file. The bars
> inside the table are drawn by DAX measures and shown by the native table; the highlighted rows, the tooltips and the
> three views of page 2 are formatting, report-page tooltips and bookmarks. So the report opens wherever Power BI
> does, with nothing to install and nothing for an admin to approve, and every visual keeps Power BI's own keyboard
> and screen-reader support.
>
> **How it is built**
>
> - Only the provided data. The three cases are the dataset's own Low, Expected and High assumptions.
> - Every title states its finding. Each finding names the move that answers it, and each move names its finding.
> - Two yardsticks: NPV through 2032 at 8% in 2025 dollars, and "a year on cost" (operating profit added in 2032
>   divided by capex), because NPV counts nothing after 2032.
> - One colour per decision: blue for what we fund now, dark blue and clay for the two later steps.
>
> **Accessibility**
>
> Alt text on every visual, rewritten for the case in view. A keyboard path through both pages. Body text, labels and
> numbers at WCAG AA contrast. No meaning in colour alone: lines differ by dash, marks by shape, a step is named in
> words beside its colour, and every line is named at its end.
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

## What "100% native" rests on (for whoever is asked)

Read from the report's files on 16 Nov after the save of 22:42: 194 visuals, every `visualType` one of Power BI's own
(81 cards, 69 text boxes, 9 buttons, 8 scatter charts, 6 line charts, 6 tables, 6 shapes, 3 images, 2 slicers, 3 bar
and column charts, 1 area chart); no `publicCustomVisuals`, no custom visual package. The "body text" wording in the
accessibility paragraph is deliberate: the orange dot between the two parts of the page label is 3.2:1 on the banner.
