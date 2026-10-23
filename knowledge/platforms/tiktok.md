# TikTok Ads (TikTok Ads Manager, Smart+, Symphony, Spark Ads, TikTok Shop)

Status: reference for 2-hour case rounds. Written 2026-10-23. [CHECK] = verify before relying on it. The case's own numbers beat everything below.

## 1. What it is good for
- Funnel role: discovery and demand creation first; efficient mid/lower funnel via algorithmic optimisation (pixel/Events API/MMP). Strongest where short vertical video is the native behaviour.
- Intent: low (entertainment feed), high impulse potential. Search is growing (TikTok search ads / Search Ads Toggle, keyword insights) [CHECK].
- Audience: skews 16-34, heavy Gen Z and young millennials; growing 35+. Big in Southeast Asia, Middle East, Africa, LatAm, UK, US. Mobile-first, Android-heavy in emerging markets.
- Best for: awareness at scale, app installs (young urban consumers), impulse e-commerce, TikTok Shop, entertainment/FMCG/beauty/fashion/food/gaming/consumer fintech, trends and creator-led storytelling.
- Weak for: B2B, high-consideration purchases without strong creative, brand-safe premium contexts for some advertisers, strict last-click ROAS proof.
- Surfaces: For You Feed (core), Search, TikTok Shop, Pangle (audience network), TopView, in-feed.

## 2. Campaign structure & objectives (2025-2026)
- Advertising objectives: Awareness (Reach), Consideration (Traffic, Video views, Community interaction, App promotion, Lead generation), Conversion (Website conversions, App promotion, Product sales/TikTok Shop) [CHECK exact naming].
- Smart+ (Smart Performance): automation suite for Web, App and Catalog; Smart+ campaigns auto-optimise targeting, creative combination, bidding and placement using one campaign-level setup (rolled out 2025 replacing Smart Performance Campaign/Automated Creative Optimization) [CHECK names/availability].
  - Use for scale once you have creative volume and event signal; manual campaigns still available for control/testing.
- Symphony: TikTok's generative AI creative suite (Symphony Creative Studio, Digital Avatars, translation and dubbing, image-to-video, AI script, Symphony Assistant) [CHECK].
- Spark Ads: boost organic or creator posts as ads with authorisation codes (7/30/60/365 days) keeping social proof. Often outperform non-Spark ads on engagement; test for conversions.
- Account structure that works: 1 campaign per objective, 1-3 ad groups, 5-10+ creatives per ad group, consolidated; use Smart+ or Value-based optimisation when signal volume allows.
- Ad formats: In-Feed, Spark Ads, Carousel (image), Collection Ads, Dynamic Showcase Ads (DSA / catalog), Video Shopping Ads, Lead Gen, TopView, Brand Takeover, Branded Hashtag Challenge, Branded Effects, Pangle.
- App campaigns: App promotion (App Install, App Event, Value Optimization). iOS uses SKAN via MMP; Android via MMP deterministic/Install Referrer. Smart+ App campaigns [CHECK].
- Shop: TikTok Shop / GMV Max (for Shop sellers) automate ads [CHECK name/status].

## 3. Bidding & budget
- Strategies: Lowest cost (default), Cost cap, Bid cap [Max delivery], ROAS (value) goals, Maximum delivery. Budget types: daily or lifetime, campaign or ad-group level (Campaign Budget Optimisation available).
- Learning phase: ad group needs ~50 optimisation events within about 7 days of launch or significant edit. Too little volume = "Learning limited".
- Budget rules of thumb: daily ad-group budget at least ~2x target CPA, ideally enough to produce 50 events in 7 days (similar to Meta: ~7x CPA). TikTok has minimum budgets (campaign ~$50/day, ad group ~$20/day) [CHECK].
- Cost cap: use when stable; set above current CPA, tighten gradually. Over-tight caps cause underdelivery.
- Scaling: increase budget 15-30% per 24-48 h at most (rule of thumb) to avoid learning reset; or duplicate best ad group with new creative.
- Significant edits that reset learning: changing the optimisation event, bid strategy, targeting, creative swap on some setups, budget changes beyond ~20-30%.
- Dayparting rarely needed with broad targeting; watch frequency.

## 4. Targeting & signals
- Broad is the default winner with strong creative. Targeting options: demographics (age, gender, language, location), interests, behaviours (video interactions, hashtag/creator interactions), device (OS, model, carrier, connection), custom audiences (customer file, pixel/app events, engagement), lookalikes.
- Smart+ and interest expansion/Automatic targeting use signals from creative and conversions.
- Signals: TikTok Pixel + Events API (server-side) with deduplication (event_id); for app, MMP SDK; Advanced Matching (hashed email/phone). EMQ-like score in Events Manager [CHECK].
- Exclusions: exclude past purchasers or converters in prospecting.
- Brand safety: inventory filter (Expanded, Standard, Limited), third-party verification (IAS, DV, Zefr) [CHECK], category exclusions. Pangle placement optional (often lower quality; test and exclude if needed).
- Creator/UGC data: hashtags and creator interactions as audiences; Creative Center (Top Ads, Trends, Keyword insights) as research source.

## 5. Creative: what wins
- Native, organic-feeling, vertical 9:16 full-screen. Ads that look like TikToks outperform ads that look like ads.
- Hook in first 1-3 seconds: face to camera, bold visual, question, "POV", result first; fast cuts; text overlay.
- Length: 9-15 s for conversion; up to 30-60 s for storytelling/education. TikTok allows ads up to 10 minutes but short wins on cost [CHECK].
- Sound ON: voice-over, trending/commercial sounds, music. Use licensed audio (Commercial Music Library for business accounts; trending sounds from regular accounts may not be licensed for ads).
- UGC/creator-led: real people, imperfect lighting, authentic voice, first-person demonstration. Creators via TikTok One / Creator Marketplace; use Spark Ads for creator posts.
- Show the product/app in use within 2 seconds; clear CTA by the end; on-screen subtitles.
- Creative volume: refresh often. Test 5-10 new concepts weekly if budget allows; fatigue is fast (often 5-14 days at scale) [rule of thumb].
- Safe zones: keep key content out of the bottom ~20-25% (caption/CTA UI) and right edge ~130 px (icons), top ~130 px [CHECK exact]; TikTok provides a safe zone overlay in Ads Manager.
- Text: ad text 12-100 chars (English), brand name 2-20 chars [CHECK]; keep on-screen text short and centred.
- Fatigue signals: falling 2-second view rate / hook rate, rising CPM and CPA, falling CTR, rising frequency (>3 for week), comment sentiment shift.
- Diversify: different creators, angles, formats (talking head, demo, skit, trend, before/after, text-led, slideshow/carousel image ads).
- App installs: short gameplay/app demo, "how it works in 15 seconds", local language/creators, authentic reactions, price/benefit callout.

## 6. Ad specs cheat sheet
| Item | Spec |
|---|---|
| Video aspect ratio | 9:16 recommended (also 1:1, 16:9 supported); 1080x1920 |
| Video length | 5 s to 60 s typical (up to 10 min allowed [CHECK]); 9-15 s best for conversion |
| File type / size | MP4, MOV, MPEG, 3GP, AVI; up to ~500 MB [CHECK] |
| Ad text | 12-100 chars (English) |
| App/brand name | 2-20 chars (English) |
| Image ads | 9:16, 1:1, 16:9; 1080x1920 / 640x640 / 1200x628; carousel image (in-feed) up to 10 images [CHECK] |
| Spark Ads | organic post + authorisation code (7/30/60/365 days) |
| Resolution | >= 720p; 1080p preferred |
| CTA | preset list or dynamic CTA |
| Safe zone | avoid UI zones (bottom ~20%, right ~130 px) |

## 7. Measurement & attribution
- Default attribution: 7-day click, 1-day view (can be reduced to 1-day click for tighter view). Event-based attribution; app via MMP with its own windows [CHECK defaults].
- Reporting metrics: 2-sec video view, 6-sec view, completion, hook rate (2s views / impressions), CTR (destination), CVR, CPA, ROAS, in-app events.
- Lift tools: Conversion Lift Study (CLS, holdout), Brand Lift Study (BLS), Search lift [CHECK], Incrementality via MMM partners. Geo lift available through partners.
- Pixel vs MMP discrepancies: reconcile TikTok-reported vs MMP/backend; view-through share can be large.
- Measure incremental with holdouts, geo splits, or compare blended CAC/MER pre/post.
- Beware: TikTok "assisted" effect often shows up in direct/organic/search; use post-purchase surveys ("How did you hear about us?") and branded-search lift.

## 8. DO's
1. Build creative first, targeting second; plan a creative matrix (hook x angle x creator x length).
2. Use 9:16 native video with sound and captions; hook in 1-3 seconds; design for sound on.
3. Use Spark Ads with creators or organic top performers; collect authorisation codes early.
4. Install Pixel + Events API (or MMP + SKAN) and validate events before spend.
5. Launch broad or Smart+ with consolidated ad groups and 5-10 distinct creatives.
6. Optimise for the deepest event that reaches ~50 events per week; step down to a shallower event if needed.
7. Refresh creative weekly; kill creatives with low hook rate early.
8. Exclude converters; separate retargeting only if audience is large enough.
9. Localise creative (language, creators, humour, landmarks, currency) for market fit.
10. Use Creative Center for trend/competitive research; adopt trend formats quickly while relevant.
11. Test Pangle/placement splits and exclude if quality is poor.
12. Use brand safety filters aligned with brand risk appetite.

## 9. DON'Ts
1. Do not repurpose polished TV/Instagram ads without native adaptation.
2. Do not use horizontal/square video in feed placements.
3. Do not put key text in the UI overlay zones.
4. Do not judge by CTR/CPI or video views only; view-through and cheap installs can mislead.
5. Do not run many ad groups with small budgets (learning limited).
6. Do not rely on a single winning creative; fatigue arrives fast.
7. Do not use unlicensed music in ads (policy rejection); use Commercial Music Library or original audio.
8. Do not set an aggressive cost cap that starves delivery.
9. Do not ignore comments (negative sentiment, product questions); moderate and respond.
10. Do not treat TikTok as last-click only; consider assisted effects and halo.
11. Do not skip AI-generated content labels where required.
12. Do not overpromise instant CPA; plan for 7+ days of learning and creative iteration.

## 10. Method of success (playbook)
1. Launch (day 0): tracking tested (Pixel/Events API/MMP), account structure kept simple, 5-10 creatives in 3+ concepts, broad targeting.
2. Learn (days 1-7): no major edits; monitor hook rate, CPM, CTR, CPA by creative; keep budget stable.
3. Evaluate (day 7-10): cut bottom creatives (low hook, no conversions after ~2-3x CPA spend), scale top; analyse by concept.
4. Optimise: add Spark Ads of top organic/creator posts; shift to deeper event or ROAS goal; test Smart+.
5. Scale: raise budgets 20-30% per step; duplicate winners; expand geos/languages.
6. Refresh: new creative batch weekly; new hooks on winning concepts; seasonal trends.
7. Validate: lift study or blended CAC/survey signals.

## 11. KPI benchmarks (orders of magnitude; always prefer the case's benchmarks)
- Vary heavily by country, vertical, creative, season. Sanity checks only.
- CPM: about $2-$10 in many markets; emerging markets lower, US/UK/Western Europe higher ($6-$15+) [CHECK for market].
- CPC (destination): ~$0.1-$1.2 typical; CTR ~0.5-1.5% typical for in-feed.
- Hook rate (2s views/impressions): 25-40%+ is healthy [rule of thumb, no official number].
- Video completion for 15 s ads: ~5-15% typical.
- CVR (click to conversion on web): ~1-4%; install CVR from click varies strongly.
- App: CPI from ~$0.3-$2 in emerging markets, $1-$5 in US/EU [CHECK]; cost per deep event much higher.
- TikTok CPA often higher than Meta on direct response in some markets but cheaper at reach; compare by blended outcomes.

## 12. AI features on this platform
- Symphony: AI script generation, Digital Avatars (stock and custom), AI dubbing/translation, image-to-video, AI-generated backgrounds, creative editing, Symphony Assistant [CHECK full list].
- Automation: Smart+ (campaign setup, creative combination, targeting, bidding), GMV Max for Shop, Automated Creative Optimization, Search Ads Toggle.
- Disclosure/labelling: TikTok requires labelling of realistic AI-generated content (AIGC label) and automatically labels content with C2PA Content Credentials; ads with AI avatars must disclose AI-generated where the platform requires it. Certain AI claims are restricted (deceptive deepfakes, fake endorsements) [CHECK exact policy].
- Practical: AI avatars scale volume but test against real creators; authenticity is the ranking factor in user response.

## 13. Common traps in a case/competition setting
- Judging by CPI/CTR/views instead of the business KPI. TikTok install CPI is often low; deep-event conversion may be weaker.
- Ignoring creative volume: a plan with 2 creatives for TikTok is weak; show a concept pipeline.
- Using polished brand video; judges expect native, UGC, creator-led, Spark Ads.
- Not accounting for learning phase and fatigue timeline.
- Misreading view-through: 1-day view conversions and assisted effects confuse direct attribution; propose lift or holdout.
- Overlooking safe zones, sound, captions in a creative brief.
- Assuming audience = Gen Z only; check the case's target audience and age mix.
- Forgetting policy/regulatory context (country-specific ad restrictions, finance claims, music licensing).
- Over-allocating budget to TikTok when the case audience/market is not TikTok-heavy.
