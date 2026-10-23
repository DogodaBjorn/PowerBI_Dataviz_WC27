# AI disclosure, legal and brand-safety risk

Status: 2026-10-23. Written from background knowledge, NO live lookup: platform rules change often. Every rule below is [CHECK] on the platform's current help page before relying on it in a deliverable. Not legal advice.

## 1. Platform labelling rules (summary)

| Platform | Mechanism | What triggers it | Notes |
|---|---|---|---|
| Meta (Facebook/Instagram/Threads) | "AI info" label (replaced "Made with AI" in 2024); automatic label from C2PA/IPTC metadata and industry signals; advertiser/creator self-disclosure | Photorealistic images, realistic video or audio made/edited with AI; ads that use AI to depict real people or events in ways that could mislead | Ad tools with generative features (Advantage+ creative) may add labels automatically; undisclosed realistic AI content can get penalised [CHECK] |
| TikTok | AIGC label; auto-label via C2PA content credentials; creator toggle "AI-generated content" | Realistic AI-generated images, video, audio; AI avatars | Unlabelled realistic AI content can be removed or limited; ad policies require disclosure for AI-generated realistic content [CHECK] |
| YouTube | Creator disclosure "altered or synthetic content" in upload flow; label in description or on video player (more prominent for sensitive topics) | Realistic content that could be mistaken for real (real person says/does something they didn't; altered real events; realistic scene generated) | Not needed for clearly unrealistic/animated content, productivity use (script help, captions, beauty filter) [CHECK] |
| Google Ads | Ad policies: Misrepresentation, Manipulated media (deepfakes), Political content disclosure for synthetic/digitally altered election ads; general ban on deceptive content; Merchant Center requires AI-generated images to keep IPTC "trainedAlgorithmicMedia" metadata | Synthetic elements in election ads; AI-generated product images in feeds | Do not strip metadata from AI-generated Shopping images [CHECK] |
| LinkedIn | C2PA "CR" content credentials label | Content with provenance metadata | Auto-displayed [CHECK] |
| Pinterest | "AI modified" label, can filter AI content in feeds | AI-generated or modified images | [CHECK] |
| Snapchat | Context cards / watermark for AI-generated images | Snap AI features | [CHECK] |

Practical standard for the deliverable: embed C2PA/content credentials where tools support them, keep original files, keep a log (tool, prompt, date, reviewer), and tick the platform AI-disclosure toggle whenever realistic synthetic content appears. For luxury, prefer real photography of the product; use AI only for non-product context, and label.

## 2. EU AI Act transparency (Article 50)

- Article 50 sets transparency obligations: (a) AI systems interacting with people must tell them they are interacting with AI (chatbots), (b) providers of generative systems must mark outputs in a machine-readable format, (c) deployers of deepfakes must disclose that content is artificially generated or manipulated, (d) deployers of AI-generated text published to inform the public on matters of public interest must disclose, unless human-reviewed/editorially responsible.
- Application date: transparency obligations apply from 2 August 2026 [CHECK exact scope and any postponement: the European Commission's "Digital Omnibus" proposals (Nov 2025) discussed delays and transitional periods for parts of the Act, notably for marking obligations on systems already on the market; confirm the final text as of today].
- A Code of Practice on marking and labelling AI-generated content was being drafted by the Commission (2025-2026) [CHECK status and final guidance].
- Marketing implications: AI chat concierge must disclose "you are chatting with an AI assistant"; realistic deepfake-like people or voices in ads need a visible disclosure; artistic/creative/satirical works have a lighter disclosure ("in a way that does not hamper enjoyment") [CHECK]; keep provider-side watermark/metadata intact; non-EU companies serving EU users are in scope.
- Also relevant: GDPR (profiling, automated decisions, consent for personal data in prompts), ePrivacy/consent mode, DSA (ad transparency on platforms), Unfair Commercial Practices Directive (misleading imagery of products), consumer-protection rules on influencer/AI-influencer disclosure.
- Fines: up to EUR 15m or 3% of global turnover for transparency violations [CHECK].

## 3. Deepfake, likeness and IP risks

| Risk | Example | Mitigation |
|---|---|---|
| Likeness / voice | AI avatar resembling a celebrity or royal; voice clone | Written consent and contract for any real person; avoid "lookalike" prompts; no royals/political figures; ban using named people in prompts |
| Collaborator IP | Fabergé x 007 / Game of Thrones imagery in AI output | Check licence scope; do not ask AI to mimic licensed IP unless approved |
| Third-party brands | Generated phones, cars, clothes showing real logos | Negative prompts + review; remove or blur |
| Copyright / style mimicry | "In the style of [living artist]" or archival Fabergé works | No living-artist style prompts; historic works: verify rights of photographs/archives |
| Trademark | AI-generated copy that uses competitors' marks | Keyword/term filters |
| Training data / output ownership | Tools differ on commercial rights and indemnity | Use tools with commercial licence and IP indemnity (Adobe Firefly, Google, some enterprise tiers) [CHECK]; keep contracts |
| Fake heritage | AI-generated "archive" images presented as real | Never present AI imagery as historical documentation; label concept art |
| Data leakage | Client data pasted into public chatbots | Enterprise/zero-retention tools, DPA, no PII in prompts |
| Authenticity claims | "Hand-made" vs AI-generated visuals | Do not claim craftsmanship for AI visuals; keep real macro shots of real work |

## 4. Brand-safety and hallucination guardrails

- Grounding: use retrieval from approved sources (catalogue, provenance DB, brand book) for any factual claim; no free-form claims about stones, dates, prices, carat, origin.
- Rulebook as checklist: tone words, forbidden words (cheap, discount, sale, bargain, replica), forbidden imagery (clichés, political symbols), mandatory elements (logo placement, disclaimers).
- Human approval for: anything publicly visible, any price/availability statement, any provenance claim, any content with a person.
- Automated pre-checks: LLM-as-judge against brand rulebook, image classifier for logos/text errors, spelling/grammar, number match against catalogue.
- Logging: prompts, outputs, approver, version; retain for audit.
- Chatbots: scope-limited, refuse price negotiation and legal/medical/financial claims, hand over to humans, show "AI assistant" label, store transcripts under GDPR.
- Incident plan: kill switch, takedown contacts per platform, holding statement.
- Test sets: red-team prompts (political, sanctions, Russia topics, discount requests, competitor questions) before launch. Fabergé-specific: the bot must not comment on geopolitics, ownership, sanctions or Romanov history beyond approved copy.

## 5. Prompt/brief checklist for AI creators (image/video tools)

### Typical failures to prevent or check
- Hands/fingers: wrong count, merged, unnatural grip (especially when wearing rings!).
- Text rendering: garbled letters on signs, packaging, UI; fix by adding text in post (never rely on the model).
- Logos: invented or real third-party logos on phones, cars, bags, clothing; the brand's own logo distorted.
- Jewellery fidelity: wrong stone cut, wrong facets, wrong metal colour, invented gems, melting enamel; NEVER use AI to render the actual product, composite the real photo instead.
- Locale: wrong ethnicity/clothing/architecture/street signs/driving side/plug sockets for the target market; stereotyped depiction of regions (e.g. Gulf).
- Wrong era or cultural artefacts: anachronistic details in "historic" scenes, incorrect Russian imperial symbols (double-headed eagle misdrawn), wrong Cyrillic.
- Generic stock look: over-smooth skin, plastic bokeh, symmetrical faces, "AI sheen", over-saturated gold and teal-orange grading.
- Physics: reflections, shadows, light direction, liquid behaviour, objects passing through each other, gravity of fabrics and chains.
- Safety/realism: seat belts missing or wrong, drivers on phones, wrong traffic, no helmets, champagne pouring unrealistically, candles near fabrics.
- Video: temporal flicker, morphing faces, drifting product shape, lip-sync errors, time-lapse artefacts, audio mismatch.
- Anatomy and proportions: too-long necks (relevant to pendants), duplicated limbs, earrings mismatching left/right.
- Skin/age/beauty: unrealistic retouching; diversity tokenism; sexualised or objectifying output.
- Aspect ratio and safe zones: key subject cropped by platform UI.
- Metadata: C2PA lost on export; missing AI label.

### Standard prompt template (copy/paste)
```
Goal/channel/format: [Instagram Reel 9:16, 6s, sound-off]
Brand moment: [what must be visible, for how many seconds]
Subject: [who/what, age range, locale, clothing, no logos]
Setting: [location, time of day, light direction and quality]
Camera: [lens, framing, movement, depth of field]
Style: [reference words from brand book; restrained, negative space]
Colour: [palette; no neon, no heavy teal-orange]
Product: [REAL photo supplied as reference - do not re-draw]
Text on screen: [exact words, added in editing, not generated]
Must NOT appear: [competitor logos, brand logos on devices, hands in frame close-up, text in scene, political symbols, discount language, celebrities/royals]
Audio: [music/silence; voice guidance]
Disclosure: [AI label needed? C2PA on?]
```

### Review checklist before publish
1. Product faithful to the real photo (stone, metal, scale).
2. Zoom 200% on hands, faces, text, edges, reflections.
3. No third-party logos or real people lookalikes.
4. Locale/cultural check by a native reviewer.
5. Claims verified against catalogue/provenance.
6. Disclosure label set; metadata retained.
7. Brand rulebook pass (tone, palette, typography, no discount language).
8. Legal pass if licensed IP (Bond, GoT) or heritage claims.
9. Archive file: prompt, tool, version, reviewer, date.
