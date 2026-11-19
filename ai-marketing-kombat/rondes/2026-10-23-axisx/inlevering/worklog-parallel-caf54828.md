# Work log (exported from the Claude Code session)

## 13:58 UTC · User

volgens mij heb ik ergens een hook bouwer en taste skill misschien in de E: repo .. kan je die er even bijpakken en de brief en de Strategische context erbij halen en mij even wat betere hooks voorstellen dan de From feeling lost in your own body to feeling in control again

gebaseerd op verschillende persona's en afgestemd op het doel om ABM op communities en direct communication op community leaders te doen?


**Model (13:58 UTC):**

Ik zoek eerst de hook-bouwer en taste-skill op E: en de brief en de strategische context.


- tool `PowerShell`: Search E: for hook and taste skill folders

- tool `PowerShell`: List AxisX round files

- tool `PowerShell`: List hook and taste skill files

- tool `Read`: E:\PerformanceOps\AxisX_Founding_500_strategisch_context_extract.md

- tool `Read`: E:\PerformanceOps\rondes\2026-10-23-axisx\brief\Brief - Stage 2.pdf


**Model (13:58 UTC):**

Gevonden: `hook-generator` (social-media-skills), `viral-hooks` (in Hugo's library) en `taste-skill`. Ik lees ze plus de regels en het doelgroeponderzoek.


- tool `Bash`: Read hook skills and start of taste skill

- tool `Bash`: Read rules, audience research, campaign input


- tool `Bash`: Check existing personas and hook archetypes


- tool `Bash`: Check format of AI error log


**Model (13:59 UTC):**

Ik schrijf de hooks naar een bestand (Engels, inleverklaar) en log de gevonden AI-fout.


- tool `Write`: E:\PerformanceOps\rondes\2026-10-23-axisx\hooks.md

- tool `Bash`: Append caught AI error to log


**Model (14:00 UTC):**

Geschreven voor: jou als campagnemateriaal. De teksten zelf richten zich op community-leiders en hun leden, en zijn in het Engels.

Alles staat in [hooks.md](rondes/2026-10-23-axisx/hooks.md). Ik heb `hook-generator` gebruikt voor het korte formaat van LinkedIn-posts en `viral-hooks` uit de map van Hugo's voor archetypes, de drielaagse hook (beeld, gesproken tekst, tekst op scherm) en de anti-patronen. De taste-skill heb ik niet gebruikt: die gaat over het ontwerp van landingspagina's. Hij komt van pas bij de webfunnel, niet bij hooks.

**Waarom "From feeling lost…" niet werkt als hook:** elke wellness-app kan die zin gebruiken. Hij noemt niet wat AxisX echt anders doet: één persoonlijk systeem en het rapport voor de arts na twee weken. Hij richt zich ook tot de verkeerde lezer. Bij ABM op communities is de eerste lezer de moderator, en die vraagt zich af waarom ze het vertrouwen van haar leden aan jou zou geven. Houd de zin als positionering op de landingspagina.

**Wat erin staat:**
1. **Hooks voor community-leiders**, per type: subreddit-moderator, Facebook-groep of een community zoals The Latte Lounge, nieuwsbriefschrijver of podcastmaker, coach of praktijk, en Peanut-groep. Elke hook geeft iets terug: gereserveerde plekken, een geanonimiseerde samenvatting per thema, een Q&A op hun voorwaarden en geen verplichting om iets te onderschrijven. Mijn favorieten:
   - *"Founder Q&A request: you set the rules"* voor Reddit
   - *"A two-week summary your clients can take to their GP"* voor coaches
2. **Hooks voor leden, voor 5 persona's** binnen het segment uit de brief:
   - de maand waarin alles veranderde
   - de planner
   - al drie keer bij de huisarts geweest
   - zet zichzelf als laatste
   - de scepticus

   De sterkste is P3: *"Two weeks of logging. One page. Walk into your appointment with evidence, not 'I just don't feel like me'."* Die raakt het eerste moment waarop de app waarde levert.
3. **Referral-hooks** die de vriendin geen medisch label geven.
4. **Testopzet:** leiders beoordelen we op het aantal keer dat ze ja zeggen per founder-uur. Leden beoordelen we per persona op onboarding en of ze de app op dag 7 openen, niet op CTR.

**Gevangen AI-fout:** ons eigen doelgroeponderzoek raadde *"Is this perimenopause?"* aan als hook. Die richt zich op vrouwen die het nog niet herkennen, en die sluit de brief uit voor de eerste 500. Ik heb dit toegevoegd aan [ai-fouten.md](rondes/2026-10-23-axisx/ai-fouten.md).

**Nog na te gaan:**
- De regel "They asked for order, not more advice" is onze lezing van de brief, geen citaat van de founder.
- De aantallen bij de beloningen staan nog als [placeholder], want daarover is nog niets besloten.


## 14:02 UTC · User

Je hebt de hooks staan he? Volgensmij iser een pannellid die hier wel even de selectie uit kan maken


- tool `Bash`: Read panel definitions


**Model (14:02 UTC):**

Savannah Sanchez is de aangewezen persoon: haar vraag in het panel is "would anyone stop scrolling in the first two seconds?". Ik lees eerst haar profiel.


- tool `Bash`: Read Sanchez profile and panel log tail



- tool `Bash`: Append Sanchez selection and panel log entry


**Model (14:03 UTC):**

Savannah Sanchez heeft de selectie gemaakt (gesimuleerd op basis van haar publieke werk). Ze toetste elke hook op vier punten: landt hij binnen 3 seconden, werkt hij zonder geluid, kan een echt persoon hem zeggen, en is het eerste beeld anders dan bij de andere varianten. Haar selectie staat in sectie 6 van [hooks.md](rondes/2026-10-23-axisx/hooks.md) en de review is gelogd in [panel-log.md](rondes/2026-10-23-axisx/panel-log.md).

**Deze 4 hooks voor leden gaan door, elk op een andere drijfveer:**
1. *"Your doctor has ten minutes."* met op het scherm *2 weeks. 1 page. For your GP.* Dit is de oude P3, ingekort omdat de lange versie te traag was voor 3 seconden. Deze werkt het sterkst omdat hij naar het rapport voor de arts wijst, het eerste moment waarop de app waarde levert.
2. *"Sleep, mood, memory, cycle. All different in the same month."* Gericht op het heetste subsegment uit de brief, en hij werkt volledig zonder geluid.
3. *"You've said 'I'm fine' for months."* Werkt alleen als een echte vrouw hem zegt, en dat is precies de bedoeling.
4. *"You track your runs, your sleep and your money."* Spreekt de planners aan bij wie het geleidelijk begint. Dit is de zwakste van de vier, maar hij brengt variatie in het cohort.

**Wat eruit gaat:**
- De vage hooks gaan eruit: "another article", "could last years" en "someone you love".
- De hooks voor sceptici verhuizen naar de koptekst van de landingspagina.
- "Founding 500" komt als afsluiter aan het eind, niet als opening.

**Productieregels:**
- Echte vrouwen die in de camera praten, met de founder voorop. Ondertiteld en 60 tot 90 seconden lang, passend bij 40+. Geen AI-avatar.
- 8 openingen: 4 hooks met elk 2 verschillende eerste beelden, de rest van de video blijft gelijk.
- Per community een hook-log bijhouden.

**Community-leiders:** daar is haar blik zwakker. Ze houdt Reddit (*you set the rules*), de coaches (*two-week summary*), de nieuwsbrieven (*60 women*) en de groepsbeheerders. Peanut valt af. Het aantal gereserveerde plekken per community gaat van 50 naar 10, in lijn met de schaarste per community die Sutherland in panelreview 3 adviseerde.

**Dit moet nog van de founder komen:** de eerste zin van haar eigen video. Die gaat over haar eigen verhaal, en dat hebben we niet. Die laat ik bewust open, want die moet niet door AI geschreven worden.


## 14:20 UTC · User

Ja dat wordt de laatste slide in het deck aan de founder: geef hier alsjeblieft jouw sterkste zin passend bij wat je gezien hebt.


- tool `Bash`: Check deck structure in submission file


- tool `Write`: E:\PerformanceOps\rondes\2026-10-23-axisx\slide-laatste-founder.md

**Model (14:20 UTC):**

Geschreven voor: de founder, als laatste slide van het deck.

De slide staat in [slide-laatste-founder.md](rondes/2026-10-23-axisx/slide-laatste-founder.md). Ik heb haar zin bewust niet zelf geschreven. De slide vraagt haar om die zin, met drie vragen die haar helpen hem te vinden:

**Titel:** *The one line we can't write for you*

- **Opening:** "Every opening in this plan starts with a real woman. The first one should be you."
- **Wat we zagen:** een maand waarin alles verandert, aantekeningen op vijf plekken, te lang "I'm fine" zeggen, en twee weken loggen waar een arts eindelijk iets mee kan. Dat sluit aan op de vier hooks die door Sanchez zijn gekomen.
- **Drie vragen:**
  1. Welk moment liet je beginnen met AxisX?
  2. Wat had je toen nodig en had je niet?
  3. Wat had je willen horen?
- **Drie regels voor haar zin:** over haarzelf en niet over de app, binnen 3 seconden uitgesproken, en iets wat alleen zij kan zeggen.
- **Beeld:** één lege regel in het midden, verder niets.

**Twee keuzes die je moet weten:**
- Vraag 1 is neutraal gesteld ("What moment made you start building"). We weten niet of de founder het zelf doormaakt of dat het om iemand dicht bij haar gaat. Om die reden staat er in vraag 3 ook "or to her".
- In de sprekersnotitie staat waarom de zin leeg blijft: een model schrijft iets dat glad klinkt, en vrouwen in deze communities horen dat het niet van haar is. Daarmee is de slide ook bewijs voor het onderdeel "how we worked".

**Let op het aantal slides:** het deck mag 5 tot 8 slides hebben. Deze slide telt mee, dus houd er rekening mee bij het bouwen. Er is nog geen deck. In [inlevering.md](rondes/2026-10-23-axisx/inlevering.md) staat het deck nog als open punt.


## 14:26 UTC · User

Ja eens dat we dit in de laatste slide meenemen om de founder te activeren.


- tool `Bash`: Read submission checklist header

- tool `Edit`: E:\PerformanceOps\rondes\2026-10-23-axisx\inlevering.md

**Model (14:27 UTC):**

Genoteerd: de slide "The one line we can't write for you" wordt de afsluiter van het deck. Ik heb het besluit vastgelegd onder het deckpunt in [inlevering.md](rondes/2026-10-23-axisx/inlevering.md), met een verwijzing naar [slide-laatste-founder.md](rondes/2026-10-23-axisx/slide-laatste-founder.md). Daar staat ook bij dat deze slide meetelt in de 5 tot 8 slides.

Dan blijven er 4 tot 7 slides over voor de verplichte onderdelen: hoe we de brief lazen, de strategie voor de eerste 500, het geld ($5k en $50k) en de bronnen.

