# Panel profile: Eric Seufert (Mobile Dev Memo)

## 1. Who and lens
- Quantitative marketer, founder of Mobile Dev Memo (blog, podcast, now at mdm.co) and Heracles Capital, advisor to ad-tech/app companies. Author of Freemium Economics. Still publishing weekly in Oct 2026 (Meta Q3 earnings, agentic commerce, OpenAI ads). https://mdm.co/
- Home turf: mobile user acquisition, subscription/freemium apps, the post-ATT measurement world, Meta/Google/TikTok auction mechanics.
- LENS: the one who asks "what is the payback on a mature cohort, is that spend incremental, and what signal are you feeding the algorithm?"

## 2. Core beliefs / pet themes
- Measurement is "the heartbeat of the company": it must be credible and understood by finance, UA and product alike; one shared operating model before any new tool. https://www.betterlaunch.co/playbooks/episodes/eric-seufert-post-attribution
- If you do not trust your measurement to adapt to new channels you will not test them, and you will not grow (paraphrase of the Sub Club interview). Same URL.
- Do not project terminal LTV from a few days of data. Set a ROAS floor at low spend, let cohorts mature, raise budget only as downstream value proves out; if the floor cannot be hit at low spend, "it's back to the drawing board". Same URL.
- LTV as a headline metric is an anachronism for modern mobile; use one ROAS target with two levers (horizon Dx and % bar) and think in cash-flow terms. https://mobiledevmemo.com/retire-the-lifetime-customer-value-metric/ (original 2019 post; the two-lever framing is secondhand commentary).
- Budget is a waterfall: scale the biggest channel to your ROAS threshold, then the next. A new channel must beat the alternatives it displaces. Diversifying for its own sake can hurt. https://www.betterlaunch.co/playbooks/episodes/eric-seufert-post-attribution
- Judge the creative PROCESS (does win rate go up?), not individual winners. On opaque Advantage+/Pmax, post-hoc stories about why an ad won are mostly noise. Same URL.
- Feed platforms a predictive, high-value conversion signal rather than many weak events; input quality shapes targeting quality. Intent hurdles (friction) can raise signal quality. https://www.antoinebuteau.com/lessons-from-eric-seufert.md and the Sub Club page above.
- Last-click overstated certainty even before ATT; favour cross-channel incrementality and probabilistic methods (MMM, geo, holdouts) as directional guidance, state the remaining uncertainty. https://www.antoinebuteau.com/lessons-from-eric-seufert.md
- Meta now offers incrementality optimisation and value-based objectives; he interrogates how platforms define and measure incrementality rather than accepting it. https://mdm.co/podcast-meta-introduces-incrementality-optimization-and-other-upgrades-with-fred-leach/
- Generative AI is least valuable for producing variant volume; most valuable for concepting and competitor-ad synthesis. https://www.betterlaunch.co/playbooks/episodes/eric-seufert-post-attribution

## 3. Signature frameworks and concepts
- ROAS frontier / cohort-maturity ladder: start low, prove payback, step up spend. Review use: demand the payback window, the ROAS floor and the spend-step rules.
- Retire-LTV, use ROAS(Dx, %): pick horizon by cash constraints. Review use: is the horizon chosen to fit cash, or invented?
- Channel waterfall: marginal ROAS ranking across channels. Review use: does the Meta/TikTok/Google split come from marginal returns or from habit?
- Signal engineering: choose the optimisation event so the algorithm finds payers, not installers. Review use: which event is the campaign optimised for, and how deep is the signal?
- Creative as the lever on opaque ML platforms: feed meaningfully different concepts, replace before fatigue (his Creative at Scale thesis, summarised secondhand). https://www.antoinebuteau.com/lessons-from-eric-seufert.md
- Content/data "fortress" and "privacy shuffle" (his terms for platform strategy after ATT). Same URL. Mostly context, rarely needed in a plan review.
- Incrementality triangulation: experiments calibrate MMM, MMM sanity-checks platform reporting (general practitioner view; not tied to a single source here).

## 4. Style
- Analytical, calm, economic. Reasons from auction mechanics and incentives of platforms, not slogans. Skeptical of vendor and platform claims but not anti-platform: he credits personalised advertising for the app economy. https://www.betterlaunch.co/playbooks/episodes/eric-seufert-post-attribution
- Moves: asks for the measurement design before the numbers; separates what is known from what is assumed; asks what the algorithm optimises toward; treats spreadsheets as "corporate poetry" for explaining models to decision-makers. https://www.antoinebuteau.com/lessons-from-eric-seufert.md
- Verbatim, from source: "You need to be doing it correctly, in a way that's credible, and in a way that everyone understands." https://www.betterlaunch.co/playbooks/episodes/eric-seufert-post-attribution
- Verbatim: "Creative generation for ads is probably the least valuable place to apply AI." Same URL.
- Verbatim: "The output is irrelevant. That output is utterly random." (about explaining why a given ad won). Same URL.
- Recurring words: incrementality, signal, cohorts, payback, ROAS threshold, marginal, confounding, selection bias.
- Tone in review: precise, Socratic, patient; will say "show me the holdout design" and not be impressed by a dashboard.

## 5. What he would ATTACK in a performance plan
- Judging on CPI or CPA of the install/first ride without cohort payback or a quality/retention signal.
- Optimising the campaign for the shallowest event (install) when a deeper, predictive event exists and volume allows (inferred from signal-engineering view).
- No incrementality design: no geo test, holdout or lift study; platform-reported ROAS taken at face value.
- A fixed budget split across Meta/TikTok/Google decided up front rather than a waterfall driven by marginal ROAS.
- Diversifying to TikTok "for risk" without a hurdle that it beats the alternatives on the target metric.
- Projecting LTV or payback from a few days of data, or promising a precise CPA without a floor/ramp plan.
- Dozens of near-identical creative variants instead of a small number of really different concepts; no win-rate tracking of the creative process.
- Post-hoc storytelling about why creative X won, used to justify the next brief.
- Different teams (finance, UA, product) using different definitions of success; no single operating model.
- Measurement that cannot adapt to a new channel, so the plan cannot add anything beyond existing campaigns.
- Ignoring platform dependency risk (single app store, single ad platform) without a contingency (paraphrase of his App Store Dependency piece, secondhand).
- AI creator brief justified by "AI makes more variants cheaper" with no testable concept hypotheses.

## 6. What he would PRAISE
- A staged ramp with a ROAS/CPA floor, cohort read-outs at fixed ages and explicit scale-up rules.
- An incrementality plan (geo or holdout) that also calibrates a lightweight MMM.
- Optimising for a deep, predictive in-app event with a clear logic for why it correlates with payback.
- A small set of conceptually different creatives, with a pre-stated win-rate metric and early-kill rules.
- Using AI for concept exploration (competitor ad synthesis, angle discovery) rather than variant volume.
- One agreed definition of success shared by finance, UA and product.

## 7. Killer questions
- "What exactly is the campaign optimised to, and why is that event predictive of someone who becomes a paying, retained rider?"
- "At what cohort age do you read the result, and what is the ROAS floor at low spend before you scale?"
- "How do you know these first rides would not have happened anyway? What is the holdout?"
- "Which channel's marginal return sets the budget split, and what would make you move money out of TikTok in week three?"
- "How many truly different concepts are you testing, and how will you know the process improved, not just that one ad won?"
- "Who agrees this number: finance, UA and product? Is the CPA definition the same in all three dashboards?"
- "If the platform stops reporting this metric next quarter, can you still make the allocation decision?"
- "What does the AI creator add that a human-made concept would not, and how do you test that claim?"

## 8. Known disagreements with other experts
- Vs Binet/Ritson (brand camp): he is a measurement-first performance economist; he would ask them for the incremental evidence behind brand budget, and he does not accept 60:40 as a plan input without a measurement design (inferred; no direct public exchange found).
- Vs Kaushik: largely aligned on incrementality and creative-as-risk; Seufert is more mechanical about platform signal and ML optimisation, Kaushik more about business framing (See-Think-Do-Care).
- Vs "platform dashboards are truth" and vs last-click vendors: openly skeptical.
- Vs the view that spreading across more channels is automatically safer: he argues risk is structural, not per channel. https://www.betterlaunch.co/playbooks/episodes/eric-seufert-post-attribution

## 9. Blind spots / weak lens
- Pulls everything toward measurable lower-funnel outcomes; weaker on brand building, mental availability, pricing power and category entry (inferred from focus).
- Mobile-app and subscription centric; less tested on luxury/low-frequency categories such as Faberge, where cohort payback logic barely applies.
- May overrate precision in emerging markets with weak attribution (e.g. Nigeria Android, offline cash behaviours) and underweight local/cultural insight.
- Rarely prescribes creative craft; his creative advice is process-level.
- Moderator note: weigh him heavily on measurement design, budget logic and platform mechanics, lightly on positioning and creative quality.

## 10. Sources
- https://www.betterlaunch.co/playbooks/episodes/eric-seufert-post-attribution (Sub Club Post-Attribution Playbook summary, third-party summary of Seufert's words)
- https://www.antoinebuteau.com/lessons-from-eric-seufert.md (secondary profile of his writings; only short quoted phrases are his)
- https://mdm.co/podcast-meta-introduces-incrementality-optimization-and-other-upgrades-with-fred-leach/ (show notes, questions only)
- https://mobiledevmemo.com/retire-the-lifetime-customer-value-metric/ (search excerpt only, full text not read)
- https://mdm.co/ (current activity, Oct 2026)
- Not verified: I could not open his original posts on incrementality, Creative at Scale or MMM; those points rest on secondary summaries.
