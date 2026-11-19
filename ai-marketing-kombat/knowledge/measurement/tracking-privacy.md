# Tracking, Signal Quality and Privacy

Why it matters: ad algorithms optimize on the events you send. Bad/late/missing events = wrong optimization and false CPAs. Check tracking before blaming creative.

## 1. Server-side and enhanced signals

| Tool | What | Key details | Pitfall |
|---|---|---|---|
| Meta Conversions API (CAPI) | Server-to-server events to Meta (alongside or instead of pixel) | Send hashed (SHA-256) email/phone/name/etc., client_ip, user_agent, fbp, fbc (from fbclid); event_id shared with pixel for de-dup; event_name matches pixel; Event Match Quality (EMQ) score in Events Manager; for apps: App Events via SDK or MMP + CAPI for app events [CHECK]; Conversions API Gateway = no-code setup | Missing event_id = double counting; late events (>7 days) ignored; wrong value/currency |
| Google Enhanced Conversions | Hashed first-party data (email/phone/address) sent with conversion tag to improve match | Enhanced conversions for web (tag-based) and for leads (offline upload with GCLID or hashed identifiers); uses SHA-256 | Needs consent; do not send before consent in EEA |
| Google offline conversion import | Upload CRM outcome with GCLID/GBRAID/WBRAID | Lets bidding optimize to qualified/closed events | Upload lag must be inside the window |
| Consent Mode v2 | Consent signals (ad_storage, analytics_storage, ad_user_data, ad_personalization) | Required for Google ads personalization and measurement in the EEA/UK since March 2024; Basic (tags blocked until consent) vs Advanced (cookieless pings sent, enabling conversion modelling) | No consent signals = loss of audiences and conversion modelling in EEA; implement via a Google-certified CMP |
| Server-side tagging (sGTM) | GTM server container on your own (sub)domain relays events to vendors | Benefits: first-party context, longer cookie life (Safari), control over data sent, faster pages, can enrich events (margin, CRM status), filter PII; run on Cloud Run / App Engine / managed providers | Costs infrastructure money; not a consent bypass; misconfigured domain = no benefit |
| TikTok Events API | Server events to TikTok (and Pixel) | Send ttclid, ttp (cookie), hashed email/phone, event_id for de-dup; Events API via partners/GTM; [CHECK] latest matching fields | Same de-dup and consent rules |
| MMP + SDK (apps) | SDK or server-to-server events from the app to MMP, MMP postbacks to networks | Pass key events (first ride, purchase value) and revenue; configure postback mapping for each network | Event renamed/unmapped = optimization on the wrong event |
| LinkedIn Conversions API | Server events including offline CRM stages | Helps B2B quality loop | Requires LinkedIn click ID (li_fat_id) or hashed email |

Signal quality checklist (5 minutes):
1. Is the business event (first ride / purchase) actually sent to the platform, with value?
2. Do platform counts reconcile with backend/MMP within a tolerable margin (+/-10-20%; more is a flag)?
3. Event de-dup via event_id working? Duplicate rate?
4. EMQ / match rate acceptable (Meta: aim for good or higher [CHECK])?
5. Latency: events arrive within hours, not days?
6. Consent coverage: what share of traffic has consent, and what is modelled?

## 2. Privacy law basics (not legal advice)

- GDPR (EU/UK GDPR): lawful basis required; for ad tracking via cookies/identifiers consent is the usual basis. Rights: access, erasure, objection, portability. Data minimization, purpose limitation, DPAs with vendors, international transfers need safeguards (EU-US Data Privacy Framework [CHECK] status).
- ePrivacy Directive (cookie law): consent needed before storing/reading non-essential data on a device (cookies, local storage, SDK identifiers), regardless of whether data is personal.
- Valid consent: freely given, specific, informed, unambiguous, as easy to withdraw as to give; no pre-ticked boxes; reject as easy as accept (regulator guidance, e.g. CNIL).
- Hashing is not anonymization: hashed emails remain personal data.
- Special categories (health, religion, etc.) and sensitive targeting are restricted by laws and platform policies (Meta removed many detailed targeting options).
- Other regimes: CCPA/CPRA (US California, opt-out of sale/sharing), LGPD (Brazil), PIPEDA (Canada), Nigeria NDPA 2023 (consent, data subject rights, cross-border transfer rules) [CHECK], Kenya DPA, South Africa POPIA. For a Nigeria case: Nigerian Data Protection Act applies for local users; GDPR relevant only for EEA users.
- Apple: ATT requires opt-in for cross-app tracking; SKAN/AAK is the privacy-preserving route. Google Play: Data Safety section; GAID rules.
- Kids: restrictions on targeting minors across platforms.

## 3. Cookie and identifier landscape (status as of mid-2026) [CHECK all rows]

| Item | Status | Implication |
|---|---|---|
| Chrome third-party cookie deprecation | Google dropped the plan to force removal (2024-25); Chrome keeps third-party cookies with user choice via existing settings [CHECK latest]; Privacy Sandbox ad APIs largely retired in 2025 [CHECK] | Do not assume cookies vanish; do not rely on them either |
| Safari ITP / Firefox ETP | Third-party cookies blocked; first-party cookie lifetimes capped (JS-set cookies 7 days; link-decoration restrictions) | Server-set first-party cookies and sGTM help |
| Apple ATT / SKAN / AAK | Active; low opt-in rates | Aggregated iOS measurement; modelling |
| Android Privacy Sandbox / GAID | GAID still used; Privacy Sandbox on Android scaled back [CHECK] | Android attribution mostly deterministic still |
| Ad blockers / browser privacy features | Block pixels for a meaningful share of desktop users | Server-side events recover part |
| Consent rejection | 30-60% in EEA depending on CMP design [CHECK, wide range] | Modelled conversions, first-party data |

## 4. First-party data strategy

- Collect: login, email/phone with value exchange (loyalty, booking, receipts), in-app events, surveys (zero-party).
- Store: CDP or warehouse (BigQuery/Snowflake/Fabric), consent flags stored with the profile.
- Activate: customer match / custom audiences (hashed), CAPI/Enhanced Conversions, value-based lookalikes, suppression lists, CRM lifecycle journeys, offline conversion import.
- Measure: backend as source of truth, MER, incrementality tests, MMM.
- Governance: consent management, retention policy, DPAs, data clean rooms for partners (Meta Advanced Analytics, Google Ads Data Hub, Amazon Clean Rooms [CHECK names]).
- Priorities by effort: (1) send the real business event with value, (2) de-dup via event_id, (3) CAPI/Enhanced Conversions with hashed identifiers (consented), (4) sGTM on own domain, (5) offline/CRM quality events, (6) clean rooms/MMM.

## 5. Jury one-liners

- "We send the first-ride event with value to every channel so each algorithm optimizes the real outcome, not installs."
- "Server-side events plus consent-aware tagging recover signal without bypassing consent."
- "We measure through a first-party source of truth and verify it with incrementality tests."
