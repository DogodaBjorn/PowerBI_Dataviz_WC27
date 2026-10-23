# AI across the marketing funnel (2026 view)

Status: 2026-10-23, from background knowledge (no live lookup); maturity ratings are judgement. Tool names change fast: [CHECK] versions/availability before naming in a pitch.
Maturity: M = mature (safe to run in production), E = emerging (works with human review), X = experimental (pilot only).

## 1. Use cases by funnel stage

| Stage | What AI does | Maturity 2026 | Example tools (generic / named) | KPI impact | Main risks |
|---|---|---|---|---|---|
| Research / insight | Summarise reports, mine reviews/forums/social, cluster themes, competitor ad analysis, synthetic personas to pressure-test ideas | M (summarising, clustering); X (synthetic personas as truth) | LLMs (Claude, ChatGPT, Gemini); Perplexity; Brandwatch, Talkwalker, Sprinklr; Meta Ad Library, Google Ads Transparency | Faster insight cycle; better brief quality | Hallucinated stats, biased sample, synthetic personas mistaken for real research |
| Strategy | Scenario planning, positioning options, messaging matrices, media-mix hypotheses, brief drafting | E | LLMs with company knowledge; Notion AI; custom GPT/Claude projects | Time to strategy; fewer blind spots | Generic outputs; no brand insight; over-trust |
| Creative generation (image/video) | Backgrounds, scenes, variants, resizing, motion, voice-over, music, lip-sync/translation | M (variants, resizing, backgrounds); E (video clips); X (full ad from prompt for premium brands) | Midjourney, Firefly, Imagen, Flux, GPT-image; Runway, Veo, Sora, Kling, Luma, Pika; ElevenLabs; HeyGen/Synthesia; Canva, Photoshop Generative Fill; Meta Advantage+ creative | Output volume; test velocity; cost per asset | Wrong details (hands, text, logos), generic look, IP/likeness, label obligations, product misrepresentation |
| Copy | Headlines, descriptions, ad variants, localisation, tone-checks | M | LLMs; Google Ads asset generation; Meta text variations; Jasper, Copy.ai | Variant count; CTR/CVR with testing | Off-brand tone, claims not substantiated, sameness |
| Personalisation | Dynamic creative, next-best-offer, onsite recommendations, email send-time | M (recs, send-time); E (generative one-to-one) | Dynamic Yield, Bloomreach, Klaviyo, Braze, Salesforce Einstein, Adobe Target | CVR, AOV, retention | Privacy, creepiness, filter bubbles |
| Media buying / bidding | Automated bidding, audience expansion, budget allocation, creative optimisation, anomaly alerts | M (smart bidding, PMax, Advantage+) | Google Smart Bidding, PMax, Demand Gen; Meta Advantage+; TikTok Smart+; Amazon DSP; The Trade Desk Kokai; Optmyzr, Skai | CPA/ROAS, scale | Black box, placement control, brand safety, cannibalisation, learning phase on low volume |
| Measurement | MMM, incrementality, attribution, anomaly detection, report narration | M (MMM tooling); E (LLM analysts); X (auto-experiments) | Google Meridian, Meta Robyn, PyMC-Marketing; Measured, Haus, Recast, Northbeam; GA4; Looker/Power BI + LLM | Better budget decisions; waste reduction | Low-volume data, false precision, black-box models |
| CRM / lifecycle | Segmentation, churn/propensity, lead scoring, content generation, journey orchestration | M | HubSpot, Salesforce, Braze, Klaviyo, Iterable; CDPs (Segment, mParticle) | LTV, repeat rate | Consent, data quality |
| Customer service | Chatbots, agent assist, email triage, voice AI | M (FAQ, triage); E (full resolution) | Intercom Fin, Zendesk AI, Ada, Salesforce Agentforce, custom RAG bots | CSAT, response time, cost to serve | Wrong answers, brand voice, escalation failure; disclose AI (EU AI Act Art. 50) |
| SEO / GEO | Content briefs, entity optimisation, schema, AI-answer monitoring, internal linking | M (SEO assist); E (GEO measurement) | Semrush, Ahrefs, Surfer, Clearscope; Profound, Peec AI, AthenaHQ (GEO) | Organic visibility, AI-answer share | Spam-content penalties, hallucinated facts, unstable GEO metrics |
| Social / community | Listening, reply drafts, trend alerts, UGC curation | M (listening); E (auto-reply) | Brandwatch, Sprout Social, Hootsuite | Sentiment, response time | Tone-deaf auto replies |
| Commerce / feed | Product-data enrichment, attribute tagging, feed optimisation | M | Feedonomics, DataFeedWatch, Channable; GPT/Gemini enrichment | Shopping CTR, ROAS | Wrong attributes, image-label metadata (AI images in Merchant Center) |

## 2. Agentic marketing workflows

Definition: an LLM-driven agent that plans, calls tools (APIs, MCP servers, browsers), checks results and loops, instead of one-shot generation.

| Workflow | Steps | Typical tools | Maturity |
|---|---|---|---|
| Weekly performance analyst | Pull data (Google Ads/Meta/GA4 APIs) -> detect anomalies -> hypothesise -> draft report + recommended actions | MCP connectors (Google Ads, Meta Ads, GA4), LLM, BI | E |
| Creative production line | Brief -> concept ideas -> image/video generation -> brand-rules check -> human review -> upload to platform -> tag with hypothesis | Claude/GPT, Runway/Veo, Canva API, DAM, ad-platform API | E |
| Search-term and negative keyword guardian | Review search terms daily -> classify intent (fake/replica/cheap) -> propose negatives | Google Ads API, LLM | M/E |
| Lead qualifier + booking agent | Enquiry arrives -> enrich -> score -> reply or route -> book appointment -> brief advisor | CRM API, LLM, calendar | E |
| GEO monitor | Query list across AI engines -> capture answers/citations -> flag errors -> suggest content fixes | Peec/Profound or custom scripts | E |
| Competitive watch | Scan competitor ads, launches, press -> weekly digest | Ad libraries, web search, LLM | M |
| Self-optimising budget agent | Reallocates spend autonomously across channels | Platform APIs | X (keep human approval for spend changes) |

### Human-in-the-loop design (use this on a slide)
- Tiering: AI proposes, human approves anything customer-facing, spend-changing or brand-defining. Auto-execute only low-risk, reversible tasks (tagging, reporting, negative keyword suggestions with review).
- Guardrails: brand rulebook as machine-readable checklist; restricted tool permissions (read-only by default; spend caps); audit log of every action; kill switch; sampling QA of outputs.
- Escalation: confidence thresholds, VIP client flag = always human.
- Feedback loop: advisors/art directors rate outputs; ratings feed prompt updates and evaluation sets.
- Evaluation: golden test set (50-100 examples), regression tests per prompt change, red-team for off-brand/unsafe outputs.
- Governance: data-processing agreement, model/vendor register, GDPR DPIA for personal data, AI-disclosure policy (see ai-disclosure-and-risk.md).

## 3. How to present an AI solution to a jury (template)

Order: problem -> AI mechanism -> data needed -> guardrails -> KPI + incrementality -> pilot 30/60/90 -> risks. Aim for 1 slide per row, or 1 slide total plus demo.

1. Problem (1 sentence, one number)
   - e.g. "Boutique sales are invisible to ad platforms, so algorithms optimise for cheap clicks."
2. AI mechanism (what the AI does, in plain language, with a simple diagram)
   - Input -> model -> output -> action -> feedback.
3. Data needed (and who owns it)
   - First-party: CRM, boutique sales, enquiry forms, product catalogue. External: platform data, search trends. Consent status. Data quality gaps.
4. Guardrails
   - Brand rules, human approval points, privacy, disclosure labels, kill switch, QA sampling.
5. KPI and how to measure incrementally
   - Primary KPI (e.g. cost per qualified appointment), secondary (lead quality, AOV, brand search), guardrail KPIs (frequency, brand-safety incidents, complaints).
   - Test design: geo holdout or lift test or A/B vs current process; minimum detectable effect; run-length; success threshold stated up front.
6. Pilot plan
   - Days 0-30: set-up (data, consent, tracking, baseline, brand rulebook, evaluation set), launch on one market/channel.
   - Days 31-60: run test vs control, weekly human review, tune prompts/models, add second use case.
   - Days 61-90: read incrementality, decide scale/stop, document playbook, extend to next market, hand over to team.
   - Include budget range and team time.
7. Risks and mitigations
   - Brand risk (off-tone) -> human approval; legal (labels, IP) -> checklist; data (privacy) -> consent + hashing; performance (low volume) -> value-based signals + MMM; dependency (vendor lock-in) -> model-agnostic design.

Jury tips
- Lead with business outcome, not tool names. One concrete example beats a feature list.
- Show the human role explicitly (advisor, art director). Luxury juries distrust "replacing craft".
- State what you will NOT do with AI (e.g. generate the jewellery itself, auto-discount).
- Show one number the jury can remember (e.g. "target: 20% lower cost per qualified appointment, tested with a geo holdout").
- Have a fallback demo screenshot; do not depend on live generation.

## 4. Quick maturity guide for claims

- Safe to claim as proven: smart bidding with conversion value, MMM, AI copy variants, AI customer-service triage, feed enrichment, send-time optimisation.
- Claim with caveats: generative video ads for luxury, AI concierge, GEO measurement, AI lead scoring (needs data).
- Avoid claiming: autonomous end-to-end campaign management, fully AI-generated hero creative for a heritage jewellery brand, synthetic personas as research.
