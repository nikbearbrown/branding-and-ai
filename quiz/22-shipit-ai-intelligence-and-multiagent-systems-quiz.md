# Chapter Quiz: AI Intelligence and Multi-Agent Systems

*Chapter 22 (Appendix S3) of Branding and AI: Building the Creative Engineer*

> **Instructions:** Attempt every question before checking the answer key.
> Do not look at the answers while working — the act of retrieval is the
> learning. If you are unsure, make your best attempt and mark it with (?).
> Review the answer key after completing all questions, not after each one.

---

## Learning Objectives Covered

This quiz assesses the following chapter objectives:

- Classify an AI system by pattern (single call, chained calls, tool-using agent, multi-agent) and identify its failure mode
- Explain why the choice between autonomous and orchestrated architecture is a brand decision as much as a technical one
- Identify the three failure modes of autonomous agents (compounding error, cost runaway, trust collapse) and their mechanisms
- Read an agent specification (role, goal, backstory, tools, allow_delegation) and explain what each component does
- Select an anti-hallucination pattern and justify the choice for a specific use case

---

## Section 1 — Recall and Recognition (Questions 1–5)

*Target: Bloom's Remember / Understand*
*Format: Multiple-choice (3 options) and True/False*
*Target difficulty: p = 0.77–0.85*

---

**Question 1** *(Multiple-Choice)*

The chapter describes four patterns of AI intelligence in a workflow. Which answer correctly names all four and the key distinguishing feature of each?

A) Rule-based, learned, generative, and adaptive — distinguished by whether the system uses explicit rules, training data, generation, or feedback.
B) Single LLM call (one prompt, one response, deterministic flow), chained calls (output of one call becomes input to the next), tool-using agent / ReAct (LLM controls the next step via tool calls), and multi-agent system (multiple specialized agents coordinated by an orchestrator or shared state).
C) Supervised, unsupervised, reinforcement, and transformer — the four machine learning paradigms underlying modern AI systems.

---

**Question 2** *(True/False)*

The chapter classifies Madison's five-layer architecture (Intelligence, Content, Research, Experience, Performance) as an autonomous multi-agent system, because each layer operates independently without orchestration.

☐ True  ☐ False

---

**Question 3** *(Multiple-Choice)*

The chapter explains that `allow_delegation=False` in the Madison `competitor_analyst` agent specification is not cosmetic. What does this parameter specifically control, and why does it matter architecturally?

A) It controls whether the agent's output is displayed to the user — setting it to False means outputs are kept internal to the pipeline.
B) It prevents the agent from handing off to other agents, keeping the orchestration decision with the workflow layer rather than with the agent itself — this is the architectural commitment that separates Madison's orchestrated approach from AutoGPT's autonomous approach, and it ensures failures remain local to one agent rather than propagating through sub-agent chains.
C) It prevents the agent from using delegation patterns in its code generation, ensuring the output follows functional programming principles.

---

**Question 4** *(Multiple-Choice)*

The chapter names three failure modes specific to autonomous agents (Pattern 3 and autonomous Pattern 4). Which answer correctly names all three with their mechanisms?

A) Overfitting (agent trains on user feedback), hallucination (agent generates false information), and timeout (agent exceeds compute limits).
B) Compounding error (step N-1 error conditions step N on a false foundation, with the probability of an error-free chain decreasing geometrically), cost runaway (each step calls a model; without a hard step ceiling and cost ceiling, the agent can make arbitrarily many calls), and trust collapse on visible failure (watching a live failure damages long-term trust more severely than opaque failure).
C) Context overflow (agent loses track of earlier steps), prompt injection (adversarial inputs redirect the agent), and rate limiting (APIs throttle autonomous agents that call too frequently).

---

**Question 5** *(True/False)*

The chapter recommends Pattern 1 (single LLM call) as universally sufficient for student AI tool projects, because it is the most predictable pattern and the reliability trade-off of more complex patterns is not justified for course-level projects.

☐ True  ☐ False

---

## Section 2 — Application and Analysis (Questions 6–9)

*Target: Bloom's Apply / Analyze*
*Format: Multiple-choice (3 options) and Short-Answer*
*Target difficulty: p = 0.50–0.70*

---

**Question 6** *(Scenario-Based Multiple-Choice)*

A student building an AI research tool for a Sage-archetype brand has written the following agent goal: "Research this topic thoroughly and provide a complete and comprehensive answer." The student is applying the chapter's anti-hallucination discipline. What is wrong with this goal and how should it be revised?

A) The goal is too short — it needs at least three to five sentences to give the LLM sufficient context to perform well.
B) The goal implicitly rewards completeness, which is the opposite of the anti-hallucination discipline. A Sage tool must guard against its shadow (dogmatism — confident wrong answers). The goal should add: an explicit permission to abstain ("if you cannot verify a claim with search results, say 'I cannot verify this'"), a structured output schema with null fields for unverifiable data, and a constraint against inferring from general knowledge when search results are empty.
C) The goal is acceptable as written, but should be supplemented with a safety filter that blocks the agent from discussing sensitive topics.

---

**Question 7** *(Short-Answer)*

The chapter uses the contrast between Architecture A (autonomous, transparent reasoning trace) and Architecture B (orchestrated, structured brief with a finished report) to illustrate that the architecture choice is a brand decision. Explain the brand experience each architecture creates and under what conditions each is more appropriate.

*Your answer:*

_____________________

---

**Question 8** *(Multiple-Choice)*

The chapter describes three anti-hallucination patterns for agent goals, from weakest to strongest. What are they, and which does the chapter recommend as a starting point?

A) Confidence scoring (weakest), output verification (middle), human review (strongest) — human review is recommended as the starting point.
B) Permission to abstain (weakest), structured output with null fields (middle), and confidence labeling (strongest) — the chapter recommends structured output with null fields (Pattern 2) as the right starting point for most projects.
C) Prompt hedging (weakest), temperature reduction (middle), and model switching (strongest) — temperature reduction is recommended as the starting point.

---

**Question 9** *(Short-Answer)*

The chapter states that in the Madison `competitor_analyst` agent, the `goal` "contains a discipline, not just a task." Using the exact agent specification from the chapter, explain what discipline the goal encodes and how it prevents a specific failure mode of the Sage archetype.

*Your answer:*

_____________________

---

## Section 3 — Synthesis and Evaluation (Questions 10–11)

*Target: Bloom's Evaluate / Create*
*Format: Short-Answer or Brief-Response*
*Target difficulty: p = 0.30–0.50*

---

**Question 10** *(Brief-Response)*

The chapter argues that the failure modes of autonomous agents (compounding error, cost runaway, trust collapse) are mitigated in orchestrated systems at the cost of rigidity and specification work. It also acknowledges that "the autonomous-agent quadrant is improving." Evaluate whether the chapter's current architectural preference for orchestrated systems is a durable principle or a contingent recommendation. What would need to change in autonomous agent capabilities for the recommendation to reverse, and does the chapter's "deeper principle" survive even if the recommendation reverses?

*Your response (2–4 sentences):*

_____________________

---

**Question 11** *(Transfer — Brief-Response)*

The chapter argues that each AI pattern's failure mode must be "chosen on purpose" by an informed architect — there is no architecture that wins on every dimension. Apply this principle to the design of an automated essay-grading system for a university. The system must score student essays and provide feedback. Identify two different AI-intelligence patterns that could be used, describe the trade-off each produces for the grading use case, and explain which one the architecture-as-brand-decision argument would favor for a university that values transparency and student trust.

*Your response (2–4 sentences):*

_____________________

---

## Answer Key

> Read this section only after completing all questions.

---

**Q1 — B**
*Correct because:* The chapter names exactly these four patterns: single LLM call (prompt in, response out, deterministic flow, most predictable), chained calls (sequential LLM calls where each output feeds the next input, overall sequence is deterministic but each step introduces non-determinism), tool-using agent / ReAct (LLM reasons, calls tools, observes results, loops — LLM controls the next step), and multi-agent system (multiple specialized agents with an orchestrator deciding which runs when).
*Why the distractors are wrong:*
- A) Rule-based, learned, generative, and adaptive are not the chapter's four patterns — they are general ML paradigm categories.
- C) Supervised, unsupervised, reinforcement, and transformer are ML training paradigms, not the chapter's agentic architecture patterns.
*Chapter reference:* Four Patterns of AI Intelligence

---

**Q2 — False**
*Correct because:* The chapter explicitly states: "Madison lives firmly in the orchestrated quadrant." The five layers are specialized agents; the n8n orchestration layer decides which runs when. The chapter contrasts this with autonomous agents (high autonomy, low orchestrator control) and places Madison in the orchestrated quadrant (low autonomy per agent, high orchestrator control).
*Chapter reference:* Four Patterns / autonomy-orchestration grid / Madison marked in orchestrated quadrant

---

**Q3 — B**
*Correct because:* The chapter explains: "`allow_delegation=False` is the orchestration commitment in code. This agent cannot hand off to other agents. It does its job and returns. The orchestration layer — not the agent — decides what happens next. This single parameter is the architectural choice that separates Madison's approach from AutoGPT's." When this architecture fails, it fails locally — one agent's output is wrong, traceable to a specific node. AutoGPT agents could spawn sub-agents, leading to distributed, difficult-to-debug failure.
*Why the distractors are wrong:*
- A) `allow_delegation` does not control display of output to users; it controls agent-to-agent delegation.
- C) Delegation in the CrewAI sense refers to agent task delegation, not programming paradigms.
*Chapter reference:* The Madison Agents as a Worked Case / `allow_delegation=False`

---

**Q4 — B**
*Correct because:* The chapter names and explains all three: compounding error (step N is conditioned on step N-1; a 10% error rate per step leaves only ~35% probability of error-free output after 10 steps, ~1.5% after 40 steps — a geometric decay); cost runaway (each step calls a model at a cost; without step ceiling, cost ceiling, and circuit breaker for repeated identical tool calls, the agent can spend indefinitely); trust collapse on visible failure (watching a live failure in real time is more damaging to long-term trust than opaque failure, particularly when the user has been told to trust the system).
*Why the distractors are wrong:*
- A) Overfitting, hallucination, and timeout are related concepts but are not the chapter's three named autonomous-agent failure modes with their mechanisms.
- C) Context overflow, prompt injection, and rate limiting are real risks but are not the chapter's three named failure modes for autonomous agents.
*Chapter reference:* What Goes Wrong in the Autonomous Quadrant

---

**Q5 — False**
*Correct because:* The chapter states: "Pick the simpler pattern first and add complexity only when you hit its ceiling." It does not recommend Pattern 1 as universally sufficient — it recommends using the appropriate pattern for the task. The chapter explicitly describes when to move to Patterns 2, 3, and 4: when the task requires sequential sub-tasks (Pattern 2), adaptive reasoning with tool calls (Pattern 3), or multiple specializations that need to be independently debuggable (Pattern 4).
*Chapter reference:* Building the AI Layer / pick the simpler pattern first

---

**Q6 — B**
*Correct because:* The chapter explains that "most prompts implicitly reward completeness" — a goal that says "complete and comprehensive" tells the LLM to fill gaps with inference rather than acknowledge limitations. The Sage shadow is dogmatism — wrong answers delivered with high confidence. The chapter's anti-hallucination discipline requires: permission to abstain, structured output with null fields for unverifiable items, and constraints against inferring from general knowledge when search results are empty.
*Why the distractors are wrong:*
- A) Length is not the issue; the problem is the goal's implicit reward structure, not its brevity.
- C) Safety filters for sensitive topics are not the chapter's anti-hallucination discipline — the issue is the goal's reward of completeness over honesty.
*Chapter reference:* Writing Agent Specifications / anti-hallucination patterns / Sage archetype shadow

---

**Q7 — Short-Answer**
*Model answer:* Architecture A (autonomous, visible reasoning trace) creates a brand experience of transparency — the user watches the agent work, which feels collaborative and alive when it succeeds. The failure mode is equally visible: the user watches the system loop, fail, or produce wrong reasoning, and that visible failure is maximally damaging to trust. Architecture B (orchestrated, structured brief, finished report) creates a brand experience of competence — the user submits a structured brief and receives a deliverable, which feels professional and frictionless. The failure mode is opaque: a missing or wrong report, with no visible path to understanding why. Architecture A is appropriate for tools where the user wants to direct the exploration and observe the process (research collaboration, creative exploration). Architecture B is appropriate for tools where the user wants a deliverable, not a process (enterprise reporting, automated intelligence summaries). The chapter connects this to archetype: a Sage brand that promises trustworthy authoritative output should prefer Architecture B, with guards preventing the Sage's shadow (confident wrong answers); a Creator brand exploring originality might benefit from Architecture A if the user wants to direct the AI's process.
*What a strong answer includes:*
- The brand experience each architecture creates (transparency vs. competence)
- The failure mode each produces and why it differs in trust impact
- The conditions under which each is more appropriate
*Chapter reference:* Why Architecture Is the Brand Decision / Architecture A vs. B

---

**Q8 — B**
*Correct because:* The chapter names three patterns in order from weakest to strongest: Pattern 1 (permission to abstain — add to the goal "say 'I cannot verify this' rather than guessing"), Pattern 2 (structured output with null fields — require JSON with fields set to null for unverifiable items), and Pattern 3 (confidence labeling — each claim labeled verified, inferred, or unverifiable). The chapter explicitly recommends: "For most projects, Pattern 2 is the right starting point."
*Why the distractors are wrong:*
- A) Human review is not one of the chapter's three patterns; it is a downstream governance practice, not an agent specification technique.
- C) Prompt hedging, temperature reduction, and model switching are not the chapter's three named anti-hallucination patterns.
*Chapter reference:* Writing Agent Specifications / anti-hallucination patterns / Pattern 2 recommended

---

**Q9 — Short-Answer**
*Model answer:* The `competitor_analyst` goal in the chapter reads: "Find and summarize competitor info cautiously. Return structured JSON. If you cannot verify a data point, set it null and explain limitations." The discipline in this goal is the anti-hallucination instruction: "If you cannot verify a data point, set it null and explain limitations." This encodes the chapter's anti-hallucination Pattern 2 (structured null fields) directly into the task specification. It prevents the Sage archetype's shadow — dogmatism, meaning overconfident wrong answers — by building the constraint into the agent's output structure before generation rather than relying on post-hoc validation. An agent without this instruction would default to completing the JSON fields with inferred or fabricated data, because the base reward from most prompts is completeness. The "set it null" instruction explicitly overrides that default.
*What a strong answer includes:*
- The exact discipline in the goal ("set it null and explain limitations")
- The anti-hallucination Pattern 2 connection
- The Sage shadow (dogmatism) that this discipline addresses
- Why placing the constraint in the goal is more reliable than post-hoc validation
*Chapter reference:* The Madison Agents as a Worked Case / `competitor_analyst` annotation

---

**Q10 — Brief-Response**
*Model answer:* The preference for orchestrated systems is a contingent recommendation, not a durable principle — the chapter says so explicitly, noting that if autonomous agents achieve parity on production-reliability metrics (uptime, cost predictability, mean time to recovery) by 2027 or 2028, the recommendation changes. What would need to change is: per-step error rates would need to come down significantly (so compounding error no longer decays to near-zero at 40 steps), cost controls would need to be default rather than requiring manual configuration, and self-correction would need to be reliable enough to make visible failure rare. The chapter's "deeper principle," however, is explicitly stated as durable: "the choice between autonomy and orchestration is a brand decision" — it encodes a theory of what the user should trust and what kind of failure the brand is willing to absorb, regardless of whether autonomous agents improve. That principle survives even if the technical recommendation reverses, because the brand-alignment question remains whether the chosen architecture expresses the archetype or the archetype's shadow.
*What a strong answer includes:*
- The contingent nature of the technical recommendation
- Specific conditions under which it would reverse (per-step error rates, cost controls, self-correction)
- The durable deeper principle (architecture as brand decision) and why it survives
*Chapter reference:* A Note on What Is Changing / deeper principle / What Would Change My Mind

---

**Q11 — Transfer Brief-Response**
*Model answer:* Two applicable patterns: Pattern 1 (single LLM call) would have the system score each essay in one prompt, returning a score and feedback — highly predictable, cost-bounded, but constrained to what can be specified in a single prompt and unable to handle multi-stage rubric evaluation adaptively. Pattern 2 (chained calls) would use sequential steps: rubric extraction, argument identification, evidence evaluation, and feedback synthesis, each as a separate LLM call — more capable of complex evaluation but with error propagation risk (a mis-classified argument structure in step 2 affects all downstream steps). For a university that values transparency and student trust, the architecture-as-brand-decision argument favors Pattern 2 with visible intermediate steps that can be shown to students ("here is how the system identified your thesis, here is how it evaluated your evidence") — this creates a trust-building experience of competent, explainable judgment rather than opaque scoring, and it is independently debuggable when a student disputes a grade, allowing the instructor to trace exactly which step produced a given score.
*What a strong answer includes:*
- Two patterns identified with their trade-offs for the grading context
- Application of the architecture-as-brand-decision argument to transparency/trust
- A specific connection between architectural choice and user-facing experience
*Chapter reference:* Four Patterns / Architecture as Brand Decision / Why Architecture Is the Brand Decision (transfer application)

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

- Treating all multi-agent systems as equally autonomous — students miss the distinction between autonomous multi-agent, orchestrated multi-agent, and conversational multi-agent systems.
- Believing that anti-hallucination requires model switching or temperature tuning, rather than goal specification changes.
- Missing the compound-error mechanism — students understand that errors occur but do not grasp the geometric decay of error-free probability across many steps.

**Signs a student needs to return to the chapter before this quiz:**

- Cannot explain what `allow_delegation=False` means architecturally and why it matters for failure localization.
- Does not understand why a goal that rewards completeness produces hallucination.

**Scaffolding adjustments:**

- *For students who score below 5:* Start with the four patterns as a classification exercise — classify five real AI products into the four patterns before engaging the failure modes or agent specifications.
- *For students who score 11/11 on first attempt:* Ask them to write a complete agent specification for a core agent in their own tool, including anti-hallucination guards appropriate for their archetype's shadow, and run it against three test inputs (easy, medium, adversarial) with documentation of what happened.
