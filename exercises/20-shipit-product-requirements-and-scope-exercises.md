# Chapter 20: ShipIt — Product Requirements and Scope — Practice Exercises

*INFO 7375 · Branding and AI · Northeastern University*

---

> **How to use these exercises:**
> Work through each tier in order. Do not skip ahead to later tiers before completing earlier ones — the tiers scaffold your understanding. Attempt every exercise before checking the answer key. For open-ended questions, write at least 2–3 sentences before reading the model answer. The act of attempting is where the learning happens.

---

## Learning Objectives

- Distinguish the PRD's four sections (Problem, Gap, Tool, MVP Boundary) and explain what each must contain
- Apply the what-vs.-how distinction to identify PRD contamination
- Explain what MVP means in the Build-Measure-Learn framework (validated learning, not minimal effort)
- Write the $100,000 no — the scope refusal that defines a product's identity
- Explain how scope discipline compounds as brand identity using the Linear case

*Every exercise below maps to at least one of these objectives. The `(Tests: ...)` tag on each exercise identifies which one(s) by full concept name.*

---

## Worked Example

*Study this example before attempting Tier 1. After reading it, close it and try to recall the key steps from memory before moving on.*

**Problem:** A student is drafting the Problem section of a PRD for a tool that would help independent musicians track where their music is being streamed, by region, in a single dashboard. Their current draft: "Musicians need better data about their streams." Improve this to a strong Problem section.

**Approach:**
- Step 1 — Identify the failure mode. "Musicians need better data" is a symptom statement. It describes an absence ("better data") without naming a user precisely enough to find ten of them, a task specifically enough to see what they currently do, a frequency that implies real cost, or a failure mode that explains what "better" means.
- Step 2 — Find the specific user. "Independent musicians" is vague. "Independent musicians who release music on Spotify, Apple Music, and Bandcamp without a label deal or distribution manager" is a person. They have specific constraints (no team, no analytics staff) and a specific problem scope.
- Step 3 — Find the specific task. What do they currently do? They log into three or four platforms separately, check stream counts manually, try to spot geographic patterns by eye, and copy numbers into a spreadsheet — a weekly task with no aggregation and no trend visualization.
- Step 4 — Identify the cost. Time (45–60 minutes per platform review), consequence (decisions about where to promote or tour are made on rough intuition rather than actual geographic data), and failure mode (they miss breakout regions that their data, viewed separately, would have revealed).

**Answer:** "Independent musicians releasing on three or more platforms without label representation spend 90–120 minutes per week logging into separate dashboards to manually check stream counts, trying to identify geographic breakout regions by comparing screenshots and spreadsheet rows. The effort is high, the comparison is imprecise, and musicians routinely miss regional momentum until it has already peaked — because no single view shows them where their streams are growing fastest, across all platforms, in one place."

**What to notice:** The strong Problem section has a specific user (independent musicians without label representation), a specific task (manual comparison across platform dashboards), a specific frequency (weekly), and a specific failure mode (missing regional breakout momentum). Every element is testable — you can find ten people who fit this description and ask whether the problem statement is accurate.

---

## Tier 1 — Warm-Up (Exercises 1–6)

*Bloom's Level: Remember / Understand*
*Purpose: Verify that the chapter's core concepts and vocabulary are in place before you apply them.*

---

**Exercise 1**

Name the four sections of a one-page PRD. For each, write the single question it answers — using the chapter's framing, not a paraphrase.

*(Tests: PRD four sections — names and core questions)*

**Answer:** (1) Problem: What specific problem are you solving, for whom, and how often does it cost them something? (2) Gap: What already exists to solve this problem, and where does it fall short? (3) Tool: What, exactly, will you build? (4) MVP Boundary: What is in scope for v1, and — explicitly — what is not?

**Common error:** Describing the Tool section as "what the architecture is" or "how it will be built." The Tool section describes the what — the output and behavior from the user's perspective — not the engineering implementation.

*Chapter reference:* Chapter 20, "What a PRD Actually Is."

---

**Exercise 2**

True / False: "Minimum viable product" means the product with the fewest features that can still be called a product.

*Explain your reasoning in one sentence:*

*(Tests: MVP — validated learning definition vs. common misreading)*

**Answer:** False. MVP means the smallest product version that allows the team to collect maximum validated learning about customers with minimum effort. "Minimum" modifies the effort required to run the learning cycle — not the feature count. An MVP may require several features to generate the behavioral data that tests the core hypothesis.

**Common error:** Agreeing with the statement because "minimum" sounds like "fewest features." The chapter is explicit that "minimum" refers to effort relative to the learning goal, not to product completeness.

*Chapter reference:* Chapter 20, "What 'Minimum Viable Product' Actually Means."

---

**Exercise 3**

In your own words, explain the *what-vs.-how* distinction in the PRD. Give one example of a "how" that has been smuggled into a "what" statement.

*(Tests: what-vs.-how distinction — PRD contamination)*

**Answer:** The PRD specifies what the product needs to do — the behavior and output from the user's perspective. The engineering team decides how to implement it. The distinction matters because when "how" decisions appear in the PRD, they get treated as requirements, creating false constraints that are hard to change when implementation needs to evolve. Example of "how" smuggled into "what": "The tool sends users a daily email summary via SendGrid at 7 a.m. Eastern using a Handlebars template." The "what" is "the tool sends users a daily email summary." SendGrid, 7 a.m. Eastern, and Handlebars are implementation decisions that do not belong in the PRD.

**Common error:** Treating the what-vs.-how distinction as purely about technical specificity (e.g., "name the database" = how). The distinction is about who has decision authority — the PRD constrains what the product does; engineering decides how it does it.

*Chapter reference:* Chapter 20, "What a PRD Actually Is."

---

**Exercise 4**

The chapter identifies specific failure modes for each of the four PRD sections. Match each failure mode to its section:

(a) "Marketing professionals need better competitive intelligence." 
(b) "There are tools out there, but they're not quite right."
(c) "An AI-powered platform for marketing intelligence."
(d) An out-of-scope list with two items.

*(Tests: PRD four sections — failure modes by section)*

**Answer:** (a) Problem section failure — "abstracting the user" and describing a symptom rather than a cause. "Marketing professionals" is not a specific user; "better competitive intelligence" is an outcome without a task, frequency, or cost. (b) Gap section failure — vagueness. A gap analysis must name actual products and explain exactly what each one gets wrong for the specific user; "not quite right" is not a gap analysis. (c) Tool section failure — marketing language. "AI-powered platform" is a press release sentence that tells the reader nothing about what the product does, how it does it at the output level, or who it is for. (d) MVP Boundary failure — an out list that is too short. Every PRD has an "in" list by default; the discipline is in the "out" list. Two items suggests the team has not done the hard work of deciding what to refuse.

**Common error:** Labeling (a) as a Gap failure because "it doesn't name competitors." The problem is in the Problem section — the user and the symptom/cause distinction — not in the competitive analysis.

*Chapter reference:* Chapter 20, "What a PRD Actually Is."

---

**Exercise 5**

In your own words, explain the *$100,000 no* as the chapter defines it. What distinguishes it from a routine "out of scope" decision?

*(Tests: $100,000 no — scope discipline definition)*

**Answer:** The $100,000 no is the feature a product team would decline even when declining it costs them something real — a genuine user request, a paying customer, a feature that is technically feasible. It is not a routine "out of scope" decision because every product has things that are out of scope by default without any discipline being required. The $100,000 no is distinguished by the acknowledgment of cost: you are refusing something a real user wants, with a real argument for why it belongs in the product, because building it would compromise the product's core point of view. The Linear example: refusing enterprise customization worth significant contract value because the customization conflicted with the product's philosophy of opinionated, simple software.

**Common error:** Describing the $100,000 no as simply "refusing features." The discipline is in refusing features that have a real user advocate and a real argument — not features that nobody asked for.

*Chapter reference:* Chapter 20, "The $100,000 No."

---

**Exercise 6**

The chapter uses the Linear case to illustrate "scope discipline compounds." Using only the chapter's framework, explain the mechanism by which each refusal of a scope-compromising feature makes the product stronger over time — not just smaller.

*(Tests: scope discipline as brand identity — Linear case mechanism)*

**Answer:** Each time Linear refuses a feature that would compromise the core (opinionated, fast, designed around a specific model of how engineering teams should work), they preserve the coherence of the experience that made the product worth using. Over time, that coherence becomes the product's identity: the specific experience that engineers recommend when they want to escape Jira's accumulated complexity. The identity becomes the brand. The brand attracts more users who value that specific coherence, which deepens it further. Meanwhile, each time a competitor accepts a scope-compromising feature — usually for a specific customer's revenue — they spend coherence for cash. Over successive cycles, the disciplined product's coherence compounds into brand identity while the undisciplined product's accumulated incoherence drives away the original user base. Scope discipline is not about keeping the product small — it is about preserving the coherence that made the product worth using, so each new user encounters the same experience that made the previous users advocates.

**Common error:** Describing scope discipline as "keeping the product simple." The chapter's argument is about coherence — a specific designed experience — not about simplicity as an aesthetic preference.

*Chapter reference:* Chapter 20, "Scope Discipline as Identity: The Linear Case."

---

## Tier 2 — Application (Exercises 7–14)

*Bloom's Level: Apply / Analyze*
*Purpose: Use the chapter's concepts in realistic situations.*

---

**Exercise 7** *(Scenario-Based Application)*

Rahel is writing the Problem section of her PRD for a tool that would help language learners track vocabulary retention across multiple learning apps. Her current draft: "Language learners struggle to retain vocabulary because they use many different apps that do not share data. There is no single place to see their full vocabulary progress."

Apply the chapter's Problem section criteria. What specifically is missing or weak in Rahel's draft? Rewrite it to produce a strong Problem section.

*(Tests: PRD Problem section — specific user, task, frequency, cost, failure mode)*

**Answer:** What is missing: (1) The user is still too vague — "language learners" could be tourists using Duolingo or professional translators. A specific user would have a learning goal, a context, and a current behavior. (2) There is no frequency — how often does this problem surface? (3) There is no specific task — what does the learner currently do when they want to check their vocabulary retention across apps? (4) The failure mode is described as "no single place" — but what fails as a result of not having a single place? What decision gets made badly, or what effort gets duplicated? Rewrite: "Adult language learners studying a second language at an intermediate level (B1–B2) who use two or more vocabulary apps simultaneously (such as Anki and an in-browser extension) have no way to see which words they have reviewed across all apps and which are due for review. As a result, they either re-study words they already know (wasting study sessions) or neglect words that appeared in only one app (losing retention they thought they had built). Learners report spending 15–20 minutes before each session trying to reconcile what they 'already know' across their tools, and still making avoidable errors in the gaps."

**Common error:** Adding a specific user type but still omitting the task and the failure mode. A strong Problem section includes all four: user, task (or current workaround), frequency/cost, and failure mode (what goes wrong as a result).

*Chapter reference:* Chapter 20, "What a PRD Actually Is — Section 1: Problem."

---

**Exercise 8** *(Error Analysis)*

> The following MVP Boundary section was submitted by a student for a sentiment analysis tool.

*"In scope for v1: RSS feed ingestion, sentiment scoring, Google Sheets output, email notifications, multi-user support with admin roles, team-level dashboards, Slack integration, historical trend analysis, social media monitoring. Out of scope for v1: browser extension."*

1. Identify the primary error in this MVP Boundary section.
2. Explain the misconception that caused it — what did the student misunderstand about what the MVP Boundary is supposed to do?
3. Rewrite the MVP Boundary section to reflect the chapter's guidance.

*(Tests: MVP Boundary — scope discipline and the out-of-scope list)*

**Answer:**
1. The in-scope list is overloaded with features that should be in the out-of-scope list. Multi-user support with admin roles, team-level dashboards, Slack integration, historical trend analysis, and social media monitoring are all significant scope additions that change the product's complexity and delay the core hypothesis test. The out-of-scope list has one item — which signals no real scope discipline was applied.
2. The misconception: the student treated the MVP Boundary as a feature roadmap — a list of everything they want to build, labeled "in scope." The chapter's definition of MVP is "the smallest thing that produces validated learning about the core hypothesis." The student has not identified a core hypothesis; they have listed everything they could imagine building and called it v1.
3. Rewrite: *In scope for v1:* Up to 10 RSS feeds per user, configured manually; sentiment scoring (positive/neutral/negative + one-sentence summary) using the OpenAI API; daily output to a single designated Google Sheet; email notification when the sheet has been updated. *Out of scope for v1:* Multi-user accounts or team sharing (changes the product from personal tool to team platform — different design philosophy); social media monitoring (requires different APIs, different rate limiting, different content normalization); team-level dashboards (out until single-user value is validated); Slack integration (out until Google Sheets proves insufficient); historical trend analysis beyond 30 days (requires different data storage architecture). *$100,000 no:* Multi-user accounts — even if an enterprise prospect asks and will pay, building it changes every subsequent design decision.

**Common error:** Keeping multi-user support in scope and only moving social media monitoring to the out list. A strong rewrite moves all the features the chapter would classify as scope creep out of v1, with archetype-reason rationale for each.

*Chapter reference:* Chapter 20, "What a PRD Actually Is — Section 4: MVP Boundary."

---

**Exercise 9** *(AI Interaction — with verification requirement)*

First, write your own answer without consulting AI:
*"What is validated learning in the Build-Measure-Learn loop, and why does it require a 'version' (real product) rather than a mock or prototype?"*

Then read the following AI-generated response:

*AI response: "Validated learning in the Build-Measure-Learn loop refers to knowledge gained from testing your product with real users that confirms or disconfirms your hypotheses. The key difference between validated learning and unvalidated feedback is that validated learning comes from users' actual behavior with the product, not just their stated opinions. A real product version is necessary because user behavior with a mock or prototype is artificially constrained — users know they are testing something that is not real, which changes how they interact with it. With a real product, users bring their actual workflows, real data, and genuine stakes, which produces more accurate behavioral evidence for or against your hypothesis."*

1. Identify the strongest point in the AI's response.
2. Identify one gap or imprecision relative to the chapter's specific treatment of validated learning.
3. Write a correction or extension.
4. State the specific behavioral metric you would use to validate the core hypothesis from the chapter's worked example (the marketing manager competitive intelligence tool).

*(Tests: MVP and Build-Measure-Learn loop — evaluation of AI output)*

**Answer:**
1. Strongest point: "Users bring their actual workflows, real data, and genuine stakes" — this captures why a version produces different behavioral data than a prototype. The insight that prototype behavior is "artificially constrained" is correct.
2. Gap: The AI's definition of validated learning does not include the prerequisite that you must know *which* hypothesis you are testing before you build. The chapter is explicit: "The Build-Measure-Learn loop only works if you know, before you build, which assumption you are testing. If you do not know what you are testing, you cannot interpret the results." The AI presents validated learning as something that happens naturally with a real product and real users — but the chapter's point is that the hypothesis must be specified in advance in the PRD's problem statement for the learning to be interpretable.
3. Extension: "Validated learning is not simply user feedback on a real product — it requires a pre-specified hypothesis that the product version is designed to test. Without the hypothesis, behavioral data cannot be interpreted: a user who stops using the tool after two weeks might be telling you the intelligence is not actionable, the format is wrong, or the cadence is wrong. You need to know which one the PRD's problem statement was testing in order to learn from the failure."
4. Specific behavioral metric: "Marketing managers at small B2B companies will open the Google Sheet summary at least three times per week after the first two weeks of use." This metric is behavioral (opening the sheet, not self-reporting that they like it), has a specific threshold (three times per week), has a specific timeframe (after the first two weeks, which controls for novelty effects), and is directly tied to the problem statement's claim about daily utility.

*Chapter reference:* Chapter 20, "What 'Minimum Viable Product' Actually Means."

---

**Exercise 10** *(Self-Explanation)*

In this chapter, the PRD specifies the *what* and engineering decides the *how*. Explain in 2–3 sentences why keeping the "how" out of the PRD matters — not just as a procedural rule, but using the specific consequence the chapter identifies when "how" decisions appear in the PRD. Your explanation must use the term "false constraints."

*(Tests: what-vs.-how distinction — self-explanation of the false-constraints consequence)*

**Answer:** When implementation decisions (the "how") appear in the PRD, they get treated as requirements. Engineers build against them. When the implementation needs to change — which the chapter notes it always does — the PRD becomes a source of false constraints: boundaries on engineering decisions that were never actually product requirements, only one person's early preference about technology. The consequence is that a defensible technology choice (SendGrid, GPT-4o-mini, a specific temperature setting) becomes entrenched in the product's requirements documentation, making it difficult to swap out even when a better option or lower-cost alternative exists. The PRD should preserve engineering flexibility; contaminating it with "how" decisions forecloses options that were never the PRD's to foreclose.

**Common error:** Describing the problem as "engineers don't like being told what tools to use." The chapter's argument is structural — false constraints make the PRD unable to serve its function as a living document that engineering can build against.

*Chapter reference:* Chapter 20, "What a PRD Actually Is."

---

**Exercise 11** *(Cumulative — prior chapter concept)*

In Chapter 1, you learned about *archetypes as forcing functions* — that a clearly committed archetype makes certain choices obvious and certain choices unavailable. In this chapter, you are working with the *$100,000 no* — the scope refusal that defines the product's identity.

The chapter states: "the archetype tells you what kind of tool to build. The problem statement tells you for whom." Apply this relationship to the $100,000 no: how does a clearly committed archetype make the $100,000 no easier to identify and defend against pressure?

*(Tests: archetype as forcing function + $100,000 no — interleaved application)*

**Answer:** A clearly committed archetype provides the point of view from which a scope refusal is defensible. Without an archetype, every feature request must be evaluated in isolation — "is this a good feature?" — which almost always produces "yes." With an archetype, the question changes: "does this feature belong in this product, given what this product is for and who it is for?" The Creator archetype building a generative content pipeline for independent creators has a $100,000 no when an enterprise client wants multi-team permission management: building it would change the product from an individual creator's tool to an enterprise content management system, and those are different products with different archetypes. The archetype is the forcing function that makes the refusal principled rather than arbitrary — the team can explain not just "we won't build this" but "we won't build this because it would require us to become a different kind of product for a different kind of user, which would compromise the experience that the users who came for the Creator archetype value." The archetype is what the chapter describes as a "point of view strong enough to hold under pressure."

**Common error:** Treating the $100,000 no as a budget or capacity decision rather than an identity decision. The chapter is explicit: the refusal is "not because the feature is technically impossible or economically worthless" — it is because building it would damage the product's coherence.

*Chapter reference:* Chapter 20, "The $100,000 No"; Chapter 1, "Archetypes as Forcing Functions."

---

**Exercise 12** *(Scenario-Based Application)*

Tariq is writing the Gap section of a PRD for a tool that helps independent freelancers track project profitability — not just hours billed but actual profit after expenses, tool subscriptions, and taxes. His current Gap section: "There are accounting tools like QuickBooks and FreshBooks, but freelancers don't like them. Also, spreadsheets work for some people."

Apply the chapter's Gap section criteria. What specifically is missing? Rewrite the Gap section.

*(Tests: PRD Gap section — specific competitors, specific failure modes)*

**Answer:** What is missing: (1) The Gap section must name actual products and explain exactly what each one gets wrong for the specific user. "Freelancers don't like them" is not a failure mode analysis. (2) No specific failure mode for QuickBooks or FreshBooks is named. (3) The spreadsheet option is acknowledged but not analyzed. (4) No implication about what gap exists — what the market has and what the market lacks for this specific user. Rewrite: "QuickBooks Self-Employed tracks income and expenses and estimates quarterly taxes, but it requires manual categorization of every transaction, does not track time against projects, and has no concept of 'per-project profitability' — freelancers with multiple simultaneous clients cannot see which projects are actually profitable after tool costs, research time, and revision rounds. FreshBooks generates professional invoices and tracks time by client, but its profitability view is revenue-minus-time, with no way to deduct tool subscriptions, asset purchases, or project-specific overhead. Spreadsheets can do all of this, but require significant setup and ongoing manual maintenance; most freelancers maintain them for one quarter and abandon them when the upkeep exceeds the insight value. The gap: a tool that tracks actual per-project profitability — revenue minus time (at target rate) minus expenses minus allocated overhead — in a format a non-accountant can interpret without manual data entry."

**Common error:** Adding specific competitors but still omitting specific failure modes. A strong Gap section explains not just who the competitors are but exactly what they fail to do for this specific user.

*Chapter reference:* Chapter 20, "What a PRD Actually Is — Section 2: Gap."

---

**Exercise 13** *(Application)*

The chapter distinguishes between a *testable hypothesis* and a *vision statement* in the context of the MVP. For each of the following, classify it as a testable hypothesis or a vision statement, and explain your reasoning:

(a) "Independent musicians will check regional streaming data three times per week if it is surfaced in a single dashboard with trend indicators."
(b) "Our tool will become the go-to analytics platform for independent musicians globally."
(c) "Freelancers will pay $15/month for a project profitability tool if it requires less than five minutes of setup and produces a profitability report on the first project within the first session."
(d) "AI-powered financial tools will transform the freelance economy."

*(Tests: MVP — testable hypothesis vs. vision statement)*

**Answer:** (a) Testable hypothesis — it has a specific behavior (check regional data), a specific threshold (three times per week), a specific product version (single dashboard with trend indicators), and a measurable outcome within an MVP window. (b) Vision statement — "go-to platform globally" is not testable within an MVP window; it describes an end state, not a hypothesis about a specific user behavior the MVP can test. (c) Testable hypothesis — it has a specific behavior (pay $15/month), a condition (less than five minutes setup), and a specific outcome threshold (profitability report on first project in first session), all measurable within an MVP trial period. (d) Vision statement — "transform the freelance economy" is not falsifiable within any reasonable timeframe and does not describe a specific user behavior. It belongs in a pitch deck, not a PRD.

**Common error:** Labeling (b) as testable because "you can check whether it becomes go-to." The chapter's criterion is whether the hypothesis produces falsifiable behavioral evidence within the MVP window — a multi-year market position claim does not meet this criterion.

*Chapter reference:* Chapter 20, "What 'Minimum Viable Product' Actually Means."

---

**Exercise 14** *(Application)*

The chapter says: "A PRD is a contract with future-you: a record of the decisions you made when you were thinking clearly, preserved for the moment when you are thinking under pressure." Explain in 2–3 sentences what type of pressure the PRD is designed to resist and give one specific example of a scenario where a PRD with a strong $100,000 no would prevent a bad decision.

*(Tests: PRD as decision record — contract with future-self under pressure)*

**Answer:** The pressure the PRD is designed to resist is scope creep — the accumulated result of in-the-moment decisions made under social or commercial pressure, each individually defensible but collectively incoherent. The $100,000 no in the out-of-scope list is specifically designed to survive the moment when a real user with a real budget asks for the refused feature. Specific example: a team building a personal competitive intelligence tool for solo marketers has written in their PRD: "$100,000 no — multi-user accounts (changes product from personal tool to team platform)." Three months after launch, an enterprise marketing director offers a $12,000 annual contract if the team adds multi-user accounts with admin roles. Without the PRD, the team debates the feature under commercial pressure and the social weight of a real paying offer. With the PRD, the team has the reasoning they wrote when they were thinking clearly: "building multi-user accounts changes every subsequent design decision — permissions, audit trails, admin interfaces — and we stop building the personal tool and start building a different product." The PRD does not make the decision; it preserves the reasoning that the team already made when they were not under pressure.

**Common error:** Describing the PRD as preventing "bad ideas" or "feature bloat" generically. The chapter's specific claim is about preserving decisions made when thinking clearly against the pressure of specific, real, commercially tempting requests.

*Chapter reference:* Chapter 20, "What the PRD Is Actually Doing."

---

## Tier 3 — Synthesis (Exercises 15–16)

*Bloom's Level: Analyze / Evaluate*
*Purpose: Connect this chapter's concepts to a concept from a prior chapter.*

---

**Exercise 15** *(Cross-Chapter Synthesis)*

In Chapter 6, you learned about *brand archetypes as forcing functions* and the concept of *brand equity* — the accumulated recognition and trust that compounds when a brand makes consistent identity choices. In this chapter, you are working with *scope discipline as brand identity*, illustrated by the Linear case.

The chapter makes a specific claim: "scope discipline compounds." Evaluate this claim using the brand equity concept from Chapter 6. How does each scope refusal contribute to equity accumulation? And under what conditions might the inverse be true — when does scope discipline *erode* equity rather than build it?

*This question connects scope discipline as brand identity (Chapter 20) to brand archetypes and equity accumulation (Chapter 6).*

*What distinguishes a surface answer from a strong one:*
- A strong answer shows the specific mechanism by which scope refusals accumulate brand equity — not just "consistency = trust" but the specific archetype-coherence mechanism
- A strong answer identifies the condition under which scope discipline erodes equity — when it is not grounded in a coherent point of view
- A strong answer uses the Linear case to illustrate at least one direction of the argument

*(Tests: scope discipline as brand identity + brand equity accumulation — Ch. 20 + Ch. 6)*

**Answer:** Brand equity accumulates when users repeatedly encounter a coherent, distinctive experience that matches the brand's archetype and promise — each positive encounter deepens the associative network and makes the brand more recognizable and trustworthy. In Linear's case, each scope refusal preserves the specific experience (opinionated, fast, engineer-centered) that made the product worth using. Over time, users who value that experience become advocates who recommend it specifically because of what it does not do — the absence of Jira's complexity is itself a brand signal. Each refusal is therefore a small act of equity accumulation: it deepens the coherence of the experience, which deepens the brand's recognizability as "the tool that engineers recommend when they want to escape Jira." The inverse condition: scope discipline erodes equity when it is not grounded in a coherent archetype. A team that refuses features arbitrarily — without a clear point of view about what the product is for and who it serves — produces a product that is small and rigid without being coherently anything. Users experience the refusals as unhelpfulness rather than as disciplined design. The chapter names this: "I teach the $100,000 no as a tool. What I have not yet figured out is how to teach the underlying point of view that makes the no meaningful rather than merely rigid." Without the archetype-grounded point of view, scope discipline is sterile rather than productive.

*What a surface answer looks like:* "Scope discipline builds brand equity because Linear has a consistent identity." This mentions both concepts but does not show the mechanism by which each refusal contributes to equity accumulation.

*Common error:* Missing the inverse condition — treating scope discipline as universally beneficial without addressing when it produces rigidity rather than coherence.

*Chapter reference:* Chapter 20, "Scope Discipline as Identity"; Chapter 6, "Archetypes as Brand Equity."

---

**Exercise 16** *(Cross-Chapter Synthesis)*

In Chapter 18, you learned about the *negative-space rule* for portfolio curation: what you refuse to include defines the portfolio's point of view as clearly as what you include. In this chapter, you are working with the *MVP Boundary's out-of-scope list* as a scope discipline mechanism.

A student argues: "The negative-space rule and the $100,000 no are the same concept applied to different contexts — they are both just about deciding what to leave out." Evaluate this argument. In what ways are the two concepts genuinely analogous? In what specific ways do they differ, and why do the differences matter?

*This question connects the negative-space rule (Chapter 18) to the MVP Boundary and $100,000 no (Chapter 20).*

*What distinguishes a surface answer from a strong one:*
- A strong answer names the genuine analogy — what the two concepts share in mechanism
- A strong answer identifies at least one specific difference in purpose or application that the student's argument flattens
- A strong answer uses a concrete example to illustrate the difference, not just describe it abstractly

*(Tests: negative-space rule + $100,000 no — Ch. 18 + Ch. 20)*

**Answer:** The genuine analogy: both concepts hold that the decision to exclude something is an active identity claim, not a passive default. The portfolio that excludes a bootcamp CRUD app is making a claim about what kind of engineer the builder is; the PRD that excludes multi-user accounts is making a claim about what kind of product this is and what user it is for. Both apply the same structural insight: identity is defined as much by refusal as by inclusion. The differences: (1) Purpose and stakes. The negative-space rule is a curation and identity discipline — the cost of a wrong exclusion is a less coherent portfolio identity. The $100,000 no is a scope and commercial discipline — the cost of a wrong refusal is a lost contract and a real user left unserved. The stakes of the $100,000 no are operationally higher, which is why the chapter treats it as a specific, named commitment that requires being written down before the pressure arrives. (2) Timing. The negative-space rule is applied retrospectively to completed work — you choose among projects that exist. The $100,000 no is applied prospectively — you name the feature you will refuse before anyone has asked for it, so the decision is made when you are thinking clearly. (3) External pressure. The negative-space rule operates without external pressure (no one is actively lobbying for the bootcamp CRUD app to be included). The $100,000 no is specifically designed to survive external pressure — a real user with a real budget asking for the refused feature.

*Common error:* Agreeing that the two concepts are the same and describing only their similarities. A strong answer engages the specific structural differences.

*Chapter reference:* Chapter 20, "The $100,000 No"; Chapter 18, "Curation and negative space."

---

## Tier 4 — Challenge (Exercise 17)

*Bloom's Level: Evaluate / Create*
*Purpose: Transfer beyond what was explicitly taught.*

---

**Exercise 17** *(Transfer Challenge)*

The chapter's "Still Puzzling" section identifies a genuine unsolved problem: the $100,000 no requires a coherent point of view to be meaningful rather than arbitrary — "a sterile discipline rather than a productive one." The chapter does not have a teachable rule for how to develop the underlying point of view.

Design a three-stage diagnostic process that a student could use — before writing the PRD — to determine whether their $100,000 no is grounded in a coherent product identity or is merely arbitrary. The diagnostic should produce different results for two students: one who has a clear archetype and a specific user, and one who has a vague archetype and a generic user.

*A strong response will address:*
- What questions or tests reveal whether a team has a genuine point of view strong enough to generate principled refusals
- How to distinguish a refusal grounded in product identity from one that is a default ("we haven't built it yet") or a capacity decision ("we don't have time")
- What the output of the diagnostic looks like for a student who does not yet have the required point of view — and what they should do

*(Tests: $100,000 no + PRD as decision record applied to a novel design challenge)*

---

## Answer Key

> Attempt all exercises before reading this section.
> For Tier 3 and Tier 4, your answer does not need to match the model exactly — use the "what a strong answer includes" criteria to evaluate your own response.

---

**Worked Example**
*No answer needed — the worked example is its own model.*

---

**Ex 1** — *Four PRD sections*
*Model answer:* Problem: what specific problem, for whom, how often? Gap: what exists, where does it fall short? Tool: what exactly will you build? MVP Boundary: what is in scope, and what explicitly is not?
*Common error:* Describing Tool as "what the architecture is" rather than what the product does from the user's perspective.
*Chapter reference:* Ch. 20, "What a PRD Actually Is."

---

**Ex 2** — *MVP definition*
*Answer:* False.
*Correct because:* MVP means the smallest version that produces maximum validated learning about the core hypothesis, not the version with the fewest features.
*Common error:* Agreeing because "minimum" sounds like "fewest features."
*Chapter reference:* Ch. 20, "What 'Minimum Viable Product' Actually Means."

---

**Ex 3** — *What-vs.-how distinction*
*Model answer:* The PRD specifies what; engineering decides how. When "how" appears in the PRD, it becomes a false constraint. Example: "via SendGrid at 7 a.m. Eastern using a Handlebars template" is "how" smuggled into a "what" statement.
*Common error:* Treating the distinction as being about technical specificity rather than decision authority.
*Chapter reference:* Ch. 20, "What a PRD Actually Is."

---

**Ex 4** — *PRD section failure modes*
*Model answer:* (a) Problem — abstracting the user + symptom not cause. (b) Gap — vagueness, no named competitors. (c) Tool — marketing language. (d) MVP Boundary — out list too short.
*Common error:* Labeling (a) as Gap because "it doesn't name competitors."
*Chapter reference:* Ch. 20, "What a PRD Actually Is."

---

**Ex 5** — *$100,000 no*
*Model answer:* The $100,000 no is the feature a team would refuse even when refusing costs something real. It is distinguished from routine out-of-scope decisions by the acknowledgment of cost: a real user wants it, a real argument exists for it, and the team refuses anyway because building it would compromise the product's point of view.
*Common error:* Describing it as simply "refusing features."
*Chapter reference:* Ch. 20, "The $100,000 No."

---

**Ex 6** — *Scope discipline compounds*
*Model answer:* Each refusal preserves coherence. Coherence becomes identity. Identity becomes brand. Brand attracts users who value the specific coherence, deepening it further. The inverse: accepting scope-compromising features spends coherence for cash, accumulating incoherence that drives away original users.
*Common error:* Describing scope discipline as "keeping the product simple" rather than as preserving coherence.
*Chapter reference:* Ch. 20, "Scope Discipline as Identity: The Linear Case."

---

**Ex 7** — *Problem section rewrite*
*Model answer:* Strong rewrite includes: specific user (intermediate language learner using 2+ apps), specific task (comparing vocabulary status across apps), specific cost (15–20 min reconciliation per session), specific failure mode (re-studying known words or losing retention in gaps).
*Common error:* Adding a specific user type but omitting the task and failure mode.
*Chapter reference:* Ch. 20, "What a PRD Actually Is — Section 1."

---

**Ex 8** — *MVP Boundary error analysis*
*Error:* In-scope list is overloaded with multi-user features, dashboards, Slack integration, historical analysis, social media monitoring — none of which test the core hypothesis.
*Misconception:* Treating the MVP Boundary as a feature roadmap rather than the smallest testable version.
*Corrected version:* In scope: RSS feeds, sentiment scoring, Google Sheets output, email notification. Out scope: multi-user, social media, dashboards, Slack, historical analysis. $100,000 no: multi-user (changes product category).
*Chapter reference:* Ch. 20, "What a PRD Actually Is — Section 4."

---

**Ex 9** — *AI Interaction — validated learning*
*Model answer:* Strongest: real stakes produce real behavioral data. Gap: AI omits the pre-specified hypothesis requirement. Extension: validated learning requires knowing the hypothesis before building. Behavioral metric: three opens/week after first two weeks of use.
*What a strong answer includes:* The specific hypothesis-first requirement; a behavioral (not attitudinal) metric tied to the problem statement.
*Chapter reference:* Ch. 20, "What 'Minimum Viable Product' Actually Means."

---

**Ex 10** — *Self-explanation: false constraints*
*Model answer:* "How" decisions in the PRD become requirements. When implementation must change, the PRD becomes a source of false constraints — boundaries on engineering decisions that were never product requirements. This forecloses options the PRD had no authority to foreclose.
*Common error:* Describing the problem as engineers not wanting to be told what tools to use.
*Chapter reference:* Ch. 20, "What a PRD Actually Is."

---

**Ex 11** — *Cumulative: archetype as forcing function + $100,000 no*
*Model answer:* The archetype provides the point of view from which refusals are principled rather than arbitrary. Without archetype, the question is "is this a good feature?" — almost always yes. With archetype, the question is "does this feature belong in this product for this user given what this product is for?" The archetype makes the no defensible under pressure.
*Common error:* Treating the $100,000 no as a budget/capacity decision.
*Chapter reference:* Ch. 20, "The $100,000 No"; Ch. 1, "Archetypes as Forcing Functions."

---

**Ex 12** — *Gap section rewrite*
*Model answer:* Strong rewrite names QuickBooks, FreshBooks, and spreadsheets with specific failure modes for each. Implies the gap: revenue-minus-time-minus-expenses profitability view, in non-accountant language, without manual entry.
*Common error:* Adding competitor names without specific failure modes.
*Chapter reference:* Ch. 20, "What a PRD Actually Is — Section 2."

---

**Ex 13** — *Testable hypothesis vs. vision statement*
*Model answer:* (a) Testable. (b) Vision. (c) Testable. (d) Vision.
*Common error:* Labeling (b) as testable because "you can check market position."
*Chapter reference:* Ch. 20, "What 'Minimum Viable Product' Actually Means."

---

**Ex 14** — *PRD as contract with future-self*
*Model answer:* Resists scope creep under commercial and social pressure. Example: $12,000 enterprise offer for multi-user accounts — the PRD's $100,000 no preserved the reasoning made when thinking clearly, before pressure.
*Common error:* Describing the PRD as preventing "bad ideas" generically.
*Chapter reference:* Ch. 20, "What the PRD Is Actually Doing."

---

**Ex 15** — *Synthesis: scope discipline + brand equity*
*Model answer:* Each refusal preserves the specific experience that accumulated the equity. Inverse condition: scope discipline erodes equity when not grounded in archetype — produces rigidity without coherence. Linear case: refusals are legible as "this is what the product is for"; arbitrary refusals are just unhelpfulness.
*What a strong answer includes:* Specific mechanism of equity accumulation through refusals; the inverse condition; Linear case applied.
*Common error:* Missing the inverse condition.
*Chapter reference:* Ch. 20, "Scope Discipline as Identity"; Ch. 6, "Archetypes as Brand Equity."

---

**Ex 16** — *Synthesis: negative-space rule + $100,000 no*
*Model answer:* Genuine analogy: both treat refusal as an active identity claim. Differences: (1) stakes — portfolio identity vs. commercial and operational commitments; (2) timing — retrospective (existing projects) vs. prospective (written before pressure); (3) external pressure — negative-space rule operates without external advocacy; $100,000 no is specifically designed to survive a real user's real request.
*What a strong answer includes:* The genuine analogy named; at least one specific difference with concrete illustration.
*Common error:* Only describing similarities, not engaging the structural differences.
*Chapter reference:* Ch. 20, "The $100,000 No"; Ch. 18, "Curation and negative space."

---

**Ex 17 — Challenge**
*No model answer provided.*
*A strong response will address:*
- Stage 1: Does the student have a specific user (can name ten people who fit the description) and a specific archetype (can name a feature request they would decline and explain why it contradicts the archetype)?
- Stage 2: Can the student explain the $100,000 no in terms of what the product would become if the refused feature were built — and is that transformation clearly undesirable given the user and archetype?
- Stage 3: If the student cannot answer Stage 2 clearly, they do not yet have the required point of view — the diagnostic should recommend returning to the PRD's Problem section and the archetype work before attempting the $100,000 no
*This question is intentionally open-ended. Discuss your response with a peer or instructor to evaluate your reasoning.*

---

## Self-Assessment Rubric

| Score | Meaning | Next step |
|---|---|---|
| Tier 1 complete, most correct | Core concepts in place | Move to Tier 2 |
| Tier 2 mostly correct | Applying concepts well | Move to Tier 3 |
| Tier 2 struggling (>2 wrong) | Gaps in application | Return to flagged sections, then redo Tier 2 |
| Tier 3 attempted and close | Strong conceptual understanding | Proceed to Tier 4 |
| Tier 3 missed the integration | Concepts learned in isolation | Revisit the prior chapter referenced in the question |
| Tier 4 attempted seriously | Ready for advanced work | Compare with a peer or discuss with instructor |

*Tiers 3 and 4 are not required for all students in all courses. Check your syllabus for which tiers are assigned.*
