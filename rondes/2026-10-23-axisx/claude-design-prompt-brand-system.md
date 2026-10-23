# Claude Design prompt: AxisX brand system and design system

Paste everything below the line into Claude Design. Fill the [brackets] first if you have the answer; otherwise leave them and Claude Design will propose and label the choice as an assumption.

---

You are building a brand system and a UI design system for AxisX, and a campaign layer on top of it called "The Founding 500". Work in this order: 1) brand foundations, 2) design tokens and components, 3) campaign layer, 4) the four deliverables listed at the end. Label every choice you could not verify as "assumption". Do not invent facts about the company.

## 1. What AxisX is

- iOS app for women's hormonal health. Perimenopause is the entry point; broader hormonal health later. Closed beta now, public App Store release expected 4 to 6 weeks after mid October 2026.
- How it works: a woman describes what has changed in her own words, one sentence. The app builds her a personal system: what to track, habits, reminders, dashboards, and it rebuilds as new data comes in. After about two weeks it produces a one-page summary she can take to her doctor.
- Positioning line: "A personal system for understanding and managing your changing hormonal health, built around your life." Internal positioning: an app for women who think. Core creative idea: "No two systems alike".
- Audience: women 39+ in the UK, US and Northern Europe who already recognise that perimenopause has started and are looking for support. Many are planners who track their runs, sleep and money but not this. About 15 to 20 percent are sceptical of AI. They are tired of fragmented advice, of saying "I'm fine", and of ten-minute doctor appointments where they cannot explain what changed.
- Competitors and what to avoid looking like: Flo (pastel pink, cycle app, owns "Perimenopause Score"), Balance by Dr Louise Newson (clinical, doctor-led), BetterMe (fitness aesthetics), thePause, Peri Track, MenoPal. The Meta Ad Library in this category is full of pseudo-doctor pages selling supplements and bracelets. AxisX must be instantly distinguishable from all of that.
- Founder: one woman, 60 interviews before writing code. She is the first face of the brand. Honest, direct, not glossy.
- Hard red lines: the app does not diagnose, treat, cure or prescribe and does not replace a doctor. Never use those four verbs as promises. No health-outcome claims in headlines. Beta status is always stated honestly.

## 2. Brand foundations to deliver

Brand personality (use these five words as the anchor): clear, honest, capable, warm, grown-up. Not: cute, pink, clinical, girlboss, wellness-guru, tech-bro.

Tone of voice: short sentences, plain English, second person, no exclamation marks, no medical jargon, no em-dashes. She talks like a smart friend who happens to be organised. Give five do and five don't example lines.

Visual territory to explore: "the notebook that finally makes sense". A quiet, structured, almost editorial look: records, pages, timelines, one-page summaries, handwritten input turning into typeset order. Real women photographed on their phones, in kitchens, parked cars, waiting rooms. Not stock, not AI-generated people, not illustrations of uteruses, flowers, waves or moons.

Colour: existing placeholder palette from the pitch deck, treat it as a starting point, not as fixed: ink #1d1b26, accent #7a3e9d (deep plum), soft #f4eef8, line #ddd3e6, muted #5d5a6b. Decide whether deep plum is distinctive enough against Flo pink and Balance teal, and propose one alternative direction. Requirements: WCAG AA for body text on all backgrounds, a dark mode, one signal colour for "your reminder" that is not red (red reads as alarm or blood in this category). [Insert the real app palette here if the founder has one; otherwise mark the palette as an assumption.]

Typography: one highly legible sans for UI and data (variable weight, good numerals, works at 14 px on iPhone), and optionally one warmer serif or humanist face for headlines and the founder's voice. The audience is 39+; minimum body size 16 px on web, 15 pt in app. Show the type scale.

Logo and wordmark: do not redesign the AxisX logo unless asked. [Insert logo file or link.] Define clear space, minimum sizes and a mono version. If no logo exists yet, propose a wordmark that works as an app icon at 60 px.

Distinctive asset to own: the "system card". A compact card that shows one woman's system: 3 things she tracks, 2 habits, 1 reminder time, and "doctor page on day 14". This card is the repeatable brand asset across app, landing pages, social posts and ads. Design it so it is recognisable at thumbnail size and in a 9:16 video frame.

## 3. Design system (tokens and components)

Deliver tokens for colour, type, spacing (4 pt base), radius, elevation and motion. Then components, mobile first, iPhone-sized:

- Free-text input "Tell it like you'd tell a friend" (the product-native starting point: large, calm, one field).
- Quiz screens: single choice, multi choice, age bands, progress indicator for 8 screens, and a "later list" state for people who do not qualify, worded kindly.
- System card (see above) in three sizes: in-app, landing hero, social thumbnail.
- Dashboard tiles for tracked items and a simple 14-day timeline.
- Reminder component.
- Doctor summary: a one-page document layout, print-ready A4 and US Letter, black and white safe. This is the product's hero output; make it look like something a GP respects.
- Honest box: a standard disclosure block ("AxisX is in closed beta on iPhone. It doesn't diagnose or replace your doctor. We use AI to build your system; you decide what goes in.").
- Consent checkboxes for health data (GDPR article 9) and for email, visually separate.
- Buttons, forms, toasts, empty states, error states.
- Landing page template per community with a slot for an invite code and a slot for a founder video.
- Email templates: approval ("Your place is held"), founder welcome, day 3 / 7 / 14 feedback prompts.

## 4. Campaign layer: The Founding 500

Campaign name: "The Founding 500". Sub line: "No two systems alike". The internal project name "First 500 Systems" never appears publicly.

Mechanics the design must express:
- Place numbers: "Founding member #137 of 500". Design the badge and how it appears in app, in email and as a shareable image.
- Places are "held" for a community, never "left" or "remaining". Example: "[10] places held for [community name]".
- Each member gets 3 invites "for a woman like you". Design the invite card.
- Offer line: "Free during beta, founding price held for launch. In return: tell us what we haven't accounted for."
- Communities and partners first: the first reader is often a moderator, group admin, newsletter writer or menopause coach. Provide a one-page partner sheet layout and a co-branded landing header where the community's name sits next to AxisX without touching the logo.

Video and social formats (real women, founder first, captions always on, 60 to 90 seconds, 9:16 and 1:1):
- Title-safe zones, caption style, lower third for first name and "Founding member #n".
- First-frame text treatments for these four hooks: "2 weeks. 1 page. For your GP." / "4 changes. 0 connections." / "Write down what isn't." / "Tracked everything. Except this."
- Carousel template "Her system: tablet at 7, protein at 12, note at 17:00", built on the system card.
- Deck slide template consistent with the system, including a near-empty final slide with one blank line, like the first page of a notebook, no logo, no app screen.

Compliance built into the templates:
- No question about her health in ad copy ("Are you in perimenopause?" is not allowed under Meta personal attributes rules). Templates should not have a slot that invites that.
- No before/after, no body imagery, no named-doctor advertorial look.
- Beta badge visible on every acquisition surface until public launch; make it easy to swap to "Now on the App Store" without redesign.

## 5. Must not appear anywhere

Pink pastel palette, flowers, moons, waves, butterflies, hourglasses, uterus illustrations, hot flush flames, AI-generated faces, stock photos of laughing women in white, medical cross or stethoscope icons, scores or percentages that look like a diagnosis, the words diagnose, cure, treat, prescribe as promises, exclamation marks, em-dashes, the phrase "feel like yourself again".

## 6. Deliverables

1. Brand book: personality, voice with examples, colour, type, imagery direction, the system card as distinctive asset, dos and don'ts.
2. Design system file: tokens plus the components in section 3, light and dark, with a short usage note per component.
3. Campaign kit: Founding 500 badge, invite card, partner sheet, landing template, four first-frame treatments, carousel template, deck template, email templates.
4. One page "assumptions and open questions" listing every choice that needs the founder's confirmation (real palette, logo, app typography, whether plum stays).

Explain your reasoning for the two or three biggest decisions (colour direction, type pairing, system card form) in one paragraph each, then build.
