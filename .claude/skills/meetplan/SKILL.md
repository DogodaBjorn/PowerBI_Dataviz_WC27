---
name: meetplan
description: Maakt een meetplan voor een campagne of AI-toepassing: welke KPI, welke events en tracking (CAPI, Enhanced Conversions, Consent Mode, MMP, offline conversies), en hoe je de toegevoegde waarde incrementeel bewijst (holdout, geo-lift, conversion lift, MMM). Ook als tracking-audit. Gebruik bij "meetplan", "hoe meten we dit", "incrementaliteit", "tracking audit", "attributie", "bewijs dat het werkt".
---

# Meetplan

## 1. Van doel naar meetbare KPI
| Laag | Vraag | Voorbeeld |
|---|---|---|
| Business-doel | Wat moet er gebeuren? | 150k nieuwe rijders / meer boutique-verkoop |
| Primaire KPI | Welke ene metric beslist? | CPA eerste rit / omzet uit afspraken |
| Signalen (leading) | Wat zie je eerder? | installs, afspraakaanvragen, hook rate |
| Guardrails | Wat mag niet verslechteren? | merkzoekvolume, retourpercentage, merksentiment |

## 2. Eventplan
Per event: naam, definitie, waar het vuurt (app, site, boutique/CRM), welke bron (pixel + CAPI, Enhanced Conversions, MMP, offline import), deduplicatiesleutel, consentafhankelijkheid, en welk platform erop optimaliseert. Optimaliseer op het diepste event met genoeg volume (richtlijn ~50 per week per ad set op Meta [CHECK]).

## 3. Tracking-audit (checklist)
- Conversie-API's actief en gededupliceerd (Meta CAPI, TikTok Events API, Google Enhanced Conversions); matchkwaliteit.
- Consent Mode v2 in de EER; aandeel geweigerde consent bekend.
- iOS: SKAdNetwork/AdAttributionKit-setup via MMP; conversiewaardeschema dekt het business-event.
- Offline/CRM-conversies terug naar de platforms (cruciaal bij luxe en lange beslistrajecten).
- UTM-conventie en GA4-kanaalgroepering kloppen.
- Een bron van waarheid buiten de platforms (MMP, GA4, server-side verzamelaar of data warehouse).

## 4. Incrementaliteit: kies de methode
| Situatie | Methode |
|---|---|
| Eén kanaal, genoeg volume | Platform conversion lift / holdout |
| Lokaal te splitsen, offline effect | Geo-lift (bv. GeoLift, Meridian geo) |
| Hele mix, lange termijn | MMM (Meridian, Robyn), gekalibreerd met experimenten |
| AI-toepassing (bv. personalisatie) | Willekeurige holdout van klanten of boutiques |
| Weinig volume (luxe) | Langere looptijd, geaggregeerde regio's, Bayesiaanse inschatting, leading indicators |
Driehoek: attributie voor de dag-tot-dagsturing, experimenten voor het causale bewijs, MMM voor de verdeling. Zie `knowledge/measurement/`.

## 5. Output (Engels, voor inlevering)
- Primary KPI + target, with formula.
- Events and sources (compact table).
- How we prove incrementality (method, holdout size, duration, decision rule).
- Reporting cadence and who decides.
- Risks: consent loss, iOS signal loss, low volume; mitigation.

## Valkuilen
- Succes meten met de metric die het systeem zelf optimaliseert.
- Platform-gerapporteerde conversies optellen over kanalen heen (dubbeltelling).
- Een holdout te klein of te kort om iets te kunnen zien. Reken de minimale detecteerbare effectgrootte uit (`knowledge/measurement/experiment-design.md`).
