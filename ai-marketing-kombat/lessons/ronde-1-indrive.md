# Lessen uit ronde 1 (inDrive Nigeria, 21 okt 2026, 60 minuten)

Bron: werkmap `rondes/2026-10-21-indrive/` (tot 19 nov 2026 `E:\InDrive Kombat`; hand-in-stage1.md, brief-laatste-check.md, loudbox-bevindingen.md) en het sessieverloop.

## Wat werkte
1. **Zelf doorrekenen leverde de sterkste inzichten.** CPI, IPM, eerste ritten en ritratio per creative berekend. Daaruit: "goedkope installs voorspellen geen rijders" (CTR vs ritratio r = -0,02) en "zonder NG-01 is de blended CPA $5,75 in plaats van $3,82" (concentratiecheck).
2. **Inzichtformat Insight · Evidence · So what**, met getallen én formule in de evidence. Jury ziet dat je gerekend hebt.
3. **Loudbox MCP gaf feiten die niemand anders had**: dezelfde keyframe bij winnaar en verliezer (format beslist, niet het beeld), gedeeld eindscherm bij vier TikToks (de hook beslist), een celebrity-project als vervuiler, de ₦3.000-cap van de concurrent-promo via Ad Library, en klantreviews als persona-bewijs.
4. **Twee AI's naast elkaar** (Claude + ChatGPT) en dan samenvoegen. ChatGPT leverde "$4,00 = $600k ÷ 150k" en "100 eerste ritten voor je schaalt".
5. **Een aparte laatste check van de brief tegen het plan** (brief-laatste-check.md) ving 6 harde fouten: formaat alleen 9:16 of 1:1, formatnamen moeten "Static, motion or UGC" zijn, gordels voor bestuurder én passagier, geen telefoonmerk, geen echte straatnamen in UI-mocks, en de message-split klopte niet met het budget.
6. **Ongebruikte hints uit de brief** maakten het onderscheidend: "most rides are shared" (tweede persoon in beeld), "market is oversupplied" (drie chauffeurs reageren), festive season, peer trust → UGC.

## Wat beter moet
1. **Opstarttijd.** De MCP werd pas bij de start toegevoegd en de eerste vraag ging over brand guidelines. Zet tools en werkmap vóór de start klaar (skill `ronde-start`).
2. **Afgebroken antwoorden.** Een lang antwoord brak af ("Your response above was cut off"). Schrijf naar bestanden in delen.
3. **De creative brief moest standalone zijn.** Pas in v3 was hij leesbaar zonder de rest. Begin meteen met een brief die een AI-creator zonder context kan uitvoeren (skill `creative-brief-ai`).
4. **Te veel versies** (brief v2, v3, xlsx v2, v3, filled). Eén werkbestand per onderdeel, versies alleen in git.
5. **Beeld eerst bekijken, dan beschrijven.** Beide AI's beschreven NG-01 als "passagier voert prijs in"; het keyframe toont een interfacevergelijking zonder persoon.
6. **Een puur cijfermatige pass koos de verkeerde winnaar** (NG-15, $0,49 CPA, maar meer ritten dan installs). Sanity checks vóór ranking.
7. **Verboden woord in de inzending.** `scripts/woordcheck.py` vond achteraf "taxi" twee keer buiten de must-not-lijst (hypothese 1: "no taxi symbols"; creative brief: "no taxi checker pattern"). Ook in een ontkenning telt het woord. Draai de woordcheck altijd vóór insturen.
8. **Formulier eerst lezen.** Het inlevertemplate (xlsx) bepaalde de velden en de toegestane waarden. Lees het template in de eerste 10 minuten.

## Jury-patronen om te onthouden
- "Competitor and trend research counts only if it visibly shaped one of your hypotheses": zet het in de hypothese, niet alleen in "how you worked".
- "Insight and source" wil een briefsectie (A2, A3), creative-ID's of een concurrent-ad/trend. Altijd minstens twee soorten bron.
- Scale/stop moet een resultaat-KPI zijn met drempel én minimum data. Ambitie per hypothese: als het bewijs $1-2 haalbaar maakt, zet de scale-drempel daar.
- Updates: één regel per update, ook "changed nothing because ..." is toegestaan.
- "How you worked": max 5 regels, minstens één gevangen AI-fout.
