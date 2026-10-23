# Induik 5: Measurement link, quiz to day 7 (one woman, one ID)

**Answer.** Yes, one woman can be followed from quiz to day 7, but only on a first-party key that we create ourselves: her **email**, captured in the quiz and used again for the TestFlight invite and the in-app login. TestFlight itself passes no attribution, referrer or URL parameter into the app (no source found that says it does), and public-link testers are anonymous to the developer, so **invite by email, not by public link**.
The scheme survives the move to the App Store without a rebuild of the funnel, because it does not depend on TestFlight. What the App Store adds later (deferred deep links via an MMP, SKAN/AdAttributionKit) is a bonus for paid, not a requirement for the 500.

Date of research: 2026-10-23. Every claim has a URL. "Unverified" = not found on an official page. "Inference" = our reasoning from a cited page.

---

## 1. TestFlight limits (verified)

| Topic | What the source says | Source |
|---|---|---|
| External testers | "up to 10,000 external testers per app" | https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers |
| Internal testers | Up to 100 team members with an App Store Connect role | https://developer.apple.com/testflight/ |
| Builds | "share up to 100 builds"; testers on up to 30 devices | https://developer.apple.com/testflight/ |
| Build expiry | "You can test a build for up to 90 days." After that the build "becomes unavailable for testers" | https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview |
| After expiry (tester view) | Tester cannot open the beta build and must install the App Store version | https://testflight.apple.com/ |
| Beta App Review | First build added to an external group goes to App Review; later builds "may not require a full review". One build per version in review at a time; max 6 submissions per 24 h | https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview , https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers |
| Required metadata | Beta app description and beta app review information are required for external testers | https://developer.apple.com/testflight/ |
| Groups | External group requires an internal group first; multiple groups, different builds per group | https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers , https://developer.apple.com/testflight/ |
| Public link limit | Optional tester limit per link, "a number between 1 and 10,000"; link can be disabled any time; filter only by device/OS criteria | https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers |
| Public link sharing risk | "anyone can share this link, so testers could potentially join your testing group even if you do not invite them directly" | https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers |
| Data per tester, email invite | Name, email, installation date, sessions, crashes shown in App Store Connect | https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers |
| Data per tester, public link | Shown as **anonymous**; installation date, sessions, crashes still shown; excluded from CSV export | https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers , https://developer.apple.com/help/app-store-connect/test-a-beta-version/view-tester-information |
| CSV export | Contains first name, last name, email only; **not** status, sessions, crashes | https://developer.apple.com/help/app-store-connect/test-a-beta-version/view-tester-information |
| Metric delay | Tester metrics only for installed testers, up to 24 h delay | https://developer.apple.com/help/app-store-connect/test-a-beta-version/view-tester-information |
| Public link funnel metrics | Views in TestFlight, Accepted, Didn't meet criteria, Didn't accept (with reason), 30-day window | https://developer.apple.com/help/app-store-connect/test-a-beta-version/view-tester-information |
| Feedback and crashes | Screenshot feedback with markup; crash reports with optional tester context | https://developer.apple.com/testflight/ |
| Beta replaces App Store version | If the App Store version is installed, "the beta version of the app will replace it" | https://testflight.apple.com/ |
| App Analytics vs TestFlight | App Analytics excludes sales metrics from TestFlight builds. Whether App Analytics sessions include TestFlight: **unverified** | https://developer.apple.com/help/app-store-connect/measure-app-performance/differences-in-reporting-tools |
| Referrer / attribution through TestFlight install | No Apple page found that offers any referrer or campaign parameter on a TestFlight install. **Unverified** (treat as: none) | n/a |
| SKAdNetwork with TestFlight | For advertisers "the answer is no": the advertised app must be live in the App Store (Branch FAQ, secondary source) | https://help.branch.io/faq/docs/can-skadnetwork-be-tested-via-testflight |
| Universal links | apple-app-site-association is fetched via Apple's CDN from iOS 14; the "developer" alternate mode (direct fetch) only works for apps signed with a development profile | https://developer.apple.com/documentation/xcode/supporting-associated-domains , https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.associated-domains |
| Universal links in a TestFlight build | Inference: a TestFlight build is distribution-signed, so it uses the normal CDN path; universal links should work if the AASA file is public. No Apple page states it explicitly: **unverified** | as above |
| Deferred deep link on TestFlight | Apple forum report of an empty deferred deep link on TestFlight, no official answer. **Unverified**, plan without it | https://developer.apple.com/forums/thread/83389 |

**What TestFlight measures for us (with email invites):** per woman, install date, sessions, crashes, feedback. Not: "opened on day 7" as an exportable field (sessions are not in the CSV). So TestFlight is a cross-check, not the D7 source.

---

## 2. Options to link quiz to app user

| Option | How | Verdict | Source |
|---|---|---|---|
| A. Email as key (recommended) | Quiz captures email; same email gets the TestFlight email invite; app login with the same email (one-time code or magic link) | Deterministic, works in TestFlight and App Store, no SDK needed | Tester email visible for email invites: https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers |
| B. Web2Wave user_id via deep link page | Web2Wave link `https://quiz.YOURDOMAIN.com/deeplink?user_id={GUID}&email={EMAIL}` sends user_id + email into the app via custom URL scheme, **if the app is already installed**; user must "install the app via the link and then REVISIT the link" | Works as a second click after install. Its auto-redirect points to the App Store, not TestFlight, so during beta the install step needs our own instruction (inference) | https://docs.web2wave.com/docs/pass-subscription-from-web2web-to-app |
| C. Web2Wave deferred deep link `identify()` | SDK call on first open matches device to web session by IP + device model / screen size / timezone, **last 48 hours only**; returns no ID if ambiguous | Probabilistic. Breaks if application to approval to install takes more than 48 h, or on a different device. Use as convenience, never as the key. TestFlight compatibility: unverified | https://docs.web2wave.com/docs/index |
| D. MMP (AppsFlyer, Adjust, Branch) | Web2Wave: "Most teams get that user_id through a mobile measurement partner" via install deep link | No value in beta: SKAN needs an App Store app (Branch), deferred deep link on TestFlight unverified. Consider after public release for paid | https://docs.web2wave.com/docs/index , https://help.branch.io/faq/docs/can-skadnetwork-be-tested-via-testflight |
| E. Invite code typed in onboarding | Quiz/approval email shows a short code; she enters it in onboarding | Good fallback if email login is not built; adds friction (inference) | n/a, design choice |

Web2Wave also stores quiz answers per user_id and exposes them via API (our Web2Wave MCP has `web2wave_get_user_properties` and `web2wave_export_quiz_answers`), so the quiz profile can be joined to the app user by user_id or email.

---

## 3. Recommended ID flow

```
1. Quiz (Web2Wave)            -> w2w_user_id created; email + explicit health-data consent captured
2. Application / approval     -> our sheet/CRM: axisx_id = w2w_user_id, email, quiz type, source (utm)
3. TestFlight EMAIL invite    -> same email added to external group (not public link)
4. Install                    -> App Store Connect shows email + install date (cross-check)
5. App onboarding login       -> email + one-time code (or magic universal link carrying a signed token)
                                 backend maps email -> axisx_id; app stores axisx_id
6. App events                 -> every event keyed on axisx_id: onboarding_complete (= day 0),
                                 app_open (with date), feedback_given, report_pdf_created
7. D7                         -> app_open on calendar day 7 after onboarding_complete
                                 (count per quiz type and per source)
8. Public release             -> same app login, same events; add App Store link + optional MMP/AAK for paid
```

**Day 7 definition to fix now:** day 0 = date of `onboarding_complete` in her local time zone; retained D7 = at least one `app_open` on day 7 (not "day 7 or later"). Write it in the meetplan so the 300 is counted the same way every time.

**Minimum build in the app (founder's dev):** email login, one analytics tool keyed on axisx_id (first-party or a product analytics tool), 4 events above. Without the login step there is no deterministic link and D7 per source cannot be shown to the investor.

---

## 4. What breaks where

| Step | What can break | Mitigation |
|---|---|---|
| Quiz to invite | She uses a different email for Apple ID / TestFlight than in the quiz | The invite goes to the quiz email; the in-app login uses the quiz email regardless of her Apple ID, so the app link holds. Only the App Store Connect cross-check breaks (inference) |
| Public link used anyway | Testers anonymous in App Store Connect; link can be forwarded | Use email invites; if a public link is used for speed, the in-app email login still links her (inference) |
| identify() fingerprint | 48 h window, shared IP/device model, Safari without device model | Only as auto-fill; email login is the truth |
| 90-day build expiry | Beta stops opening after 90 days | 4-6 weeks to release is inside 90 days; each new build restarts the clock (testflight-overview) |
| Beta to App Store | Beta replaces App Store version (testflight.apple.com); whether login/keychain data carries over between beta and App Store install: **unverified** | Server-side axisx_id, so re-login with email restores the link |
| TestFlight to paid attribution | No SKAN/AAK on TestFlight (Branch FAQ) | Paid attribution only after public release; for the 500 use utm on quiz + email key |
| Metrics delay | App Store Connect tester metrics up to 24 h late | Use own app events for D7 |

---

## 5. Privacy

- **Health data.** Perimenopause symptom answers relate to "the physical or mental health of a natural person" (GDPR Art. 4(15)) and fall under Art. 9(1) "data concerning health". Processing needs, among the options, "explicit consent ... for one or more specified purposes" (Art. 9(2)(a)). So the quiz needs an explicit, separate consent checkbox naming the purpose (personalising the app, linking quiz answers to her app account). Sources: https://gdpr-info.eu/art-4-gdpr/ , https://gdpr-info.eu/art-9-gdpr/
- **ATT.** Apple defines tracking as linking data from your app "with user or device data collected from other companies' apps, websites, or offline properties for targeted advertising or advertising measurement purposes", or sharing with data brokers. Linking our own quiz to our own app for product use is, by inference, not tracking and needs no ATT prompt. It becomes tracking if a third-party SDK combines the data with other companies' data for ads, which Apple says developers are responsible for. Source: https://developer.apple.com/app-store/user-privacy-and-data-use/
- **Ad pixels on the quiz.** Do not send quiz answers (symptoms) to Meta/TikTok pixels; send only neutral events (quiz_start, quiz_complete). Inference from Art. 9 plus Apple's tracking definition; platform-specific health-data rules: unverified here.
- **TestFlight data.** Apple shares crash logs, name, email, usage and feedback with the developer, who may use it only to improve the app and not share it with third parties (https://testflight.apple.com/). Inference: do not use the App Store Connect tester export as a marketing list; use our own consented quiz email.
- **Processor.** Web2Wave hosts the quiz answers; a data processing agreement with Web2Wave: unverified, check before launch.

---

## 6. Risks (short)

1. Founder's developer must build email login + 4 events before the first invites; without it D7 per source is not measurable. Highest risk.
2. Manual email invites for 500 women are work; App Store Connect API for adding beta testers exists in our knowledge but was not verified in this research.
3. Public link temptation for speed loses identity in App Store Connect (anonymous) and lets the link spread to people outside the target group.
4. Health-data consent missing or vague invalidates the link between quiz answers and app behaviour for EU/UK users.
5. Deferred deep linking and SKAN are not available as a basis during beta; do not promise them in the plan before public release.
