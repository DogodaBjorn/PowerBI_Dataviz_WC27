# Google Ads (Search, Performance Max, Demand Gen, YouTube, App campaigns, Shopping)

Status: reference for 2-hour case rounds. Written 2026-10-23. [CHECK] = verify before relying on it. The case's own numbers beat everything below.

## 1. What it is good for
- Funnel role: captures existing demand (Search, Shopping, Brand) and creates/extends demand (YouTube, Demand Gen, Display, PMax, App campaigns across Play/YouTube/Search/Discover).
- Intent: Search = highest explicit intent (query). Shopping = high commercial intent. YouTube/Demand Gen = low to mid intent, visual discovery. PMax = mixed, algorithm decides surfaces. App campaigns = installs/in-app actions across Google inventory.
- Audience: effectively global reach; strong across devices; Android ecosystem (Play Store) is a direct app-install lever; YouTube is the largest video platform on mobile and CTV.
- Best for: lead gen, e-commerce, local, app installs (especially Android), brand defence, competitor conquesting, upper funnel video.
- Weak for: creating demand where no search volume exists (use Meta/TikTok/YouTube first), tight B2B firmographics (LinkedIn), social proof discovery.

## 2. Campaign structure & objectives (2025-2026)
- Campaign types: Search, Performance Max, Demand Gen, Video (YouTube), App, Shopping (standard, feed-only PMax), Display, Hotel/Travel, Local.
- Search:
  - Keyword match types: exact, phrase, broad. Current recommendation: broad match + Smart Bidding + good negatives and conversion signals; exact/phrase for control and brand.
  - AI Max for Search campaigns (rolled out 2025): keywordless/expanded matching using AI, text customisation, final URL expansion. Opt-in toggle in existing Search campaigns. Treat as test; compare against standard campaigns via experiment [CHECK scope/availability]. Dynamic Search Ads are being folded into AI Max [CHECK].
  - Responsive Search Ads (RSA): up to 15 headlines (30 chars), 4 descriptions (90 chars); pin sparingly; Ad Strength is a hint, not a KPI.
  - Structure: themed ad groups (keywords grouped by intent), brand vs non-brand split, high-intent vs generic, locations. Avoid over-fragmentation; Smart Bidding needs volume.
- Performance Max (PMax):
  - One campaign across Search, YouTube, Display, Discover, Gmail, Maps. Inputs: asset groups (images, videos, headlines, descriptions), audience signals (hints), feed (retail), conversion goals, budget, bidding.
  - Controls: brand exclusions, search themes (like keywords hints), account-level negative keywords, URL exclusions, location/time controls, channel performance reporting (search terms, placements) available since 2025 [CHECK extent], "new customer acquisition" goals.
  - Use a single asset group per distinct product/theme; add video (else Google auto-generates one).
  - Risk: cannibalises brand search and retargeting; inflates ROAS with brand/existing customers.
- Demand Gen:
  - Visual, social-style campaigns across YouTube (In-Feed, Shorts, In-stream), Discover, Gmail. Replaces Discovery and Video Action Campaigns (VAC). Supports lookalike segments, custom segments, Customer Match, product feed (shopping).
  - Good for: mid-funnel discovery, prospecting, A/B with Meta/TikTok-type creative. Use video + image; 9:16, 1:1, 16:9 assets.
- YouTube / Video campaigns: formats: skippable in-stream, non-skippable in-stream (15 s; up to 30 s in some inventory [CHECK]), bumper (6 s), in-feed, Shorts, Masthead (reservation), CTV. Goals via Video reach campaigns (VRC: efficient reach, non-skippable reach, target frequency) and Demand Gen for action. Brand Lift measurement on request.
- App campaigns (formerly UAC): goal = installs, in-app actions, in-app action value (tROAS), pre-registration, engagement (re-engagement). Inputs: text, images, videos, HTML5; Google assembles ads across Search, Play, YouTube, Display, Discover [CHECK current placements]. No manual placement control; assets and bids/budget are the levers. Needs Firebase/GA4 or MMP with SDK or SKAN setup for iOS.
- Shopping: Merchant Center feed drives it. Feed quality (title, GTIN, price, availability, images) is the main lever. Standard Shopping gives bid/query control; feed-only PMax gives automation. Free product listings run alongside.
- Local/other: Local services ads, Hotel ads: specific verticals.

## 3. Bidding & budget
- Smart Bidding strategies: Maximise conversions (optional tCPA), Maximise conversion value (optional tROAS), tCPA, tROAS, Maximise clicks, Manual CPC (legacy), Target impression share (Search brand defence), Maximise reach / Target CPM / Target CPV (video).
- Data thresholds (rules of thumb): tCPA wants ~30+ conversions per 30 days per campaign; tROAS wants ~50+ conversions per 30 days and consistent value data. With less, start with Maximise conversions (no target) then add target after 2-4 weeks.
- Learning period: ~1-2 weeks after a bid strategy/budget/conversion change. "Learning" status flagged at campaign level. Avoid changing targets by more than ~20% at a time.
- Budget rules of thumb:
  - Search: daily budget at least ~10x target CPA to avoid constraint [CHECK], and enough to capture the keyword set.
  - App campaigns: Google recommends daily budget at least ~50x tCPA for install campaigns [CHECK], ~10x for in-app action tCPA (e.g. first ride event) if you expect few events; more is better.
  - PMax: budget >= ~3x tCPA/day, ideally ~10x [CHECK].
- tCPA / tROAS use: start slightly above achieved CPA / below achieved ROAS, tighten gradually. Setting an overly aggressive target throttles delivery.
- Value-based bidding: pass real value (revenue/margin/LTV). For app: pass in-app event value.
- Portfolio bid strategies share data across campaigns, helpful for small campaigns [rule of thumb].
- Seasonality adjustments / data exclusions for short promos or tracking outages.
- Shared budgets are generally a poor control; prefer explicit allocation by marginal CPA.

## 4. Targeting & signals
- Search: queries (keywords/themes), audiences as observation or targeting (in-market, custom segments, Customer Match, remarketing), locations, devices, ad schedules.
- PMax / Demand Gen / App: audience signals or lookalikes are hints that steer the algorithm, not hard restrictions (except Demand Gen targeting is a restriction by default unless optimised targeting is enabled [CHECK]).
- First-party data: Customer Match (hashed email/phone) for targeting, exclusion and value-based bidding; remarketing lists; GA4 audiences. Upload customer lifecycle data for "new customer" bidding.
- Conversion signals (critical):
  - Google tag + Enhanced Conversions (web and leads), GA4 key events, offline conversion import (OCI) for CRM, server-side tagging (sGTM), Consent Mode v2 (EEA/UK requirement for personalisation and measurement).
  - App: Firebase or MMP; SKAN for iOS; Google Ads App conversion tracking; in-app event with value.
  - Data Manager API and first-party tagging improvements in 2025-2026 [CHECK].
- Negative keywords: account-level lists; brand exclusions in PMax/AI Max; placement exclusions on Display/Video.
- Geo: presence vs presence or interest setting; exclude irrelevant regions.
- Device and OS targeting: critical for apps (Android only for Play, iOS for App Store).

## 5. Creative: what wins
- Search: ad copy that mirrors query and states the offer, price, proof, and CTA; use all RSA headline slots; include keyword in headline 1; location/currency; sitelinks, callouts, structured snippets, price assets, image assets, call and lead form assets.
- PMax: complete the asset group (max headlines/descriptions, 5+ images in multiple ratios, 1+ videos in 16:9, 9:16, 1:1). Multiple strong videos beat auto-generated ones.
- Video/YouTube: first 5 seconds (before skip) must hook and brand; 15 s cut-downs; 6 s bumpers; vertical 9:16 for Shorts; sound-on works on YouTube more than on TikTok; captions help. Include CTA and end card; ABCD framework (Attention, Brand, Connection, Direction) is Google's recommended heuristic.
- Demand Gen: Meta/TikTok-style creative, 9:16 + 1:1 + 4:5 + 1.91:1 images; product-led or creator/UGC style; carousels for multi-product.
- App: provide many assets (short vertical videos 9:16, 1:1, 16:9, 10-30 s; images; text), localised; Google tests combinations. Show app UI + benefit in the first seconds.
- Asset diversity > asset volume: different angles. Check asset-level ratings (Low/Good/Best) as hints, with caution (ratings relative to other assets, not business value).
- Fatigue signals: falling CTR/VTR, rising CPA, rising frequency in Demand Gen/Video; refresh every ~4-8 weeks, faster for narrow audiences.

## 6. Ad specs cheat sheet
| Item | Spec |
|---|---|
| RSA headline | 30 chars, up to 15 headlines (min 3) |
| RSA description | 90 chars, up to 4 (min 2) |
| Display path | 15 chars x 2 |
| Sitelink | 25 chars title, 35 chars x 2 description lines |
| Callout | 25 chars |
| PMax text assets | headlines 30 chars (3-15), long headlines 90 chars (1-5), descriptions 60/90 chars (2-5), business name 25 chars [CHECK counts] |
| PMax / Display images | landscape 1.91:1 (1200x628), square 1:1 (1200x1200), portrait 4:5 (960x1200) [CHECK], logo 1:1 and 4:1 |
| Video | YouTube-hosted; 16:9, 9:16, 1:1 |
| Skippable in-stream | skippable after 5 s; no hard max; best practice 15-30 s for action [CHECK] |
| Bumper | 6 s non-skippable |
| Shorts | 9:16 up to 60 s (Shorts ads: 60 s max [CHECK]) |
| Demand Gen text | headline 40 chars, description 90 chars, business name 25 chars [CHECK] |
| App campaign text | up to 4 text lines/headlines (25-30 chars) and descriptions (90 chars) [CHECK exact limits] |
| App campaign video | 9:16, 1:1, 16:9; 10-30 s recommended |
| Shopping | feed title 150 chars (first 70 matter), images >=100x100 px (non-apparel), >=250x250 (apparel) |

## 7. Measurement & attribution
- Attribution model: data-driven attribution (DDA) is the default for most conversion actions (last-click/first-click/linear/etc. deprecated or limited for most accounts [CHECK]).
- Windows: click-through conversion window default 30 days (adjustable 1-90 days); view-through conversion window default 1 day (Display/Video); Engaged-view conversion (EVC) window 3 days for YouTube ads (user watched >=10 s for in-stream or interacts) [CHECK]. Conversion windows are set per conversion action.
- Platform-reported issues: Search brand and PMax can claim existing demand. Always split brand/non-brand and new/returning customers.
- Lift/incrementality tools: Conversion Lift (user-based holdout, requires spend threshold), Geo experiments / matched markets via Experiments or Meridian MMM (open-source), Brand Lift (YouTube), Search lift, Campaign Experiments (A/B split of traffic, e.g. AI Max on/off, bidding strategy tests), Reach Planner.
- Google Analytics 4: separate, event-based attribution (DDA); numbers will not match Google Ads.
- Import first-party and CRM outcome data (OCI) to optimise for qualified leads, not form fills.
- App: in-app reporting from Firebase/MMP; install attribution uses click window 30 days (default) and view window 1 day [CHECK]. iOS limited by SKAN.

## 8. DO's
1. Fix conversion tracking first: correct primary conversion actions only (avoid counting micro-events as primary), Enhanced Conversions, OCI for leads, Consent Mode v2 in EEA.
2. Separate brand and non-brand; protect brand with exact match/Target impression share or brand PMax exclusion.
3. Build Search around intent clusters; use broad match only with Smart Bidding, good negatives and sufficient conversions.
4. Run AI Max, PMax and Demand Gen as experiments (Campaign Experiments) against a baseline, not as blind switches.
5. Give PMax and Demand Gen real creative: multiple videos in vertical and horizontal formats, product imagery, UGC style.
6. Use value-based bidding with real values; segment "new customer" value higher if the goal is acquisition.
7. For app campaigns, optimise toward the deepest event with volume (installs > registration > first ride/purchase), use Android and iOS separate campaigns.
8. Use exclusions: negatives, brand lists, placements/YouTube channels, geographic exclusions.
9. Check search term and placement reports weekly; add negatives for irrelevant queries.
10. Make budgets non-limiting for winners; check "limited by budget".
11. Align landing page speed and relevance; message match to ad copy.
12. For case plans: show a budget split with funnel logic (Search for capture, YouTube/Demand Gen for demand creation, App campaigns for installs) and marginal CPA reasoning.

## 9. DON'Ts
1. Do not count every micro-conversion (page view, click) as a primary conversion in Smart Bidding.
2. Do not judge PMax on blended ROAS without separating brand/existing customers.
3. Do not set aggressive tCPA/tROAS from day one with little data (throttled delivery).
4. Do not change bid strategy/budget/targets multiple times a week (resets learning).
5. Do not run tiny budgets across many campaigns; consolidate.
6. Do not launch PMax/Demand Gen with only a few weak assets or without video.
7. Do not turn on broad match without negatives and conversion value signals.
8. Do not forget exclusions of existing customers when acquisition is the goal.
9. Do not rely on Ad Strength or asset ratings as the success metric.
10. Do not optimise App campaigns for installs and then evaluate on deep funnel conversion without testing the deep event bidding.
11. Do not mix Android and iOS in one app campaign when you need separate learning and SKAN handling.
12. Do not ignore Display/Partner network leakage in Search (turn off Search Partners/Display expansion unless tested).
13. Do not assume view-through conversions on YouTube/Display are incremental.

## 10. Method of success (playbook)
1. Launch: audit tracking and conversion actions; define KPI hierarchy; choose campaign mix based on demand (search volume) and goal.
2. Start: Search (brand + non-brand intent clusters) with Maximise conversions or tCPA; PMax or Demand Gen for incremental reach; App campaign for installs if app goal.
3. Learn (week 1-2): keep changes minimal; monitor search terms, placements, impression share, budget limits; add negatives.
4. Optimise (week 2-4): move to tCPA/tROAS when stable; split winners; add video assets; apply experiments for AI Max/PMax; adjust budgets toward lowest marginal CPA.
5. Scale: raise budgets 20-30% steps; expand keywords/themes and geos; add new audiences/lookalikes (Demand Gen); add new asset groups.
6. Refresh: swap in new creatives every few weeks; review asset performance; refresh feed titles; update ad copy with seasonal offers.
7. Validate: run lift test/geo experiment; reconcile with backend/CRM and GA4.

## 11. KPI benchmarks (orders of magnitude; case benchmarks win)
- Highly dependent on market, vertical, seasonality and match type. Use as sanity checks only.
- Search CPC: often ~$0.3-$3 in many markets; $2-$15+ in competitive US/EU verticals (legal, insurance, finance, B2B SaaS). Emerging markets lower [CHECK for the case market].
- Search CTR: ~3-8% (brand much higher, non-brand lower). Search conversion rate: ~2-8% depending on funnel.
- Shopping CPC: ~$0.2-$1.5; PMax CPM mixed.
- YouTube: CPV ~ $0.01-$0.10 typical; CPM ~ $3-$15 (bumper/reach cheaper in emerging markets); view rate for skippable in-stream ~15-35% [CHECK].
- Demand Gen: CPM ~ $3-$12; CTR ~0.5-1.5% (varies strongly).
- App campaigns: CPI ~$0.2-$3 on Android in emerging markets, $1-$5+ in US/EU [CHECK]. Cost per in-app action is often 3-20x CPI. ROAS depends on LTV.
- Brand search CVR is typically several times higher than non-brand; do not blend them.

## 12. AI features on this platform
- Automation: Smart Bidding, PMax, AI Max for Search, Demand Gen with optimised targeting/lookalikes, App campaigns, broad match, dynamic ads, Final URL expansion, text customisation.
- Generative creative: asset generation with Gemini in Google Ads (headlines, descriptions, images, sitelinks), image editing and expansion, video generation/editing (Veo-based tools in Asset Studio / YouTube Shorts tools [CHECK]), automatically created assets (ACA), "Product Studio" in Merchant Center.
- Conversational features: Google Ads Advisor (Gemini-based chat) and AI-driven recommendations [CHECK].
- Ads in AI surfaces: ads in AI Overviews and AI Mode in Search (expanding, launched 2025 for eligible campaigns using AI Max/PMax/broad match) [CHECK scope].
- Disclosure: Google Ads political content policy requires disclosure for synthetic content in election ads; SynthID watermarking on Google-generated assets; misrepresentation policies apply to AI content [CHECK specifics].

## 13. Common traps in a case/competition setting
- Judging on CTR/CPC/CPI instead of the business KPI (e.g. CPA first ride).
- Over-crediting PMax/Brand search ROAS without incrementality (brand captured existing demand).
- Using Maximise conversions without target on a conversion defined as installs; the system will chase cheap low-quality installs. Choose the right event.
- Overlooking learning: promising precise tCPA after 2 days.
- Ignoring data requirements: tROAS with 5 conversions per month.
- Ignoring Android vs iOS split and SKAN limits when reasoning about iOS performance.
- Misreading YouTube view-through and EVC conversions as incremental.
- Not segmenting by geography (e.g. Lagos vs rest of Nigeria) where CPMs/CPIs differ.
- Underplaying negative keywords and brand exclusion controls; AI-led setups need guardrails.
- Allocating budget to Search despite low search volume for a new/app category; Search captures demand, it does not create it.
