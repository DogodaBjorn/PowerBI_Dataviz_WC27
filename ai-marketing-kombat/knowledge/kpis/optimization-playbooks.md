# Optimization Playbooks by Target KPI

Format per KPI: Diagnose | Levers by layer | Platform levers | Do NOT | Wait before judging | Trade-offs.
Platform features change fast; items marked [CHECK] should be verified in the live UI.

General order of attack: tracking sanity -> creative -> offer/landing/onboarding -> audience/placement -> bidding -> budget. Creative is the largest lever on Meta/TikTok; bidding/structure matter more on Google.

Learning-phase facts (approximate, [CHECK] current docs):
- Meta: ad set exits learning at about 50 optimization events in 7 days. Significant edits (budget change >~20%, bid, audience, new ad) can reset it.
- Google smart bidding: roughly 30+ conversions in the last 30 days per campaign is a common floor; more is better [CHECK]. Allow 1-2 weeks after strategy change (conversion lag longer for apps).
- TikTok: about 50 conversions per ad group to exit learning [CHECK]. Fatigue is faster than Meta.
- LinkedIn: slow, small volumes; judge on 2-4 weeks and use cost per qualified lead.

---

## 1. Lower CPM

- Diagnose: CPM by placement, audience size, country, device, creative (quality ranking), daily trend, seasonality (Q4, local events). Compare to platform benchmark ranges only as context.
- Levers
  - Audience: broaden (remove stacked interests/lookalike narrowing), larger geo, avoid heavy overlap between ad sets.
  - Creative: higher engagement lowers effective CPM (auction rewards expected action rate); native, platform-style formats.
  - Placement: allow automatic placements; check if Audience Network / low-quality inventory drives the low CPM but bad quality.
  - Bidding: lowest cost / no cap for volume; bid caps can throttle delivery and keep CPM artificially stable but starve reach.
  - Budget/timing: avoid peak competition windows when not needed; do not fragment budget across too many ad sets.
- Platform: Meta - consolidate ad sets, Advantage+ placements. Google - Demand Gen/YouTube reach formats cheaper than Search; TikTok - CPM varies strongly by market and creative vertical; LinkedIn - CPM structurally high, narrow B2B audiences push it up; widen job-function targeting before cutting.
- Do NOT: optimize CPM in isolation; low CPM with low CTR and CVR gives high CPA.
- Wait: 3-5 days or 50k+ impressions per ad set.
- Trade-off: cheap reach in low-intent placements usually raises cost per business event.

## 2. Raise CTR

- Diagnose: link CTR (not all-clicks) by creative, placement, format, hook rate, hold rate, frequency trend, first-3-second drop-off.
- Levers
  - Creative: stronger first 1-2 seconds, human faces/UGC, native look, clear single benefit, benefit-led caption, strong CTA, correct aspect ratio (9:16 for Reels/TikTok), text readable muted.
  - Offer: concrete, specific, with a number or a deadline.
  - Audience: better match between message and segment (segment-specific creatives).
  - Frequency: refresh before fatigue; CTR dropping while frequency rises = fatigue.
- Platform: Meta - test several distinct concepts, not 5 variants of one; TikTok - sound on, trend-native, Spark Ads (boost organic creator posts); Google - RSA headlines with the user's wording, assets per theme; LinkedIn - thought-leader ads, document ads, native lead forms.
- Do NOT: use clickbait, misleading hooks, or vague curiosity that attracts non-buyers. CTR up + CVR down = no gain.
- Wait: 1,000-2,000 impressions per creative for a rough CTR read; ~100 clicks for a stable CTR.
- Trade-off: broad-appeal hooks lift CTR and dilute intent. Judge CTR only together with CVR or IPM and cost per event.

## 3. Raise CVR (click to conversion; install to action)

- Diagnose: CVR by device, OS, country, source/placement, landing page, load time; compare click-to-landing-view (speed loss); form drop-off; tracking differences.
- Levers
  - Audience: exclude low-intent segments/placements that click but do not convert.
  - Creative: message match between ad and landing page/store listing; pre-qualify in the ad (price, who it is for).
  - Offer: clearer value, lower friction (guest checkout, fewer fields), social proof, guarantees.
  - Landing page / app onboarding: speed (<3 s mobile), single CTA, deep link to the right screen, reduced registration friction, show value before sign-up, first-ride/first-purchase incentive handled in-app.
  - Bidding: optimize for the downstream event once volume allows (e.g. install -> registration -> first ride).
- Platform: Meta - instant forms vs website (volume vs quality); App campaigns - optimize for in-app events (AEO) / value (VO); Google - landing page experience, search term to page match; TikTok - in-feed to landing page speed, avoid long forms; LinkedIn - lead gen forms prefilled lift CVR but may lower quality.
- Do NOT: change creative and landing page at the same time (cannot attribute); do not optimize CVR with a discount you cannot afford.
- Wait: at least 100 conversions per variant for a firm read, or run a proper A/B (see experiment-design.md).
- Trade-off: easier conversion usually = lower quality; check downstream (activation, SQL rate, retention).

## 4. Lower CPA (headline KPI)

- Diagnose: split CPA with the driver tree (CPM x CTR x CVR). Find the binding constraint (kpi-tree.md). Check tracking and attribution window mismatches first (a CPA that moved 2 days after a change may be pure lag).
- Levers
  - Audience: let the algorithm find buyers (broad), add exclusions of existing customers; lookalikes from high-value events, not from installs.
  - Creative: scale winners by concept, kill the tail. Most CPA gain comes from creative on social.
  - Offer: first-purchase/first-ride incentive sized by LTV, tested.
  - Landing/onboarding: reduce friction before the key event.
  - Bidding: optimize for the business event, not the proxy. Cost cap / tCPA near the achieved CPA, not below.
  - Budget: move budget from CPA > 1.5x target to CPA < target (see scale-stop-rules.md); keep a test budget.
  - Placement: remove placements with lots of spend and zero events.
  - Frequency: cap or refresh when high.
- Platform: Meta - consolidate, conversion event with enough volume (move up the funnel if <50/week), cost cap for control, Advantage+ audience/placements; Google - tCPA only with conversion volume, Performance Max/App campaigns asset quality and diversity, negative keywords for Search; TikTok - fresh creatives weekly, broad targeting, Smart+ campaigns [CHECK]; LinkedIn - cost cap or manual bid, tighten ICP, use lead forms plus offline conversion sync.
- Do NOT: judge CPA on <30 conversions per cell; cut creatives on early noise; set tCPA/cost cap well below achievable (delivery collapses); make many simultaneous changes.
- Wait: until conversions per decision unit meet the minimum (see scale-stop-rules.md) and the conversion lag has passed.
- Trade-off: lower CPA via bottom-funnel audiences (retargeting) is not scalable and often non-incremental.

## 5. Raise ROAS

- Diagnose: ROAS = AOV x CVR / CPC. Look at AOV, margin, return rate, new vs returning customer split, attributed vs blended (MER).
- Levers
  - Audience: prospecting vs retargeting split; value-based lookalikes; customer lists to suppress or expand.
  - Creative: show higher-ticket or bundle; product-level creatives for high-margin SKUs.
  - Offer: bundles, thresholds (free shipping at X), upsell, subscription.
  - Landing: product page quality, reviews, cart recovery.
  - Bidding: tROAS / value optimization with purchase value passed correctly (check value parameter).
  - Budget: shift to products/geos with best contribution margin; use POAS, not ROAS, for mixed-margin catalogs.
- Platform: Meta - Advantage+ sales campaigns, catalog; Google - Performance Max with product feed, feed quality (titles, prices, images); TikTok - Shop/Video Shopping ads [CHECK]; LinkedIn - not typical.
- Do NOT: set tROAS too high (starves delivery: spend falls, ROAS looks great, revenue falls); judge platform ROAS as truth (retargeting inflates it).
- Wait: purchase cycle length plus attribution window (7-14 days minimum for considered purchases).
- Trade-off: ROAS and scale move opposite ways; maximize contribution profit, not ROAS.

## 6. Lower CAC / improve payback

- Diagnose: CAC by cohort and channel, new-customer share, first-order margin, payback curve, discount dependency.
- Levers: raise first-order margin (bundles, higher AOV); push to cheaper channels via mix; improve onboarding and activation; speed up second purchase (lifecycle, CRM); annual plans/prepay for SaaS; reduce incentive cost; cut payroll-heavy steps (lead response time).
- Platform: use value-based bidding on predicted LTV where available (Meta value optimization, Google tROAS with LTV values) [CHECK feature availability].
- Do NOT: compare paid CAC with fully loaded CAC; chase cheap installs that never ride/buy.
- Wait: payback is by definition long; use early indicators (D7 activation, 30-day margin per cohort).
- Trade-off: shorter payback often = smaller cohorts and lower total growth.

## 7. Raise LTV

- Diagnose: retention curves by acquisition source/creative/cohort, repeat rate, order frequency, margin per period, churn reasons.
- Levers: acquire higher-quality users (value-based targeting, exclusions of promo-hunters); onboarding and first-value moment; CRM/push/email lifecycle; loyalty, subscription, cross-sell; pricing; reduce churn (win-back, annual plans).
- Platform: send downstream events or value to ad platforms (CAPI/Events API/MMP postbacks) so bidding learns who retains; creative that sets true expectations.
- Do NOT: promise more than the product delivers; incentives that attract one-time users.
- Wait: 30-90 days of cohort data; use D7/D30 retention as leading indicators.
- Trade-off: LTV forecasts are assumptions; state them and sensitivity-test (+/-20%).

## 8. Raise reach efficiency (cost per unique reach, incremental reach)

- Diagnose: cost per 1,000 reached (CPMr = spend / reach x 1000), frequency distribution, overlap across ad sets/platforms.
- Levers: reach & frequency buying (Meta R&F, TikTok Reach & Frequency, YouTube reach campaigns); frequency caps (e.g. 2-4/week for awareness [CHECK vs category]); combine platforms with complementary audiences (e.g. YouTube + Meta + TikTok) and de-dup using a single-source panel or MMM; one big audience instead of many overlapping ones; shorter formats (6 s bumper) for reach.
- Do NOT: sum reach across platforms; chase reach with rising frequency.
- Wait: reach builds over the flight; judge on total flight, with a weekly pace check.
- Trade-off: cheap reach in wrong audience is waste; define the target audience first.

## 9. Raise brand lift

- Diagnose: study design (control vs exposed), question wording, sample, which metric moved (awareness, ad recall, consideration, intent), frequency band where lift builds.
- Levers: strong branding in the first 2-3 seconds, repeated distinct brand assets (logo, sound, colour), enough frequency (often 3+ in the window [CHECK]), longer or sound-on formats for recall, reach quality (right audience), consistent creative across channels.
- Platform: Meta/YouTube/TikTok brand lift studies need budget thresholds (minimum spend varies; [CHECK]). Use reach and frequency buying.
- Do NOT: judge brand with CTR/CPA; run a lift study on a tiny budget.
- Wait: end of flight; study results usually need the full flight and survey completes.
- Trade-off: branding-heavy creative can lower CTR; that is fine for brand objectives.

## 10. Improve lead quality

- Diagnose: lead-to-SQL, SQL-to-win, by source/campaign/form/creative; time to first contact; fake/low-intent lead rate.
- Levers
  - Audience: tighter ICP (job title, company size), customer-list lookalikes seeded from won deals, exclusion of competitors/students.
  - Creative/offer: qualify in the ad (price, requirements, who it is not for); gated content with higher commitment (demo vs ebook).
  - Form/landing: more fields or a qualifying question; use "higher intent" form types; email verification; CAPTCHA.
  - Bidding: optimize to SQL/qualified lead via offline conversion import (CRM -> Meta CAPI for CRM, Google offline conversions, LinkedIn conversions API) [CHECK naming].
  - Speed to lead: respond in minutes.
- Platform: Meta - higher intent form option, offline conversions; Google - offline conversion import with GCLID; LinkedIn - lead gen forms with qualifying questions, Matched Audiences; TikTok - instant form quality varies, add a qualifying question.
- Do NOT: report CPL as the success metric; keep optimizing to the lead event when SQL feedback shows low quality.
- Wait: 2-6 weeks for SQL/opportunity feedback; use a proxy (qualifying question answer, meeting booked) meanwhile.
- Trade-off: stricter qualification lowers lead volume and raises CPL while lowering cost per SQL.

---

## Cross-cutting trade-off table

| Push | Side effect | Check |
|---|---|---|
| CTR up with curiosity hook | CVR / activation down | CPA of the business event |
| tROAS / tCPA too tight | Delivery starves, spend drops | Spend vs budget, impression share |
| Narrow audience | CPM and frequency up | Frequency, CPM trend |
| Cheap CPI via incentive/rewarded | Retention and first-event rate down | Cost per key event |
| Budget +50% overnight | Learning reset, CPA spike | Step up 20-30% |
| More variants of same concept | Little new learning | Test new concepts, not tweaks |
| Retargeting focus | ROAS up, incrementality low | Holdout / MER |
| Optimize for shallow event | Volume up, quality down | Downstream rate |
