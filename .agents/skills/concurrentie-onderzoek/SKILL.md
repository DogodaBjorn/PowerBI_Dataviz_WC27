---
name: concurrentie-onderzoek
description: Haalt in korte tijd concurrent-, trend- en klantbewijs op dat een hypothese zichtbaar vormt: Meta Ad Library, Loudbox (creatives, reviews, brand assets), WebSearch. Gebruik bij "wat doet de concurrent", "reviews", "Ad Library", "trend", "Loudbox", of als een hypothese bewijs van buiten nodig heeft.
---

# Concurrentie- en trendonderzoek (timebox 10 minuten)

Regel: onderzoek telt alleen als het zichtbaar een hypothese, boodschap of brief vormt. Begin daarom bij de vraag, niet bij de bron.

## 1. Stel de vraag
Welke hypothese of keuze wordt sterker met extern bewijs? Bv. "spreken klanten van de concurrent over onverwachte prijzen?", "wat beloven de lopende ads van de concurrent precies?".

## 2. Bronnen
| Bron | Hoe | Levert |
|---|---|---|
| Loudbox demo (`loudbox-demo` MCP) | `describe_demo_data` eerst, dan `query_demo_data`, `get_creative_preview` | Creatives met previews/keyframes, brand assets, klantreviews |
| Meta Ad Library (`claude_ai_Meta_Ad`, laad met ToolSearch `ads_library_search`) | zoek op merk/pagina en land | Lopende ads, aanbod, voorwaarden, looptijd, formats |
| Google Ads Transparency Center, TikTok Creative Center/Top Ads | WebSearch/WebFetch | Ads en trends per markt |
| App-store reviews, Trustpilot, Reddit | WebSearch, Loudbox | Klanttaal, pijnpunten, letterlijke quotes |
| Nieuws/marktdata | WebSearch | Context voor updates |

## 3. Noteer per bevinding
`Bevinding · Bron/tool · Letterlijk citaat of getal · Welke hypothese het voedt`
Schrijf naar `rondes/<ronde>/onderzoek.md`.

## 4. Gebruik
- Zet klantcitaten in het veld Insight and source van de hypothese.
- Zet concurrentaanbod in de case-update-regel of als reden voor een boodschapkeuze.
- Noem in "How we worked" welke tool het gaf.

## Valkuilen
- Concurrenten noemen in creatives of boodschappen (vaak verboden).
- Te lang zoeken: na 10 minuten stoppen met wat je hebt.
- Previews niet zelf bekijken en toch beschrijven.
