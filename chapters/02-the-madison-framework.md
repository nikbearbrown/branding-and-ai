# Chapter 2 — The Madison Framework
*Five roles, one pipeline, and the moment you realize architecture is brand.*

---

Most people approaching AI product development have a vivid sense of what they want a tool to *do* — and almost no sense of what makes one architecture different from another. They have watched demos. They have used ChatGPT. They know approximately what "agent" means the way you might know approximately what "leverage" means in finance: enough to use the word confidently, not enough to make decisions with it.

That gap is what this chapter closes. We are going to read one real, open-source framework — [Madison](https://www.humanitarians.ai/madison) — as if it were a schematic. We will trace one layer in enough mechanical detail that you could explain it to a skeptical colleague. And then we will follow the design choices that produced a five-layer architecture all the way out to where they land in brand strategy. By the end, you will have a mental model for reading any multi-agent system — the ability to hear the word "agent," ask immediately which of four distinct things the speaker means, and understand why that question determines everything about how the product fails, how it is sold, and how much trust customers can reasonably extend.

You need one thing from Chapter 1 before we proceed: your archetype. If you did not finish the Self-as-Project exercise, finish it now. It carries real weight at the end of this chapter. You also need a working definition of what an LLM is — a function that takes text in and produces text out — and enough comfort with Python-style pseudocode to follow a recipe. The reasoning traces ahead are written exactly that way.

---

I want to start with a word that is doing too much work.

The word *agent* in 2026 carries four different meanings depending on who is speaking and in what context. This is not a pedantic complaint. It is a practical one: because the four meanings produce four completely different products with four completely different failure modes.

**The first meaning** is the simplest and the most common on LinkedIn. "I built an agent that summarizes emails." This means: I wrote a prompt, I call an API, I get text back. It is a function with a prompt. Useful. Not what researchers mean by agent.

**The second meaning** is closer to the formal definition. An LLM with tools and a loop. The system can reach into the world — call APIs, read files, take actions — and then it loops: take an action, observe the result, reason about what to do next, take another action. This is approximately what Yao et al. described in their 2023 ReAct paper, which we will examine in detail shortly.

**The third meaning** is the science-fiction meaning, which is approximately real. An LLM that runs autonomously over a sustained horizon — plans its own work, sequences its own actions, reports outcomes rather than asking for guidance at each step. Devin 2.0 lives here: multiple instances in parallel sandboxed environments, working through tasks while you sleep.

**The fourth meaning** is how Madison uses the word. An agent is a specialized role in a larger system — a named component with defined inputs and outputs, optimized for a particular kind of work, coordinated by an orchestration layer. Agent as module.

These four meanings are not in conflict. They describe different levels of abstraction. A Madison Intelligence Agent (meaning 4) is implemented using a ReAct loop (meaning 2). Devin (meaning 3) probably contains many sub-agents in meaning 2. The summarization function (meaning 1) might live inside a Madison workflow.

What matters for you, building a product, is knowing which meaning you are operating in. Because meaning 3 and meaning 4 produce very different failure modes. An autonomous system that hallucinates partway through a twelve-step task has corrupted its own output by the time you notice. A role-in-pipeline that hallucinates at step three fails loudly, immediately, at a known location. The architecture determines how you debug, how you recover, and how much trust your customers can reasonably extend.

Madison uses meaning 4.

<!-- → [TABLE: Four meanings of "agent" — columns: meaning number, informal label, example product, what it implies architecturally, dominant failure mode. Row for each meaning in this section.] -->

---

Now let me show you what Madison actually is.

The [Madison project page](https://www.humanitarians.ai/madison) describes itself as "an open-source, agent-based AI marketing intelligence framework designed to transform branding, marketing, and advertising." Read past the marketing copy and you find the operative sentence: "Madison organizes specialized AI agents that collaborate under an orchestration layer to deliver cohesive, data-driven marketing solutions."

Five layers:

**Intelligence Agents** gather and analyze data — reputation monitoring, trend analysis, sentiment scoring from the morning news cycle.

**Content Agents** create, optimize, and distribute marketing materials — brand voice consistency, multi-platform adaptation, headline variants.

**Research Agents** process data to uncover customer insights — automated survey analysis, synthetic persona development, segmentation.

**Experience Agents** enhance customer interactions through AI concierge systems and customer journey transformation.

**Performance Agents** measure and optimize outcomes — multi-armed bandit experiments, predictive analytics, continuous improvement.

Plus the glue: an **Orchestration Layer** that coordinates all of them through cross-project validation, dynamic resource allocation, and continuous learning from performance metrics.

If you are a working marketer looking at this list, something should feel familiar. This is the same division of labor you would find in any reasonably sized marketing organization. A research team. A content team. An analytics team. A customer experience function. An intelligence function watching the market. Madison has made those boundaries machine-readable.

Sit with that observation for a moment, because it is not obvious and it matters. The question Madison's architects answered — implicitly or explicitly — was: *what is the natural decomposition of marketing work into specialized jobs that can be done well in isolation and assembled into a coherent whole?* And their answer maps almost exactly onto how human marketing organizations divide labor after thirty years of organizational learning.

That borrowing is a feature. Organizations learned to split marketing this way because the functions have genuinely different information needs, different output formats, different cadences, and different success metrics. An Intelligence function needs fresh data every morning. A Content function needs a brief and brand voice parameters. A Performance function needs experiment results. Designing agents along the same boundaries means each one can be optimized for its specific job without knowing how the others work. The orchestration layer handles the connective tissue.

Now I want to show you what the alternative looks like — because the choice of five layers over one mega-agent is the most important architectural decision in Madison, and understanding why it was the right choice illuminates most of what you need to know about multi-agent design.

Suppose we designed Madison as a single large model with a long prompt and access to every data source. On a demo, this works beautifully. In production, three things break.

Token costs become unsustainable. Every time the system runs, it re-reads all available context: the news feed, the brand brief, the experiment results, the customer journey data. By end of day, the same news article has been embedded in twenty different prompts. You are paying for context tokens on work the system has already done.

Failure modes blur. When the system gives a wrong answer — a miscategorized sentiment, a misaligned headline, a broken customer journey recommendation — you cannot locate the fault. Did the model misread the news? Build a bad persona? Draft a tone-deaf message? In a mega-agent, the answer is "somewhere in the model," which is not actionable.

The product has no surfaces. From the customer's perspective, the mega-agent is a black box. There is nothing to name, version, sell separately, or improve in isolation. No feature roadmap. No pricing tier. No partner integration.

<!-- → [FIGURE: Side-by-side diagram — left: five labeled agent boxes connected through a central orchestration node with labeled input/output arrows; right: one opaque "mega-agent" box annotated "no surfaces, no fault location." Caption: the same capability, two different architectures, two different products.] -->

Now contrast the layered design. Each layer is specialized, inspectable, and named. The Intelligence Agent delivers scored news to the orchestrator. The Content Agent takes a brief and returns three headline variants. The Performance Agent runs experiments on which variant lands. Each one can be tested, versioned, swapped, and — crucially — *named* in the product. A customer can say: "Our Intelligence layer is running; our Content layer is broken." That is a diagnostic capability. It is also a sales capability: you can sell tiers, sell add-ons, sell the Intelligence layer to a customer who does not need the Content layer.

Here is the part that trips people when they first encounter it: the five-layer choice is simultaneously an engineering decision and a brand decision. The same architectural choice that improves debuggability also makes the product saleable. The architecture produces a product surface the brand can attach to — and it does so as a direct consequence of engineering choices made for entirely mechanical reasons.

Hold that principle. We will come back to it.

---

Before we go deeper into Madison's mechanics, I want to anchor the architecture discussion in two products you may already use — because Madison's design decisions look different once you have seen the same underlying technology produce radically different architectures.

[Cursor](https://cursor.com/) is a fork of Visual Studio Code with AI woven into the editing surface. The architectural commitment is augmentation: the developer stays in the driver's seat at all times. Real-time completions, inline chat, multi-file agent mode — but always with the developer reviewing and approving each change. Cursor's brand is "AI for engineers who want to be better engineers."

[Devin](https://devinai.ai/), built by Cognition Labs, runs in a sandboxed cloud environment with its own IDE, browser, and shell. Devin 2.0 introduced multiple parallel instances in isolated virtual machines, each working through a well-specified task with limited human intervention. Devin's brand is "AI engineers you assign work to."

Same underlying technology stack. Same frontier LLMs. Wildly different architectures. And consequently, wildly different brand positions and customer relationships.

A senior developer choosing between Cursor and Devin is not comparing capabilities. They are comparing models of agency and trust. Cursor says: *you remain expert; we accelerate you.* Devin says: *we handle the defined work; you handle the judgment calls.*

Madison's choice of a five-layer orchestrated pipeline puts it on the Cursor end of this spectrum, not the Devin end. Each layer does a defined job; the orchestration layer connects them; humans review at the points where consequential decisions land. This is not because autonomy is bad. It is because marketing decisions that go wrong in the wild are expensive in ways that a sandboxed coding task is not. A tone-deaf campaign post, a mispriced offer, a misread sentiment trend — these have real costs that are asymmetric and hard to reverse. The architecture encodes a theory of risk.

When you choose your own architecture, you are choosing a theory of risk. Make that choice explicitly.

<!-- → [FIGURE: Horizontal spectrum from "user in full control / augmentation" (left) to "system autonomous, human reviews outcomes / delegation" (right). Cursor at left, Devin at right, Madison left-of-center highlighted. Each endpoint annotated with brand position and recovery model.] -->

---

I have been talking about what Madison's layers *do* as if they were static modules. Now I want to show you the small machine running inside each one — because it changes how you reason about failure, performance, and design.

The pattern comes from Yao et al.'s 2023 paper, "ReAct: Synergizing Reasoning and Acting in Language Models," published at ICLR. ReAct's core observation is that an LLM doing useful work in the world needs to interleave two operations: *reasoning* (thinking about what to do next, in natural language) and *acting* (calling a tool, querying an API, modifying state). Pure chain-of-thought is all reasoning — the model talks to itself but cannot reach into the world. Pure tool-use without reasoning is reactive — the model calls APIs without a coherent plan for what to do with the results. ReAct interleaves the two, and Yao et al. showed this beats both alternatives: 34 percentage points better than imitation learning on ALFWorld, a household task benchmark.

Here is the loop in abstract form:

```
THOUGHT: [LLM reasons about the current state and what to do next]
ACTION:  [LLM calls a tool — search, API, file read, write]
OBSERVATION: [Tool returns a result]
THOUGHT: [LLM updates its reasoning in light of the result]
ACTION:  [LLM takes the next action]
... [loop continues until goal reached or stopping condition fires]
```

Now watch what a Madison Intelligence Agent looks like when you write out its actual reasoning trace:

```
THOUGHT: It is 7 a.m. Time to pull the daily news cycle for Brand X.
ACTION:  Pull RSS feeds, Google News API, watched subreddits.
OBSERVATION: 870 articles received.

THOUGHT: Deduplicating before scoring saves tokens and prevents counting
         the same story multiple times.
ACTION:  Run MD5 hash on titles; Levenshtein distance on near-matches.
OBSERVATION: 87 unique articles remaining.

THOUGHT: Score each article for sentiment and topic relevance.
ACTION:  Send each article to GPT-4o-mini with sentiment scoring prompt.
OBSERVATION: 87 articles returned with scores and relevance tags.

THOUGHT: Write results to storage and trigger dashboard refresh.
ACTION:  Append to Google Sheet; fire Plotly dashboard webhook.
OBSERVATION: Dashboard updated. Job complete.
```

Each step is a thought-action-observation cycle. The LLM is not just calling APIs — it is *reasoning about why* it is calling them and *what to do* with the results. That is what makes this an agent in meaning 2, even though it functions as a role in meaning 4. The same loop runs in every Madison layer, with different tools and different reasoning prompts. The Research Agent reasons about survey data and acts on clustering calls. The Content Agent reasons about brand voice parameters and acts on generation calls. The Performance Agent reasons about experiment results and acts on Thompson sampling allocation calls.

<!-- → [FIGURE: One complete ReAct cycle for the Intelligence Agent — four nodes in a loop: THOUGHT → ACTION → OBSERVATION → THOUGHT. The feedback arrow from OBSERVATION back to THOUGHT highlighted. Annotated with the actual content from the news-scoring trace above.] -->

Understanding the loop also teaches you where the failure modes live.

A *reasoning failure* is when the model decides to do the wrong thing because it misread the state. Scoring all 870 articles without deduplicating first. Expensive, recoverable — it produces a result, just an overpriced one.

An *action failure* is when the tool call fails, returns an error, or returns data in an unexpected format. A well-designed agent handles this gracefully: the observation *is* the error, the next thought reasons about recovery. A poorly designed agent either crashes or hallucinates a response as if the tool call had succeeded. The second is much worse.

An *observation failure* is the most dangerous kind. The tool returns a plausible-looking but incorrect result, and the model's reasoning does not catch it. The loop continues on false premises. This is why the Performance layer in Madison matters so much: it creates a closed feedback loop where eventual real-world outcomes — did the content actually perform? — can correct errors that slipped through the reasoning-action-observation chain upstream.

Knowing these failure modes in advance shapes how you design your own loops. You want action failures to be loud. You want observation failures to be recoverable. You want at least one layer in your system whose job is checking that the other layers were right.

---

Each Madison layer runs its own ReAct loop. The orchestration layer connects them. Understanding orchestration is where the most consequential design decisions live — and where the most consequential failures happen.

There are two dominant orchestration patterns in 2026. Madison uses one. The other is worth knowing.

**Graph-based orchestration** — n8n and LangGraph are the leading examples — treats the workflow as a directed graph. Nodes are operations: a Python function, an LLM call, a database write. Edges are data flows: the output of node A becomes the input of node B. The workflow is defined in advance. Every path through the graph is explicit. Every edge is testable. Madison's reference implementation uses n8n for this.

**Conversation-based orchestration** — Microsoft AutoGen is the leading example — treats agents as conversation participants. The orchestrator is a meta-agent that communicates with sub-agents in natural language. Agents can talk to each other directly, negotiate, and self-organize to handle task sequences that were not pre-specified.

The trade-off names itself. Graph-based orchestration is predictable: every step is defined, every failure is locatable, every path is auditable. Conversation-based is flexible: agents can handle novel task sequences that no one anticipated, but the failure modes are harder to isolate and the debugging surface is enormous.

Madison chose predictability. For a marketing intelligence framework that needs to run at 7 a.m. every day, write clean data to a stable schema, and feed a dashboard a marketing director trusts, predictability is the correct trade. For a research assistant exploring a genuinely novel question — where the right sequence of actions depends on what earlier actions discover — conversation might be better.

The core technologies Madison deploys reflect this commitment to structured, auditable work: GPT-4o and BERT for language tasks, PCA and clustering for data analysis, Thompson sampling and contextual bandits for content optimization, Neo4j and RDF for knowledge graph work. Neo4j for brand perception tracking because graph databases represent relationships between brand entities naturally. Thompson sampling because it handles the exploration-exploitation trade-off in multi-armed bandit problems better than naive approaches. Each technology choice is a production choice, not a novelty pick. They compound: each one makes the system more legible to the engineer maintaining it and more trustworthy to the customer paying for it.

<!-- → [TABLE: Graph-based vs. conversation-based orchestration — columns: property, graph-based (n8n/LangGraph), conversation-based (AutoGen). Rows: failure locatability, handling of novel task sequences, auditability, debugging surface, best fit use case.] -->

One more orchestration choice worth naming: where humans sit in the pipeline. Madison includes "human-in-the-loop validation" as an explicit feature. Consequential decisions — what content to publish, how to allocate campaign budget, what persona to use for a customer interaction — are reviewed by a human before execution. This is the right choice for marketing work in 2026. The downside of a bad autonomous marketing decision is severe and hard to reverse; the upside of removing the human review is modest. Where you place humans in your own pipeline is not a philosophical question. It is a risk-engineering question. Identify the decisions in your system where a wrong answer is expensive and hard to reverse. Put humans there. Automate everything else.

---

I want to make the brand argument explicit now, because it is the insight this chapter was designed to produce.

Every architectural choice you make has a brand consequence. Not in the sense that it changes your logo. In the sense that it determines what your customers can see, name, trust, and rely on.

Five named layers instead of one mega-agent means a customer can say: "Our Intelligence layer is running; our Content layer is broken." That sentence is a diagnostic capability. It is also a sales capability — you can sell tiers, sell add-ons, sell the Intelligence layer to a customer who does not need the Content layer. You can version each layer independently. You can communicate changes clearly. You can hire a vendor to replace one layer without rebuilding the system. None of this is possible if your product is a black box.

The Cursor / Devin comparison makes the same point from a different direction. Cursor's architecture — AI embedded in the editor, developer always in control — creates a brand position: *we trust developers*. Devin's architecture — autonomous agent in a sandboxed environment — creates a different one: *we handle defined work so you don't have to*. Neither position was articulated in a marketing document first. Both emerged from architectural commitments made for technical reasons, whose brand implications became visible later.

This is how most product positioning actually works. Engineers make choices. Choices create affordances. Affordances create brand experience. Marketing writes copy that describes the experience the engineers already produced.

You are in the rare position of designing a product from scratch. You can run this process deliberately: choose the architecture with the brand consequences you want, rather than discovering your brand in the choices you made for other reasons.

Most textbooks about AI products do not contain that sentence. I am putting it here because it is true and it matters for the work you will do in Chapter 4.

---

Madison is a reference architecture, not a template. Reading it well teaches you what to do. Copying it produces a worse Madison. Here is how to extract what is useful.

Start with the overview page before the code. The [Madison project page](https://www.humanitarians.ai/madison) names the five-layer architecture, the orchestration approach, and the core technology choices in language any practitioner can parse. You need that mental model before any implementation detail makes sense.

Pick one layer and trace it end to end. Find the Intelligence Agent in the [GitHub repository](https://github.com/Humanitariansai/Madison). Look for the workflow definition and the LLM call. You will not understand every detail on a first reading. What you are looking for is the shape of the pipeline — ingestion, reasoning, action, observation, output. Once you can see that shape in one Madison layer, you will see it in every agent system you encounter.

Let your archetype pick your layer. A Sage archetype — analytical, insight-driven — should start with the Intelligence layer. A Creator should start with the Content layer. A Caregiver should start with the Experience layer. The archetype narrows the vast design space to the piece of Madison that corresponds to the problem you actually care about solving.

And notice what Madison's architecture does not solve. Madison is built for organizations that already have data sources, brand guidelines, and marketing workflows. The Knowledge Graph infrastructure (Neo4j, RDF, SPARQL) for brand perception tracking assumes you already have brand perception worth tracking. Every architecture embeds assumptions about who the user is and what state they are already in. Reading those assumptions teaches you what the architecture is actually for — and what you will need to supply differently.

<!-- → [TABLE: Madison layers by best-fit archetype — columns: layer name, primary function, best-fit archetype, what to customize, one failure mode to watch. One row per layer.] -->

---

Let me pull it together so the connections are explicit.

Madison's five-layer architecture is a solution to three compounding problems: token economics, failure isolation, and product legibility. These three problems are not independent — they compound. A system with poor failure isolation is also hard to sell, because customers cannot identify what went wrong or trust that it has been fixed.

The ReAct loop — reasoning, acting, observing — is the small machine inside each layer. Understanding it tells you where the failure modes live and how to design against them. The Performance layer closes the feedback loop that catches what the other layers miss.

Graph-based orchestration connects the loops and encodes the theory of risk. Where you put humans in the pipeline is where you have decided the consequences of being wrong are too high to automate.

And all of it — every engineering choice — has a brand consequence. The architecture determines what the customer can see, name, trust, and buy. That is design philosophy dressed as system design.

Here is the integrating principle to carry into Chapter 3:

> A multi-agent system is a theory of how a job should be decomposed, in code. The decomposition determines how the system fails, how it is sold, and how it is trusted. Design the decomposition first. The code is implementation.

---

## Chapter Summary

The word "agent" is now a diagnostic tool for you, not a piece of vocabulary. When you hear it, you ask: which of four meanings? That question alone routes you to the right failure modes, the right orchestration pattern, the right brand consequences. Most people building AI products in 2026 cannot ask it. You can.

The deeper thing this chapter was trying to produce is the understanding that architecture is not a neutral engineering choice. Every structural decision — five layers versus one, graph orchestration versus conversation, humans at these approval points and not those — encodes a theory of risk, a theory of labor decomposition, and a theory of what customers need to see in order to trust the system. Madison's architects probably did not articulate it this way. But the five-layer structure maps almost exactly onto how mature marketing organizations divide labor, which is thirty years of accumulated organizational learning about what tasks need different rhythms, different data, different success metrics. That borrowing was either deliberate or remarkably lucky. Either way, it is the right answer.

The common mistake — and I have watched it happen repeatedly — is designing the most capable system imaginable rather than the most legible one a customer will trust. Capability without legibility is a demo. Legibility without capability is a toy. Madison earns its value because it chose legibility as the primary constraint and found that capability followed naturally from specialization.

If you can explain to a non-technical marketing director why Madison has five agents instead of one, and why that matters for their Monday morning dashboard, you understand this chapter. That is the test. Everything else is detail.

---

## Connections Forward

Chapter 3 stress-tests your archetype with richer evidence. You will bring the layer you picked here — and the theory of why it fits you — and you will have that theory challenged. The archetype that survives the challenge is the one worth building around.

Chapter 4 asks you to write a Product Requirements Document specifying a tool that takes a Madison pattern and applies it to a problem of your choosing. The quality of that document depends entirely on how clearly you understand the pattern you are applying — which is what this chapter was for.

**What would change my mind:** A production deployment study showing that conversation-based multi-agent systems outperform graph-orchestrated systems on production reliability metrics — not capability benchmarks, but uptime, debuggability, and mean time to recovery. The current evidence suggests graph orchestration is winning the production fight. That could change.

**Still puzzling:** The exact boundary between "agent as role" and "agent as autonomous system" has not stabilized. Devin claims autonomy; in practice it runs in a sandboxed environment with humans reviewing most pull requests. Madison uses orchestrated roles; in practice the LLM inside each layer makes local decisions that look agentic. I used four meanings as a scaffold in this chapter. I expect a cleaner taxonomy to emerge within two years.

---

## Exercises

### Warm-Up

**W1.** List the four meanings of "agent" from this chapter. For each, give one real product or tool from 2025–2026 that uses that meaning. Which meaning does Madison use?
*Tests: Objective 1 — define agent with precision.*
*Difficulty: Low.*

**W2.** Name Madison's five agent layers and the orchestration layer. For each, write one sentence: what does this layer take as input, and what does it produce as output?
*Tests: Objective 2 — describe the five-layer architecture.*
*Difficulty: Low.*

**W3.** The ReAct loop has three steps: Thought, Action, Observation. Write out a five-step ReAct trace for the Madison Performance Agent optimizing between two headline variants. You can invent plausible-sounding data; label it as hypothetical.
*Tests: Objective 3 — trace the ReAct loop through a layer.*
*Difficulty: Low-medium.*

### Application

**A1.** Take a marketing task you have actually done — sending a campaign, writing a social post, analyzing survey results — and map it to one Madison layer. Write a ReAct trace showing how the corresponding Madison agent would do that task. Identify one place where the agent's reasoning might fail and one place where the observation might be unreliable.
*Tests: Objectives 2 and 3.*
*Difficulty: Medium.*

**A2.** A startup tells you they built a "unified AI marketing agent" — one model that does everything Madison distributes across five layers. Using the three failure modes (token costs, failure blur, no product surfaces), write a two-paragraph technical critique of their architecture. Be specific: give one example of each failure mode as it would manifest in their product.
*Tests: Objective 2.*
*Difficulty: Medium.*

**A3.** Graph-based and conversation-based orchestration are described in this chapter. Suppose you are building a competitive intelligence tool for a hedge fund — daily sentiment scoring on 500 public companies, delivered to analysts at 6 a.m. Which orchestration model do you choose and why? Now suppose you are building a research assistant for a pharmaceutical scientist exploring an unknown disease mechanism. Which orchestration model do you choose and why? Write two paragraphs, one per scenario.
*Tests: Objective 5.*
*Difficulty: Medium.*

**A4.** The chapter argues that "architecture is brand." Find one product you use regularly — any software product, not necessarily AI — and make the argument that one of its architectural choices is also a brand choice. What was the engineering reason for the choice? What is the brand consequence? What would the product's brand position be if they had made the opposite architectural choice?
*Tests: Objective 4.*
*Difficulty: Medium.*

### Synthesis

**S1.** The Cursor / Devin comparison uses two products with the same underlying technology and different architectures to illustrate different brand positions. Find a second pair of products from any domain that makes the same point: same underlying capability, different architecture, different brand position. Write a structured comparison: architecture of each, how they differ, what brand position each produces, and which theory of risk each encodes.
*Tests: Objectives 4 and 5.*
*Difficulty: Medium-high.*

**S2.** Design a sixth Madison layer — call it whatever you want — that addresses a gap you see in the five existing layers. Specify: what it does, what it takes as input, what it produces, how it connects to at least two existing layers through the orchestration layer, and what failure mode is specific to your layer. Then argue whether your layer should use graph-based or conversation-based orchestration, and why.
*Tests: Objectives 1, 2, 3, and 5.*
*Difficulty: High.*

**S3.** The Feynman test asks: can you explain to a non-technical marketing director why Madison has five agents instead of one, and why that matters for their Monday morning dashboard? Write that explanation in 200 words or fewer, in plain English, without using the words "agent," "token," "orchestration," or "ReAct." Then write a second version for a CTO. Compare: what changed between the two versions, and what stayed the same?
*Tests: Objectives 1, 2, and 4.*
*Difficulty: High.*

### Challenge

**C1.** The chapter ends with a "Still puzzling" note: the boundary between "agent as role" and "agent as autonomous system" has not stabilized. Propose a taxonomy that resolves this ambiguity. Your taxonomy should use at least three dimensions (not just a binary), correctly classify Madison, Cursor, Devin, and one other system of your choosing, and predict what a "fully autonomous marketing agent" would look like on your taxonomy — and whether it would be desirable.
*Tests: All objectives.*
*Difficulty: Very high.*

**C2.** The chapter claims that graph-based orchestration is winning the production fight over conversation-based orchestration in 2026. Find evidence that challenges this claim — either a production deployment of a conversation-based system that outperforms graph-based on reliability, or a theoretical argument for why conversation-based systems will close the reliability gap. Evaluate the strength of your evidence honestly. What would it take to change the chapter's claim?
*Tests: Objective 5; stress-tests the book's own arguments.*
*Difficulty: Very high.*

---

## LLM Exercise — Self-as-Project

**Project:** Self-as-Project
**What you're building this chapter:** A "Personal Career Architecture" doc that treats your job search as a multi-agent system you orchestrate.
**Tool:** Claude Project (your *"My Personal Brand"* project from Chapter 1).

**The Prompt:**

```
Use my Personal Brand Baseline (already in this project's files / context) as the starting point.

Chapter 2 teaches the Madison framework: a five-layer agent architecture
(Intelligence, Content, Research, Experience, Performance) plus an
orchestration layer. Each layer is a specialized role with defined inputs
and outputs.

I want to apply that pattern to my own job search. Treat me as the
orchestration layer. Treat the work my career requires as a set of
specialized roles I either do myself or delegate to AI tools.

For each of the five Madison layers, write:

1. Intelligence — what I need to know about the AI / tech / brand-AI job
   market. What signals matter (job posting trends, companies hiring, recent
   funding, recent layoffs, technology shifts). What sources feed this.
   How often I should refresh.

2. Content — what I need to publish to be visible. What kinds of artifacts
   (blog posts, GitHub commits, LinkedIn updates, portfolio pieces, comments
   on others' work). What cadence is sustainable for me.

3. Research — what I need to learn about specific employers I'm targeting.
   How I research a company before applying or before an interview.
   What I should know that most candidates won't bother to find.

4. Experience — what the people-facing work looks like. Networking
   conversations, informational interviews, follow-ups, recruiter
   relationships. Who I should talk to. How often.

5. Performance — what I measure. Application count is wrong; outcomes per
   application is closer. Networking conversations per week. Response rate
   on outreach. What metrics actually predict offers.

For each layer, give me:
- One concrete weekly action I commit to
- One AI tool that could augment that layer (Claude, Cursor, an n8n
  workflow, a custom GPT, etc.) — name it specifically
- One failure mode I should watch for in that layer

Then — based on my archetype from Chapter 1 — tell me which layer is most
load-bearing for my brand. A Sage gets traction through Intelligence +
Content. A Hero through Performance + Experience. A Magician through
Content + Experience. A Caregiver through Experience + Research.
Pick mine and justify.

Output a Markdown document called "Personal Career Architecture — [my name]"
with the five layer plans plus the load-bearing-layer call.
```

**What this produces:** A career-systems document. Five named layers, weekly commitments, tool suggestions, failure-mode watch list, and a clear answer to "where should I put the most energy."

**How to adapt:** If you're not job-searching (e.g., applying to PhD programs or starting a company), reframe the layers — Intelligence becomes program/market research; Performance becomes publication count or revenue. Builds directly on the archetype from Chapter 1.

**Preview of next chapter:** Chapter 3 stress-tests your provisional archetype against richer evidence and forces you to commit — or revise.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Marshall McLuhan** spent the 1960s arguing — to a public that mostly didn't yet have the vocabulary for it — that the *medium* shapes the message it carries, and that the architecture of a communication system is the message far more than any individual transmission through it. The Madison framework's central claim is the same shape, applied to AI tooling: the structural choices in the workflow (parallel ingestion branches, audit logs, the role split across the five agents) are the brand long before the marketing copy is written.

![Marshall McLuhan, c. 1960s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](../images/marshall-mcluhan.jpg)
*Marshall McLuhan, c. 1960s. AI-generated portrait based on a public domain photograph.*

![Marshall McLuhan](../images/marshall-mcluhan-2tn.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Marshall McLuhan, and how does his claim that *the medium is the message* connect to the Madison framework's argument that an AI system's architecture *is* the brand — that the role split, the contracts, the audit trail are the message far more than any UI copy? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Marshall McLuhan"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain "the medium is the message" in plain language, without quoting *Understanding Media*
- Ask it to compare McLuhan's hot-vs-cool media distinction to the difference between a chatbot interface and an agentic workflow
- Add a constraint: "Answer as if you're writing the architectural rationale for a five-agent Madison-style system"

What changes? What gets better? What gets worse?

---

---

## AI+1 — Self-as-Project on Madison

**Project:** Self-as-Project — *your brand, end to end*
**This chapter adds:** the role map for your brand's pipeline — which Madison roles you need, and where humans gate.
**Madison recipes:** [`madison-marketing-intelligence-orchestrator`](../madison/recipes/madison-marketing-intelligence-orchestrator.md), [`intelligence-agent`](../madison/recipes/intelligence-agent.md)

> The architecture *is* a brand surface (this chapter's thesis). You decide the decomposition; Madison runs the roles; you gate the decisions that carry brand risk.

### Exercise 1 — When to Use AI
- *Map your brand tasks onto the five roles + orchestration.* **Why it works:** drafting a structure you then correct.
- *Draft the input/output contract for each role.* **Why it works:** reformatting a known division of labor.
- *Spot which role your brand currently has no coverage for.* **Why it works:** pattern-spotting a gap you confirm.

**Tell:** you can independently evaluate the role map against your real work.

### Exercise 2 — When NOT to Use AI
- *Deciding which brand decisions stay human-gated.* **Why it fails:** accountability is non-delegable — the chapter's whole point.
- *Choosing graph- vs. conversation-based orchestration for your case.* **Why it fails:** a design trade-off the model will paper over.
- *Accepting a vendor's "one autonomous agent does everything" claim.* **Why it fails:** failure-blur — you must reason about where it fails loudly vs. silently.

**Tell:** you've crossed the line when "the orchestrator decided" replaces your reasoning.
**Series connection:** trains architecture literacy — hearing "agent" and asking *which of four meanings*.

### Exercise 3 — Recipe Exercise
**Build:** a one-page role map for your brand pipeline. **Run:** [`madison-marketing-intelligence-orchestrator`](../madison/recipes/madison-marketing-intelligence-orchestrator.md) over your Chapter 1 signal baseline. **Tool:** Claude Project.

```
Using the Madison orchestrator recipe approach, draft the agent role map for MY
brand pipeline. For each of the five roles (Intelligence, Content, Research,
Experience, Performance) plus the orchestration layer, state: input, output,
cadence, and the named failure mode if this role hallucinates. Then mark which
TWO decisions in this pipeline must stay human-gated and why. Use my Ch 1 signal
baseline as context. Invent no metrics; this is a structural draft.
```
**Adapt:** drop roles your brand genuinely doesn't need yet — name the omission as a scope choice, not an oversight.

### Exercise 4 — CLI Exercise
**Build:** `your-brand/role-map.md`. **Tool:** [`wrap-your-tool`](../madison/wrap-your-tool/) or Claude Code.

```
Write your-brand/role-map.md: a table (role | input | output | cadence | failure
mode | human-gated?) for the five roles + orchestration, tuned to my brand. End
with one line naming the role with no current coverage. Do not invent performance
numbers. Stop after writing the file.
```
**Inspect:** every role has typed I/O and a named failure mode; at least one decision is human-gated.
**If it goes wrong:** the model marks everything "human-gated" to be safe — force it to choose exactly the decisions where brand accountability actually lives.

### Exercise 5 — AI Validation Exercise
**Validate:** the role map. Pass / Fail / Cannot-determine, one line of evidence each:
- **Correctness:** does each role's I/O match the four-meanings-of-agent distinction (role-in-pipeline, not autonomous)?
- **Completeness:** five roles + orchestration all present with failure modes?
- **Scope:** a *map*, not a build plan?
- **Brand-specific:** is "architecture as brand surface" reflected — does the map imply something a customer would feel?
- **Failure-mode:** does any role silently depend on another's unverified output? Name it.

**Tags:** madison-framework · multi-agent-systems · ReAct · n8n · architecture-as-brand · cursor · devin · agent-loop · orchestration · INFO-7375
