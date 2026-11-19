# Loudbox-bevindingen: wat alleen uit de MCP-connector komt

Geschreven voor: wie de eindconclusies afrondt met de ChatGPT-handoff en het samenvoegvoorstel in de hand. Dit document bevat uitsluitend wat niet uit de brief, de CSV of de visual guidelines te halen is, en wat dat verandert aan insights, hypotheses, budget en vooral de creative brief.

Bronnen, allemaal via `loudbox-demo` (read-only demo, workspace `nigeria-...`, dataset `indrive-ng-q3-2026-v1`):
- `creativeLibrary.detail` + `get_creative_preview`: één keyframe per Q3-creative, alle 20 bekeken. Lage resolutie (360x640 tot 1080x1920), één frame, geen audio, geen tijdlijn.
- `voiceOfCustomer.dashboard`: App Store-reviews Nigeria, 50 per merk, inDrive (sept-okt 2026) en Bolt (apr-okt 2026). Door Loudbox gethematiseerd, met citaten en bron-ID's.
- `creativeLibrary.list` per concurrent: Bolt 22 betaalde ads, Uber 0, Lagride 6 organische LinkedIn-posts.
- `brandAssets.list`: de inDrive modulaire kit als bestanden (56 assets).

Beperkingen vooraf: een keyframe is niet de video. Bij vier AI-video's (NG-09, 10, 12, 13) is het keyframe identiek, dus daar zie ik waarschijnlijk een gedeeld eindscherm en niet de hook. Reviews zijn één platform, 50 stuks, niet representatief. Alles hieronder is daarom "waargenomen op het keyframe" of "gemeld door reviewers", geen bewezen oorzaak.

---

## 1. Visuele audit van de 20 creatives

| ID | Kanaal, formaat | Wat het keyframe toont | inDrive-moment zichtbaar? | CPA | Lezing |
|---|---|---|---|---:|---|
| NG-01 | Google static 1200x628 | Split screen: links grijze kaart met taxi-checkerpatroon en een vaste "NGN"-prijsbalk, rechts groene inDrive-kaart met NGN-slider (min/plus). Geen mens, geen headline. | Ja, prijs-slider | 0.97 | Pure interface-vergelijking: "vaste prijs" versus "jij schuift". Geen gezicht nodig gebleken. |
| NG-02 | Google motion 9:16 | Zelfde split verticaal, boven anoniem/onder inDrive. | Ja, slider | 1.70 | Zelfde concept, zelfde elementen, 9:16 motion. |
| NG-03 | Google motion 1200x628 | Zelfde split als NG-01, maar als motion in landscape. | Ja, slider | 8.44 | Identiek keyframe aan NG-01. Het verschil zit dus in format of plaatsing, niet in het beeld. Bevestigt ChatGPT's nuance. |
| NG-04 | TikTok UGC 15 s | Echte hand, echte telefoon, scherm "Finding drivers, Your offer NGN 3,200", groene bevestigknop. Textieltafel, huiskamer. | Ja, fare-scherm in echte hand | 4.22 | Authentiek fare-moment, net boven target. |
| NG-05 | TikTok UGC 17 s | Zelfde opzet, NGN 3,700, "Automatically accept the nearest driver". | Ja, fare-scherm | 7.32 | Zelfde beeld als NG-04, veel slechter resultaat op meer spend. Keyframe verklaart het verschil niet. |
| NG-06 | Google motion 1200x628, Pidgin | Straatscène Lagos met wachtende mensen, chauffeurskaart "₦4,100 Accept", kop "Plans don change? We dey with you", knop "Continue dey waka with inDrive". | Ja, chauffeurskaart met prijs | 2.14 | Pidgin in de kop, situatie-hook, één interface-kaart. |
| NG-07 | Google motion 9:16, Pidgin | Jonge vrouw aan cafétafel met telefoon, één chauffeurskaart "₦4,100 Accept" boven haar, kop "Travel as you like am. Na your price, na your driver." Wit logo op foto. | Ja, prijs én chauffeur in de kop | 1.58 | De enige creative die beide USP's in één regel zegt. Beste IPM van het kwartaal. |
| NG-08 | Meta static 9:16 | Jongeman op markt met motorverkeer, telefoon met lijst van drie chauffeurs (₦4,400 / ₦4,100 / ₦4,600), kop "Calm in the chaos. Get around the city easily." Rechtsonder "Created using AI". | Ja, chauffeurslijst, maar de kop gaat over gemak | 42.05 | Brand-fit op beeld, misfit in de boodschap. Gemak-claim trekt klikkers, geen rijders. |
| NG-09 | TikTok AI video | Alleen een telefoon op groen met drie chauffeurs (Vincent ₦4,300, Jennifer ₦4,100, Damilare ₦3,900) met sterren en Accept. Geen mens. | Ja, chauffeurslijst (waarschijnlijk eindscherm) | 20.22 | Zie opmerking: NG-09/10/12/13 delen dit frame. |
| NG-10 | TikTok AI video | Identiek aan NG-09. | Idem | 3.45 | Het verschil tussen 3.45 en 20.22 zit dus in de eerste seconden, niet in het eindscherm. |
| NG-11 | TikTok AI video | Duidelijk AI-gegenereerde vrouw in regen op stoep, tekstbalk "With inDrive, you choose your fare and your driver." Groene rendering-artefacten links. | Alleen in tekst, geen scherm | 4.58 | Zichtbaar synthetisch, geen app in beeld, toch bijna op target. |
| NG-12 | TikTok AI video | Identiek aan NG-09. | Idem | 15.08 | |
| NG-13 | TikTok AI video | Identiek aan NG-09. | Idem | 3.79 | |
| NG-14 | Meta static 9:16 | Stel in de stad, twee kleine chauffeurskaarten (Vincent 4.6, Damilare 4.9) met "NGN", kop "Choose the driver. Show care.", knop "Start the date early". | Ja, maar klein | 3.86 | Chauffeurskeuze als romantisch gebaar. CTR 11%, CVR 1,25%. |
| NG-15 | Meta motion 9:16 | Celebrity KieKie in pak met groene gele, kop "KieKie is on wahala duty", "Got a wahala? Kiekie and inDrive will fix it". | Nee, niets op het keyframe | 0.49 | Special project = influencer-samenwerking. Verklaart de onmogelijke cijfers: organische/celebrity-attributie, geen performance-creative. Niet vergelijkbaar. |
| NG-16 | Google motion 1200x628, 6 s | Vrouw in auto met gordel, regen op raam, telefoon met kaart, kop "Ride in rainy season and stay dry!". | Nee. Geen prijs, geen chauffeur. | 3.43 | Brand MISFIT volgens Appendix B, toch op target. Bewijst dat brand fit en CPA losstaan, en dat dit concept in Q4 niet mag terugkomen zoals het is. |
| NG-17 | Meta+Google static 1:1 | Vrouw met telefoon thuis, telefoon met kaart, kop "No palava rides", knop "Choose your price", chauffeurskaart "Adeogun 5.0 ₦4,100". "Created using AI". | Ja, prijsknop en chauffeurskaart | 19.64 | Alle juiste elementen, 1:1, gemengde kanalen, slecht resultaat. Formaat/plaatsing weegt zwaarder dan elementen. |
| NG-18 | TikTok UGC 30 s | Chauffeurslijst over een UGC-beeld, ondertitel "I can even choose my driver based on reviews and ratings." | Ja, als overlay | 12.82 | Juiste boodschap, lange video. |
| NG-19 | TikTok UGC 33 s | Videogesprek-opmaak, jongeman praat tegen camera, vrouw in hoek, ondertitel "before you book". | Nee op dit frame | 7.31 | Gesprek-skit, app niet in beeld. |
| NG-20 | TikTok UGC | Telefoon op groen met "₦4100" slider en knop "Offer your price", tekst "and that's exactly". | Ja, fare-scherm (waarschijnlijk eindscherm) | 81.01 | Correct fare-moment, slechtste CPA. Het eindscherm is niet wat faalde. |

### Wat dit verandert aan de analyse

1. **Brand fit verklaart de Q3-resultaten niet.** Zestien van de twintig keyframes tonen een slider, fare-scherm of chauffeurslijst. De drie grootste verliezers (NG-20, NG-08, NG-09) hebben het allemaal. De enige echte misfit (NG-16) haalt target. De jury scoort brand fit als harde poort, niet als prestatievoorspeller. Voor de hypotheses betekent dit: brand fit is de toegangsprijs, de winst zit in formaat, kanaal, lengte en de kop.
2. **NG-01 is geen "mens stelt prijs voor", het is een interface-vergelijking zonder mens.** Links een anonieme app met taxi-checkerpatroon en een vaste prijsbalk, rechts de inDrive-slider. Het samenvoegvoorstel beschrijft het als "jouw prijs tegenover een prijs die springt" en de ChatGPT-brief als "links een Nigeriaanse passagier die een prijsvoorstel invoert". Beide kloppen niet met het beeld. Twee gevolgen. Als H1 "het NG-01-concept" claimt, beschrijf het dan correct. En let op: het taxi-checkerpatroon aan de "slechte" kant zit dicht tegen de regel "geen taxi's negatief afbeelden" aan. In een Q4-versie: anonieme app zonder taxi-symboliek.
3. **Keyframe NG-01 = keyframe NG-03.** Zelfde beeld, CPA 0.97 tegenover 8.44. Het verschil is static tegenover motion in landscape op Google. Dat is het sterkste bewijs in de hele set dat je formaat en plaatsing moet testen bij gelijk beeld, en het onderbouwt een statische H1.
4. **NG-15 is een celebrity-samenwerking (KieKie).** Daarmee is de onmogelijke 269% install-to-ride verklaard: dit zijn geen performance-cijfers maar een special project met andere attributie. In insight 5 kun je nu zeggen waarom je het uitsluit, in plaats van alleen dat het niet klopt.
5. **De vier AI-video's delen één eindscherm.** NG-09 (20.22), NG-10 (3.45), NG-12 (15.08), NG-13 (3.79) eindigen op dezelfde chauffeurslijst zonder mens. Het verschil van factor zes zit dus volledig in de eerste seconden: de situatie-hook (late night, rush hour) versus het verhaal (plans changed, family first). Dit maakt ChatGPT's insight 2 hard en geeft de brief een concrete regel: de situatie in de eerste 2 seconden, het scherm daarna, niet andersom.
6. **"Created using AI" staat rechtsonder op NG-08, NG-11 en NG-17.** inDrive labelt AI-beeld zichtbaar. De brief moet dat voorschrijven, anders levert de AI-creator het zonder en wijkt het af van de huisregel.
7. **Alle statics zetten het zwarte woordmerk linksboven tegen de rand op groen, NG-07 wit op foto.** Precies de richtlijn. De bedragen zijn overal naira: ₦3.200, 3.700, 3.900, 4.100 (vier keer), 4.300, 4.400, 4.600. Chauffeursnamen: Vincent, Jennifer, Damilare, Adeogun, Mateo (NG-06, dat is een kit-placeholder, niet Nigeriaans). De brief hoort een bandbreedte en Nigeriaanse namen uit meerdere groepen voor te schrijven.
8. **Pidgin zit in de kop, niet in een voetnoot** (NG-06 "Plans don change? We dey with you", NG-07 "Travel as you like am. Na your price, na your driver", NG-17 "No palava rides"). De NG-07-regel is de enige in de set die prijs én chauffeur in één adem noemt. Die regel verdient hergebruik.

---

## 2. Reviews (voice of customer)

### Bolt, 50 reviews, thema's met aantal bewijsstukken
- **Geoffreerde prijs wijkt af van wat gevraagd wordt (23).** "when I book a ride that the app says 1500 the drivers still ask me to pay 5k..6k claiming that these prices are old prices." "Bolt issues you a receipt for half of the amount you paid." "I end up not using the app most times and opt for public transportation." Reviewers vragen om "dependable upfront prices".
- **Comfort en gedrag wisselen (33).** "No AC instead u will have to increase the money to get the AC." Reviewers vragen expliciet om "rebooking trusted drivers" en zelf te kiezen of er muziek speelt.
- **Annuleringen op piekmomenten (13).** "Drivers keep cancelling at peak periods." "once they see the pickup distance is far they would cancel."
- **Chauffeurs (3):** klacht over 25% commissie, brandstofkosten. (Let op: het woord "commission" is verboden in onze uitingen; niet citeren.)

### inDrive, 50 reviews
- **Zelf de prijs bepalen wordt gewaardeerd, maar de waarde voelt wisselend (12).** "I enjoy the fact I get to negotiate price with the drivers." Maar ook: Lekki naar mainland bijna ₦30k, en een rit van ₦3.500 die ₦6.900 werd door een bestemmingsfout.
- **Chauffeurs willen leefbare tarieven (7):** lage biedingen, maar twee opties om te verhogen.
- **Goede chauffeurs krijgen lof, slechte ritten missen opvolging (29).** "driven in style and comfort, car superbly neat."
- Verificatie-frictie (WhatsApp-code), kaartdekking.

### Wat dit verandert
- **De sterkste reden om inDrive te proberen staat in de Bolt-reviews, niet in de inDrive-reviews:** de prijs die de app noemt is niet de prijs die je betaalt. Dat is marktpijn die inDrive structureel oplost en die in geen enkele Q3-creative is gebruikt. Dit is de insight-met-bron voor Ngozi ("never overpay") en voor de briefregel "Agree on price before you ride." Zonder concurrentnaam te noemen.
- **"Rebooking trusted drivers" is een letterlijke vraag van Bolt-gebruikers.** Dat is de Choose-your-driver-USP in klanttaal. Bruikbaar als onderbouwing voor elke chauffeurskeuze-hypothese.
- **Annuleren op piekmomenten en bij verre pickups** is de spiegel van "drivers respond to your offer": bij inDrive kiest de chauffeur die wél wil. Dit onderbouwt de rush-hour/late-night-hook zonder snelheid te beloven.
- **Klanten zeggen zelf "negotiate".** Het woord is verboden in uitingen. In de brief dus expliciet: nooit "negotiate", ook niet als quote, wel "agree on price".
- **Voorzichtigheid:** inDrive-reviewers melden zelf prijsverrassingen (bestemmingsfout, lange ritten). Claim dus niet "nooit verrassingen", wel "de prijs die jij voorstelt en de chauffeur accepteert".
- **Brandstof:** zowel Bolt- als inDrive-chauffeurs noemen brandstofkosten. Dat bevestigt update 2 vanuit de markt en pleit voor de toon "een prijs waar jullie allebei ja op zeggen", niet "goedkoop".

---

## 3. Concurrentie-advertenties

- **Bolt, 22 betaalde ads, drie boodschappen:** "Pay up to 40% less for your first 3 rides! Capped at NGN 3,000" (5 ads, statics 9:16 en 6 s video's); "Get the Bolt app for moments you need to hurry, and moments you plan ahead for" (9 video's, 20 tot 35 s); "Make your life easier. Get Bolt" (4 video's, 55 tot 66 s); "Whatever the plan. There's a Bolt ride for it" (4, static en 6 s).
- **Uber: nul advertenties in de bibliotheek.** Consistent met update 1 (Uber weg per 2 september).
- **Lagride: alleen organische LinkedIn-posts** (elektrische voertuigen, events, 50% korting voor eventgasten). Geen performance-advertenties.

### Wat dit verandert
- **Update 3 is geverifieerd en gepreciseerd:** 40% korting op de eerste drie ritten, gemaximeerd op ₦3.000. Dat maximum staat niet in de update. Het betekent dat Bolt's korting op een rit van ₦4.100 effectief ₦1.640 is, en op een lange rit nooit meer dan ₦3.000. Je hoeft er niet tegenin te bieden; wel kun je in de updateregel zeggen dat je de cap kent en daarom bij "jij stelt de prijs voor" blijft.
- **Bolt bezet gelegenheid en gemak** ("moments you need to hurry", "whatever the plan", "make your life easier") met lange video's. Dat is precies de "Arrive fresh"-hoek. Onze data zegt bovendien dat lang verliest. Niet daar gaan zitten; prijs en chauffeurskeuze zijn onbezet.
- **Update 1 wordt sterker:** er is geen Uber-communicatie meer. Voormalige Uber-gebruikers (premium, "betere auto's") zijn alleen door Bolt-korting aangesproken. Dat is het argument voor een Ngozi/Comfort-hypothese met "Comfort at a price you set", zoals het samenvoegvoorstel wil.

---

## 4. Correcties en aanvullingen op de twee stukken

**Op de ChatGPT-handoff**
- Insight 2 nuance ("creatorvideo's eerst bekijken") is nu gedaan: NG-18 toont de chauffeurslijst als overlay met de juiste zin, NG-19 toont een videogesprek zonder app. Ze zijn niet generiek, ze zijn lang (30-33 s) en de app komt laat of niet. De kwalificatie "generic storytelling" kan vervangen worden door "30 s+ met het inDrive-moment laat of afwezig".
- Insight 5: NG-15 is een KieKie-celebrity-project. Dat is de verklaring, niet "meetfout".
- Briefcompositie "links een passagier die een prijs invoert": NG-01 heeft geen mens. Wil je de mens erin (NG-07 bewijst dat dat ook werkt), zeg dan dat het een nieuw concept is, geen NG-01-herhaling.
- "Choose your ride" in de supporting line: terecht door het samenvoegvoorstel afgewezen; "Choose your driver" of de NG-07-regel.

**Op het samenvoegvoorstel**
- "Split screen: jouw prijs tegenover een prijs die springt": NG-01 toont een vaste prijsbalk tegenover een slider, geen springende prijs. Springende prijs is een goede Q4-hook (Chidi's pijnpunt én de Bolt-reviews), maar noem het dan een doorontwikkeling.
- Vraag "kijk even naar de preview van NG-01": gedaan, zie tabel.
- Ngozi met "Comfort at a price you set": de Bolt-reviews ("no AC unless you pay more", "rebooking trusted drivers") en het Uber-gat geven daar nu een bron voor die in de brief gevraagd wordt ("competitor ad or trend").
- Meta-zwaar budget: de visuele audit steunt dat. Van de vier Meta-creatives had er geen één de combinatie static + fare-slider + situatie-hook die op Google won. NG-08 en NG-17 hadden de elementen maar een gemak-kop of 1:1 op gemengde kanalen. Meta is dus niet "bewezen slecht", het is onbeproefd met het winnende recept.

---

## 5. Concreet voor de creative brief (veld voor veld)

- **Hypothesis / why:** verwijs naar het NG-01=NG-03-paar (zelfde beeld, 0.97 tegenover 8.44) als bewijs dat static met een grote slider het veiligste formaat is, en naar NG-07 als bewijs dat een mens plus één kaart ook werkt op 9:16.
- **Who is in it:** Nigeriaanse persoon, telefoon in hand, situatie herkenbaar (NG-06 straat, NG-07 café, NG-08 markt). Niet alleen een telefoon op groen (NG-09/12/20-eindscherm-look).
- **The inDrive moment:** slider of fare-kaart als grootste element, bedrag in naira tussen ₦3.200 en ₦4.600 (waargenomen bandbreedte), chauffeursnaam Nigeriaans en uit een andere groep dan de passagier (Tunde/Ngozi/Musa in plaats van kit-placeholder "Mateo"). Bij video: situatie in seconde 0-2, scherm vanaf seconde 2, minimaal 4 s leesbaar; het eindscherm telt niet (gedeeld eindscherm NG-09/10/12/13 verklaart niets).
- **Scene by scene / headline:** Pidgin in de kop is bewezen (NG-06/07), niet alleen als variant. De NG-07-regel "Na your price, na your driver" dekt beide USP's; een Engelse zusterregel: "Your price. Your driver."
- **Must not appear:** naast de brieflijst: taxi-checkerpatroon aan de "andere app"-kant; het woord "negotiate" ook niet als klantquote; "commission"; geen gemak- of comfort-kop boven het prijsmoment (NG-08-fout); geen kit-placeholder-namen; dollarteken.
- **Toevoegen aan de brief:** regel "Created using AI" klein rechtsonder in Poppins Regular, zoals NG-08/11/17. Logo zwart linksboven tegen de rand op groen; wit alleen op foto.
- **Music and voice:** uit de keyframes niet af te leiden; brief en guidelines blijven leidend (Afrobeats, geen Zuid-Afrikaanse muziek).

---

## 6. Voor "How you worked" (één regel, Engels)

Used the Loudbox MCP (`creativeLibrary.detail`, `get_creative_preview`, `voiceOfCustomer.dashboard`, `creativeLibrary.list` for competitors) to look at all 20 Q3 keyframes and 100 app-store reviews; this showed that 16 of 20 creatives already had a price or driver screen, so brand fit does not explain Q3 results, that NG-15 was a celebrity project, that four AI videos share one end screen, and that Bolt's 40% offer is capped at NGN 3,000.

Gevangen AI-aanname, bruikbaar als tweede voorbeeld: twee eerdere AI-analyses beschreven NG-01 als "een passagier die een prijs invoert" respectievelijk "een prijs die springt"; het keyframe toont een interface-vergelijking zonder mens en zonder springende prijs. Gecorrigeerd na het bekijken van de preview.
