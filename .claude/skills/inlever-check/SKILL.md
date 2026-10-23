---
name: inlever-check
description: Toetst een inlevering (hand-in, creative brief, pitch) regel voor regel tegen de brief en het template, draait de verbodenwoordencheck en rekent alle getallen na. Gebruik vóór insturen, bij "check", "laatste check", "klopt dit met de brief", of 15 minuten voor het eind.
---

# Inlever-check: de brief is wet

Dit was in ronde 1 het meest waardevolle kwartier: 6 harde fouten gevangen.

## Werkwijze
1. Lees de brief opnieuw helemaal (niet uit het geheugen) en het template. Lees de inlevering helemaal.
2. Draai de woordcheck:
   ```
   python -I scripts/woordcheck.py rondes/<ronde>/inlevering.md --regels rondes/<ronde>/regels.md
   ```
   `regels.md` bevat een blok `## Verboden woorden` met één woord of frase per regel. Het script meldt elke treffer met regelnummer.
3. Reken elk getal na: totalen tellen op, percentages kloppen, CPA's volgen uit spend ÷ events, valuta consequent.
4. Loop de checklist af en schrijf de bevindingen naar `rondes/<ronde>/check.md`, gesorteerd op impact.

## Checklist
**A. Formulier**
- Alle verplichte onderdelen aanwezig, in de gevraagde aantallen (bv. 3-5 inzichten, precies 3 hypotheses).
- Veldwaarden letterlijk uit het template (formaten, formatnamen, kanaalnamen).
- Lengtegrenzen (max regels, max woorden).
- De "one line on which hypothesis it brings to life" en vergelijkbare kleine verplichte regels.

**B. Harde regels**
- Elke regel uit `regels.md` afgevinkt, per onderdeel (hypotheses én brief).
- Merkvoordeel zichtbaar zoals de brief het definieert (niet alleen in een eindkaart of voetnoot).
- Geen concurrenten, merken van derden, verboden claims, cultuurregels geschonden.

**C. Bewijs**
- Elke bewering in de inzichten heeft een getal of bron.
- Onderzoek staat zichtbaar in een hypothese, niet alleen in "how we worked".
- Geen beeldbeschrijving die niet geverifieerd is.

**D. Ongebruikte hints**
- Welke zinnen uit de brief kunnen een hypothese of de creative brief nog sterker maken? Noem max 5, met waar ze passen.

**E. Leesbaarheid voor de jury**
- Elke tabelcel begint met de kern. Geen jargon dat de brief niet gebruikt.
- Updates: één regel per update.

## Output
Kort in de chat: "Moet veranderen" (harde fouten, met de fix), "Kan beter" (max 5), "Laten zoals het is". Daarna fixes doorvoeren als Bjorn ja zegt, of direct als hij gezegd heeft dat het mag.
