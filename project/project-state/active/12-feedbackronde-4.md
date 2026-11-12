# 12 - Feedbackronde 4: minder tekst, meer oranje, de tooltip, drie standen op P2

**Datum:** 2026-11-10 · **Gevraagd door:** Bjorn (feedback op de renders van 9 november: "The skeleton stands and the lay out does as well") · **Branch:** `feedback-ronde-4` (afgetakt van `rebuild-09-10`; lokale commits per fase, geen push zonder Bjorns ja). Plan van aanpak: `C:\Users\TrainerBjorn\.claude\plans\i-have-some-feedback-prancy-thompson.md` (goedgekeurd 10 november).

## 1. Wat Bjorn vroeg

1. **Minder geschreven tekst.** De conclusie staat in de titel van een visual; de ondersteunende tekst is één zin, hooguit anderhalf.
2. **Iets meer oranje**, zodat het niet alleen blauw en grijs is.
3. **De tooltip op de scatter is het wow-moment**: duidelijk welke acties in het pakket zitten, wat ze kosten en opleveren.
4. **Een duidelijke plek voor "waar kijk ik naar"**, vóór de grafiek zelf.
5. **De interactie rechts klopt niet.** "Considered, not recommended" als tekst onder A is verwarrend; het dropdown-filter rechtsboven zegt niet waarvoor het is; en er is geen manier om zelf een plan samen te stellen. Gewenst: drie standen: de aanbeveling (standaard), B en C met de reden waarom niet, en bouw-je-eigen-plan. In de tweede en derde stand krimpt de scatter en komt onderaan een vergelijking van het cumulatieve netto-effect, A altijd blauw.
6. **NPS**: op de KPI-tegel erbij dat de NPS nog positief is maar daalt.

## 2. Besluiten van Bjorn (10 november, in de sessie)

| Onderwerp | Besluit |
|---|---|
| De selector van bouw-je-eigen-plan | **Deneb** (Vega, geavanceerde cross-filtering: een gewone klik zet een zet aan of uit). Een native button slicer blijft als terugvaloptie achter één vlag (`--selector=native`) voor het geval de Desktop-proef faalt. |
| Navigatie tussen de drie standen | **Een tabbalk** bovenin het rechterpaneel (`Recommended: A` · `Considered: B and C` · `Build your own`); de actieve tab is gevuld. Het dropdown "Package in focus" vervalt. |
| NPS-regel | "still positive, but falling every year · last of 4" (jaar-op-jaar bewaakt in het model; de zusters en de 2021-waarde in de alt-tekst). |
| 136 ongecommitte Desktop-bestanden (hersave van 10 november, P2 in de planstand, scenario High) | Weggegooid, zoals op 9 november. |

## 3. Wat er is gebouwd

**Copy-dieet (sketch_model.py).** `F1 Note`, `F2 Note`, `F3 Note` elk één zin (R1 en R5 blijven als bijzin; de voorrenovatie-telling en de rang gingen naar de alt-tekst). `Rec Note (text)` vervangt `Rec Answers`, `Rec Held` en `Rec Rules` op het canvas: "Each move answers a page-1 finding (F2, F3, F1); the other $50.6M waits until all three are live in Apr 2028, because no further move pays back by 2032." `Alt B/C Why` en `Alt B/C WhyNot`: één zin waarom overwogen, één zin waarom niet gekozen. Scatter-titel begint met "Only". Beide footers één regel. `KPI NPS Context (text)` nieuw.

**Meer oranje, binnen de kitrollen.** De context-regels van de KPI-band in Burnt Tangerine waar het nieuws slecht is (marge gedaald, hoogste OTA-aandeel, NPS laatste en dalend), Deep Coffee waar Goodnight Inn de beste is (`KPI * Context Color`). De F-code in de kickers (F1, F2 …) in Burnt Tangerine. De onzekerheidsregel onder de aanbeveling in Burnt Tangerine. In de vergelijkers: C en "Your plan" in Tangerine, A altijd Coffee Blue. In de tooltip de payback-regel Burnt Tangerine als het pakket niet terugverdient. Tangerine op Night voor de eyebrow-cijfers haalt 4,5:1 niet (4,2:1) en is niet gedaan.

**De leesgids.** Een Ice-tegel boven de scatter (`z_tile_guide`): kicker "HOW TO READ THIS CHART", een legenda met de drie soorten stippen, en één zin uit het model (`Guide (text)`): elke stip is een van de 456 pakketten, capex opzij, NPV omhoog, boven de lijn verdient het terug; hover voor wat erin zit en wat niet.

**De tooltip (`tt-package`, 480 x 488).** Chip, naam, de case rechtsboven (`TT Case`); NPV groot met statisch label, capex; de payback-regel (gekleurd); de drie cases; de kop "In this package: 3 moves, what each costs and returns"; een tabel van de zetten in het pakket (`tbl_tt_moves`: Move · Answers · Capex · NPV, de NPV's afgerond zodat ze optellen tot het pakket, `TT Move *`); en één gedempte regel "Not in it: …" (`TT Not Included`).

**Drie standen op P2 (opzet-layout.json v4, opzet_report.py).** Elke slot, tegel en kaart draagt `state` (een lijst). Drie display-only bookmarks `bm_p2_rec` / `bm_p2_alts` / `bm_p2_build` tonen de visuals van één stand; de tabs zijn knoppen in twee uitvoeringen (actief/inactief), ook per bookmark getoond.

- **rec** (standaard): grote scatterkaart met de leesgids; rechts de aanbevelingstegel (chip, titel, mix, vier getallen, `Rec Note`), de waterval "Where the NPV comes from", het cumulatieve-effectdiagram Low/Expected/High (nu 200 px hoog, met jaar-as), de onzekerheidsregel.
- **alts**: kleine scatterkaart (tweede stapel `hero_s_packages*`, want een bookmark kan een visual niet verkleinen); paneel met titel "Considered, not recommended", twee tegels B en C (chip, titel, drie getallen, waarom overwogen, waarom niet, mini-waterval) en onderaan de vergelijker `ch_cmp_alts` (A Coffee Blue 3 px, B Night, C Tangerine gestreept; titel `Cmp Alts Title`).
- **build**: dezelfde kleine scatterkaart met een vierde laag, de Tangerine stip "Your plan" (`BuildPoint`); paneel met de Deneb-selector `dn_build_selector` (tien zetten, één klik zet aan of uit), de tegel "Your plan" (`Build Title`, drie getallen, de regelcheck `Build Valid (text)` in Burnt Tangerine als een regel niet klopt, de waterval van het eigen plan) en de vergelijker `ch_cmp_build` (Your plan Tangerine tegen A). Leeg: "Nothing picked yet", de vergelijker toont alleen A.

**Model voor bouw-je-eigen-plan.** `BuildMove`: een losgekoppelde kopie van de tien Goodnight Inn-zetten (gesorteerd op Expected NPV); `BuildPoint`: één rij. De `Build *`-measures lezen de selectie via `ALLSELECTED(BuildMove)` (zodat een watervalrij de hele selectie ziet en een ongefilterde tabel als leeg telt) en zetten haar met `TREATAS` op `InvestmentProjects`; pakket-NPV is de som van de zetten (de dataset kent geen interactie-effecten, 40_package_matrix.py). A's visuals zien de selectie nooit: het paneel-interactiemodel zet de selector op `NoFilter` naar alles behalve de zes build-visuals.

**De Deneb-spec** (`project/deliverables/deneb-specs/dn_build_selector.json`, geschreven door `project/tools/build_selector_spec.py`): Vega, geavanceerde cross-filtering. De klik-handler bouwt de nieuwe set uit de rijen die Power BI als geselecteerd meldt (`__selected__ = 'on'`) plus of min de aangeklikte rij en past die toe met `pbiCrossFilterApply(event, filterexpressie, {limit: 50})`; de laatste rij eraf roept `pbiCrossFilterClear()` aan. Geen Ctrl, geen interne staat die van de host kan afdrijven. Bron: deneb.guide, Advanced Cross-Filtering en de PBIR Implementation Guide (credit in CREDITS.md).

**a11y_check.py** kent nu de drie standen (lijsten), kaarten met een stand, en tegels als sub-kaarten in de leesvolgorde (B helemaal, dan C).

## 4. Controles

| Controle | Uitkomst |
|---|---|
| `sketch_model.py` | 30 tabellen, 418 measures, 22 relaties; `validate_tmdl.py` 0 fouten |
| `opzet_report.py` | P1 41 visuals, P2 69 visuals (37 verborgen in de rec-stand), tooltip 10; 3 bookmarks |
| `schema_check.py` | 131 bestanden, 0 fouten (ook het Deneb-visual en de `DataFilter`-interacties) |
| `a11y_check.py` | 0 fouten, 0 notities, over de drie standen |
| Desktop | drie standen, Deneb-klikken, tooltip, Low/High, 1366: zie §5 en `SELF-REVIEW.md` |

## 5. Status en open punten

- [x] Desktop-proef Deneb (10 november, `screenshots/2026-11-10-feedbackronde-4/07-10`): het visual laadt uit AppSource, een gewone klik zet een rij aan, een tweede klik uit; de getallen, de waterval, de vergelijker en de stip op de scatter volgen. Geen terugval nodig.
- [x] Renders 1920 (P1, P2 in drie standen, Low/Expected/High, de tooltip op A en C, de selector met drie en vier zetten) en 1366 (vier shots); `SELF-REVIEW.md` erbij.
- [x] Correcties na de eerste render: scattertitel korter, leesgids 112 px (twee regels), de mini-watervallen van B en C vervangen door de zinnen plus een payback-regel, cijfers op 18 pt op de kaarten met drie getallen, tooltip 480 x 520, "level"-geval in de vergelijker-titels.
- [ ] Toetsenbordpas in de leesmodus (tabs bereikbaar en benoemd); de Deneb-selector is met het toetsenbord niet te bedienen: bekende beperking (BUILD_LOG, SELF-REVIEW).
- [ ] Bjorn: Publish to Web mét het Deneb-visual (certified; poort 08 V2, R6/N10), de tooltip met een muis, zoom op 1366.
- [ ] Commit na Bjorns ja (alles staat ongecommit op `feedback-ronde-4`); `rebuild-09-10` is nog niet gepusht.

## 6. Ronde 5 (10 november, tweede blik van Bjorn op de renders van ronde 4)

**Gevraagd.** (1) A, B en C goed geplaatst op de scatter, in alle drie de standen. (2) B is puur op de capex/NPV-mix niet gekozen, A was simpelweg beter; C is overwogen als strategische investering gericht op NPS, niet het financiele risico van nu, opnieuw bekijken bij break-even of als NPS onder 0 zakt. (3) De leesgids: 456 mogelijke combinaties van de aangeboden acties binnen het budget. (4) Een groot alarm in bouw-je-eigen-plan zodra de selectie het budget overschrijdt. (5) De tooltip: ontwerpelementen (hij was wit en vierkant) en capex en NPV met hetzelfde aantal decimalen.

**Gebouwd.**
- **Letters A/B/C.** De A/B/C-laag kreeg een eigen groottemaat per stapel (`Named Point Size`, `Named Point Size (small)`). Gemeten in Desktop: Power BI tekent de diameter evenredig met de waarde tot een plafond per visual; in de grote scatter staan de letters nu gecentreerd in stippen van 22 px (5.8 / 5.3 bij multiplier -40). In de kleine scatter zet Power BI de letters ONDER de stippen, ongeacht de grootte (16, 23, 29 px geprobeerd; bij -40 plafonneert hij de stippen op 10 px). Daarom tekent de kleine laag de letter als een Night-label onder de stip (`categoryLabels.enableBackground`), wit op Night, leesbaar op Ice, wit en de wolk.
- **B en C.** `Alt B WhyNot`: "Not picked purely on the capex-to-NPV mix: $2.25M more capex for an NPV $0.6M lower, so A is simply the better deal." (het NPV-verschil uit de getoonde, afgeronde cijfers; bewaakt voor een scenario waarin B hoger uitkomt). `Alt C Why`: "Considered as a strategic investment: the refresh of the 10 oldest hotels is the move that targets NPS head-on (F3)." `Alt C WhyNot`: "Not the financial risk to take now: NPV -$23.4M, below zero in every case, even High (-$11.4M). One to revisit once A has broken even, or if NPS drops below 0 and growth is at risk." De why-not-slots 96 px (drie regels), de payback-regel op y 608.
- **Leesgids.** `Guide (text)`: "Each dot is one of 456 possible packages: a combination of the 10 moves on offer that stays within the $60.0M budget (at least 3 moves, 1 of them growth). ..." (aantallen en budget uit het model); tegel 136 px, tekst 96 px (drie regels), de grote scatter 24 px lager (y 384, h 616).
- **Budgetalarm.** De titelrij van de tegel "Your plan" is het alarm: boven het budget wordt hij een Tangerine-band met witte tekst van 18 pt ("Over the $60.0M budget by $16.65M"; WCAG grote tekst, 4.2:1). Techniek: `dyn(..., fill_measure=)` zet de achtergrond van het visual op `Build Title Fill` en de tekst op `Build Title Ink`, tak voor tak gepaard; `a11y_check.py` controleert zulke paren per tak (`ordered_colours`) en kent nu ook de tegelvulling onder een visual (`TILE_FILL`). De Deneb-selector kreeg een voetregel (`footerH` 28): "Picked: 3 moves, $22.4M of $60.0M", en in Burnt Tangerine vet "Over budget by $16.65M: $76.65M picked, the cap is $60.0M" (dataset +`CapexNum`, +`Budget`). De regelzin zegt nu "over the budget". De cijfers op de tegel 16 pt (drie kolommen in 464 px).
- **Tooltip.** De pagina is transparant met een eigen basiskaart (radius 12, zonder schaduw), een Night-kopband (chip, naam, case; de onderhoeken recht gezet door een tweede tegel met radius 0) en een Ice-tegel onder de zettentabel; canvas 480 x 552, "Not in it" drie regels. Capex en NPV in de tooltip allebei met twee decimalen (`fmc2`, `sfm2`; `shown_parts(expr, unit)` rondt de zetten nu op $0.01M zodat ze blijven optellen). Desktops tooltip-container houdt zijn eigen rechte hoeken (bekend).
- **Renderen op afstand.** Met een losgekoppelde RDP-sessie tekent de WebView alleen een frame direct na een viewportwijziging: elke shot na een `metrics`-wissel, lege (witte) frames weggegooid. Vastgelegd in `SELF-REVIEW.md` van ronde 5.

**Controles.** `validate_tmdl` 0, `schema_check` 134 bestanden / 0 fouten, `a11y_check` 0 fouten; renders en `SELF-REVIEW.md` in `project/deliverables/screenshots/2026-11-10-feedbackronde-5/` (rec, alts, build leeg / drie zetten / twee zetten / boven budget, tooltip C). Model 30 tabellen, 424 measures.

**Open.** Zie par. 5: toetsenbordpas, Bjorns Publish-to-Web-poort met Deneb, commit na Bjorns ja (alles ongecommit op `feedback-ronde-4`).

## 7. Ronde 6 (10 november: de voetnoot, de tooltip als bewijskaart, F1-F4 als referentie op P2, hover-detail op F3 en F4)

**Gevraagd.** Bjorn: (1) waarom staat "Not shown: ..." in de bronregel (antwoord: onderzoeksronde R4 van 9 november, een bewuste scopingzin; besluit: weg van het canvas, naar de inzendnotities); (2) tooltip-data die het verhaal van F3 en F4 verrijkt; (3) F1 t/m F4 zichtbaarder en als referentie op P2, hover om de conclusie en het visual terug te zien zonder terug te bladeren. Plus een second opinion (Fable 5.2) op de pakket-tooltip: de "core four" (oordeel over drie cases, range bar met break-even, waterval per zet, vaste zettenraster), SVG-in-DAX in native visuals, geen drillthrough (tweepaginalimiet), geen animatie, geen Deneb/HTML in tooltips.

**Gebouwd.**
- **Voetnoot.** `FOOTER` (P1) en `Footer P2 (text)`: bron plus de twee echte voorbehouden (gewogen gastscores, 2021 als gedrukt basisjaar; parameters en afronding op P2). De scopingzin staat niet meer op het canvas.
- **Pakket-tooltip als bewijskaart (`tt-package`, 560 x 568).** `TT Payback (text)` is een oordeel over alle drie de cases ("Does not pay back by 2032, not even in the High case" / "... except in Low; cash positive from 2031" / "only in the High case" / "in every case"). `TT Range SVG`: een vaste NPV-as voor alle 456 pakketten, de wolk als histogramstrook, A/B/C-streepjes met letters, de Low-High-band met de Expected-stip, de break-even-lijn, Low en High als getal. `TT Moves SVG`: de zetten als lijst (positief eerst, de zinker laatst) met capex, NPV en een watervalbalk per zet op een schaal per pakket, plus een totaalrij; de zet-NPV's afgerond op $0.01M zodat ze optellen. `TT Move Grid (svg)`: de tien zetten in de vaste volgorde van de selector, gevuld = in het pakket. Alles SVG-in-DAX in image-visuals (het chip-patroon; conventies van Kerry Kolosko, CREDITS). Een `tableEx` met beeldkolom is geprobeerd en afgewezen (de tabel maakt beeldcellen vierkant en negeerde de verborgen sorteersleutel). Tekst-tweelingen: `TT Range (text)` en `TT Moves (text)` in de tooltip-well van de toetsenbordlaag, `Alt TT Moves` noemt ook wat er niet in zit. `a11y_check.py`: elke `font-size` in een SVG-measure wordt aan de 16 px-vloer gehouden.
- **F1-F4 op P2.** Vier chips rechtsboven in de nachtbanner (waar het vervaagde merkteken zit; Bjorns plek): code in eyebrow-blauw, naam in wit, haarlijn; alt-tekst = de kopzin van de bevinding. Hover opent `tt-f1` ... `tt-f4` (560 breed): nachtband "F# · naam", de kopzin, dezelfde grafiek als op P1 (de P1-bouwers zijn functies geworden: `f1_chart` ... `f4_chart`, `f2_folio`, `f4_types`), de noot (F4: de drie bezettingscijfers). Een card visual neemt een report-page tooltip: de spike slaagde, geen terugval nodig.
- **Hover-detail.** `tt-f3-band` (op `Hotels[Renovation Age Label]`): kop met hotels en kamers, NPS / bezetting / RevPAR 2025 met de merkcijfers eronder, NPS 2021-2025 band tegen merk, de twee zwakste gastscores (`Weakest Scores (text)`). `tt-f4-hotel` (op `Hotels[Hotel Short Name]`): kop met locatietype en kamers, bezetting / ADR / RevPAR 2025 met de merkcijfers, bezetting per maand 2025 hotel tegen merk, de drie grootste gastsegmenten (`Segments 2025 (text)`). Gebonden via `chart(..., tooltip_page=)`; de alt-tekst van de F3-grafiek zegt wat een hover toevoegt. Map 14 in het model.
- **DAX-lessen.** `rows` en `top` zijn gereserveerde woorden (hernoemd); een measure met syntaxfout breekt elke query op het model ("SYNTAXERROR"); de SVG-kleurhelper overschaduwde even de `PCT`-formaatstring (hernoemd naar `HX`).

**Controles.** `validate_tmdl` 0, `schema_check` 191 bestanden / 0 fouten, `a11y_check` 0 fouten; alle measures evalueren zonder fout (INFO.MEASURES). Renders en `SELF-REVIEW.md` in `project/deliverables/screenshots/2026-11-10-feedbackronde-6/` (P1, tooltip op A / C / wolk, P2 met chips, vier chip-tooltips, F3-band, F4-hotel). Model 30 tabellen, 442 measures; rapport 2 pagina's + 7 tooltip-pagina's.

**Tooltip-huid, definitief (11 november, na twee afgekeurde pogingen).** Bjorn: ontwerp elementen die voor de tooltip gemaakt zijn, pers geen bestaande ergens in. Een tooltip is nu een dashboard-KAART, geen miniatuur van de pagina: witte pagina (de strook die de tooltip-host boven de pagina schildert krijgt de paginakleur en valt zo weg), een kicker-regel in de kleuren van de bevinding (de `kicker()` van het dashboard), de titel, de inhoud; de hanger-chip is het enige merkteken op de pakketkaart. Geen banner, geen lockup, geen nachtband, geen ingesprongen kader. Alle zeven tooltip-pagina's.

**Paginaachtergrond (11 november).** De witte/Oat strook boven de banner in Desktop: Desktop schildert de paginaachtergrond over een weergavegebied van 1100 px voor een pagina van 1080, dus de achtergrondKLEUR werd zichtbaar. De rapportpagina's hebben nu de nachtscène zelf als achtergrondbeeld (`canvas-night-page.jpg`: dezelfde scène met 20 px banner erboven, linksboven verankerd op ware grootte, uit `brand_canvas_v3.night(extra_top=20)`), zodat de banner bovenaan begint; het canvas-visual op de pagina blijft de exacte scène van 1920 x 1080, uitgelijnd met de kaarten, in elke host. Niets op het canvas is verschoven; `brand_canvas_v3.py` leest de horizon alleen uit de rapportpagina's.

**Open.** Zie par. 5; de commit op `feedback-ronde-4` na Bjorns ja (rondes 4, 5 en 6 staan ongecommit).

## 8. Ronde 7 (11 november: de tooltips als de pagina in het klein; de pakket-tooltip afgeslankt)

**Wat Bjorn vroeg.** Na de push van rondes 4 tot 6 (commit `ec39cd1`): een tooltip-eigen ontwerp met de midnight-banner
en een titel in de stijl van de pagina, daaronder de visuals in kaarten met dezelfde pop-out-schaduw, als een miniatuur
van de pagina in zinnige verhoudingen; voor alle tooltips. En de scatter-tooltip inhoudelijk afslanken: te veel
informatie, de gemarkeerde blokjes (het zettenraster) ogen rommelig.

**Wat er is gebouwd.**
- Elke tooltip-pagina heeft nu een eigen nachtscene op eigen maat (`brand_canvas_v3.tooltip`, `canvas-tt-<pagina>.jpg`):
  de Night-naar-navy band tot een horizon 24 px onder de eerste kaart, het Coffee Blue-licht rechts, de haarlijn op de
  horizon, daaronder de Oat-pagina met haar zachte gloed; geen hanger (een stempel op dit formaat). De scene staat als
  `z_canvas` op de pagina en, 20 px hoger, als achtergrondbeeld, zodat de strook die de tooltip-host boven de pagina
  schildert ook banner is (dezelfde oplossing als voor de rapportpagina's in ronde 6).
- Banner: de kicker op y 16 in de eyebrow-stijl van de pagina (`F3 · THE FADING WELCOME`, `PACKAGE C · EXPECTED CASE`),
  de titel op y 40 in wit Segoe UI Semibold. Kaarten: wit, radius 12, de kaartschaduw van de pagina, 16 px marge en
  16 px binnenruimte, 24 px in de banner hangend. Lay-out v7; het raster van 8 px, de kaartgrenzen en de paginahoogte
  worden door het lay-outscript gecontroleerd.
- Pakket-tooltip, afgeslankt (560 x 536): banner (kicker, titel); kaart 1 = NPV, capex, het oordeel over de drie cases,
  de bereikbalk op de gedeelde as (band Low-High, Expected-punt, break-even, A/B/C-streepjes, de getallen Low en High);
  kaart 2 = "In this package: n moves" met de lijst Move | Capex | NPV en een totaalregel. Weg: de hanger-chip, het
  case-label (nu in de kicker), de histogramstrook, de kolom Answers, de watervalbalkjes, het zettenraster met bijschrift.
  Model: `TT Kicker (text)` nieuw; `TT Chip`, `TT Case (text)`, `TT Mix (text)`, `TT Move Grid (svg)`, `TT Grid Label
  (text)` weg (438 metingen).
- Bevindingenpagina's (560 x 448, F4 384): banner, een kaart met de P1-grafiek en de noot. Detailpagina's (560 x 560):
  banner met de band of het hotel als titel; een kaart met de drie cijfers en die van het merk; een kaart met de
  tweelijnsgrafiek en de slotregel. De maandas van F4 toont een letter per maand (`Date[Month Letter]`, gesorteerd op
  maandnummer): op 496 px draaiden de drieletterige namen schuin.
- `a11y_check.py`: tekst buiten een kaart op een tooltip-pagina wordt tegen de pixels van haar eigen scene getoetst
  (de banner), zoals op de nachtzone van de pagina.

**Geleerd.** Een cardVisual met tekst van 12 pt heeft 64 px nodig voor twee regels en 88 px voor drie; op 56 en 72 px
kapt hij af met een beletselteken. De zettenkaart houdt ruimte voor het grootste pakket (8 zetten: kop + 8 rijen +
totaal = 200 px), dus bij een pakket van 3 zetten blijft de onderste helft leeg; een vaste lay-out kan niet meegroeien.
Desktops knop "Externe wijzigingen toepassen" herschrijft bij elk gebruik de MODELmap (`cultures/en-US.tmdl`): het model
is daarna opnieuw uit `sketch_model.py` gegenereerd; de rapportmap bleef van de generator.

**Controles.** validate_tmdl 0, schema_check 185 bestanden 0 fouten, a11y_check 0; renders in
`project/deliverables/screenshots/2026-11-11-feedbackronde-7/` (P1, P2, de pakket-tooltip op A, C en een wolkpunt, de
F3-chip, de F3-band, het F4-hotel) met `SELF-REVIEW.md`.

**Achtergrond niet meer dubbel (11 november, Bjorns tweede blik).** "De achtergrond lijkt dubbel; haal de overlay weg."
Elke pagina droeg de scene twee keer: als achtergrondbeeld (op ware grootte, dus op elke zoom behalve 100 % niet meer
gelijk aan de pagina) en als paginavullende beeld-visual `z_canvas` erbovenop. De eerste fix haalde de verkeerde weg
(het achtergrondbeeld); Bjorn corrigeerde dat. Definitief: de scene is de PAGINA-ACHTERGROND, geschaald naar de pagina
('Fit'): op de rapportpagina's het nachtcanvas, op elke tooltip-pagina haar eigen scene; de `z_canvas`-visual is overal
weg. Gecontroleerd in Desktop: de achtergrond schaalt mee bij een kleine viewport en op ware grootte. Eén Desktop-eigen
effect: Desktop past het beeld in zijn weergavegebied, 20 px hoger dan de pagina, dus in Desktop staat de scene zo'n
10 tot 15 px hoger dan ontworpen; in de Service en Publish to Web is het gebied de pagina zelf en klopt de uitlijning
precies. `canvas-night-page.jpg` en de `-bg`-tweelingen van de tooltip-scenes zijn verwijderd.

**Screenshots v6.** Op Bjorns verzoek een complete set van het rapport in `project/deliverables/screenshots/screenshots-v6/`:
P1 met de F3-band- en F4-hotel-hover; P2 in Expected, Low en High, de zoom op A/B/C, de pakket-tooltip op A, B, C en een
wolkpunt, de vier F-chips, de staten Considered (B en C) en Build your own (leeg, A nagebouwd, over budget), en terug
naar Recommended.

**Open.** Bjorns to-do's op basis van deze set; Publish to Web, muis- en toetsenbordronde, merge.

## 9. Ronde 8 (11 november: de banner en de titels; de scene pixelvast; meer lucht)

**Wat Bjorn zag.** "De banner en de plaats van titel en ondertitel kloppen niet." Gemeten in Desktop: een pagina-achtergrondbeeld
met schaal Fit wordt in het weergavegebied van de host gepast, en dat van Desktop is hoger dan de pagina, dus daar schuift
de scene omhoog: 14 px op 100 %, 38 px op 60 % zoom (op Bjorns zoom lag de horizon dus boven de KPI-kaart in plaats van
64 px eronder). In de Service is het gebied de pagina zelf; daar klopte het. Bjorns voorstel erbij: "zet de titels hoger
en laat de bovenste visuals over het bannerblauw hangen, dan winnen we canvasruimte voor wat meer witruimte overal".

**De scene pixelvast (`opzet_report.py`, `SCENE_VISUAL = True`).** Een visual staat in paginapixels, in elke host. De
scene is daarom weer de onderste visual (`z_canvas`, z 0, buiten de tabvolgorde), op de rapportpagina's het nachtcanvas,
op elke tooltip-pagina haar eigen scene. De pagina-achtergrond houdt dezelfde scene met Fit: zo toont de strook die Desktop
boven een pagina tekent banner in plaats van effen Night (ronde 6), en omdat Fit met de pagina meeschaalt staat er op geen
enkele zoom een tweede scene (het dubbele beeld van ronde 7 kwam van schaal Normal: ware grootte). Gecontroleerd op ware
grootte en op 45 % (de volledige Desktop-vensters staan in de set als `00_P1_desktop_45pct_desktop.png` en
`09_P2_desktop_45pct_desktop.png`). `SCENE_VISUAL = False` geeft alleen de achtergrond (Service-exact, Desktop verschoven).

**Layout v8 (`opzet-layout.json`).** De kop hoger: headline y 80 (was 88), ondertitel y 128 in een slot van 24 (was 136/32),
de F-chips op P2 y 72 (was 80; 8 px onder de masthead). De eerste kaartrij op y 168 (was 184), de horizon volgt
(`brand_canvas_v3`: eerste rij + 64 = 232), dus de KPI-kaart en de twee P2-kaarten hangen 64 px in de banner, zoals eerder.
De gewonnen 16 px gaan naar lucht: op P1 verticale goten van 24 in plaats van 16 (KPI naar F-kaarten, F-kaarten naar F4),
de F4-kaart 8 px hoger (16 px onder de grafiek), de notities in de F-kaarten eindigen 8 px boven de kaartrand; op P2
schuift de inhoud van scatter en paneel 16 px omhoog, de scatter en de cumulatieve grafiek worden 16 px hoger, in alts en
build krijgt de vergelijkingskaart een goot van 24 en een 8 px hogere grafiek. De voet op y 1032 (slot 48, was 1024/56).
Tooltip-pagina's ongewijzigd (v7).

**Schermafbeeldingen.** `project/deliverables/screenshots/screenshots-v7/`: de v6-set opnieuw op de nieuwe geometrie, met
dezelfde nummering, plus de twee Desktop-vensters op 45 %. Alle 24 beelden in de pixels nagekeken (banner, titels, kaarten,
de drie P2-staten, de scenario's, de zoom, de pakket-tooltip op A/B/C/wolk, de vier chips, de F3/F4-hover, A nagebouwd,
over budget). Desktop-klikcoördinaten voor de set: tabbalk y 204, scenario y 260, zoom y 196, chips y 100, Deneb-rijen
341,4 + 26,8 i, F3-band (1397, 497).

**Poorten.** validate_tmdl 34 bestanden 0 fouten; schema_check 185 bestanden 0 falend; a11y_check 0 fouten, 0 notities.
Het modelmapje opnieuw gegenereerd (Desktop schreef bij elke start zijn `cultures/en-US.tmdl`).

**Open.** Bjorns blik op v7 en zijn to-do's; de commit op `feedback-ronde-4` na zijn ja (ronde 8 staat ongecommit);
Publish to Web, muis- en toetsenbordronde, merge.

## 10. Ronde 9 (11 november: V9, de eindversie)

**Wat Bjorn deed en vroeg.** Hij sloeg het rapport op vanuit Desktop na twee handmatige ingrepen: de `z_canvas`-visual op P1 en P2
opnieuw verwijderd (het pagina-achtergrondbeeld met Fit "werkt prima", de kleine Desktop-verschuiving aanvaard) en de kopregels
hoger gezet. Daarbij vier opdrachten: (1) zijn Desktop-wijzigingen in de generator overnemen; (2) een beoordeling met de
taste-skill, UI/UX Pro en een "hallmark"-skill op AI-tells, plaatsing, witruimte en ontrommelen; (3) oranje tooltip-scenes met
het vervaagde deurkaartje in oranje, de lay-out verder gelijk; (4) elke standaard-tooltip (off brand) uit, of een ontworpen
tooltip waar die iets toevoegt. Op de twee vragen: een nieuw tooltip-page alleen waar het waarde heeft (dat is de jaar-tooltip
op de drie cumulatieve grafieken); de paginanummers in de eyebrow worden een hotelwoordspeling met de paginanaam als tagline.

**Overgenomen uit Desktop (`opzet_report.py`, lay-out v9).** Op de rapportpagina's is het achtergrondbeeld (Fit) de enige drager
van de scene; de tooltip-pagina's houden hun scene ook als onderste visual (`SCENE_VISUAL_TOOLTIP`), exact onder de tooltip-host.
De kop op beide pagina's gelijk en op het 8 px-raster: logo y 16, eyebrow en masthead y 24, headline y 64, ondertitel y 112, de
F-chips op P2 y 56; de eerste kaartrij blijft 168 (horizon 232). `report.json` krijgt `settings.useEnhancedTooltips: false`
(Bjorns Desktop-instelling). De rest van Desktops herschrijving (z- en tab-hernummering, schema 2.14.0, de build-staat met Low,
cultures) is verworpen: de generator schrijft de rec-staat met Expected.

**Beoordeling (design-taste-frontend par. 9, ui-ux-pro-max, dataviz-canon, dashboard-audit, humanizer; er bestaat geen
"hallmark"-skill op deze machine).** Oordeel: goed, een stap van best in class; wat het daar hield waren de teksttells en de
standaard-tooltips. Gedaan: de sectienummers "01/02" weg, de eyebrow is nu "THE WAKE-UP CALL  ·  THE BRAND REVIEW" en "ROOM TO
INVEST  ·  THE INVESTMENT STRATEGY" (woordspeling in eyebrow-blauw, naam in gedempt wit; alternatieven voor P2 als Bjorn wil:
"CHECKING OUT THE OPTIONS", "THE TURNDOWN SERVICE"); de middenpunt gerantsoeneerd tot een per regel (ondertitel P2, band- en
hotelkoppen, merkregels, zwakste scores, kamernachten, KPI-onderregels, de toetsenbord-tweeling van de bereikbalk); de notities
F1, F2, F3 en de aanbevelingsnoot als gewone zinnen in plaats van puntkomma-kettingen en een aforisme; "page-1 finding" wordt
"a finding on The Brand Review page". Plaatsing: de folio-tabel 112 px (geen schuifbalk meer), de leesgids op P2 twee regels
(tegel 112, de scatter 24 px hoger), de chip-tooltip-titel 72 px (F4 brak af), de F4-chip-tooltip als liggende balken met de
volledige hotelnamen (200 px, pagina 424), de kleine F1/F2-grafieken met een categorische jaaras (elk jaar een label). Bewust
gelaten: de drie gelijke F-kaarten (drie bevindingen van gelijk gewicht, F4 breekt het ritme), de samenvallende lijnen in de
cumulatieve grafiek bij Expected, "Totaal" op de watervallen in Desktop (de kijker-locale in Publish to Web), en de lege
build-waterval met zijn $0-balk: een filter kan hem niet blanco maken, Power BI tekent de totaalbalk hoe dan ook.

**Oranje tooltip-scenes (`brand_canvas_v3.tooltip`, palet 'orange').** Band Burnt Tangerine naar donkerder rechts, Tangerine-licht
rechts, hairline en vervaagd deurkaartje (`hanger_mask` op tooltip-schaal, 8 %) in signaaltint en Tangerine; de Oat-pagina met
haar gloed ongewijzigd; kicker in `TT_KICKER` (#FCE6DB), titel wit. Acht scenes (zeven bestaande maten plus `tt-year`). Waiver
vastgelegd in `brand.yaml` (`depth.tooltip_orange`) en `status.yaml`: "Tangerine never draws a brand" vervalt voor de
tooltip-banner alleen. `a11y_check` meet de banner-contrasten: 0 fouten.

**Tooltips per visual.** Power BI's eigen tooltip staat uit op elke visual zonder report-page-tooltip (`finish()` stap 4), met
een uitzondering: de toetsenbord-wolklaag van de scatter houdt haar Tooltips-well als teksttweeling van de pakketkaart. Nieuw:
`tt-year` (560 x 376), een pagina voor de drie cumulatieve grafieken: kicker, "To the end of 2030: where every package stands",
kaart 1 pakket A in Low/Expected/High, kaart 2 A, B, C en "your plan" in de case in beeld ("none yet" zolang niets gekozen is).
Model: 14 maten erbij (452), `TT Year A (Low/Expected/High)`, de teksten, twee alt-teksten.

**Schermafbeeldingen.** `project/deliverables/screenshots/screenshots-v8/`: 28 beelden, de v7-nummering plus de jaar-tooltip op
de drie grafieken (18, 31, 42), de KPI-hover die niets toont (04) en de twee Desktop-vensters op 45 %. Alle beelden in de pixels
nagekeken; het enige Desktop-artefact is het selectiekader rond de scenario-slicer na een klik (bewerkmodus).

**Poorten.** validate_tmdl 34 bestanden 0 fouten; schema_check 193 bestanden 0 falend; a11y_check 0 fouten, 0 notities;
`build_selector_spec.py` ongewijzigd. Het modelmapje opnieuw gegenereerd, `cultures/` verwijderd.

**Tweede blik (11 november, 's avonds).** Bjorn: de band was de donkere oranje geworden, niet de felle; en "geen overlap van de
bovenste visuals op de banner, en de tekst staat te laag" (in Desktop op zijn zoom schuift het Fit-achtergrondbeeld omhoog).
Gedaan: (1) de band in de felle Tangerine (#E86C36 naar #E6662F, lichtoranje gloed, deurkaartje en hairline in de signaaltint);
witte tekst haalt daarop 3,4:1, dus kicker en titel staan in Night (4,7:1 op de donkerste pixel, a11y_check 0); (2) de scene is
weer de onderste visual op elke pagina (`SCENE_VISUAL`), pixelvast in elke host, het achtergrondbeeld vult alleen de strook
boven de pagina (de twee vallen op de pagina samen, dus niets dubbel); (3) de kopregels exact op Bjorns Desktop-posities
(logo 12, eyebrow en masthead 20, headline 60, ondertitel 108, chips 48; `pbir_lib.visual` staat daarvoor een 4 px-raster toe).
Set v8 opnieuw opgenomen (28 beelden). Poorten: schema_check 195 bestanden 0 falend, a11y_check 0.

**Open.** Bjorns ja op V9; de commit op `feedback-ronde-4` (rondes 8 en 9 staan ongecommit); Publish to Web met Deneb en de
tooltips, muis- en toetsenbordronde, merge.

## 11. Ronde 10 (11 november: de tooltips compact en op schaal; de overlay overal weg)

**Wat Bjorn zag en vroeg.** Na de lagenronde en het weghalen van de `z_canvas`-overlay op P1, P2 en vijf tooltip-pagina's:
de overlay moet overal weg; de tooltips zijn te groot, "buitenproportioneel als je hovert in de service"; en een grondige
verbeterronde met de taste-skill, met bronnen die te verifiëren zijn.

**Bronnen (geverifieerd, 11 november).**
- Microsoft Learn, *Extend visuals with report page tooltips* (guidance): "Configure your page tooltip to be small. You can use
  the built-in Tooltip option (320 pixels wide, 240 pixels high) ... Take care not to use a page size that's too large: it can
  obscure the visuals on the source page"; ontwerp op *Actual Size*; "the same theme and style as the report"; niet interactief,
  geen scrollen; altijd verborgen. https://learn.microsoft.com/en-us/power-bi/guidance/report-page-tooltips
- Microsoft Learn, *Visual tooltips in Power BI*: de rapportinstelling "Tooltip size is affected by canvas size" (tooltip
  autoscale): "resizes tooltips based on the canvas size so they look right on different screen sizes".
  https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-visual-tooltips
- Het PBIR-rapportschema 3.3.0 (`settings`): `useScaledTooltips` = "If enabled, the tooltip will scale to match canvas zoom";
  `useEnhancedTooltips` = "Uses better tooltips for the visuals in this report".
  https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/3.3.0/schema.json
- Microsoft Learn, *Create report tooltips*: "Your tooltip can be any size, but keep in mind that tooltips hover over the report
  canvas"; screenreaders lezen een tooltip-pagina niet. https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-tooltips
- Fabric Community (Power BI Updates Blog), *Deep dive into tooltip options in Power BI visuals*: report-page tooltips zijn niet
  interactief; voor interactie een drillthrough-pagina. https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Deep-dive-into-tooltip-options-in-Power-BI-visuals-Generally/ba-p/5255518
- Niet gevonden bij Havens, Kolosko of Data Goblins: een gepubliceerde maatregel voor tooltip-pagina's; de maat hieronder volgt
  Microsofts "klein" en de 320 x 240-referentie.

**Diagnose.** Een tooltip-pagina rendert op ware pixelgrootte terwijl de rapportpagina (1920 breed) in de Service naar het
venster schaalt; zonder autoscale is een tooltip van 560 px op een 1366-venster dus 40 % groter ten opzichte van de pagina
dan in Desktop op 100 %. Daarbij waren de pagina's zelf groot (560 x 448 tot 560 x 560; de F3-band-tooltip werd op P1 aan de
bovenkant afgekapt, render v8 02) en droegen zij de titel in de banner, twee kaarten met eigen marges en veel lucht.

**Gedaan.**
- `report.json` `settings.useScaledTooltips: true` (naast `useEnhancedTooltips: false`): de tooltip schaalt mee met de
  canvas-zoom, in Desktop, de Service en Publish to Web.
- Alle acht tooltip-pagina's 440 px breed (was 560), op het 8 px-raster, `opzet-layout.json`: bevindingen F1-F3 440 x 336
  (was 448), F4 440 x 376 (was 424), de detailpagina's F3-band en F4-hotel 440 x 448 (was 560) in één kaart, het pakket
  440 x 504 (was 536), het jaar 440 x 312 (was 376). Met autoscale is dat op een 1366-venster 313 px breed, bij Microsofts
  320-referentie.
- De huid: de oranje band (ronde 9, Bjorns keuze) draagt alleen nog de kicker (24 px op y 16, horizon op 72); de titel staat
  in Night in de kaart, als eerste regel, zoals de F-kaarten op P1 (kicker, titel, inhoud). Eén kaart per pagina waar het kan
  (detailpagina's), twee op het pakket en het jaar. Inhoud ongewijzigd: dezelfde maten, grafieken en SVG's.
- De SVG's op pakketbreedte: `TTW`/`TTL` 376 (was 496); de zettenlijst met rijhoogte 18 en hoogte 184 (was 20 / 200), de
  kolommen Capex op `TTL - 96` en NPV op `TTL`. `sketch_model.py`, 452 maten, ongewijzigd in aantal.
- `SCENE_VISUAL = False` in `opzet_report.py`: de generator zet de `z_canvas`-overlay nergens meer (Bjorns besluit van vandaag,
  de scene is overal het pagina-achtergrondbeeld met Fit). De scenes zijn op de nieuwe maten opnieuw gegenereerd
  (`brand_canvas_v3.py`, acht `canvas-tt-*.jpg`).
- P1 en P2 niet opnieuw gegenereerd: Bjorns lagen- en tabvolgorde uit Desktop (commit `e63aa76`) blijft staan; de generator
  schrijft die nog niet.

**Poorten.** validate_tmdl 30 bestanden 0 fouten; a11y_check 0 fouten, 0 notities; pbir_detect: de tooltip-pagina's zonder
bevinding (de acht open bevindingen zijn de P1/P2-kopposities op het 4 px-raster en de chip- en tegelkleuren, van vóór deze
ronde); Microsofts validator: dezelfde ene fout als ervoor (de geneste kleur in `categoryLabels.backgroundColor` van de
A/B/C-laag van de scatter; Desktop rendert hem). `schema_check` haalde één schema niet op (404); open.

**Open.** Renders van de acht pagina's in Desktop; Bjorns blik; de hover-set (v9) opnieuw; Publish to Web met autoscale.

**Na de renders (11 november, drie bouwrondes op de pagina's zelf, Desktop met tijdelijke voorbeeldfilters).** Eindmaten
480 px breed (440 liet de titels en jaartallen niet staan): F1 tot F3 480 x 456, F4 480 x 416, F3-band en F4-hotel
480 x 464, pakket 480 x 536, jaar 480 x 320; met autoscale op een 1366-venster 341 px breed. Geleerd en vastgelegd in de
lay-out: een cardVisual-titel van 14 pt heeft 80 px voor twee regels, een noot van 12 pt 136 px voor vier regels (F2), de
drie cijfers met label 56 px. In de kleine grafieken staan de lijnlabels niet meer aan het lijneinde (ze kantelden de
jaartallen en verdrongen elkaar); de legenda staat bovenaan (F1, F3-band, F4-hotel). De kleine F2 toont Goodnight Inn tegen
"the other three brands" als één lijn (`Trend OTA Sisters`, 453 maten): vier merknamen passen op 416 px in geen legenda en
niet aan de lijneinden. De maandas van het hotel blijft de gewone as (een categorische as van twaalf letters kreeg een
schuifbalk). Renders: `project/deliverables/screenshots/2026-11-11-feedbackronde-10/` (de acht pagina's op ware grootte;
de hover-set op P1/P2 is nog niet opnieuw opgenomen). `schema_check` haalt één schema niet meer op (404), was al zo.
