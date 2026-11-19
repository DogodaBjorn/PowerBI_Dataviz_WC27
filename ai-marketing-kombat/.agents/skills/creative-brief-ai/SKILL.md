---
name: creative-brief-ai
description: Schrijft een creative brief die een AI-creator (beeld/video-tool of mens met AI) zonder andere context kan uitvoeren, inclusief merkmoment, specs en een volledige must-not-appear-lijst. Gebruik bij "creative brief", "brief voor de AI-creator", "prompt voor Codex Design/Runway/Canva", of als een hypothese naar productie moet.
---

# Creative brief voor een AI-creator

**Standalone-regel**: de brief moet werken voor iemand die de case, de data en de andere stukken nooit zag. Geen "zie hypothese 1", geen interne ID's zonder uitleg. (In ronde 1 kostte dit een extra versie.)

## Velden (gebruik de velden van het template als die er zijn; anders deze)
1. **Which hypothesis it brings to life**: één regel bovenaan.
2. **Hypothesis**: waarom dit zou moeten werken, met het bewijs in gewone woorden.
3. **Format and size**: exact (1080x1920, 1080x1080), static/motion/UGC, lengte, leverbestanden (PNG + gelaagd), taalvarianten.
4. **Channel and placement**.
5. **Who is in it**: leeftijd, achtergrond, kleding, houding, wie er nog meer is, setting met sfeer maar zonder echte adressen of merken.
6. **The brand moment**: het ene beeld/moment waaraan de kijker het merkvoordeel ziet, met hoeveel van het beeld het inneemt en hoe lang (video). Exacte UI-teksten en bedragen als er een app-scherm in zit.
7. **Headline, visual, CTA**: letterlijke teksten per taal, font, kleur, plaats, logo-plaatsing, AI-label ("Created using AI") als de brief dat vraagt.
8. **Scene by scene** (video): seconde 0-2 hook, daarna het merkmoment, max lengte.
9. **Music and voice**: origineel, geen herkenbare artiest, genre, taal; wat niet (bv. muziek uit verkeerd land).
10. **Must not appear**: volledig, zie checklist hieronder.

## Must-not-appear-checklist (standaardfouten van AI-tools)
- Verboden woorden uit de brief, ook als citaat.
- Merken van derden: telefoonlogo's, automerken, kentekens, winkelnamen, concurrentkleuren of -layouts.
- Echte adressen, straatnamen, herkenbare gebouwen, echte personen of hun gelijkenis.
- Verkeerde cast/locale, generieke stockuitstraling, placeholder-namen uit een brandkit.
- Onleesbare of verbasterde tekst in beeld; tekst in het beeld laten zetten in plaats van renderen.
- Handen, vingers, fysica; gordels om voor iedereen in een auto.
- Luxe of te nieuwe producten als de brief "niet upmarket" zegt; omgekeerd: goedkope uitstraling bij luxe.
- Religieuze plekken, alcohol, roken, scheldwoorden, ook in muziek, als de brief dat uitsluit.
- Claims die de brief niet toestaat (veiligheid, snelheid, korting, "beste").
- Valuta en eenheden van het verkeerde land.

## Daarna
- Optioneel: zet de brief om naar een prompt voor de tool (Codex Design, Runway, Canva). Prompt = scène + merkmoment + tekst apart + negatieve lijst.
- Draai `inlever-check` op de brief.
- Kennis: `knowledge/creative/creative-principles.md`, `knowledge/ai-marketing/ai-disclosure-and-risk.md`.
