# Chapter Quiz: Pipelines & Workflow (on Madison)

*Chapter 21 (Appendix S2) of Branding and AI: Building the Creative Engineer*

> **Instructions:** Attempt every question before checking the answer key.
> Do not look at the answers while working — the act of retrieval is the
> learning. If you are unsure, make your best attempt and mark it with (?).
> Review the answer key after completing all questions, not after each one.

---

## Learning Objectives Covered

This quiz assesses the following chapter objectives:

- Explain why a pipeline is a chain of contracts rather than a piece of code, and what this means for reliability
- Classify a pipeline as ETL, stream-processing, workflow-automation, or inference
- Apply the three survival disciplines (document, design degraded modes, monitor) to a real pipeline scenario
- Explain the Apollo/Reddit damage asymmetry and its mechanism
- Identify the four degraded-mode levels and select the appropriate one for a given failure scenario

---

## Section 1 — Recall and Recognition (Questions 1–5)

*Target: Bloom's Remember / Understand*
*Format: Multiple-choice (3 options) and True/False*
*Target difficulty: p = 0.77–0.85*

---

**Question 1** *(Multiple-Choice)*

The chapter argues that a data pipeline is not primarily a piece of code — it is something else. What is the chapter's definition?

A) A pipeline is a deployment artifact: a set of configuration files that define how services are composed and scheduled in production.
B) A pipeline is a chain of contracts — agreements between components about how data flows, in what shape, at what cost, subject to what rate limits, each owned by someone else and subject to change without consent.
C) A pipeline is a workflow specification: a formal definition of the sequence of steps that transforms raw data into a product output.

---

**Question 2** *(True/False)*

The chapter classifies the Madison Intelligence Agent as a stream-processing pipeline, because it continuously processes articles from RSS feeds in near-real-time.

☐ True  ☐ False

---

**Question 3** *(Multiple-Choice)*

The chapter names three survival disciplines for managing pipeline contracts. Which answer correctly names all three?

A) Test every node, version-control the workflow, and document the deployment environment.
B) Document every external dependency before building on it, design a degraded mode for every critical dependency, and monitor the contracts (not just the workflow execution).
C) Use only stable open-source dependencies, avoid proprietary APIs, and run the workflow on self-hosted infrastructure.

---

**Question 4** *(Multiple-Choice)*

The chapter describes four levels of degraded mode, in increasing order of robustness. Which answer correctly names them in order?

A) Error logging, service restart, fallback API, and graceful shutdown.
B) Informative failure, partial degradation, fallback source, and graceful staleness.
C) Silent failure, retry logic, circuit breaker, and manual override.

---

**Question 5** *(True/False)*

In the Apollo/Reddit case, both Apollo and Reddit experienced approximately equivalent brand damage — Apollo lost its product while Reddit lost its reputation as a developer-friendly platform.

☐ True  ☐ False

---

## Section 2 — Application and Analysis (Questions 6–9)

*Target: Bloom's Apply / Analyze*
*Format: Multiple-choice (3 options) and Short-Answer*
*Target difficulty: p = 0.50–0.70*

---

**Question 6** *(Scenario-Based Multiple-Choice)*

A student's n8n pipeline pulls articles from a Twitter API, scores them with GPT-4o-mini, and writes results to Google Sheets. Three months after launch, Twitter changes its API pricing, making the student's usage unaffordable. Users see no update in the Google Sheet that day and email the student asking if the tool is broken. Which degraded mode would have produced the best user experience at the moment of contract failure, and why?

A) Graceful staleness — the tool continues to serve the most recent valid Sheet update with a visible timestamp, and users see that the data is stale rather than the tool appearing broken, buying time for the student to find an alternative source or contact users proactively.
B) Silent failure — the system should absorb API failures without bothering users, who will simply check back later when the problem is resolved.
C) Informative failure — the tool immediately shows users a message that the Twitter API is unavailable and that the situation is being investigated, even if no data has been served that day.

---

**Question 7** *(Short-Answer)*

The chapter describes n8n's key architectural advantage for pipelines: each node is independently replaceable. Explain why this property is specifically valuable for managing contract risk, using the example of swapping one API node for another.

*Your answer:*

_____________________

---

**Question 8** *(Multiple-Choice)*

The chapter argues that the Apollo/Reddit case illustrates a pattern where "damage flows downhill" in a contract chain. What is the specific mechanism the chapter identifies?

A) Third-party apps receive negative press coverage whenever a platform changes its API, regardless of their quality.
B) The largest, most diversified party (Reddit) absorbs diffuse reputational damage spread across a large user base; the smallest, most dependent party (Apollo) absorbs concentrated, immediate, product-killing damage because users see "this tool stopped working" rather than "upstream contract failure."
C) Platform API changes are always legally the responsibility of the downstream developer, who accepted the API terms of service and therefore bears the full reputational consequence.

---

**Question 9** *(Short-Answer)*

The chapter's four-node build pipeline (Schedule Trigger → HTTP Request → Code: Transform + Deduplicate → Google Sheets) has specific contracts at each node. Name the three external contracts this pipeline depends on and describe, for each, what the documented contract should specify.

*Your answer:*

_____________________

---

## Section 3 — Synthesis and Evaluation (Questions 10–11)

*Target: Bloom's Evaluate / Create*
*Format: Short-Answer or Brief-Response*
*Target difficulty: p = 0.30–0.50*

---

**Question 10** *(Brief-Response)*

The chapter's "Still Puzzling" section admits it does not yet have a principled framework for deciding when to accept a fragile-but-rich contract versus a stable-but-limited one. Evaluate the chapter's working heuristic: "If the contract is controlled by a single platform, budget for its failure from day one." Is this heuristic sufficient, or does it still leave a decision that the builder must make explicitly? What additional factor, not named in the heuristic, would most improve its precision?

*Your response (2–4 sentences):*

_____________________

---

**Question 11** *(Transfer — Brief-Response)*

The chapter applies Joan Robinson's concept of monopsony to explain why Apollo had no leverage when Reddit changed its pricing. Apply this same economic structure to a different scenario: a small publishing house that depends on a single major book distributor for 80% of its sales. The distributor changes its terms, increasing its cut from 40% to 55% of cover price. What does Robinson's monopsony analysis predict about the publisher's options, and what would the chapter's three survival disciplines recommend the publisher have done before this moment arrived?

*Your response (2–4 sentences):*

_____________________

---

## Answer Key

> Read this section only after completing all questions.

---

**Q1 — B**
*Correct because:* The chapter's opening reframe is that a pipeline is not primarily code; it is "a chain of contracts, each owned by someone else, each subject to change without your consent." The pipeline runs as long as every agreement holds and breaks when one agreement fails. This frame is the thesis the entire appendix builds on.
*Why the distractors are wrong:*
- A) A deployment artifact or configuration file is a technical description of how a pipeline is specified, not the chapter's conceptual reframe.
- C) A workflow specification is a related concept but does not capture the chapter's key insight about external ownership and change risk.
*Chapter reference:* A pipeline is a chain of contracts

---

**Q2 — False**
*Correct because:* The chapter explicitly classifies the Madison Intelligence Agent as a workflow-automation pipeline with an inference step (Pattern 3 and 4 working together), run on a six-hour schedule — not real-time or near-real-time. Stream-processing pipelines are for continuous flows processed in near-real-time (e.g., fraud detection at ten thousand transactions per second). The chapter notes the six-hour cadence is a contract-aware scheduling decision.
*Chapter reference:* Four kinds of data pipeline / Reading Madison

---

**Q3 — B**
*Correct because:* The chapter names three disciplines explicitly: document every external dependency before building on it (forces conscious confrontation with the contract); design a degraded mode for every critical dependency (answers "what does the product do when this fails?"); and monitor the contracts, not just the workflow execution (alerts on contract-level events like rate limit changes, pricing shifts, and terms updates).
*Why the distractors are wrong:*
- A) Testing, version control, and deployment documentation are engineering practices but are not the three survival disciplines the chapter names.
- C) Avoiding proprietary APIs and using self-hosted infrastructure are related strategies but are not the chapter's three named disciplines.
*Chapter reference:* Three survival disciplines

---

**Q4 — B**
*Correct because:* The chapter names four levels in increasing order of robustness: informative failure (detects the break and shows the user a clear message rather than an opaque error — the minimum viable degraded mode), partial degradation (the broken feature is disabled while the rest continues), fallback source (the broken dependency is replaced by an alternative), and graceful staleness (continues to serve the last successful result with a visible timestamp — stale data is usually better than no data).
*Why the distractors are wrong:*
- A) Error logging, service restart, fallback API, and graceful shutdown are not the chapter's four levels.
- C) Silent failure, retry logic, circuit breaker, and manual override are related engineering patterns but not the chapter's degraded-mode taxonomy.
*Chapter reference:* Three survival disciplines / degraded mode taxonomy

---

**Q5 — False**
*Correct because:* The chapter explicitly describes an asymmetry: "Reddit — the upstream actor that caused the failure — received diffuse reputational damage spread across a large company with hundreds of millions of users. Apollo, Reddit Is Fun, and ReddPlanet — the downstream tools — received concentrated, immediate, product-killing damage." The damage was highly asymmetric in favor of the larger party. Christian Selig personally emerged with his reputation strengthened, but Apollo the product died.
*Chapter reference:* Apollo as a brand story / damage asymmetry

---

**Q6 — A**
*Correct because:* Graceful staleness is the most appropriate degraded mode in this scenario because the tool was providing value through current data; stale data from the previous day or week is still more useful than no data, and a visible timestamp tells users the data is stale rather than leading them to conclude the tool is broken. Informative failure (Option C) could work as a minimum viable fallback, but graceful staleness with a timestamp provides better user experience by serving something useful rather than nothing. The chapter notes: "Stale data is usually better than no data, as long as the staleness is legible."
*Why the distractors are wrong:*
- B) Silent failure is the worst degraded mode — users see the tool as broken, cannot distinguish contract failure from technical failure, and lose trust without any explanation.
- C) Informative failure is viable as a minimum but graceful staleness, by also serving the last successful result, provides more value than informative failure alone.
*Chapter reference:* Three survival disciplines / degraded mode taxonomy / graceful staleness

---

**Q7 — Short-Answer**
*Model answer:* In a single Python script with multiple API calls interwoven, the contracts are embedded throughout the code — swapping one API for another may require touching many parts of the file, and it is not obvious where the dependency boundary is. n8n's node architecture makes every contract a separately labeled, independently replaceable node with clearly defined inputs and outputs. When OpenAI changes its pricing, the student can swap the OpenAI node for a Claude node without touching the data-ingestion nodes, the transformation logic, or the output nodes. The contract is visible as a discrete unit, which means the student can reason about it before it fails ("this node has a pricing risk") and isolate it when it does fail ("the error is in this specific node, not the whole workflow"). This is the chapter's argument that visual workflows make contracts structurally visible in a way that scripts require deliberate discipline to achieve.
*What a strong answer includes:*
- The contrast with a monolithic script where contracts are interwoven
- The specific benefit: isolatable, swappable nodes for each dependency
- The connection between visibility and reasoning / debugging
*Chapter reference:* Building it in n8n / independent replaceability

---

**Q8 — B**
*Correct because:* The chapter's damage-asymmetry argument is specific: the upstream party is large and diversified, so reputational damage spreads across many millions of users and many products — diffuse damage. The downstream party is small and entirely dependent on the upstream contract, so when the contract fails, the downstream product fails entirely — concentrated damage. The user sees "this tool stopped working," not "upstream contract failure," so the brand damage flows to the name on the front page.
*Why the distractors are wrong:*
- A) Press coverage is a mechanism of damage propagation but not the chapter's explanation of why the asymmetry exists.
- C) Legal responsibility is not the chapter's explanation; the asymmetry is economic and perceptual, not legal.
*Chapter reference:* Apollo as a brand story / damage asymmetry mechanism

---

**Q9 — Short-Answer**
*Model answer:* The four-node pipeline has three external contracts: (1) The Schedule Trigger's contract with time — documented as "runs hourly; if n8n is down, the run is skipped and not retried unless a catch-up mechanism is added." The documentation should specify that n8n's own availability is a contract and has failure modes. (2) The HTTP Request node's contract with the Hacker News RSS feed — documented as "no authentication required, no rate limit documented, stable Atom format since 2006, risk: low." Should specify the URL, authentication requirement, rate limit (if any), data format, and the historical stability of the format as a risk indicator. (3) The Google Sheets node's contract with Google's API — should specify the OAuth credential, the rate limits for Google Sheets API calls, the data schema expected by the target sheet, and what the degraded mode is if Google credentials expire or the sheet is deleted.
*What a strong answer includes:*
- All three external contracts identified
- The documentation format (what the service provides, cost, rate limit, terms)
- A specific degraded mode note for at least one
*Chapter reference:* Building it in n8n / four-node pipeline / document the contract

---

**Q10 — Brief-Response**
*Model answer:* The heuristic ("if controlled by a single platform, budget for its failure from day one") is necessary but not sufficient — it tells you when to be worried but not what to do about it. The key factor the heuristic does not address is the substitutability of the contract: a single-platform contract that has a realistic alternative (another social media platform's API, a competing search engine's data) is meaningfully different from one that has no alternative (the only source of Reddit data is Reddit's API). The additional factor that would most improve precision is: whether a genuinely equivalent alternative exists that the product could switch to without fundamental redesign. If yes, budgeting for failure means building a swappable architecture; if no, budgeting for failure means either accepting the structural constraint with eyes open or avoiding the dependency entirely.
*What a strong answer includes:*
- Acknowledgment of what the heuristic does well (identifies risk)
- The missing factor (substitutability / existence of alternatives)
- A practical implication for design
*Chapter reference:* Still Puzzling / contract stability heuristic

---

**Q11 — Transfer Brief-Response**
*Model answer:* Robinson's monopsony analysis predicts that the publisher has no leverage: with 80% of sales through one distributor, the publisher has no credible threat to walk away, so the distributor can change terms unilaterally and extract whatever margin the publisher can afford to pay rather than exit. This is the same structural position Apollo occupied with Reddit — one buyer, no realistic alternative, terms set unilaterally. The chapter's three survival disciplines would have recommended: (1) documenting the contract terms (acknowledging the 40% cut, the distributor's renewal rights, and the "subject to change" reality) before becoming dependent; (2) designing a degraded mode — in this context, a direct-sales channel, a second distributor covering even 20% of sales, or an e-commerce capability — so that a rate increase does not produce a binary choice between acceptance and shutdown; and (3) monitoring the relationship (tracking the distributor's communications about industry trends, term renegotiations with other publishers, signals of margin pressure in their own business) as early warning before a formal notice arrives.
*What a strong answer includes:*
- Robinson's monopsony mechanism applied to the publishing context
- Application of all three survival disciplines to the publisher scenario
- The parallel to Apollo's structural position
*Chapter reference:* Pipeline as contract / three survival disciplines / Apollo damage asymmetry / AI Wayback Machine — Joan Robinson (transfer application)

---

## Self-Assessment Rubric

After reviewing the answer key, score yourself:

| Score | Meaning | Next step |
|---|---|---|
| 9–11 / 11 | Strong retention — ready to move on | Proceed to the next chapter |
| 7–8 / 11 | Partial mastery — specific gaps present | Return to the sections flagged in wrong answers |
| 5–6 / 11 | Foundational gaps | Reread the chapter, then retake the quiz |
| Below 5 / 11 | Chapter concepts not yet consolidated | Reread, then work through the exercises before retaking |

*Note: Section 3 questions are weighted more heavily. Getting Q10 and Q11 wrong while getting Sections 1–2 right is a signal of surface-level knowledge — not mastery.*

---

## Instructor Notes

**Bloom's distribution for this quiz:**

| Level | Questions | % of Quiz |
|---|---|---|
| Remember / Understand | Q1–Q5 | ~45% |
| Apply / Analyze | Q6–Q9 | ~36% |
| Evaluate / Create | Q10–Q11 | ~18% |

**Psychometric targets:**
- Section 1 items: p-value target 0.77–0.85; r_pb ≥ 0.30
- Section 2 items: p-value target 0.50–0.70; r_pb ≥ 0.30
- Section 3 items: p-value target 0.30–0.50; r_pb ≥ 0.40

**Common errors to watch for in student work:**

- Treating "monitoring the workflow" as equivalent to "monitoring the contracts" — students miss that a workflow can execute successfully while an underlying contract is silently degrading.
- Misidentifying informative failure as the strongest degraded mode (it is the minimum viable level, not the most robust).
- Describing the Apollo damage asymmetry in terms of press coverage or public relations rather than the structural concentration-vs-diffusion mechanism.

**Signs a student needs to return to the chapter before this quiz:**

- Cannot name the four pipeline categories and distinguish workflow-automation from ETL.
- Does not understand why n8n's node architecture makes contracts visible in a way that script-based pipelines do not.

**Scaffolding adjustments:**

- *For students who score below 5:* Walk through the Apollo case as a contract-analysis exercise — identify the contract, who owned it, how it changed, and what each party experienced — before engaging the degraded-mode taxonomy.
- *For students who score 11/11 on first attempt:* Ask them to complete the chapter's "break it on purpose" exercise: trigger a deliberate contract failure in their n8n pipeline (point the HTTP Request at a bad URL), document what happened, and implement at least one of the four degraded modes as a real code change in the workflow.
