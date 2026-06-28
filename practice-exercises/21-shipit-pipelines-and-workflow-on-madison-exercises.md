# Chapter 21: ShipIt — Pipelines and Workflow on Madison — Practice Exercises

*INFO 7375 · Branding and AI · Northeastern University*

---

> **How to use these exercises:**
> Work through each tier in order. Do not skip ahead to later tiers before completing earlier ones — the tiers scaffold your understanding. Attempt every exercise before checking the answer key. For open-ended questions, write at least 2–3 sentences before reading the model answer. The act of attempting is where the learning happens.

---

## Learning Objectives

- Distinguish the four pipeline types (ETL, streaming, workflow-automation, inference) and match each to its appropriate use case
- Explain why a pipeline is a chain of contracts rather than primarily a piece of code
- Apply the Apollo/Reddit case to understand damage asymmetry in contract chains
- Design and implement the three survival disciplines: document every dependency, design degraded modes, monitor contracts
- Apply the four degraded mode levels (informative failure, partial degradation, fallback source, graceful staleness) to a given pipeline scenario
- Build a working n8n workflow pipeline

*Every exercise below maps to at least one of these objectives. The `(Tests: ...)` tag on each exercise identifies which one(s) by full concept name.*

---

## Worked Example

*Study this example before attempting Tier 1. After reading it, close it and try to recall the key steps from memory before moving on.*

**Problem:** Isabelle is building a tool that tracks price changes for a small set of competitor products by scraping their public pricing pages daily. She plans to use a single Python script that: (1) fetches each competitor's pricing page, (2) extracts prices using CSS selectors, (3) compares to yesterday's stored prices, and (4) sends an email if any prices changed. What are the external contracts this pipeline depends on, and what degraded mode should she design for each?

**Approach:**
- Step 1 — Identify every external dependency. Each pricing page is an HTTP resource — its contract includes: the page will respond, the page's HTML structure will remain consistent (CSS selectors will still select the right elements), the pricing information will be in a machine-readable format, and the site will not block automated requests. Email sending (Step 4) depends on an email service contract: the service will accept outbound email, deliver it, and not flag it as spam.
- Step 2 — Document each contract. Pricing pages: "5 competitor pricing pages — HTML scraping via CSS selectors; no authentication required; risk: HIGH (pages can restructure without notice, CDN may block scrapers, prices may be in dynamically loaded JavaScript rather than static HTML)." Email service: "SMTP via Gmail or SendGrid — low risk, stable contract, rate limit: typically 100–500 per day."
- Step 3 — Design degraded modes for the highest-risk contracts. Pricing page scraping is the fragile contract. Degraded modes in increasing order of robustness: (a) Informative failure — if a scrape fails, the tool logs the failure with timestamp and notifies Isabelle "Competitor A page failed to parse today — check manually" rather than silently skipping or crashing. (b) Partial degradation — if one competitor's page fails, the tool continues scraping and reporting on the others; only the failed competitor's data is missing that day. (c) Fallback source — if the pricing page restructures, check whether the competitor publishes pricing in a press release, an RSS feed, or a structured data API as an alternative source. (d) Graceful staleness — if the page is temporarily unreachable, serve yesterday's price with a "[price as of yesterday — check manually for today]" flag.

**Answer:** Isabelle's pipeline depends on five pricing page contracts (high risk — HTML structure, scraper blocking, JavaScript rendering) and one email service contract (low risk — stable, standard). For the high-risk contracts, she should implement at minimum: informative failure (log and notify on any parse failure) and partial degradation (continue with available pages). She should document both the risk level and the degraded mode in the workflow itself, not in a separate wiki.

**What to notice:** The pipeline is not primarily a script — it is a set of agreements Isabelle does not control. The Python code is implementation; the contracts are the infrastructure. Designing for contract failure before writing the code is the discipline that separates a pipeline that is still running six months later from one that breaks silently.

---

## Tier 1 — Warm-Up (Exercises 1–6)

*Bloom's Level: Remember / Understand*
*Purpose: Verify that the chapter's core concepts and vocabulary are in place before you apply them.*

---

**Exercise 1**

Name the four pipeline categories. For each, write one sentence describing the appropriate use case and one sentence describing a use case where it would produce the wrong result.

*(Tests: four pipeline types — use cases and discriminations)*

**Answer:** (1) ETL (Extract, Transform, Load): appropriate for large-scale batch data engineering — pulling data from sources, cleaning it, and writing it to a warehouse for long-term analysis. Wrong for: real-time event processing (the batch orientation introduces latency that makes ETL unsuitable for fraud detection or live recommendation updates). (2) Stream processing: appropriate for high-throughput, low-latency continuous event flows — payment fraud detection, real-time recommendation updates. Wrong for: small-scale projects where operational complexity (Kafka, Flink) far exceeds the volume and latency requirements. (3) Workflow automation (n8n, Zapier, Make): appropriate for small teams connecting multiple external APIs, scheduling tasks, and gluing services together without heavy infrastructure. Wrong for: processing millions of events per second where throughput and latency matter, or where the visual graph is too complex to maintain. (4) Inference pipeline: appropriate for workflows where an LLM call processes, classifies, or synthesizes content as a step in a larger pipeline. Wrong for: use as a primary data retrieval or transformation mechanism where deterministic logic would be faster, cheaper, and more reliable.

**Common error:** Treating stream processing and inference pipelines as alternatives. They are on different dimensions — stream processing is about throughput and latency; inference pipelines describe how AI reasoning is integrated. Madison's architecture uses both types 3 and 4 together.

*Chapter reference:* Chapter 21, "Four kinds of data pipeline."

---

**Exercise 2**

True / False: A pipeline that runs successfully — every node returns 200, every connection passes data — is definitively reliable, because all its contracts are holding.

*Explain your reasoning in one sentence:*

*(Tests: pipeline as chain of contracts — contract-level vs. execution-level monitoring)*

**Answer:** False. A pipeline can run successfully at the execution level while the underlying contracts are silently degrading: rate limits may be creeping down, pricing tiers may have shifted, schema fields may have been deprecated without announcement, terms of service may have been updated. Monitoring workflow execution confirms that the pipeline ran; it does not confirm that the contracts on which it depends remain stable and aligned with the product's needs.

**Common error:** Agreeing because "if 200 returns and data passes, the contract is holding." The chapter distinguishes execution success from contract stability — a rate limit reduction, for example, does not cause an immediate execution failure but changes the contract in a way that will eventually break the pipeline.

*Chapter reference:* Chapter 21, "Three survival disciplines."

---

**Exercise 3**

In your own words, explain the *damage asymmetry* the Apollo/Reddit case illustrates. Who absorbed what kind of damage, and why is the distribution asymmetric?

*(Tests: Apollo/Reddit — damage asymmetry in contract chains)*

**Answer:** Reddit (the upstream actor that changed the contract) absorbed diffuse, reputational damage spread across a large company with hundreds of millions of users — the damage was distributed and absorbed by a platform with broad defensive surface. Apollo (the downstream actor most dependent on the contract) absorbed concentrated, product-killing damage: the product shut down in 30 days, and users who had paid for premium features lost their tool. Christian Selig personally maintained his reputation through transparency, but the product died. The distribution is asymmetric because damage flows downhill in a contract chain: the largest, most diversified party absorbs a spread; the smallest, most dependent party absorbs everything. Apollo had no realistic alternative source for Reddit data — its entire product value was built on a single platform's API. The platform's business-model shift was the earthquake; Apollo was the structure built on fault lines it could not control.

**Common error:** Describing the asymmetry as "Reddit is bigger than Apollo." The mechanism is not size — it is concentration of dependency. A large downstream actor with diversified contracts would absorb less damage than Apollo did. The asymmetry is produced by dependency concentration, not by organizational scale.

*Chapter reference:* Chapter 21, "Apollo as a brand story."

---

**Exercise 4**

Label each of the following degraded modes according to the chapter's four-level taxonomy (informative failure, partial degradation, fallback source, graceful staleness). Then rank them from least to most robust.

(a) When the Reddit API fails, the tool continues to serve the last successfully retrieved posts with a banner: "Content last updated 6 hours ago — Reddit API currently unavailable."
(b) When the Reddit API fails, the tool displays: "Reddit feed unavailable — checking status. Other content sources are loading normally."
(c) When the Reddit API fails, the tool automatically switches to fetching from the subreddit's RSS feed instead.
(d) When the Reddit API fails, the tool disables the Reddit section while the rest of the dashboard (Twitter feed, blog RSS) continues normally.

*(Tests: four degraded modes — classification and ranking)*

**Answer:** (a) Graceful staleness — serves last successful result with visible timestamp/indicator. (b) Informative failure — detects the break and shows the user a clear message about what is unavailable and why, rather than an opaque error. (c) Fallback source — broken dependency is replaced by an alternative (subreddit RSS). (d) Partial degradation — the feature depending on the broken contract is disabled while the rest continues. Ranking from least to most robust: informative failure (b) < partial degradation (d) < graceful staleness (a) < fallback source (c). Note: the chapter lists them in this order as "increasing order of robustness," though the exact ranking of (a) and (d) may legitimately depend on context — staleness may be more or less useful than partial degradation depending on how critical that data source is.

**Common error:** Ranking informative failure as least robust and therefore least important. The chapter is clear that informative failure is "the minimum viable degraded mode" — it is least robust but not optional; it is the floor, not an optional extra.

*Chapter reference:* Chapter 21, "Three survival disciplines — degraded modes."

---

**Exercise 5**

The chapter describes n8n's key architectural property as making contracts *visible* in a way that monolithic scripts do not. In your own words, explain what this means and why it matters for pipeline reliability.

*(Tests: n8n workflow automation — contracts visible, independently replaceable nodes)*

**Answer:** In a monolithic Python script, each external dependency (API call, database write, transformation step) is embedded inside the code — the dependencies are interwoven, and swapping one API for another may require touching multiple parts of the file. When something breaks, the failure point is not obviously localized. In an n8n workflow, every dependency is a separately labeled node with a defined input and output. The contracts (what each service provides, at what cost, under what rate limit, subject to what terms) are visible in the workflow graph — you can inspect which node calls which external service without reading code. When a contract changes (OpenAI raises prices, Reddit's API breaks), you identify the specific node that implements that contract and replace it without touching adjacent nodes. This visibility matters for reliability because you can reason about contract failure before it happens (which nodes are highest risk?) and isolate failures when they do happen (which node failed, and what does its degraded mode do?).

**Common error:** Describing n8n as "easier to use than Python." The chapter's argument is architectural — it is about which representation makes contracts visible and independently addressable, not about which tool is more user-friendly.

*Chapter reference:* Chapter 21, "Building it in n8n."

---

**Exercise 6**

The chapter identifies the Apollo case as "a business failure, not a pipeline-design failure" — but simultaneously argues that the three survival disciplines would have changed the outcome. Explain in two sentences what the survival disciplines could and could not have done for Apollo.

*(Tests: three survival disciplines — scope and limits of the disciplines)*

**Answer:** The three survival disciplines — document the contract, design degraded modes, monitor the contract — could have given Apollo earlier warning of the pricing shift (monitoring for contract changes) and would have produced a product that communicated the failure to users clearly and managed degradation gracefully (informative failure, partial degradation). What the survival disciplines could not have done: they cannot address the structural monopsony problem. Apollo depended on Reddit data with no viable alternative source, and no amount of contract documentation, degraded mode design, or monitoring changes the fact that Reddit held all pricing power. The disciplines manage the consequences of contract failure; they cannot prevent a platform from choosing to make the tool economically unviable.

**Common error:** Claiming the survival disciplines would have "saved Apollo." The chapter distinguishes: the disciplines address "smaller, more tractable failure modes" — rate limit changes, schema updates, pricing tier shifts. The Apollo failure was a business model shutdown, which is a structural constraint the disciplines cannot address.

*Chapter reference:* Chapter 21, "Three survival disciplines" and conclusion section.

---

## Tier 2 — Application (Exercises 7–14)

*Bloom's Level: Apply / Analyze*
*Purpose: Use the chapter's concepts in realistic situations.*

---

**Exercise 7** *(Scenario-Based Application)*

Priya is building a workflow automation pipeline that aggregates job postings for AI engineer roles from three sources: LinkedIn's API, Indeed's data feed, and a set of company career page RSS feeds. She has not yet documented the contracts.

For each of the three sources, write a one-sentence contract documentation entry in the format the chapter specifies: what the service provides, what it costs, what its rate limit is, and what your degraded mode is.

*(Tests: document every dependency — contract documentation format)*

**Answer:** (1) LinkedIn Jobs API: "LinkedIn Jobs API — provides structured job posting data by keyword and location; pricing and access tier: requires LinkedIn partner API access (not publicly available without approval, cost varies by tier); rate limit: varies by partnership tier; risk: HIGH — access requires application and approval, terms prohibit scraping; degraded mode: if LinkedIn API becomes unavailable or requires re-approval, switch to LinkedIn RSS feed for saved searches as fallback." (2) Indeed data feed: "Indeed Publisher API — provides job posting data by keyword/location; pricing: free for non-commercial use with attribution, commercial use requires publisher account; rate limit: 25 results per query, 250 queries per day on free tier; risk: MEDIUM — free tier is subject to Indeed's business model decisions, similar to Twitter API; degraded mode: switch to indeed.com RSS feeds for saved searches, which are stable and require no authentication." (3) Company career page RSS: "Company RSS feeds — direct career page feeds from target companies; cost: free; rate limit: none documented; risk: LOW — RSS is stable, no single provider can change the specification; degraded mode: informative failure if any individual company's feed is unreachable, with continued processing of available feeds."

**Common error:** Writing contract documentation that describes what the API does but omits the risk level and degraded mode. The chapter's format specifically includes the degraded mode as part of each entry, not as a separate document.

*Chapter reference:* Chapter 21, "Three survival disciplines — document the contract."

---

**Exercise 8** *(Error Analysis)*

> The following pipeline description was submitted by a student as their four-node n8n workflow design.

*"Node 1: Schedule trigger (daily at 8 a.m.). Node 2: HTTP Request to OpenAI API — sends all 50 RSS items from today's news to GPT-4 and asks for a daily summary. Node 3: Google Sheets write — writes the summary to a sheet. Node 4: Email notification — sends the summary to the user."*

1. Identify the primary pipeline design error.
2. Explain the contract risk this error creates.
3. Redesign the workflow to address the problem.

*(Tests: pipeline as chain of contracts — contract design and failure mode identification)*

**Answer:**
1. The primary error is in Node 2: sending all 50 RSS items to a single GPT-4 call. This is a fragile, expensive, and non-decomposable design — the entire pipeline's intelligence step is a single massive LLM call with a large context window, no intermediate validation, and maximum exposure to API failures.
2. Contract risks: (a) Cost risk — sending 50 items per call to GPT-4 at current pricing could cost $0.50–$2.00+ per daily run depending on item length; the chapter's worked example achieves similar results at under $0.80 per run by using GPT-4o-mini and processing items in scored batches rather than one enormous prompt. (b) Rate limit risk — a single call with a very large context is more likely to hit token limits or rate limits than distributed calls. (c) Failure scope — if this single call fails, the entire pipeline produces nothing; there is no intermediate output to fall back on. (d) Validation gap — the output of a single large synthesis call cannot be validated against any intermediate state, so errors in the summary cannot be attributed to specific source items.
3. Redesign: Node 1 (Schedule trigger) → Node 2 (HTTP Request: fetch RSS feeds — separate nodes per feed or a loop) → Node 3 (Code: deduplicate by URL) → Node 4 (Loop: for each deduplicated item, GPT-4o-mini call for per-item sentiment scoring and one-sentence summary) → Node 5 (Google Sheets write: append rows per item) → Node 6 (Code: generate daily digest from scored rows) → Node 7 (Email notification). This distributes the AI calls across items, enables per-item validation, and localizes failures to individual items rather than the entire daily output.

**Common error:** Identifying only the cost problem without noting the failure-scope problem. A strong error analysis includes both the cost contract risk and the pipeline design vulnerability.

*Chapter reference:* Chapter 21, "Building it in n8n" and Madison workflow design.

---

**Exercise 9** *(AI Interaction — with verification requirement)*

First, write your own answer without consulting AI:
*"What does 'graceful staleness' mean as a degraded mode, and when is stale data better than no data?"*

Then read the following AI-generated response:

*AI response: "Graceful staleness is a degraded mode where an application continues to serve cached or previously retrieved data when the live source is unavailable. It is better than showing an error page because users can still access the last known state of the data. Graceful staleness is most useful for dashboards and monitoring tools where some data is better than no data. The key is to show users when the data was last updated so they know it might be outdated. This approach is common in distributed systems design and is closely related to the CAP theorem's availability-consistency trade-off."*

1. Identify the strongest point in the AI's response.
2. Identify one gap or imprecision relative to the chapter's treatment.
3. Write a correction or extension.
4. State the specific test you would use to verify whether your pipeline's graceful staleness implementation is working correctly before deploying it.

*(Tests: four degraded modes — graceful staleness evaluation of AI output)*

**Answer:**
1. Strongest point: "Show users when the data was last updated so they know it might be outdated" — this captures the essential requirement of graceful staleness (legible staleness) accurately. The chapter is explicit: "Stale data is usually better than no data, as long as the staleness is legible."
2. Gap: The AI response does not mention the chapter's specific framing of graceful staleness as the *most robust* of the four degraded modes — the hierarchy (informative failure < partial degradation < fallback source < graceful staleness) is missing. The AI presents it as one option among alternatives, not as the highest-robustness tier of a ranked taxonomy. Also, the CAP theorem reference, while technically accurate, is not part of this chapter's framework and may distract from the pipeline-design-specific context.
3. Extension: "In the chapter's taxonomy, graceful staleness is the most robust degraded mode precisely because the tool continues functioning — the user receives actionable output (the last successful result) rather than nothing or a partial result. The key design requirement is making the staleness legible: a timestamp ('content last updated 6 hours ago'), a banner, or a colored indicator that the data may not be current. Without legible staleness, the degraded mode fails because the user cannot distinguish fresh data from stale data and may act on outdated intelligence."
4. Verification test: In your n8n workflow, disconnect the RSS source node (or point it at a bad URL). Verify that: (a) the pipeline does not crash — it completes with the stale data path; (b) the Google Sheet or output contains the last successful result, not a blank or an error message; (c) the output includes a visible timestamp or indicator showing when the data was last successfully retrieved; (d) a second test input that reconnects the source produces fresh data in the next run.

*Chapter reference:* Chapter 21, "Three survival disciplines — degraded modes."

---

**Exercise 10** *(Self-Explanation)*

In this chapter, a workflow automation pipeline (n8n) is used instead of a single Python script for building a data collection and processing workflow. Explain in 2–3 sentences why the chapter recommends n8n for this use case — not because n8n is easier to learn, but using the specific architectural reason the chapter identifies. Your explanation must use the term "independently replaceable."

*(Tests: n8n workflow automation — architectural reason for use vs. monolithic scripts)*

**Answer:** The chapter recommends n8n because it makes each external contract an independently replaceable node — a separately labeled unit with a defined input and output that can be swapped when the contract behind it changes, without modifying adjacent nodes. In a monolithic Python script, external dependencies are interwoven in the code; replacing one API call may require touching multiple parts of the file, and the failure point of a broken contract is not obviously localized. In an n8n workflow, when OpenAI's pricing changes and you want to switch to a different model provider, you replace the OpenAI node — the transformation and output nodes remain unchanged. This independence is the architectural property that makes the three survival disciplines (document, degrade, monitor) practical to implement on a per-contract basis.

**Common error:** Explaining n8n as "easier to use because it's visual." The chapter's architectural argument is specifically about contract visibility and independent replaceability — not about the visual interface's usability.

*Chapter reference:* Chapter 21, "Building it in n8n."

---

**Exercise 11** *(Cumulative — prior chapter concept)*

In Chapter 20, you learned about the *MVP Boundary* and the $100,000 no — the discipline of explicitly specifying what a product will not do in v1. In this chapter, you are working with the three survival disciplines and the decision about which external services to depend on at all.

A student is building an MVP pipeline that ingests social media sentiment about her personal brand. She is deciding whether to depend on the Twitter/X API (rich social data, but controlled by a single platform) or RSS feeds of blogs and forums in her field (less data, but stable contracts). Apply both the MVP Boundary discipline and the contract stability heuristic to help her decide.

*(Tests: contract stability heuristic + MVP Boundary — interleaved application)*

**Answer:** The MVP Boundary discipline asks: what is the smallest set of dependencies that allows the student to test her core hypothesis? Her core hypothesis for an MVP might be: "I can surface relevant mentions of my work and my field in a daily summary that helps me identify opportunities to engage." RSS feeds from relevant blogs and forums can test this hypothesis — they provide content she can process, score, and surface in a daily brief. Twitter/X data would be richer, but the chapter's contract stability heuristic warns explicitly: the Twitter API "failed all three criteria" (controlled by single platform, priced below value until business model shifted, changed unilaterally). For an MVP, the student should use RSS feeds: they satisfy the core hypothesis test, they are stable contracts that will not shut down her MVP before she can validate the hypothesis, and adding Twitter/X later (once the MVP's core value is validated) is a v2 decision that belongs in the out-of-scope list. The $100,000 no in this context is Twitter/X in v1: she would decline even if someone offered to set up the API credentials for her, because the contract fragility risk outweighs the data richness for an unvalidated MVP.

**Common error:** Recommending Twitter/X because "more data is better for testing." The MVP Boundary discipline is about the smallest test of the core hypothesis, not the most data-rich test. A hypothesis that requires Twitter/X data to test is a different hypothesis than one that can be tested with RSS.

*Chapter reference:* Chapter 21, "Three survival disciplines" and contract stability heuristic; Chapter 20, "MVP Boundary."

---

**Exercise 12** *(Scenario-Based Application)*

The chapter describes the Madison Intelligence Agent's design choice to run ingestion in parallel branches (RSS, Google News API, Reddit), each as a separate HTTP Request node. What specific failure mode does this design address, and what would happen to the pipeline's reliability if all three sources were collapsed into a single ingestion step?

*(Tests: pipeline design — parallel branches as degraded mode design)*

**Answer:** The parallel branch design addresses the failure mode that any single source can become unavailable or return malformed data without breaking the entire ingestion step. When each source is a separate node, a Reddit API failure affects only the Reddit branch — the RSS and Google News branches continue, and the pipeline produces a summary based on two sources rather than three. This is partial degradation implemented at the architecture level rather than the error-handling level. If all three sources were collapsed into a single ingestion step (for example, one HTTP Request node with three API calls in a single Python code block), a failure in any one source — a Reddit 429 rate limit error, a Google News API schema change — could cause the entire ingestion step to fail, producing no content for that run. The parallel branch design is degraded mode as architecture: the failure scope is limited to one branch by design, not by error handling.

**Common error:** Describing the parallel branches as a performance optimization (parallel execution = faster). The chapter's purpose for the design is failure isolation, not speed.

*Chapter reference:* Chapter 21, "Reading Madison + breaking it on purpose."

---

**Exercise 13** *(Application)*

The chapter identifies three contract-stability criteria for choosing external services: (1) stable for a long time, (2) maintained by multiple parties rather than a single platform, and (3) does not depend on the platform's business model remaining aligned with your use. Apply these three criteria to evaluate the following two data sources for a student building a news aggregation pipeline:

(a) The Hacker News RSS feed (news.ycombinator.com/rss)
(b) A startup's public API that aggregates AI research paper abstracts and currently offers a free tier

*(Tests: contract stability heuristic — applying three criteria to evaluate specific sources)*

**Answer:** (a) Hacker News RSS: (1) Stability over time — the chapter specifically uses HN RSS as its example, noting it has been in "stable Atom format since 2006." Scores well. (2) Multiple parties — RSS is a standard implemented by thousands of services; no single party can change the specification in a way that breaks all implementations. Scores well. (3) Business model alignment — Hacker News RSS is operated by Y Combinator; it is not a primary revenue source and is unlikely to be monetized or terminated for business model reasons. Scores reasonably well. Overall: LOW risk, strong contract. (b) Startup AI research paper API: (1) Stability over time — a startup with a new free tier API has no long track record. Scores poorly. (2) Multiple parties — controlled by a single startup; if they pivot, are acquired, or run out of funding, the API disappears. Scores poorly. (3) Business model alignment — a free tier provided by an early-stage startup is precisely the pattern the chapter warns about: "cheap or free because the platform had not yet monetized the capability." Scores poorly. Overall: HIGH risk, fragile contract. Design a fallback source (arXiv RSS feed) before depending on this API.

**Common error:** Evaluating only criterion (1) and (3) without applying criterion (2) — missing that the "multiple parties" criterion is what distinguishes protocol-level contracts (RSS) from platform-dependent contracts.

*Chapter reference:* Chapter 21, "Three survival disciplines" and contract stability conclusion section.

---

**Exercise 14** *(Application)*

The chapter describes n8n's error handling using two mechanisms: node-level error outputs and error workflows. For each of the following pipeline failures, specify which mechanism is more appropriate and what the error handler should do:

(a) The HTTP Request node fetching an RSS feed returns 404 because the feed URL has moved.
(b) The entire workflow crashes at an unknown point and the user has no record of what ran or failed.
(c) The Google Sheets write node fails because the API quota has been exceeded.

*(Tests: n8n error handling — node-level error outputs vs. error workflows)*

**Answer:** (a) Node-level error output on the HTTP Request node. The failure is local and known — a 404 from a specific URL. The error output should return a fallback value (empty item list for this feed) with a logged note ("Feed X returned 404 — URL may have changed") so the pipeline continues with available feeds. The specific node's error output handles this without interrupting the workflow. (b) Error workflow (pipeline-level). If the pipeline crashed at an unknown point, a node-level error handler could not have caught it (the failure location is not known). The error workflow, configured in Workflow Settings, runs when the main workflow fails at any point and sends a notification with the workflow name, the node that failed, and the error message. This is the contract-monitoring hook. (c) Node-level error output on the Google Sheets write node, plus a monitoring alert. An exceeded API quota is a contract-level event — it signals that the usage pattern has crossed a threshold in the Google Sheets contract. The node-level error output should catch the failure and route to a fallback write (local file, different storage) while the monitoring system should track how close to the quota the pipeline is reaching, to prevent hitting the ceiling next time.

**Common error:** Recommending only node-level error outputs for all three cases. The chapter is explicit that pipeline-level error workflows exist specifically for failures the developer did not anticipate — a crashed workflow at an unknown point requires pipeline-level handling.

*Chapter reference:* Chapter 21, "Harden it" — error handling section.

---

## Tier 3 — Synthesis (Exercises 15–16)

*Bloom's Level: Analyze / Evaluate*
*Purpose: Connect this chapter's concepts to a concept from a prior chapter.*

---

**Exercise 15** *(Cross-Chapter Synthesis)*

In Chapter 19, you learned about *building for after* — the importance of compounding returns from consistent behavior over time (publishing cadence, portfolio updates, relationship engagements). In this chapter, you are working with *pipeline reliability* as a product experience — the chapter's claim that "a pipeline that runs silently and reliably is invisible to the user, which is exactly what you want."

A student argues: "Pipeline reliability is a backend concern. Brand experience lives in the interface and the content. No one ever said 'I love this tool's brand' because the pipeline never missed a day." Evaluate this argument using both chapters' frameworks.

*This question connects pipeline reliability (Chapter 21) to the compounding returns of consistent brand behavior (Chapter 19).*

*What distinguishes a surface answer from a strong one:*
- A strong answer uses Chapter 19's compounding-cadence argument to explain why pipeline reliability is a brand asset, not a backend concern
- A strong answer uses Chapter 21's damage asymmetry to explain what happens to the brand when pipeline reliability fails
- A strong answer shows the interaction: consistency (Ch. 19) is the mechanism by which reliability (Ch. 21) accumulates brand trust

*(Tests: pipeline reliability as brand asset + compounding behavior — Ch. 21 + Ch. 19)*

**Answer:** The student's argument conflates brand experience with brand interface — the visible layer of UI, copy, and content. Chapter 19's compounding argument shows that brand equity accumulates through consistent, repeated positive experiences — the chapter's post-launch plan is built around cadence (monthly publishing, quarterly portfolio updates) because consistency is the mechanism of compounding. A pipeline that delivers reliably every day is doing the same work: each successful delivery is a small compounding event, and the accumulated expectation of reliability is a form of trust that builds without the user consciously noting it. Chapter 21 makes the consequence explicit: "A pipeline that fails is immediately visible, and the user sees your product fail, not the upstream contract that broke." The brand damage from a single visible failure is not proportional to the reliability that accumulated before it — trust is asymmetric. The student's argument would predict that reliability failures go unnoticed because "no one noted the good runs." The chapter's Apollo case shows the inverse: the failure is immediately visible and brand-damaging precisely because users had come to rely on reliability they never consciously noticed. Reliability is invisible when present; catastrophic to brand trust when absent. That asymmetry makes it a brand asset, not a backend concern.

*What a surface answer looks like:* "Reliability is important for user experience." This mentions both concepts but does not show the compounding mechanism or the damage asymmetry.

*Common error:* Missing the asymmetry argument — treating reliability as linearly proportional to brand trust rather than as an invisible positive accumulation with a catastrophic failure mode.

*Chapter reference:* Chapter 21, "Apollo as a brand story"; Chapter 19, "Building for After."

---

**Exercise 16** *(Cross-Chapter Synthesis)*

In Chapter 20, you learned about the *Build-Measure-Learn loop* and the importance of the MVP producing validated behavioral data. In this chapter, you are working with *the three survival disciplines* (document, degrade, monitor).

A student argues: "The survival disciplines are premature optimization for an MVP. The point of an MVP is to learn fast — adding contract documentation, degraded modes, and monitoring before you have validated users is engineering overhead that delays the learning cycle."

Evaluate this argument. Where is it correct, and where does it underestimate the cost of reliability failures during the MVP measurement period?

*This question connects the Build-Measure-Learn loop (Chapter 20) to the three survival disciplines (Chapter 21).*

*What distinguishes a surface answer from a strong one:*
- A strong answer identifies what the argument gets right — there is a real tension between moving fast and building robust degraded modes
- A strong answer explains why pipeline failures during the MVP measurement period corrupt the learning, not just inconvenience users
- A strong answer recommends which discipline(s) are essential even for an MVP and which can be deferred

*(Tests: Build-Measure-Learn loop + three survival disciplines — Ch. 20 + Ch. 21)*

**Answer:** The argument gets one thing right: full degraded mode implementation (four levels for every dependency) is engineering overhead that may not be justified for an MVP with zero validated users. If no one is using the tool yet, graceful staleness and fallback sources are optimizing a reliability experience nobody is having. There is a real trade-off between shipping fast and building robustly, and the chapter acknowledges it: the survival disciplines are a discipline, not a checkbox. What the argument underestimates: the MVP measurement period requires behavioral data from real users acting on real stakes with real workflows. If the pipeline fails silently during the measurement period, the data is corrupted: a user who would have opened the Google Sheet three times per week cannot demonstrate that behavior if the sheet was not updated on two of those days. The failure does not just inconvenience users — it makes the Build-Measure-Learn data uninterpretable. The minimum required disciplines for an MVP: (1) Informative failure — mandatory. The MVP must detect and communicate failures so the builder knows when measurement data is missing. (2) Document contracts — mandatory, but can be a one-line entry per dependency, not a full compliance document. (3) Partial degradation and graceful staleness — can be deferred until the core hypothesis is validated. Fallback sources — can be deferred unless the primary source is clearly fragile (Twitter API, single-platform API with recent price changes). The argument is correct that full robustness is premature for an MVP; it is incorrect that the survival disciplines are uniformly skippable.

*Common error:* Concluding either that all survival disciplines are premature for MVPs or that all are required. A strong answer draws the line between which disciplines protect the learning cycle (informative failure, contract documentation) and which can be deferred.

*Chapter reference:* Chapter 21, "Three survival disciplines"; Chapter 20, "What 'Minimum Viable Product' Actually Means."

---

## Tier 4 — Challenge (Exercise 17)

*Bloom's Level: Evaluate / Create*
*Purpose: Transfer beyond what was explicitly taught.*

---

**Exercise 17** *(Transfer Challenge)*

The chapter argues that RSS and Atom feeds are more stable contracts than platform APIs because they are "maintained by multiple parties rather than a single platform." However, RSS adoption has been declining — many major platforms (Facebook, Twitter/X, many news sites) have removed or hidden their RSS feeds, and some aggregators have shut down (Google Reader closed in 2013).

Design a counter-argument to the chapter's RSS stability claim. Under what conditions might the RSS standard itself become an unreliable contract? What would need to happen for RSS to fail as a stable foundation, and how would a pipeline designer know in advance whether RSS is as stable as the chapter claims for their specific use case?

*A strong response will address:*
- What specific conditions would undermine the "multiple parties, no single controller" property of RSS
- Whether declining adoption changes the stability calculus in ways the chapter does not address
- What a pipeline designer should check before relying on RSS as a stable contract for a specific set of sources

*(Tests: contract stability heuristic applied to a challenge to the chapter's own example)*

---

## Answer Key

> Attempt all exercises before reading this section.
> For Tier 3 and Tier 4, your answer does not need to match the model exactly — use the "what a strong answer includes" criteria to evaluate your own response.

---

**Worked Example**
*No answer needed — the worked example is its own model.*

---

**Ex 1** — *Four pipeline types*
*Model answer:* ETL (batch data warehousing, not real-time); streaming (high-throughput low-latency, not small-scale); workflow automation (multiple external APIs, not millions of events/sec); inference (AI reasoning step, not primary retrieval).
*Common error:* Treating streaming and inference as alternatives rather than as pipelines in different dimensions.
*Chapter reference:* Ch. 21, "Four kinds of data pipeline."

---

**Ex 2** — *Execution success vs. contract stability*
*Answer:* False.
*Correct because:* Execution success (200 returns) does not confirm contract stability — rate limits, pricing, schema changes, and terms can degrade silently without immediately causing execution failures.
*Common error:* Agreeing because "if it runs, the contracts are holding."
*Chapter reference:* Ch. 21, "Three survival disciplines."

---

**Ex 3** — *Apollo damage asymmetry*
*Model answer:* Reddit absorbed diffuse reputational damage; Apollo absorbed concentrated product-killing damage. Asymmetric because damage flows to the smallest, most dependent party — concentration of dependency, not organizational size, drives the asymmetry.
*Common error:* Attributing asymmetry to Reddit's larger size rather than to Apollo's dependency concentration.
*Chapter reference:* Ch. 21, "Apollo as a brand story."

---

**Ex 4** — *Degraded mode classification and ranking*
*Model answer:* (a) Graceful staleness. (b) Informative failure. (c) Fallback source. (d) Partial degradation. Ranking: (b) < (d) < (a) < (c), least to most robust.
*Common error:* Treating informative failure as optional because it is least robust.
*Chapter reference:* Ch. 21, "Three survival disciplines — degraded modes."

---

**Ex 5** — *n8n and independently replaceable contracts*
*Model answer:* In a monolithic script, contracts are interwoven; in n8n, each contract is a separately labeled, independently replaceable node. When a contract changes, you replace one node without touching adjacent nodes. This visibility is the architectural property that enables per-contract failure reasoning.
*Common error:* Describing n8n as "easier to use because it's visual."
*Chapter reference:* Ch. 21, "Building it in n8n."

---

**Ex 6** — *What the survival disciplines could and could not do for Apollo*
*Model answer:* Could: provide earlier warning (monitoring), communicate failure to users (informative failure), manage degradation gracefully. Could not: address the structural monopsony — no amount of monitoring changes Reddit's ability to charge $20M/year to a one-developer shop.
*Common error:* Claiming the survival disciplines would have saved Apollo.
*Chapter reference:* Ch. 21, "Three survival disciplines" and conclusion.

---

**Ex 7** — *Contract documentation for three sources*
*Model answer:* Each entry includes: what the service provides, cost, rate limit, risk level, and degraded mode. LinkedIn: HIGH risk (requires partner API, terms prohibit scraping). Indeed: MEDIUM risk (free tier subject to business model decisions). Company RSS: LOW risk (stable, no single provider controls).
*Common error:* Writing contract documentation without the risk level and degraded mode.
*Chapter reference:* Ch. 21, "Three survival disciplines — document."

---

**Ex 8** — *Pipeline error analysis*
*Error:* Single massive GPT-4 call for all 50 items — fragile, expensive, non-validatable.
*Contract risks:* Cost, rate limits, failure scope (one call fails = nothing produced), no intermediate validation.
*Redesign:* Separate ingestion, deduplication, per-item LLM calls, per-item Sheets writes, then digest assembly.
*Chapter reference:* Ch. 21, "Building it in n8n" and Madison workflow design.

---

**Ex 9** — *AI Interaction — graceful staleness*
*Model answer:* Strongest: "show users when data was last updated." Gap: missing the hierarchy — graceful staleness is the most robust tier. Extension: legible staleness is mandatory; stale data without a timestamp is a confidence misalignment. Verification: disconnect source, verify (a) no crash, (b) last result served, (c) staleness indicator present, (d) fresh data appears on reconnection.
*Chapter reference:* Ch. 21, "Three survival disciplines — degraded modes."

---

**Ex 10** — *Self-explanation: n8n architectural reason*
*Model answer:* n8n makes each contract independently replaceable — a labeled node with defined inputs and outputs, swappable when the contract behind it changes. Monolithic scripts hide contracts inside interwoven code, making failure localization and contract swapping more difficult.
*Common error:* Describing n8n as easier to use rather than architecturally distinct.
*Chapter reference:* Ch. 21, "Building it in n8n."

---

**Ex 11** — *Cumulative: MVP Boundary + contract stability*
*Model answer:* RSS feeds can test the core hypothesis, are stable contracts, and belong in v1. Twitter/X fails all three contract stability criteria and belongs in the out-of-scope list. $100,000 no = Twitter/X in v1.
*Common error:* Recommending Twitter/X because "more data is better for testing."
*Chapter reference:* Ch. 21, "Three survival disciplines"; Ch. 20, "MVP Boundary."

---

**Ex 12** — *Parallel branches as degraded mode design*
*Model answer:* Parallel branches address the failure mode that any single source can fail without breaking the entire ingestion step — this is partial degradation implemented at the architecture level. Collapsing branches into one step would make a single-source failure cause total ingestion failure.
*Common error:* Describing parallel branches as a performance optimization.
*Chapter reference:* Ch. 21, "Reading Madison + breaking it on purpose."

---

**Ex 13** — *Contract stability applied to two sources*
*Model answer:* HN RSS: LOW risk (stable since 2006, RSS is multi-party, not a primary revenue source). Startup API: HIGH risk (no track record, single-party control, free tier pre-monetization pattern). Recommend arXiv RSS as fallback for the startup API.
*Common error:* Evaluating only criteria (1) and (3), missing the "multiple parties" criterion.
*Chapter reference:* Ch. 21, "Three survival disciplines" and stability heuristic.

---

**Ex 14** — *n8n error handling mechanisms*
*Model answer:* (a) Node-level error output on HTTP Request — local, known failure; fallback to empty list. (b) Error workflow (pipeline-level) — unknown crash point requires pipeline-level notification. (c) Node-level error output on Sheets write + monitoring for quota proximity.
*Common error:* Recommending only node-level error outputs for all three.
*Chapter reference:* Ch. 21, "Harden it."

---

**Ex 15** — *Synthesis: pipeline reliability + compounding behavior*
*Model answer:* Reliability accumulates trust through consistent silent delivery (Ch. 19 cadence mechanism). Failure is immediately visible and catastrophic to brand trust (Apollo case). Reliability is invisible when present; catastrophic when absent — that asymmetry makes it a brand asset, not a backend concern.
*What a strong answer includes:* Compounding mechanism; damage asymmetry; interaction between the two chapters.
*Common error:* Treating reliability as linearly proportional to trust rather than asymmetrically damaging when absent.
*Chapter reference:* Ch. 21, "Apollo as a brand story"; Ch. 19, "Building for After."

---

**Ex 16** — *Synthesis: Build-Measure-Learn + survival disciplines*
*Model answer:* Argument is partially correct (full robustness is premature for zero-user MVP). It underestimates: pipeline failures during the MVP measurement period corrupt the behavioral data, making the Build-Measure-Learn cycle uninterpretable. Minimum required: informative failure + contract documentation. Can defer: higher-level degraded modes for v1 with validated users.
*Common error:* Treating all survival disciplines as either uniformly required or uniformly skippable for MVPs.
*Chapter reference:* Ch. 21, "Three survival disciplines"; Ch. 20, "What 'Minimum Viable Product' Actually Means."

---

**Ex 17 — Challenge**
*No model answer provided.*
*A strong response will address:*
- Specific conditions that would undermine multi-party maintenance: if RSS feed provision became concentrated among a small set of major publishers who all adopted a different standard, the multi-party property would erode
- Declining adoption changes the calculus for specific sources (many specific sites have removed RSS) but not for the standard itself — the distinction between "a specific site's RSS feed" and "the RSS standard" is key
- What to check per specific use case: whether the specific sources needed still publish RSS, whether those feeds have been updated recently, whether the content behind the feed is behind a paywall that the RSS link does not reach
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
