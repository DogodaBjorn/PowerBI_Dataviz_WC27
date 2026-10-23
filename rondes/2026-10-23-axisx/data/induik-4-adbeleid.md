# Induik 4: ad policy for a perimenopause app (Meta, Google, TikTok, Apple Ads)

**Answer first.**
1. No channel is blocked for reaching women 40-55: age, gender and location targeting stay available on Meta and Google. Interest or audience targeting on menopause/health is the blocked part (Google: verified; Meta: health interests gone per Meta guidance, exact 2022 removal list unverified).
2. The real blocker is optimization on Meta: a symptom tracker fits Meta's own "health and wellness" data source definition ("wellness tracker"), which can restrict mid/lower funnel events, block custom events until reviewed, or fully restrict all events, per country or globally. Plan for optimizing on installs or link clicks, and treat "onboarding completed" as a bonus, not the base case.
3. Legit workaround: broad targeting (women, 39+, country) plus creative that self-selects, optimize on the highest event the platform still allows, and measure onboarding and D7 in our own analytics. Renaming a health event to hide it from Meta's classifier is not a workaround, it is a Business Tools Terms breach.

Researched 2026-10-23. Meta pages were retrieved through Meta's own help-center tool (Meta Ads MCP, `ads_get_help_article`), because WebFetch on facebook.com returns only the page title. Google, Apple, TikTok and Washington AG pages were read with WebFetch. Anything not read on an official page is marked **unverified**.

## Traffic light per channel

| Channel | (a) Women 40-55 interested in menopause | (b) Optimize on onboarding completion | (c) Web quiz to app | Key sources |
|---|---|---|---|---|
| Meta (FB/IG) | GREEN for age 40-55 + women + country. RED for health or menopause interests (Meta tells advertisers to avoid health info when describing audiences). Ads must target 18+. | ORANGE to RED. Depends on the category Meta assigns to the app/dataset. Possible: core setup (OK), restricted mid/lower funnel events, or full restriction (then only awareness, engagement, traffic). | ORANGE. Pixel on quiz pages is the riskiest data source: quiz answers on symptoms are prohibited information. Core setup strips URL paths and custom parameters. | https://www.facebook.com/business/help/1402913027039332 , https://www.facebook.com/business/help/511197658391698 , https://www.facebook.com/business/help/124742407297678 , https://www.facebook.com/business/help/361948878201809 , https://www.facebook.com/business/help/2489235377779939 , https://www.facebook.com/business/help/2557868957763449 , https://www.facebook.com/business/help/440167386536513 , https://www.facebook.com/business/help/128066880933676 |
| Google Ads | GREEN for demographics (age, gender) and Google predefined audiences. RED for Customer Match, your data segments (remarketing), lookalikes, audience expansion. Demand Gen may not serve with its default curated audiences. | ORANGE (unverified). No Google policy page found that blocks in-app conversion events for health apps. The audience restrictions apply, the event restriction is not documented. | ORANGE. Web conversions fine; no remarketing of quiz visitors in a health category. | https://support.google.com/adspolicy/answer/16701855?hl=en , https://support.google.com/adspolicy/answer/143465?hl=en , https://support.google.com/adspolicy/answer/16258024?hl=en , https://support.google.com/adspolicy/answer/176031?hl=en |
| TikTok | GREEN (unverified for targeting). Healthcare policy has no health/wellness-app category for US, UK or EU sections; 18+ applies to medical categories. | ORANGE. Custom events are "not applicable for campaign optimization"; use a standard event. Event names must not suggest sensitive information. | ORANGE. Same data rules as Meta in spirit; do not send quiz answers. | https://ads.tiktok.com/help/article/tiktok-ads-policy-healthcare-pharmaceuticals?lang=en , https://ads.tiktok.com/help/article/custom-events?lang=en |
| Apple Ads (App Store) | GREEN for Search Results placement. Apple lists "Pharmaceutical and Medical" as allowed in Search Results, partially on Search tab, not on Today tab or Product Page; adults only. Whether a wellness tracker counts as "Medical" is unverified. | RED by design (unverified): Apple Ads optimizes and bids on taps/installs, not in-app events. | Not applicable (App Store native). | https://ads.apple.com/policies |

## Meta details (verified on official pages via Meta help-center tool)

- **Classification applies to apps, not only web.** "We categorize data sources, such as website domains and mobile apps, that send us data through the Meta Business Tools." Category "health and wellness" covers "health-related products and services (examples include, a patient portal, wellness tracker, telemedicine platform...)". Meta can assign it; a Meta-assigned category cannot be changed by the advertiser, only re-reviewed. https://www.facebook.com/business/help/1402913027039332
- **Three restriction levels**, "can be specific to certain countries or regions, or they could be applied globally": (1) core setup, blocks custom parameters and URL paths; (2) "restricts the sharing of specific mid and lower funnel events"; (3) full restriction, Meta Business Tools "cannot be used for ads purposes". With restrictions, custom events are blocked until reviewed and confirmed. Meta's own advice: move to upper-funnel events, or with full restriction to awareness, engagement and traffic (link clicks). https://www.facebook.com/business/help/511197658391698
- **Core setup** covers "custom web, app, and offline events": confirmed custom events can still be used in campaigns. https://www.facebook.com/business/help/124742407297678
- **Prohibited information** includes "sexual and reproductive health", "body specifications, bodily activities, and biological cycles", "medical condition trackers". Event, conversion and audience names and criteria "must not reflect, imply, or be based on any prohibited information." https://www.facebook.com/business/help/361948878201809
- **App setup note:** "don't share sensitive user data with us when setting up events." https://www.facebook.com/business/help/754990972934516
- **Ads are allowed:** with 18+ targeting Meta allows ads for reproductive health products addressing "the effects of menopause" and "women's reproductive health apps, such as femtech apps". https://www.facebook.com/business/help/2489235377779939
- **Copy rule:** no asserting or implying personal attributes incl. "physical or mental health (including medical conditions)"; "we don't allow ads that ask questions about personal attributes." So "Are you going through menopause?" and "Struggling with your hot flushes?" are out. "You" is fine if no attribute is named. https://www.facebook.com/business/help/2557868957763449
- **Health copy rules:** no clickbait in a health context, no "promises of specific outcomes within a set timeframe". https://www.facebook.com/business/help/2489235377779939
- **Targeting:** in the audience describer Meta says "avoid sensitive topics such as race or health information" (https://www.facebook.com/business/help/440167386536513). Advantage+ detailed targeting "doesn't apply to location, age or gender"; those settings "continue to apply" (https://www.facebook.com/business/help/128066880933676). Detailed targeting exclusions removed since 31 March 2025 (https://www.facebook.com/business/help/458835214668072).
- **US state privacy:** Limited Data Use flag exists for SDK, App Events API, Pixel, CAPI for listed US states. https://www.facebook.com/business/help/1151133471911882

**Unverified for Meta:** the exact list of restricted mid/lower funnel events (vendor blogs name Purchase and AddToCart); whether app install optimization survives the middle tier (official page only says upper-funnel events are the alternative; under full restriction only awareness, engagement, traffic); a US-first rollout in January 2025 (vendor blogs, e.g. haus.io, triplewhale.com); the exact 2022 removal of health interests such as menopause (Meta newsroom URLs 404'd).

## Google details (verified with WebFetch)

- Health is a sensitive interest category: physical or mental health conditions, chronic conditions, "intimate body function health issues". Not supported: advertiser-curated audiences, Customer Match, your data segments, audience expansion, lookalikes. Supported: Google predefined audiences, demographics, in-market, affinity, life events, location. Menopause is not named; that a menopause tracker falls under "Health" is likely but unverified. https://support.google.com/adspolicy/answer/16701855?hl=en
- Same list on the main policy page; remarketing ("data segments, previously called remarketing") not supported; Demand Gen "may be restricted from serving". https://support.google.com/adspolicy/answer/143465?hl=en
- May 2025 update only narrowed scope (excludes healthcare professional content); ban on targeting by health stays. https://support.google.com/adspolicy/answer/16258024?hl=en
- **Certification: not needed.** Healthcare and medicines policy requires certification only for prescription drug services, pharma, addiction services, abortion, health insurance and similar. A tracker without drugs, telemedicine or diagnosis is outside those. Avoid prescription drug terms and "speculative or experimental" treatment claims. The separate "Sexual health and wellness" policy was not checked (unverified). https://support.google.com/adspolicy/answer/176031?hl=en
- **App campaigns:** the policy pages do not mention App campaigns. Whether in-app action optimization is limited for health apps is unverified.

## Washington My Health My Data (US)

"An app that tracks someone's digestion or perspiration is collecting consumer health data." Selling consumer health data needs prior valid authorization; violation is a per se Consumer Protection Act violation, enforceable by private action. Small businesses in scope since 30 June 2024. https://www.atg.wa.gov/protecting-washingtonians-personal-health-data-and-privacy
So what: sending symptom-linked events to Meta/Google/TikTok for US users needs consent on the screen where data is collected. Legal check, not a channel decision. GDPR Article 9 (health as special category, EU/UK) not researched here: unverified.

## TikTok and Apple (verified with WebFetch)

- TikTok healthcare policy: US, UK and EU sections have no health/wellness or tracking-app category; 18+ applies to OTC medicines, medical devices, medical institutions. Tracking apps only named in some Asian markets. https://ads.tiktok.com/help/article/tiktok-ads-policy-healthcare-pharmaceuticals?lang=en
- TikTok custom events: "not applicable for campaign optimization"; "Don't use custom event names that are suggestive of sensitive information". https://ads.tiktok.com/help/article/custom-events?lang=en
- Apple Ads: "Pharmaceutical and Medical": Search Results allowed, Search tab partially, Today tab and Product Page not allowed; "may be shown to adults only". No health-targeting rules on the page. https://ads.apple.com/policies

## Workarounds: legit vs not

| Workaround | Verdict | Why |
|---|---|---|
| Broad targeting (women, 39+ or 40-55, country) + creative that self-selects ("an app for women who think", the doctor-report use case) | LEGIT | Age/gender/location allowed on Meta and Google; creative does the targeting. |
| Optimize on install (Meta app promotion, Google App campaigns, Apple Ads) and measure onboarding + D7 in own analytics/MMP | LEGIT | Matches Meta's own advice to move up-funnel. CAC per completed onboarding is computed by us, not by the platform. |
| Optimize on a standard event (e.g. CompleteRegistration) fired at end of onboarding, with no health parameters, confirmed in Events Manager | LEGIT IF Meta still allows that event for our category | Honest event, no prohibited info. May be on the restricted list (unverified). |
| Custom event "event_4" or a neutral name that stands for a health action, to dodge the category restriction | NOT LEGIT, high risk | Names and criteria "must not reflect, imply, or be based on" prohibited info; Meta can block events or suspend Business Tools use. Do not put in the deck as a tactic. |
| Pixel on web quiz sending answers (symptoms) as parameters or in URLs | NOT LEGIT | Prohibited information; also MHMDA exposure in the US. |
| Remarketing quiz visitors or uploading the beta list (Customer Match / lookalikes) on Google | NOT ALLOWED | Health sensitive category. On Meta: custom audiences based on health criteria not allowed; a plain email list of beta users is not explicitly banned on the pages read (unverified). |
| Ad copy as a question on symptoms ("Are you in perimenopause?") | NOT ALLOWED (Meta) | Personal attributes policy. Use third person or product benefit: "Perimenopause, tracked. A report your doctor can read." |

## Caveats

- Meta's restriction level is set per data source and per country; we only know ours after the SDK sends data. Check Events Manager > data source categories in week 1 of Plan B, before committing budget.
- For the $50k plan: model Meta CAC on install optimization (worst realistic case), with event optimization as upside.
- The brief says the web quiz to App Store flow does not exist yet, so (c) is a design choice: keep quiz answers off the pixel.
- Third-party blogs used only as pointers (haus.io, triplewhale.com, pixelflow, elevar); none of their claims are used as fact above.
