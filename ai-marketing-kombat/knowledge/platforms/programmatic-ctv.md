# Programmatic, CTV and DOOH (DV360, The Trade Desk, CTV, DOOH)

Status: short reference for 2-hour case rounds. Written 2026-10-23. [CHECK] = verify before relying on it. The case's own numbers beat everything below.

## 1. What it is good for
- Funnel role: reach and frequency control across the open web, apps, video, audio, CTV and out-of-home; also retargeting and prospecting with 1P/3P data, contextual and curated deals.
- Intent: low to medium. High-quality environments (premium publishers, CTV) build brand and consideration; weak direct-response unless paired with strong measurement.
- Audience: any, via data (1P, contextual, curated), but cookie loss (Safari/Firefox always; Chrome third-party cookies still allowed in Chrome after Google's 2025 decision not to roll out a standalone prompt [CHECK]) pushes toward ID solutions (UID2, ID5, RampID), contextual and publisher/retail data.
- Best for: awareness/reach, big brands, CTV video, premium inventory, local/geo-based campaigns (DOOH), retargeting and cross-device sequencing, in markets with digital TV adoption.
- Weak for: small budgets (setup and fees), fast learning DR, markets with low premium inventory, app-install cases (usually less efficient than Meta/Google/TikTok).

## 2. Campaign structure & objectives
- DSPs: Google Display & Video 360 (DV360), The Trade Desk (TTD; Kokai platform, Koa AI, OpenPath, Sincera), Amazon DSP, Yahoo DSP, MediaMath (closed 2023), Xandr Invest (Microsoft Invest sunset 2025-2026 [CHECK]), Adform, Basis, Criteo.
- DV360: Insertion Orders > Line Items; auction types: open auction, private marketplace (PMP), preferred deals, programmatic guaranteed; YouTube and Google video partners; Floodlight for conversion tracking; Campaign Manager 360 (ad server).
- TTD: campaigns > ad groups; Kokai AI audience scoring; bid factors; deal desk; Ventura OS (CTV OS) [CHECK].
- Inventory types: display, native, video (in-stream/outstream), audio, CTV/OTT (Roku, Samsung, LG, Vizio, Amazon Fire TV, Netflix ads tier, Disney+ ads, Peacock, Prime Video, YouTube CTV), DOOH.
- Typical structure: prospecting (contextual + audience), retargeting (site/app visitors), CTV reach, sequential messaging, deals with premium publishers.
- Curation / supply path optimisation (SPO): prefer direct paths, sellers.json/ads.txt-verified supply, curated marketplaces.

## 3. Bidding & budget
- Bidding: fixed CPM, maximise viewable CPM, tCPA, tROAS/ value bidding (DSP algos), CPCV for video (CPCV on some CTV deals), target frequency, pacing flights.
- Learning: algorithmic bidding needs conversion volume (~50 conversions/week/line item rule of thumb) and enough impressions; otherwise use CPM/ viewable CPM with controlled frequency.
- Budget: minimums often $10k+/month for managed service; self-serve possible with lower minimums; platform fees (DSP fee ~10-20% of media, data fees, ad verification fees 0.05-0.20 CPM) reduce working media [CHECK]. Compare "working media" share.
- Frequency: cap per user per day/week (e.g. 3-7 per week for CTV; 1-3 per day for display).
- Dayparting and geo for DOOH and local; weather/event triggers.

## 4. Targeting & signals
- Contextual (keyword/category, page content, brand safe), audience segments (1P CRM match, 3P data marketplaces, lookalikes), demographic, geo/geo-fence, device, daypart, curated marketplaces, retail data (Amazon, Walmart Connect, Kroger).
- IDs: UID2/EUID, ID5, RampID, Netid; CAPI-like server-to-server conversion APIs; clean rooms (AMC, LiveRamp, InfoSum, Snowflake).
- CTV: household targeting via ACR data (Samsung, LG, Vizio), IP matching; deduplicated reach across linear and streaming via panel/CTV graphs.
- DOOH: audience impressions (mobility data), venue types (roadside, transit, malls, airports, gyms), time and weather triggers.
- Brand safety: pre-bid (IAS, DoubleVerify, Zefr, Oracle) and exclusion lists; avoid MFA (Made-for-advertising) sites.

## 5. Creative: what wins
- CTV: 15 s or 30 s, full-screen; sound on; large type; clear brand in first 2-3 seconds; QR code or branded search CTA; 1080p (1920x1080), MP4/H.264, VAST tags; non-skippable mostly.
- Programmatic video: 6, 15, 30 s; vertical for mobile in-app; captions for muted autoplay.
- Display: IAB standard sizes (300x250, 728x90, 160x600, 300x600, 320x50, 970x250); HTML5 under ~150 KB initial load; lightweight; clear CTA.
- Native: 1.91:1 image + short headline; native feel.
- DOOH: very short copy (<7 words), high contrast, big brand, simple visual, viewable from distance; static or 6-15 s loop; vary by daypart/context (weather, traffic).
- Audio: 15-30 s with strong audio logo and call to action.
- Dynamic creative optimisation (DCO) for retargeting and weather/location triggers.

## 6. Ad specs cheat sheet
| Item | Spec |
|---|---|
| CTV video | 15 s / 30 s, 1920x1080, MP4, H.264, VAST 3/4, 16:9 |
| Online video | 6/15/30 s, VAST/VPAID (deprecated), 16:9 or 9:16 in-app |
| Display sizes | 300x250, 728x90, 160x600, 300x600, 320x50, 970x250; <=150 KB initial for HTML5 [CHECK] |
| Native | 1200x628 image + 25-90 char headline [CHECK] |
| DOOH | formats vary: 1080x1920 (portrait), 1920x1080 (landscape), digital billboards 1080x360 etc.; static 8-15 s loops |
| Audio | 15/30 s MP3, VAST audio |
| Viewability (MRC) | display 50% of pixels for 1 s; video 50% for 2 s continuous |

## 7. Measurement & attribution
- Metrics: viewable impressions, viewability rate (MRC standards), IVT (invalid traffic), VCR (video completion rate), CPCV, reach/frequency (deduplicated), attention metrics (Adelaide, Lumen), brand lift, search lift, site visits, footfall (DOOH), conversions (view-through and click-through).
- Attribution: platform ad server (Floodlight/CM360), TTD pixel/UID2, MMP for apps; defaults vary: view-through windows 7-30 days are common in DSPs and wildly overstate impact.
- Incrementality: geo holdouts, ghost bids/PSA tests, brand lift, MMM; CTV: lift via panels and matched markets; DOOH: mobile location lift.
- Beware: completed view on CTV is not attention (living room, TV may be off), and VTR/VCR from non-skippable formats is inflated.

## 8. DO's
1. Pick DSP/format based on budget, markets and measurement ability.
2. Use verified supply paths (SPO, ads.txt), premium PMPs for brand-safe reach.
3. Cap frequency; dedupe reach across CTV, display and YouTube.
4. Use brand lift or geo tests to prove impact; define success metric up front.
5. Pair CTV/DOOH with search/social to capture induced demand; QR/branded search CTAs.
6. Exclude MFA sites and low-quality apps; verify with third-party tools.
7. Consider fee stack and working media share when comparing options.
8. Use contextual targeting where IDs are weak; test creative variants.

## 9. DON'Ts
1. Do not use programmatic display for last-click performance goals without safeguards.
2. Do not rely on view-through conversions as proof.
3. Do not run CTV without frequency control (overserving).
4. Do not buy open exchange cheap CPM without verification.
5. Do not ignore viewability and IVT.
6. Do not compare CPM across formats as a quality signal.
7. Do not overspend on DOOH without a trackable metric or geo link.
8. Do not use large HTML5 files or landscape-only creative for mobile in-app.

## 10. Method of success (playbook)
1. Define objective (reach, brand lift, site visits, conversions) and measurement approach.
2. Set up: DSP, pixels/Floodlight/UID2, verification, deals.
3. Launch: 2-3 audience/context packages, 2-3 creatives, fixed CPM or viewable CPM, frequency cap.
4. Learn 2 weeks; optimise inventory (exclude low-quality), tune frequency, pace.
5. Scale: add CTV/PMP, sequential messaging; expand geos; retarget engaged users.
6. Validate: lift study, geo test, blended results.

## 11. KPI benchmarks (orders of magnitude; prefer the case's own benchmarks)
- Display CPM ~$1-$8 (open web), PMP $5-$15; video CPM ~$5-$25; CTV CPM ~$15-$40 (US; lower elsewhere) [CHECK]; DOOH CPM ~$5-$20 (varies by venue); audio ~$8-$20.
- Display CTR ~0.05-0.2%; Video VCR 60-90% (non-skippable), 15-35% skippable; viewability 60-80% typical target; IVT <2-3% [rule of thumb].
- DSP+data fees reduce working media (often 60-80% working media) [CHECK].

## 12. AI features
- Algorithmic bidding and audience scoring: TTD Kokai/Koa, DV360 optimised targeting and automated bidding, Amazon DSP optimisation, Google Gemini-based creative generation in DV360 [CHECK], contextual AI (semantic classification), generative creative for DCO.
- Disclosure: CTV and publisher partners follow their own AI content rules; EU AI Act transparency obligations for synthetic content (phased 2025-2026) [CHECK].

## 13. Common traps in a case/competition setting
- Treating CTV/programmatic as DR with view-through "ROAS".
- Ignoring fee stack, viewability, MFA.
- Selecting CTV in markets with limited streaming penetration (verify local CTV and DOOH availability).
- No lift measurement plan.
- Over-weighting reach metrics rather than business KPI.
