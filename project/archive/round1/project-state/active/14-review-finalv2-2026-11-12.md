# 14 - Review FinalV1 naar FinalV2, 12 november 2026

**Datum:** 2026-11-12 · **Op verzoek van:** Bjorn ("nog één keer een volledige review om hem van FinalV1 naar FinalV2 te brengen, finale-waardig ook op de details") · **Bekeken:** branch `feedback-ronde-4` (commit `1361f71`, Björns Desktop-save van 12 nov): alle twaalf renders in `project/deliverables/screenshots/ScreenshotsFinalV1/` pixel voor pixel, met 2x-uitsnedes van de kopzones, de F2-lijnlabels en de bereikbalk van de pakket-tooltip; de README van de set; plannen 10 t/m 12 en de vorige review (doc 13).

## Door meten aan doc 13: wat is opgelost, wat niet

**Opgelost of structureel verwerkt:**

- [x] Tooltip-skelet uniform en on-brand (Bjorns punten van 11 nov): alle acht tooltip-pagina's dragen dezelfde huid - oranje band met het hanger-watermerk, kicker in Night, titel als stelling in de kaart, inhoud in één of twee kaarten. Het patroon "één tooltip = verdict + visual + comparator" is overal terug te zien.
- [x] Uniforme tooltip-ervaring: de standaard Power BI-tooltip staat uit op visuals zonder ontworpen tooltip (plan 12, ronde 9); geen enkele native tooltip in de set zichtbaar. De jaar-tooltip (17) vult het laatste gat.
- [x] M5 uit doc 13 (pakket-tooltip verliest zijn kop op A): in `16_tt-package.png` staan kicker ("PACKAGE A · EXPECTED CASE"), titel en NPV gewoon in beeld. Live placement onder Publish-to-Web blijft een poortpunt (M4 hieronder).
- [x] Tooltip-clutter: het pakket is afgeslankt tot twee kaarten (cijfers + bereikbalk; zettenlijst met totaal) en leest rustig.

**Nog open (in FinalV1 geverifieerd aanwezig):**

- [ ] Hanger versus masthead en chips (doc 13 M1) → M2 hieronder, nu met een besliste oplossing.
- [ ] Notatiemix (doc 13 M3) → M3 hieronder.
- [ ] Publish-to-Web-poort (doc 13 M4) → M4 hieronder.
- [ ] Your-plan-tegel kapt het bereikcijfer af (doc 13 S2) → S2.
- [ ] Route naar main (doc 13 S5) → M5, opgewaardeerd omdat de inzending nadert.
- [ ] Room-nights-regel in tt-f4-hotel (doc 13 N2) → N6.

## MUST (voor de inzending)

- [ ] **M1. De bereikbalk in de pakket-tooltip verliest zijn labels op pakket A.**
  - *Wat:* in `16_tt-package.png` botsen de letters B en A en hun streepjes met elkaar én met het label "High +12.7": A (+3.28) en B (+2.70) staan 0,6 apart op de as, dus de hele rechterkant van de schaal wordt één klont van twee letters, twee streepjes, de blauwe stip, de band en het High-label binnen ±40 px. Dit is de meest gehoverde stip (de aanbeveling) en het wow-moment van het rapport; precies daar moet de schaal feilloos lezen.
  - *Waar:* `TT Range SVG` in `sketch_model.py`: vaste labelposities boven de ticks, geen botsingsregels.
  - *Actie:* botsingsregels in de SVG-generator: (1) "Low x" links uitlijnen op de bandstart, "High x" rechts op het bandeind, nooit onder de A/B-streepjes; (2) minimale horizontale afstand tussen twee pakketletters 24 px - komen A en B dichterbij, dan A boven de band en B onder de band, elk met een eigen streepje; (3) C alleen tekenen als hij minstens 24 px van de break-even-tick af ligt. Daarna de tooltip op A én op C opnieuw renderen als bewijs.

- [ ] **M2. Hanger en masthead/chips claimen dezelfde hoek (Bjorns punt van 11 nov, onveranderd).**
  - *Wat:* op P1 loopt "2021 TO 2025 · FOR THE BOARD OF PILLOW & KEY GROUP" dwars door het gat van de hanger (2x-uitsnede bevestigt: het gat zit op exact de masthead-hoogte, y ~44). Op P2 verdwijnt de hanger vrijwel volledig achter de F1-F4-chips; alleen een rand piept erboven uit. De hanger is het enige merktheater op de pagina (D2b, Bjorns eigen keuze).
  - *Besliste oplossing:* (a) hanger ±50 px naar beneden in `brand_canvas_v3.py`, zodat het gat onder de masthead-regel en boven de horizon valt; (b) de vier F-chips verhuizen van de banner naar de footerrij van P2, rechts uitgelijnd naast de bronregel, in dezelfde pil-stijl met dezelfde hover-tooltips - ze zijn een referentie bij het lezen, geen kop, en de footerrij heeft de ruimte; (c) één gedeelde scene opnieuw genereren en P1 en P2 renderen. Verworpen alternatieven: hanger weg op P2 (strijdig met D2b, Bjorns expliciete keuze) en hanger naar links schuiven (botst daar met de headline).

- [ ] **M3. Notatie: nu beslissen, met een default (doc 13 M3, onveranderd).**
  - *Wat:* native labels volgen de viewer-locale (F3 "+6,8" / "−4,9", F4 "91,9%", waterval "+$3,4M" en "Totaal", KPI-kaarten in tt-f3-band en tt-f4-hotel "79,2% / $84,99"), terwijl alle tekst-measures en SVG's op en-US staan ("79.4%", "$107"). De mix staat binnen één tooltip (tt-f4-hotel) en binnen één paneel (de aanbevelingstegel naast de waterval op P2).
  - *Kern:* onder een en-US-browser verdwijnt de mix vanzelf - dan toont alles punten. De jury is Engelstalig; het risico zit alleen bij niet-Engelse viewers.
  - *Actie (default = accepteren):* in de P2W-poort (M4) met een en-US-browser vastleggen dat de mix weg is, plus één nl-NL-screenshot als bekende beperking in de inzendnotities. Alleen als Bjorn ook Nederlandstalige viewers verwacht: de F3/F4-barlabels, waterval-labels en de KPI-kaarten in de detail-tooltips converteren naar tekst/SVG op en-US (duurder).

- [ ] **M4. Publish-to-Web-poort draaien (open sinds ronde 4; nu ook voor de geschaalde tooltips).**
  - *Checklist:* het Deneb-selectorvisual (certified, maar onbewezen onder P2W); `useScaledTooltips` live op 1366 en 1920 (de tooltip-pagina's zijn nu 480 px en schalen mee - alleen Desktop heeft dat gezien); de hanger/achtergrond met schaal Fit op meerdere zooms; notatie (M3); Segoe UI op een machine zonder Segoe (Mac); de pakket-tooltip met de muis op stip A hoog in de wolk (placement); een toetsenbordronde. Doel: uiterlijk 17 november.

- [ ] **M5. Route naar main.**
  - *Wat:* FinalV1 staat alleen op `feedback-ronde-4`; `main` toont de staat van 11 november en vier PR's staan open die allemaal zijn ingehaald (#2, #5, #8, #11).
  - *Actie:* #2, #5, #8 en #11 sluiten als vervallen; één PR van `feedback-ronde-4` naar main; mergen voor de inzending, zodat main (en de jurylink) de waarheid toont.

## SHOULD

- [ ] **S1. F2 op P1: vier lijnen, drie labels.** Maison d'Or valt weg door een botsing met P&K Select aan het lijneinde; de kruisende grijze lijn (±33% in 2021 naar ±25% in 2025) is naamloos (2x-uitsnede van `01`). *Actie:* zoals in de tooltip (tt-f2): een legenda bovenaan in plaats van eindlabels. Uniform met de tooltips en botsingsvrij.
- [ ] **S2. Build-your-own, lege stand.** "+0.0 to +0.0" met een afgekapt label ("NPV, Low to High, …") en een zwevende "$0.0M / Totaal"-restwaterval midden in de tegel (render `04`). *Actie:* label verkorten ("NPV range, $M") en het slot verbreden; een statische ondertitel in de watervaltegel ("Pick moves on the left; your plan appears here") zodat de $0-balk een wachtplek krijgt in plaats van een fout te lijken.
- [ ] **S3. De kleurtaal breekt in de detail-tooltips.** In `14_tt-f3-band` en `15_tt-f4-hotel` is "This band"/"This hotel" Night en is Goodnight Inn GRIJS, terwijl GN overal in het rapport Coffee Blue is (kit D6: één kleur, één betekenis). *Actie:* de GN-vergelijkingslijn Coffee Blue maken; het gehoverde item blijft Night (de focus). Legenda-stippen volgen.
- [ ] **S4. Tegenstrijdige boodschap op één scherm.** De vergelijker-titel zegt "B ends level with A by 2032" terwijl de B-tegel er direct boven zegt "an NPV $0.6M lower, so A is simply the better deal" (render `03`). *Actie:* titel wordt "B ends within $1M of A by 2032; C never breaks even" (het bedrag uit het model).
- [ ] **S5. F1-titel zonder beginjaar leest als kersenplukken.** "After commissions, the margin fell from 36.5% to 33.7%" terwijl de grafiek in 2021 op ±33% begint: over het hele venster is de marge vrijwel vlak; de val is een 2023-2025-verhaal (de KPI-regel zegt het wél: "−2.8 pt since 2023"). *Actie:* "After commissions, the margin fell 2.8 points since 2023" of "since 2023" aan de titel toevoegen.
- [ ] **S6. Generator-pariteit met Bjorns Desktop-save.** Commit `1361f71` is een handmatige Desktop-hersave (schema 2.14, herschreven sleutelvolgorde, een nieuwe `cultures/`-map). De generators schrijven die staat niet; een rebuild vanuit `opzet_report.py` kan Bjorns handmatige laag- en kopposities overschrijven (de eigen regel: fixes gaan in de generator, nooit met de hand). *Actie:* de generator-uitvoer diffen met de Desktop-save en de deltas overnemen, zoals ronde 9 deed voor de kopposities - of expliciet vastleggen dat de huidige PBIR tot na de inzending de bron is en de generator daarna wordt bijgewerkt.

## NICE

- [ ] **N1. Selector-capex in gemengde precisie** ("$5.0M" naast "$4.25M" en "$24.75M", render `04`): één formaat, bijvoorbeeld één decimaal ("$4.3M", "$24.8M").
- [ ] **N2. Merk-comparator op andere precisie dan de KPI erboven** ("$84,99" versus "$85"; "79,2%" versus "79.4%" in `14`/`15`): de merkregel op dezelfde decimalen, of "(rounded)" erbij.
- [ ] **N3. tt-year-titel "where every package stands"** toont alleen A, B, C en je eigen plan: "where the four options stand".
- [ ] **N4. De nullijn onder F3 is een zware balk.** Bjorns eerdere voorkeur (7 nov): dunner en in een contrasttint - 2 px Dusk.
- [ ] **N5. Lege onderkant van tooltip-kaarten** (tt-f1/f2/f3, en kaart 2 van het pakket bij drie zetten): de inhoud verticaal centreren in de kaart, of bewust laten - een vaste lay-out kan niet meegroeien met acht zetten (bekende beperking).
- [ ] **N6. Room-nights-regel in tt-f4-hotel** ("leisure 39% · business travel 24% · family 22% · other 15%") beantwoordt geen beslisvraag (doc 13 N2; Bjorns clutter-punt van 11 nov): weg, of één gedempte bijzin.

## Inhoudelijke steekproef (intern consistent, geen actie)

Twaalf getallen nagetrokken over de renders heen: pakket A klopt overal (capex 5.00 + 2.40 + 2.00 = 9.40; NPV 3.37 + 0.51 − 0.60 = 3.28; selector, aanbevelingstegel, waterval en tooltip spreken elkaar niet tegen); B (9.40 − 2.00 + 4.25 = 11.65 capex; +2.7 NPV); C (36.9; −23.4; −34.8 tot −11.4); headline P2 (9.4 + 50.6 = 60.0); F4 (vijf van de zeven balken blauw; 82.0 / 79.1 / 77.5); de F2-foliotabel (109.31 − 19.68 = 89.63; 111.56 − 4.46 = 107.10); tt-year (−6.7 / −0.2 / +6.8 naar eind 2030; A/B/C op −0.2 / −1.1 / −30.1 - zie ook S4); "cash positive from 2031" is gelijk in tegel, tooltip en grafiektitel. De undiscounted-cumulatief-cijfers en de discounted-NPV-cijfers zijn netjes uit elkaar gelabeld ("$M, UNDISCOUNTED" in de kicker van tt-year). FEIT en INSCHATTING blijven schoon gescheiden ("Our reading:", "An association, not proof of cause", "Read with care:").

## Niet te beoordelen vanaf hier

- Live hover-placement en -grootte onder Publish-to-Web, de Deneb-selector in de service, toetsenbord en schermlezer, Mac-fonts: allemaal M4.
- De over-budget-stand en een gevulde bouw-waterval staan niet in deze set; S2/S3 uit doc 13 (regelzin en afgekapte categorienamen) zijn daardoor onverifieerd. Meenemen in de render-set van FinalV2.

## Wat al sterk staat

De uniforme tooltip-huid met de oranje band en het hanger-watermerk - het merk aanwezig zonder opschmuk; het patroon "één kaart is één verdict, één visual, één comparator"; de drie standen op P2 met de tabbalk en de vergelijkers (A altijd blauw); de leesgids boven de scatter; het budgetalarm als tegeltitel; en de koppen die stellingen zijn in plaats van onderwerpen. Met M1, M2 en M4-M5 eruit is dit een finale-waardige inzending.
