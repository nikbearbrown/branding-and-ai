# Chapter 5: Data Pipelines and Workflow Automation

> **Voice anchor:** `voice-unanchored`. Voice for this draft is Feynman per CLAUDE.md §6 + textbook:chapter SKILL.md.

## Suggested titles

1. *The Day Apollo Stopped*
2. *Pipelines, Contracts, and the People Who Trusted You*
3. *Data Pipelines and Workflow Automation*

## TL;DR

A data pipeline is a chain of contracts you do not control: an API, a rate limit, a price, a schema. The pipeline is only as reliable as the weakest contract in the chain. Building well means designing for the day a contract changes, not pretending it won't.

---

On May 31, 2023, Christian Selig — the developer of [Apollo](https://en.wikipedia.org/wiki/Reddit_API_controversy), the most-loved third-party Reddit app — published a number. Reddit had announced new API pricing in April: $0.24 per 1,000 calls. Selig calculated what that would mean for Apollo. The app had made roughly seven billion API requests in the previous month. Multiplying out the new price, Apollo would owe Reddit somewhere around $20 million a year.

Apollo, run by one developer, had revenue measured in the hundreds of thousands. Twenty million was not a price — it was a kill order delivered with three months' notice. On June 8, Selig announced Apollo would shut down on June 30. Two other major third-party Reddit apps — Reddit Is Fun and ReddPlanet — followed. On June 12, thousands of subreddits went private in protest. By July, the third-party Reddit ecosystem that had existed for over a decade was effectively gone.

Apollo was not a bad pipeline. It was an excellent pipeline — well-designed, performant, beloved by users. What killed it was the contract it depended on. Reddit owned the API; Reddit could change the price; the price changed; the pipeline collapsed.

This chapter is about pipelines like Apollo's: data pipelines that depend on external services, that look stable when you build them, and that turn out to be fragile in ways that only become visible when something upstream changes. By the end of it, you will be able to design and implement an n8n workflow for your tool, and — more importantly — you will know how to build the pipeline so that the day Reddit (or Twitter, or OpenAI, or your favorite scraping target) changes its terms is not the day your product dies.

---

## What "data pipeline" actually means

The phrase *data pipeline* has, like most technical terms in 2026, multiple jobs:

1. **ETL pipeline.** Extract-Transform-Load. The classical data-engineering pattern: pull data from sources, clean and reshape it, write it to a warehouse. SQL-heavy, batch-oriented, mature.
2. **Stream-processing pipeline.** Kafka, Flink, Spark Streaming. Continuous flows of events processed in near-real-time.
3. **Workflow-automation pipeline.** n8n, Zapier, Make. Visual node graphs that connect APIs, transform data, schedule tasks. Lighter than ETL, more general than stream processing.
4. **Inference pipeline.** LLM call, embedding, vector store retrieval, response. The newest member of the family, often glued together with Python and a vector database.

Madison's pipelines, and yours, will mostly be type #3 with hooks into type #4. n8n is the orchestration layer; LLM calls happen inside it. The Madison Intelligence Agent's [own README](https://github.com/humanitariansai/madison) describes its workflow as 40+ nodes in n8n connecting RSS feeds, Google News API, Reddit, GPT-4o-mini, and Google Sheets. That is a workflow-automation pipeline doing inference work as a step.

What unifies all four meanings is the *contract structure*. A pipeline is a chain of components, and between every pair of components is a contract: how data flows, how often, in what shape, at what cost. The pipeline runs as long as every contract holds. The pipeline breaks when one contract fails.

For your build, n8n is the right tool because it makes the contracts visible. You can see, in the visual node graph, exactly where data comes from, what shape it is in at each step, and where each external dependency lives. Tools that hide the contracts (a single Python script that imports requests, makes ten API calls, processes data, writes to a database, all in 200 lines) make pipelines that work today and break opaquely six months from now.

---

## n8n in two minutes

n8n is an [open-source workflow automation platform](https://github.com/n8n-io/n8n) — fair-code licensed, self-hostable, with 400+ pre-built integrations and the ability to write JavaScript or Python at any node. The Community Edition is free for self-hosted use; the Cloud version starts at €20/month for managed hosting.

The core concepts are three:

- **Nodes** — operations. A node can be a webhook trigger, an HTTP request, a database insert, a function call, an LLM completion, a conditional branch, anything.
- **Connections** — edges between nodes. Data flows along connections from output port to input port, often with type-checking on the shape of the data.
- **Workflows** — named graphs of nodes and connections. A workflow has a trigger (schedule, webhook, manual), executes its nodes in dependency order, and produces output (a stored result, an email, a downstream API call).

A workflow can be exported as JSON. The Madison Content Agent's full workflow lives in `pantry/madison/Content_Agent_full_workflow.json`. Open it and you will see the structure: a webhook trigger, a JavaScript code node that builds a prompt, an OpenAI call, a JSON parser, a CSV writer, a response node. Six steps, each with a defined input and output, each replaceable independently if a contract changes.

That last property — *independently replaceable* — is what n8n buys you over a single-script pipeline. When OpenAI raises its prices, you swap the OpenAI node for a Claude node and rerun. When Reddit's API breaks your ingestion step, you swap the Reddit node for an RSS-feed-of-Reddit-mirrors node, or you remove that data source entirely without touching the rest of the workflow. The visual graph forces the contracts to be explicit, which means you can reason about them when one of them shifts.

---

## Why pipeline fragility is a brand problem, not just a technical one

The deep work this chapter is about: every external dependency in your pipeline is a brand commitment, whether you mean it to be or not.

Here is the mechanism. When you build a pipeline that depends on, say, Twitter's API for sentiment analysis, you are implicitly promising your users: *my product will continue to work as long as Twitter's API continues to behave the way it does today.* If Twitter changes its terms — pricing, rate limits, what data is available — your product changes too, or breaks. Your users do not see the upstream contract change. They see *your* product fail.

The brand consequence is asymmetric. When Reddit broke Apollo, public sympathy went to Apollo, and Christian Selig's reputation as a developer was — if anything — strengthened. He had built well; an upstream actor had broken his work in public; his transparency about the math made the breakage legible. But Apollo *the product* still died. Users who had paid for Apollo's lifetime subscription lost their tool. Selig's brand survived; his product did not.

Most students do not have Selig's transparency reflexes. When their pipeline breaks because of an upstream change, the user-facing failure looks like *their* fault. The user sees "this AI tool stopped working." They do not see "Reddit changed their API in a way that broke this tool." The brand damage accrues to the product whose name is on the front page, not the upstream service that caused the break.

This is why pipeline-fragility incidents are paired with brand failures in the textbook's case structure. The pipeline is a brand asset. When the pipeline fails — for any reason, including reasons you did not cause — the brand pays. Designing the pipeline well means designing for the failure modes you do not control.

### A worked case: three platform-API ruptures, three downstream failures

**Reddit, June 2023.** Already opened. Apollo, RIF, ReddPlanet shut down. Thousands of subreddits went private in protest. The third-party ecosystem that had supported Reddit for over a decade was effectively dismantled. Reddit's stated rationale: monetize the data ahead of an IPO. The actor making the change was clearly Reddit, but the products that visibly failed were the third-party apps.

**Twitter, February 2023.** [Twitter's free API tier was deprecated](https://developer.twitter.com/en/docs/twitter-api), with new tiers starting at $100/month for severely limited access. Academic researchers using Twitter's research API found their work disrupted overnight. Hundreds of third-party tools — sentiment dashboards, archive bots, Twitter clients — broke or pivoted away. The brand damage to Twitter (which by then had become X) was real but diffuse; the brand damage to the third-party tools was concentrated and immediate.

**Heroku, November 2022.** [Heroku ended its free tier](https://blog.heroku.com/next-chapter), deprecating the free dyno that had hosted hundreds of thousands of student and side projects. Many tools built by students simply went offline because nobody renewed them on a paid tier. The user-facing failure was "this app is no longer available." The upstream cause was Heroku changing its terms.

Three different industries, three different upstream actors, the same pattern. A platform makes a unilateral decision; downstream tools break; downstream users blame the tool, not the platform. The brand damage flows downhill.

---

## Designing for the contracts you do not control

The discipline this chapter asks you to install: treat every external dependency as a contract that *will* change, not as infrastructure that won't.

Three habits to build into every pipeline:

**1. Document the contract before you depend on it.** When you add an external API to a workflow, write a one-line note in the workflow's documentation: *what this API gives us, what it costs, what the rate limit is, what happens at the limit.* The note forces you to confront the dependency consciously, which is the first step toward planning around it.

**2. Build a degraded mode for every critical dependency.** If your tool depends on Reddit data and Reddit's API breaks, what does the tool do? "It crashes" is a real answer; it is also a brand decision. Better answers: it falls back to RSS mirrors of Reddit; it disables the Reddit-dependent feature gracefully; it shows the user a clear message about what is unavailable and why. The degraded mode does not have to be elegant. It has to exist.

**3. Monitor the contracts, not just the workflow.** A workflow can be running successfully — every node returns 200, every connection passes data — while the underlying contract is silently changing. Rate limits creep down. Pricing tiers shift. Schemas drift. You want alerts on contract-level events, not just on execution failures. n8n has nodes for this; OpenAI has billing alerts; APIs typically have changelogs you can subscribe to. Wire them up.

The Madison Intelligence Agent's workflow does some of this automatically. It rate-limits at the orchestration layer (not at the LLM). It writes processed results to Google Sheets, which means the data outlives the workflow — a Sheet you can read independently of whether the workflow ran today. It uses RSS as a primary ingestion mode, which is one of the more stable contracts on the internet (the Atom and RSS specs have been mostly stable since the mid-2000s and are unlikely to change unilaterally).

These choices were not accidents. They are the architectural reflections of an awareness that *external contracts will change*. When you design your own pipeline, study Madison's choices for what they are: bets about which contracts are durable and which are fragile.

---

## What you build in this chapter

A working n8n pipeline that ingests data from at least one external source, transforms it through at least one processing step, and writes output to a place where you can verify the result. Concretely:

- Set up an n8n instance (self-hosted via Docker, or cloud).
- Build a workflow with a scheduled trigger (start with hourly).
- Pull data from one external API or RSS feed.
- Add a transformation step (filter, deduplicate, format).
- Write output to a verifiable destination (Google Sheet, file, webhook).
- Document each node's purpose and its external contract dependencies.
- Add error handling at the trigger and a degraded mode for at least one critical node.

This is the smallest pipeline that does real work. It is also the seed of the AI-intelligence work in Chapter 6, where you will add LLM-based processing to this same workflow.

The Madison Intelligence Agent's workflow is the reference. Open `pantry/madison/Intelligence-Agent/n8n_workflow.json` and trace the data flow from RSS ingestion through deduplication through sentiment scoring through Sheet writes. Your workflow will be smaller — no need to match Madison's scale — but the *shape* should be the same.

---

## What you walk out with

A working n8n pipeline. A definition of "data pipeline" that is not "the script that pulls data" but "the chain of contracts your tool depends on." Three documented cases of pipeline fragility cascading into brand damage. The discipline of building degraded modes for every critical external dependency.

I should be honest about the limits of n8n. It is a workflow tool, not a data engineering platform. For high-throughput streaming workloads, for complex SQL transformations, for production-grade ETL — n8n is the wrong tool. Engineers running 10TB-per-hour pipelines use Kafka and Spark and Airflow. n8n is the right tool for what you are doing — orchestrating API calls, glueing services together, building the kind of pipeline a small team can run on a single server.

The deeper reading for what serious data infrastructure looks like is [Martin Kleppmann's *Designing Data-Intensive Applications*](https://dataintensive.net/), now in its second edition. The book is the canonical reference for the concepts your n8n workflow is a small instance of: reliability, scalability, maintainability, replication, consistency. You will not need it for the build sequence in this course. You will need it the moment you go beyond the build sequence into production.

---

## Embedded exercise: build your first pipeline

Before Chapter 6:

1. Set up n8n (cloud or self-hosted). Document your setup choices in your project README.
2. Build the pipeline above: trigger → external source → transformation → verifiable destination.
3. Write a one-paragraph "contracts" document listing every external dependency, what it costs, what its rate limit is, and what your degraded mode is for each one.
4. Break one of the contracts deliberately. Disconnect the API key, point at a dead URL, comment out a critical node. Observe what happens. Fix the workflow so it fails gracefully instead of crashing.

Bring the working workflow and the contracts document to Chapter 6, where the AI-intelligence layer goes on top of this foundation.

---

**What would change my mind:** Strong evidence that students learn pipeline-design skills better through code-first frameworks (Python + a few libraries) than through visual workflow tools like n8n. The current pedagogical claim is that visual workflows force the contracts to be visible in a way that script-based pipelines do not. The claim is plausible but not empirically settled.

**Still puzzling:** The trade-off between contract-stability and feature-richness when choosing external services. RSS is stable but limited. Twitter (when it had a free API) was rich but unstable. The choice between "rich and unstable" and "limited and stable" is a strategic call that students consistently get wrong, and I don't yet have a clean rule of thumb to teach for it.

---

## 📌 LLM Exercise — Self-as-Project

**Project:** Self-as-Project
**What you're building this chapter:** A **Career Pipeline** spec — the workflow that takes you from "discovers an opportunity" to "signs an offer," with documented contracts and degraded modes.
**Tool:** Claude Project for the design pass; Cowork for actually setting up the tracking spreadsheet.

**The Prompt:**

```
Design my job-search pipeline using the Chapter 5 framework: every external dependency is a contract; every contract can break; every break has a degraded mode.

The pipeline has stages. For each stage, document: what enters, what exits, what external contract it depends on, what failure mode would break it, and what my degraded mode is.

Stages to map:

1. DISCOVERY. How job opportunities reach me. Sources: job boards, LinkedIn alerts, referrals, recruiter cold-outreach, my own published work.
2. QUALIFICATION. The PRD-filter pass. Does this role fit my Career PRD's IN list? Yes/no decision.
3. APPLICATION. The actual application work — resume tailoring, cover note, portfolio link, network warm-up.
4. NETWORK ACTIVATION. Reaching out to anyone I know at the company before or during the application.
5. INTERVIEW PREPARATION. Research, talking points, technical practice.
6. INTERVIEW EXECUTION. The conversation itself, follow-up notes.
7. NEGOTIATION. Offer, counter, accept/decline.
8. ONBOARDING / TRANSITION. The first 30 days at the new role, or the post-decline cleanup.

For each stage:
- What's the input?
- What's the output?
- What external contract does it depend on? (E.g., "LinkedIn's recruiter messaging works"; "the company's ATS parses my PDF correctly"; "my reference at Company X is reachable.")
- What's the most likely failure mode?
- What's my degraded mode?

Then — recommend 3 tools or systems that would automate or augment this pipeline. Could be a Notion database, an Airtable tracker, a Cowork-managed spreadsheet, an n8n workflow, or a custom Claude Project. For each, name the specific stage(s) it would help and what the setup cost is.

Output a Markdown document called "Career Pipeline — [my name]" with the eight stages mapped, plus the tool recommendations.
```

**What this produces:** A documented pipeline you can build a tracking system around. Many students stall in Stage 5 (interview prep) without realizing it; the pipeline view exposes where the bottleneck is.

**How to adapt:** If you're not job-searching, replace the stages with the equivalent for your goal (PhD application: discovery → qualification → personal-statement drafting → recommender activation → submission → interview → decision). Uses the Career PRD from Chapter 4 as the qualification filter.

**Preview of next chapter:** Chapter 6 builds an AI-powered career-search assistant on top of this pipeline.

---

**Tags:** n8n · data-pipeline · workflow-automation · reddit-api · apollo · pipeline-fragility · external-contracts · madison-intelligence-agent · INFO-7375
