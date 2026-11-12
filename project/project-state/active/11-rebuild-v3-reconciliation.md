# 11 - Rebuild-pakket 09 + 10 op de v3-build: afstemming en besluiten

**Datum:** 2026-11-09 · **Gevraagd door:** Bjorn ("I have added two commits to the Dataviz WC 27 repository both consisting of rebuild instructions. One is data and content related one is design related. I want both implemented in the Goodnight Inn report. Then finally I want a double triple check on accessibility alt text etc.") · **Branch:** `rebuild-09-10` (afgetakt van `upgrade-opzet-v3`, met `origin/design-rebuild` erin gemerged; lokale commits, geen push zonder Bjorns ja).

## 1. Waarom dit document

Plan 09 (`09-research-based-rebuild.md`, inhoud) en plan 10 (`10-design-rebuild.md`, vorm) zijn geschreven tegen `main`. De echte build staat op `upgrade-opzet-v3` (tien commits verder, niet in `main`): review-v2-fixes (K1, vaste A/B/C), verbeterplan ronde 3 (V1-V5, 11 pt-vloer) en het meubilair als visuals. Daardoor bestaan meerdere doelen uit de plannen niet meer:

- `hero_brand_compare` en `c_compare_sub` zijn weg: P1 is nu de KPI-band (vier cellen) plus F1-F4. De KPI_ROWS-tabel en de `KPI Text *`/`Trend Title *`-measures staan niet meer op het canvas (BUILD_LOG).
- De koppen zijn measures (`Headline P1/P2 (text)`), geen statische deurhanger-zinnen; die staan nu in de pay-off (`PAYOFF`) naast het logo.
- Kaarten en logo zijn visuals (`card_frames()`, `brand_row()`), geen achtergrond-PNG: een pagina-achtergrond met Fit verschoof op 7 november toen Desktop het canvas niet-uniform schaalde (BUILD_LOG:112). Plan 10 D2 tekent zone en schaduw in die achtergrond-PNG.
- Regelnummers zijn verschoven (sketch_model.py +17 tot +460, opzet_report.py +10 tot +190).

Dit document legt per punt vast hoe de **bedoeling** van 09 en 10 op de v3-architectuur landt. De inhoud van 09 en 10 verandert niet; waar dit document afwijkt, gaat dit document voor.

## 2. Besluiten van Bjorn (9 november, in de sessie)

| Onderwerp | Besluit |
|---|---|
| 138 ongecommitte Desktop-bestanden op v3 (schema 2.11 naar 2.14, herordening, cultures-bestand) | Weggegooid: geen inhoudelijke wijziging, de generators schrijven alles opnieuw. |
| Night header | **D7 night-glow, met waiver**: verloop Night naar navy in de zone, Coffee Blue gloed, zwaardere schaduw onder de hoofdkaart, blauwe gloed onder de aanbeveling, plus de D2b-hanger. |
| Lettervloer | **12 pt / 16 px** (kit 3.1 `typography.floor`). Past het P2-paneel niet op 1366, dan gaat detail naar de tooltip, nooit kleinere letters. Vervangt de 11 pt van 08 R4. |
| R1 (prijskracht) | Eerst gepland als RevPAR-index in KPI-cel 4. **Na de haalbaarheidscheck (zie R1 hieronder) besloot Bjorn: één zin in de F1-noot, NPS blijft in cel 4** als kwaliteitssignaal. Geen vierde trendslot: P1 heeft geen ruimte. |
| Koppen (D5) | De v3-koppen (measures) blijven. D5 geldt alleen voor de resterende deurhanger-copy en kleurnamen. |
| Brand row | Vignettes (hanger met gezicht) en pay-off-regels eruit; in het pay-off-slot de eyebrow "01  THE BRAND REVIEW" / "02  THE INVESTMENT STRATEGY". |
| Git | Branch `rebuild-09-10`, lokale commits per stap, geen push. |

**WAIVER D7, 2026-11-09, Bjorn:** voor de header-zone vervalt design hard rule 6 voor gradients (verloop Night naar navy, Coffee Blue gloed); lock 9 (één kaartstijl per pagina) wordt gebogen voor de zwaardere schaduw onder de hoofdkaart en de gloed onder de aanbeveling. Reden: Bjorn koos de night-glow-variant ("more oompf", plan 10 paragraaf "Hoe we hier kwamen"). De D2b-waiver (de vervaagde hanger) blijft van kracht.

## 3. Afstemming per punt

### Deel A: plan 09

| Punt | Plan (tegen `main`) | Op v3 |
|---|---|---|
| R1 | Twee indexrijen in `KPI_ROWS` (hero-tabel), optioneel vierde trendslot | Haalbaarheidscheck `project/analysis/42_price_index.py` (uitkomst `output/price_index.txt`): RevPAR-index 2025 bij 2021 = 100 is GN 136 (3e van 4), zusters 130 tot 235; die spreiding is het COVID-herstel (P&K Select bezetting 38 % naar 72 %). Op basis 2023 bewegen de merken samen: ADR GN +2,7 %, zusters +1,6 % tot +4,7 %. Bjorn koos: **één zin in `F1 Note (text)`**, afgeleid uit het model (ADR-groei sinds 2023 tegen de zusters, met 'in lijn met / sneller / trager' bewaakt): "Room rates rose 2.7% since 2023, in line with the other brands (1.6% to 4.7%): no price premium to absorb the commissions." |
| R2 | Label "F3 · Recommend us?" en `Trend Title NPS` herformuleren | NPS blijft in KPI-cel 4 met het label **"Guest quality: net promoter score"** (kwaliteitssignaal, niet dé merk-KPI). F3 houdt NPS als operationeel signaal (renovatieleeftijd). Keller-ladder-commentaar en KpiLine-label bijgewerkt. Methodologiezin rijdt mee met R4. |
| R3 | Nieuwe `Plan Margin (text)` op een leeg slot | Geen vrij slot; `Rec Held`/`Not Funded` dragen het argument al. De marginale toets wordt een bijzin in **`Rec Held (text)`**: het beste pakket dat A plus minstens één initiatief bevat, de extra capex en het NPV-verschil in het gekozen scenario. Alleen als die NPV lager is dan A's; anders leeg (geen valse claim in High). |
| R4 | Zin in `FOOTER` | Zin in `FOOTER` (P1) en in `Footer P2 (text)`. Geen repo-pad op het canvas. |
| R5 | Zin in `c_compare_sub` | Zin in `F2 Note (text)`, gelabeld "Our reading:" (INSCHATTING), rang uit het model: "Our reading: the fullest brand of the four grows by reach and direct rebooking, not loyalty schemes." Ingekort zodat de noot op 12 pt in drie regels onder de folio past (render 9 nov). |

### Deel B: plan 10

| Punt | Op v3 |
|---|---|
| D1 | Zoals gepland (kit, theme, constanten). Fonts als de stack die Desktop zelf schrijft: `'Segoe UI', wf_segoe-ui_normal, helvetica, arial, sans-serif` en `'Segoe UI Semibold', wf_segoe-ui_semibold, …`; `wf_segoe-ui_*` zijn de webfonts van de service (antwoord op de Mac-vraag, te bevestigen in de Publish-to-Web-test). |
| D2 + D7 | Geen pagina-achtergrond: **`brand_canvas_v3.py`** (het hulpmiddel dat plan 10 D7 noemt; numpy + Pillow, geditherde JPEG van 31 KB) tekent het night-glow-canvas met de horizon uit de slotmap, en het komt als **decoratieve image-visual `z_canvas`** op z 0, zodat het met de visuals meeschaalt. Een eerste SVG-port in `opzet_backgrounds.mjs` gaf zichtbare banding en is teruggedraaid; dat script is nu gemarkeerd als niet meer gebruikt. Beide pagina's delen één canvasbestand (zelfde horizon). Kaartschaduw via de per-visual `dropShadow` van de kaartframes (geen theme-schaduw). **Horizon = bovenkant eerste kaartrij + 64 = y 248**: de +128 uit plan 10 (y 312) is gemeten op de `main`-layout; op v3 eindigt de P1-KPI-kaart op y 304 en zou hij los in de zone zweven. |
| D2b | `hangerLayer()` in hetzelfde canvas, binnen de zone. |
| D3 | Zonetekst licht: masthead en subtitel ZONE_MUTED, kop ZONE_TEXT, eyebrow ZONE_EYEBROW. |
| D4 | Kaartframes zonder haarlijn, met schaduw. Binnentegel `z_tile_rec` (de aanbeveling) krijgt onder de D7-waiver de blauwe gloed; de bookmarkcode verbergt `z_tile_*` al in de planstaat. |
| D5 | Kleurnamen uit copy, alt-teksten en docstrings; pay-off vervangen door de eyebrow. |
| D6 | Marks ACCENT_MARK, tekst ACCENT, signalen SIGNAL_MARK, zusters en context SLATE (`#8E897D`). `Package Point Color` loopt op v3 via `Package[Preset]`: A ACCENT_MARK, B en C INK, de wolk SLATE (was LILAC, 2,10:1). Chips: de gezichtsloze hanger. |

## 4. Toegankelijkheid (de drievoudige controle)

Basislijn (verkenning 9 november): alle visuals behalve acht tekstvakken hadden alt-tekst, maar alles statisch; 33 alt-teksten waren alleen een measure-naam; drie noemden kleuren die na de merkwissel fout zijn; zeven bevatten hard getypte getallen; decoratief meubilair zat in de tab-volgorde en de brand row werd na de footer voorgelezen; kickers (13 px) en mastheads (14 px) lagen onder de vloer; reekslabels in Warm Grey haalden 3,5:1 (tekst vraagt 4,5:1); de lila wolk 2,10:1; de luchthavenbalken alleen in kleur.

Aanpak:

1. **Machinecontrole**: nieuw `project/tools/a11y_check.py` (stdlib) over de gegenereerde PBIR, het canvas en de zone-samples.
2. **Gerenderde controle**: Desktop via de WebView2-DevTools-poort: screenshots op 1920 en 1366, de accessibility tree (wat een schermlezer krijgt) en een gescripte toetsenbordwandeling.
3. **Onafhankelijke review**: een verse agent zonder mijn bevindingen, met de checklist en de renders.

Onderzoek vooraf (research-first):

- `general.altText` accepteert elke expressie (schema visualConfiguration 2.6.0: `altText: {}`), dus een measure-binding valideert.
- Een PBIR-vlag "hide from tab order" bestaat niet in `VisualContainerPosition`; Desktop schrijft decoratieve visuals met een **negatieve `tabOrder`** (-1, -1000; gezien in Desktop-bestanden van hp-world-champs). Dat gebruiken we; de toetsenbordwandeling bevestigt het.

Uitkomst: zie paragraaf 5 (na de build).

## 5. Uitkomst (9 november)

### Build

Commits op `rebuild-09-10` (lokaal, niet gepusht): merge van design-rebuild, doc 11, kit en model, report-rebuild, renderronde, reviewronde. Renders: `project/deliverables/screenshots/2026-11-09-rebuild-09-10/` (01-03 op 1920, W1366a-c op 1366). Validatie: zie BUILD_LOG.

Ontdekt en opgelost tijdens het bouwen (niet in 09/10 voorzien):

- **Tekstkaarten op 12 pt:** een cardVisual heeft circa 24 px plus 21,5 px per regel nodig (gemeten in Desktop); past de tekst niet, dan eindigt hij zonder waarschuwing op "…". Alle slots zijn daarop gemeten. Drie teksten zijn ingekort waar ze herhaalden wat elders staat: `Rec Rules` (zonder de namen van de groei-initiatieven, die in de plantabel en Rec Mix staan), `Not Funded` (kortere reden), `Footer P2` (één regel). R5 is ingekort om onder de folio te passen. **Graag even naar kijken, Bjorn.**
- **`responsive` uit op alle grafieken:** het verkleinde 12 pt-astekst in kleine grafieken onder de vloer. Wat de planstaat dan niet kwijt kan, is met de hand weggelaten: de waardeas van de waterval (elke balk draagt zijn label; de uiteinden komen uit het model, `Waterfall Y Start/End`) en beide assen van de cumulatieve grafiek (het terugverdienjaar staat in de titel, de eindwaarden in de alt-tekst, de nullijn heet "Break-even").
- **De oudste renovatieband in Tangerine** in plaats van Coffee Blue: het is een risicosignaal (de enige negatieve NPS), en blauw betekent in kit 3.1 "Goodnight Inn, ons plan".

### Toegankelijkheid: drie controles

1. **Machine** (`project/tools/a11y_check.py`): 0 fouten. De check vangt vijf geplante defecten in een kopie (alt weg, kleurwoord en getal in alt, font 10 pt, donkere tekst op de zone, footer vóór de kop in de tab-volgorde) en daarna ook een statische alt op een knop met een measure-label. Contrast op de zone, gemeten op de lichtste pixel onder elke tekst: kop 7,4:1, eyebrow 9,0:1, masthead 5,3:1, subtitel 5,2:1.
2. **Gerenderd** (Desktop, DOM en accessibility tree via DevTools): de namen die een schermlezer krijgt kloppen met het canvas; de tab-volgorde in de DOM (`tab-order`) is die van de generator; decoratief meubilair heeft een negatieve volgorde. Hierbij gevonden en hersteld: een fout in `Alt F2 Chart` (alle zustermerken lazen 29,1 %, het filter werd in de iterator gewist), een masthead in hoofdletters als naam, het voorvoegsel "Button:", afgekapte teksten, een scrollende foliotabel en plantabel, een afgesneden tooltiplabel, `responsive`. **Niet te verifiëren in Desktop:** de toetsenbordwandeling (in bewerkmodus is alles focusbaar en blijft de focus in de visual-header hangen) en schermlezergedrag in leesmodus. Bladermodus van een schermlezer volgt de DOM, en Power BI sorteert die op positie: de koppen van de drie F-kolommen worden naast elkaar voorgelezen voor hun grafieken; Tab volgt wel de ingestelde volgorde.
3. **Onafhankelijke review** (verse agent, zonder mijn bevindingen): 0 blockers, 6 major, 8 minor, 4 notes.

| # | Bevinding | Afhandeling |
|---|---|---|
| 1 | Pakketkaart alleen met de muis | Opgelost: de wolk (456 pakketten) is een tabstop met header (Show as table) en terugverdienjaar, NPV-bandbreedte en initiatieven in de Tooltips-bron; "Hover a dot" uit de alt-tekst. |
| 2 | F1-alt sprak de titel tegen | Opgelost: stijgt tot 36,5 % in 2023, daalt naar 33,7 % in 2025, kloof 8,4 naar 10,6 punten. |
| 3 | F1-lijnen alleen op kleur | Opgelost: namen aan de lijnuiteinden, zoals F2. |
| 4 | Cumulatief: jaar onleesbaar, blauwe lijn zonder naam | Opgelost: titel met terugverdienjaar uit het model, legenda met lijnstijlen (Low gestreept, Expected gestippeld, High doorgetrokken, "This case" dik blauw), de lijn van het gekozen scenario neemt het pad over. De grafiek blijft klein (96 px). |
| 5 | Knopnaam bevat het zichtbare label niet (WCAG 2.5.3) | Opgelost: `Alt Open Plan (text)`; nieuwe regel in a11y_check. |
| 6 | 12 pt is op 1366 effectief ~8,5 pt | **Besluit Bjorn** (12 pt-vloer; 14 pt kost een herindeling). Browserzoom testen in Publish-to-Web. |
| 7 | F4-labels in de balktoppen | Opgelost: as tot 1,3. |
| 8 | P&K Select en Maison d'Or zelfde grijs | Geaccepteerd: beide zijn context; namen met hulplijnen, waarden in de alt-tekst. |
| 9 | Chipkolom, "·", korte koppen in de plantabel | Geaccepteerd: de Status-kolom draagt de staat; de alt-tekst noemt de kolommen voluit. Schermlezeruitspraak van de beeldcel: P2W-test. |
| 10 | NPV en capex niet uitgeschreven | Opgelost: "net present value (NPV)" in de P2-subtitel en in de alt-teksten. |
| 11 | Alt begint met grafiektype; F4 op hele procenten; watervalvolgorde | Opgelost (nieuwe regel in a11y_check); middenpunten in voorgelezen tekst: P2W-test. |
| 12 | Alt-teksten boven 250 tekens | Opgelost: alle alt-measures ≤ 241 in alle 9 combinaties scenario × focus (DAX-query in Desktop); `Alt Rec Held` voor de kaart van 261 tekens. |
| 13 | Blauw betekent twee dingen | Opgelost waar het botste: oudste band in Tangerine. Waterval: plus blauw, min Tangerine, met teken. |
| 14 | Locale-mix (decimale komma's) | Bekend (N10), P2W-test. |
| 15 | 27 tabstops, logo-alt | Opgelost: kickers uit de tab-volgorde (titel leest "F1, the margin. …"), P1 nu 22 stops; logo "Goodnight Inn". |
| 16 | Dropdown zonder zichtbare rand | Opgelost: pilrand in Dusk. |
| 17 | "Marker size" in Show as table | Geaccepteerd (alleen in de A/B/C-laag). |
| 18 | `check_contrast.py` toetst alleen themaparen | Afgevangen door a11y_check (echte paren, zonepixels); het framework-script is read-only. |

### Inhoudelijke acceptatiechecks (09/10)

- R1: de zin in F1 ("Room rates rose 2.7% since 2023, in line with the other brands (1.6% to 4.7%)") komt overeen met `42_price_index.py` (ADR-index 2023 = 100: GN 102,7, zusters 101,6 tot 104,7).
- R2: NPS staat nergens als dé merk-KPI; de cel heet "Guest quality: net promoter score".
- R3: de marginale bijzin verschijnt in alle 9 combinaties en klopt met `packages.csv` (Expected −$1,1M, Low −$2,6M, High −$0,1M).
- R4 en R5: leesbaar op 1366 (W1366c, W1366a).
- D1: `B5175F` komt nergens meer voor in generators, model of rapport.
- D6: Tangerine tekent geen merk of reeksidentiteit (Low, kosten in de waterval, de oudste band, NPV onder nul in de tooltip).

### Nog open (bij Bjorn)

- **Publish-to-Web-gate:** toetsenbordwandeling in leesmodus; schermlezer (NVDA of VoiceOver) op de link, inclusief de chipcel en de middenpunten; Segoe UI op een Mac of in een browser zonder Segoe UI (`wf_segoe-ui_*`); browserzoom op 1366; locale (N10); de pakkettooltip met de muis.
- Push van `rebuild-09-10` en een PR.
