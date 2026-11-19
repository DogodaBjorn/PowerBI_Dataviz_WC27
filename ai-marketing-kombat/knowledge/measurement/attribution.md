# Attribution

One-line truth: attribution assigns credit, it does not prove cause. Every platform grades its own homework. Use it for day-to-day optimization, use experiments / MMM for the budget split.

## 1. Click vs view-through

| Type | Credit when | Strength | Weakness |
|---|---|---|---|
| Click-through (CTA) | Converted within window after a click | Strong evidence of influence | Misses upper-funnel/TV/social "seen not clicked" effects; branded search steals credit |
| View-through (VTA) | Converted within window after an impression, no click | Captures reach/video effect | High over-claim: people who were going to buy anyway get "viewed"; retargeting inflates it |
| Engaged-view | Watched >= N seconds (e.g. YouTube 10 s / Meta 5 s video) then converted | Middle ground | Platform-specific definitions [CHECK] |

Rule: report click-through and view-through separately; use view-through for directional upper-funnel reads only.

## 2. Platform default windows (verify before the round) [CHECK]

| Platform | Typical default | Notes |
|---|---|---|
| Meta | 7-day click + 1-day view (also 1-day click, 1-day engaged-view) | Meta reduced/removed some longer view windows (7d/28d view) in 2025-26 [CHECK]; reports differ between "Attribution setting" columns; modelled/aggregated for iOS opt-out users |
| Google Ads | 30-day click (adjustable to 90), 1-day view for YouTube/Display, engaged-view 3 days | Data-driven attribution default for most conversion actions; modelled conversions via Consent Mode |
| TikTok | 7-day click + 1-day view (also 1-day engaged-view) | Configurable [CHECK] |
| LinkedIn | 30-day click, 7-day view default [CHECK] | Often under-credited vs Google on B2B |
| GA4 | Data-driven (default), lookback 30 days acquisition, 90 days other events | Paid + organic; first/linear/time-decay/position-based models were removed in 2023 |
| MMP (AppsFlyer/Adjust) | Click 7 days, view 1 day (typical defaults) | Configurable per network |

Different windows = different numbers. Same-window comparison before any cross-platform comparison.

## 3. Last-click vs data-driven vs others

| Model | Idea | Use |
|---|---|---|
| Last click | 100% to last touch | Simple, conservative for upper funnel; rewards search/brand/retargeting |
| First click | 100% to first touch | Discovery view (GA4 no longer offers; do in BigQuery) |
| Linear / time decay / position | Rules | Rarely better than data-driven; illustrative |
| Data-driven (DDA) | ML estimates marginal contribution from converting vs non-converting paths | Better than last click if enough volume; still fed by tracked touches only (no TV, offline); not causal |

## 4. Why platforms over-claim

- Each platform counts its own touches: the same purchase can be claimed by Meta, Google and TikTok, and organic. Sum of platform conversions > actual conversions (often substantially).
- View-through and long windows take credit for conversions that would happen anyway (baseline).
- Modelled conversions fill gaps (iOS, consent denial) with assumptions the platform controls.
- Retargeting and branded search target people who are already converting.
- Auto-bidding optimizes toward people likely to convert regardless of ad (selection effect).
- Cross-device and cookie loss add noise in both directions.
How to say it: "Platform-reported conversions total 1.6x our actual orders. We use them for relative comparison inside a platform and calibrate the budget split with incrementality tests."

## 5. De-duplication

- Single source of truth: one system counts business events (MMP for apps, backend/GA4 for web), platforms import it.
- Use stable event IDs (event_id) so pixel/SDK and server events (CAPI) de-dup in Meta; use transaction_id for Google; same for TikTok Events API.
- MMP does last-touch (with the MMP's own rules) across all networks and de-duplicates for you. "Self-attributing networks" (SANs: Meta, Google, TikTok, Apple Search Ads, X) report their own installs which the MMP reconciles by passing click/impression data [CHECK per MMP].
- Reconcile weekly: platform sum vs MMP/backend vs finance. Ratio = over-claim factor. Apply it only for directional reads.
- Blended view: MER / blended CPA = total spend / total business events, immune to attribution disputes.

## 6. Mobile app attribution

### Android
- Google Play Install Referrer is the main deterministic click-to-install link; GAID availability and Privacy Sandbox on Android status [CHECK].
- Deterministic-ish; MMP matches clicks to installs; view-through via probabilistic/ID matching is limited.
- In markets with Android majority (e.g. Nigeria, much of Africa, India, SEA, LatAm) SKAN is a small part of the picture; but verify iOS share [CHECK].

### iOS
- ATT (App Tracking Transparency) opt-in is low in many markets; non-consented installs are attributed via SKAdNetwork (SKAN) or AdAttributionKit (AAK, iOS 17.4+, adds re-engagement and alternative marketplaces).
- SKAN: aggregated, delayed postbacks, a conversion value (6 bits in v3; fine/coarse values in v4+), crowd-anonymity thresholds, source identifier (campaign-level ID, 2-4 digits in v4), up to 3 postbacks in v4 (0-2 days, 3-7 days, 8-35 days). Hierarchical source IDs. Limited creative / ad set granularity.
- Consequences: you cannot rank 20 creatives on iOS by first-ride CPA from SKAN; use Android or in-platform modelled data for creative reads, and apply learning to iOS.
- Probabilistic attribution (fingerprinting) is prohibited by Apple policy; MMPs offer modelled/aggregated alternatives [CHECK]. 

### MMPs (AppsFlyer, Adjust, Branch, Singular, Kochava)
- Single install/event dedup across networks; postback events to networks; fraud filtering (Protect360, Fraud Prevention Suite); cohort retention reports; SKAN decoding; LTV and ROAS cohorts.
- Typical checks: click-to-install time (CTIT) distributions (very short = click injection, very long = click flooding), install-to-event delay, rejected installs, retention vs network.
- Event lag: first-ride/first-purchase postbacks can arrive hours to days later; ad platform optimization uses what it receives.

## 7. GA4 basics

- Event-based; key events (formerly conversions) are flagged events.
- Reporting identity: blended (user ID, Google signals, device ID, modelling). Behavioural modelling fills consent gaps.
- Attribution: data-driven / last-click models for Paid & Organic channels; lookback windows adjustable (30 days acquisition, 90 days other).
- UTM discipline: utm_source/medium/campaign consistent and lowercase; auto-tagging (gclid) for Google Ads; Meta/TikTok need manual UTM params ({{campaign.name}} etc.).
- Mismatches vs ad platform: GA4 credits by session source (click-based), platforms by their own window and view-through; so platform > GA4 normally.
- Sampling/thresholding: small cohorts may be hidden; use BigQuery export for rigor.

## 8. How to talk about it in a jury (3 lines)

1. "Platforms over-claim, so we judge on one deduplicated source (MMP/backend) and use the same attribution window for every channel."
2. "We use attribution to optimise within channels and incrementality tests to set the budget between channels."
3. "iOS signals are aggregated and delayed, so creative-level decisions come from Android/in-platform data and are applied cautiously to iOS."

Checklist when you receive data: which window, click or view, which tool (MMP vs platform vs GA4), event definition, time lag, last-touch or data-driven, were conversions modelled?
