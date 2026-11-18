# 16 - FinalV2 gebouwd, 12 november 2026

**Datum:** 2026-11-12 · **Op verzoek van:** Bjorn ("Lees bouwplan 15 en voer het volledig uit, fase voor fase. Begin met de
route naar main") · **Bron:** doc 15 (bouwplan), doc 14 (review) · **Branch:** `feedback-ronde-4` · **Renders:**
`project/deliverables/screenshots/ScreenshotsFinalV2/` (README met per render het bewijs en de niet-gemaakte P2W-set).

## Route naar main (fase 6, op Bjorns verzoek als eerste)

PR's #2, #5, #8 en #11 gesloten ("Vervallen: ingehaald door feedback-ronde-4 (FinalV2)."); PR #12 (`feedback-ronde-4` →
`main`, FinalV1 en docs 13-15) gemerged als `6eaee33`; `main` daarna teruggehaald in de werkbranch. De FinalV2-build gaat
in een tweede PR naar `main`.

## Fase 0 - S6 pariteit

Generators in een scratchmap gedraaid en semantisch gediffd tegen `1361f71`: 119 rapportbestanden verschilden, waarvan
115 alleen in `z` en `tabOrder` (Bjorns lagenpas van 11 nov, en Desktops `active: true` op kolomprojecties). Geen enkel
x/y/w/h-verschil: de kopposities zaten al in de generator (ronde 9). Overgenomen: de z- en tabvolgorde van alle 112
visuals op P1 en P2 in `project/design-prototypes/opzet-layering.json`; `opzet_report.py` legt ze als laatste over de
gegenereerde waarden (`layered()`), ontbrekende visuals houden de generatorwaarden. Verworpen als Desktop-artefact: schema
2.14, sleutelvolgorde, `drillFilterOtherVisuals`, bookmark-versie 1.0, de Deneb-runtimeobjecten (`developer`,
`stateManagement`, `vega.version`) op de selector, de gestripte tekststijl op het lege paneel-kaartje, de alfabetische
resourcevolgorde in report.json, en in het model: de weggelaten `dataType`-regels op berekende tabellen, de
broncode-opmaak, `ref cultureInfo en-US` plus de map `cultures/` (de generator schrijft die niet; na elke rebuild
verwijderd). Rebuild = `1361f71` op alle posities (17 bewuste verschillen: de chips en de voetregel van fase 1).

## Fase 1 - M2

- **Hanger:** `brand_canvas_v3.night()` plakt het masker op y −56 (was −150). Het plan zei ±50 px; gemeten (mask-bbox)
  is het gat 144 px hoog en stond op y 1-87, dus 50 px lager (y 22-166) liep de masthead (y 20-44) er nog doorheen. Op
  −56 staat het gat op y 66-210: onder de masthead, ook met Desktops 15 px-drift van een Fit-achtergrond, en 22 px boven
  de horizon (232). Hele scene opnieuw gegenereerd en als resource vervangen; geen overlay-visual (`SCENE_VISUAL`
  blijft False). Render 01.
- **Chips:** naar de voetregel, x 1216/1384/1552/1720, w 160, **y 1024** (het plan zei 1032; op 1032 eindigt de pil op de
  paginarand en Desktop knipt de onderrand en de descenders af, render 12 nov), h 48, geen verticale padding (met 4 px
  kapte de naam). Tabvolgorde 52010-52040 (na Bjorns voetregel 52000, niet 9010: zijn nummering telt in duizendtallen).
  `z_footer2` w 1152. **Kleuren afgeweken van het plan:** de night-zone-tokens (ZONE_EYEBROW/ZONE_TEXT/ZONE_MUTED) vielen
  op de crème ondergrond op 1.1:1 (a11y_check 16 fouten); de pil draagt nu de kickerkleuren van de witte kaarten: code
  Burnt Tangerine, naam Dusk, hairline Warm Grey. Tooltip-binding ongewijzigd. Render 02.

## Fase 2 - M1

`TT Range SVG` herschreven, 416 x 72 (het plan gaf 56 vrij; met B onder de band en een eigen labelrij was 72 nodig).
Regels: (1) Low/High op een eigen rij (baseline 66) onder streepjes, band, stip en B's letter; Low eindigt op de bandstart
(of begint op de linkerrand als de band binnen 80 px start), High begint op het bandeinde of eindigt op de rechterrand
als er geen 88 px over zijn; geen klem onder een streepje meer. (2) A en B binnen 24 px: A boven de band met een streepje
van letter tot bandrand, B onder de band met een streepje van bandrand tot letter (baseline 50); de twee streepjes raken
elkaar niet, ook niet op 2 px afstand (A 345, B 343 op de vaste as). (3) C alleen bij ≥ 24 px van break-even, A en B.
Lay-out: `tt_range_svg` h 72, kaart 1 h 256, kaart 2 y 312, canvas 480 x 552. Renders 16 (A) en 17 (C): geen botsing.

## Fase 3

- **S1** F2 op P1: legenda bovenaan, geen lijneindlabels. **Terugval toegepast** (de besliste uit paragraaf 8): met vier
  lijnen waren de drie zusters één Warm Grey, dus drie identieke grijze legendastippen (REVIEW m3, de reden waarom de
  lijneinden ooit de namen droegen); P1 toont nu, als de tooltip, Goodnight Inn tegen "The other three brands"
  (`Trend OTA Sisters`). De alt-tekst noemt de zusters nog apart.
- **S2** labels "NPV range, $M" in de drie cijferkaarten; `Build WF Note (text)` als gedempte titel (12 pt Dusk, niet vet;
  `chart(..., muted=True)`): leeg "Pick moves on the left; your plan appears here.", gevuld "Where your NPV comes from,
  $M through 2032 (scenario)". De titelrij kostte 24 px: `c_you_rules` h 32, waterval y 456 h 160, asmarges 1.6x + $1M
  (`Build WF Y Start/End`), anders stonden de labels op de balken. Renders 04-06.
- **S3** `line_pair`: merk in Coffee Blue, gehoverde band/hotel Night. Daarbij een ronde-10-fout hersteld: de `valueAxis`
  van die grafiek was in een regelcommentaar beland (geen rasterlijnen, geen 50-100 %-bereik op het hotel).
- **S4** "ends within $1M of A by 2032". **S5** "fell 2.8 points since 2023", op de afgeronde getoonde waarden zoals de
  KPI-regel (REVIEW M8; ongerond gaf 2.7 naast −2.8). **N1** `Move Capex (text)` één decimaal. **N2** merkregels op
  `$#,0.00`. **N3** "where the four options stand". **N4** nullijn F3 `width 2`. **N5** tt-f1/f2/f3: grafiek en noot 8 px
  omlaag (gemeten leegte 18-25 px). **N6** `Segments 2025 (text)` van de hotelpagina; de pagina 64 px korter (480 x 400)
  in plaats van lege ademruimte.

## Fase 4 - M3

Geaccepteerd zoals besloten; de nl-NL-mix staat in de README van de set als bekende beperking (render 26 is P2W).

## Fase 5 - M4 Publish-to-Web-poort: NIET GEDAAN

Publiceren is Bjorns handeling (rule mutation-safety); er is nog geen jurylink. De renders 20-28 ontbreken, met een
notitie in de README. Desktop-bewijs dat alvast staat: tooltips op 480 px met `useScaledTooltips`, de Deneb-selector die
de cijfers stuurt (05, 06 via de filter-stand-in).

## Poorten

validate_tmdl --strict 34 bestanden 0 fouten; a11y_check 0 fouten, 0 notities; schema_check 182 bestanden 0 falend
(cache aanwezig); pbir_detect 4 onbewaakte bevindingen (was 8: de chipkleuren zijn weg; rest = kopposities op het 4
px-raster en `#EAF2FB` op de leesgids-tegel en in de Deneb-spec, alle van vóór deze ronde); Microsofts validator 1 fout
(de bekende `categoryLabels.backgroundColor` op de A/B/C-laag) en 25 waarschuwingen (24 tekstvakken van 24 px, de
dubbele filternaam `flt_top7`), ongewijzigd. Model 454 maten (+ `Build WF Note (text)`).

## Werkwijze renders

Twee Desktop-vensters: het project (P1, P2 rec, tt-f1..f4) en een wegwerpkopie in de scratchpad (`copyprep.py`: voorbeeld-
filters op tt-package/tt-f3-band/tt-f4-hotel/tt-year, bookmark-zichtbaarheid, bouwplan als visual-filter op de zes
build-targets). Het project krijgt nooit voorbeeldfilters (les van 11 nov). Vensters op 1280 x 800 gezet (een venster
over twee schermen gaf een pagina van 530 px). `crop.py`: kaders beginnen op y 168 op beide pagina's (de docstring zei
184; de V1-crops van P1 stonden daardoor 16 px te hoog, de V2-set is goed).

## Open

- Publish-to-Web-poort (fase 5) en de renders 20-28; de inzendnotities (nl-NL-notatie, Deneb-toetsenbord).
- Bjorns blik op FinalV2; de tweede PR naar `main`.
- Desktop-vensters: Bjorn sloot beide met Opslaan (12 nov, na de merge). De project-save schreef een oudere stand van
  tt-package en tt-f4-hotel terug (lay-out en canvasbeelden; die pagina's waren alleen in de kopie herladen) plus
  Desktop-artefacten. Teruggezet naar `c8d13c6` via `git stash` ("Desktop-save 2026-11-12"); niets verloren. Regel
  voortaan: de agent sluit zijn eigen Desktop-vensters zonder opslaan aan het eind van de ronde.

## Restpunten uit verificatie 17 (12 nov, middag)

Bron: [doc 17](17-verificatie-finalv2-2026-11-12.md), "Wat nu nog moet" 1 en de README-opdracht. De P2W-poort (punt 2)
doet Bjorn handmatig na publicatie.

- **Watervalnaam leesbaar.** `BuildMove` kreeg een kolom `Waterfall Label` (SWITCH op ProjectID, hoogstens 12 tekens:
  Booking app, Revenue mgmt, Kiosks, Breakfast, Gatwick +40, Toronto +40, Kingston +40, Energy, Boston hotel,
  Refresh 10; `sortByColumn: Sort` zoals Short Name). Alleen `ch_build_waterfall` gebruikt die kolom; selector,
  tooltips en de A-waterval houden de volledige Short Name. Generator `sketch_model.py` (BUILD_MOVE + kolomlijst) en
  `opzet_report.py` (regel 853). Echte diff: BuildMove.tmdl +10 regels, ch_build_waterfall/visual.json 3 regels.
  Render 05: "Booking app / Revenue mgmt / Toronto +40", twee regels, geen ellips; 06: "Energy / Boston hotel /
  Refresh 10".
- **Echte klikrenders 05 en 06.** Wegwerpkopie in de build-stand zonder enig filter (`copyprep.py build A -`), venster
  1920 x 1080 op het hoofdscherm. `mouse_event`-klikken bereikten Deneb niet (Desktop selecteert dan alleen de visual-
  container, render 12 nov); `PostMessage` van WM_MOUSEMOVE/LBUTTONDOWN/LBUTTONUP naar de `Chrome_RenderWidgetHostHWND`
  van de rapportweergave wel (scratch-script `click_post.ps1`; rijcoördinaten: pagina-oorsprong op scherm (47,5; 182,5),
  0,765 schermpx per logische px, rijen 26,8 px hoog onder een kop van 32). Rij 1/2/6 (GI-01, GI-10, GI-04) → 05:
  drie vinkjes, voetregel "Picked: 3 moves, $13.2M of $60.0M", tegel "Your plan: 3 moves, live by May 2028". Herladen,
  rij 10/9/8 (GI-07, GI-08, GI-03) → 06: voetregel in Tangerine "Over budget by $9.25M: $69.25M picked, the cap is
  $60.0M", alarmband. Geen visual-filters meer in 05/06; de README zegt dat. Rijvolgorde uit het model (DAX via de
  modeling-MCP op poort 49158): GI-01, GI-10, GI-02, GI-09, GI-05, GI-04, GI-06, GI-03, GI-08, GI-07.
- **README** herschreven: werkwijze per render, de watervalkolom, "Totaal" (nl-NL), en een paragraaf over wat alleen de
  gepubliceerde versie kan tonen (20-28, toetsenbordronde, tooltip zwevend op zijn plaats, 1366 px in de browser).
- **Poorten:** validate_tmdl 34 bestanden 0 fouten; schema_check 0 falend; a11y_check 0; pbir_detect 4 onbewaakt
  (ongewijzigd, van vóór deze ronde); Microsofts validator 1 fout + 25 waarschuwingen (ongewijzigd, bekend).
- **Desktop** aan het eind gesloten via CloseMainWindow en "Niet opslaan" (UI Automation); geen PBIDesktop-proces
  meer. De projectmap is nooit in Desktop geopend in deze ronde.

## Screenshotronde 2 en de watervalnamen bij 8 tot 10 balken (12 nov, avond)

Bjorn vroeg om extra screenshots in de PR zodat zijn controle-agent de wijzigingen kan nalopen. Bij het renderen van
een plan met acht zetten bleek de fix van de middag onvolledig: vanaf vijf balken kantelt Desktop de aslabels en knipt
ze op circa 75 px af ("Bookin...", "Revenue mg..."), en het eerste label wordt eerder afgeknipt omdat het links buiten
de visual uitsteekt ("Booki..." zelfs bij "Booking").

- **Oplossing gemeten in de kopie:** `categoryAxis.maxMarginFactor` (themaschema 2.143, waterfallChart) op 40 maakte
  het krapper, niet ruimer; teruggedraaid, de as blijft op standaard. De namen zijn op de gemeten breedte gekozen:
  eerste balk (altijd GI-01, sorteervolgorde 1) "App", GI-10 "Rev. mgmt", GI-08 "Boston"; breedste blijvende naam
  "Kingston +40". Alleen `sketch_model.py` (BUILD_MOVE) en de generatorcommentaar in `opzet_report.py` zijn gewijzigd;
  echte diff: BuildMove.tmdl 1 regel.
- **Renders 01 tot 08 allemaal opnieuw** vanaf de gecommitte boom, venster 1920 x 1080, zodat de set één formaat heeft
  (2940 px breed). Nieuw: 07 (acht zetten, $46.45M, binnen budget) en 08 (alle tien, $100.7M, alarm). In 05, 07 en 08
  staat elk label voluit. Bekend en geaccepteerd: bij acht of meer balken raakt het eerste datalabel ("+$3,4M") zijn
  balk (automatische plaatsing van Power BI in een visual van 160 px hoog); in 08 valt de plan-stip buiten de capex-as
  van de scatter ($62M) en wordt dus niet getekend.
- **Desktop-landmijnen van deze ronde:** (1) een modelwijziging (kolomwaarden) komt niet mee met `powerbi-desktop
  reload`; de kopie moet zonder `.pbi`-cache opnieuw geopend worden, waarna Desktop om "Nu vernieuwen" vraagt (data van
  de blob, circa 20 s); (2) de "Niet opslaan"-knop weigerde eenmaal via UI Automation ("Toegangstoets is al
  geregistreerd") en muisklikken bereikten het venster niet; de wegwerpkopie is toen met Stop-Process gestopt (geen
  projectrisico, de projectmap stond niet open); (3) de pid uit de bridge-JSON is Int64 en moet naar `[int]` voor
  UI Automation.
- **Desktop-save om 16:33, niet door mij.** Tussen een schone `git status` en de start van deze ronde waren 221
  bestanden onder project/pbip gewijzigd met het save-patroon (cultures/, bookmark-versie 1.0, z-hernummering,
  tabOrder, ontbrekende regeleinden); de inhoud (Waterfall Label, lay-out) was intact. Geparkeerd in
  `git stash` ("Desktop-save 2026-11-12 16:33"), boom terug naar HEAD. Daarna schijnbaar 221 gewijzigde bestanden na
  regeneratie: dat was alleen stat-ruis van `core.autocrlf` (`git diff --stat` 5 bestanden; werkelijke commit klein).
- **Poorten:** validate_tmdl 0 fouten; schema_check 0; a11y_check 0; pbir_detect 4 onbewaakt (ongewijzigd).

## Hover-signifier en definitiepagina (12 nov, avond, op Bjorns akkoord)

Bjorn: de hovers zitten op essentiele plekken maar niets laat zien dat ze er zijn; en een definitielijst voor de
afkortingen. Akkoord gegeven op het voorstel (een kleine i-in-cirkel in oranje, een verborgen tooltippagina met de
definities), gebouwd in de generatoren.

- **Signifier:** `Info Badge SVG` (sketch_model.py, C14): een ring met een i in Tangerine, 16 px, als SVG-image-measure
  zonder tekst (rendert overal gelijk, ook onder Publish to Web). Geplaatst (`badge()` in opzet_report.py) rechtsboven
  op elk visual dat een paginatooltip opent en nergens anders: P1 de kaarten F3 en F4; P2 de scatterkaart (groot en
  klein), de drie cumulatieve grafieken en de vijf chips. Bij een chip ligt de badge ONDER de chip (de kaart is
  transparant), zodat de chip de hover houdt. Decoratief, buiten de tabvolgorde.
- **Hint:** `Info Hint SVG`, in de voetregelrij van beide pagina's, rechts uitgelijnd tegen de Definitions-chip: de
  badge en "hover for more" (16 px, de vloer). Legt het teken één keer per pagina uit.
- **Definitions-chip** (`chip_def` / `chip_def2`, `pill()` in de generator, dezelfde pil als F1-F4): "Definitions" in
  Burnt Tangerine, "the terms explained" eronder; tooltip = de nieuwe verborgen pagina `tt-glossary` (480 x 544, eigen
  oranje scene via brand_canvas_v3.py; de oudere scenes bleven byte-gelijk omdat de pagina achteraan staat). Alt-tekst
  `Alt Definitions (text)`: de woordenlijst in één adem (245 tekens, onder Desktops limiet van 250), zodat een
  toetsenbord- of screenreadergebruiker de termen ook krijgt.
- **Woordenlijst** (`GLOSSARY` in opzet_report.py, negen regels, één textbox): NPV, capex, run-rate, pays back /
  break-even, Low / Expected / High, NPS, ADR, RevPAR, OTA. In de woorden van het rapport zelf; alleen jaartallen, geen
  getypte cijfers (rente en budget blijven in het model en op de pagina's).
- **Lay-out** (opzet-layout.json): P2 voetregelrij = bronregel 864 px, hint 136 px, vijf chips van 160 px (152 px
  knipte "The fading welcome" af, gemeten); de zoomtoggle 16 px naar links (672) en de scattertitel 600 px zodat de badge
  op 1040 vrij staat. P1: bronregel 1504 px, hint 152 px, chip 160 px. Nieuwe slots dragen z en tab op de schaal van
  opzet-layering.json (dat bestand kent ze niet; `layered()` laat ze staan).
- **Renders:** 01 tot 04 opnieuw (de voetregelrij en de badges), 19_tt-glossary nieuw. 05 tot 08 zijn van de ronde
  ervoor en verschillen alleen in de voetregelrij en de badges (README zegt het). Een tooltip zwevend boven de chip
  staat niet in de set: een geposte muisbeweging opent hem niet in de bridge-capture.
- **Toetsenbord:** hover is niet met het toetsenbord bereikbaar; de alt-tekst van de chip vangt dat op. Een
  bookmarkpaneel met knop blijft de optie als de toetsenbordronde in de service erom vraagt (plan 15, fase 5).
- **Poorten:** validate_tmdl 0 fouten; schema_check 0; a11y_check 0 (incl. SVG-tekstvloer, alt-lengte, leesvolgorde
  met de chip na de bronregel); pbir_detect 4 onbewaakt (ongewijzigd). Model: 458 measures (+4). Desktop: wegwerpkopie
  zonder `.pbi`-cache geopend, "Nu vernieuwen" via UI Automation, aan het eind gesloten zonder opslaan.

## Koplijn in plaats van chips, en de woordenreview (12 nov, laat)

Bjorn op de render van de vorige ronde: de voetregel is weer vol terwijl de kop leeg voelt; de tagline rechtsboven
zegt niets; de tooltipkop "$M, undiscounted" voegt niets toe; en elke tekst op de pagina moet een functie hebben of
weg (AI-tells, bloat).

- **Koplijn** (`header_line()` in opzet_report.py, in het slot van de masthead, rechts uitgelijnd op de Night-band):
  P1 `ⓘ hover for more · Definitions`; P2 `ⓘ hover for more · Revisit the facts F1 F2 F3 F4 · Definitions`. De
  hover-woorden (`hover_word()`: cardVisual in zone_eyebrow, geen pil) dragen de tooltips tt-f1 tot tt-f4 en
  tt-glossary en de alt-teksten van de vindingen en de woordenlijst; de woorden en de punten staan buiten de
  tabvolgorde. De mastheads ("2021 TO 2025 · FOR THE BOARD ..." en "2027 TO 2032 · GOODNIGHT INN BUDGET ...") zijn
  weg; de measures Masthead P2 (text) / Alt Masthead P2 blijven ongebruikt in het model. De voetregel is weer alleen de
  bronregel (P1 1856 px, P2 1152 px). De hint-SVG is 136 px breed in de gedempte zone-inkt (#C9D0DC). Waiver
  zone-text-header-line in pbir-detect-waivers.yaml voor #A9CDF0 op hdr_*.
- **Woordenreview, doorgevoerd** (alles anders bleef omdat het werk doet):
  - Uncertainty: "Read with care: in the Low case no package pays back by 2032, and A ends at ..." → "Low case: no
    package pays back by 2032; A ends at ...".
  - B waarom: "Considered because it swaps the X for the Y: a guest-score effect ..." → "Considered: it swaps the X for
    the Y, a guest-score effect ...". B waarom niet: "Not picked purely on the capex-to-NPV mix: $2.25M more capex for
    an NPV $0.6M lower, so A is simply the better deal." → "Not picked: $2.25M more capex than A for $0.6M less NPV."
  - C titel: "C · Why not renovate? For comparison" → "C · Why not renovate?". C waarom: "Considered as a strategic
    investment: the refresh ... is the move that targets NPS head-on (F3)." → "Considered: the refresh ... is the one
    move aimed at NPS (F3)." C waarom niet: "Not the financial risk to take now: NPV ..." → "Not picked: NPV ...";
    "One to revisit once A has broken even, or if NPS drops below 0 and growth is at risk." → "Revisit once A has
    broken even, or if NPS falls below 0."
  - Alts-intro: "Both were weighed against A; the chart below compares all three over time." → "Both weighed against
    A; the chart below compares all three."
  - Bouw-comparer leeg: "Pick moves on the right to compare your plan with A (Expected case)" → "Your plan against A,
    $M (Expected case)" (de ene instructie staat in het watervalslot: "Pick moves on the left; your plan appears
    here."; "on the right" klopte bovendien niet).
  - Legenda cumulatieve grafiek: "This case" → "Case in view".
  - Jaartooltip: kop "CUMULATIVE NET IMPACT · $M, UNDISCOUNTED" → "CUMULATIVE NET IMPACT, $M"; titel "To the end of
    2030: where the four options stand" → "At the end of 2030"; kaarttitel "Package A, our recommendation, in the
    three cases" → "A in the three cases".
  - Definitiepagina: kop "DEFINITIONS · THE SHORT WORDS ON THESE PAGES" → "DEFINITIONS"; titel "What the terms mean"
    → "The terms on these pages"; het chiplabel "the terms explained" is weg.
- **Bewust gelaten:** "Our reading:" in F2 (gelabelde interpretatie, plan 09 R5); "An association, not proof of cause."
  in F3 (het voorbehoud is de functie); de eyebrow-puns (ronde 9, Bjorn); "HOW TO READ THIS CHART" met de leesgids;
  "Hover a dot for its moves" in de gids (de instructie op de plek zelf); de bouw-intro (concreet: wat volgt de klik).
- **Renders:** 01 tot 04, 18 en 19 opnieuw; 05 tot 08 van de ronde ervoor (voetregel en kop verschillen).
- **Poorten:** validate_tmdl 0; schema_check 0; a11y_check 0; pbir_detect 4 onbewaakt (ongewijzigd, met de nieuwe
  waiver). Desktop: kopie zonder cache heropend, "Nu vernieuwen", aan het eind gesloten zonder opslaan.
