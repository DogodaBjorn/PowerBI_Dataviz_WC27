# 13 - Review en to-do, 11 november 2026

**Datum:** 2026-11-11 · **Op verzoek van:** Bjorn ("doe nog een keer review op je punten en de inhoud, en maak daar een to-do lijst van") · **Bekeken:** branch `feedback-ronde-4` (ec39cd1): de PBIR van `GoodnightInn-opzet.pbip`, de generators (`sketch_model.py`, `opzet_report.py`, `brand_canvas_v3.py`), alle renders van ronde 4-6 pixel voor pixel, kit 3.1 (`goodnight-inn-wakeup`) en plannen 08-12.

## Al opgelost (afgevinkt, geen actie meer)

- [x] Tooltip-tabs verborgen: alle 7 tooltip-pagina's hebben `type: Tooltip` en `HiddenInViewMode`; alleen P1 en P2 staan als tab.
- [x] Build staat in de repo (branch `feedback-ronde-4`; naar main is apart punt, zie SHOULD-5).
- [x] Tekst-measures en de SVG-maten in de tooltips lopen nu vast op en-US (model-culture en-US; de SVG-rangebalk expliciet met culture-argument).
- [x] Comparator naast de KPI's: contextregels onder de vier KPI's op P1, en in `tt-f4-hotel` de merkcijfers direct onder de hotelcijfers.
- [x] Airports-claim: "5 of the 7 fullest" noemt de n en claimt geen significantie.
- [x] Lettervloer 12 pt / 16 px, bewaakt door `a11y_check.py` (0 fouten), ook in de SVG-in-DAX-maten.
- [x] Tooltip-dichtheid: het vaste zettenraster ("filled = in this package") vervangt de losse chips; de pakket-tooltip is nu een bewijskaart (verdict, rangebalk, waterval per zet).
- [x] Footers: bronregel plus alleen de echte voorbehouden; de scopingzin is weg.

## MUST (voor publicatie)

- [ ] **M1. Logo rechtsboven en achtergrond herstellen (Bjorns punt).**
  - *Wat:* op P2 liggen de F1-F4-chips dwars over de vervaagde hanger in de nachtzone; alleen het gat en wat randen piepen eruit (render `2026-11-10-feedbackronde-6/20_P2_chips.png`). Op P1 loopt de regel "2021 TO 2025 · FOR THE BOARD..." door het gat van de hanger. De hanger was juist het enige merktheater (D2b, Bjorns eigen waarschuwing van 9 nov: "it feels like the faded door hanger on the right top has been lost").
  - *Waar:* de chips zitten op de plek van de hanger ("Bjorns plek", ronde 6). Beide claims op dezelfde hoek werken elkaar weg.
  - *Waarom:* zonder leesbare hanger verliest de pagina zijn merkherkenning rechtsboven; de chips lezen nu ook als bedekking in plaats van compositie.
  - *Actie:* kies een van: (a) chips naar links schuiven zodat de hanger vrij komt, (b) hanger verplaatsen/verkleinen zodat hij naast de chips leest, (c) chips verlaten de banner (bijv. onder de headline). Daarna P1 en P2 opnieuw renderen.
- [ ] **M2. De pagina-achtergrond van 11 nov is nooit geverifieerd gerenderd.**
  - *Wat:* de rapportpagina's dragen nu `canvas-night-page.jpg` (1920x1100) als achtergrondbeeld, met 20 px banner boven de scène. Na die wijziging zijn alleen tooltips opnieuw gerenderd; P1 en P2 niet.
  - *Waar:* `brand_canvas_v3.py` `night(extra_top=20)` en de `page.json`-achtergrond. De aanname dat Desktop de pagina 20 px onder de achtergrond plaatst (zodat beide hangers exact overlappen) staat als feit in de code, maar is nergens getest vastgelegd.
  - *Waarom:* als de host anders rendert (andere zoom, Publish-to-Web, Mac), verschuift de achtergrond-hanger ten opzichte van de scène in `z_canvas`: dubbele of gehakte hanger, horizon uit lijn. Dat is zichtbaar op het eerste scherm dat de jury ziet.
  - *Actie:* P1 en P2 renderen in Desktop op 1920 én 1366, en in Publish-to-Web (schone browser): strook bovenin, hanger en horizon op exact dezelfde plek als de kaarten verwachten, geen dubbeling.
- [ ] **M3. Getalnotatie: tekst is nu en-US, grafieklabels volgen nog de kijker.**
  - *Wat:* alle tekst-measures tonen punten (79.4%, $107, ook op een nl-NL-machine), maar kaart- en aslabels en datalabels van grafieken volgen de locale van de viewer: in de eigen nl-NL-renders "+6,8", "91,9%", "+$3,4M". Binnen een visual (F4: headline 82.0% met punt, barlabels 91,9% met komma) en binnen een tooltip (tt-f4-hotel: KPI's 91,9% / $102,78, merklijn 79.4% / $107) staat de mix er nog.
  - *Waar:* veldformaten van native visuals (geen culture-te dwingen) versus FORMAT-tekst (model-culture en-US).
  - *Waarom:* een jurylid met een niet-Engelse browser ziet de mix; het oogt slordig in precies de visuals met de hoofdclaim.
  - *Actie:* expliciet beslissen en vastleggen. Realistische opties: (a) accepteren - Engelse jury, Engelse browsers - en in de inzendnotities vermelden; (b) de meest zichtbare labels (F4-barlabels, KPI-tegels, watervallen) ook als tekst/SVG op en-US zetten. In beide gevallen: in de Publish-to-Web-poort met een nl-NL én een en-US browser controleren wat de jury echt ziet.
- [ ] **M4. Publish-to-Web-poort draaien (staat open sinds ronde 4).**
  - *Wat:* publiceren en in een schone browser testen: het Deneb-selectorvisual (certified, maar onbewezen onder P2W), de tooltips met een muis, zoom op 1366, Segoe UI op een machine zonder Segoe (Mac), notatie (M3), de nieuwe achtergrond (M2).
  - *Waarom:* "must render under Publish-to-Web" is een wedstrijdregel; alles hierboven is in Desktop getest, niet in de service.
- [ ] **M5. De pakket-tooltip op A verliest zijn kop.**
  - *Wat:* in render `2026-11-10-feedbackronde-6/13_tooltip_A.png` begint de kaart boven de bovenrand van het canvas: chip, naam en case-tag zijn niet zichtbaar; het begint direct bij "+$3.28M". Op C (render 11) staat de kop er wel.
  - *Waar:* `tt-package` (560x568) op een stip hoog in de scatter; Power BI plaatst de tooltip dan deels buiten beeld.
  - *Waarom:* A is de meest aangeklikte stip; de self-review claimt "fully on the canvas", de render toont het omgekeerde.
  - *Actie:* live verifiëren (ook onder M4); zo nodig de tooltip-pagina korter maken of de positie van A's hover-zone aanpassen.

## SHOULD

- [ ] **S1. Re-render-gat dichten.** Meerdere late fixes hebben geen verifiërende render in de eindtoestand: de regelzin in de bouw-tegel (shot `feedbackronde-5/08` toont nog "Not yet within the rules: within the budget." bij $16,65M over budget; de TMDL zegt inmiddels "over the budget" maar geen render bewijst het), de chip-tooltips F1, F2 en F4 in de nieuwe kaart-skin (alleen F3 is opnieuw gerenderd; in de oude skin kapte F1's noot af midden in een woord), en de W1366-set (dateert van ronde 4: oude footer, geen chips).
- [ ] **S2. Your-plan-tegel: bereikcijfer kapt af.** Shot `feedbackronde-5/08`: "-67.7 to -3..." en label "NPV, Low to High, ..." vallen weg bij brede ranges. Meer breedte of een korter format voor uitschieters.
- [ ] **S3. Waterval in de bouw-stand kapt categorienamen.** "Revenue manag...", "Energy progra...", "Boston new h...", "Refresh 10 old..." (shot 08). Kortere assennamen of schuine labels.
- [ ] **S4. Zwevend visual-header-chroom in de banner.** Bij hover op de chips en de tabbalk verschijnt een losse witte pil met pictogrammen boven de nachtbanner (renders 21, 23 en W1366a). Ziet eruit als een fout, ook al is "visual header zichtbaar" een bewuste keuze uit de kit (show as table, focus mode). Beslissen: header uit op niet-data-visuals, of zo laten en bewust verantwoorden.
- [ ] **S5. Route naar main.** PR #11 (`design-rebuild`) staat nog open terwijl die branch al in `feedback-ronde-4` is gemerged; voor `feedback-ronde-4` zelf is nog geen PR. Voor de inzending (17 nov) moet main de waarheid tonen. Beslissen: #11 sluiten en één PR van `feedback-ronde-4` naar main.

## NICE

- [ ] **N1. Dezelfde zet, ander bedrag.** Revenue management staat in de tooltip van A als +$0.51M en in die van C als +$0.50M (afronding per pakket, zodat de delen optellen). Rond eenmalig per zet af en laat het pakkettotaal de som van de afgeronde delen zijn; dan is elke zet overal gelijk.
- [ ] **N2. Room-nights-regel in tt-f4-hotel weg of kleiner.** "leisure 39% · business travel 24% · family 22% · other 15%" beantwoordt geen beslisvraag op deze pagina (eigen regel: minder tekst).
- [ ] **N3. Kit-doc bijwerken.** `brand.yaml` (3.1) noemt nog horizon = eerste kaartrij + 128 (y 312); de build gebruikt + 64 (y 248). Eén regel in de kit, voorkomt een verkeerde rebuild later.

## Inhoudelijke steekproef (geen actie nodig)

Ongeveer vijftien getallen op P1, P2 en in de tooltips nagerekend en getoetst aan plannen 09-12 en de kit-documenten: pakket A (9.40 = 5.00 + 2.40 + 2.00; +3.28 = 3.37 + 0.51 - 0.60), pakket C (36.90; -23.44), de F2-foliotabel (109.31 - 19.68 = 89.63; 111.56 - 4.46 = 107.10), F1 (-2.8 pt), F4 (82.0 / 79.1 / 77.5, 5 van 7), headline P2 (9.4 + 50.6 = 60.0), de over-budget-tegel (5.00 + 2.40 + 15.00 + 24.75 + 29.50 = 76.65, en 76.65 - 60.0 = 16.65). Alles intern consistent. FEIT en INSCHATTING zijn netjes gescheiden ("our reading is that...", "an association, not proof of cause", "Read with care: ...", "counterfactual" benoemd). De dataset zelf zit niet in de repo (gitignored), dus herleiding uit de bron is niet vanaf hier te controleren; de eigen gates (`validate_tmdl`, INFO.MEASURES) rapporteren 0 fouten.

## Niet te beoordelen vanaf hier

- De echte Publish-to-Web-weergave (Deneb, fonts, achtergrond, notatie per browser): daarvoor is M4 de poort.
- Of de hanger achter de chips in een live sessie anders leest dan op de renders: M1 vraagt een korte blik van Bjorn op de twee opties.
- Toetsenbordbediening van de Deneb-selector (bekende beperking, al vastgelegd in plan 12 par. 5).

## Wat al sterk staat

Verdict eerst in elke tooltip, de bewijskaart met vaste NPV-as en break-even, inline labels in plaats van legenda's, de leesgids boven de scatter, het budgetalarm in de tegeltitel, en een consequente kleurtaal (blauw = Goodnight Inn/het plan, oranje = signaal, grijs = context). De structuur van FEIT naast INSCHATTING is voorbeeldig.
