# LinkedIn Ads (Campaign Manager)

Status: reference for 2-hour case rounds. Written 2026-10-23. [CHECK] = verify before relying on it. The case's own numbers beat everything below.

## 1. What it is good for
- Funnel role: B2B demand creation and capture via firmographic precision; ABM; recruiting/employer brand; thought leadership. Weak as a cheap-volume channel.
- Intent: professional context, not purchase intent. Lead-gen form flows capture intent on the spot.
- Audience: professionals (job title, seniority, function, industry, company size, skills, groups). Targetable by company list (ABM). Skews to white-collar, 25-54, high income.
- Best for: B2B SaaS, professional services, finance/B2B fintech, enterprise tech, HR/recruitment, events/webinars, high-ACV products.
- Weak for: mass-market consumer, low-ticket impulse purchases, app installs for consumers, markets with low LinkedIn penetration.

## 2. Campaign structure & objectives (2025-2026)
- Objectives: Brand awareness, Website visits, Engagement, Video views, Lead generation, Website conversions, Job applicants (Talent leads) [CHECK].
- Formats: Single image, Carousel, Video, Document ads, Thought Leader Ads (promote member/employee posts), Event ads, Conversation ads, Message ads (Sponsored Messaging; InMail), Text ads, Dynamic/Follower/Spotlight ads (right rail, desktop), Lead Gen Forms (prefilled).
- Structure: 1 campaign per objective/audience/funnel stage; 2-4 ads per campaign; separate retargeting campaign (website retargeting, video viewers, Lead Gen form openers, company page engagers).
- Funnel stack example: Awareness (video/thought leader to broad ICP) > Consideration (document ads, case studies, webinar) > Conversion (Lead Gen Form with offer/demo; retarget engaged audiences).
- Audience Network (LinkedIn Audience Network, LAN) extends beyond LinkedIn feed to partner apps/sites; usually test and exclude if quality is poor [CHECK].
- LinkedIn Accelerate (AI-assisted campaign setup, 2025) simplifies creation: goal + budget + creative, AI builds audience and optimisation [CHECK availability].
- Predictive Audiences and Audience Expansion: AI-generated lookalikes from first-party data (min 300 matched members for Matched Audiences; Predictive requires larger seed) [CHECK].

## 3. Bidding & budget
- Bid strategies: Maximum delivery (automated; default), Cost cap (cost per result target), Manual bidding (CPC/CPM/CPS).
- Costs are high: auction is B2B-priced. Minimum budgets: daily min $10, lifetime $100 per campaign [CHECK]. Practical minimum for learning: enough budget for roughly 15 conversions per audience per month [rule of thumb]; thin budget on tiny audiences yields noise.
- No hard learning phase like Meta, but algorithm stabilises after about 1-2 weeks and with enough impressions (rule of thumb: >=100 clicks or 15-25 conversions before judging).
- Audience size: aim 50,000+ for sponsored content (min 300 for matched audiences; 1,000+ for some formats). Overly narrow = high CPM, no delivery [CHECK thresholds].
- Use Maximum delivery to learn; apply Cost cap if CPL/CPA drifts; use manual bid only with a clear competitor bid view and CPM/CPC range suggested by LinkedIn.
- Frequency: manage via audience size and time; B2B audiences saturate quickly; rotate creatives every 2-4 weeks.
- Lead gen forms: CPL typically lower than landing page; volume vs quality tradeoff.

## 4. Targeting & signals
- Native targeting: job title, job function, seniority, industry, company size, company name/list (ABM), skills, groups, member interests, degrees, years of experience, company growth rate, followers of your page; location; language.
- Matched Audiences: website retargeting (Insight Tag), contact lists (email, min 300 members), company lists (ABM; min 300 companies), video viewers, Lead Gen form audiences, event audiences, account lists via CRM integration (HubSpot, Salesforce).
- Audience Expansion (turn on for volume; off for strict ABM); Predictive Audiences (build from conversions); Lookalikes limited now.
- Exclusions: competitors, current customers, employees, job seekers, irrelevant seniority (e.g. exclude entry level for enterprise B2B), irrelevant job functions.
- Signals: LinkedIn Insight Tag + Conversions API (CAPI) for server-side; offline conversions via CRM; revenue attribution reports; Lead Gen Form -> CRM sync.
- Targeting stack: too many layers (title AND company size AND skills AND seniority) kills reach. Start with 2-3 attributes (e.g. job function + seniority + company size).

## 5. Creative: what wins
- Thought-leadership, authentic employee/exec voices (Thought Leader Ads), data-led insights, clear value-proposition headline, pain point framing for the persona.
- Video: 15-30 s for sponsored video; up to 90 s for storytelling; subtitles essential (muted viewing). Face-led, founder/expert-led, client testimonial.
- Document ads (PDF carousels): strong for lead gen with gated content (reports, checklists).
- Images: 1.91:1 or 1:1; simple visuals, people, charts; avoid stock-photo feel. Native-looking posts outperform banner ads.
- Copy: intro text 150 chars recommended before truncation (up to 600); headline ~70 chars recommended (up to 200); one clear CTA; address role and problem; specific numbers.
- Offer: webinars, benchmark reports, free tools, trials, templates; demo requests need warm audiences.
- Message ads: short, personal, one CTA; avoid overuse (spam fatigue); frequency cap 1 message per 30 days per member [CHECK].
- Volume: 3-5 ads per campaign, rotate; fatigue appears faster on small audiences. Watch CTR below ~0.3% and rising CPC.
- Safe zone/format: mobile feed shows 1:1 and 4:5-like; vertical video (9:16) supported in mobile feed [CHECK]; test 1:1 and 4:5.

## 6. Ad specs cheat sheet
| Item | Spec |
|---|---|
| Single image | 1200x627 (1.91:1) or 1200x1200 (1:1); JPG/PNG up to 5 MB |
| Carousel | 2-10 cards, 1080x1080 (1:1); intro 255 chars; card headline 45 chars |
| Video | 3 s to 30 min; recommended 15-30 s; MP4, up to 200 MB; 16:9, 1:1, 4:5, 9:16 [CHECK] |
| Intro text | up to 600 chars (150 recommended before truncation) |
| Headline | up to 200 chars (70 recommended) |
| Description | up to 300 chars (not shown on mobile) |
| Document ad | PDF/PPT/Word up to 100 MB, up to 300 pages; first pages gated by form [CHECK] |
| Lead Gen Form | headline 60 chars, details up to 160 chars, custom questions up to 3 [CHECK] |
| Message ad | subject 60 chars, body 1,500 chars, CTA button 20 chars [CHECK] |
| Conversation ad | intro 500 chars, up to 5 CTAs 25 chars [CHECK] |
| Text ad | headline 25 chars, description 75 chars, 100x100 image |

## 7. Measurement & attribution
- Default attribution: 30-day click, 7-day view (configurable 1/7/30 days for click; 1/7/30 for view) [CHECK]. Last-touch plus option of all-touch/linear and position-based in Revenue Attribution Report.
- Insight Tag conversions; offline conversions (CRM) with Conversions API; Revenue Attribution Report (with Salesforce/HubSpot) for pipeline and revenue.
- Funnel metrics: CTR (0.4-0.7% is typical single image), CPC, CPL, cost per MQL/SQL/opportunity, pipeline value, ROAS on closed-won. Always push to SQL/opportunity, not just form CPL.
- Lift tools: Brand Lift study (via LinkedIn), Conversion Lift (CLS) available at scale [CHECK]; MMM via partners. Lift tests usually need large budgets.
- B2B reality: long sales cycles (3-12 months), multiple stakeholders; LinkedIn influences deals not captured in last-click; use account-level engagement and pipeline influence metrics.
- Lead quality: LinkedIn Lead Gen forms produce high volume but variable quality; require qualification question or CRM scoring; compare conversion to opportunity versus other channels.

## 8. DO's
1. Start from ICP: job function + seniority + company size (+ industry), 50k+ audience.
2. Combine Thought Leader Ads and company-page ads for trust and cheaper CPM.
3. Use Lead Gen Forms with a strong offer and 3-5 fields; sync to CRM; qualify.
4. Retarget: website visitors, video viewers (50%+), form openers, event registrants, document ad viewers.
5. Separate prospecting and retargeting campaigns; use different offers.
6. Rotate creatives every 2-4 weeks; test 3-5 variants.
7. Exclude existing customers, employees, competitors, job seekers.
8. Use Maximum delivery to start; move to cost cap on stable performance.
9. Feed back offline conversions (SQLs/closed-won) via CAPI to refine optimisation.
10. Use company lists for ABM; pair with sales outreach and LinkedIn Sales Navigator.
11. Report pipeline and cost per opportunity, not only CPL.
12. Use UTM and CRM campaign codes to compare with other channels.

## 9. DON'Ts
1. Do not target extremely narrow audiences (under ~10k) and expect scale.
2. Do not expect consumer-level CPCs ($5-$15+ is common).
3. Do not judge by CTR or CPL alone; evaluate MQL/SQL.
4. Do not use only gated PDF offers for cold audiences without warming.
5. Do not reuse generic stock-image banners.
6. Do not overuse Message ads (spam and cap).
7. Do not leave Audience Network on without checking placement quality.
8. Do not mix retargeting pools too small to deliver.
9. Do not set bids below recommended range and then call the channel dead.
10. Do not skip the Insight Tag and CAPI setup.
11. Do not run too many audiences with split budgets (e.g. $10/day each).
12. Do not assume more layers of targeting improves quality; reach dies first.

## 10. Method of success (playbook)
1. Define ICP, offers per funnel stage, and CRM tracking (Insight Tag, CAPI, UTMs).
2. Launch: 1 prospecting campaign (job function x seniority x company size) with 3 creatives (thought leader, video, document); 1 retargeting campaign.
3. Learn (2 weeks): monitor CTR, CPC, CPL, form completion rate; fix targeting width; cut weak creative.
4. Qualify: compare lead-to-MQL/SQL by creative and audience; adjust offers and questions.
5. Scale: expand audience (add titles/adjacent industries), increase budgets, use Audience Expansion/Predictive Audiences; add ABM list campaigns.
6. Refresh creatives every 2-4 weeks; test new offers; rotate Thought Leader posts.
7. Validate: pipeline attribution, brand lift, account-level engagement, sales feedback.

## 11. KPI benchmarks (orders of magnitude; prefer the case's own benchmarks)
- Highly market and audience dependent; LinkedIn is the most expensive mainstream paid social platform.
- CPM: about $20-$100+ (B2B senior audiences at the top end).
- CPC: roughly $3-$15 (sponsored content); Message ads cost per send $0.2-$1+ [CHECK].
- CTR: sponsored content about 0.3-0.7%; video 0.3-0.6%; message open rates 40-60%+ for InMail but low click rate [CHECK].
- Lead Gen Form CVR: ~8-15% of clicks (open to submit) [CHECK]; CPL about $30-$150+ depending on audience/seniority; MQL to SQL conversion usually lower than other channels' MQL quality.
- Cost per opportunity/closed-won varies by ACV; LinkedIn often justified by higher ACV.

## 12. AI features on this platform
- AI-assisted campaign creation (Accelerate), AI-generated ad copy (introductory text and headlines), AI-assisted image suggestions, audience expansion/Predictive Audiences, AI-powered lead matching and "Buyer Groups" (account-level targeting) [CHECK], LinkedIn Premium AI-assisted recruiter tools (not ads).
- Automated bidding: Maximum delivery with optimisation for chosen objective.
- Disclosure: LinkedIn applies C2PA/Content Credentials ("CR" icon) to AI-generated images on the platform; ads policy forbids deceptive AI content; disclose where required by local regulation [CHECK].
- Practical: human subject-matter voice still outperforms generic AI copy in B2B.

## 13. Common traps in a case/competition setting
- Judging LinkedIn on CPC/CPM against Meta/Google: it will always look "expensive". Judge on cost per qualified lead/opportunity and ACV.
- Using LinkedIn for a consumer app or low-ticket goal (e.g. rides): poor fit unless the case targets B2B (corporate rides, drivers' recruitment is a possible edge case).
- Ignoring audience size and budget interplay: tiny audiences + tiny budget = no data.
- Choosing awareness metrics for a lead-gen KPI.
- Not accounting for sales cycle length: cannot measure revenue within 2 hours; use leading indicators (SQL rate, meetings).
- Counting form fills as qualified leads.
- Over-reliance on view-through (7-day view) default; separate click-based results.
