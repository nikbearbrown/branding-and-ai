# Module 21 — ShipIt: Pipelines & Workflow on Madison: Wonder Edition
## Companion Chapter

> **Wonder Edition:** Read this alongside the chapter, not instead of it.

**Content note:** Despite the filename "21-shipit-pipelines-and-workflow-on-madison," this chapter is filed as Appendix S2 in the book. This companion follows the actual chapter content.

## The Strange Question

Apollo was a Reddit client built by one developer. By most technical measures, it was excellent — performant, well-designed, praised universally by the several hundred thousand people who paid for it.

On May 31, 2023, Christian Selig published the math: Reddit's new API pricing would cost Apollo approximately $20 million per year. The app had revenue in the hundreds of thousands.

Apollo shut down on June 30, 2023.

The code did not break. The servers did not fail. No bug was found. No design flaw was exposed. The product that users had praised and paid for simply stopped existing, thirty days after the number was published.

Reddit received diffuse reputational damage spread across a company with hundreds of millions of users. Apollo — the excellent, praised, paid-for product — received concentrated, total, product-killing damage.

How can a well-built, technically sound product be destroyed not by a flaw in itself, but by a change in something it depends on that the builder did not write and cannot control?

## First Intuition

The intuitive model: a pipeline is code. It fetches data, processes it, writes it somewhere. Its reliability depends on the quality of the code. Well-written code is reliable code. The discipline of building a good pipeline is a software engineering discipline: clean functions, error handling, good tests, thoughtful architecture.

This model comes from software engineering itself. The canonical bugs are in the code: a null pointer, a race condition, an off-by-one error. The canonical fixes are also in the code: better testing, stricter types, more careful logic. The code is what you control. The code is where the work is.

> **► Planning prompt:** Before reading further, write down your mental model of what makes a data pipeline reliable. If a pipeline has been running without errors for three months, what is the primary thing that could cause it to fail next week? Is the primary risk in the code you wrote, or somewhere else? Write it down before continuing.

## The Surprise

But a pipeline is not primarily a piece of code. It is a chain of contracts, each owned by someone else, each subject to change without consent.

Between every component in a pipeline — every API call, every database write, every transformation step — there is an agreement about how data flows: what shape, at what cost, subject to what rate limits, governed by what terms of service. The pipeline runs as long as every agreement holds. The pipeline breaks when one agreement fails. The agreements are not the builder's to control.

Apollo's code did not change. Apollo's servers did not fail. The agreement Apollo depended on — Reddit's API terms, which governed cost — changed. The pipeline broke not in the code but at the contract edge. The excellent code and the excellent design were irrelevant to the failure mode.

The same pattern ran at Twitter (February 2023: free API tier ended, hundreds of tools broke overnight), at Heroku (November 2022: free dynos ended, thousands of student projects went offline), and at dozens of smaller platforms. Different industries, different upstream actors, the same structure: platform makes a unilateral change, downstream products break, downstream users blame the tool, brand damage flows to the smallest actor in the chain.

> **► Monitoring prompt:** In your own words, describe what your initial model assumed about the relationship between code quality and pipeline reliability. What specific mechanism does the Apollo case reveal that the code-quality model cannot account for? What does your current model still fail to explain about why brand damage flows to the smallest party in a contract chain, not to the party that changed the contract?

## The Hidden Structure

Therefore, pipeline design is contract management. Three disciplines answer the question "when a contract changes, what does the product do?" before the contract changes.

First: document every external dependency before building on it, in the workflow itself, as a node description or README section. One sentence per dependency: what this service provides, what it costs, what the rate limit is, what the terms allow. Writing "Reddit API — terms allow third-party clients, subject to change" acknowledges the "subject to change" as part of the design. The documentation forces conscious confrontation with the dependency before dependence on it is established.

Second: every critical external dependency needs a degraded mode — the answer to "what does the product do when this contract fails?" Four levels: informative failure (the product shows the user what is unavailable and why, rather than an opaque error), partial degradation (the broken feature is disabled while the rest continues), fallback source (the broken dependency is replaced by an alternative), graceful staleness (the last successful result is served with a visible timestamp). Stale data is usually better than no data, as long as the staleness is legible.

Third: monitor the contracts, not just the workflow execution. A workflow can run successfully — every node returns 200 — while the underlying contract is silently degrading. Rate limits creep down. Terms of service are updated. Wire the API's status-page RSS feed into the monitoring channel. Set billing alerts on upstream services. This catches a contract change before it crashes the pipeline.

> "It is tempting to think pipeline reliability is primarily a software engineering problem — that well-written, well-tested code is reliable code and that the discipline of building a good pipeline is the discipline of writing good software. But Apollo's failure was not in the code; it was at a contract edge the code could not control. The correct model holds that a pipeline's reliability is determined by the weakest contract in its dependency chain, not by the quality of its own code, and that contract management — documenting, planning degraded modes for, and monitoring each external dependency — is the primary engineering discipline for pipeline reliability. The key distinction is between failure modes that originate inside the code (debuggable, controllable) and failure modes that originate in contracts the builder does not control (preventable only through dependency design)."

**The three pipeline disciplines applied to the four-node build:**

| Node | External contract | Contract risk | Documented degraded mode |
|---|---|---|---|
| Schedule Trigger | Time (n8n's scheduler) | Low — internal | Log missed run, do not retry silently |
| HTTP Request: RSS | Hacker News RSS format (Atom, stable since 2006) | Low — multi-party, no single owner | Log HTTP error, return empty item list, continue |
| Google Sheets write | Google Sheets API (OAuth, stable) | Moderate — single platform | Log write failure, buffer result locally |

## Try Looking At It This Way

**Target:** Pipeline-as-chain-of-contracts — the reframing of a data pipeline from a sequence of code steps to a chain of agreements with external parties, each agreement owned by someone else, each subject to change without consent, with the pipeline's reliability determined by the weakest contract in the chain.

**Base:** A supply chain for a restaurant.

**Features:**
- The pipeline's data flow corresponds to the restaurant's ingredient supply chain
- Each external API or service corresponds to a supplier
- The contract terms (rate limits, pricing, data format) correspond to the supplier's delivery agreement (price, volume, lead time, quality spec)
- A degraded mode corresponds to a substitute ingredient or recipe adaptation when one supplier fails
- Monitoring for contract changes corresponds to a procurement manager tracking supplier price announcements before they take effect

**Commonalities:** In both systems, the end product's reliability is determined not by the quality of the work done inside the operation but by the stability of the agreements that supply it. A restaurant with excellent chefs and excellent recipes can have its service disrupted entirely by a single supplier who changes pricing, product formulation, or delivery schedule. The restaurant's response — maintaining substitute suppliers, designing menus with ingredient redundancy, monitoring for supplier changes in advance — is structurally identical to the pipeline designer's three disciplines. The analogy holds at the dependency structure level: the "weakest contract in the chain" failure mode applies equally to supply chains and data pipelines.

**Boundaries:** A restaurant supplier typically gives advance notice of price changes — market conventions in the food industry create norms around lead time. Reddit gave Apollo three months' notice; Twitter gave thirty days. But some contract changes happen without any advance notice — an API schema update that deprecates a field the pipeline depends on may be announced in a changelog that no one reads. Unlike a supply chain, where sudden total termination of a supplier without notice is unusual enough to qualify as a legal dispute, API terms changes can be effective immediately if the terms reserve that right. The restaurant analogy implies a negotiation and notice culture that platform API relationships often do not have.

**Conclusions:** Treat every external dependency as a contract. Document it before building on it. Plan a degraded mode before the contract fails. Monitor for changes before they reach the pipeline. The code is only as reliable as the weakest contract it depends on.

## Where The Analogy Breaks

Unlike a supply chain, where a restaurant can typically source the same ingredient from multiple suppliers and maintain redundancy without fundamentally changing the product, some data pipeline dependencies have no realistic alternative. Reddit data exists on Reddit; a pipeline that needs Reddit data has no alternative source if Reddit's API becomes unaffordable. The supply-chain analogy implies that a fallback source is always available — that the degraded-mode discipline "choose an alternative supplier" is always executable. The Apollo case illustrates the structural failure mode the analogy cannot address: the platform's monopsony — its status as the only source for its own data — means no fallback source exists. The three disciplines help with recoverable failures; they cannot prevent the structural failure that results from building a business inside someone else's monopsony. The supply chain analogy implies more substitutability than platform-dependent pipelines actually have.

## Small Discovery

**Raw data:**

A regional florist chain operated twelve retail locations. Deliveries were coordinated through a third-party platform that handled routing, driver assignment, and customer notifications. The platform charged a 12% transaction fee on all deliveries.

In March of one year, the platform announced that the transaction fee would rise to 22% effective 60 days later. The platform was the florist's exclusive delivery coordination service; no contract required exclusivity, but no alternative had been evaluated.

The florist had three options:
- Accept the new rate and absorb the margin reduction
- Reject the new rate, terminate the relationship, and build a direct delivery operation in 60 days
- Negotiate for a transitional rate while building a partial alternative

The florist took Option 3. They negotiated a 16% transitional rate for six months. During that period, they built direct delivery capability for 40% of their highest-volume orders, documented their delivery process to enable future alternatives, and established a relationship with a competitor platform.

At the end of the transitional period: the new platform agreement was at 18%, covering 60% of volume. Direct delivery covered 40%. Total delivery cost per order: 11% (blended).

**Pattern search:** The florist's platform partner changed contract terms unilaterally with 60 days' notice. What degraded-mode level did the florist deploy in response — informative failure, partial degradation, fallback source, or graceful staleness — and what would have happened if they had had no degraded mode designed in advance?

**Prediction:** If the florist had, before the platform announced the price increase, documented their delivery dependency and built even a partial direct-delivery capability as a proof-of-concept, would the 60-day transition have been easier, harder, or roughly the same? Write your prediction before continuing.

---

**Revelation:** The florist deployed a fallback-source degraded mode: partial migration to an alternative that had been built during the transition window. With no pre-existing degraded mode, the 60-day window would have forced a binary choice — accept the 22% or terminate the relationship — because building a direct delivery operation from scratch in 60 days is not achievable. The transition "easier with prior preparation" question has a direct answer in the pipeline discipline: the three disciplines are not responses to a crisis already underway; they are preparations for the crisis before it arrives. A florist who had documented the dependency ("third-party delivery platform, 12% fee, 60-day notice provision, no exclusivity requirement, no fallback source built") and maintained a partial direct-delivery capability as a standard practice would have entered the 60-day window with options already partially executed rather than needing to build them from scratch. The Apollo case is the same failure: no degraded mode was designed in advance because the contract terms had been stable long enough that the dependency felt permanent.

## What This Changes

1. **What question can the reader now answer?** Why Apollo's excellent code was irrelevant to its failure — and why the failure was predictable from the structure of the dependency, not from any flaw in the product.

2. **What looks different in a specific design decision?** The decision to add a new external service to the pipeline. Before this chapter, the question is "does this API provide what I need?" After this chapter, the question is "what happens to my product when this API changes its terms, and have I documented that answer?" An API that cannot be documented with a realistic degraded mode is a design risk, not just a technical dependency.

3. **Practice Bridge:** The student can now build the four-node n8n pipeline (Schedule → RSS fetch → Transform/Deduplicate → Google Sheets write) and document the three external contracts it depends on using the prescribed format: what the service provides, what it costs, what the rate limit is, what the terms allow, and what the degraded mode is for each contract failure. The documentation is not a README exercise — it is the first iteration of the contract-management discipline that determines whether the pipeline is still running six months after the build.

4. **What question does this leave open?** The pipeline's external contracts include, after Module 22 (AI intelligence and multiagent systems), at least one LLM API contract. That contract has its own pricing structure, rate limits, terms of service, and failure modes — and the specific failure modes of LLM API contracts (hallucination, cost runaway, context limit changes) are distinct from those of data API contracts.

## Wonder Questions

1. The chapter proposes RSS as a more stable contract than platform APIs because it is maintained by multiple parties and not dependent on a single business model. But RSS is also limited: no authentication, minimal metadata, no social engagement signals. A pipeline that needs rich social data has no stable-contract alternative. How do you decide when to accept a fragile-but-rich contract, and what does "budget for its failure from day one" look like in practice?

2. The three degraded modes (partial degradation, fallback source, graceful staleness) all assume the failure is temporary or recoverable. Apollo's failure was permanent — the contract was not changed back, and no fallback source for Reddit data existed. Is there a fourth degraded mode for permanent contract failure, and what does a pipeline designed for that scenario look like?

3. The chapter shows that brand damage flows to the smallest, most dependent actor in a contract chain. Selig's personal reputation was strengthened by his transparency; Apollo the product died. A student building their first tool on a free-tier API is in Selig's position — dependent on a platform they do not control. What specific transparency practice would protect the builder's personal reputation if the API they depend on changes terms, even if it cannot save the product?

4. n8n's visual workflow structure makes contracts visible as separately labeled nodes. The chapter argues this is an advantage over monolithic Python scripts where dependencies are interwoven. But visual tools add their own contract: n8n itself is a dependency, with its own pricing, its own terms of service, and its own change history. A student who builds entirely inside n8n has a pipeline-within-a-pipeline dependency problem. How do you document and degrade the tool you are using to manage dependencies?

5. The chapter's "still puzzling" section identifies no clean rule for when to accept a fragile-but-rich contract versus preferring stable-but-limited alternatives. A heuristic is offered: "if the contract is controlled by a single platform, budget for its failure from day one." Is that heuristic sufficient for a student making the dependency choice in a product that genuinely needs the rich contract to function? What additional information would turn the heuristic into a rule?

---

> **What the concept is:** Pipeline-as-chain-of-contracts — the reframing of data pipeline reliability from a software engineering problem (quality of the code) to a contract management problem (stability of the external dependencies), with the three disciplines (document, design degraded modes, monitor) as the primary engineering practice for managing contracts the builder does not control.
>
> **What it explains:** Why Apollo's excellent code was irrelevant to its failure; why brand damage flows to the smallest actor in a contract chain; why n8n's visual structure makes contracts visible in ways that monolithic scripts do not; why RSS is a more reliable contract than platform APIs for pipelines that do not require rich social data.
>
> **What it does NOT mean:** That well-written code is unimportant. Within the contracts the builder controls — the transformation logic, the deduplication algorithm, the output formatting — code quality determines reliability in the traditional sense. The pipeline-as-contracts reframing adds a layer above code quality, not a replacement for it.
>
> **What comes next:** Module 22 (AI intelligence and multiagent systems) addresses the specific contracts that LLM API calls add to the pipeline — and the distinctive failure modes (hallucination, cost runaway, context limit) that LLM contracts introduce beyond the standard data-pipeline failure modes.
