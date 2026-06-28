# Chapter 22: ShipIt — AI Intelligence and Multi-Agent Systems — Practice Exercises

*INFO 7375 · Branding and AI · Northeastern University*

---

> **How to use these exercises:**
> Work through each tier in order. Do not skip ahead to later tiers before completing earlier ones — the tiers scaffold your understanding. Attempt every exercise before checking the answer key. For open-ended questions, write at least 2–3 sentences before reading the model answer. The act of attempting is where the learning happens.

---

## Learning Objectives

- Identify and distinguish the four AI intelligence patterns (single LLM call, chained calls, tool-using agent/ReAct, multi-agent system)
- Explain the orchestrated vs. autonomous multi-agent distinction and its production reliability consequences
- Identify and explain the three autonomous-agent failure modes (compounding error, cost runaway, trust collapse)
- Map archetypes to appropriate architecture choices and identify when an architecture expresses the archetype's shadow
- Apply the Cursor-vs.-Devin (augments vs. automates) distinction to architectural decisions
- Write a complete agent specification with anti-hallucination guards

*Every exercise below maps to at least one of these objectives. The `(Tests: ...)` tag on each exercise identifies which one(s) by full concept name.*

---

## Worked Example

*Study this example before attempting Tier 1. After reading it, close it and try to recall the key steps from memory before moving on.*

**Problem:** A student is building a Sage-archetype newsletter tool that summarizes peer-reviewed climate technology research for a non-specialist audience. They are deciding whether to use Pattern 2 (chained calls) or Pattern 3 (tool-using agent/ReAct). Apply the chapter's framework to make the architectural decision and write the decision statement.

**Approach:**
- Step 1 — Identify the task structure. The task is: (1) find recent research on a given topic, (2) extract key findings, (3) write a summary in non-specialist language, (4) fact-check that the findings are attributed to real, verifiable sources. Can these sub-tasks be fully enumerated in advance? Largely yes — the sequence is predictable.
- Step 2 — Assess whether adaptive reasoning is required. Pattern 3 (tool-using agent) is appropriate when "the task requires genuinely adaptive reasoning and the space of sub-tasks cannot be fully enumerated in advance." Here, the task is sequential and predictable. The newsletter is produced on a defined schedule from defined sources. Pattern 2 (chained calls) is more appropriate.
- Step 3 — Apply the Sage archetype check. The Sage's shadow is dogmatism — wrong answers delivered with high confidence. A tool-using agent's autonomy creates a higher risk of compounding errors that produce a confident-sounding wrong answer (dogmatism in code). A chained call architecture allows validation between each step, reducing the risk of a confident error propagating through the full output.
- Step 4 — Write the decision statement. The chapter requires an explicit, written decision statement before building.

**Answer:** Decision statement: "This pipeline uses chained calls to research and summarize climate technology findings, because the task decomposes into three natural sequential sub-steps (search, extract, summarize) and I need to validate the research output at step 2 before the summarization step produces public-facing text. The Sage archetype's anti-shadow requirement — that the system must never produce confident wrong answers — reinforces this choice: chained calls allow a validation step between research and summarization that an autonomous agent does not provide by default."

**What to notice:** The decision statement explicitly connects the architectural choice to the archetype constraint. The chapter's core argument is that architecture and archetype are not independent decisions — the failure mode most likely to destroy the brand is the archetype's shadow expressed in code.

---

## Tier 1 — Warm-Up (Exercises 1–6)

*Bloom's Level: Remember / Understand*
*Purpose: Verify that the chapter's core concepts and vocabulary are in place before you apply them.*

---

**Exercise 1**

Name the four AI intelligence patterns. For each, write one sentence describing who or what controls the next step in the workflow.

*(Tests: four AI intelligence patterns — names and control structure)*

**Answer:** (1) Single LLM call: the workflow (the developer's code or n8n graph) controls the entire process — a prompt goes in, a response comes out, the pipeline moves on. The LLM has no agency over what happens before or after. (2) Chained calls: the workflow graph controls the sequence — the developer has pre-determined the order of LLM calls and the data that passes between them. Each LLM call does one task; the orchestrating graph decides what runs next. (3) Tool-using agent (ReAct): the LLM controls the next step within a loop — the LLM reasons about what tool to call, observes the result, reasons again, and decides whether to call another tool or stop. The workflow provides the tools; the LLM decides when and in what order to use them. (4) Multi-agent system: an orchestrator (workflow graph or state machine) decides which agent runs when; each agent is an LLM-driven specialist that does its job and returns. The agents do not control the overall flow; the orchestrator does.

**Common error:** Describing chained calls as similar to multi-agent systems because "both have multiple LLM calls." The critical difference is in who controls the next step: in chained calls, the workflow graph controls the sequence deterministically; in multi-agent systems, specialized agents do differentiated work within an orchestrator-controlled flow.

*Chapter reference:* Chapter 22, "Four Patterns of AI Intelligence."

---

**Exercise 2**

True / False: An orchestrated multi-agent system, because it uses multiple agents, is a form of autonomous agent system.

*Explain your reasoning in one sentence:*

*(Tests: orchestrated vs. autonomous agents — conceptual distinction)*

**Answer:** False. In an orchestrated multi-agent system, the workflow or state machine decides which agent runs when — the agents do specialized work and do not control their own next step. Autonomy requires each agent to be able to decide its own next step within a goal, which orchestrated systems explicitly prevent. The chapter identifies `allow_delegation=False` in Madison's architecture as the code-level implementation of this distinction.

**Common error:** Agreeing because "multi-agent = many agents = more autonomy." The chapter is explicit that the autonomy dimension and the number of agents are independent — what matters is whether agents control their own next step or whether an orchestrator does.

*Chapter reference:* Chapter 22, "Four Patterns of AI Intelligence — Pattern 4 internal spectrum."

---

**Exercise 3**

The chapter describes three autonomous-agent failure modes from the AutoGPT case. Name all three, explain the mechanism for each in one sentence, and identify the production control that addresses cost runaway.

*(Tests: three autonomous-agent failure modes — mechanisms and production controls)*

**Answer:** (1) Compounding error: each step is conditioned on the previous step; if step N-1 was wrong, step N is built on a false foundation, and errors multiply geometrically across many steps — a 10% error rate per step leaves only a 35% chance of an error-free output after 10 steps. (2) Cost runaway: each step calls a model at a cost; an agent without a hard step ceiling can make arbitrarily many calls in pursuit of a goal it cannot reach or recognize as reached. Three production controls address cost runaway: a maximum step count, a per-execution cost ceiling, and a circuit breaker that halts the agent if it has called the same tool with the same inputs more than N times. (3) Trust collapse on visible failure: when a user watches an autonomous agent loop for forty minutes and produce nothing, the brand fails in real time with the user's money on the meter — visible failure is more damaging to long-term trust than opaque failure, and the damage distributed across the category ("autonomous agents don't work"), not just the specific product.

**Common error:** Naming cost runaway as the most significant failure mode because it is financially tangible. The chapter treats trust collapse as particularly consequential because it damages the entire category of autonomous agents, not just the specific product.

*Chapter reference:* Chapter 22, "What Goes Wrong in the Autonomous Quadrant."

---

**Exercise 4**

Label each of the following as *orchestrated multi-agent*, *autonomous multi-agent*, or *conversational multi-agent*, then give one piece of evidence from the description:

(a) Five specialized agents (intelligence, content, research, experience, performance) coordinated by an n8n workflow graph that determines which agent runs at each step of the pipeline. Each agent cannot hand off work to other agents.
(b) A user provides a high-level objective; the system decomposes it into sub-tasks, assigns them to agents, monitors progress, and loops until the goal is complete or it runs out of steps. The user provides no further input.
(c) Three agents (a writer, a critic, and a fact-checker) communicate outputs to each other iteratively until they collectively converge on a final article. The process runs without a workflow graph.

*(Tests: orchestrated vs. autonomous vs. conversational multi-agent — classification with evidence)*

**Answer:** (a) Orchestrated multi-agent — evidence: the n8n workflow graph determines which agent runs at each step; agents cannot delegate or hand off work. This matches the chapter's description of Madison and CrewAI Flows/LangGraph. (b) Autonomous multi-agent — evidence: user provides a goal and no further input; the system decomposes, assigns, and loops autonomously. This matches the AutoGPT/BabyAGI pattern. (c) Conversational multi-agent — evidence: agents communicate with each other until convergence, with no external orchestrator controlling the flow. This matches Microsoft AutoGen's original pattern.

**Common error:** Labeling (c) as orchestrated because "there is a defined process (write, critique, fact-check)." The distinguishing criterion is whether an external orchestrator decides the sequence — in (c), the agents communicate with each other and converge, without an orchestrator controlling each step.

*Chapter reference:* Chapter 22, "Four Patterns of AI Intelligence — Pattern 4 internal spectrum."

---

**Exercise 5**

The chapter uses the Cursor/Devin contrast to illustrate the difference between "augments" and "automates." In your own words, explain what each term means in this context and why the control-loop tightness is the key variable.

*(Tests: Cursor augments vs. Devin automates — architectural control-loop distinction)*

**Answer:** "Augments" means the human remains in the decision loop: Cursor suggests code in the IDE, the developer sees each suggestion and accepts, rejects, or modifies it before it becomes part of the codebase. The control loop is tight — the feedback interval between AI output and human review is measured in seconds, and the cost of a bad suggestion is low (the developer sees it and discards it before it propagates). "Automates" means the human hands off a task and waits: Devin receives a task, works autonomously, and produces a result. The control loop is loose — the feedback interval may be minutes to hours, and when Devin produces a bad approach, the failure may be discovered after significant downstream work has been built on a bad foundation. Control-loop tightness is the key variable because it determines the cost of a failure: tight loops catch errors before they propagate; loose loops allow errors to compound through many downstream steps before detection.

**Common error:** Describing the distinction as "Cursor is a code suggestion tool and Devin is a coding agent" — this describes the products' features without capturing the architectural principle (control-loop tightness) that makes the distinction matter.

*Chapter reference:* Chapter 22, "Why Architecture Is the Brand Decision."

---

**Exercise 6**

Explain what an anti-hallucination guard is in the context of an agent specification, and name the three patterns from weakest to strongest.

*(Tests: agent specification — anti-hallucination guard patterns)*

**Answer:** An anti-hallucination guard is an instruction embedded in an agent's specification (specifically in the goal or backstory) that directs the LLM to handle uncertainty explicitly rather than fabricating confident-sounding responses. LLMs hallucinate under uncertainty by default because prompts implicitly reward completeness; the guard counteracts this by giving explicit permission or instruction to produce incomplete but honest output. Three patterns from weakest to strongest: (1) Permission to abstain — add to the goal: "If you cannot verify a claim with the information provided, say 'I cannot verify this' rather than guessing." This gives the LLM explicit permission to produce an incomplete answer. (2) Structured output with null fields — require JSON output with a defined schema; fields that cannot be confidently populated are set to `null` with an explanatory note field. This makes incompleteness machine-readable and handleable downstream. (3) Confidence labeling — require the agent to label each claim: `verified`, `inferred`, or `unverifiable`. More informative than null fields but more work to implement. For most projects, Pattern 2 is the recommended starting point.

**Common error:** Treating anti-hallucination guards as post-processing validation steps applied after the agent generates output. The chapter specifically places them inside the goal (before generation), because guards in the prompt are more reliable than guards in a separate validation step.

*Chapter reference:* Chapter 22, "Writing Agent Specifications — anti-hallucination guards."

---

## Tier 2 — Application (Exercises 7–14)

*Bloom's Level: Apply / Analyze*
*Purpose: Use the chapter's concepts in realistic situations.*

---

**Exercise 7** *(Scenario-Based Application)*

For each of the following tasks, identify which AI intelligence pattern (single call, chained calls, tool-using agent, multi-agent) is most appropriate and write the decision statement the chapter's format requires.

(a) A tool that takes a blog post URL and returns a Twitter/X thread version (7 tweets with hooks).
(b) A research tool that takes a company name, searches recent news and LinkedIn, reads the relevant pages, and produces a competitive intelligence summary.
(c) A content pipeline that: (1) extracts topics from a brief, (2) for each topic generates three headline options, (3) scores headlines for clarity, (4) selects the top headline per topic and writes a 200-word section.
(d) A multi-source market analysis tool where one agent gathers competitor data, another analyzes market trends, and a third synthesizes the findings into a strategic memo.

*(Tests: four AI intelligence patterns — pattern identification with decision statement)*

**Answer:** (a) Single LLM call — decision statement: "This pipeline uses a single LLM call to convert a blog post into a Twitter thread, because the task can be fully specified in one prompt (input: article text; output: 7 tweets with hooks) and the output can be validated against the structural requirement (7 items, each under 280 characters)." (b) Tool-using agent (ReAct) — decision statement: "This pipeline uses a tool-using agent to produce a competitive intelligence summary, because the task requires adaptive reasoning (which news is relevant? which LinkedIn profile is the right one? what does the article say that matters for this company?) and the sub-tasks cannot be fully enumerated in advance. Step ceiling: 15 tool calls. Cost ceiling: $0.50 per execution." (c) Chained calls — decision statement: "This pipeline uses chained calls to produce topically organized content sections, because the task has four natural sequential sub-steps and I need to validate topic extraction at step 1 before running headline generation for each topic at step 2." (d) Multi-agent — decision statement: "This pipeline uses a multi-agent system with three agents (competitor research, trend analysis, synthesis) to produce a market memo, because the task decomposes into genuinely distinct specializations and I need each to be independently debuggable."

**Common error:** Recommending a multi-agent system for (a) or (b) because "more agents = more capability." The chapter is explicit that each pattern up the stack adds cost and complexity; use the simplest pattern that meets the task's requirements.

*Chapter reference:* Chapter 22, "Building the AI Layer in Your Pipeline."

---

**Exercise 8** *(Error Analysis)*

> The following agent specification was submitted by a student.

```python
Agent(
    role="Research Assistant",
    goal="Find information about the topic and write a comprehensive summary.",
    backstory="You are a helpful research assistant.",
    tools=["search", "fetch_url", "write_file", "send_email"],
    allow_delegation=True,
)
```

1. Identify three specific problems with this specification.
2. Explain the failure mode each problem is likely to produce.
3. Write a corrected specification for a Sage-archetype competitive intelligence tool.

*(Tests: agent specification — role, goal, backstory, anti-hallucination, allow_delegation)*

**Answer:**
1. Three problems: (a) The goal has no anti-hallucination instruction — "find information and write a comprehensive summary" implicitly rewards completeness, which will cause the agent to produce confident-sounding text even when information is unavailable or uncertain. (b) The tools include `write_file` and `send_email` — a research agent should not have write-to-disk or send-email capabilities, which gives it agency beyond research and creates risk of unintended outputs (writing files to unexpected locations, sending emails the user did not authorize). (c) `allow_delegation=True` — this allows the agent to hand off work to other agents, which is the explicit architecture choice that the chapter identifies as the AutoGPT failure mode in code. A research agent should do its job and return, not spawn sub-agents.
2. Failure modes: (a) No anti-hallucination instruction → the agent fabricates confident-sounding claims when primary sources are unavailable — dogmatism in code, the Sage archetype's shadow. (b) Excessive tool access → the agent may write files or send emails as part of an "efficient" workflow the developer did not intend, with no human in the loop before outputs leave the system. (c) `allow_delegation=True` → the agent can spawn sub-agents or redirect work, removing the orchestrator's control of the flow and introducing unpredictable cost and behavior.
3. Corrected specification:
```python
Agent(
    role="Competitive Intelligence Analyst",
    goal=(
        "Search for and summarize competitor information on the topic provided. "
        "Return a structured JSON with fields: summary (2-3 sentences), key_findings "
        "(list of 3-5 with sources), confidence (verified | inferred | unverifiable per finding). "
        "If you cannot verify a data point, set it null and explain the limitation. "
        "Do not infer from general knowledge when search results are unavailable."
    ),
    backstory=(
        "Expert in competitive intelligence. Prefers evidence and transparency over guessing. "
        "When forced to choose between a complete answer and an honest one, always chooses honest."
    ),
    tools=["search", "fetch_url"],
    allow_delegation=False,
)
```

**Common error:** Identifying only the `allow_delegation` problem and missing the anti-hallucination and tool-scope problems. A strong error analysis names all three.

*Chapter reference:* Chapter 22, "Writing Agent Specifications."

---

**Exercise 9** *(AI Interaction — with verification requirement)*

First, write your own answer without consulting AI:
*"What is the difference between an orchestrated multi-agent system and an autonomous multi-agent system, and what are the production reliability trade-offs between them?"*

Then read the following AI-generated response:

*AI response: "An orchestrated multi-agent system has a central controller — an orchestrator — that directs agents and manages the flow of work. Each agent is specialized and does a specific task. An autonomous multi-agent system gives agents more freedom to decide their own next steps and collaborate without a central controller. In terms of reliability, orchestrated systems are more predictable but less flexible; autonomous systems are more flexible and can handle unexpected situations but are harder to debug and control. The main reliability risk of autonomous systems is that agents can get stuck in loops or take unintended actions, which can be expensive and produce wrong results."*

1. Identify the strongest point in the AI's response.
2. Identify the most significant gap relative to the chapter's treatment.
3. Write a correction or extension.
4. State the specific evidence you would use to verify whether an orchestrated system outperforms an autonomous one for your specific use case.

*(Tests: orchestrated vs. autonomous agents — evaluation of AI output)*

**Answer:**
1. Strongest point: "Orchestrated systems are more predictable but less flexible; autonomous systems are more flexible but harder to debug and control" — this accurately captures the central trade-off.
2. Most significant gap: The AI response omits the compounding error failure mode and the trust collapse failure mode — it mentions "get stuck in loops" and "expensive" (cost runaway), but not the geometric error-compounding mechanism or the brand-level damage of visible failure. The chapter's 10% per-step error rate calculation (35% success at 10 steps, 12% at 20 steps, 1.5% at 40 steps) is the most important reliability argument for orchestration, and it is entirely absent.
3. Extension: "The production reliability argument for orchestration rests primarily on the compounding error mechanism: with a 10% error rate per step, the probability of an error-free autonomous agent chain collapses to roughly 1.5% at 40 steps — not because the model is bad, but because errors multiply at each step that builds on a wrong previous step. An orchestrated system inserts validation between each step, catching wrong outputs before they become foundations for the next step. The second missing piece is trust collapse: when an autonomous agent fails visibly, users associate the failure with the entire category of autonomous agents, not just the specific product. The brand damage is categorical, not individual."
4. Verification test for your specific use case: Build a test suite of 20 inputs covering easy, medium, and adversarial cases. Run the same task through your orchestrated pipeline and through an equivalent autonomous agent. Measure: (1) percentage of outputs that are fully correct, (2) percentage of outputs that contain at least one hallucinated or unattributed claim, (3) cost per execution, (4) execution time. If the autonomous agent outperforms the orchestrated one on all four metrics for your specific task, the architecture recommendation for your use case changes.

*Chapter reference:* Chapter 22, "What Goes Wrong in the Autonomous Quadrant."

---

**Exercise 10** *(Self-Explanation)*

In this chapter, the Madison architecture uses `allow_delegation=False` for every agent. Explain in 2–3 sentences why this single parameter is described as "the orchestration commitment in code" — what failure mode does it prevent, and why is it architecturally significant rather than just a configuration choice?

*(Tests: orchestrated multi-agent — allow_delegation=False as the orchestration commitment)*

**Answer:** `allow_delegation=False` prevents an agent from handing off work to other agents, spawning sub-agents, or redirecting its own task — which are the mechanisms that enable compounding error in autonomous systems. When `allow_delegation=True`, an agent can interpret its goal as broadly as possible and recruit other agents to pursue sub-goals, removing the orchestrator's control over which agent runs when. The parameter is architecturally significant rather than just a configuration choice because it encodes the design decision about where control lives: with the orchestrator (the workflow graph) or with the agents themselves. In the AutoGPT architecture, agents could spawn sub-agents — this is what made the system autonomous and what made failures unlocatable across a distributed trace. Setting `allow_delegation=False` is the single line of code that ensures failures stay local to one agent's output rather than propagating across a distributed agent network.

**Common error:** Treating `allow_delegation=False` as a safety feature added after the system is built. The chapter presents it as an architectural commitment made upfront — it encodes the decision about who controls the flow.

*Chapter reference:* Chapter 22, "The Madison Agents as a Worked Case."

---

**Exercise 11** *(Cumulative — prior chapter concept)*

In Chapter 6, you learned about *archetype shadows* — the failure mode that emerges when an archetype's strength is inverted or unchecked. In this chapter, you are working with the *archetype-architecture mapping* — the claim that the architectural choice is a brand decision, and the failure mode most likely to destroy the brand is the archetype's shadow in code.

For the Explorer archetype, the chapter identifies aimlessness as the shadow — "no destination, no coherent result" — and warns that an Explorer tool is a high-risk candidate for autonomous architecture. Apply this mapping to a specific product scenario: an Explorer-archetype tool that helps screenwriters discover unexpected plot connections across a database of produced films.

What would the Explorer archetype's shadow look like expressed as an AI failure mode in this specific product, and what architectural choice would prevent it?

*(Tests: archetype-architecture mapping + archetype shadows — interleaved application)*

**Answer:** The Explorer archetype's core motivation is discovery, autonomy, and finding unexpected connections — these are the strengths the screenwriting tool is designed to amplify. The Explorer's shadow is aimlessness: the system that explores endlessly without producing a coherent, useful result. Expressed as an AI failure mode in this product: an autonomous agent that receives the query "find unexpected plot connections for a heist film set in a museum" and begins exploring the film database — finding connections, generating sub-queries, pulling related films, identifying structural patterns — without a defined stopping criterion. The exploration continues for forty API calls and fifteen minutes, producing an enormous intermediate result set that the agent cannot synthesize into a usable format because it never stopped exploring to produce. The screenwriter sees a process that ran for a long time and delivered nothing useful. This is the Explorer's shadow in literal form — the autonomous exploration that never reaches a destination. Architectural prevention: use a chained call or orchestrated multi-agent architecture that defines the discovery task as a bounded sequence: (1) identify candidate films by genre/era/setting, (2) extract structural patterns per film, (3) find cross-film pattern overlaps, (4) present the top 5 unexpected overlaps. Each step has a defined output requirement and validation. The Explorer archetype is expressed in step (3) — the creative juxtaposition — not in an unbounded exploration loop.

**Common error:** Concluding that the Explorer archetype cannot be expressed in an AI product because autonomy is its shadow. The chapter argues that the archetype can be expressed through bounded exploration — the Explorer spirit in the *content* of the output, not in the *architecture* of the process.

*Chapter reference:* Chapter 22, "Why Architecture Is the Brand Decision"; Chapter 6, "Archetypes and Shadows."

---

**Exercise 12** *(Scenario-Based Application)*

A team is building a Caregiver-archetype health information tool that answers patient questions about managing chronic conditions. They are considering Pattern 3 (tool-using agent) because "the agent can search for the most recent medical guidelines and provide a comprehensive answer."

Apply the chapter's archetype-architecture mapping to evaluate this choice. What is the Caregiver archetype's shadow expressed as an AI failure mode in this context, and does Pattern 3 serve or endanger the archetype?

*(Tests: archetype-architecture mapping — Caregiver archetype applied to a specific product)*

**Answer:** The Caregiver archetype's core motivation is helping people — warmth, accessibility, and genuine concern for the user's wellbeing. The chapter's archetype-architecture table (not reproduced verbatim but implied by the framework) would suggest the Caregiver's shadow in AI is conditional, but the most dangerous failure mode for a health information tool is an overly confident wrong answer delivered in a warm, reassuring tone. A Pattern 3 tool-using agent, by nature of the ReAct loop, may search for information, find something plausible, and produce a confident-sounding answer without explicit uncertainty signals — especially if the goal does not include anti-hallucination guards. The Caregiver's tone (warm, accessible) combined with a confident but incorrect health claim is the shadow expressed in code: the system feels safe and caring while delivering potentially harmful misinformation. Pattern 3 can be made to serve the Caregiver archetype, but only with specific architectural safeguards: (1) anti-hallucination guards in every agent's goal ("If the answer requires medical advice beyond general health information, say so explicitly and recommend consulting a healthcare provider"); (2) a structured output requirement that includes a confidence level and a source citation for every factual claim; (3) a hard stop rule that routes queries requiring specific medical advice (dosage, diagnosis, treatment) to a "please consult your doctor" response rather than attempting a comprehensive answer. Without these guards, Pattern 3 exposes the Caregiver shadow: confidence where uncertainty would be more honest.

**Common error:** Recommending against Pattern 3 for all health information tools. The chapter's framework recommends architectural choices paired with appropriate guards, not blanket prohibitions based on archetype.

*Chapter reference:* Chapter 22, "Why Architecture Is the Brand Decision" and archetype-architecture mapping.

---

**Exercise 13** *(Application)*

Read the following partial agent specification and identify: (a) what each component is doing, (b) which failure mode each component is designed to prevent, and (c) what is still missing.

```python
Agent(
    role="Climate Technology Research Analyst",
    goal=(
        "Summarize peer-reviewed research on the topic provided. "
        "Return a structured JSON with: summary (2-3 sentences), "
        "key_findings (list of 3-5), sources (list of URLs or DOIs), "
        "confidence (verified | inferred | unverifiable per finding). "
        "Do not include findings you cannot attribute to a specific source."
    ),
    backstory=(
        "A researcher trained in evidence-based communication. "
        "When forced to choose between an interesting claim and a "
        "verifiable one, always chooses verifiable. Never rounds up."
    ),
    tools=["search", "fetch_url", "extract_text"],
    allow_delegation=False,
)
```

*(Tests: agent specification anatomy — role, goal, backstory, tools, allow_delegation)*

**Answer:** (a) What each component does: The role ("Climate Technology Research Analyst") activates LLM training-data associations with evidence-based, professional research contexts — it primes the LLM to behave as an expert who gathers and cites sources. The goal narrows the task to peer-reviewed research, specifies the output schema (JSON with defined fields), requires source attribution, and includes an anti-hallucination instruction ("Do not include findings you cannot attribute to a specific source"). The backstory is the tie-breaker for edge cases the goal did not anticipate — "when forced to choose between interesting and verifiable, always verifiable" tells the LLM how to resolve ambiguous situations the goal cannot enumerate. "Never rounds up" is the key phrase: it instructs the LLM that in a conflict between a complete-looking answer and an honest one, honesty wins. The tools are constrained to three (search, fetch_url, extract_text) — no writing or synthesis tool, because this agent's job is research, not composition. `allow_delegation=False` ensures the agent does its job and returns; it cannot spawn sub-agents. (b) Failure modes prevented: role → prevents wandering and off-topic outputs; goal + schema → prevents unstructured or uncitable outputs; "do not include unfounded findings" → prevents hallucinated claims; backstory "never rounds up" → prevents confident guessing under uncertainty; constrained tools → prevents unintended side effects; `allow_delegation=False` → prevents autonomous branching. (c) What is missing: the goal does not include the instruction about what to do when the topic is outside the search results ("If a topic is outside your search results, say so — do not infer from general knowledge"). This is the second anti-hallucination instruction from the chapter's full example and is important for handling edge cases where the LLM might fall back on training data rather than search results.

**Common error:** Identifying the missing element as "a confidence instruction" when the goal already includes confidence labeling. The specific missing element is the instruction about what to do when search results are absent entirely.

*Chapter reference:* Chapter 22, "Writing Agent Specifications."

---

**Exercise 14** *(Application)*

The chapter describes two ways an AI pipeline can be wrapped with deterministic neighbors: "a fetch step prepares the input, the AI call processes it, a format step normalizes the output, a write step stores it." Explain why each of these deterministic wrapper steps matters — what failure mode does each address, and what would happen if the AI step were "floating in isolation" without them?

*(Tests: wrapping AI steps in deterministic neighbors — validation and failure localization)*

**Answer:** Fetch step (deterministic input preparation): Ensures the AI call receives only the context it needs, formatted consistently. Without this, the AI step may receive malformed input, incomplete data, or context from the wrong source — and the error will appear inside the AI step, which is harder to diagnose than an error in the deterministic fetch step. The fetch step is where the contract with the data source is mediated; if the data source changes its schema, the fetch step is the failure point, not the AI step. Format step (deterministic output normalization): Ensures the AI's output is in the expected structure before it reaches the write step. Without this, a free-text or differently-structured AI output passes directly to a database write or downstream process that expects a specific schema — and the write step fails in a way that is hard to attribute (did the AI produce wrong output, or did the write step fail to parse?). The format step validates the AI's output against a schema and routes to an error handler when the schema is invalid, ensuring the error is surfaced rather than propagated. Write step (deterministic storage): Ensures the data is stored in a verified, consistent location. Without it, the AI step might attempt to write to storage directly, with no intermediate validation that the output is write-ready. The sequence — fetch → AI → format → write — means the AI step is surrounded by deterministic checkpoints that catch input problems before the AI runs and output problems before the data propagates.

**Common error:** Describing the deterministic wrapper steps as "making the pipeline more complex." The chapter's argument is that the wrappers reduce debugging complexity by localizing failures to specific steps — a failure in a deterministic step is easier to diagnose than a failure inside an AI step.

*Chapter reference:* Chapter 22, "Building the AI Layer in Your Pipeline."

---

## Tier 3 — Synthesis (Exercises 15–16)

*Bloom's Level: Analyze / Evaluate*
*Purpose: Connect this chapter's concepts to a concept from a prior chapter.*

---

**Exercise 15** *(Cross-Chapter Synthesis)*

In Chapter 21, you learned about *pipeline reliability as a brand asset* — the chapter argues that a pipeline that runs silently and reliably is invisible to the user (which is exactly what you want), while a pipeline that fails makes the user see the brand fail. In this chapter, you are working with the *trade-off matrix* between autonomous agents (high flexibility, low predictability) and orchestrated multi-agent systems (low flexibility, high predictability).

A team building a Creator-archetype generative content tool argues: "We should use an autonomous agent because flexibility is core to the Creator brand — our tool should be able to explore and surprise users. Predictability is a Sage value, not ours."

Evaluate this argument using both chapters' frameworks. Where is it correct, and where does it misapply the archetype-architecture mapping?

*This question connects pipeline reliability as a brand asset (Chapter 21) to the archetype-architecture mapping (Chapter 22).*

*What distinguishes a surface answer from a strong one:*
- A strong answer uses Chapter 21's reliability argument to explain the brand cost of visible autonomous failures — not just the technical cost
- A strong answer uses Chapter 22's archetype-architecture mapping to distinguish where the Creator archetype should be expressed (in the output's originality) vs. where it should not (in the architecture's unpredictability)
- A strong answer shows the interaction: the autonomy/flexibility trade-off does not mean the Creator archetype requires autonomous architecture — it means the creative output should feel exploratory, regardless of what architecture produces it

*(Tests: pipeline reliability as brand asset + archetype-architecture mapping — Ch. 21 + Ch. 22)*

**Answer:** The team is correct that flexibility and exploration are core to the Creator archetype — the brand promise is originality and the ability to generate something new. But the argument misapplies the archetype-architecture mapping in two ways. First, the chapter explicitly addresses this: "A Creator brand amplifies originality. The Creator's shadow is perfectionism — the system so invested in its own process that it forgets the user's need." An autonomous agent that explores endlessly and delivers nothing is expressing the Creator's shadow (process over output) rather than the Creator's strength (originality). The flexibility of autonomy does not guarantee creative output; it guarantees unpredictability, which is not the same thing. Second, Chapter 21's reliability argument shows the brand cost of visible failure: when a Creator tool fails visibly — loops for thirty minutes, delivers an incoherent result, or costs $80 without producing output — the user does not think "this is charmingly unpredictable." They think the tool does not work. The brand damage flows to the product, not to the architecture. The correct mapping for a Creator tool: the creativity is expressed in the *output* (original, surprising, generative) not in the *process* (autonomous, unpredictable). An orchestrated multi-agent system with specialized agents (one for concept generation, one for variation, one for selection) can produce output that feels exploratory and original while running with the predictability that keeps the brand promise intact. The Creator archetype should be in the content; the orchestration should be in the infrastructure.

*What a surface answer looks like:* "Flexibility is good for Creators but bad for reliability." This mentions both concepts but does not show how the archetype-architecture mapping specifically addresses where the Creator's exploration should be expressed.

*Common error:* Agreeing with the team that autonomous architecture is the only way to express the Creator archetype. The chapter is clear that the Creator's shadow, not its strength, is expressed in architectural autonomy.

*Chapter reference:* Chapter 22, "Why Architecture Is the Brand Decision"; Chapter 21, "Apollo as a brand story."

---

**Exercise 16** *(Cross-Chapter Synthesis)*

In Chapter 20, you learned about the *MVP Boundary* — specifically, that the out-of-scope list must be as disciplined as the in-scope list, and that the $100,000 no defines the product's identity. In this chapter, you are working with the *architectural decision statement* — the requirement to write down which AI intelligence pattern you are using and why, before building.

A student argues: "The architectural decision statement and the MVP Boundary are both about committing to scope before pressure arrives. They are the same discipline applied to different decisions." Evaluate this argument. In what ways are the two discipline mechanisms genuinely analogous? In what specific way do they differ in what they are designed to protect against?

*This question connects the MVP Boundary (Chapter 20) to the architectural decision statement (Chapter 22).*

*What distinguishes a surface answer from a strong one:*
- A strong answer names the genuine analogy precisely
- A strong answer identifies the specific type of pressure each mechanism is designed to resist
- A strong answer shows that the failure mode of not writing the architectural decision statement is different from the failure mode of not writing the $100,000 no

*(Tests: architectural decision statement + MVP Boundary — Ch. 22 + Ch. 20)*

**Answer:** The genuine analogy: both the MVP Boundary and the architectural decision statement are mechanisms for making explicit decisions before the pressure to deviate arrives. The MVP Boundary commits to the out-of-scope list while the team is thinking clearly about product identity; the architectural decision statement commits to the AI intelligence pattern before building, so there is something to evaluate against when the system behaves unexpectedly. Both prevent ad hoc decision-making under pressure from producing incoherent results. The specific differences: (1) Type of pressure. The MVP Boundary is designed to resist *commercial* pressure — a real user with a real budget asking for the refused feature. The architectural decision statement is designed to resist *complexity creep* — the natural drift from a simple pattern (single call) toward a more complex pattern (autonomous agent) because "the task grew" or "we wanted to add this capability." The pressures are different: one is external and commercial; the other is internal and technical. (2) Failure mode when omitted. If the $100,000 no is not written, the team faces commercial pressure without a recorded rationale, and features accumulate through individual in-the-moment decisions. If the architectural decision statement is not written, the team builds without a reference point for evaluating unexpected behavior — when the system does something strange, there is no recorded intent to evaluate against. The chapter: "A student who has written down their architectural choice before building has something to evaluate against when the system behaves unexpectedly. A student who drifted into an architecture has nothing."

*Common error:* Treating the two as identical because "both are about making decisions early." A strong answer names the different pressures and different failure modes.

*Chapter reference:* Chapter 22, "Building the AI Layer in Your Pipeline"; Chapter 20, "The $100,000 No."

---

## Tier 4 — Challenge (Exercise 17)

*Bloom's Level: Evaluate / Create*
*Purpose: Transfer beyond what was explicitly taught.*

---

**Exercise 17** *(Transfer Challenge)*

The chapter's "A Note on What Is Changing" section acknowledges that autonomous-agent failure modes are improving and that by 2027 or 2028, the reliability arguments for orchestration may be substantially weaker. The chapter says: "The choice between autonomy and orchestration is a brand decision. The boundary between where the AI decides and where the human does encodes a theory of what the user should trust, what the product should be accountable for, and what kind of failure the brand is willing to absorb. That principle holds regardless of whether autonomous agents improve."

If autonomous agents achieve parity with orchestrated systems on production-reliability metrics — the three failure modes (compounding error, cost runaway, trust collapse) are substantially mitigated by improved frameworks — what changes about the architecture-as-brand-decision argument? Does the architectural choice between autonomous and orchestrated systems become *less consequential* as a brand expression, or does it remain consequential for *different reasons*?

*A strong response will address:*
- Which parts of the architecture-as-brand-decision argument are stable regardless of reliability improvements
- Which parts of the argument are contingent on the current reliability gap between autonomous and orchestrated systems
- What the new differentiating brand signal would be if both architectures became equally reliable

*(Tests: architecture-as-brand-decision applied to the chapter's own temporal claim)*

---

## Answer Key

> Attempt all exercises before reading this section.
> For Tier 3 and Tier 4, your answer does not need to match the model exactly — use the "what a strong answer includes" criteria to evaluate your own response.

---

**Worked Example**
*No answer needed — the worked example is its own model.*

---

**Ex 1** — *Four AI intelligence patterns*
*Model answer:* Single call (workflow controls, prompt → response). Chained calls (workflow graph controls sequence, deterministic between LLM steps). Tool-using agent (LLM controls next step within a loop). Multi-agent (orchestrator controls which agent runs when; agents do specialized work).
*Common error:* Conflating chained calls and multi-agent because both have multiple LLM calls.
*Chapter reference:* Ch. 22, "Four Patterns of AI Intelligence."

---

**Ex 2** — *Orchestrated vs. autonomous multi-agent*
*Answer:* False.
*Correct because:* In orchestrated systems, the workflow graph controls which agent runs; agents cannot decide their own next step. This is the opposite of autonomy.
*Common error:* Equating "multiple agents" with "autonomous."
*Chapter reference:* Ch. 22, "Four Patterns — Pattern 4 internal spectrum."

---

**Ex 3** — *Three autonomous-agent failure modes*
*Model answer:* Compounding error (errors multiply geometrically across steps). Cost runaway (unbounded API calls without step/cost ceiling). Trust collapse (visible failure damages user trust and the category). Cost runaway production controls: max step count, per-execution cost ceiling, repeated-call circuit breaker.
*Common error:* Treating cost runaway as the most significant failure mode and missing trust collapse's categorical brand damage.
*Chapter reference:* Ch. 22, "What Goes Wrong in the Autonomous Quadrant."

---

**Ex 4** — *Multi-agent system classification*
*Model answer:* (a) Orchestrated — workflow graph controls, `allow_delegation=False`. (b) Autonomous — user sets goal, agents decompose and loop. (c) Conversational — agents communicate with each other until convergence, no external orchestrator.
*Common error:* Labeling (c) as orchestrated because "there is a defined process."
*Chapter reference:* Ch. 22, "Four Patterns — Pattern 4 internal spectrum."

---

**Ex 5** — *Cursor augments vs. Devin automates*
*Model answer:* Augments = human in the loop, tight feedback, low cost-of-failure. Automates = human hands off, loose feedback, errors may compound before detection. Control-loop tightness determines cost of failure.
*Common error:* Describing as "Cursor = code suggestions, Devin = coding agent" without the architectural control-loop principle.
*Chapter reference:* Ch. 22, "Why Architecture Is the Brand Decision."

---

**Ex 6** — *Anti-hallucination guards*
*Model answer:* Instructions embedded in agent goal or backstory that direct the LLM to handle uncertainty explicitly. Three patterns: (1) permission to abstain (weakest), (2) structured output with null fields (recommended starting point), (3) confidence labeling (strongest). Placed inside the prompt before generation, not in post-processing.
*Common error:* Treating anti-hallucination guards as post-processing validation steps.
*Chapter reference:* Ch. 22, "Writing Agent Specifications — anti-hallucination."

---

**Ex 7** — *Pattern identification with decision statements*
*Model answer:* (a) Single call (fully specifiable in one prompt, structurally validatable). (b) Tool-using agent (adaptive reasoning, cannot enumerate sub-tasks, with step and cost ceilings). (c) Chained calls (four sequential sub-steps, validate at step 1 before step 2). (d) Multi-agent (three distinct specializations, independently debuggable).
*Common error:* Recommending multi-agent for (a) or (b) — using the most complex pattern when simpler patterns suffice.
*Chapter reference:* Ch. 22, "Building the AI Layer in Your Pipeline."

---

**Ex 8** — *Agent specification error analysis*
*Three problems:* No anti-hallucination instruction → hallucination. Excessive tools (write_file, send_email) → unintended side effects. `allow_delegation=True` → autonomous branching, unlocatable failures.
*Corrected version:* Sage-archetype competitive intelligence agent with structured JSON output, confidence labeling, constrained tools, `allow_delegation=False`.
*Chapter reference:* Ch. 22, "Writing Agent Specifications."

---

**Ex 9** — *AI Interaction — orchestrated vs. autonomous*
*Model answer:* Strongest: predictability vs. flexibility trade-off. Gap: compounding error mechanism and trust collapse absent. Extension: 10% per-step error rate collapses to 1.5% at 40 steps; trust collapse damages the category. Verification: 20-input test suite measuring correctness, hallucination rate, cost, and time.
*Chapter reference:* Ch. 22, "What Goes Wrong in the Autonomous Quadrant."

---

**Ex 10** — *allow_delegation=False as orchestration commitment*
*Model answer:* Prevents agents from spawning sub-agents or redirecting work, keeping orchestrator control over flow. Architecturally significant because it encodes who controls the process: orchestrator (workflow graph) or agents (autonomous). Ensures failures stay local to one agent's output.
*Common error:* Treating it as a post-build safety feature rather than an upfront architectural commitment.
*Chapter reference:* Ch. 22, "The Madison Agents as a Worked Case."

---

**Ex 11** — *Cumulative: archetype shadows + archetype-architecture mapping*
*Model answer:* Explorer shadow = aimlessness → autonomous agent that explores endlessly without producing a coherent result. Prevention: bounded chained or orchestrated architecture that defines the discovery task as a sequence with defined output requirements at each step. The Explorer archetype is expressed in the output's unexpected connections, not in the architecture's unbounded exploration.
*Common error:* Concluding the Explorer archetype cannot be expressed in AI products.
*Chapter reference:* Ch. 22, "Why Architecture Is the Brand Decision"; Ch. 6, "Archetypes and Shadows."

---

**Ex 12** — *Caregiver archetype applied to health information tool*
*Model answer:* Caregiver shadow in this context = warm, confident wrong health information. Pattern 3 can serve the archetype with guards: "recommend consulting a healthcare provider" for clinical queries; structured output with confidence and source citation; hard stop rule for advice beyond general information.
*Common error:* Recommending against Pattern 3 for all health information tools.
*Chapter reference:* Ch. 22, "Why Architecture Is the Brand Decision."

---

**Ex 13** — *Agent specification anatomy*
*Model answer:* Role: activates research associations, primes evidence-based behavior. Goal: task scope + schema + "do not include unfounded findings." Backstory: tie-breaker ("never rounds up"). Tools: constrained to search, fetch, extract — no writing tools. `allow_delegation=False`: keeps failures local. Missing: "if topic is outside search results, say so — do not infer from general knowledge."
*Common error:* Identifying the missing element as "confidence instruction" when confidence labeling is already present.
*Chapter reference:* Ch. 22, "Writing Agent Specifications."

---

**Ex 14** — *Deterministic wrapper steps*
*Model answer:* Fetch step: mediates data source contract, localizes schema change failures to a deterministic step. Format step: validates AI output against schema before downstream use — surfaces errors rather than propagating them. Write step: ensures write-ready output in a verified, consistent location. Without them, the AI step is the failure point for problems that originated in input or output handling, making debugging harder.
*Common error:* Describing wrappers as making the pipeline more complex rather than reducing debugging complexity.
*Chapter reference:* Ch. 22, "Building the AI Layer in Your Pipeline."

---

**Ex 15** — *Synthesis: pipeline reliability + archetype-architecture mapping*
*Model answer:* Flexibility ≠ autonomous architecture for the Creator brand. Creator shadow (perfectionism/process over output) is expressed in autonomous loops, not in creative output. Chapter 21: visible autonomous failures damage the brand, regardless of archetype. Creator archetype should be expressed in the output's originality, produced by an orchestrated architecture that keeps the brand promise intact.
*What a strong answer includes:* Creator shadow applied to autonomous architecture; Ch. 21 brand damage argument; where the Creator archetype should be expressed.
*Common error:* Agreeing that autonomous architecture is the only way to express the Creator archetype.
*Chapter reference:* Ch. 22, "Why Architecture Is the Brand Decision"; Ch. 21, "Apollo as a brand story."

---

**Ex 16** — *Synthesis: architectural decision statement + MVP Boundary*
*Model answer:* Genuine analogy: both commit to explicit decisions before pressure arrives. Differences: MVP Boundary resists commercial pressure (external, from users); architectural decision statement resists complexity creep (internal, technical drift). Failure modes differ: missing $100,000 no → accumulated commercial feature requests; missing decision statement → no reference point for evaluating unexpected behavior.
*What a strong answer includes:* Precise naming of the genuine analogy; two specific differences in pressure type and failure mode.
*Common error:* Treating both as identical because "both are about making early decisions."
*Chapter reference:* Ch. 22, "Building the AI Layer in Your Pipeline"; Ch. 20, "The $100,000 No."

---

**Ex 17 — Challenge**
*No model answer provided.*
*A strong response will address:*
- Stable regardless of reliability improvements: the choice encodes a theory of what users should trust and what the product is accountable for — this is a brand question that exists independently of reliability
- Contingent on current reliability gap: the current reliability argument for orchestration is strongest when compounding error rates are significant; if autonomous agents achieve per-step error rates approaching zero, the geometric compounding argument weakens
- New differentiating signal if both become equally reliable: the differentiation may shift from "which architecture fails less" to "which architecture makes failure transparent vs. opaque" — the visibility of failure becomes the brand differentiator rather than the frequency of failure
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
