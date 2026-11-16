# The gallery post: texts and images (16 Nov 2026, night: the final cover, the native-visuals line, the fuller story)

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

## The description (about 880 words)

> **Goodnight Inn has the fullest hotels in the Pillow & Key Group. So why is its margin slipping?**
>
> My brand is Goodnight Inn, the group's budget brand of 50 hotels. The Board has $60M for it. I computed all 456
> investment packages the rules allow. Six pay back by 2032. The best one spends $9.4M. Think you can beat it? Page 2
> lets you build your own.
>
> **How I built it.** About 75% from my mobile phone with Claude, 20% with Claude on my laptop and 5% fine-tuning by
> hand. 100% native Power BI visuals, and even more passion to build something beautiful.
>
> **Page 1 · The Wake-up Call: where the brand stands**
>
> Four numbers open the page: occupancy of 79.4%, the best of the four brands; an operating margin after commissions
> of 33.7%, down 2.8 points since 2023; half the room revenue arriving through online agencies; and a net promoter
> score of +3.3, the lowest of the four and falling every year. Four findings explain them, each ending in the
> investment option it leads to.
>
> - **I. The margin.** Of the 2.8 points, commissions took 1.0 and running costs 1.8. Room rates rose no faster than
>   at the sister brands, so price does not absorb it.
> - **II. The middleman.** Online agencies book 50% of room revenue, up from 33% in 2021. Same room, same night: the
>   guest pays $2.25 more when booking direct and Goodnight Inn keeps $17.47 more. Nothing rewards the guest for it.
> - **III. The fading welcome.** Since 2018 the brand spent $1.0M per hotel on renovation, the other brands $5.9M to
>   $7.9M. Hotels last renovated ten or more years ago score an NPS of −4.9. An association, not proof of cause, and
>   the page says so.
> - **IV. Where we are full.** Five of the seven fullest hotels are airports. Toronto topped 90% occupancy in 17 of
>   the last 24 months.
>
> **Page 2 · Room to Invest: where the money goes, and why**
>
> Ten moves are on offer. Each gets two tests: does it earn more a year than our 8% cost of money, and does it pay
> back by 2032? The recommendation, package A, is the three moves that earn most on their cost: a booking app with
> member rates (47.0% a year), revenue management (32.0%) and self check-in kiosks at the 20 busiest hotels (20.6%).
>
> $9.4M now adds $3.5M a year to operating profit by 2032 and undoes half of what went wrong: distribution cost falls
> from 11.3% to 10.1% of room revenue, and the margin climbs back from 33.7% to 35.1%.
>
> The rest of the $60M waits for one Board meeting in mid-2028, with the rule written down. Step 2: $12.4M for 40
> extra rooms each at Gatwick and Toronto, if the first money worked and both hotels stay full. Step 3: $29.5M for a
> refresh of the ten oldest hotels, only with a case beyond 2032. $8.7M is not needed and stays with the group.
>
> The risk is on the page too. In the Low case package A ends 2032 at −$5.5M and still earns $1.0M a year by then.
> It is the best of the 456 packages in all three cases.
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
> - NPV through 2032 at 8%, in 2025 dollars, is the challenge's yardstick. It counts nothing after 2032, so every
>   move also shows what it earns a year on its cost.
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
>
> Enjoy reading! Questions, remarks and feedback are always more than welcome.
>
> Cheers,
> TrainerBjorn

## A shorter description, if the form limits the length (about 330 words)

Take the teaser, the two page sections without their bullet lists and without the paragraph on the risk, "Three
things to try" and the first two sentences of "100% native Power BI visuals".

## Lines to add if a reviewer asks (still true)

- **Why A and not B.** The alternative with the breakfast upgrade instead of the kiosks earns $0.5M more a year, but
  less on its cost (34.0% against 37.5%) and $0.6M less through 2032.
- **Why the refresh keeps a step.** It does not pay back by 2032 and earns just under our 8%. It stays at the gate
  because it is the one move that answers the fading welcome, and the data cannot price what waiting costs.
- **How the numbers were checked.** 765 automated checks compare the numbers on the pages with the workbook.
- **When it goes live.** Revenue management in July 2027, the app in October 2027, the kiosks in April 2028; package A
  is cash positive during 2031 in the Expected case.

## What the claims rest on (for whoever is asked)

- **100% native.** Read from the report's files on 16 Nov after the save of 22:42: 194 visuals, every `visualType` one
  of Power BI's own (81 cards, 69 text boxes, 9 buttons, 8 scatter charts, 6 line charts, 6 tables, 6 shapes, 3 images,
  2 slicers, 3 bar and column charts, 1 area chart); no `publicCustomVisuals`, no custom visual package.
- **"The three moves that earn most on their cost".** The first three rows of the table, ranked by "a year on cost"
  in the Expected case (47.0%, 32.0%, 20.6%; the fourth is 19.8%).
- **"Best of the 456 in all three cases".** Read from the model's Package table: package A has the highest NPV
  through 2032 in the Low, the Expected and the High case.
- **"Body text" in the accessibility paragraph** is deliberate: the orange dot between the two parts of the page
  label is 3.2:1 on the banner.
