# Meta Ads (Facebook, Instagram, Threads, Audience Network, WhatsApp)

Status: reference for 2-hour case rounds. Written 2026-10-23. Items marked [CHECK] = verify before relying on them. In a case, the case's own data and benchmarks beat everything below.

## 1. What it is good for
- Funnel role: full funnel, but strongest at demand generation (create and capture low-to-mid intent at scale) and efficient lower-funnel via algorithmic optimisation on pixel/CAPI/app events.
- Intent: low to medium (interruption, feed/Reels/Stories). No explicit query intent. Exception: click-to-WhatsApp/Messenger gives conversational intent.
- Audience: broadest reach of any paid channel (Facebook + Instagram + Messenger + WhatsApp + Threads). Skews 18-44 on Instagram, wider age on Facebook. Strong in emerging markets (Nigeria, India, Brazil, Indonesia, Philippines), Android-heavy, mobile-first.
- Best for: app installs and app events, e-commerce (catalog), lead gen (instant forms), local, messaging-based sales, awareness at scale, retargeting.
- Weak for: high-intent capture (use Google Search), B2B firmographic precision (use LinkedIn), long-form consideration video on TV screens.
- Surfaces: Facebook Feed/Reels/Stories/Marketplace/Search results, Instagram Feed/Reels/Stories/Explore/Profile feed, Messenger, Threads (ads global since 2025 [CHECK]), Audience Network (third-party apps/sites), WhatsApp (Status ads, Updates tab, click-to-WhatsApp [CHECK scope by market]).

## 2. Campaign structure & objectives (2025-2026)
- Objectives (ODAX): Awareness, Traffic, Engagement, Leads, App promotion, Sales. Optimisation goal and conversion location are set at ad set level.
- Automation stack: Advantage+ sales campaigns (replaced ASC and Shopping), Advantage+ app campaigns (replaced AAA), Advantage+ leads [CHECK name/availability], plus Advantage+ audience, placements, creative as toggles in manual campaigns. Meta is pushing to "give the algorithm budget + creative + goal, it does the rest".
- Andromeda-era logic (retrieval/ranking rebuild, 2025): creative IS the targeting. The system matches each ad to people by what the creative signals. Implications:
  - More genuinely different creative concepts beat more audiences.
  - Near-duplicate ads (same concept, small tweaks) get collapsed and add little. Diversify concept, angle, format, persona, hook, not colour of button.
  - Rule of thumb: 3-5+ distinct concepts per ad set at launch, each with 2-3 variants. [rule of thumb, not Meta spec]
- Consolidation: fewer campaigns and ad sets, more budget per ad set so each exits learning. Typical lean structure:
  - 1 prospecting campaign (Advantage+ / broad) + 1 retargeting or existing-customer campaign (if audience large enough) + optional test campaign.
  - Avoid splitting by age/gender/placement. Fragmentation starves learning.
- Test structure: separate "creative testing" campaign (CBO or fixed ABO, 1 ad set, 4-6 ads), promote winners into scale campaign. Use Meta A/B test tool for clean split tests.
- CBO (Advantage+ campaign budget) vs ABO: CBO for scale with similar ad sets; ABO for tests where each cell must get budget.
- App campaigns: Advantage+ app campaign needs MMP/SDK (AppsFlyer, Adjust, Singular, Branch) or Meta SDK. Choose optimisation: App installs (volume, cheap, low quality risk) vs App events (first purchase / first ride / registration) vs Value. Iterate installs > mid-funnel event > deep event as event volume allows.
- WhatsApp/Messenger: Sales or Leads or Engagement with Messaging destination; optimise for conversations, or for conversions after conversation (via Conversions API for Business Messaging [CHECK]).

## 3. Bidding & budget
- Strategies: Highest volume (lowest cost), Cost per result goal (cost cap, the usual control), Bid cap, ROAS goal, Highest value (value optimisation).
- Learning phase: ad set needs ~50 optimisation events in 7 days after launch or significant edit. "Learning limited" = not enough events (budget too low, too many ad sets, event too deep, audience too narrow).
- Budget rule of thumb: daily ad set budget >= (target CPA x 50) / 7, i.e. about 7x target CPA per ad set per day. If CPA is $20, budget ~$140/day per ad set. If the budget cannot support it, optimise for a higher-funnel event (e.g. install instead of first ride, add-to-cart instead of purchase) or consolidate ad sets.
- Cost cap: use when you have a known CPA ceiling and a stable account history. Set cap near, not far below, the achieved CPA (a cap far below market CPA throttles delivery to near zero). Start at 1.0-1.2x current CPA, tighten gradually.
- Lowest cost (no cap): use for launch and learning; watch CPA, then add a cap if it drifts.
- ROAS goal / Highest value: only with purchase value passed reliably and enough purchase volume (50+/week ideal).
- Significant edits that reset learning: budget change >~20-30% at once (rule of thumb), new ad creative added to ad set (can re-enter learning, though adding ads is generally tolerated), audience or optimisation event change, pausing for 7+ days.
- Scaling: vertical (raise budget 15-25% every 2-3 days) or horizontal (duplicate winning ad set with new creative). Do not double budgets overnight.
- Spending pace: ad delivery is front-loaded if lowest cost; accelerated delivery is no longer a typical option [CHECK].

## 4. Targeting & signals
- Default 2026 posture: broad (Advantage+ audience) with country/age minimum/language where needed; creative does the narrowing. Audience suggestions (interests, lookalikes, custom audiences) act as hints, not hard limits, in Advantage+ audience.
- Detailed (interest/behaviour) targeting: many options were consolidated or removed in 2024-2025; exclusions and some narrow options are restricted [CHECK current list]. Use interests only for hard constraints or niche B2B-ish cases.
- Hard constraints still available: location, minimum age, language [CHECK], custom audience exclusions (e.g. exclude existing customers) in manual audience setup. Advantage+ sales campaigns have an "existing customer budget cap" control.
- Lookalikes: still available; value-based lookalikes use customer LTV. Typically 1-3% seeds; for markets with a small population use 5-10%. Usually matched or beaten by Advantage+ audience at scale; still useful as a signal.
- First-party data: customer lists (hashed email/phone), website/app events, engagement audiences (video viewers, IG engagers, lead form openers). Uploading customer lists improves optimisation and enables retargeting/exclusion.
- Signal quality is the main lever:
  - Pixel + Conversions API (server-side) both on, deduplicated with identical event_id and event_name.
  - Event Match Quality (EMQ): aim for 6+/10 on key events; pass email, phone, external_id, fbp/fbc, IP, user agent.
  - Aggregated Event Measurement (iOS 14.5+): limited event prioritisation for web [CHECK current state; Meta eased AEM limits]. App: SKAdNetwork via MMP for iOS; Google Install Referrer for Android.
  - Domain verification, event prioritisation, value rules.
- Mobile app: MMP integration or Meta SDK, App Events API for server events, in-app event definitions (e.g. first_ride_completed) with value if possible.
- Leads: Instant forms with higher-intent form type ("More volume" vs "Higher intent" with review step), CRM integration to send lead quality back (Conversion Leads optimisation [CHECK name]).

## 5. Creative: what wins
- Mobile-first, vertical, native-looking. Reels-style 9:16 is the default winning format for prospecting; 4:5 for Feed.
- Hook in the first 1-3 seconds: pattern interrupt, a person talking to camera, a problem statement, a result, or a visible product in use. 3-second view rate and hook rate (3s plays / impressions) diagnose the hook.
- Length: 6-15 s for conversion video; up to 30-60 s for storytelling/education. Test one short and one longer cut.
- Sound-on design with captions burned in (many watch muted). Use clear audio, native voice, subtitles.
- UGC/creator-style and founder-led beat polished studio ads in most direct-response contexts. Test both; polished works for brand and premium.
- Message-market fit: put the offer, price, or key benefit in the first frame/headline. Local language, local slang, local context, local currency in emerging markets.
- Static/image still works: 1:1 and 4:5, one message, large type. Carousel for multi-product or step-by-step stories.
- Creative diversity (Andromeda): vary format (video, static, carousel), concept, persona, pain point, offer, length, CTA. Aim for at least 3-5 truly distinct concepts per active ad set, refresh weekly or bi-weekly.
- Safe zones for Reels/Stories (9:16): keep key text and faces away from top ~14% and bottom ~35% of the frame (UI overlays) and ~6% sides [CHECK exact]. Rule of thumb: keep everything important within the central 1080x1420 area.
- Text rules: no hard character limit on image text now, but keep copy short and legible. Primary text truncates ~125 characters in feed (front-load the message).
- Fatigue signals: frequency > ~3 in 7 days for prospecting (rule of thumb), falling CTR / 3s view rate, rising CPM and CPA, negative comments, falling thumb-stop. Remedy: new concept, not a new colour.
- Advantage+ creative toggles (auto crop, music, text improvement, image expansion, adding overlays, 3D animation, visual touch-ups) can lift results but can distort brand. Inspect and switch off what breaks brand or compliance.
- For app installs: show the app UI in use + the core benefit + a clear CTA ("Install now"), playable/short demo clips, local language, lite-network considerations in emerging markets (small file sizes, short videos).

## 6. Ad specs cheat sheet
| Item | Spec (recommended / limit) |
|---|---|
| Feed image | 1080x1080 (1:1) or 1080x1350 (4:5); min width 600 px; 1.91:1 link ads 1200x628 |
| Stories/Reels image/video | 1080x1920 (9:16) |
| Video file | MP4/MOV, up to 4 GB (Reels/Stories typically recommended under ~250 MB), H.264 |
| Reels ad length | up to 90 s; best practice 6-30 s [CHECK max] |
| Stories ad length | up to 60 s per card [CHECK]; best practice 15 s or less |
| Feed video length | 1 s to 241 min allowed; best practice <30 s |
| Primary text | 125 chars before "See more" (no hard limit, ~2,200 max) [CHECK] |
| Headline | 40 chars recommended (~255 max) |
| Link description | ~30 chars recommended |
| Carousel | 2 to 10 cards, 1:1 recommended, cards 1080x1080 |
| Collection / Instant Experience | cover image/video + product set |
| Image text | no hard cap now; keep legible and short |
| CTA | preset list (Install now, Shop now, Learn more, Send message, Sign up, Book now, etc.) |

## 7. Measurement & attribution
- Default attribution setting: 7-day click + 1-day view (Meta also reports 1-day click, 1-day engage-through). In early 2026 Meta removed 7-day and 28-day view-through windows from API/reporting [CHECK]. Always state the window used when quoting CPA.
- Attribution setting at ad set level; "Incremental attribution" optimisation option (optimises for incremental conversions) rolled out 2025 [CHECK availability].
- Platform-reported vs reality: Meta over-credits view-through and claims conversions that would have happened anyway (esp. in retargeting and branded demand). iOS ATT shrinks observable conversions; modeled conversions and CAPI fill gaps.
- Tools:
  - A/B test (Experiments): clean split test of creatives/audiences/strategies.
  - Conversion Lift (holdout, user or geo-based): true incrementality; needs budget and time (typically 2-4 weeks) [rule of thumb].
  - Brand Lift (poll-based): awareness, ad recall, consideration.
  - Meta's open-source MMM Robyn, and Meridian-style MMM from Google; Meta Marketing Mix Models via partners.
  - Geo-holdout designs run outside the platform.
- In-platform diagnostics: Quality ranking, Engagement rate ranking, Conversion rate ranking (relative to competing ads in same audience).
- App: SKAN postbacks (conversion value, coarse values) vs MMP probabilistic/aggregated attribution; Android deterministic via Install Referrer. Expect iOS under-reporting.
- Cross-check: platform CPA vs MMP/backend CPA vs blended CAC/MER. If Meta says 2x ROAS and blended is 1x, trust blended.

## 8. DO's
1. Match optimisation event to business KPI, one step shallower if volume < 50/week/ad set (e.g. optimise registration if first-ride volume is too low, then validate downstream).
2. Send CAPI + pixel (or MMP/App Events API) with dedupe and strong match keys before launch.
3. Launch broad (Advantage+ audience) with 3-5 distinct creative concepts; let the algorithm find pockets.
4. Consolidate: fewer ad sets, each with enough budget (>= ~7x target CPA/day) to exit learning in a week.
5. Treat creative as the targeting lever; build a weekly concept pipeline (hooks x formats x personas).
6. Use 9:16 video with burned-in captions and a strong first second for Reels/Stories placements; 4:5 for feed.
7. Use cost cap / bid cap only after the account has stable history; set above current CPA, tighten gradually.
8. Exclude existing customers/recent converters from prospecting; separate retargeting with a clean budget cap.
9. Segment reporting by placement and optimise through creative or placement exclusions (e.g. Audience Network) if quality is poor.
10. Read results at the downstream KPI (first ride, purchase, qualified lead, LTV), not CTR or CPI alone.
11. Use naming conventions (concept_hook_format_version) so you can analyse by concept.
12. For tests, change one variable, let each cell exit learning, set a decision rule in advance (e.g. min 50 conversions or X spend per cell).

## 9. DON'Ts
1. Do not slice audiences by age/gender/interest/placement into many small ad sets (fragmented learning).
2. Do not judge by CTR, CPC or CPI alone. Cheap installs often convert poorly to the deep event.
3. Do not edit budgets, audiences or creatives daily during learning (resets and noise).
4. Do not set a cost cap far below achievable CPA, then conclude "Meta doesn't work" (under-delivery).
5. Do not rely on 28-day click or view-through windows to claim ROAS; check blended numbers.
6. Do not mix retargeting and prospecting in one ad set without an existing-customer control.
7. Do not run near-duplicate creatives and call it testing (Andromeda collapses them).
8. Do not leave all Advantage+ creative enhancements on blindly (brand risk, policy risk).
9. Do not use heavy text-over-image or misleading claims (policy, quality score, rejection).
10. Do not ignore Audience Network quality for install campaigns (junk installs, accidental clicks).
11. Do not launch an app campaign without a working MMP/SKAN setup and a test of the event firing.
12. Do not pause and restart ad sets repeatedly (loses learning).
13. Do not scale more than ~20-30% per step on cost-capped sets without checking CPA stability.

## 10. Method of success (playbook)
1. Launch (day 0): confirm tracking (test events in Events Manager / MMP, EMQ, dedupe); define KPI hierarchy (north-star: cost per first ride / purchase / qualified lead; guardrails: CPI, CTR, frequency).
2. Set up: 1 prospecting campaign (Advantage+ / broad), 1-2 ad sets max, 4-6 ads with distinct concepts; optional retargeting campaign.
3. Learn (days 1-7): do not touch except to fix errors; watch delivery, learning status, hook rate, CPA trend; kill obvious zero-spend or policy-rejected ads only.
4. Evaluate (day 7-10): compare ads by downstream CPA and volume; need minimum statistical weight (e.g. 20-50 conversions per decision, or a clear 2x gap); pause losers, keep winners.
5. Optimise: shift to deeper event if volume allows; add cost cap; add 3-5 new concepts informed by winners (new hooks on winning angle, new angles).
6. Scale: +15-25% budget every 2-3 days while CPA holds; duplicate winners into new ad sets with new creative; expand geography/placements.
7. Refresh: new creative batch every 1-2 weeks (or at frequency/CPA fatigue signals); retire fatigued ads; recycle best hooks to new formats.
8. Validate: run lift/holdout or compare to backend data before reporting ROAS.

## 11. KPI benchmarks (orders of magnitude; ALWAYS prefer the case's own benchmarks)
- Caveat: strongly varies by country, vertical, season, creative, objective and currency. Use only to sanity-check.
- CPM: about $2-$15 in many markets, higher ($10-$30+) in US/Western Europe/Q4; emerging markets (e.g. Nigeria, India) often low single digits [CHECK for the case market].
- CPC (link click): roughly $0.2-$2 typical; lower in emerging markets, higher in finance/B2B.
- CTR (link): about 0.5-2% in feed; Reels/Stories often lower; install ads higher IPM-based.
- CVR (click to lead/purchase): about 1-5% on web depending on funnel; landing page matters.
- App: CPI from ~$0.3-$3 in emerging markets to $2-$6+ in US/EU on Android [CHECK]; IPM (installs per 1000 impressions) ~ 3-15 [CHECK]. Cost per deep event is typically 3-20x CPI. IPM does not predict downstream conversion.
- Lead gen (instant form): cheap per lead, often low intent; call-qualified lead cost is a multiple of the form lead cost.
- Frequency: prospecting ~1.5-3 per week healthy; >4 signals fatigue/over-saturation in small audiences.

## 12. AI features on this platform
- Advantage+ creative: auto-generated image variations, background generation, image expansion (to fit 9:16), text variations/generation, video generation from images, virtual try-on, music/audio, product overlays; "Meta AI" generative tools in Ads Manager and Business AI (messaging agents) [CHECK exact names].
- Automated bidding/targeting: Advantage+ sales/app/leads campaigns, Advantage+ audience, Advantage+ placements, Advantage+ budget, GEM/Andromeda ranking.
- Meta has publicised plans to automate more of campaign creation (give goal + budget; AI builds creative + targeting) by end of 2026 [CHECK].
- Disclosure: Meta labels AI-generated content via C2PA/IPTC metadata ("AI info" label). Ads: political, electoral and social-issue ads using photorealistic AI-altered content must disclose digital alteration. For commercial ads, disclose where deepfake-like realism could mislead [CHECK]. Meta's ad policy also bars deceptive AI content (fake endorsements, fake testimonials).
- Practical: AI-generated humans/avatars can underperform authenticity; test AI-only vs human creative.

## 13. Common traps in a case/competition setting
- Judging by CTR/CPC/CPI: high IPM or low CPI on Meta often does not predict the deep event (first ride, purchase). Always compute cost per business action.
- Using engagement or video-view objectives for a conversion KPI. Match the objective to the judging KPI.
- Splitting budget over too many ad sets in a 2-hour round: there is no time for learning. Simplify, consolidate, pick optimisation events with volume.
- Not factoring learning phase into plan: show the learning timeline (week 1 learning, week 2 optimise) rather than promising instant CPA.
- Misreading view-through: 1-day view conversions inflate CPA performance; separate click-only vs click+view.
- Ignoring creative requirement: Andromeda means a plan with one creative is weak. Show a concept matrix.
- Forgetting measurement setup (CAPI, SKAN/MMP, EMQ) in the plan: judges often reward a clean measurement plan.
- Overpromising targeting precision (interest stacks) when the platform direction is broad + creative.
- Budget split logic: Meta tends to win reach and scale; justify allocation by marginal CPA and by incrementality evidence, not by platform-reported ROAS alone.
- Ignoring country context: payment methods, device quality, network speed, language, regulation, currency volatility.
