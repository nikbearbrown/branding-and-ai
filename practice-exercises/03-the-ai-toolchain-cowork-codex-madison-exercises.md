# Chapter 3 — The AI Toolchain: Cowork, Codex, Madison: Practice Exercises

**Course:** INFO 7375 — Branding and AI: Building the Creative Engineer
**Chapter learning objectives tested:** Four meanings of "agent" in AI; Madison's 5-layer architecture (Intelligence/Content/Research/Experience/Performance + Orchestration); ReAct loop (Thought→Action→Observation); three failure modes of ReAct (reasoning/action/observation); graph-based vs. conversation-based orchestration; architecture as brand decision; McLuhan's "medium is the message."

---

## Worked Example

**Problem:** A startup is building an AI tool that monitors competitor news and generates a weekly briefing report. Their lead engineer says: "Let's just use a single LLM call—give it all the RSS articles and ask it to write the briefing." Their product manager counters: "We should use a ReAct loop so the agent can search for additional context when it finds a story it doesn't fully understand." 

Using the ReAct framework from Chapter 3, evaluate both proposals. Which is more appropriate for this use case, and what failure mode does each carry?

**Approach:** Apply the Thought→Action→Observation loop definition from Chapter 3. Identify what a single LLM call can and cannot do. Then analyze whether the competitor news briefing task has the properties that benefit from ReAct's adaptive reasoning.

**Answer:** The single LLM call approach treats the task as a one-shot generation problem: all context is provided upfront, the model generates a response, and the loop ends. This works when the task is fully specified in the input context—but competitor news briefing involves understanding implications that depend on context the model may not have (a competitor's product launch may only be significant if you know what their previous roadmap was, which requires memory or retrieval). The failure mode is reasoning failure: the model generates a briefing that misses significance because it lacked context it needed but could not retrieve.

The ReAct loop allows the agent to reason ("this story mentions a feature that might conflict with our strategy—I should look up our current feature roadmap"), act (search or retrieve relevant information), and observe (incorporate the search result into its understanding) before generating the final briefing. The ReAct loop is more appropriate here because the task involves reasoning about significance, not just summarization. However, it introduces its own failure mode: observation failure, where the agent retrieves incorrect or irrelevant information and incorporates it confidently into its reasoning.

**What to notice:** The choice between a single LLM call and a ReAct loop is not "simpler vs. more powerful." It is a decision about the failure mode profile: single calls fail when context is incomplete; ReAct loops fail when the agent's reasoning or retrieved observations lead it astray. The product manager is right that the competitor briefing task benefits from ReAct—but the team needs to design for observation failure, not assume the loop will reliably self-correct.

---

## Tier 1 — Remember and Understand

### Contrastive Classification (Required)

**1.1** The chapter identifies four distinct meanings of the term "agent" used in AI product discussions. Below are four descriptions. Match each description to its meaning from Chapter 3's taxonomy, and explain in one sentence why each description fits that meaning rather than one of the other three.

(a) "Our RAG pipeline retrieves relevant documentation chunks, passes them to GPT-4o-mini with a system prompt, and returns a formatted answer. It runs end-to-end without user input after the initial query."

(b) "Our orchestration layer assigns customer service requests to specialized sub-agents—one for billing, one for technical support, one for returns—based on the request type."

(c) "Claude acts as our senior brand strategist. It reviews content drafts, flags off-brand language, and suggests revisions, but a human approves every change before publication."

(d) "Our Devin-equivalent system receives a bug report, opens the relevant files, runs the test suite, proposes a fix, submits a pull request, and continues working until the CI passes—without human checkpoints."

`(Tests: four meanings of "agent" in AI — contrastive classification)`

**Answer:**
(a) *LLM with tools and a loop* — the system performs retrieval (tool use), calls an LLM, and returns a result end-to-end; it has a defined task scope and runs deterministically. It is not a "role in a pipeline" because it performs the complete task, not a specialized sub-task within a larger system.

(b) *Role in a multi-agent pipeline* — the orchestration layer assigns work to specialized sub-agents; each sub-agent is an "agent" in the sense of playing a defined role within a coordinated architecture. This is not autonomous agency because the orchestration layer makes the routing decisions.

(c) *Function plus prompt (or role-based agent)* — Claude is playing a designated role (senior brand strategist) with a specific function (reviewing and flagging content); human approval gates prevent autonomous action. The key distinction from the autonomous category is the human checkpoint.

(d) *Autonomous agent* — the system sets its own sub-goals (run tests, propose fix, iterate until CI passes), acts without human checkpoints, and self-directs until the high-level goal is achieved. This is the fullest sense of agency in the chapter's taxonomy.

*Common error:* Students often classify (a) as autonomous because it "runs without user input"—but autonomy in the chapter's framework refers to self-directed goal-setting and action without human approval, not merely to automated execution of a fixed pipeline.

*Chapter reference:* Chapter 3, "Four Meanings of Agent."

---

**1.2** Name the five layers of Madison's architecture and the Orchestration layer. For each of the five layers, write one sentence describing what that layer does and why it is a separate layer rather than being absorbed into one of the others.

`(Tests: Madison's 5-layer architecture — layer identity and rationale)`

**Answer:** Intelligence: ingests and analyzes external signals (news, competitor activity, market data)—a separate layer because retrieval and analysis is a distinct technical and quality concern from content creation. Content: generates brand-consistent content (copy, headlines, summaries)—a separate layer because the content generation task requires different models, prompts, and quality criteria than intelligence analysis. Research: performs deep, multi-step research and synthesis—a separate layer because research requires multi-step reasoning and verification that differs structurally from both intelligence monitoring and content generation. Experience: manages user-facing interactions and interfaces—a separate layer because the user experience layer must be responsive and context-aware in ways that analytical layers do not require. Performance: monitors brand performance metrics and attribution—a separate layer because performance measurement requires different data sources and reporting cadences than operational layers. Orchestration: coordinates the other five layers, routing tasks and managing state—a separate cross-cutting layer because coordination logic would otherwise be duplicated across all layers, creating incoherence.

*Common error:* Describing the layers as interchangeable modules without explaining why the separation exists (what would go wrong if the layers were merged).

*Chapter reference:* Chapter 3, "Madison's 5-Layer Architecture."

---

**1.3** Trace the Thought→Action→Observation loop for the following scenario: an agent is asked to identify whether a competitor has announced a new pricing tier in the past 30 days. The agent searches a news API, finds three relevant articles, reads them, and determines that no pricing announcement has been made. Write out the Thought, Action, and Observation for each cycle of the loop, and identify where the loop terminates and why.

`(Tests: ReAct loop — Thought/Action/Observation cycle tracing)`

**Answer:**

*Cycle 1:*
- Thought: "I need to determine whether a competitor announced a new pricing tier in the last 30 days. I should search for their pricing announcements in recent news."
- Action: Query news API for "[competitor name] pricing announcement" with a 30-day date filter.
- Observation: Three articles returned: two are general industry pieces mentioning the competitor in passing; one is a product update article from 22 days ago that discusses feature releases.

*Cycle 2:*
- Thought: "None of the articles clearly confirm a pricing announcement. The product update article mentions features but not pricing—I should read it more carefully."
- Action: Retrieve full text of the product update article and extract pricing-relevant passages.
- Observation: The article discusses three new features and a small interface redesign; no pricing tier changes are mentioned.

*Cycle 3:*
- Thought: "I have checked the available sources and found no evidence of a pricing announcement. The task is complete."
- Action: Generate final response: "No pricing announcement detected in the past 30 days based on available news sources."
- Observation: (Loop terminates—goal achieved.)

The loop terminates because the agent has completed the assigned goal: it has searched, verified, and arrived at a conclusion it can report with appropriate confidence.

*Chapter reference:* Chapter 3, "ReAct Loop."

---

**1.4** McLuhan's phrase "the medium is the message" is cited in the chapter in the context of AI architecture choices. In two to three sentences, explain what McLuhan meant by this phrase and how the chapter applies it to the decision between graph-based and conversation-based orchestration.

`(Tests: McLuhan's medium is the message — applied to architecture as brand decision)`

**Answer:** McLuhan argued that the medium through which communication is delivered shapes the audience's experience and understanding independently of the content—the form is itself meaningful. The chapter applies this to AI architecture by arguing that the choice between graph-based orchestration (n8n, LangGraph—structured, explicit, deterministic) and conversation-based orchestration (AutoGen—emergent, adaptive, less predictable) is not neutral: it shapes what kind of product the user experiences, what failure modes appear, and what trust relationships are possible. A product built on graph-based orchestration signals predictability and auditability; one built on conversation-based orchestration signals flexibility and emergent collaboration—the architecture, like the medium, communicates something beyond its functional output.

*Chapter reference:* Chapter 3, "Architecture as Brand Decision," "McLuhan."

---

**1.5** The chapter identifies three failure modes of the ReAct loop. Name all three, and for each, give one example of how that failure mode would manifest in a research agent that is tasked with summarizing peer-reviewed literature on a topic.

`(Tests: ReAct failure modes — reasoning/action/observation)`

**Answer:**

*Reasoning failure:* The agent's internal reasoning about what to do next is flawed. Example: the research agent reasons "this topic is well-studied, so three papers will be sufficient" and terminates before finding the most relevant recent publication, producing an incomplete summary that misses the current state of the field.

*Action failure:* The agent reasons correctly but executes the action incorrectly. Example: the agent correctly identifies it needs to search Google Scholar but constructs a search query with incorrect terms or syntax, retrieving papers from an unrelated field and including them in its summary.

*Observation failure:* The agent retrieves correct information but misinterprets or misrepresents what it observed. Example: the agent retrieves a meta-analysis paper and a primary study, but misreads the meta-analysis's conclusion as applying to the primary study's specific sample—reporting a finding that the individual study did not actually support.

*Common error:* Students often describe reasoning and action failure as the same thing (both are "the agent doing the wrong thing"). The distinction is where the error occurs: reasoning failure is in the Thought step; action failure is in the Action step (correctly reasoned but incorrectly executed); observation failure is in the Observation step (correct action, but the retrieved information is misread or incorporated incorrectly).

*Chapter reference:* Chapter 3, "Three Failure Modes of ReAct."

---

## Tier 2 — Apply and Analyze

### Error Analysis (Required)

**2.1** A student building an AI competitor analysis tool writes the following architectural description in their project README:

> "My tool uses an agentic approach. The agent uses ReAct to loop through competitor websites, extract pricing information, and write a summary. I chose ReAct over a simple LLM call because agents are smarter and can handle complex tasks. The agent also uses Madison's Content layer to make sure the output sounds good."

Identify the specific errors or misuses of the chapter's concepts in this description (there are at least three). Rewrite the architectural description correctly, using precise vocabulary from Chapter 3.

`(Tests: ReAct framework, Madison architecture — misapplication identification and correction)`

**Answer — Errors:**

Error 1: *"Agents are smarter" is not the reason to choose ReAct.* The chapter identifies the choice between a single LLM call and a ReAct loop based on whether the task requires adaptive reasoning about intermediate observations—not based on general intelligence. Using ReAct for a task that could be accomplished with a chained LLM call adds unnecessary complexity and new failure modes without benefit.

Error 2: *The student treats Madison's Content layer as a style-editing layer at the end of a pipeline.* Madison's Content layer generates brand-consistent content as a specialized function within a coordinated architecture; it is not an output-polishing step appended to an unrelated pipeline. Using it this way would require the pipeline to interface with the Content layer's input expectations, which are specific to Madison's architecture.

Error 3: *"Loop through competitor websites" is not how ReAct works with web content.* The ReAct loop reasons about what actions to take and interprets observations; it does not "loop through" a list of URLs as a batch operation unless designed specifically to do so. Describing it as looping through websites conflates the ReAct reasoning cycle with an iteration construct.

**Rewritten description:** "My tool uses a multi-step architecture. An initial ingestion step retrieves publicly available pricing pages from a predefined list of competitor URLs using an HTTP request node in n8n. A ReAct agent then receives the extracted text, reasons about what additional context is needed (searching for pricing-change announcements in recent news), and synthesizes the available information into a structured pricing comparison. A final formatting step generates the summary output in my brand's voice. I chose a ReAct agent for the synthesis step because pricing interpretation requires reasoning about significance and context that cannot be specified in a single prompt—but I keep the ingestion step deterministic to avoid action failures in data collection."

*Chapter reference:* Chapter 3, "ReAct Loop," "Madison Architecture," "Architecture as Brand Decision."

---

### Self-Explanation Exercise (Required)

**2.2** The chapter argues that the choice between graph-based orchestration (n8n, LangGraph) and conversation-based orchestration (AutoGen) is a *brand decision*, not just a technical one. Using only Chapter 3's concepts and vocabulary, explain *why* this must be true. Your explanation should reason from the McLuhan principle and at least one concrete consequence for the user's experience.

`(Tests: architecture as brand decision — principled reasoning using McLuhan's medium is the message)`

**Answer (model):** McLuhan's claim is that the form of a communication shapes its meaning independently of the content. Applied to orchestration architecture: graph-based systems produce deterministic, inspectable workflows—a user or developer can trace exactly which node ran when and what output it produced. Conversation-based systems produce emergent coordination—agents negotiate, iterate, and sometimes produce unexpected paths to a result. These are not just different technical implementations of the same product; they are different brand experiences. A graph-based system signals auditability, predictability, and control—values consistent with a Sage or Ruler archetype where trust comes from transparency. A conversation-based system signals adaptability, emergence, and exploration—values consistent with a Creator or Explorer archetype where discovery is part of the value. When a product built on graph-based orchestration fails, the failure is locatable (a specific node produced bad output). When a product built on conversation-based orchestration fails, the failure is diffuse (the emergent conversation went wrong in ways that are difficult to reproduce or explain). These different failure mode profiles are not separable from the brand experience: the user of a graph-based system who encounters a failure learns something auditable; the user of a conversation-based system who encounters a failure experiences opacity. The architecture is communicating these properties even when nothing goes wrong.

*Chapter reference:* Chapter 3, "Architecture as Brand Decision," "McLuhan," "Graph-Based vs. Conversation-Based Orchestration."

---

### Cumulative Exercise (Required — integrates Chapter 2 concepts)

**2.3** Chapter 2 argues that brand equity accumulates through consistent experiences and is revealed under adversity. Chapter 3 argues that architecture choices shape the user's trust relationship with a product. Apply both frameworks to the following scenario:

A developer tool startup has built a code review agent using conversation-based orchestration (AutoGen). The tool works well under normal conditions, but after three months, a user reports that the agent produced a confident code review that missed a significant security vulnerability—and the failure was not reproducible (the team cannot replicate the conversation path that led to the error). Analyze this failure using both Chapter 2's brand equity framework and Chapter 3's architecture concepts.

*(References Chapter 2's brand equity and adversity test; Chapter 3's orchestration failure modes and architecture as brand decision.)*

`(Tests: brand equity under adversity [Chapter 2] + ReAct/orchestration failure modes [Chapter 3] — integrated analysis)`

**Answer (model):** From Chapter 2's perspective: the security vulnerability failure is an adversity test. Before the failure, the tool may have accumulated positive equity—positive judgments, strong performance reviews. The forgiveness dimension of equity (one of the three manifestations) determines whether users stay. In this case, the failure is high-stakes (security) and the company cannot provide an explanation (non-reproducible failure)—two factors that compound the trust damage. A brand with deep equity might survive one such failure; a startup tool with limited accumulated equity likely cannot. From Chapter 3's perspective: the failure is an observation failure (or a reasoning failure) within the conversation-based orchestration. The non-reproducibility is a structural property of conversation-based systems: emergent agent coordination creates execution paths that are difficult or impossible to replay exactly. A graph-based system would have produced an auditable trace showing exactly which node made the incorrect reasoning step—enabling both explanation and correction. The architecture decision (AutoGen/conversation-based) was a brand decision that accepted opacity as a trade-off for adaptability. Under adversity, that trade-off reveals itself: the startup cannot explain the failure because the medium (emergent coordination) does not produce an explanation. The McLuhan principle applies: the medium (non-reproducible conversation orchestration) communicated opacity even in the tool's better days; the adversity just made the communication visible.

*Chapter reference:* Chapter 3, "Architecture as Brand Decision," orchestration; Chapter 2, "Brand Equity Under Adversity."

---

### AI Interaction Exercise (Required)

**2.4** Choose Option A or Option B.

**Option A (Evaluate and Verify):** Ask an AI assistant: "What is the ReAct pattern in AI agents, and what are its main failure modes?"

(1) Record the response (or a representative excerpt).
(2) Identify one thing the AI correctly explained.
(3) Identify one thing the AI omitted or got wrong relative to Chapter 3. Pay particular attention to whether the AI distinguished reasoning, action, and observation failures as separate categories.
(4) Write a corrected explanation of the three failure modes using Chapter 3's framework.

`(Tests: ReAct loop and failure modes — AI response evaluation)`

**Option B (Answer First, Then Compare):** Before using any AI tool, write your own explanation of the three ReAct failure modes (reasoning, action, observation), with one example of each from a research or analysis task. Then ask an AI the same question.

(1) Where did the AI agree with your explanation?
(2) Where did the AI add something useful you had not considered?
(3) Where did the AI's explanation differ from Chapter 3 in a way you believe is incorrect?
(4) Write a synthesis explanation you are confident is accurate.

`(Tests: ReAct failure modes — self-assessment and verification against chapter content)`

*Verification step (required for both options):* Locate the original Yao et al. (2023) "ReAct: Synergizing Reasoning and Acting in Language Models" paper (available on arXiv). Confirm whether the AI's description of the ReAct loop matches the original paper's formulation or introduces significant modifications. Note one specific point of convergence or divergence.

*Chapter reference:* Chapter 3, "ReAct Loop," "Three Failure Modes."

---

**2.5** The chapter says "architecture is a brand decision." A classmate argues: "Architecture is purely a technical decision based on scalability, cost, and reliability. Brand is about logos, colors, and messaging. These are completely different domains." In two to three sentences, respond to this argument using the chapter's reasoning.

`(Tests: architecture as brand decision — principled response)`

**Answer:** The chapter's argument is that brand is not the output of a logo or a tagline but the sum of every experience a user has with a product—including the failure modes they encounter, the speed of the tool, the accuracy of its outputs, and whether it can explain itself when something goes wrong. Architecture decisions directly shape all of these experiences: a graph-based system that is auditable and predictable produces a different brand experience from a conversation-based system that is adaptive and opaque, even if both have identical logos and taglines. McLuhan's formulation makes this precise: the medium (the architecture) communicates independently of the content (the outputs), which means the classmate's separation of architecture from brand is not supported by the evidence of how users actually experience and evaluate products.

*Chapter reference:* Chapter 3, "Architecture as Brand Decision," "McLuhan."

---

## Tier 3 — Analyze and Evaluate

**3.1** Cursor (the AI-powered IDE) and Devin (the autonomous software engineering agent) are both AI tools for developers, both using LLMs, and both aimed at improving engineering productivity. Compare them using Chapter 3's framework along three dimensions: (a) where in the four-agent-meanings taxonomy each falls; (b) how their ReAct implementations (or lack thereof) differ; (c) how their different architectures constitute different brand positions—what each communicates to the user about what to trust, what to expect, and what happens when something goes wrong.

*(References Chapter 3's four-agent taxonomy, ReAct framework, and architecture-as-brand-decision.)*

`(Tests: four-agent taxonomy, ReAct, architecture as brand — integrated comparative analysis)`

**Model answer:**

(a) *Four-agent taxonomy:* Cursor sits closest to "LLM with tools and a loop" or "role in a pipeline"—it enhances the developer's workflow at specific moments (code completion, test generation, refactoring suggestions) with the developer maintaining control over what is accepted and what is rejected. Devin is the fullest expression of the "autonomous agent" meaning: it sets sub-goals, runs code, reads error output, revises its approach, and completes tasks without human checkpoints within the execution window.

(b) *ReAct implementation:* Cursor's tight human-in-the-loop design means its reasoning cycles are short and each action is immediately validated by the developer before proceeding—the developer functions as the observation-interpretation layer. Devin uses a ReAct-style loop fully autonomously: it reads its test output (Observation), reasons about the next fix (Thought), and acts (Action) through many cycles without human review. This makes Devin more powerful for independent task completion and more vulnerable to compounding observation failures across many cycles.

(c) *Architecture as brand position:* Cursor communicates: "you remain in control; I am a tool that amplifies your judgment." When Cursor makes a bad suggestion, the developer rejects it immediately—failure is contained and low-cost. Devin communicates: "delegate to me; I will complete the task." When Devin's autonomous loop produces a bad intermediate decision, subsequent steps build on a flawed foundation—failure is potentially expensive and difficult to localize. These are not equivalent brand positions: Cursor's architecture builds trust through transparency and control; Devin's architecture requires trust upfront and delivers audit trails only after the fact.

*Common error:* Describing the two tools as simply "different levels of automation" without engaging the failure mode implications and the trust relationship each architecture creates.

*Chapter reference:* Chapter 3 throughout.

---

**3.2** A skeptic argues: "Madison's five-layer architecture is unnecessarily complex. You could accomplish the same marketing intelligence tasks with a single, well-prompted LLM call—the layer separation is organizational theater that adds coordination overhead without meaningful benefit." Construct the strongest version of this counterargument, and then evaluate whether Madison's architecture is justified. Your evaluation should reference specific properties of the ReAct failure modes and the orchestration models from Chapter 3.

*(References Chapter 3's Madison architecture, ReAct failure modes, and orchestration models.)*

`(Tests: Madison architecture — evaluating the justification for layer separation against a coherent counterargument)`

**Model answer:** The counterargument's strongest form: a well-prompted LLM with access to the right tools can perform retrieval, analysis, content generation, and performance assessment in a single session; the coordination overhead of five specialized layers creates latency, complexity, and failure points at each inter-layer boundary. For small-scale marketing intelligence tasks, a single-prompt system may produce equivalent output with far less engineering complexity.

Evaluation: The counterargument is right for small-scale, low-stakes tasks where a single prompt can capture the full context needed. It fails for the tasks Madison is designed for: high-volume, ongoing, multi-source marketing intelligence with multiple output formats (intelligence reports, content drafts, performance dashboards). The justification for layer separation is primarily about *failure localization and iterative improvement*: a failure in the Intelligence layer (bad source data) is distinguishable from a failure in the Content layer (off-brand writing) only if the layers are separated. In a single-prompt system, a bad output from the LLM could be caused by poor source retrieval, weak reasoning, or poor generation—there is no way to diagnose which. As the chapter notes in the ReAct failure-mode discussion: observation failure, reasoning failure, and action failure have different diagnoses and different fixes. Layer separation makes the diagnosis possible. The skeptic's counterargument is also weakened by the architecture-as-brand-decision argument: the five-layer separation creates auditable, improvable components that can be independently upgraded as models improve—a property a monolithic single-prompt system cannot provide.

*Chapter reference:* Chapter 3, "Madison Architecture," "ReAct Failure Modes," "Architecture as Brand Decision."

---

## Tier 4 — Evaluate and Create

**4.1 — Challenge Exercise**

The chapter argues that architecture choices are brand decisions because the medium (the architecture's form) communicates independently of the content (the outputs). This argument draws on McLuhan, published in 1964.

Design a test that could determine whether a tool's architecture is actually detectable by users as a brand signal—that is, whether users experience graph-based and conversation-based orchestration as producing meaningfully different brand impressions, independent of the quality of the outputs.

Your design should address:
- What would you show or give to users in each condition?
- How would you control for output quality (so that the architecture, not the quality, is the variable)?
- What user behaviors or perceptions would you measure?
- What result would confirm or refute the chapter's architecture-as-brand-decision claim?
- What confound is hardest to eliminate in this design?

Your response should be 400–600 words. Do not provide a model answer; evaluate based on:
- Does the design isolate architecture as the independent variable?
- Does it specify measurable brand perception outcomes?
- Does it engage the hardest confound (users may not consciously detect architecture but may sense failure modes differently)?
- Does it state what a falsifying result would look like?

`(Tests: architecture as brand decision — experimental design for McLuhan's claim applied to AI products)`

---

## Answer Key

| Item | Correct Answer | Common Error | Chapter Reference |
|------|---------------|--------------|-------------------|
| 1.1 | (a) LLM+tools+loop; (b) Role-in-pipeline; (c) Function+prompt/role; (d) Autonomous | Classifying (a) as autonomous because it "runs without user input" | Ch. 3, Four Meanings of Agent |
| 1.2 | Five layers + Orchestration, each with distinct technical function and quality concern | Describing layers without explaining why separation exists | Ch. 3, Madison Architecture |
| 1.3 | Three-cycle ReAct trace with correct Thought/Action/Observation structure and termination condition | Conflating Thought with Action; missing termination reasoning | Ch. 3, ReAct Loop |
| 1.4 | McLuhan: medium shapes meaning; applied: graph-based signals control/auditability, conversation-based signals adaptability/opacity | Treating McLuhan as only about mass media, not applicable to software | Ch. 3, McLuhan / Architecture as Brand Decision |
| 1.5 | Reasoning: wrong Thought; Action: wrong execution of correct Thought; Observation: misreading correct observation | Conflating reasoning and action failure as the same error type | Ch. 3, Three Failure Modes |
| 2.1 | Three errors: "agents are smarter" (wrong reason); Content layer misuse; "loop through" mischaracterizes ReAct | Catching one or two errors but missing the third | Ch. 3, ReAct / Madison Architecture |
| 2.2 | McLuhan applied: orchestration form communicates audit/control vs. opacity independent of output content | Treating architecture choice as purely technical with no brand consequence | Ch. 3, Architecture as Brand Decision |
| 2.3 | Forgiveness dimension (Ch. 2) + observation/reasoning failure + non-reproducibility as structural property of conversation orchestration | Analyzing only one chapter; not connecting architecture type to equity impact | Ch. 3 + Ch. 2 integration |
| 2.5 | Brand = sum of user experiences including failure modes; architecture shapes all of these; McLuhan supports this | Accepting the classmate's separation of technical and brand decisions | Ch. 3, Architecture as Brand Decision |
| 3.1 | Cursor = tools+loop/role; Devin = autonomous; ReAct loop length differs; brand positions differ on trust relationship and failure cost | Describing as "levels of automation" without engaging failure modes or trust | Ch. 3 throughout |
| 3.2 | Counterargument strongest for small-scale tasks; fails for high-volume multi-output; layer separation enables failure localization and iterative improvement | Accepting counterargument without engaging the failure localization argument | Ch. 3, Madison Architecture / ReAct Failure Modes |

---

## Instructor Notes

**Tier 1 volume:** 5 items (chapter has 5+ LOs)
**Worked example:** Uses competitor news briefing scenario to model the ReAct vs. single-LLM-call decision and failure mode reasoning before exercises begin
**Contrastive classification (1.1):** Targets the most common misconception—conflating "automated execution" with "autonomous agency"; all four options are plausible AI system descriptions
**Error analysis (2.1):** Three genuine conceptual errors in the student's description, not typos; errors reflect common misapplication of technical vocabulary from the chapter
**Self-explanation (2.2):** Requires applying McLuhan's principle to architecture; prevents students from saying "the book says so" by requiring derivation from the medium-message reasoning
**Cumulative (2.3):** Integrates Chapter 2 (brand equity under adversity, forgiveness dimension) with Chapter 3 (orchestration failure modes); explicitly requires referencing both chapters
**AI interaction (2.4):** Verification step requires locating the Yao et al. (2023) arXiv paper; plausible AI response expected to describe ReAct correctly at a high level but may conflate the three failure modes or omit observation failure as a distinct category
**Synthesis exercises (3.1–3.2):** Both reference Chapter 3 explicitly; 3.1 uses Cursor/Devin as real examples named in the chapter; 3.2 requires constructing a genuine counterargument before evaluating
**Challenge (4.1):** Tests experimental design ability applied to the McLuhan claim; no model answer; rubric criteria listed for instructor; hardest confound (conscious vs. unconscious detection of architecture) is specified as a required engagement point
