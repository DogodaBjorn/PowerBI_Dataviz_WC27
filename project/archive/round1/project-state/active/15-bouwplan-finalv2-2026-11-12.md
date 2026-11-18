# 15 - Bouwplan FinalV2, 12 november 2026

**Datum:** 2026-11-12 · **Op verzoek van:** Bjorn ("expliciete instructies voor elke fix, dus dat het een bouwplan wordt"; "ik wil eigenlijk alles doorgevoerd"; "als laatste meegeven dat hij van V2 ook weer alle nodige screenshots maakt, en ook expliciet de nodige") · **Bron:** review doc 14 (`14-review-finalv2-2026-11-12.md`), plannen 10-12, doc 13 · **Reikwijdte:** ALLE punten uit doc 14: MUST M1-M5, SHOULD S1-S6, NICE N1-N6. Waar de review een keuze openliet, staat hier de besliste keuze met één regel onderbouwing (paragraaf 8). Geen open vragen in dit plan.

**Context:** Power BI Dataviz World Champs 2027, ronde 1, Goodnight Inn ("The Wake-up Call"). Inzenddeadline **18 november 2026**, inzending gepland **17 november**. Werkbranch: `feedback-ronde-4` (commit na Bjorns blik, zoals steeds). Documentatie zoals deze gaat rechtstreeks op `main`.

---

## 0. Huisregels voor dit plan

1. **Fixes gaan in de generator, nooit met de hand** (de eigen regel uit de bouwhistorie). Daarom is fase 0 (generator-pariteit, S6) de eerste stap: elke latere rebuild hangt ervan af.
2. **Poorten na elke fase:** `sketch_model.py` opnieuw draaien bij modelwijzigingen (`validate_tmdl` 0 fouten), `opzet_report.py` bij rapportwijzigingen (`schema_check` 0 fouten, `a11y_check` 0 fouten / 0 notities).
3. **Verifieer visueel, in de pixels.** Elke stap noemt de render uit de ScreenshotsFinalV2-set (paragraaf 7) die het bewijs levert. Geen stap is klaar op "de generator draait".
4. **De PBIR-bron van waarheid is nu commit `1361f71`** (Bjorns Desktop-save van 12 nov). Fase 0 maakt de generators daarmee gelijk; daarna is de generator weer de bron.
5. Bestandsverwijzingen: model = `project/tools/sketch_model.py`, rapport = `project/tools/opzet_report.py`, lay-out = `project/design-prototypes/opzet-layout.json`, achtergronden = `project/tools/brand_canvas_v3.py` → `project/deliverables/backgrounds/`, geregistreerde resources = `project/pbip/GoodnightInn-opzet.Report/StaticResources/RegisteredResources/`.

---

## Fase 0 - S6: generator-pariteit met Bjorns Desktop-save (voorwaarde voor alles)

**Waarom eerst:** commit `1361f71` is een handmatige Desktop-hersave (schema 2.14, herschreven sleutelvolgorde, een nieuwe `cultures/`-map, handmatige laag- en kopposities). De generators schrijven die staat niet; een rebuild vanuit `opzet_report.py` zou Bjorns handmatige posities overschrijven. Fase 1 en 2 vereisen een rebuild, dus eerst pariteit.

**Stappen:**
1. Draai in een schone checkout van `feedback-ronde-4` `python project/tools/sketch_model.py` en `python project/tools/opzet_report.py` in een tijdelijke uitvoermap.
2. Diff de gegenereerde PBIR-boom tegen de bestanden op commit `1361f71`.
3. Splits de deltas in twee bakken:
   - **Desktop-artefacten (NIET overnemen):** schemaversie 2.14, sleutelvolgorde-herschrijvingen, de `cultures/`-map. Documenteer ze als bekende afwijking, zoals ronde 9 deed.
   - **Bjorns echte wijzigingen (WEL overnemen):** handmatige laag- en kopposities. Neem ze over in `opzet_report.py` / `opzet-layout.json`, zoals ronde 9 de kopposities overnam (logo y 12, eyebrow/masthead y 20, headline y 60, ondertitel y 108, chips y 48; 4 px-raster toegestaan in `pbir_lib.visual`).
4. Draai de generators opnieuw en diff nogmaals: de uitkomst moet op de overgenomen posities **identiek** zijn aan `1361f71`.
5. Leg de uitkomst vast in één alinea in de buildlog van deze ronde (welke deltas overgenomen, welke verworpen).

**Check:** rebuild = `1361f71` op alle overgenomen posities; `schema_check` en `a11y_check` 0 fouten.

---

## Fase 1 - M2: hanger en chips (Bjorns eigen punt)

### 1a. De hanger 50 px omlaag — het hele achtergrondbeeld opnieuw genereren

**KRITIEKE INSTRUCTIE (Bjorn, 12 nov):** de masthead/hanger is een **background-jpg**. De fix is: het **hele achtergrondbeeld opnieuw genereren** met de hanger op de nieuwe plek. **Verboden:** een nieuwe hanger-afbeelding als image-visual bovenop het rapport leggen (de overlay-variant — die heeft hij eerder gedaan en is in ronde 9/10 bewust overal verwijderd; `SCENE_VISUAL = False` en `z_canvas` komen NIET terug, op geen enkele pagina).

**Wijziging:**
1. `project/tools/brand_canvas_v3.py`, functie `night()`: `canvas.paste(m, (1350, -150 + extra_top))` → `canvas.paste(m, (1350, -100 + extra_top))`. Effect: het hangergat verschuift van y ~44 naar y ~94 - **onder** de masthead-regel (y 20-44) en ruim **boven** de horizon (y 232). X blijft 1350; schaal (7.2), kanteling (10°) en dekking (6%) ongewijzigd.
2. Regenereer alle achtergronden:
   `python project/tools/brand_canvas_v3.py project/deliverables/backgrounds project/design-prototypes/opzet-layout.json`
   (schrijft `canvas-night.jpg` plus de acht `canvas-tt-*.jpg`; de tooltip-scenes zijn inhoudelijk ongewijzigd - de rng is geseed, dus die blijven gelijk.)
3. Vervang het geregistreerde resource: kopieer `project/deliverables/backgrounds/canvas-night.jpg` over `project/pbip/GoodnightInn-opzet.Report/StaticResources/RegisteredResources/canvas-night.jpg`. Verder niets: de pagina's verwijzen al naar dat resource als achtergrond (Fit).
4. `a11y_check.py` draaien (de zone-samples toetsen tekstcontrast op de pixels van de scene).

**Check:** render `01`: de masthead ("2021 TO 2025 · FOR THE BOARD OF PILLOW & KEY GROUP") loopt **niet** meer door het hangergat; de hanger wordt nog steeds door de horizon geknipt; er is **geen** extra image-visual op de pagina (controleer de selectiepane-lijst: geen `z_canvas`, geen nieuwe afbeelding). Render `02`: hanger vrij zichtbaar in de banner (de chips zijn weg, zie 1b).

### 1b. De vier F-chips van de banner naar de footerrij van P2

**Waarom:** op P2 verdween de hanger vrijwel helemaal achter de F1-F4-chips. De chips zijn een referentie bij het lezen, geen kop; de footerrij heeft de ruimte.

**Wijziging** (`project/design-prototypes/opzet-layout.json`, pagina `p2-investment-strategy`):
1. `chip_f1` … `chip_f4`: van `y 48, h 56` (banner) naar **`y 1032, h 48`**, x-posities **`1216 / 1384 / 1552 / 1720`** (w 160, goot 8): rechts uitgelijnd naast de bronregel, de laatste chip eindigt op x 1880, binnen de paginamarge van 32.
2. `z_footer2`: `w 1856` → **`w 1152`** (x 32 blijft), zodat de bronregel nooit onder de chips loopt.
3. Tabvolgorde: chips van tab 102-108 naar de staart naast de footer: **`9010 / 9020 / 9030 / 9040`**.
4. `opzet_report.py` hoeft niet te wijzigen: `finding_chips()` leest posities uit de layout. De pil blijft identiek (border radius 12 in ZONE_MUTED, code in ZONE_EYEBROW, naam in ZONE_TEXT, gecentreerd). **Besliste terugval:** kapt de naam op h 48, dan code en naam op één regel ("F1 · The margin") in BODY maat S - geen open punt, eerst proberen in de huidige vorm.
5. De hover-tooltips (`tt-f1` … `tt-f4`) blijven aan dezelfde vier card-visuals gekoppeld; aan de binding niets wijzigen.
6. Regenereer P2 met `opzet_report.py` (na fase 0).

**Check:** render `02`: chips in de footerrij, zelfde pil-stijl, bronregel ongekort; hover op elke chip opent nog steeds de juiste tooltip; de banner draagt nu alleen eyebrow/masthead en de vrije hanger.

---

## Fase 2 - M1: botsingsregels in de bereikbalk van de pakket-tooltip

**Waarom:** dit is dé wow-tooltip op de meest gehoverde stip (pakket A, de aanbeveling). Op A botsen de letters B en A, hun streepjes en het label "High +12.7" (A +3.28 en B +2.70 staan 0,6 apart op de as).

**Wijziging** (`project/tools/sketch_model.py`, measure `TT Range SVG`, ~regel 1609). De huidige botsinglogica is onvoldoende: `VAR xAOff = IF ( ABS ( xA - xB ) < 18, ...)` verschuift letters slechts ±6 px, en de clamps `xLo = MAX ( xL, 44 )` / `xHi = MIN ( xH + 4, TTW - 88 )` kijken niet naar de streepjes. Bouw drie regels:

1. **Low/High-labels op de banduiteinden, nooit onder de A/B-streepjes:** het Low-label eindigt minstens 24 px links van het dichtstbijzijnde streepje; het High-label begint minstens 24 px rechts van het dichtstbijzijnde streepje. Verscherp de clamps daartoe (reken met xA/xB/xC/x0).
2. **Minimaal 24 px tussen pakketletters:** komen A en B dichterbij dan 24 px, dan A **boven** de band (huidige positie, y 13) en B **onder** de band, elk met een eigen streepje (nieuwe variant van `_tick` met het streepje omlaag verlengd en de letter eronder). De ±6-verschuiving (`xAOff`/`xBOff`) vervalt.
3. **C alleen tekenen** als xC minstens 24 px van de break-even-tick (x0) én van A en B ligt.
4. Mag de SVG hoger (48 → 56) om B onder de band kwijt te kunnen: pas dan ook kaart 1 van `tt-package` in de layout aan, op het 8 px-raster.

**Check:** render `16` (tooltip op **A**: A, B, beide streepjes, de blauwe stip én "High +12.7" allemaal vrij van elkaar) én render `17` (tooltip op **C**: dezelfde eis). Geen enkele botsing toegestaan; zo nodig regels bijschroeven en opnieuw renderen tot het klopt.

---

## Fase 3 - SHOULD en NICE (model + rapport)

### S1 - F2 op P1: legenda bovenaan in plaats van eindlabels
- **Wijziging** (`opzet_report.py`, `f2_chart`, ~regel 315): de niet-small variant krijgt dezelfde oplossing als de tooltip-variant: `"legend": legend(True, BODY, S, INK2, "Top")` en `"seriesLabels": show b(False)` (eindlabels uit). De vier series blijven (Goodnight Inn + drie zusters; P1 is breed genoeg). **Besliste terugval:** kapt een merknaam in de legenda, dan de zusters samenvoegen tot één lijn "The other three brands" (`Trend OTA Sisters`), zoals in de tooltip.
- **Check:** render `01`: vier lijnen, vier leesbare namen in de legenda; Maison d'Or valt niet meer weg; geen naamloze grijze lijn.

### S2 - Build-your-own: lege stand opruimen
- **Label:** `opzet_report.py` regels ~792, ~809 en ~825: het derde label `"NPV, Low to High, $M"` → **`"NPV range, $M"`** in alle drie de nums_cards (rec, B/C en your-plan), zodat de staten gelijk blijven. Het slot `c_you_nums` (w 464) is met het korte label breed genoeg; controleer op afkapping.
- **Ondertitel in de watervaltegel:** geef `ch_build_waterfall` een statische titel via het bestaande `title_measure`-argument van `waterfall()` (regel ~827): nieuwe tekstmeasure `Build WF Note (text)` = **"Pick moves on the left; your plan appears here."**, gedempte stijl. Zo leest de $0-restwaterval als wachtplek, niet als fout.
- **Check:** render `04` (leeg: kort label volledig zichtbaar, ondertitel aanwezig) en render `05` (gevuld).

### S3 - Kleurtaal in de detail-tooltips: GN wordt Coffee Blue
- **Wijziging** (`opzet_report.py`, `line_pair`, ~regel 415): in `series_colors({mref(own): INK, mref(brand): SLATE})` wordt de brand-kleur **`ACCENT_MARK` (Coffee Blue #2589D8)** - dezelfde kleur als de GN-lijn in F2 en de A-lijn in de vergelijkers (kit D6: één kleur, één betekenis). Het gehoverde item blijft `INK` (Night, de focus). De legenda-stippen volgen automatisch. Raakt `tt-f3-band` en `tt-f4-hotel`.
- **Check:** renders `14` en `15`: GN-lijn Coffee Blue, gehoverde band/hotel Night.

### S4 - Vergelijker-titel in overeenstemming met de B-tegel
- **Wijziging** (`sketch_model.py`, `Cmp Alts Title (text)`, ~regel 1507): de tak `ROUND ( ( a32 - b32 ) / 100000, 0 ) = 0` levert nu "ends level with A by 2032" → wordt **"ends within $1M of A by 2032"**. De C-tak ("never breaks even" / "breaks even in …") blijft.
- **Check:** render `03`: titel ("B ends within $1M of A by 2032; C never breaks even") strookt met de B-tegel ("an NPV $0.6M lower").

### S5 - F1-titel met beginjaar
- **Wijziging** (`sketch_model.py`, `F1 Title (text)`, ~regel 1095): de RETURN wordt
  `"After commissions, the margin " & IF ( z < a, "fell", "rose" ) & " " & FORMAT ( ABS ( z - a ) * 100, "0.0" ) & " points since 2023"`
  → "After commissions, the margin fell 2.8 points since 2023" (dezelfde vorm als de KPI-regel "−2.8 pt since 2023"; de val is een 2023-2025-verhaal, de grafiek begint in 2021 op ~33%).
- **Check:** render `01`.

### N1 - Selector-capex in één precisie
- **Wijziging** (`sketch_model.py`, `Move Capex (text)`, ~regel 1565): `fmc(...)` vervangen door een vaste één-decimaal-formatter: `FORMAT ( ( ... ) / 1000000, "$#,0.0" ) & "M"` ("$5.0M" blijft "$5.0M", "$4.25M" → "$4.3M", "$24.75M" → "$24.8M"). **Alleen deze measure:** `fmc` zelf blijft bestaan voor de plekken waar getoonde delen moeten optellen tot getoonde totalen (tooltip-zettenlijst). De Deneb-voetregel sommeert op `CapexNum` en is al één decimaal.
- **Check:** renders `05` en `06`: alle capex-bedragen in de selector met precies één decimaal.

### N2 - Merk-comparator op dezelfde precisie als de KPI erboven
- **Wijziging** (`sketch_model.py`, `Band vs Brand (text)` ~regel 1675 en `Hotel vs Brand (text)` ~regel 1696): de FORMAT-strings voor RevPAR en ADR van `"$#,0"` → **`"$#,0.00"`** (→ "$84.99", gelijk aan de KPI erboven). De percentages blijven `"0.0%"`.
- **Check:** renders `14` en `15`: merkregel en KPI's op identieke decimalen.

### N3 - tt-year-titel
- **Wijziging** (`sketch_model.py`, `TT Year Title (text)`, ~regel 1493): "where every package stands" → **"where the four options stand"** (de kaart toont A, B, C en je eigen plan).
- **Check:** render `18`.

### N4 - Nullijn onder F3 dunner
- **Wijziging** (`opzet_report.py`, `f3_chart`, ~regel 352): `y1AxisReferenceLine` krijgt **`"width": num(2)`** (de scatter en de cumulatieve grafiek zetten `width` al, regels ~633/~714 - zelfde objectvorm). Kleur blijft Dusk (`INK2` #4B5466), zoals Bjorns voorkeur van 7 nov.
- **Check:** render `01` (en `12`): de nullijn is een dunne lijn, geen zware balk.

### N5 - Lege onderkant van tooltip-kaarten — beslist
- **tt-f1 / tt-f2 / tt-f3:** inhoud verticaal centreren. Meet per pagina de lege ruimte onder de laatste inhoud in de kaart (uit de render), en schuif `ttf_chart` en `ttf_note` in de layout elk met de helft daarvan omlaag (8 px-raster).
- **tt-package kaart 2 (zettenlijst): bewust ongemoeid laten.** De vaste lay-out is op het grootste pakket (8 zetten) berekend; centreren zou de lijst per pakket verticaal laten springen. Vastleggen als bekende beperking.
- **Check:** renders `10`-`12` (gecentreerd), render `16` (onveranderd, top-aligned).

### N6 - Room-nights-regel uit tt-f4-hotel — beslist: weg
- **Wijziging** (`opzet_report.py`, `detail_page_visuals` voor `TT_F4`): de slotregel `Segments 2025 (text)` (`foot`) van de pagina verwijderen. De measure mag ongebruikt blijven staan of mee weg; de vrijgekomen ruimte wordt ademruimte onderin de kaart (consistent met N5).
- **Reden:** de regel ("leisure 39% · business travel 24% · family 22% · other 15%") beantwoordt geen beslisvraag (doc 13 N2; Bjorns clutter-punt van 11 nov).
- **Check:** render `15`: de regel is weg, de kaart blijft in balans.

---

## Fase 4 - M3: notatie — beslist: accepteren en vastleggen in de publish-gate

**Beslissing: geen conversie.** Alle eigen tekst-measures en SVG's staan op en-US; native labels volgen de viewer-locale. Onder een en-US-browser - de jury - is alles consistent en verdwijnt de mix vanzelf. Alleen niet-Engelse viewers zien de mix. Dit wordt dus een verificatiepunt van fase 5 plus één nl-NL-screenshot (render `26`) als bekende beperking in de inzendnotities. Alleen als Bjorn alsnog Nederlandstalige viewers verwacht wordt dit een conversieklus (F3/F4-barlabels, waterval-labels en de KPI-kaarten in de detail-tooltips naar tekst/SVG op en-US); nu niet.

---

## Fase 5 - M4: de Publish-to-Web-poort — uiterlijk 17 november

Alles tot nu toe is in Desktop getest; de jury kijkt in de browser. Bjorn publiceert; de bouwer verifieert en legt vast. Elke stap heeft een pass-criterium en een bewijsrender (paragraaf 7).

1. **Publiceren:** naar de service, Publish-to-Web aanzetten, de jurylink noteren.
2. **Deneb-selector in de service:** een gewone klik zet een zet aan/uit; getallen, waterval, vergelijker en de Tangerine stip volgen. (Bewijs: `22`.) Faalt dit, dan de vastgelegde terugval: `--selector=native` (plan 12, besluitentabel).
3. **Geschaalde tooltips (`useScaledTooltips`):** op 1366 én 1920 hoveren; de tooltips schalen mee met het canvas en zijn niet buitenproportioneel. Specifiek de pakket-tooltip met de muis op stip A hoog in de wolk: placement klopt, kop in beeld. (Bewijs: `21`, `23`, `27`.)
4. **Achtergrond op Fit, meerdere zooms:** geen dubbele scene, hanger op zijn plek, banner sluit aan. (Bewijs: `24`, `25`.)
5. **Notatie (M3):** en-US-browser: overal punten, geen komma/punt-mix. Daarna één nl-NL-sessie: mix vastleggen in `26` voor de inzendnotities.
6. **Fonts op een machine zonder Segoe UI (Mac):** de webfont-stack (`wf_segoe-ui_*`) doet zijn werk; geen font-uitval, geen verschoven regels. (Bewijs: `28`.)
7. **Toetsenbordronde:** de tabbalk is bereikbaar en benoemd; vastleggen dat de Deneb-selector met het toetsenbord niet te bedienen is (bekende beperking, zoals in de buildlog en in de inzendnotities).
8. **Uitkomst:** alle punten groen = de poort is geslaagd. Bevindingen en de twee bekende beperkingen (nl-NL-notatie, Deneb-toetsenbord) gaan in de inzendnotities.

---

## Fase 6 - M5: route naar main (na Bjorns ja op FinalV2, voor de inzending)

1. **Sluit PR's #2, #5, #8 en #11** (open geverifieerd op 12 nov; allemaal ingehaald door `feedback-ronde-4`) met de comment: "Vervallen: ingehaald door feedback-ronde-4 (FinalV2)."
2. **Eén PR van `feedback-ronde-4` naar `main`; mergen.**
3. **Controleer:** `main` toont FinalV2 - het PBIP, `ScreenshotsFinalV2/` en docs 13-15. De jurylink uit fase 5 wijst naar de gepubliceerde versie van deze staat.

---

## 7. Screenshots van FinalV2 (laatste stap, ná alle fixes)

**Map:** `project/deliverables/screenshots/ScreenshotsFinalV2/` op `feedback-ronde-4`.
**Werkwijze:** identiek aan de V1-set - renders via de Desktop Bridge op scale 2, bijgesneden tot de pagina; contextuele tooltips (14-17) en bookmark-staten (03-06) uit een wegwerpkopie van het project met een tijdelijk paginafilter of de bookmark-zichtbaarheid toegepast; het gecommitte project krijgt die filters niet.
**README:** een `README.md` in de map volgens exact het patroon van de V1-README (tabel: bestand → wat het toont; notitie over de wegwerpkopie en `useScaledTooltips`).

**Desktop-set (verplicht, allemaal):**

| Bestand | Toont | Bewijst |
|---|---|---|
| `01_p1-brand-review.png` | Pagina 1 zoals hij opent | M2 (masthead vrij van de hanger), S1 (F2-legenda), S5 (F1-titel), N4 (nullijn) |
| `02_p2-investment-strategy_recommended-A.png` | Pagina 2, bookmark "Recommended: A", scenario Expected, alle pakketten | M2 (chips in de footer), S2 (kort label op de rec-tegel) |
| `03_p2-investment-strategy_considered-B-C.png` | Pagina 2, bookmark "Considered: B and C" | S4 (vergelijker-titel) |
| `04_p2-investment-strategy_build-your-own-empty.png` | Pagina 2, bookmark "Build your own", niets gekozen | S2 (label, ondertitel, lege stand leest als wachtplek) |
| `05_p2-investment-strategy_build-your-own-filled.png` | Dezelfde stand met **minstens 3 geldige zetten** (nieuw in V2) | Gevulde bouw-waterval, N1 (selector-capex één decimaal), regelcheck |
| `06_p2-investment-strategy_build-your-own-over-budget.png` | Dezelfde stand **boven het budget** (nieuw in V2) | Het budgetalarm (Tangerine band + selector-voetregel) |
| `10_tt-f1.png` … `13_tt-f4.png` | De vier bevindingstooltips | N5 (centrering), ongewijzigde huid |
| `14_tt-f3-band.png` | Band-tooltip, gerenderd voor "10 years or more" | S3 (GN Coffee Blue), N2 (precisie) |
| `15_tt-f4-hotel.png` | Hotel-tooltip, gerenderd voor Toronto Pearson Airport | S3, N2, N6 (room-nights weg) |
| `16_tt-package-A.png` | Pakket-tooltip op **pakket A**, Expected | **M1**: bereikbalk zonder botsingen |
| `17_tt-package-C.png` | Pakket-tooltip op **pakket C**, Expected | **M1**: idem op C |
| `18_tt-year.png` | Jaar-tooltip, gerenderd voor 2030 | N3 (titel) |

**Publish-to-Web-set (verplicht, direct na fase 5, in dezelfde map):**

| Bestand | Toont |
|---|---|
| `20_p2w-p1-1366.png` | P1 onder Publish-to-Web op een 1366-venster (en-US) |
| `21_p2w-p2-rec-1366.png` | P2 rec-stand onder P2W op 1366, met één gehoverde tooltip (schaalcheck) |
| `22_p2w-p2-build-deneb-1366.png` | De Deneb-selector in de service ná een klik: getallen/waterval/vergelijker gevolgd |
| `23_p2w-tt-package-hover-A.png` | De pakket-tooltip met de muis op stip A hoog in de wolk: placement en kop in beeld |
| `24_p2w-zoom-45pct.png` | P2 op 45% zoom: geen dubbele scene, hanger op zijn plek |
| `25_p2w-zoom-100pct.png` | P2 op 100% zoom: idem |
| `26_p2w-notatie-nlNL.png` | Eén nl-NL-sessie: de komma/punt-mix als bekende beperking voor de inzendnotities |
| `27_p2w-p2-1920.png` | P2 onder P2W op een 1920-venster |
| `28_p2w-mac-fonts.png` | P1 en P2 op een machine zonder Segoe UI (Mac): geen font-uitval |

De toetsenbordronde (fase 5, stap 7) levert geen screenshot maar één alinea in de README van de set.

---

## 8. Besliste keuzes (waar doc 14 ze openliet)

| Punt | Beslissing | Eén regel waarom |
|---|---|---|
| M3 notatie | Accepteren; verifiëren in fase 5 + één nl-NL-shot als bekende beperking | Onder een en-US-browser (de jury) is alles consistent; conversie is duur en risicovol vlak voor de deadline |
| S1 terugval | Eerst 4-namen-legenda; kapt een naam, dan zusters samenvoegen zoals de tooltip | Uniform met de tooltips en botsingsvrij; de samenvoeging is de bewezen smalle variant |
| S6 pariteit | Deltas overnemen in de generators (geen "PBIR blijft tot na de inzending de bron") | De huisregel is fixes-in-de-generator, en fase 1-3 vereisen sowieso een rebuild |
| N5 lege kaartonderkanten | tt-f1/f2/f3 centreren; pakket-kaart 2 bewust top-aligned laten | Een vaste lay-out kan niet meegroeien met 8 zetten; centreren daar zou per pakket springen |
| N6 room-nights-regel | Weg | Beantwoordt geen beslisvraag (Bjorns clutter-punt) |
| N1 selector-precisie | Eén decimaal, alleen in `Move Capex (text)` | Eén formaat leest rustig; de optelregel van de tooltip (`fmc`/`fmc2`) blijft intact |
| Chip-terugval (M2) | Eerst tweeregelige pil op h 48; kapt het, dan éénregelig "F1 · The margin" | Zelfde pil, zelfde hover; de footerrij heeft 48 px |
