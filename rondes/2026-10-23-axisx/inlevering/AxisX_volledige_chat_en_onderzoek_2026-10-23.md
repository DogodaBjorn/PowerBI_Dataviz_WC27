# AxisX — Complete chat en onderzoeksdossier

**Datum van het gesprek:** 23 oktober 2026  
**Taal:** Nederlands  
**Doel:** integraal overdraagbaar Markdown-bestand voor Claude/Claude Code  
**Bereik:** de in dit gesprek zichtbare gebruikersberichten en inhoudelijke assistentantwoorden over AxisX, plus de **volledige tekst** van de twee eerder opgeleverde onderzoeksnotities als bijlagen.

> **Leeswijzer:** Dit is een leesbare Markdown-omzetting van het gesprek, geen technische export van ChatGPT. Tabellen, grafieken en interactieve elementen uit de chat zijn geconverteerd naar statische tekst/tabellen. Interne bronreferentiecodes en niet-overdraagbare interactieve afbeeldingen zijn waar mogelijk vervangen door bronlinks in bijlagen A en B. De overige, niet voor gebruikers zichtbare systeem- en toolberichten maken geen deel uit van dit gespreksexportbestand. De twee eerder gegenereerde onderzoeksbestanden zijn hieronder **integraal** opgenomen zodat Claude alle uitwerking en links heeft zonder losse bestanden te hoeven openen.

## Deel I — Gesprek in chronologische volgorde

### Bericht 1 — Gebruiker (23 oktober 2026, 16:00 lokale tijd bij benadering)

> kan jij wat vragen voor de casus van AxisX analyseren en proberen te beantwoorden
>
> 1. Een economisch anker: hoeveel gratis gebruikers van health-apps gaan betalen, met een gelinkte bron.
> 2. Het plafond in getallen: hoeveel vrouwen van 40 tot 55 er in UK, US en Noord-Europa zijn, hoeveel iPhone gebruiken en wat health-advertenties kosten per duizend vertoningen.
> 3. Wat Meta en Google toestaan bij advertenties voor een health-app, qua targeting en optimalisatie-events. Dat kan een kanaal blokkeren.
> 4. Of een vrouw van quiz tot dag 7 te volgen is via één user-ID, en welke grenzen TestFlight daarbij stelt.
> 5. De advertenties van concurrenten in de Ad Library aanvullen met hoe lang ze lopen en welk format ze hebben.

### Bericht 2 — Assistent: analyse van de vijf onderzoeksvragen

#### AxisX — Onderzoek en onderbouwing van de businesscase

Onderzoeksdatum: 23 oktober 2026. Markt: UK, US en Noord-Europa.

De vijf vragen zijn onderzocht voor AxisX, een app die vrouwen rond de perimenopauze ondersteunt via een persoonlijke quiz, symptoomtracking, een zevendaags begeleidingstraject en uiteindelijk een betaald abonnement. Uitgangspunten uit de casusbespreking: de eerste 500 gebruikers, een iOS-bèta via TestFlight, een beoogde D7-retentie van 60% en een mogelijke abonnementsprijs van £100 per jaar. Deze uitgangspunten dienen door de founder bevestigd te worden.

##### 1. Economisch anker — gratis health-appgebruikers naar betaald

- **2,1%:** mediane freemium-naar-betaaldconversie over alle categorieën volgens RevenueCat *State of Subscription Apps 2026*.
- **2,9%:** download-naar-betaald, Health & Fitness.
- **3,5%:** download-naar-betaald, Health & Fitness op iOS.
- **6,9%:** download-naar-trial, Health & Fitness.
- **37,7%:** trial-naar-betaald, Health & Fitness.
- **10,7%:** download-naar-betaald bij hard paywall, alle categorieën.

Deze benchmarks hebben verschillende populaties en meetvensters; download-naar-betaald wordt veelal gemeten tot dag 35 en trialconversie heeft een eigen venster. **Bron:** https://www.revenuecat.com/state-of-subscription-apps

Voor 500 installaties en een mogelijke prijs van £100 per jaar:

| Scenario | Conversie | Verwachte betalende gebruikers | Bruto jaarverkoop, puur theoretisch |
|---|---:|---:|---:|
| Conservatief | 1,0% | 5 | £500 |
| Freemium-benchmark | 2,1% | 10,5 | £1.050 |
| iOS Health & Fitness | 3,5% | 17,5 | £1.750 |
| Ambitieus | 5,0% | 25 | £2.500 |

Deze verwachtingswaarden zijn geen halve werkelijke klanten en geen gerealiseerde omzet. Belastingen, platformkosten, refunds en overige kosten zijn niet meegenomen.

**Conclusie:** hanteer 2,1% als voorlopig freemium-basisscenario, 1% als downside en 3,5–5% als ambitieuze scenario's. Gebruik betaalconversie als commerciële validatiemetriek, niet als primaire KPI voor de eerste zeven dagen. Het D7-doel toetst productgebruik en betrokkenheid, niet betalingsbereidheid.

##### 2. Het marktmaximum — vrouwen 40–55, iPhone-indicatie en CPM

De geografische definitie voor dit onderzoek is UK + US + de vijf Noordse landen Zweden, Denemarken, Noorwegen, Finland en IJsland. Het bereik 40–55 is geschat door vrouwelijke leeftijdsgroepen 40–44, 45–49 en 50–54 samen te nemen plus een vijfde van 55–59. Basis: UN World Population Prospects 2024, projecties voor 2026.

| Land | Vrouwen 40–55 | iOS-aandeel (proxy) | Afgeleide iPhone-indicatie |
|---|---:|---:|---:|
| Verenigde Staten | 33,98 mln | 53,6% | 18,21 mln |
| Verenigd Koninkrijk | 7,18 mln | 52,0% | 3,74 mln |
| Zweden | 1,04 mln | 56,1% | 0,58 mln |
| Denemarken | 0,58 mln | 62,7% | 0,37 mln |
| Noorwegen | 0,57 mln | 58,7% | 0,34 mln |
| Finland | 0,55 mln | 32,5% | 0,18 mln |
| IJsland | 0,04 mln | 60,2% | 0,02 mln |
| **Totaal** | **43,94 mln** | — | **23,43 mln** |

**Methodologische waarschuwing:** OS-verkeersaandeel is niet hetzelfde als iPhone-eigendom bij vrouwen 40–55. Er is niet gecorrigeerd voor smartphonebezit, leeftijdsspecifieke penetratie of belangstelling voor perimenopauze. Dit is een indicatieve demografische TAM en géén rechtstreeks adresseerbare gebruikersmarkt. Bronkaders: https://population.un.org/wpp/ en https://gs.statcounter.com/os-market-share/mobile/ . UK is in de oorspronkelijke analyse deels gebaseerd op Ofcom's 35–54 leeftijdsgegevens. Zie bijlage A voor precieze bronvermelding.

Sectorbenchmark: Triple Whale rapporteerde over augustus 2025–juli 2026 een mediane Meta-CPM van ongeveer **$21,80 voor Health & Wellness**, tegenover circa $15,06 over de gezamenlijke sectoren. Gepubliceerde algemene Meta-e-commerce-CPM's voor juli 2026: circa $16,08 US, $11,81 UK en $7–9 voor verschillende Noordse markten. Deze zijn géén exact AxisX- of perimenopauze-app-tarieven.

| Markt | Algemene Meta-CPM-indicatie | Voorzichtige AxisX-planningsaanname |
|---|---:|---:|
| US | $16 | $22–35 |
| UK | $12 | $15–28 |
| Noordse landen | $7–9 | $12–25 |

De laatste kolom betreft expliciete aannames, geen geobserveerde CPM. Bij $22 CPM kost één miljoen impressies $22.000; dat is niet hetzelfde als een miljoen unieke bereikte personen. Search is doorgaans CPC-gebaseerd en Google App Campaigns optimaliseren onder meer op installaties of in-app-acties: een algemene health-CPM is daar niet zinvol.

**Conclusie:** de demografische vijver is groot genoeg voor 500 bèta-gebruikers. De uitdagingen liggen eerder in relevantie, interesse, acquisitiekosten, vertrouwen en activatie.

##### 3. Meta en Google — advertentiebeleid, targeting en optimalisatie

Een health-advertentie kunnen tonen is niet hetzelfde als de persoonlijke gezondheidsinformatie van gebruikers mogen gebruiken voor targetting, retargeting of algoritmische optimalisatie.

| Onderdeel | Meta | Google |
|---|---|---|
| Advertentie voor perimenopauze-app | In beginsel mogelijk mits beleidsconform | In beginsel mogelijk mits beleidsconform |
| Geografische/demografische targeting | Soms mogelijk, beperkt of uitgebreid door automatisering | Mogelijk binnen het beleid |
| Targeting op individuele gezondheidsklachten | Niet als gevoelig persoonskenmerk gebruiken | Niet toegestaan als gepersonaliseerde health-targeting |
| Custom audiences met gezondheidsinformatie | Niet toegestaan | Niet toegestaan |
| Retargeting na health-quiz | Risicovol/beperkt, geen gevoelige informatie delen | Beperkt voor gevoelige categorieën |
| Optimalisatie op `QuizCompleted` | Afhankelijk van eventinhoud en databronrestricties | Alleen met toegestane niet-gevoelige eventinformatie |
| Optimaliseren op specifieke gezondheidsstatus | Niet toegestaan | Niet toegestaan |
| Optimaliseren op registratie of aankoop | Kan door restricties worden beperkt | Kan onder voorwaarden, zonder ongeoorloofd gebruik van health-data |

**Meta:** Business Tools Terms verbieden het doorgeven van gezondheidsinformatie via events, eventnamen en parameters. Meta kan databronnen plaatsen onder Health and Wellness met `Core Setup`, `Standard Event Restrictions` of `Full Restrictions`. Bij die laatste niveaus kunnen conversie- en advertentieoptimalisatie-events geblokkeerd worden. Dit moet per account en databron in Events Manager worden gecontroleerd; niet iedere health-app heeft automatisch alle restricties. Bronnen:

- https://www.facebook.com/legal/technology_terms
- https://www.facebook.com/business/help/511197658391698

**Google:** gezondheidsinformatie valt onder Sensitive Interest Categories voor gepersonaliseerde advertenties. Customer Match, eigen remarketingsegmenten en vergelijkbare segmenten kunnen voor deze categorie ontoelaatbaar zijn; bepaalde contextuele en demografische vormen van targeting kunnen wel toegestaan zijn. Bron: https://support.google.com/adspolicy/answer/16701855?hl=en

**Google App Campaigns en TestFlight:** reguliere App Campaigns vereisen een app die beschikbaar is in App Store of Play Store. Een alleen via TestFlight toegankelijke iOS-bèta is daardoor niet een geschikte bestemming voor zo'n installatiecampagne. Een Search-ad naar een informatieve landingspagina kan apart worden beoordeeld, mits de campagne en tracking voldoen aan health-beleid.

Advies: ontwerp het eerste 500-gebruikersplan niet rondom performance-optimalisatie op gevoelige quiz- of symptoomgebeurtenissen.

##### 4. Eén user-ID van quiz tot dag 7, en TestFlight

**Ja, technisch mogelijk met een eigen pseudonieme account-ID.** Nodig is een bewuste koppeling tussen de quizdeelnemer en de iOS-app na installatie; een publieke TestFlight-link op zichzelf identificeert de persoon niet.

Voorgestelde first-party flow:

1. **Webquiz:** maak een interne `user_id` aan; bewaar antwoorden in een afgeschermde omgeving.
2. **Account + bèta-uitnodiging:** koppel uitnodiging en account via interne ID, niet via een advertentie-ID.
3. **TestFlight-installatie + login:** dezelfde gebruiker logt in en wordt aan dezelfde interne ID gekoppeld.
4. **First-party events:** `QuizCompleted`, `AccountCreated`, `AppActivated`, `Day1Active`, `Day3Active`, `Day7Active`.

| TestFlight-onderdeel | Grens of aandachtspunt |
|---|---|
| Externe testers per app | 10.000 |
| Interne testers | 100 |
| Geldigheid van een build | 90 dagen |
| Review | Eerste externe build moet door Apple worden goedgekeurd |
| Uitnodigen | E-mail of openbare link |
| Openbare link | Naam/e-mail niet vanzelf zichtbaar voor ontwikkelaar |
| Beta-in-app-aankopen | Testaankopen zijn gratis; niet te gebruiken als gerealiseerde abonnementsomzet |

Bronnen: https://developer.apple.com/testflight/ ; https://developer.apple.com/help/app-store-connect/test-a-beta-version/ .

Gezondheidsgegevens verdienen extra bescherming, zijn onder AVG/UK GDPR bijzonder gevoelig, en moeten niet stilzwijgend aan advertentieplatformen worden doorgegeven. Intern first-party meten ≠ advertentieplatformen toegang geven. Apple App Tracking Transparency kan aanvullend gelden voor cross-company advertisingtracking.

Advies: meet D7-retentie via eigen account- en eventdata; scheid de privacyvriendelijke acquisitierapportage van gevoelige gezondheidsinformatie en van het eigen productgebruik.

##### 5. Concurrenten — Meta Ad Library looptijd en formaten

De oorspronkelijke set bestaat uit **thePause, Play Health, Waves Women en balance**. Niet alle vier konden worden onderbouwd met individuele, verifieerbare Meta Ad Library-records met startdatum, looptijd en format. Als aanvullende, aantoonbaar actieve marktvoorbeelden zijn **Midi Health** en **Alloy** onderzocht.

| Merk | Format in onderzochte steekproef | Mediane advertentielooptijd | Peildatum |
|---|---|---:|---|
| Midi Health | 97% statisch, 3% video | 48 dagen | 5 okt. 2026 |
| Alloy | 80% statisch, 17% video, 3% carrousel | 9 dagen | 5 okt. 2026 |

Midi steekproef 31 creatives; Alloy 30. Niet representatief voor hun complete advertentiearchieven. Een andere ad-monitor op 23 oktober 2026 gaf voor Alloy een bredere actieve collectie met circa 158 ads, 79% statisch/21% video, en een langstlopende actieve ad van circa zes maanden. Dit is een andere steekproef.

Genoemde individuele voorbeelden uit de advertentiesteekproeven:

- Midi Health — *Get answers at Midi*: statisch, 34 dagen zichtbaar in de onderzochte snapshot.
- Midi Health — *Relief Starts With Being Heard*: video, 49 dagen.
- Alloy — *Estrogen-Powered Skincare*: statisch, minder dan één dag bij de peiling.

Voor de oorspronkelijke concurrenten:

- **thePause / Harmoni:** bestaand product met AI-assistent, spraakregistratie en wearables; op de officiële site werden $89,99/jaar voor Premium en een proefperiode van zeven dagen vermeld. Geen independently verified Meta-format/looptijdrecord in dit onderzoek.
- **Waves Women:** programma's van vier weken, dagelijkse check-ins en genoemde prijs $50/jaar of $8/maand; geen voldoende verifieerbare Meta-steekproef.
- **Play Health:** officiële website meldde dat app en diensten zijn gesloten; niet als actieve acquisitieconcurrent positioneren.
- **balance / Dr. Louise Newson:** onvoldoende exact geïdentificeerde actieve adrecords; veel niet-gerelateerde apps en bedrijven delen deze naam.

Meta Ad Library: https://www.facebook.com/ads/library/ . Advertentieloopduur is hooguit een signaal van langere inzet; zonder CPA/ROAS-data is het **geen bewijs van creatief rendement**.

##### Overkoepelende conclusie uit deze eerste analyse

| Thema | Werkconclusie | Implicatie |
|---|---|---|
| Freemium → betaald | 2,1% mediaan in brede benchmark | Conversie conservatief modelleren |
| Doelgroep | 43,94 mln vrouwen; 23,43 mln iOS-proxy | Voldoende brede demografische TAM, niet de adresseerbare markt |
| Advertentiebeleid | Health-audiences en -events beperkt | Geen funnel bouwen die health-retargeting vereist |
| Quiz → D7 | Ja via eigen gebruikers-ID en login | First-party cohorts vanaf D0 |
| Concurrenten | Statische formaten dominant in geselecteerde steekproeven | Static naast video testen; looptijd niet verwarren met rendement |

De eerste 500 AxisX-gebruikers zijn beter als productvalidatiecohort te behandelen dan als reguliere paid-acquisition-funnel. Onderscheid tussen D7-productbetrokkenheid en daadwerkelijke betalingsbereidheid; de betaalvalidatie komt apart.

**Uitgebreide, oorspronkelijke onderzoeksnotitie inclusief bronlinks:** volledig opgenomen als *Bijlage A* hieronder.

---

### Bericht 3 — Gebruiker (23 oktober 2026)

> wederom .. output van deze analyses in md file meegeven kan dat? dan gaat dat ook naar claude

### Bericht 4 — Assistent: oplevering van eerste Markdown-notitie

Het volledige onderzoek is opgeleverd als één Markdown-bestand, klaar voor Claude Code:

**`AxisX_marktonderzoek_businesscase_2026-10-23.md`** — vijf analyses, bronlinks, cijfers, aannames en aanbevelingen. Onzekerheden zijn expliciet vastgelegd zodat Claude geverifieerde benchmarks van berekende marktinschattingen en strategische aannames kan onderscheiden. Het document is zelfstandig leesbaar en bevat onderaan een overdrachtsinstructie voor Claude.

De volledige inhoud van dit bestand staat in **Bijlage A** hieronder.

---

### Bericht 5 — Gebruiker (23 oktober 2026)

> Oké het laatste stukje waar ik graag , heel graag van jou input voor wil is het uitgebreid nadenken en op research baseren van goede vragen die we mee kunnen nemen op de landing page en de quiz om kaf van koren te scheiden. Baseer je hier echto p de target audience die de founder heeft.
>
> Dus niet het vinden van mensen die helpen activeren maar de mensen die vanuit de activatie komen kijken.. hoe gaan we daar de juiste mensen it vinden zodat we zeker zijn dat we genoeg data halen uit 500 aanmeldingen én minstens 300 plakkers hebben?

### Bericht 6 — Assistent: selectiequiz, landingspagina en D7-onderzoek

#### AxisX — De juiste 500 selecteren voor 300 actieve gebruikers

De kern is dat we **niet** moeten selecteren op wie de meeste perimenopauzeklachten heeft, maar op wie de problematiek herkent, actief een oplossing zoekt, waarde ziet in de werkwijze van AxisX en deze werkwijze daadwerkelijk in de komende week kan uitproberen.

Dat sluit aan op de eerdere beschrijving van de founderdoelgroep: vrouwen vanaf ongeveer 39 jaar die perimenopauze herkennen of vermoeden en actief ondersteuning zoeken. Niet vrouwen die eerst nog overtuigd moeten worden dat perimenopauze relevant is.

Twee doelen onderscheiden:

- **500 geschikte deelnemers:** vrouwen van wie betekenisvolle product-, behoefte- en gedragsdata worden verzameld.
- **300 blijvende gebruikers:** ≥60% van die 500 keert betekenisvol terug op dag 7.

Een quiz kan de waarschijnlijkheid van echte betrokkenheid helpen verhogen, maar niet garanderen. Alleen de allerenthousiastste deelnemers toelaten maakt de retentiecijfers selectief en minder generaliseerbaar.

##### Onderzoek dat het ontwerp onderbouwt

1. Persoonlijke relevantie, ervaren nut, personalisatie, zelfmonitoring, doelen en gebruiksgemak hangen samen met gebruik van gezondheidsapps. Review van 41 studies: https://pubmed.ncbi.nlm.nih.gov/32348255/ .
2. Onderzoek naar menopauze-apps geeft behoeften aan herkenning, begrijpelijke tracking, personalisatie, vertrouwen en ondersteuning bij gesprekken met zorgprofessionals. Zie bijlage B voor literatuurverwijzingen.
3. Een formele diagnose hoeft geen inclusie-eis te zijn: NICE en Europese endocrinologierichtlijnen behandelen klinische herkenning van perimenopauze. https://www.nice.org.uk/guidance/ng23/chapter/Recommendations .
4. Motivatie zeggen is geen daadwerkelijke gedragsmaat. Daarom vragen naar recent zoekgedrag, wat men al heeft geprobeerd en of er praktisch tijd is voor de bèta. mHealth-engagement en uitval: https://www.jmir.org/2022/4/e35120/ .

Voorgesteld proces: korte landing, kwalificatiequiz en afzonderlijke persoonlijke baseline na toelating. Gedetailleerde gevoelige symptoominformatie wordt zo niet onnodig vroeg opgevraagd.

##### De zes cruciale selectievraagthema's

| Vraag | Waarom belangrijk? |
|---|---|
| **Waarom ben je juist nu op zoek naar ondersteuning?** | Actuele hulpvraag versus algemene nieuwsgierigheid. |
| **Wat heb je de afgelopen 30 dagen al gedaan om antwoorden te vinden?** | Aantoonbare activiteit versus uitgesproken interesse. |
| **Wat wil je over zeven dagen beter begrijpen?** | Of AxisX binnen de eerste week waarde kan bieden. |
| **Hoe probeer je dit momenteel zelf bij te houden of te begrijpen?** | Bestaande alternatieven, frustraties en gewoonten. |
| **Hoeveel tijd kun je deze week realistisch vrijmaken?** | Praktische beschikbaarheid zonder kunstmatige daily-use-verplichting. |
| **Wat zou ervoor zorgen dat je na enkele dagen afhaakt?** | Product-, onboarding- en verwachtingsrisico. |

Voorgesteld als **onderzoeksverdeling**, niet als bewezen optimaal beleid: ongeveer **70% direct passend, actief hulpzoekend** en **30% relevante maar minder voorspelbare deelnemers**. Zo kan AxisX zowel kansrijke gebruikers aantrekken als voorkomen dat alleen superfans gemeten worden.

##### Rekensom: 500 registraties ≠ 300 actieve gebruikers

- Beoogd: 500 daadwerkelijke geactiveerde gebruikers × 60% D7-retentie = 300 D7-actieven.
- Voorbeeld met afhakers onderweg: 500 registraties × 90% installatie × 90% activatie × 75% D7-retentie ≈ **304 D7-actieven**.

Een doel van 500 registraties zonder onderscheid in installatie en activatie is dus niet voldoende. Meet registratie, installatie, betekenisvolle activatie en D7-terugkeer als afzonderlijke funnelstappen.

##### Ontwerpconclusie

De intake moet de founderdoelgroep herkennen, relevante behoeften zichtbaar maken en voorspellen wie waarschijnlijk binnen zeven dagen waarde ervaart. Dit mag **geen medische screening, diagnose of zelfbevestigend scoremodel** worden. De definitie van D7-retentie, het instapcohort en de MVP-functionaliteit moeten expliciet worden vastgelegd. Na de eerste 50–100 deelnemers kunnen afzonderlijke correlaties tussen intakeantwoorden en echt gebruik worden geanalyseerd, zonder achteraf de oorspronkelijke cohortdefinitie te herschrijven.

**Belangrijkste boodschap aan Claude:** ontwerp geen quiz die de meest enthousiaste 500 vrouwen selecteert. Ontwerp een intake die de juiste doelgroep identificeert, hun concrete behoefte zichtbaar maakt en vervolgens bewijs verzamelt dat AxisX daadwerkelijk waarde levert. Alleen dan zijn 300 blijvende gebruikers een geloofwaardig productsignaal; retentie alléén bewijst nog niet volledige product-market fit.

De uitgebreide notitie bevat direct inzetbare Engelstalige landingspaginacopy, drie pre-screenvragen, negen quizvragen met opties, beslisregels, cohortverdeling, privacy, eventmodel, validatieplan en bronnen. De volledige tekst staat in **Bijlage B**.

---

### Bericht 7 — Assistent: tweede Markdown-bestand opgeleverd

**`AxisX_selectiequiz_landingspagina_D7_retentie_2026-10-23.md`** — onderzoek en ontwerp voor landingspagina, quiz, selectie en D7-meting; oorspronkelijke oplevering was een Markdown-bestand van circa 4.254 woorden.

De volledige inhoud staat als **Bijlage B** hieronder.

---

### Bericht 8 — Gebruiker (23 oktober 2026)

> kan jij deze hele chat als md aanleveren?

### Bericht 9 — Assistent: huidige oplevering

Dit document bundelt het zichtbare AxisX-gesprek en beide volledige onderzoeksnotities in één Markdown-bestand dat aan Claude Code kan worden gegeven.

---

## Deel II — Volledige onderzoeksdocumenten uit het gesprek

De twee bijlagen zijn geen nieuwe antwoorden: het zijn ongewijzigd overgenomen bestanden die in eerdere stappen van dit gesprek voor Claude zijn gemaakt. Bij een verschil in detail of formulering is het uitgebreide document meer informatief dan de compacte conversatieweergave erboven; definitieve keuzes vragen steeds controle met de founderbrief en de originele bronnen.


---

# Bijlage A — Volledige notitie: marktonderzoek en businesscase

# AxisX — Marktonderzoek en onderbouwing businesscase

**Datum:** 23 oktober 2026  
**Taal:** Nederlands  
**Bestemming:** overdracht aan Claude (AI Marketing Kombat / AxisX)  
**Status:** onderzoeksnotitie, niet de definitieve case-inzending

## Doel en leeswijzer

Dit bestand bevat de uitkomsten van vijf onderzoeksvragen over de AxisX-casus:

1. Hoeveel gebruikers van gratis health-apps worden betalend?
2. Hoe groot is de doelgroep vrouwen van 40–55 in UK, US en Noord-Europa; hoeveel daarvan zijn vermoedelijk via iPhone bereikbaar; en welke advertentie-CPM's zijn aannemelijk?
3. Welke targeting, meting en optimalisatie laten Meta en Google bij health-apps toe?
4. Is een individuele quizdeelnemer betrouwbaar te volgen tot dag 7, ook via TestFlight?
5. Welke formaten en looptijden zien we bij concurrentieadvertenties?

**Belangrijk bij hergebruik:**
- `BRON / GECONTROLEERD`: gepubliceerde benchmark of officieel platformbeleid, met link.
- `BEREKEND / INDICATIEF`: zelf berekend, afhankelijk van definities en invoerwaarden; geen officieel waargenomen marktaantal.
- `AANNAME / SCENARIO`: alleen bedoeld voor financiële of mediaplanning.
- `TE VALIDEREN`: nog niet afgedekt met direct bewijs of account-specifieke platformcontrole.
- De cijfers uit verschillende datasets mogen niet worden opgeteld of vermenigvuldigd alsof het dezelfde meetpopulatie of hetzelfde conversievenster betreft.

**Werkhypothesen AxisX (afkomstig uit de voorgaande casusbespreking, niet extern geverifieerd):** iOS-bèta via TestFlight; eerste cohort van 500 gebruikers; quiz gevolgd door een app-/begeleidingsprogramma; D7-retentie-doel van 60%; mogelijke jaarprijs £100; doelgroep vrouwen van ongeveer 40–55 jaar. Controleer deze uitgangspunten tegen de laatste AxisX-casebrief.

---

## 1. Economisch anker — gratis naar betaald

### Verifieerbare benchmarks

Bron: **RevenueCat — State of Subscription Apps 2026** (geaggregeerde benchmarks van abonnementsapps; referentiegegevens grotendeels 2025).

| Maatstaf | Benchmark | Populatie en interpretatie |
|---|---:|---|
| Freemium download-to-paid bij dag 35 | **2,1%** | Mediaan alle categorieën, freemium-model |
| Hard paywall download-to-paid bij dag 35 | **10,7%** | Mediaan alle categorieën, ander toegangsmodel; niet direct vergelijkbaar zonder modelkeuze |
| Health & Fitness download-to-paid bij dag 35 | **2,9%** | Mediaan categorie, gecombineerde platformen |
| Health & Fitness op iOS download-to-paid bij dag 35 | **3,5%** | Mediaan iOS-categorie |
| Health & Fitness download-to-trial bij dag 30 | **6,9%** | Conversie naar proefabonnement, andere teller en periode |
| Health & Fitness trial-to-paid | **37,7%** | Mediaan onder gestarte trials; niet vermenigvuldigen met anders gedefinieerde cohortcijfers zonder controle |

**Directe bron:** https://www.revenuecat.com/state-of-subscription-apps

**Interpretatie:** de 2,1% is het meest conservatieve expliciete freemium-anker voor de eerste AxisX-businesscase. De 3,5% geeft een gunstiger **iOS Health & Fitness**-referentie, maar beschrijft niet noodzakelijk dezelfde freemium-subgroep. Het verschil tussen freemium, hard paywall en trial is methodologisch belangrijk.

### Scenario voor 500 installaties

Formule: `verwachte betalers = installaties × conversiepercentage`; `theoretische bruto jaarverkoop = verwachte betalers × £100`.

| Scenario | Conversie | Verwachte betalers van 500 | Theoretische bruto jaarverkoop |
|---|---:|---:|---:|
| Downside (aanname) | 1,0% | 5,0 | £500 |
| Freemium-median (bronbenchmark) | 2,1% | 10,5 | £1.050 |
| iOS H&F-vergelijking (bronbenchmark) | 3,5% | 17,5 | £1.750 |
| Upside (aanname) | 5,0% | 25,0 | £2.500 |

De aantallen 10,5 en 17,5 zijn **verwachtingswaarden**, niet halve klanten. De bedragen veronderstellen dat elke betalende gebruiker het volle jaarabonnement van £100 koopt; ze zijn **geen gerealiseerde omzet, netto-omzet of LTV**. Belasting, Apple-commissie, prijsverdeling, refunds, marketingkosten, churn en timing ontbreken. Een jaarlijkse prijs van £100 kan aanzienlijk hoger zijn dan het gebruikelijke jaarlijkse prijspunt van veel Health & Fitness-apps; neem dus geen categorieconversie zonder prijsgevoeligheid over.

**Conclusie voor de case:** laat de eerste bèta primair waardepropositie, activatie en retentie bewijzen; positioneer betaalconversie als afzonderlijke commerciële validatie ná of buiten TestFlight. Gebruik 1%, 2,1% en 3,5–5% als expliciete scenario's, niet als belofte.

---

## 2. Plafond in getallen — doelgroep, iOS en advertentiekosten

### Definitie

`Noord-Europa` = **Zweden, Denemarken, Noorwegen, Finland en IJsland**; het Verenigd Koninkrijk wordt apart meegeteld. Een andere geografische afbakening verandert de totaalcijfers.

Leeftijd `40 t/m 55 jaar (inclusief)` is in de eerdere berekening benaderd als:

`vrouwen 40–44 + vrouwen 45–49 + vrouwen 50–54 + 20% van vrouwen 55–59`.

Bronkader: UN World Population Prospects 2024, projecties voor 2026. De onderstaande landuitkomsten zijn overgenomen uit de eerdere analyse en **dienen als indicatieve cijfers**: voor een officieel te publiceren TAM moet Claude de exacte leeftijds-/seksegegevens opnieuw uit UN WPP downloaden en de berekening reproduceren.

### Demografische TAM en iPhone-proxy

| Markt | Vrouwen 40–55 (indicatie) | Gebruikte iOS-/iPhone-proxy | Vermenigvuldigde proxy (indicatie) |
|---|---:|---:|---:|
| Verenigde Staten | 33,98 mln | 53,6% | 18,21 mln |
| Verenigd Koninkrijk | 7,18 mln | 52,0% | 3,74 mln |
| Zweden | 1,04 mln | 56,1% | 0,58 mln |
| Denemarken | 0,58 mln | 62,7% | 0,37 mln |
| Noorwegen | 0,57 mln | 58,7% | 0,34 mln |
| Finland | 0,55 mln | 32,5% | 0,18 mln |
| IJsland | 0,04 mln | 60,2% | 0,02 mln |
| **Totaal** | **ca. 43,94 mln** | n.v.t. | **ca. 23,43 mln** |

**Wat deze getallen niet zeggen:**

- De iPhone-kolom is **geen** gemeten aantal unieke iPhone-gebruikende vrouwen van 40–55 jaar. Statcounter meet grotendeels OS-verkeersaandelen, niet het bezit of aantal personen. De UK-bron is een survey onder smartphonegebruikers van 35–54 jaar, eveneens niet exact de AxisX-doelgroep.
- Niet gecorrigeerd voor smartphonepenetratie, type device, gender/age-interacties, geografische verschillen binnen landen, dubbele apparaten, interesse in menopauze, klachtprevalentie, motivatie of betaalbereidheid.
- Het aandeel 55-jarigen is lineair benaderd (1/5 van vijfjaarscohort).
- De precieze percentages variëren per meetmaand en platformfilter. **Gebruik deze 23,4 miljoen niet als SAM of direct advertentiebereik.**

**Bronnen en verificatielinks:**

- UN World Population Prospects 2024: https://population.un.org/wpp/
- UN DemoData (leeftijd/geslacht, export): https://population.un.org/demodata/home
- Statcounter mobiele OS-aandelen, VS: https://gs.statcounter.com/os-market-share/mobile/united-states-of-america
- Statcounter mobiele OS-aandelen, VK: https://gs.statcounter.com/os-market-share/mobile/united-kingdom
- Statcounter, Zweden: https://gs.statcounter.com/os-market-share/mobile/sweden
- Statcounter, Denemarken: https://gs.statcounter.com/os-market-share/mobile/denmark
- Statcounter, Noorwegen: https://gs.statcounter.com/os-market-share/mobile/norway
- Statcounter, Finland: https://gs.statcounter.com/os-market-share/mobile/finland
- Statcounter, IJsland: https://gs.statcounter.com/os-market-share/mobile/iceland
- Ofcom, *Online Nation 2025* (figure 15: bij Britse smartphonebezitters van 35–54 is 52% iPhone; niet vrouwen 40–55): https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-research/online-nation/2025/online-nations-report-2025.pdf

### Media-inkoop: CPM

**BRON / GECONTROLEERD:** Triple Whale rapporteert voor Meta **Health & Wellness een mediane CPM van $21,80**, periode augustus 2025–juli 2026. Dit is een sectorbenchmark, niet een gemeten CPM voor vrouwen 40–55 met een perimenopauze-app.

Bron: https://www.triplewhale.com/blog/facebook-ads-benchmarks

Algemene, minder specifieke Meta-landindicaties genoemd in de eerdere analyse: US circa $16; UK circa $12; verschillende Noordse markten circa $7–9. Deze landcijfers zijn **niet opnieuw onafhankelijk geverifieerd met dezelfde bronmethodiek** en mogen niet als health-specifieke benchmarks worden geciteerd.

**AANNAME / te toetsen bij campagne-inzet:**

| Markt | Conservatieve planningsbandbreedte Meta CPM | Status |
|---|---:|---|
| US | $22–35 | aanname, geen gemeten AxisX-CPM |
| UK | $15–28 | aanname |
| Noordse landen | $12–25 | aanname |

`Kosten = impressies / 1000 × CPM`.

Voorbeeld: bij $22 CPM kosten 1 miljoen **impressies** ongeveer $22.000. Dat zijn geen 1 miljoen unieke bereikte vrouwen, vanwege frequentie. Google Search draait doorgaans op CPC; Google App Campaigns op installaties/in-app-acties en pas na beschikbaarheid van de app in de appstore (zie §3). Een uniforme 'Google health-CPM' is daarom niet betekenisvol.

**Beslissing:** ruim demografisch plafond; de beperking voor de eerste 500 gebruikers zit vooral in vertrouwen, relevantie, activering en kostenefficiënte distributie. Voor een investeerbare forecast: modelleer apart `TAM → relevantie → bereikbaar publiek → bezoek → quiz → registratie → activatie → D7 → betaald` met eigen aannames en gevoeligheidsanalyse.

---

## 3. Meta- en Google-beleid: targeting en optimalisatie

**Kern:** een advertentie mogen tonen betekent **niet** dat alle gebeurtenissen in de health-funnel naar Meta/Google mogen worden doorgestuurd of gebruikt voor retargeting en algoritmische optimalisatie.

### Google Ads — relatief helder beleid

Health is een **Sensitive Interest Category** in het personalisatiebeleid. De volgende **advertiser-curated audiences** zijn bij gevoelige categorieën niet toegestaan: Customer Match, eigen datasegmenten / remarketing, audience expansion en lookalike segments. Bepaalde door Google vooraf gedefinieerde doelgroepen, demografie (met uitzonderingen), geografie en toegestane contextuele methoden kunnen wel.

- Officiële policy: https://support.google.com/adspolicy/answer/16701855?hl=en
- Algemeen beleid restricted targeting: https://support.google.com/adspolicy/answer/143465

Voorbeeld:
- **Veiliger:** brede/contextuele campagne met een neutrale propositie over ondersteuning bij perimenopauze.
- **Niet als uitgangspunt:** remarketing van vrouwen met specifieke aangegeven klachten of audience-upload op basis van symptoomquiz.

**Extra kanaalblokkade:** Google vereist voor normale **App Campaigns** een app die te downloaden is in Apple App Store of Google Play. Alleen TestFlight voldoet niet. Een reguliere Search-campagne die naar een openbare informatie-/quizlandingspagina leidt kan mogelijk wel, mits tekst, landingspagina, data en targeting aan beleid voldoen.

- Google App Campaigns requirements: https://support.google.com/google-ads/answer/6247380?hl=en

### Meta — ad approval versus datadeling

Meta verbiedt het via de Business Tools doorgeven van informatie die gevoelige gezondheidsinformatie bevat of daaruit kan worden afgeleid. Bij websites/apps in health & wellness kunnen afhankelijk van de classificatie datadeling en bepaalde standaardevents beperkt worden. In de eerdere analyse werden restrictieklassen beschreven (Core Setup, Standard Event Restrictions, Full Restrictions); **controleer de huidige exacte restrictie en toegestane events in AxisX Events Manager vóór kanaalkeuze.** Niet iedere health-app krijgt automatisch een volledige blokkade.

- Meta Business Tools Terms: https://www.facebook.com/legal/technology_terms
- Meta help, data-sharing restrictions: https://www.facebook.com/business/help/511197658391698

### Kanalenmatrix voor besluitvorming

| Gebruik | Meta | Google | AxisX-advies |
|---|---|---|---|
| Informatieve campagne op basis van toegestane brede targeting | In beginsel mogelijk | In beginsel mogelijk | Eerst advertentie-/beleidstoets |
| Demografie/geografie | Mogelijk, onder actuele delivery-/audience-instellingen | Mogelijk, met uitzonderingen | Niet gelijkstellen aan exact bereik |
| Segment gebaseerd op ingevulde health-quiz | Niet gebruiken | Niet gebruiken | Geen symptom-based advertentieaudiences |
| `QuizCompleted` / `Day7Active` als advertentie-event | Kan beperkt of verboden zijn door gegevensinhoud en databronrestricties | Niet zonder passende policy-/privacytoets | First-party intern vastleggen; niet standaard doorsturen |
| Purchase-/registratie-optimalisatie | Afhankelijk van Meta-databronrestricties | Afhankelijk van beleidskader / toegestane data | Per event feitelijk toetsen, geen automatisme |
| App-installs naar TestFlight via App Campaigns | Eigen test-/linkstrategie vereist | **Geen normale App Campaigns zolang app niet live in store staat** | Begin niet met Google App Campaigns |

**Waarschuwing:** gezondheidstargeting, AVG/GDPR, Apple ATT, cookie-/SDK-consent en advertentieverificatie zijn **verschillende** eisen. Een pseudoniem of gehashte identifier maakt gevoelige informatie niet automatisch advertentiegeschikt. Onderzoek ook eventuele healthcare-/medical claims in teksten en US/UK-specifieke gezondheidsadvertentieregels.

**Aanbeveling:** het acquisitieplan voor het bèta-cohort mag niet afhankelijk zijn van het terugsturen van gezondheids- of symptoomgebaseerde events naar Meta/Google. Gebruik eigen first-party cohortmetrics en publieke/brede content, community's, partnerships en andere privacyconforme kanalen.

---

## 4. Eén user-ID van quiz tot D7, inclusief TestFlight

### Kort antwoord

**Ja, technisch kan dit**, mits AxisX een **eigen, pseudonieme en persistent account-ID** uitgeeft vóór of tijdens de quiz en diezelfde identiteit koppelt wanneer de tester voor het eerst inlogt in de iOS-app. TestFlight maakt die accountkoppeling niet vanzelf.

### Aanbevolen first-party architectuur

```text
[Website / quiz]
   → interne user_id (random UUID; niet e-mail of advertentie-ID)
   → consentstatus en quizdata in afzonderlijke, beveiligde opslag
   → uitnodiging / onboarding met eenmalige token
   → TestFlight-installatie
   → app-login of token redemption
   → koppeling aan dezelfde user_id
   → eventstore: QuizCompleted, AccountCreated, AppActivated,
                 Day1Active, Day3Active, Day7Active
   → cohortanalyse in eigen BI / backend
```

**Minimale eventschema (concept, geen gevoelige parameters):**

| Veld | Doel |
|---|---|
| `event_id` | unieke deduplicatiesleutel |
| `user_id` | first-party pseudonieme user identifier |
| `event_name` | gestandaardiseerde gebeurtenis |
| `occurred_at_utc` | tijdstip in UTC |
| `cohort_start_at_utc` | start van cohort, bv. appactivatie |
| `app_version` / `platform` | technische segmentatie |
| `consent_version` | relevante toestemmingsversie / audit trail |
| `source_category` | privacyvriendelijke herkomstgroepering, zonder health-targeting-data |

**Niet opnemen in generieke marketingevents:** individuele quizantwoorden, symptoomlabels, diagnosevermoedens, e-mailadressen, echte namen en andere gezondheidsinformatie. Leg medisch/gezondheidsinhoudelijke gegevens apart vast met passende rechtsgrond, privacyverklaring en autorisaties.

### Definitie D7-retentie (expliciet kiezen)

Voorstel: `D7 retained = gebruiker met minstens één geldige actieve gebeurtenis op kalenderdag 7 na de gekozen cohortstart`, waarbij kalenderdag en tijdzone consistent zijn. Voor een 24-uursvenster of 'return on or after day 7' ontstaat een **andere** metric; zet dit vóór meten vast.

Voorbeeld:

`D7-retentie = aantal geactiveerde gebruikers met qualifying D7-event / aantal geactiveerde gebruikers in een volledig uitgemeten cohort`.

Rapporteer apart `quiz → uitnodiging`, `uitnodiging → installatie`, `installatie → activatie`, `D1`, `D3`, `D7`. Niet alle 500 uitgenodigde vrouwen zullen activatie bereiken; wees expliciet over de noemer.

### TestFlight-grenzen

| Kenmerk | Beperking / eigenschap |
|---|---|
| Interne testers | maximaal **100** teamleden met passende App Store Connect-rollen |
| Externe testers | maximaal **10.000** |
| Eerste externe build | vereist goedkeuring via TestFlight App Review |
| Uitnodigen | e-mail of openbare link |
| Looptijd build | **90 dagen** geldig; daarna nieuwe build nodig |
| In-app purchases | sandbox: transacties gratis voor testers; geen werkelijke betaalomzet |
| Identiteit bij publieke link | TestFlight levert geen betrouwbare quiz→persoonskoppeling; eigen login nodig |

- Officieel Apple TestFlight: https://developer.apple.com/testflight/
- Apple over sandbox aankopen: https://developer.apple.com/in-app-purchase/
- Apple over 90 dagen: https://developer.apple.com/videos/play/tech-talks/110343/

**Juridische/privacygrenzen:** symptomtracking betreft doorgaans bijzondere gezondheidsgegevens onder EU/UK GDPR. Controleer een passende grondslag én uitzondering voor bijzondere persoonsgegevens, doelbinding, transparantie, dataminimalisatie, bewaartermijn, beveiliging, eventuele DPIA en toestemming voor afzonderlijke doeleinden. Ook Apple's App Tracking Transparency (ATT) kan gelden als gegevens worden gebruikt om een persoon over apps/sites van andere bedrijven te volgen voor advertenties.

**Besluit:** gebruik een first-party `user_id` en eigen eventstore als source of truth. Meet D7 primair op cohortniveau. TestFlight is geschikt om productgedrag en interesse in een betaalpropositie te observeren, niet om echte App Store-betaalconversie te claimen.

---

## 5. Concurrenten: Ad Library-formaten en looptijd

### Datakwaliteit

Voor de oorspronkelijk besproken merken **thePause, Play Health, Waves Women en balance** waren niet voor alle vier individuele, verifieerbare Meta Ad Library-records met startdatum én format beschikbaar. Het zou onjuist zijn om ontbrekende records te verzinnen.

Wel beschikbaar zijn **derdepartij-snapshots** van twee aanvullende merken in dezelfde gezondheid-/menopauzemarkt: **Midi Health** en **Alloy**. Deze zijn nuttig voor creatieve referenties, maar ze zijn geen bewijs van bereik, CPA, ROAS of winstgevendheid. Een langdurig live advertentie kan om tal van redenen live zijn.

### Gevonden creatieve steekproeven (peildatum 5 oktober 2026)

| Merk | Steekproef | Formaten | Mediane looptijd | Voorbeelden | Bron |
|---|---:|---|---:|---|---|
| Midi Health | 31 advertenties | 97% single image; 3% video | **48 dagen** | “Get answers at Midi” (statisch, 34 dagen); “Relief Starts With Being Heard” (video, 49 dagen) | https://www.sprites.ai/midi-health-ads |
| Alloy | 30 advertenties | 80% single image; 17% video; 3% carrousel | **9 dagen** | “Estrogen-Powered Skincare” (statisch, <1 dag); “Treatment, Without The Pharmacy” (statisch, 9 dagen) | https://www.sprites.ai/alloy-ads |

Dit zijn **momentopnamen / selecties**, geen complete formatdistributies van alle advertenties over de tijd. De provider toont bredere libraries (meer advertenties dan de uitgewerkte steekproef). Controleer actuele advertenties en startdatums rechtstreeks in Meta Ad Library indien de bewijsvoering doorslaggevend is.

Meta Ad Library: https://www.facebook.com/ads/library/

### Oorspronkelijke concurrenten

| Merk | Stand van onderzoek | Gevolg |
|---|---|---|
| thePause / Harmoni | Positionering/productinformatie beschikbaar, maar geen betrouwbaar individueel Ad Library-overzicht met duur en format | Niet kwantitatief rangschikken zonder screenshots/advertentie-ID's |
| Play Health | Officiële website meldt sluiting van app en dienstverlening | **Niet** als actieve app-acquisitieconcurrent presenteren; https://playhealth.com/ |
| Waves Women | Product-/pricinginformatie beschikbaar; geen verifieerbare uitgewerkte advertentiesnapshot in dit onderzoek | Ad Library-capture nodig |
| balance (Dr. Louise Newson) | Niet eenduidig geverifieerde advertenties in deze sessie; meerdere bedrijven heten “Balance” | Verifieer exacte Facebook-pagina en page ID voordat je analyseert |

### Format en looptijd op het juiste niveau vastleggen

Aanbevolen aanleverdataset voor Claude:

```csv
brand,facebook_page_id,ad_id,ad_url,first_seen_date,as_of_date,status,format,primary_hook,cta,landing_domain,source_url,confidence
```

Met `run_days = as_of_date - first_seen_date` bij actieve advertenties; leg bij beëindigde advertenties de **laatste** waargenomen actieve datum vast, anders is het slechts een geschatte ondergrens. Creatieve varianten, individuele ads en campagneclusters niet door elkaar tellen. Sla bewijs/screenshot en peildatum op.

**Creative learning, beperkt ondersteund:** de onderzochte voorbeelden bij Midi Health en Alloy bevatten relatief veel statische advertenties. Dat is een argument om statische creatives **mee te testen**, geen grond om video als minder effectief af te schrijven. De propositie ‘begrip/helderheid/erkenning’ is inhoudelijk bruikbaar als creatieve hypothese, maar de dataset levert geen bewezen creatieve effectiviteit.

---

## Integrale consequenties voor AxisX

| Vraag | Onderbouwde uitkomst | Aanbevolen actie |
|---|---|---|
| 1. Betaalconversie | Freemium mediaan 2,1%; Health & Fitness iOS mediaan 3,5% (niet identieke segmenten) | Gebruik scenario's; betaalgedrag apart na bèta valideren |
| 2. Marktmaximum | 43,94 mln vrouwen 40–55; 23,43 mln berekende iOS-proxy, beide indicatief | Herbereken TAM; maak SAM/SOM met expliciete relevante doelgroep en smartphonebezit |
| 3. Ad policies | Gezondheidsinformatie belemmert remarketing en eventdeling; Google App Campaigns vergen store-publicatie | Niet afhankelijk zijn van health-eventoptimalisatie; privacy-/accountaudit vóór paid launch |
| 4. Quiz → D7 | Met een eigen login en first-party user-ID technisch uitvoerbaar | Instrumenteer events en definieer cohort/noemer; scheid symptomen van marketingevents |
| 5. Concurrenten | Midi en Alloy-formats/looptijden onderbouwd met snapshots; originele set deels onvoldoende gedekt | Verzamel exacte Meta Ad Library-records en datum-/formatbewijs |

### Prioriteit voor de hackathon / productvalidatie

1. **Product proof:** duidelijk gedefinieerde D1/D3/D7-cohorten; verifieer of de beoogde 60% D7-retentie daadwerkelijk gemeten kan worden.
2. **Distribution proof:** voldoende relevante testers, bijvoorbeeld via community's, partnerships en vertrouwenwekkende introducties, zonder verboden health-retargeting.
3. **Economic proof:** scenario rond paid conversion en £100, nadrukkelijk nog geen bewezen LTV/CAC-businesscase.
4. **Operational proof:** TestFlight-review, app-login, consent/privacybeheer en eventinstrumentatie gereed voor een cohort van 500.
5. **Creative proof:** statische en video-adconcepten naast elkaar testen; op basis van echte performance beslissen, niet op advertentieloopduur alleen.

**Samenvattend advies:** beschouw het eerste cohort van 500 gebruikers primair als **product- en retentievalidatie**. Voor een geloofwaardige economische case zijn naast D7-retentie later afzonderlijke betaalconversie, CAC, netto-ARPU/LTV, refundrate en kanaalrestricties noodzakelijk.

---

## Openstaande controles vóór formele externe indiening

- [ ] AxisX-casebrief nalopen: exacte doelgroep, aanbod, prijs, TestFlight-plan, D7-definitie.
- [ ] UN WPP 2026 per land op geslacht/leeftijd downloaden en de 40–55 totalen reproduceerbaar vastleggen.
- [ ] iPhone-bereik vervangen door daadwerkelijk smartphone-/iOS-bezit onder vrouwen 40–55 waar mogelijk; anders duidelijke bandbreedte gebruiken.
- [ ] Meta Events Manager: restrictiestatus voor de AxisX-site/app en elke gewenste optimalisatiegebeurtenis controleren.
- [ ] Google Ads: concrete campagnevorm en toegestane conversies juridisch/technisch toetsen.
- [ ] Consentflow en scheiding tussen health-data en marketingeventdata valideren.
- [ ] App Store Connect / TestFlight, eerste externe build-review, 90-dagenverval en loginflow testen.
- [ ] Concurrerende advertenties per exacte brand/page/ad-ID, format en startdatum vastleggen; geen prestaties afleiden uit looptijd.

## Volledige kernbronnen

1. RevenueCat, *State of Subscription Apps 2026* — https://www.revenuecat.com/state-of-subscription-apps
2. United Nations, *World Population Prospects 2024* — https://population.un.org/wpp/
3. UN Population Division, *DemoData* — https://population.un.org/demodata/home
4. Ofcom, *Online Nation 2025* — https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-research/online-nation/2025/online-nations-report-2025.pdf
5. Statcounter, *Mobile OS Market Share* — https://gs.statcounter.com/os-market-share/mobile
6. Triple Whale, *Facebook Advertising Benchmarks* — https://www.triplewhale.com/blog/facebook-ads-benchmarks
7. Google Ads, *Health in personalised advertising* — https://support.google.com/adspolicy/answer/16701855?hl=en
8. Google Ads, *Restricted targeting in personalised advertising* — https://support.google.com/adspolicy/answer/143465
9. Google Ads, *About App campaigns* — https://support.google.com/google-ads/answer/6247380?hl=en
10. Meta, *Business Tools Terms* — https://www.facebook.com/legal/technology_terms
11. Meta, *Data-sharing restrictions* — https://www.facebook.com/business/help/511197658391698
12. Apple, *TestFlight* — https://developer.apple.com/testflight/
13. Apple, *In-App Purchase / sandbox testing* — https://developer.apple.com/in-app-purchase/
14. Apple, *Get started with TestFlight* — https://developer.apple.com/videos/play/tech-talks/110343/
15. Meta, *Ad Library* — https://www.facebook.com/ads/library/
16. Sprites, *Midi Health Ads (snapshot)* — https://www.sprites.ai/midi-health-ads
17. Sprites, *Alloy Ads (snapshot)* — https://www.sprites.ai/alloy-ads
18. Play Health, *Official shutdown notice* — https://playhealth.com/

---

## Overdrachtsinstructie voor Claude

Behandel dit bestand als een **onderzoeksbijlage** bij de AxisX-casus. Neem brondata, berekende indicaties, aannames en openstaande verificatiepunten **niet zonder onderscheid** over als vaststaande feiten. Gebruik officiële bronnen en reproduceerbare berekeningen voor harde claims, en label de creatieve en economische aanbevelingen als hypotheses. Waar de actuele of officiële casebrief afwijkt, heeft de casebrief voorrang.


---

# Bijlage B — Volledige notitie: landingspagina, selectiequiz en D7-retentie

# AxisX — Van landingspagina naar 500 geschikte testers en ≥300 D7-actieve gebruikers

**Onderzoeks- en ontwerpnotitie voor founder / Claude Code**  
**Datum:** 23 oktober 2026  
**Status:** beredeneerd concept, gereed voor implementatie-uitwerking en validatie met founder; **geen klinisch gevalideerd screeningsinstrument**.

## 0. Samenvatting en bronstatus

**Vraag:** Hoe filteren we *de mensen die al na de activatie op de landingspagina aankomen*, zodat we een zinvol cohort van 500 opbouwen en minstens 300 gebruikers op dag 7 aantoonbaar blijven gebruiken? Niet: hoe bereiken we de doelgroep via community's of advertenties.

**Founderdoelgroep zoals in de eerdere casusbespreking omschreven:** vrouwen vanaf ongeveer 39 jaar die perimenopauze *herkennen of vermoeden* en **actief op zoek zijn naar ondersteuning**. De appbelofte draait om persoonlijke inzichten, herkenning, tracking van veranderingen, hanteerbare begeleiding en meer regie. Het eerste experiment is een iOS/TestFlight-bèta. Getallen uit de casusbespreking: 500 eerste gebruikers, D7-retentie ≥60% (≥300 gebruikers), een toekomstig abonnementsmodel van ongeveer £100/jaar, en een mogelijke samenvatting voor een arts na twee weken. **De exacte, door de founder goedgekeurde doelgroepdefinitie, geografische toelatingsregels en feitelijk beschikbare MVP-features zijn in deze notitie niet zelfstandig aan een founder-authored brondocument geverifieerd.** Daarom zijn bepaalde keuzes hieronder expliciet *voorgestelde ontwerpbeslissingen*; beoordeel ze tegen het originele brief voordat ze als harde regels worden geïmplementeerd.

**Principiële keuze:** niet selecteren op diagnose, ernst of hoeveelheid klachten. Selecteer primair op: (1) herkenning van het probleem, (2) **actief zoeken** of al iets geprobeerd hebben, (3) een concrete *job-to-be-done* die de huidige app echt kan bedienen, en (4) capaciteit en bereidheid om de bèta in de komende week daadwerkelijk te testen. Bewaar variatie in behoeften en gebruiksgemak: louter supergemotiveerden selecteren leidt tot een niet-representatief, kunstmatig hoog retentiegetal.

**Belangrijkste resultaat van deze notitie:** complete Engelse, direct inzetbare copy voor de landingspagina; een pre-screen van 3 vragen; 9 kern-quizvragen plus optionele baseline; routing; cohortopzet; retentiedefinitie; eventmodel; privacyvoorwaarden; meetschema; cijfers; bronnen.

## 1. Wat zegt onderzoek — en wat niet?

1. **Menopauzeondersteuning moet persoonlijk en geloofwaardig zijn.** Een Britse online vragenlijst onder 1.596 respondenten (mediane leeftijd 50 jaar; veel peri- of postmenopauzaal) rapporteerde dat 77,4% zichzelf hooguit enigszins of helemaal niet geïnformeerd voelde en dat 59,1% bestaande informatie niet voldoende afgestemd vond op de eigen situatie. 92,7% had actief informatie gezocht. *Let op*: zelfgeselecteerde enquête; percentages zijn niet representatief voor alle vrouwen 39+ en geen voorspellers van AxisX-conversie. Bron: Harper et al. (2025), *InTune*, https://journals.sagepub.com/doi/10.1177/20533691251372818.
2. **Niet van een formele diagnose of één symptoom uitgaan.** NICE adviseert bij verder gezonde vrouwen ≥45 jaar met passende symptomen perimenopauze vaak klinisch, zonder labtest, te herkennen. De European Society of Endocrinology stelt dat klachten ook tussen 40 en 45 relevant kunnen zijn. Menstruatiepatronen kunnen door anticonceptie, hysterectomie of andere factoren niet informatief zijn. Geen zelfdiagnose op basis van de quiz. NICE NG23, https://www.nice.org.uk/guidance/ng23/chapter/Recommendations; ESE-guideline, https://academic.oup.com/ejendo/article/193/4/G49/8281862.
3. **De behoefte is breder dan symptoomregistratie.** Analyse van 18 menopauze-apps en reviews identificeerde behoefte aan empowerment, herkenning, eenvoud, privacy, gepersonaliseerde functies, en betere voorbereiding voor zorggesprekken. Bron: *This App Just Gets Me* (2023), https://www.tandfonline.com/doi/full/10.1080/15398285.2023.2204287.
4. **Engagement hangt samen met nut, zelfregie en ondersteuning, niet uitsluitend met symptoomlast.** Een review van 41 studies over health-appgebruik noemt personalisatie, self-monitoring, nuttige feedback, duidelijke doelen, reminders, eenvoudige bediening en ervaren nut als relevante factoren. Bron: Szinay et al. (2020), https://pubmed.ncbi.nlm.nih.gov/32348255/. Een overzicht van 19 systematische reviews in 2026 benadrukt autonomie, competentie en verbondenheid, maar vindt grote verschillen in hoe engagement wordt gemeten: https://mhealth.jmir.org/2026/1/e88382. **Deze bronnen valideren geen exact AxisX-quizscoremodel of specifiek D7-predictiepercentage.**
5. **Uitval bij health-apps is een serieus risico.** Review van 62 mHealth-studies: vaak substantiële uitval; steun, persoonlijke feedback en bruikbare herinneringen helpen, onbruikbaarheid en techniek hinderen. Bron: https://www.jmir.org/2022/4/e35120/. In een cohortstudie was 53,79% van de ingestemde onderzoeksdeelnemers ooit appgebruiker; dat is een waarschuwing om inschrijving en feitelijke activatie uit elkaar te houden, **geen AxisX-forecast**: https://pmc.ncbi.nlm.nih.gov/articles/PMC9233254/.
6. **Meeteenheid vastzetten.** Amplitude onderscheidt *Return On Day 7* (precies D7) van *Return On or After* (D7 of later), en adviseert een betekenisvolle productactie in plaats van alleen appopen als retentie-event: https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-interpret en https://amplitude.com/books/mastering-retention/the-retention-lifecycle-framework.

**Synthese:** laat de deelnemer eerst zien hoe de app haar persoonlijke behoefte kan bedienen; gebruik daarna een beperkte quiz om doelgroepfit, actuele hulpvraag en haalbare deelname te beoordelen. Verzamel gedetailleerde, gevoelige symptoomgegevens pas in de app na een duidelijke, afzonderlijke toestemming. De quiz verhoogt vermoedelijk de kwalificatiekwaliteit, maar kan 60% D7 niet waarborgen.

## 2. Het selectiemodel in één overzicht

| Laag | Vraag | Doel | Beslissing |
|---|---|---|---|
| Landing | Herken je perimenopauze of vermoed je dit en zoek je nu steun? | Relevantie | Niet-relevant → informatieve/later-route, niet als primaire bèta-gebruiker tellen |
| Landing | Leeftijdsband en land | Founder- en marktfit | Leeftijd ~39+ als kern; 39–55 als prioriteit **alleen indien bevestigd**; geen medische conclusie uit leeftijd |
| Landing | Geschikte iPhone en TestFlight | Technische haalbaarheid | Nee → wachtlijst voor latere versie, niet rekenen als active user |
| Quiz | Actief zoekgedrag in voorbije 30 dagen | Gedragsmatige intentie | Sterk signaal; niet als enige harde poort |
| Quiz | Specifiek probleem en gewenste eerste-weekwaarde | Product–need fit | Vraag die MVP niet kan vervullen → verwachtingsmanagement / later cohort |
| Quiz | Beschikbaar startmoment en realistische micro-inzet | Kans op eerste-weekdeelname | Nu instapbaar → cohort; pas later beschikbaar → geplande wachtlijst |
| App | Eerste waardevolle handeling | Echte activatie | Alleen na deze actie de 500-gebruikerscohort starten |
| Dag 7 | Betekenisvolle terugkeer | D7-uitslag | 300/500 vereist; per cohort en behoefte vergelijken |

**Niet gebruiken als harde uitsluiting:** ernst van symptomen, HRT-gebruik, formele diagnose, kinderen, werkstatus, opleidingsniveau, inkomen, etniciteit, eerdere artsbezoeken of privacybezorgdheid. Dit kan tot selectievertekening, oneerlijke uitsluiting of onnodige verzameling van gezondheidsdata leiden.

## 3. Landingspagina: copy die zichzelf selecteert

### Headline en waardepropositie (Engels, extern)

> **You already know something is changing. Let's make more sense of it.**  
> For women exploring perimenopause who want a clearer picture of their own experience — not another page of generic advice.

**Subhead:**

> Join the AxisX Founders Circle to try an early iPhone experience designed to help you reflect on patterns, build a manageable check-in habit, and see what feels useful for *you*. Help shape what comes next.

**Verwachtingsblok, vóór CTA (nooit valse productclaim):**

> **A small, real-world 7-day beta**  
> - Designed for people already exploring perimenopause and looking for support  
> - A short, personalised starting questionnaire  
> - Try the available AxisX beta features during the week  
> - Share honest feedback, including what doesn't help  
> - Free during beta, on iPhone via Apple's TestFlight  
> - Not a diagnosis, treatment or replacement for a healthcare professional

**CTA:** `See if the Founders Circle is right for me`.

**Trust copy:**

> Your answers stay with AxisX for the purposes explained in our privacy notice. Health answers are not used to build ad-platform audiences. Participation is voluntary and you can stop at any time.

**Bevestig vóóraf de feitelijke MVP-features**. Als de eerste build geen patronen/adviezen laat zien, pas bovenstaande copy aan naar wat de gebruiker werkelijk ontvangt. Belofte ≠ feature-wens.

### Drie korte pre-screenvragen (20–40 seconden)

**L1 — Relevantie [harde doelgroeppasvorm; single choice]**  
**Question:** `Which best describes what brings you here?`  
A. `I think I may be in perimenopause and I'm actively looking for support.`  
B. `I'm already getting some menopause support, but I want to better understand my own experience.`  
C. `I'm noticing changes and starting to explore whether perimenopause may be relevant.`  
D. `I'm mainly curious about menopause information for the future.`  
E. `I'm looking on behalf of someone else.`  
**Routing:** A/B = primair; C = zorgvuldig meewegen (actieve zoekvraag toetsen); D/E = informatieve route, geen primaire Founders Circle-testers.

**L2 — Leeftijd [markt- en founderfit, niet diagnostisch]**  
`Which age range are you in?`  
`Under 39 / 39–44 / 45–49 / 50–55 / 56–60 / 61+ / Prefer not to say`  
**Routing:** 39+ = kern passend bij eerdere founderindicatie; 39–55 prioriteren als uiteindelijke core-ICP dat bevestigt. 56+ niet automatisch ongeschikt verklaren als de founder een bredere doelgroep toestaat; onder 39 of onbekend = aparte toets/geen automatische medische uitsluiting.

**L3 — Testtechniek [harde huidige bètagrens]**  
`Could you use an iPhone to test an app through Apple TestFlight during the next week?`  
`Yes / I have an iPhone, but need help with TestFlight / No, I use Android / Not in the next week`  
**Routing:** Yes/help = door; Android = wachtlijst; later = later cohort. **Land als afzonderlijk dropdownveld alleen ophalen als geografische ondersteuning/het taalgebied echt een deelnamevoorwaarde is.**

**Privacy:** de formulering van L1 kan gezondheidsinformatie opleveren. Laat vóór zulke antwoorden de privacy-informatie zien en verkrijg waar vereist een rechtsgrond en toepasselijke Artikel 9-uitzondering, bijvoorbeeld specifieke uitdrukkelijke toestemming. Scheid deze van optionele marketingtoestemming. Als compliance dat niet kan, houd de publieke landing voorlopig volledig niet-gezondheidsinhoudelijk en vraag L1 pas na een behoorlijke toestemmingsstap.

## 4. Kernquiz: de negen meest waardevolle vragen

Na de pre-screen maximaal ca. 2–3 minuten, liefst adaptief. Vraag niet vooraf naar een volledige medische historie. Geef antwoordopties waarin onzekerheid en voorkeur om niet te antwoorden passen.

| ID | Exacte Engelstalige vraag en antwoordopties | Wat leert AxisX? | Hoe gebruiken? |
|---|---|---|---|
| Q1 — Perceptie | **`Where would you say you are right now?`** `I suspect perimenopause / I have discussed it with a healthcare professional / I am unsure but concerned about changes / I believe I am already postmenopausal / Other / Prefer not to say` | Zelfbeeld, niet diagnose | Segmentatie; geen geforceerde medische classificatie |
| Q2 — Recent gedrag | **`Which of these have you done in the last 30 days to understand or manage these changes? Select all that apply.`** `Searched for trusted information / Spoke to a clinician / Talked with friends or a community / Tracked symptoms, sleep or mood / Tried an app or journal / None of these / Prefer not to say` | Meer geloofwaardig *revealed effort* dan puur intentie | Prioriteringssignaal; 'geen' niet automatisch afwijzen |
| Q3 — Topprobleem | **`What's the main thing you wish felt easier right now? Choose one.`** `Making sense of the changes / Spotting patterns over time / Knowing which small steps to try / Having a clearer conversation with a clinician / Feeling less alone / I'm mainly looking for diagnosis or prescriptions / Other` | Concrete job-to-be-done | Match op *werkelijk beschikbare* bèta-features; bij diagnoseverwachting geen belofte doen |
| Q4 — Bestaande oplossing | **`What do you currently use, if anything, to make sense of what's going on?`** `Nothing consistent / Notes or calendar / Another health app / A wearable or sleep tracker / Support from a clinician / Community advice / Other` | Frictie, alternatieven, ervaringsniveau | Personalisatie; geen uitsluiting van beginners |
| Q5 — Eerste-weekresultaat | **`After one week with AxisX, which result would feel most valuable to you? Choose one.`** `I understand my experience better / I can see something useful in my own notes or patterns / I've found a simple check-in that fits my life / I have clearer notes or questions for a healthcare visit / I feel more supported / Other` | Gewenste concrete 'aha' | Later toetsen aan werkelijke waardeperceptie op D7 |
| Q6 — Tijd en haalbaarheid | **`What would realistically fit into your next seven days?`** `About a minute most days / Two or three short check-ins / One longer session / I can't commit time this week / I'm not sure` | Gewoonte- en planningsfit | Bij 'geen tijd' latere start voorstellen; niet doen alsof D7 dagelijkse deelname vereist |
| Q7 — Startbereidheid | **`When could you realistically install and try the beta?`** `Within 48 hours / Within 3–7 days / In 1–2 weeks / Later or not sure` | Nabije actiebereidheid | Bèta-cohort per startweek, niet allemaal direct uitnodigen |
| Q8 — Verwachtingsfit | **`AxisX is an early self-reflection and support tool, not a diagnostic or prescribing service. Is that what you're looking to try?`** `Yes / Mostly, but I have questions / No, I need clinical diagnosis or treatment right now` | Voorkomt verkeerde waardepropositie | 'Nee' = verwijs naar passende zorginformatie; geen foutief medisch advies |
| Q9 — Afhaakrisico | **`What would most likely stop you from using an app like this after a few days?`** `It takes too much time / I don't see a personal benefit / I worry about privacy / It's confusing or difficult / Notifications feel intrusive / My symptoms or priorities vary / Other` | Verwachte frictie en productverbetering | Eén gerichte praktische maatregel per gebruiker; privacyzorg nooit als 'slechte lead' behandelen |

**Optioneel, vrije tekst (max. 140 tekens, liefst in-app ná toelating):** `In your own words, what would you most like to make sense of this month?` Gebruik uitsluitend voor gebruikersinzicht en met privacywaarborgen; niet automatisch diagnostisch interpreteren. Vraag **niet** openbaar naar exacte menstruatiegeschiedenis, medicatie, seksueel functioneren of gedetailleerde mentale gezondheid als dat niet strikt nodig is voor selectie.

**Optionele aanvullende vraag voor kwaliteit van het onderzoek, niet voor toegang:** `How confident do you feel about understanding what's happening in your body right now?` 1–5-schaal, bij eerste appgebruik herhalen na 7 dagen. **Dit meet ervaren duidelijkheid, geen klinische uitkomst.**

### Wat de quiz uitdrukkelijk NIET hoeft te weten

- Geen bewijs van formele perimenopauzediagnose, FSH-uitslagen, HRT-status of hoeveelheid klachten als toegangspoort.
- Geen salaris, opleidingsniveau, gezinsvorm, seksuele oriëntatie, religie, etniciteit of andere gevoelige achtergrondkenmerken om 'kans op plakken' te berekenen.
- Geen vraag `Would you pay £100?` als kwalificatiecriterium voor de gratis bèta: hypothetische betalingsbereidheid is zwak bewijs, vergroot selectiebias en hoort eerder in een afzonderlijke monetisatieproef.
- Geen dramatische 'symptoomscore' of 'menopauzestadium'-uitkomst presenteren alsof de quiz een diagnose geeft.

## 5. Hoe beslist het systeem? Geen pseudo-klinische AI-score

Gebruik transparante deterministische **routing** plus een te testen prioriteitsmodel. Niet een verborgen 'risicoscore', geen voorspelde medische status.

**A — Founder-fit, uitnodigen (doel: ongeveer 70% van de eerste 500)**
- Erkent of vermoedt perimenopauze *én* is actief op zoek naar ondersteuning of kan een concrete actuele hulpvraag formuleren.
- Heeft iPhone/TestFlight-toegang, is binnen 7 dagen beschikbaar, begrijpt de bètagrenzen.
- De gekozen gewenste eerste-weekwaarde wordt daadwerkelijk door de MVP ondersteund.
- Recent gedrag (Q2) is een plus, maar géén verplichting; privacybehoefte of lagere symptoomlast verlaagt de kansen niet.

**B — Founder-fit maar minder voorspelbaar / gemengd (doel: ongeveer 30%)**
- Nog zoekend, minder app-ervaring, minder tijd, of onduidelijk wat het meeste helpt — maar wel relevant en in de komende week bereid te proberen.
- Opnemen om te leren *welke fricties AxisX moet oplossen* en te voorkomen dat alle resultaten van enthousiaste experts komen.
- Gebruik lichte, respectvolle onboardinghulp; niet manipuleren om de D7-statistiek te halen.

**C — Niet in deze bèta / later**
- Bezoeker is slechts algemeen nieuwsgierig en zoekt nu geen ondersteuning, of zoekt uitsluitend hulp voor iemand anders.
- Geen geschikt iOS-toestel of kan nu niet starten.
- Verwacht een medische diagnose, behandeling of voorschrift die AxisX niet biedt.
- Kan of wil niet instemmen met *voor deze functionaliteit echt noodzakelijke* dataverwerking. Respecteer dit; verzamel niet toch gezondheidsdetails.

**Let op:** 70/30 is een *voorstel voor onderzoeksbalans*, niet een uit onderzoek afgeleide optimale verdeling. Label beide groepen vooraf en rapporteer de uitkomsten apart én gezamenlijk. Zet selectie niet zó strak dat product–market fit alleen voor een extreem enthousiaste subset gemeten wordt.

### Score alleen als secundair experiment

Voor inzicht in het effect van vragen kun je vrijblijvende binaire indicatoren vastleggen: `active_help_search`, `recent_information_seeking`, `clear_supported_job`, `ready_within_week`, `expected_burden_fit`. Schat na circa 50–100 **daadwerkelijk gestarte** testers per indicator het verband met `meaningful_D7`; probeer geen wetenschappelijk klinkende, arbitraire puntsom als waarheidsmodel te presenteren. Kijk bovendien of vragen bepaalde relevante groepen systematisch benadelen. Evalueer uitval door installatie-/toegangsproblemen los van productretentie.

## 6. Rekenkundige werkelijkheid: 500 inschrijvingen is niet hetzelfde als 500 gebruikers

**Heldere voorkeursdefinitie:** cohort van **500 geschikte, unieke gebruikers die de app op D0 openen én de eerste betekenisvolle actie uitvoeren**. Het D7-doel is ≥300/500 = ≥60% volgens de vóór de test vastgezette definitie.

Als '500 aanmeldingen' letterlijk 500 ingestuurde quizformulieren betekent, moet je rekening houden met elk volgende verliespunt. Bijvoorbeeld een **fictief rekenvoorbeeld, niet voorspelde AxisX-cijfers**:

| Funnelstap | Percentage op vorige stap | Resterend van 500 |
|---|---:|---:|
| Ingeschreven | — | 500 |
| Geschikt en toegelaten | 90% | 450 |
| TestFlight geïnstalleerd | 90% | 405 |
| Eerste waardevolle appactie | 90% | 365 |
| Betekenisvol actief op dag 7 | 75% | **273** |

De gezamenlijke kans van inschrijving tot D7 is in dit voorbeeld `0,90 × 0,90 × 0,90 × 0,75 = 54,7%`, niet 60%. Als drie vroege stappen elk op 90% staan, zou de laatste D7-stap ongeveer **82,3%** moeten zijn om 300 over te houden. Een positieve quiz alleen maakt dat niet realistisch.

**Scenariotabel bij 500 daadwerkelijk op D0 geactiveerde gebruikers:**

| D7-retentie | D7-gebruikers | Doel 300? |
|---:|---:|---|
| 40% | 200 | Nee |
| 50% | 250 | Nee |
| 55% | 275 | Nee |
| **60%** | **300** | **Net** |
| 65% | 325 | Ja |
| 70% | 350 | Ja |

**Buffers als meer dan 500 D0-geactiveerde gebruikers zijn toegestaan:** bij 55% D7 zijn minstens `ceil(300/0,55) = 546` D0-geactiveerden nodig; bij 50% minimaal **600**. Als 500 een **harde cap** is, kun je geen buffer creëren: de werkelijke D7-retentie moet dan ≥60% zijn. Het doel is ambitieus en niet te garanderen met prescreening.

**Voorbeeld bij gemengde cohorten** (alle percentages hypothetisch): 350 A-gebruikers met 70% D7 (245) + 150 B-gebruikers met 40% D7 (60) = **305 D7-actieve gebruikers**. De beperkte marge van vijf laat juist zien dat kleine afwijkingen het doel kunnen doen missen. **Deze 70/40 zijn geen empirisch bekende conversiekansen voor AxisX.**

**Onderzoeksnauwkeurigheid:** als 300 van 500 op D7 actief zijn, is het geobserveerde percentage 60%. Een eenvoudige normale 95%-marge voor een binomiale proportie is `1,96 × sqrt(0,6 × 0,4 / 500) ≈ 4,3 procentpunt`, dus grofweg 55,7–64,3%; willekeurige steekproeffouten zijn nog niet hetzelfde als de veel grotere wervings- en selectiebias. In kleinere segmenten wordt onzekerheid duidelijk groter. Gebruik dit cohort niet voor klinische effectiviteitsclaims.

## 7. Wat moet 'plakken' betekenen? D0, D7, feedback en datawaarde

**Maak één primaire metriek:**

- **D0** = eerste daadwerkelijke, door gebruiker geïnitieerde waardevolle actie in de bèta, bijvoorbeeld een persoonlijke check-in of reflectie; niet alleen vragenlijst afgerond, app geïnstalleerd of notificatie ontvangen.
- **D7 (strikt, Return On)** = opnieuw een waardevolle, actieve apphandeling in het tijdvenster **168–192 uur** na D0 (wanneer met 24-uursdagen wordt gewerkt), zoals een check-in, een persoonlijk inzicht openen met zichtbare interactie of een aanpasbare notitie. Niet een stille push, een automatische achtergrondactie of louter inloggen.
- **D7 'in week 1 terugkeer'** = aparte aanvullende metriek: één of meer waardevolle acties tussen >0 en 7 dagen na D0. Dit is **niet** gelijk aan strikte D7.
- **D7 beoordeling** pas wanneer elke deelnemer de volledige meetperiode heeft doorlopen; lopende cohorten niet meenemen als 'uitgevallen'.

**Secundair:** D1, D3, aantal unieke dagen met waardevolle acties, persoonlijke 'aha' (ja/nee), waardering 1–5, gekozen behoefte versus ervaren waarde, startvertraging, feedbackcontact, technische errors en churnreden. Vermeld welke vraag/metric productfit versus alleen operationele frictie meet.

**De 'week-7 day' ervaring mag geen schijnretentie worden.** Vraag om feedback, maar tel die niet als productretentie wanneer de gebruiker de productwaarde niet meer ervaart. Faciliteer een natuurlijk gebruiksritme; laat deelnemers zonder schuldgevoel uitstromen.

## 8. Beschikbare data met slechts 500 deelnemers — wat moet je minimaal meten?

| Bron | Variabelen | Waarom |
|---|---|---|
| Landing | `screen_started`, `screen_completed`, `age_band`, `country`, `ios_ready` | Effectiviteit en bias van selectie |
| Quiz | `self_perceived_stage`, `active_help_search`, `help_actions_30d[]`, `primary_job`, `current_approach`, `desired_week1_outcome`, `available_checkins`, `start_window`, `expectations_fit`, `dropoff_barrier` | Hypothesen over fit/waarde/uitval |
| Uitnodiging | `eligible_status`, `cohort`, `invited_at`, `invite_accepted_at`, `installed_at`, `first_action_at` | Begrijp administratieve uitval |
| App | `meaningful_checkin_at`, `personal_insight_viewed_at`, `user_returned_at`, `feedback_submitted_at` | Kernwaarden en gedragsretentie |
| D7 | `day7_meaningful_retained`, `perceived_value`, `desired_outcome_delivered`, `barrier_reported` | Productfit en verklarende analyse |
| Tech | `device_compatibility`, `testflight_invitation_error`, `crash`, `app_version` | Technische uitval niet verwarren met productafwijzing |

**Pseudonieme koppeling:** maak een AxisX `user_id` aan en gebruik dezelfde identificatie van quiz naar login, in-app-activatie en D7. Gescheiden tabellen/rechten voor identiteits- en gezondheidsgegevens. Deel geen symptoomantwoorden, persoonlijke gezondheidssegmenten of medische eventparameters met Google/Meta. TestFlight biedt praktische bèta-ondersteuning maar niet automatisch de volledige quiz→D7-koppeling; daarvoor is eigen authenticatie/eventopslag nodig: https://developer.apple.com/testflight/.

**Beperk granulariteit:** bij 500 testers maximaal circa 3 primaire behoeftegroepen plus land/gebruikerservaring als exploratieve uitsplitsing, niet tientallen kruistabellen met te kleine cellen. De gekozen doelgroepen alleen vergelijken mits de benodigde functies in de bèta daadwerkelijk werken.

## 9. Pre-registratie en validatie: hoe voorkomen we cherry-picking?

1. Leg **voor instroom** vast: doelgroep, harde technische voorwaarden, de A/B-inclusieregels, welke score-items worden getoond en wat D7 precies is.
2. Meet voor de **eerste 50–100 D0-geactiveerde deelnemers** of antwoorden op Q2/Q3/Q6/Q7 werkelijk samenhangen met installatie, eerste waardevolle actie en vroege terugkeer. Verander niet stiekem de betekenis van reeds gerapporteerde cohorten.
3. Kijk naast gemiddelden ook naar **privacyzorgen, app-ervaring, tijdsdruk, behoeftegroep en land**. Een te laag resultaat bij een subgroep kan een oplosbaar onboardingprobleem zijn, niet een 'slechte doelgroep'.
4. Als regels worden bijgesteld, label `selection_rule_version` en rapporteer v1 en v2 apart.
5. Houd een beperkte variatie aan in het cohort: bijvoorbeeld circa 70% duidelijke founder-fit en circa 30% nog zoekende maar relevante vrouwen. Alleen binnengelaten enthousiaste gebruikers meten geeft te rooskleurige uitkomsten.
6. Vraag op dag 7 ook *waarom* iemand niet bleef, liefst met neutrale antwoordopties (`not useful yet`, `too much effort`, `trust/privacy`, `technical issue`, `life got in the way`, `other`). Een vrijwillige eenmalige exitvraag is géén retained event.
7. Rapporteer altijd **van instroom tot D7** én **van D0 tot D7**. Anders kan een mooie appretentie slechte installatie-/activatiecijfers maskeren.

## 10. Privacy, veiligheid en verwachtingmanagement

Deze vragen kunnen impliciet of expliciet gezondheidsgegevens opleveren; ook een **afgeleide score** op perimenopauze kan bijzondere persoonsgegevens betreffen. Volgens de Britse ICO is voor zulke verwerking een rechtsgrond uit Artikel 6 én een toepasselijke uitzondering uit Artikel 9 nodig. Uitdrukkelijke toestemming is een mogelijke, maar niet automatisch enige of altijd passende route; ze moet specifiek, geïnformeerd, afzonderlijk en intrekbaar zijn. De gebruiker moet weten waarom data wordt verzameld, hoe lang ze bewaard wordt, en wie er toegang heeft. **Juridische review vóór livegang**, ook voor EU/EEA-deelnemers en internationale datastromen.

- ICO special category data: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-are-the-rules-on-special-category-data/
- ICO explicit consent: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-are-the-conditions-for-processing/
- ICO data minimisation and transparency: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/special-category-data/

**Praktische consequenties:** noodzakelijke gezondheidsgegevens pas na passende informering/toestemming; scheid opt-in voor onderzoek/gebruik van opt-in voor marketing; geef 'prefer not to say'; gebruik niet automatisch volledige vragen plus persoonlijk antwoord als marketing-event; geen medisch oordeel of behandeling suggereren; werk met content- en featurechecks door founder/klinisch adviseur. De quiz is **geen medisch triage- of diagnostisch instrument**. Actuele of ernstige klachten verdienen beoordeling door een bevoegde zorgprofessional, onafhankelijk van deelname.

## 11. Wat ik expliciet aan de founder zou laten vaststellen vóór bouwen

- Is de eerste doelgroep strikt **39–55**, of in feite **39+ zonder bovengrens**? Welke landen en talen zijn werkelijk in de bèta ondersteund?
- Welke concrete first-week features werken écht: symptoomlog, patroonherkenning, uitleg, dagelijkse suggestie, feedback en/of artsrapport? Geen feature beloven die nog niet live is.
- Is het primaire doel **500 inschrijvingen** of **500 geïnstalleerde en D0-geactiveerde testers**? De vraag '300 plakkers' is zonder deze definitie mathematisch ambigu.
- Bedoelt de founder **D7-strikt** of actief *ergens tijdens week één*? Beiden rapporteren, slechts één als primary.
- Is de bèta gratis, hoe worden gezondheidsdata verwerkt, en welke onderzoeks- en feedbacktoestemmingen bestaan er?

## 12. Aanbevolen oplevering voor Claude Code

Maak op basis van deze notitie:

1. **Landing page** met kernbelofte, echte feature-beschrijving, 7-daagse verwachtingen, duidelijke privacylinks en CTA.
2. **Korte adaptieve prescreen + quiz** met bovenstaande Engelse teksten, verplichte/optionele velden, logische conditionele routing en toegankelijkheid.
3. **Wachtlijstpagina's op maat** voor geen iOS, later instappen, primair diagnoseverzoek en alleen informatie zoeken — zonder stigmatiserende of medische uitsluitclaims.
4. **Datamodel** waarin `user_id`, quizversie, beslisregelversie, toestemming, cohort, startdatum en first-party productevents apart en correct gekoppeld zijn.
5. **Dashboard** met instroom → gekwalificeerd → uitnodiging → installatie → D0 → strict D7, uitval per stap, onderzoeksgroepen en kwaliteit van data.
6. **Validatieplan** voor de eerste 50–100 geactiveerde deelnemers, zonder het criterium achteraf te verschuiven.
7. **Founder review** op feitelijke doelgroep, actuele MVP, onderbouwde privacyteksten en KPI-definitie vóór livegang.

### Eindadvies

De juiste vraag is niet *'Hoe identificeren we 500 vrouwen die zeven dagen zullen blijven?'* — dat kan een quiz niet met zekerheid. De juiste vraag is: **'Hoe zorgen we dat 500 al geïnteresseerde, geschikte vrouwen snel een echte eerste waarde ervaren, terwijl we voldoende variatie bewaren om betekenisvolle productlessen te trekken?'**

De kernselectie is: **actief hulpzoekend + concreet probleem + huidige productfit + deze week kunnen beginnen**. De rest moet de kwaliteit van AxisX zélf bewijzen.

---

## Bronnenoverzicht

1. NICE, *Menopause: identification and management (NG23)*, update 2026: https://www.nice.org.uk/guidance/ng23/chapter/Recommendations
2. European Society of Endocrinology, menopause guideline (2025): https://academic.oup.com/ejendo/article/193/4/G49/8281862
3. Harper et al. (2025), UK InTune survey: https://journals.sagepub.com/doi/10.1177/20533691251372818
4. Szinay et al. (2020), uptake/engagement systematic review: https://pubmed.ncbi.nlm.nih.gov/32348255/
5. *Mechanisms of Engagement With Mobile Health Apps* (2026): https://mhealth.jmir.org/2026/1/e88382
6. *Challenges in Participant Engagement and Retention Using Mobile Health Apps* (2022): https://www.jmir.org/2022/4/e35120/
7. *Electronic Health Record–Based Recruitment and Retention and Mobile Health App Usage* (2022): https://pmc.ncbi.nlm.nih.gov/articles/PMC9233254/
8. *“This App Just Gets Me”: Assessing Menopause Smartphone Apps* (2023): https://www.tandfonline.com/doi/full/10.1080/15398285.2023.2204287
9. *Understanding challenges of using digital health technologies for menopause information* (2026): https://pubmed.ncbi.nlm.nih.gov/41072153/
10. Amplitude, *Interpret retention analysis*: https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-interpret
11. Apple, *TestFlight*: https://developer.apple.com/testflight/
12. UK ICO, *Special category data*: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-are-the-rules-on-special-category-data/
13. UK ICO, *Conditions for processing*, including explicit consent: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-are-the-conditions-for-processing/

*Alle genoemde quizvragen, cohortsplits en selectiepercentages zijn voorstellen voor AxisX, geen gevalideerde klinische instrumenten of empirisch bewezen voorspellers van D7-retentie. Verifieer de exacte founder-brief en werkende MVP voordat copy of selectiecriteria live gaan.*

---

## Slot — Gebruik in Claude Code

Dit dossier combineert: (1) de vragen en hoofdantwoorden uit het zichtbare AxisX-gesprek, (2) de volledige markt-/beleidsonderbouwing, (3) het uitgebreide onderzoeksgebaseerde selectie- en retentieontwerp.

**Werkinstructie voor Claude:** behoud het onderscheid tussen officiële bronnen, externe benchmarks, berekende indicaties, planningsaannames, conceptueel ontwerp en nog door de founder te bevestigen uitgangspunten. Behandel geen enkele voorgestelde quizscore, conversie- of D7-waarde als empirisch gevalideerde voorspeller voor AxisX totdat het eigen productdata-onderzoek dat ondersteunt. Baseer harde selectieregels op de actuele, door de founder goedgekeurde briefing en beschikbare MVP-features.
