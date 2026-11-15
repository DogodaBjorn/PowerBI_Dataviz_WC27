# Review final-check-publish7 (15 nov 2026)

Bron: branch `rebuild-finalv3`, map `project/deliverables/final-check-publish7/`. Onafhankelijk nagekeken op de gepubliceerde service-kopie (Goodnight Inn, ververst 15 nov 18:10 CET) en op de pakketbeelden. Geen code, instellingen of merges aangeraakt.

## Oordeel
Klaar om in te leveren op inhoud en leesbaarheid van wat ik kon controleren. Eén ding kon ik zelf niet bewijzen (klik op de Build-keuzerijen, zie onder).

## Wat ik zelf heb gecontroleerd (publieke link, cookie-sessie)
- Pagina 1, pagina 2 Recommended en Build laden en renderen.
- Build opent op pakket A: "Picked: 3 moves, $9.4M of $60.0M", "Low -$5.5M · High +$12.7M". (In de ingelogde eigenaarssessie kan een onthouden keuze zichtbaar zijn: dat is geen fout.)
- De zeven publish-7-regels (B1, B3, B4, B6, B7 en B2 Expected) staan zo op de pagina. Scenario Low/High-kop en tegels kloppen. Getallen C1-C9 zijn onderling consistent.
- Alle visuals op p1, p2 en de tooltippagina's zijn native Power BI-types (actionButton, cardVisual, lineChart, scatterChart, tableEx, advancedSlicerVisual, bar/column/area, shape, image, textbox). Geen custom visual-pakketten in report.json, dus geen Deneb in de huidige build. De regel "minimaal vier ingebouwde visuals" is ruim gehaald.

## Wat ik op de beelden zag (walkthrough 16-21, 03, 14, 18, 22)
- 16/17/19/20/21: de selector wisselt echt tussen toestanden (3, 6 en 8 moves, over budget, niets gekozen). Kop, tegels, scatterpunt "You" en de cumulatieve-cashlijn volgen mee. De boodschap bij over budget ("Over the $60.0M budget by $9.3M", "Not yet within the rules") en bij niets gekozen ("Pick at least three moves...") is duidelijk.
- Tooltips (03, 14, 18): leesbaar, getallen kloppen met de tabel, ze dekken alleen tijdelijk iets af.
- 22 (1366 px): schaalt netjes, kleiner maar leesbaar.
- Kanttekening: bij 8 moves krijgt de balkengrafiek "Your plan" een schuifbalk en valt de achtste rij (Energy programme) buiten beeld. Bij het maximale scenario ziet een jurylid dus niet alle bijdragen.

## Beperkingen, eerlijk
- Klikgedrag op de Build-rijen: met mijn tooling markeerde een klik de rij maar schakelde niet om. Dat kan een tooling-beperking zijn; de beelden 16-21 van de bouwer tonen wel het omschakelen. Doe zelf één klik in een schone (uitgelogde) browser vóór het insturen.
- Gate-claims van de bouwer (hit-test op 1920/1366, toetsenbordrondes zonder naamloze stops, nl/de gelijk aan en, 16276 px bij klik) heb ik gelezen, niet zelf nagemeten.
- Deadline volgens de officiële regels: 18 nov 23:59 PT = 19 nov 08:59 CET.

## Concrete verbeteringen (optioneel, via aparte branch)
1. Waterfall "Your plan" bij 8-10 moves: rijhoogte kleiner of grafiek hoger, zodat geen schuifbalk nodig is en alle bijdragen zichtbaar zijn.
2. Zet in de beschrijving één zin dat Build opent op pakket A en dat een klik op een rij een move toevoegt of weghaalt.
3. Doe vóór het insturen een laatste controle op de publieke link in een schoon venster: open, Build, één klik, terug naar pagina 1.
