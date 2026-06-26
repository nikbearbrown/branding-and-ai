# Chapter Quiz: The AI Toolchain — Cowork, Codex, and Madison

*Chapter 3 of Branding and AI: Building the Creative Engineer*

> **Instructions:** Attempt every question before checking the answer key.
> Do not look at the answers while working — the act of retrieval is the
> learning. If you are unsure, make your best attempt and mark it with (?).
> Review the answer key after completing all questions, not after each one.

---

## Learning Objectives Covered

This quiz assesses the following chapter objectives:

- Distinguish the four meanings of the word "agent" as used in AI tooling contexts
- Describe the five Madison roles and the function of orchestration
- Explain the ReAct loop (Thought / Action / Observation) and its three failure modes
- Contrast graph-based and conversation-based multi-agent orchestration approaches
- Articulate why architecture choices are brand decisions, not purely technical ones

---

## Section 1 — Recall and Recognition (Questions 1–5)

*Target: Bloom's Remember / Understand*
*Format: Multiple-choice (3 options) and True/False*
*Target difficulty: p = 0.77–0.85*

---

**Question 1** *(Multiple-Choice)*

In the ReAct loop, what is the correct sequence of steps?

A) Action → Thought → Observation
B) Thought → Action → Observation
C) Observation → Thought → Action

---

**Question 2** *(Multiple-Choice)*

The Madison framework divides AI work into five specialized roles. Which set correctly names all five?

A) Intelligence, Content, Research, Experience, and Performance
B) Analyst, Writer, Researcher, Designer, and Optimizer
C) Planner, Executor, Validator, Publisher, and Monitor

---

**Question 3** *(True/False)*

The chapter argues that a mega-agent architecture — one general-purpose agent performing all tasks — is superior to a multi-role architecture like Madison because it requires less upfront configuration.

☐ True  ☐ False

---

**Question 4** *(Multiple-Choice)*

What distinguishes Cursor from Devin, as the chapter uses these products to illustrate a key architectural choice?

A) Cursor is a cloud product; Devin is installed locally.
B) Cursor augments the developer by suggesting code within a tight feedback loop; Devin automates longer tasks by acting more autonomously with a looser control loop.
C) Cursor uses GPT-4; Devin uses Claude — the distinction is about model choice, not architecture.

---

**Question 5** *(True/False)*

Graph-based orchestration tools like n8n and LangGraph control agent flow through a visual workflow graph, while conversation-based tools like AutoGen have agents coordinate by messaging each other.

☐ True  ☐ False

---

## Section 2 — Application and Analysis (Questions 6–9)

*Target: Bloom's Apply / Analyze*
*Format: Multiple-choice (3 options) and Short-Answer*
*Target difficulty: p = 0.50–0.70*

---

**Question 6** *(Scenario-Based Multiple-Choice)*

A student builds a marketing intelligence agent that successfully retrieves competitor news articles but consistently summarizes them inaccurately, missing the key claims. The ReAct loop completes without an error signal. Which ReAct failure mode does this represent, and what is its mechanism?

A) A reasoning failure — the agent's Thought step draws a wrong inference from accurate information before acting.
B) An observation failure — the agent retrieves accurate content but misinterprets or incompletely processes what it reads in the Observation step.
C) An action failure — the agent calls the wrong tool or calls the correct tool incorrectly, so the retrieved content is already corrupted.

---

**Question 7** *(Short-Answer)*

The chapter argues that the choice between a five-role architecture (like Madison) and a single mega-agent is a brand decision, not just a technical one. Explain what this means in two or three sentences, using specific concepts from the chapter.

*Your answer:*

_____________________

---

**Question 8** *(Multiple-Choice)*

A team is building an AI pipeline where the flow of tasks must be predictable, auditable, and reproducible — the same inputs should produce the same execution path every time. Which orchestration approach does the chapter recommend for this requirement, and why?

A) Conversation-based orchestration (AutoGen), because agents can negotiate the best path dynamically on each run.
B) Graph-based orchestration (n8n or LangGraph), because the workflow graph determines which agent runs when — execution is deterministic rather than emergent.
C) A single ReAct agent, because it eliminates coordination overhead between multiple agents.

---

**Question 9** *(Short-Answer)*

Name and briefly describe the three failure modes of the ReAct loop as defined in the chapter.

*Your answer:*

_____________________

---

## Section 3 — Synthesis and Evaluation (Questions 10–11)

*Target: Bloom's Evaluate / Create*
*Format: Short-Answer or Brief-Response*
*Target difficulty: p = 0.30–0.50*

---

**Question 10** *(Brief-Response)*

The chapter states that "architecture is a brand decision." A classmate responds: "That's marketing speak — a well-designed system is a well-designed system. The architecture should be driven by technical requirements, not brand positioning." Using specific arguments from the chapter, evaluate this claim. Is the classmate correct, partially correct, or incorrect?

*Your response (2–4 sentences):*

_____________________

---

**Question 11** *(Transfer — Brief-Response)*

The Madison framework's five-role split is designed for marketing intelligence tasks. Apply the same architectural logic — dividing work into specialized roles rather than using one general agent — to a different domain (for example, legal research, academic writing assistance, or software debugging). Name at least three specialized roles you would create, explain what each does, and identify what the "orchestration" layer would need to decide.

*Your response (2–4 sentences):*

_____________________

---

## Answer Key

> Read this section only after completing all questions.

---

**Q1 — B**
*Correct because:* The ReAct loop is Thought (the agent reasons about what to do) → Action (the agent calls a tool or takes a step) → Observation (the agent reads the result) — and then loops back to Thought. The sequence is named in the chapter and its order is essential: reasoning precedes action, and action precedes observation.
*Why the distractors are wrong:*
- A) Starting with Action would mean acting without reasoning — a description of autonomous but unguided behavior.
- C) Starting with Observation before Thought or Action describes a reactive system that reads without first planning.
*Chapter reference:* ReAct loop (Thought / Action / Observation)

---

**Q2 — A**
*Correct because:* The chapter names the five Madison roles explicitly: Intelligence (gathers and scores information), Content (writes and edits), Research (performs deep research tasks), Experience (handles user-facing interaction), and Performance (tracks and optimizes metrics). These five plus an orchestration layer constitute the full Madison framework.
*Why the distractors are wrong:*
- B) These are generic role labels not used in the chapter's framework.
- C) Planner/Executor/Validator/Publisher/Monitor is not the Madison taxonomy.
*Chapter reference:* Madison five specialized roles

---

**Q3 — False**
*Correct because:* The chapter argues against the mega-agent approach: specialized roles are easier to debug, improve, and align with specific tasks. A mega-agent performing all tasks concentrates failure and makes it harder to locate which part of the system produced a bad output. Lower configuration cost does not compensate for these reliability and debuggability costs.
*Chapter reference:* Five roles vs. mega-agent

---

**Q4 — B**
*Correct because:* The chapter uses Cursor and Devin to contrast augmentation (tight, developer-in-the-loop feedback cycle) with automation (longer autonomous task execution with less frequent human check-in). This is an architectural and product philosophy distinction, not a model or hosting distinction.
*Why the distractors are wrong:*
- A) Cloud vs. local is not the chapter's distinction between these tools.
- C) The chapter's distinction is about the control loop and autonomy architecture, not the specific model used.
*Chapter reference:* Cursor vs. Devin / augment vs. automate

---

**Q5 — True**
*Correct because:* The chapter explicitly contrasts these two orchestration styles: n8n and LangGraph use visual workflow graphs where the developer defines which agent runs when; AutoGen uses a conversational model where agents coordinate by sending messages to each other, producing emergent rather than predetermined flow.
*Chapter reference:* Graph-based vs. conversation-based orchestration

---

**Q6 — B**
*Correct because:* The scenario describes correct tool use and correct retrieval but inaccurate processing of what was retrieved — the agent misread or misinterpreted the content during the Observation step. An observation failure means the agent reads results but draws wrong conclusions from what it observed, not that the action or reasoning was wrong.
*Why the distractors are wrong:*
- A) A reasoning failure would mean the Thought step drew a wrong conclusion before acting — the scenario specifies the articles are retrieved accurately, so reasoning about what to retrieve was correct.
- C) An action failure would mean the tool call itself was wrong (wrong tool, wrong query) — the scenario specifies articles are retrieved successfully.
*Chapter reference:* ReAct failure modes / observation failure

---

**Q7 — Short-Answer**
*Model answer:* Architecture determines what experience users have when something goes wrong: a five-role system fails locally (one agent's output is wrong; the others continue) and is debuggable, while a mega-agent fails globally and opaquely. This affects what the brand promises — a brand that promises reliable, inspectable intelligence cannot deliver that promise with an architecture that fails unpredictably. The chapter's point is that architecture choices encode trust commitments, which are brand commitments.
*Common error:* Treating "brand decision" as purely visual or communicative, missing that the chapter means it in terms of what the product's behavior promises to users.
*Chapter reference:* Architecture as brand decision

---

**Q8 — B**
*Correct because:* Graph-based orchestration (n8n, LangGraph) is explicitly recommended for predictable, auditable workflows because the graph structure means the same inputs follow the same execution path. The chapter contrasts this with conversation-based orchestration, where the path emerges from agent negotiation and is less reproducible.
*Why the distractors are wrong:*
- A) Conversation-based orchestration produces emergent paths — the opposite of what predictability requires.
- C) A single ReAct agent is not multi-agent orchestration; the chapter's comparison is between orchestration styles, and a single agent does not address the coordination problem.
*Chapter reference:* Graph-based vs. conversation-based orchestration / n8n / LangGraph

---

**Q9 — Short-Answer**
*Model answer:* (1) Reasoning failure: the Thought step draws a wrong conclusion from correct information, sending the loop in the wrong direction before any action is taken. (2) Action failure: the agent calls the wrong tool or calls the right tool incorrectly, so the action step itself is flawed even if reasoning was sound. (3) Observation failure: the agent retrieves accurate content but misinterprets or incompletely reads what it observed, drawing the wrong conclusion from a correct result.
*Common error:* Describing only one or two failure modes, or conflating action failure with observation failure.
*Chapter reference:* ReAct failure modes

---

**Q10 — Brief-Response**
*Model answer:* The classmate's view is partially correct but misses the chapter's argument. Technical requirements do drive architecture — a predictable workflow needs graph-based orchestration; a creative, exploratory task might need a looser agent model. But the chapter's additional claim is that these same technical decisions determine the user experience: how failures appear, how inspectable the system is, how much the user trusts the output. That experience is a brand commitment. So the classmate is right that technical requirements matter, but wrong to separate them from brand commitments — they are the same decision viewed from different angles.
*What a strong answer includes:*
- Acknowledgment that the classmate's technical-requirements point is partially valid
- The chapter's argument that user experience (trust, debuggability, failure mode) is a brand commitment embedded in architecture
- At least one concrete example (e.g., graph-based vs. conversation-based producing different trust signals)
*Common error:* Simply asserting the classmate is wrong without engaging the technical-requirements point.
*Chapter reference:* Architecture as brand decision

---

**Q11 — Transfer Brief-Response**
*Model answer:* For a software debugging assistant, specialized roles might include: a Reproduction Agent (reproduces the bug from a description), a Diagnosis Agent (reads error logs and stack traces to identify the root cause), and a Fix-Proposal Agent (generates candidate fixes with explanations). The orchestration layer would need to decide whether to run all three sequentially or to gate the Diagnosis Agent on the Reproduction Agent's success first — and what to surface to the human when Reproduction fails, since the bug cannot be diagnosed without it.
*What a strong answer includes:*
- At least three named roles with distinct responsibilities
- An explanation of what the orchestration layer must decide
- Evidence that the student understands specialization vs. general-purpose as a design principle
*Chapter reference:* Madison architecture logic (transfer application)

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

- Confusing the three ReAct failure modes — students often conflate reasoning and observation failures.
- Treating the Cursor/Devin distinction as a model choice rather than an architectural/product philosophy choice.
- Missing the "architecture as brand decision" argument — students who focus purely on technical correctness will score poorly on Q10.

**Signs a student needs to return to the chapter before this quiz:**

- Cannot name the five Madison roles without prompting.
- Describes the ReAct loop in the wrong order.

**Scaffolding adjustments:**

- *For students who score below 5:* Start with the ReAct loop and draw the three steps as a diagram before attempting quiz questions. The loop structure is prerequisite knowledge for Q1, Q6, and Q9.
- *For students who score 11/11 on first attempt:* Ask them to design a Madison-style architecture for a specific use case from their archetype and write a one-paragraph defense of each role split.
