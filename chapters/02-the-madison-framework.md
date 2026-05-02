# Chapter 2: The Madison Framework

> **Voice anchor:** `voice-unanchored` (root style/ has only fry VOICE.md; per-book style/ empty). Voice for this draft is Feynman per CLAUDE.md §6 + textbook:chapter SKILL.md.

## Suggested titles

1. *Five Layers and a Conductor*
2. *Reading Madison Like a Schematic*
3. *The Madison Framework*

## TL;DR

Agent-based AI systems are not magic, and they are not autonomous. They are specialized roles arranged in workflows by an orchestrator, and the architecture choices in that arrangement become the product's brand surface. Madison gives us a five-layer reference architecture; reading it well teaches you to design your own.

---

It is 7:15 a.m. on a Monday. Somewhere in a Frankfurt data center, an n8n workflow wakes up. It pulls 870 articles from RSS feeds, the Google News API, and a watchlist of subreddits. It runs each headline through an MD5 hash and a Levenshtein-distance check, drops the 90% that are near-duplicates of stories it has seen before, and hands the survivors to GPT-4o-mini for sentiment scoring. Three minutes after the trigger fires, the day's first data is written to a Google Sheet. A Plotly dashboard refreshes. Somewhere, a marketing director begins their morning by reading what changed about how the world talks about their brand overnight.

That is one agent in the [Madison framework](https://github.com/humanitariansai/madison). Specifically, the Intelligence Agent — one of five. And every word I just used to describe it ("agent," "framework," "intelligence") is doing more than one job at a time, which is why people who try to build with LLMs trip on these terms more than they trip on the technical work.

This chapter is about reading Madison the way an engineer reads a schematic — to learn what is happening, why those choices were made, and what you would change if you built the next one. By the end you should be able to point at any one of Madison's five layers and explain (a) what it does, (b) why it sits where it sits, and (c) how its architectural shape becomes a brand surface that customers feel.

You should also be able to pick a Madison tool that aligns with the archetype you identified in Chapter 1 — that pick becomes your design reference for the next four chapters.

---

## What an "agent" is, and isn't

The word *agent* in 2026 is doing four different jobs in four different conversations:

1. **Agent as one LLM call.** "I built an agent that summarizes emails." (It is a function with a prompt.)
2. **Agent as an LLM with tools and a loop.** "My agent searches the web and writes a report." (This is closer to the Yao et al. *ReAct* definition — reasoning and acting interleaved.)
3. **Agent as a long-running autonomous system.** "Devin is an agent that closes Jira tickets while you sleep." (Autonomous, plans its own work, reports back.)
4. **Agent as a specialized role in a workflow.** "The Intelligence Agent gathers and scores news." (A named module in a larger system, not autonomous, not a single LLM call — a job with a defined input and output.)

Madison uses meaning #4. The framework's five-layer architecture is *not* a collection of autonomous AI assistants. It is a coordinated pipeline of specialized roles, each one tuned for a particular kind of marketing work, orchestrated through n8n workflows with human approval points where the work matters most.

Understanding this matters because the difference between meanings #3 and #4 is the difference between two very different products with two very different brand experiences. We will return to this distinction in the deep-dive. For now, hold onto the specification: in Madison, *agent* means *role-in-pipeline*, not *autonomous problem-solver*.

The five Madison layers:

- **Intelligence Agents** — gather and analyze data. Reputation monitoring, sentiment analysis, trend detection. The example I opened with is one of these.
- **Content Agents** — create, optimize, distribute marketing materials. Brand voice, multi-platform adaptation, headline variants.
- **Research Agents** — process data to uncover customer insight. Survey analysis, persona development.
- **Experience Agents** — enhance customer interactions. Concierge systems, journey transformation.
- **Performance Agents** — measure and optimize outcomes. Multi-armed bandits, predictive analytics.

Plus one more thing that is not a layer but is critical to the architecture:

- **The orchestration layer** — coordinates across agents. Cross-project validation, dynamic resource allocation, continuous learning.

If you are squinting at this list and thinking "that just looks like five marketing departments connected by a router," you have understood the architecture correctly. That's the point. Madison takes the way marketing organizations divide labor — research, content, intelligence, customer, performance — and makes the boundaries machine-readable.

The hard work of Madison is not in any one agent. It is in deciding *where the boundaries go* and *what gets handed across them*. That is also the hard work of designing your own AI tool.

---

## Reading the architecture — and why it is also brand strategy

Let me walk through one specific architectural choice in Madison and trace it all the way out to the user experience and the brand.

The choice: **five layers, not one mega-agent.**

A mega-agent design would be: one large model with a long prompt and access to every data source. The user types a marketing question and the model answers. This works on demos and falls over in production. The reasons are mechanical and worth tracing.

If a single model is responsible for ingesting 870 articles a day, deduplicating them, scoring sentiment, drafting content variants, running multi-armed bandit experiments, and delivering insights to a customer, three things happen:

1. **Token costs get unsustainable.** You are paying for the model to re-read the same context every operation. By the end of a workday, the same news article has been embedded in twenty different prompts.
2. **Failure modes blur.** When the marketing director gets a wrong answer, you cannot tell whether the model misread the news (Intelligence layer fault), built a bad persona (Research layer fault), or wrote a misaligned headline (Content layer fault). The system is uninspectable.
3. **The product has no surfaces.** From the customer's perspective, "Madison" is one black box. There is nothing to name, version, sell separately, swap out, or improve in isolation.

Now compare a layered design. Each layer is a specialized agent (or set of agents) with a defined input and output. The Intelligence Agent's job is to deliver scored news to the orchestrator. The Content Agent's job is to take a brief and return three headline variants. The Performance Agent's job is to run experiments on which variant lands. Each one can be tested, versioned, swapped, and *named*.

The naming part is brand strategy in a costume.

Look at what naming the layers does. A customer reading Madison's documentation does not see "an AI marketing tool." They see Intelligence, Content, Research, Experience, Performance. Each is a thing they can talk about with their team. Each is a feature their CFO can put a price tag on. Each is a comparison axis against a competitor. The architecture has produced a product surface that the brand can attach to.

This is what I mean when I say architecture is brand-relevant. The five-layer choice was an engineering decision (token costs, failure isolation, modular development). It was *also* a brand decision. It made Madison sellable, comparable, and explainable in language a non-engineer can use.

### A worked case: Cursor and Devin

Two AI coding products. Same underlying capability — both rely on frontier LLMs from major labs. Same target user — software engineers. Different architectures, very different brands.

[Cursor](https://cursor.com/) is a fork of Visual Studio Code with AI features built into the IDE. The architectural commitment is "augment the developer." Cursor keeps the developer in the driver's seat: real-time completions, inline chat, multi-file agent mode, but always with the developer reviewing each change. The product surface is the editor.

[Devin](https://devinai.ai/) — built by Cognition Labs — runs in a sandboxed cloud environment with its own IDE, browser, and shell. Devin 2.0 introduced what Cognition calls an "agent-native IDE experience" — multiple parallel Devin instances, each in an isolated VM, working through tasks autonomously. The architectural commitment is "replace the junior engineer for well-specified work."

Same technology stack underneath. Wildly different architectures. And consequently, wildly different brand experiences. Cursor's brand is "AI for engineers who want to be better engineers." Devin's brand is "AI engineers you assign work to." A senior developer comparing the two is not comparing capabilities — they are comparing models of how AI should fit into their workflow. The architecture *is* the brand position.

Madison's five-layer choice does the same kind of work. It says: *we are not a black-box marketing AI; we are five legible agents you can reason about, swap, and price independently.* That is a brand position even before any logo or color palette is decided.

---

## ReAct, agent loops, and what each layer is actually doing

Let me show you, mechanically, what is happening inside one Madison layer when it runs. The pattern comes from one of the most-cited papers in agent research: [Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models,"](https://arxiv.org/abs/2210.03629) ICLR 2023.

ReAct's core insight is that an LLM doing useful work in the world needs to interleave two things: *reasoning* (thinking about what to do next) and *acting* (calling a tool, querying an API, modifying state). Traditional chain-of-thought prompting is all reasoning, no acting — the model talks to itself but cannot reach into the world. Pure tool-use without reasoning is reactive — the model calls APIs without a coherent plan.

ReAct interleaves them. The model produces a reasoning trace ("I should search for recent earnings reports for this company"), takes an action ("search for 'Acme Corp Q3 2026 earnings'"), observes the result, updates its reasoning trace ("the earnings missed expectations; now I should check stock-price reaction"), takes another action, and so on. Yao et al. show this beats chain-of-thought on question answering and beats imitation learning on interactive decision-making — by 34 percentage points on the ALFWorld benchmark.

Madison's Intelligence Agent is, mechanically, a ReAct loop wrapped in n8n orchestration:

```
Reasoning: "It is 7am. Time to pull the daily news cycle for Brand X."
Action:    Pull RSS feeds, Google News API, Reddit threads.
Observation: 870 articles received.
Reasoning: "Deduplicate before scoring to save tokens."
Action:    Run MD5 hash + Levenshtein on titles.
Observation: 87 unique articles remaining.
Reasoning: "Score each one for sentiment and topic relevance."
Action:    Send each to GPT-4o-mini with sentiment prompt.
Observation: Scored set returned.
Reasoning: "Write to storage and trigger dashboard refresh."
Action:    Append to Google Sheet, fire Plotly dashboard webhook.
Observation: Dashboard updated. Job complete.
```

Each layer in Madison runs a loop like this with its own tools, its own reasoning prompts, and its own outputs. The orchestration layer (n8n in Madison's reference implementation) connects the loops — the Intelligence Agent's output becomes the Research Agent's input becomes the Content Agent's input.

This is not the only multi-agent design. The two most-cited alternatives in 2024-2025 are [LangGraph](https://blog.langchain.com/langgraph-multi-agent-workflows/) — agents-as-nodes-in-a-graph — and [Microsoft AutoGen](https://arxiv.org/abs/2308.08155) — agents-as-conversation-participants. Both are real, both are documented, and the field is converging toward graph-based orchestration as the dominant pattern. Madison's n8n-based orchestration is itself effectively a graph: nodes are operations, edges are data flows, and the workflow is the graph traversal.

The trade-off Madison makes is worth naming. Conversation-based orchestration (AutoGen) is more flexible — agents can talk to each other freely, work things out emergently. Graph-based orchestration (LangGraph, n8n) is more predictable — every step is defined in advance, every edge is testable, every failure mode is locatable. Madison chose predictability. That choice trades exploration for production reliability. For a marketing intelligence framework that needs to run at 7am every day and write to the same Google Sheet without crashing, predictability is the right trade. For a research assistant exploring a novel scientific question, conversation might be better.

You will be making this trade-off too. And it will, again, show up in your brand. A predictable, orchestrated tool feels professional and trustable; an emergent, conversational tool feels exciting and novel. Your archetype shapes which feeling you want to deliver.

---

## How to read Madison for your own design

Madison is a reference architecture. Reading it well teaches you what to do. Copying it produces a worse Madison. The work you have to do over the next four chapters is to read Madison, identify the patterns that fit your tool's purpose, and adapt them — not paste them.

Three reading moves to practice now, before Chapter 4 asks you to write a PRD:

**1. Read the README before reading the code.** The Madison repo's [README](https://github.com/humanitariansai/madison) names the five-layer architecture, the orchestration choice, and the technology stack. You need that mental model before any line of code makes sense. Same rule will apply when you read the Intelligence Agent's submodule README, and the Content Agent's workflow JSON. If a system has a README, the README is usually doing the work that lets the rest of the system make sense. Honor it.

**2. Find one layer and trace it end to end.** Pick the Intelligence Agent. Read the README. Open `n8n_workflow.json` and look at the node graph. Read `sentiment_analysis.py` and find where the GPT call happens. You will not understand every detail. That is fine. What you are looking for is the *shape* of the pipeline — ingestion, orchestration, analysis, storage, visualization. Once you can see that shape in Madison, you will see it everywhere.

**3. Pick the layer that matches your archetype.** The archetype you identified in Chapter 1 should select your starting layer. A *Sage* archetype probably gravitates to Intelligence (knowledge gathering, analysis, insight). A *Creator* archetype might pick Content (generating, iterating, distributing). A *Caregiver* archetype probably reaches for Experience (concierge systems, customer journeys). The archetype is doing real work here — it forces specification of *which problem you actually want to solve*. The chapter's deep-dive showed that legible architecture creates brand surfaces; your archetype tells you which surface is yours.

Then in Chapter 4 you will write a Product Requirements Document for a tool that takes a Madison pattern and applies it to a problem of your choosing. The deeper you read Madison now, the better that PRD will be.

---

## What you should walk out of this chapter with

A working definition of "agent" that is not magical. A reading of Madison that respects its architecture as both engineering and brand work. The ReAct loop in your head as the small machine that lives inside every Madison layer. A picked starting layer that fits your archetype.

I am betting on the shape of this kind of architecture as the dominant pattern for the next several years, but the bet is not without doubts. Conversation-based and emergent multi-agent systems may eventually outperform orchestrated graph systems on the kinds of complex, exploratory tasks where Madison's predictability becomes a constraint. There are research signals — agentic systems with self-modification, swarm-based architectures — that suggest the field is not done evolving. If those approaches mature into production reliability, the right reference architecture in 2030 may not look like Madison.

For 2026, though, Madison is the cleanest reference architecture I have found that you can read end to end without a research-lab budget. That is the reason it is in this book.

---

**What would change my mind:** A production deployment study showing that emergent multi-agent systems (AutoGen-style conversation, swarm architectures) outperform graph-orchestrated systems (LangGraph, n8n) on production reliability metrics — not on capability benchmarks but on uptime, debuggability, and time-to-recovery from incidents. The current evidence suggests graph orchestration is winning the production fight. That could change.

**Still puzzling:** The exact boundary between "agent as role" and "agent as autonomous system." Devin claims autonomy; in practice it operates within a sandboxed environment with humans approving most pull requests. Madison claims orchestrated roles; in practice the LLM inside each layer is making local decisions that look agentic. The terminology has not stabilized, and I suspect the categories I used in this chapter will be replaced by something cleaner within two years.

---

**Tags:** madison-framework · multi-agent-systems · ReAct · n8n · architecture-as-brand · cursor · devin · agent-loop · INFO-7375
