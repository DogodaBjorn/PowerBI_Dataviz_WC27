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
