# Chapter 23: ShipIt — Interface and Deployment — Practice Exercises

*INFO 7375 · Branding and AI · Northeastern University*

---

> **How to use these exercises:**
> Work through each tier in order. Do not skip ahead to later tiers before completing earlier ones — the tiers scaffold your understanding. Attempt every exercise before checking the answer key. For open-ended questions, write at least 2–3 sentences before reading the model answer. The act of attempting is where the learning happens.

---

## Learning Objectives

- Name and describe the four interface layers (visual surface, interaction model, deployment surface, brand surface) and explain how each makes an implicit promise to the user
- Identify and classify the three types of interface misalignment (confidence, capability, tone) using real product cases (Google Bard, Snapchat, Microsoft Tay)
- Distinguish between Streamlit and Gradio by use case (do work vs. try the model) and explain the mismatch risk for multi-agent systems
- Define the minimum viable interface and identify its three required elements
- Conduct an alignment audit by mapping implicit interface promises to system reality
- Write a complete, ordered README as interface

*Every exercise below maps to at least one of these objectives. The `(Tests: ...)` tag on each exercise identifies which one(s) by full concept name.*

---

## Worked Example

*Study this example before attempting Tier 1. After reading it, close it and try to recall the key steps from memory before moving on.*

**Problem:** A team has built a multi-agent competitive intelligence system that runs three agents (research, analysis, synthesis) coordinated by an n8n workflow. They are deciding between Streamlit and Gradio for the user-facing interface. Apply the chapter's framework to make the recommendation and write the alignment audit for one interface layer.

**Approach:**
- Step 1 — Identify the use case type. Streamlit is for "do work" — multi-step workflows and dashboards where users want to get a job done using a specific tool. Gradio is for "try the model" — single-purpose demos designed to let users experiment with an AI model. A multi-agent competitive intelligence system that runs research, analysis, and synthesis is clearly a "do work" tool, not a demo.
- Step 2 — Apply the mismatch test. The chapter warns: "The most common mismatch is wrapping an orchestrated multi-agent system behind a Gradio free-form prompt box." A Gradio free-form prompt box implies "you can ask me anything and I will respond" (a conversational AI experience). A multi-agent pipeline that runs three sequential specialized agents has a specific task scope and a specific output format — it is not designed for free-form general queries.
- Step 3 — Write the alignment audit for the interaction model layer.
  - Implicit promise: "Type your query and I will search for competitive intelligence about it."
  - System reality: The system runs a fixed three-agent pipeline (research → analysis → synthesis) that works best with structured company/topic inputs, not open-ended questions.
  - Misalignment type: Capability — the system cannot fulfill the broad conversational capability the free-form prompt box implies.
  - Fix: Use a structured input form (company name, industry, key questions) that accurately signals the system's scope.

**Answer:** Recommendation: Streamlit for the primary interface. Write one structured input form (company name, industry, two-three key questions) that makes the system's scope visible. Provide a processing status panel showing which agent is currently running (the chapter's "visible processing state" requirement). Present results in a structured report format, not a chat window.

Alignment audit (interaction model layer): Implicit promise: the input affordance implies the system's capability. Using a free-form prompt box implies conversational, open-ended capability. Using a structured form implies a specific, bounded task. System reality: the system runs a specific three-agent pipeline for competitive intelligence — not a general-purpose conversational system. The structured form is the honest interface.

**What to notice:** The Streamlit/Gradio decision is not primarily a technical preference — it is an alignment decision. The implicit promise of each tool's interaction model must match what the system actually does.

---

## Tier 1 — Warm-Up (Exercises 1–6)

*Bloom's Level: Remember / Understand*
*Purpose: Verify that the chapter's core concepts and vocabulary are in place before you apply them.*

---

**Exercise 1**

Name the four interface layers and explain in one sentence what promise each makes to the user.

*(Tests: four interface layers — names and implicit promises)*

**Answer:** (1) Visual surface: promises that the quality and craft of the design matches the capability of the system — a polished visual surface implies a polished, reliable system. (2) Interaction model: promises that the input affordance matches what the system can actually do — a free-form text box implies conversational capability; a structured form implies specific, bounded input. (3) Deployment surface: promises that the system is available and reliable in the context where users encounter it — a public URL promises that the system will work when accessed; a localhost demo promises nothing about production availability. (4) Brand surface: promises that the system's personality, tone, and output style are consistent with the brand's archetype — the language and behavior of the system's outputs reflect who the product is.

**Common error:** Treating the four layers as purely visual — the visual surface is only one layer. The interaction model, deployment surface, and brand surface are not visual design choices; they are architectural promises that can be broken independently of how the product looks.

*Chapter reference:* Chapter 23, "The Four Interface Layers."

---

**Exercise 2**

Name the three types of interface misalignment. For each type, name the real product case from the chapter and describe the mechanism of failure in one sentence.

*(Tests: three misalignment types — names, real cases, mechanisms)*

**Answer:** (1) Confidence misalignment — Google Bard/JWST error. Mechanism: the interface presented an AI-generated answer with the same visual confidence as a verified factual statement (no uncertainty signal, no source caveat), but the model's claim about JWST's first images was wrong. The interface promised more certainty than the model had. (2) Capability misalignment — Microsoft Tay/adversarial inputs. Mechanism: the interface presented Tay as a conversational chatbot open to any input ("The more you talk, the smarter Tay gets"), but the system had no adversarial robustness for the inputs it received from coordinated trolling. The interface promised a capability the system could not reliably deliver. (3) Tone misalignment — Snapchat redesign. Mechanism: Snapchat's interface redesign in 2018 changed the product's interaction model in ways that broke the tone contract with users who had built habits around the previous design — the brand surface and interaction model no longer aligned with the product users had adopted. The interface made a promise (continuity of experience) that the update broke.

**Common error:** Describing Tay as a confidence misalignment because "the system was confidently wrong." The Tay failure is a capability misalignment — the system claimed to be able to engage with any user in a general-purpose conversational way, but it could not handle adversarial inputs. The interface claimed a capability the system did not have.

*Chapter reference:* Chapter 23, "Three Types of Interface Misalignment."

---

**Exercise 3**

The chapter distinguishes Streamlit from Gradio by the question each is designed to answer. State each question explicitly, then identify which tool is appropriate for each of the following four use cases:

(a) A recruiter wants to evaluate whether an AI résumé screener works well enough to consider for purchase.
(b) An operations team wants to generate weekly competitive intelligence reports using a multi-agent pipeline.
(c) A research team wants to share a text classification model with colleagues at another institution for evaluation.
(d) A content manager wants to run a three-step content generation workflow (topic → outline → draft) on a daily schedule.

*(Tests: Streamlit vs. Gradio — use case distinction)*

**Answer:** Streamlit answers: "Do work." Gradio answers: "Try the model." (a) Gradio — the use case is evaluating whether the model works well enough; this is a demo/try context, not a production workflow. (b) Streamlit — the use case is running a multi-step workflow to produce a specific output on a regular schedule. This is a "do work" tool. (c) Gradio — the use case is sharing a model for evaluation; the interaction is "try this model and see what it does," not "run a workflow to accomplish a task." (d) Streamlit — the use case is a three-step workflow on a regular schedule; this is a production workflow tool, not a demo.

**Common error:** Choosing Gradio for (b) because "it is simpler to set up." The chapter's criterion is the use case, not setup complexity — a "do work" use case behind a "try the model" interface is the chapter's named mismatch.

*Chapter reference:* Chapter 23, "Streamlit vs. Gradio."

---

**Exercise 4**

What is the minimum viable interface? List its three required elements and explain in one sentence why each is necessary.

*(Tests: minimum viable interface — three required elements)*

**Answer:** The minimum viable interface has three required elements: (1) Input affordance that matches system scope — the input mechanism (text box, structured form, file upload, etc.) must signal to the user what the system can take in and what kinds of requests it can process. If the affordance implies broader capability than the system has, users will make requests the system cannot fulfill and conclude the system is broken. (2) Visible processing state — the interface must show that the system is working when it is working (a loading spinner, progress indicator, agent status panel, or status message). Without this, users cannot distinguish "the system is processing" from "the system is frozen" — a silent wait destroys confidence and trust in the product's reliability. (3) Output surface representing confidence accurately — the presentation of the system's output must reflect the system's actual certainty. If the system's output is structured JSON with a confidence field, the interface must render that confidence field visibly; presenting an uncertain output in the same visual format as a verified fact is the confidence misalignment failure mode (Google Bard/JWST).

**Common error:** Describing the minimum viable interface as purely a visual design standard (colors, fonts, spacing). The chapter's three elements are functional and architectural, not aesthetic.

*Chapter reference:* Chapter 23, "Minimum Viable Interface."

---

**Exercise 5**

The chapter describes the README as an interface and specifies six elements in a required order. List the six elements in the correct order and explain why the deployed URL must come first rather than the project description.

*(Tests: README as interface — six elements and rationale for ordering)*

**Answer:** Six elements in order: (1) Deployed URL (the live link to the running system), (2) What it does (one to two sentences describing the product's function), (3) How to use it (user-facing instructions), (4) Known limits (what the system cannot do, what inputs will fail, what edge cases are unhandled), (5) Architecture (which AI intelligence pattern, which agents if multi-agent, how they are connected), (6) Tech stack (Streamlit or Gradio, which LLM, which orchestration tool, deployment platform). The deployed URL comes first because the README is read by users who want to know whether the thing works before they want to know what it is. A visitor to a GitHub repository who sees a deployed URL first can test the product immediately; a visitor who sees a lengthy project description before the URL must read through the description and search for the link. The chapter frames this as an alignment decision: the README makes a promise about the project's state (does it run?) — putting the deployed URL first makes that promise explicit and verifiable.

**Common error:** Placing "what it does" first because "the description should orient the reader before the link." The chapter's argument is that a deployed URL is the most important piece of information and the reader should be able to access it immediately.

*Chapter reference:* Chapter 23, "README as Interface."

---

**Exercise 6**

True / False: An alignment audit produces a list of design changes to implement.

*Explain what an alignment audit actually produces and when it should be run.*

*(Tests: alignment audit — definition and purpose)*

**Answer:** False. An alignment audit produces a comparison table: on the left, the implicit promises the interface makes to the user; on the right, the system's actual capabilities and behavior at the corresponding layer. The audit is diagnostic, not prescriptive — it surfaces gaps between what the interface implies and what the system does. Changes to implement are the *response* to the audit, not the audit itself. The audit should be run before shipping: specifically, after the technical system is built and before the interface is considered final. Running it before shipping allows the team to address confidence, capability, or tone misalignments before users encounter them. It can also be run when the system's capabilities change after launch — if the underlying model is updated and its behavior changes, the interface's implicit promises may no longer match the new system reality.

**Common error:** Treating the alignment audit as a post-launch QA checklist (testing specific features). The audit is pre-launch and focuses on the alignment between interface promises and system reality, not on whether specific buttons work.

*Chapter reference:* Chapter 23, "Conducting an Alignment Audit."

---

## Tier 2 — Application (Exercises 7–14)

*Bloom's Level: Apply / Analyze*
*Purpose: Use the chapter's concepts in realistic situations.*

---

**Exercise 7** *(Scenario-Based Application)*

For each of the following interface descriptions, identify which of the four interface layers is making a broken promise, name the misalignment type (confidence, capability, or tone), and describe the fix.

(a) A career advice tool with a polished, professional visual design generates responses from a model with no access to current job market data. The responses are formatted in the same high-confidence visual style as verified market analysis.
(b) A creative writing assistant uses warm, encouraging language ("Great choice! Let's craft something beautiful together!") but when the user submits a prompt, the response is a generic, minimally contextual paragraph that does not engage with the user's specific idea.
(c) A product search tool is deployed on a company's internal Slack bot. When the company's IT team updates Slack's API version, the bot stops responding without error messages, and users assume the search feature has been removed.
(d) A text summarization tool provides a free-form text input ("Ask me anything") but only processes inputs shorter than 500 words and only works for English-language text.

*(Tests: four interface layers + three misalignment types — classification and fix)*

**Answer:** (a) Visual surface + confidence misalignment. The polished visual design and high-confidence formatting promise verified, current information, but the model has no access to current data. Fix: add a visible disclaimer (last data update, information currency) and render uncertain outputs with explicit uncertainty markers (hedging language, a "verify before acting" note). (b) Brand surface + tone misalignment. The warm, encouraging language promises a personalized, engaged creative collaborator, but the output is generic and unengaged. Fix: either improve the model's response quality to match the brand surface's tone promise, or adjust the brand surface language to set realistic expectations ("I'll help you draft a starting point you can build from"). (c) Deployment surface + capability misalignment. The Slack deployment promised availability in the channel where users work, but the deployment surface was not monitored for API compatibility — a change in the host platform broke the tool silently. Fix: implement a health-check monitor that alerts the team when the bot stops responding, and add a visible status indicator users can check before assuming the feature is gone. (d) Interaction model + capability misalignment. "Ask me anything" implies open-ended, unconstrained input, but the system has hard constraints (500-word limit, English only). Fix: replace the free-form prompt box with a structured input that signals the constraint (a character counter, a language selector limited to English, a visible word-limit notice).

**Common error:** Labeling all four as "capability misalignment" because "the system doesn't do what users expect." Each misalignment type is specific: confidence = wrong certainty level, capability = wrong scope of capability, tone = wrong personality/affect. The layer (visual, interaction, deployment, brand) is also specific to each case.

*Chapter reference:* Chapter 23, "Three Types of Interface Misalignment" and "The Four Interface Layers."

---

**Exercise 8** *(Error Analysis)*

> The following is a README submitted by a student for a multi-agent market research tool.

---
**Market Research Tool**

This project uses AI to help you research markets. It was built using Python, OpenAI GPT-4o, and n8n. The architecture includes three agents: a data collection agent, an analysis agent, and a synthesis agent. These agents are orchestrated using n8n.

**Installation:**
1. Clone the repository
2. Install requirements: `pip install -r requirements.txt`
3. Set your OpenAI API key in `.env`
4. Run `streamlit run app.py`

The tool searches for market data, analyzes trends, and produces a summary report. It works best for technology markets. Sometimes the analysis may be incomplete if data is unavailable.

**Live Demo:** [Click here](http://localhost:8501)
---

1. Identify three specific problems with this README as an interface.
2. Explain the failure mode each problem causes for users or evaluators.
3. Rewrite the README in the correct format.

*(Tests: README as interface — six elements, ordering, and common errors)*

**Answer:**
1. Three specific problems: (a) The deployed URL is at the bottom and points to `localhost:8501` — the README provides no public deployed URL, meaning evaluators cannot access the tool without running it themselves. This is a deployment surface problem, not just a README problem. (b) The ordering is wrong: the README begins with the project name (fine), then immediately goes to tech stack (architecture, installation, Python/GPT-4o/n8n) before "what it does" and before "known limits." The chapter specifies: deployed URL first, then what/how/limits/architecture/tech stack. (c) Known limits are buried in the last paragraph ("works best for technology markets," "sometimes incomplete") rather than called out explicitly — evaluators who scan will miss these constraints and encounter failures they did not anticipate.
2. Failure modes: (a) No public URL → evaluators cannot test the product; the README promises a deployed product but delivers nothing testable. (b) Tech-stack-first ordering → evaluators spend their first reading pass on installation and configuration rather than understanding what the tool does and whether it is worth their time. (c) Buried limits → evaluators test the tool with non-technology-market queries, get incomplete or wrong results, and conclude the tool is broken rather than understanding that these inputs are out of scope.
3. Rewritten README:
```
# Market Research Tool

[**Live demo** → https://market-research-tool.streamlit.app](https://market-research-tool.streamlit.app)

**What it does:** Generates structured market research reports for technology sectors by running three sequential agents (data collection, trend analysis, synthesis) coordinated through an n8n workflow.

**How to use it:** Enter a technology market name (e.g., "residential solar energy storage") and two to three specific research questions. Click "Run Research." The tool takes 60–90 seconds to run all three agents. Download the report as a PDF or copy the structured summary.

**Known limits:**
- Works for technology markets only — consumer goods, healthcare, and financial services markets produce incomplete results
- Data collection relies on web search; results may be incomplete for markets with limited English-language coverage
- Reports should be verified before using in investor or client presentations — confidence labels mark which findings are inferred vs. verified

**Architecture:** Orchestrated multi-agent system (n8n workflow): data collection agent → analysis agent → synthesis agent. Each agent uses a structured JSON output schema with confidence labeling. `allow_delegation=False` for all agents.

**Tech stack:** Streamlit, OpenAI GPT-4o, n8n (self-hosted), Python 3.11. Deployed on Railway.
```

**Common error:** Writing "Known limits: None" or placing known limits after the tech stack. The chapter argues that transparency about limits is a brand asset — users who know what the tool cannot do are more likely to trust it in the cases where it can.

*Chapter reference:* Chapter 23, "README as Interface."

---

**Exercise 9** *(AI Interaction — with verification requirement)*

First, write your own answer without consulting AI:
*"What is an alignment audit, and how do you conduct one for a Streamlit-based multi-agent pipeline?"*

Then read the following AI-generated response:

*AI response: "An alignment audit is a review process where you check whether the interface you've built accurately represents what your AI system can do. To conduct one for a Streamlit-based multi-agent pipeline: (1) Review each component of the interface — the input form, the processing display, and the output section. (2) Test the system with edge cases and unexpected inputs to see where it fails. (3) Check that the visual design is consistent and professional. (4) Verify that the loading state is visible when agents are running. (5) Update the README to reflect any issues you found."*

1. Identify the strongest point in the AI's response.
2. Identify the most significant gap relative to the chapter's treatment.
3. Write a correction or extension.
4. State the specific evidence you would use to verify that your alignment audit is complete.

*(Tests: alignment audit — definition, process, completeness)*

**Answer:**
1. Strongest point: Point (4) — "Verify that the loading state is visible when agents are running" — correctly identifies visible processing state as a required minimum viable interface element.
2. Most significant gap: The AI response describes the audit as a UI review and edge-case testing process, but the chapter's alignment audit is specifically a two-column comparison: implicit promises on the left, system reality on the right, organized by the four interface layers. The AI's process is generic UX testing, not the structured promise-vs.-reality analysis the chapter specifies. The three misalignment types (confidence, capability, tone) are entirely absent.
3. Extension: A chapter-aligned alignment audit for a Streamlit multi-agent pipeline works as follows: Create a two-column table with "Implicit promise" and "System reality" columns. Run through each of the four interface layers. Visual surface: does the polish level match the system's reliability level? If the interface is polished, users expect the system to work reliably — is that expectation accurate? Interaction model: does the input form's structure match what the system can take in? If the form has a free-form text box, it promises conversational capability — does the pipeline provide that? Deployment surface: is the app deployed at a public URL? Does the URL work from a browser without authentication? Is there a health check that confirms it is running? Brand surface: does the language in the UI (button labels, status messages, output headers) match the archetype the product is trying to embody? The output of the audit is the table itself — the list of gaps between promise and reality — not a list of fixes. Fixes come after the audit.
4. Verification evidence: The alignment audit is complete when every cell in the implicit-promise column has a corresponding entry in the system-reality column for all four layers, and every identified gap has been classified as one of the three misalignment types (confidence, capability, tone). A second test: ask someone who has not seen the system to use the interface for five minutes and write down what they think the system can do. Compare their list to the actual system capability. Gaps between their list and the reality are implicit promises the interface is making that you did not document.

*Chapter reference:* Chapter 23, "Conducting an Alignment Audit."

---

**Exercise 10** *(Self-Explanation)*

The chapter argues that the README is "an interface before the interface" — that the README makes implicit promises to users and evaluators before they ever interact with the product itself. Explain in 2–3 sentences what this means, and give one concrete example of an implicit promise a README makes that can be broken without writing a single bad word.

*(Tests: README as interface — implicit promises and pre-product alignment)*

**Answer:** The README is an interface before the interface because it shapes the user's expectation framework before they click a button or run a command. If the README presents the project as production-ready, the reader arrives at the product with production-level expectations — and a buggy or limited prototype will feel like a failed product rather than an early-stage experiment. A concrete example of an implicit promise broken without a single bad word: a README that provides a `localhost:8501` URL as the "live demo" link promises a deployed, accessible product but delivers a link that only works on the developer's machine. No word in the README is false — the URL is real, the demo exists — but the promise (that the evaluator can access the demo) is broken by the localhost deployment.

**Common error:** Describing README promises as explicit claims ("the README says it does X but it actually does Y"). The chapter's point is that implicit promises — made through formatting, ordering, and presence or absence of sections — shape expectations without stating them directly.

*Chapter reference:* Chapter 23, "README as Interface."

---

**Exercise 11** *(Cumulative — prior chapter concept)*

In Chapter 22, you learned about the *four AI intelligence patterns* — specifically that each pattern makes a different architectural choice about who controls the next step in the workflow. In this chapter, you are working with the *Streamlit vs. Gradio decision* — specifically that the interface must match the system's actual use case and capability.

Apply these two frameworks together to evaluate the following scenario: A team has built a tool-using agent (ReAct pattern) that searches for job postings, reads the relevant listings, and produces a structured job-match report for a given candidate. They are deciding between Streamlit and Gradio for the interface, and they are considering using a single free-form prompt box ("Tell me what kind of job you're looking for") as the input.

Identify: (1) which interface tool is appropriate, (2) whether the single free-form prompt box is an alignment risk, and (3) what the minimum viable interface should include for this tool.

*(Tests: Streamlit vs. Gradio + four AI intelligence patterns — Ch. 22 + Ch. 23)*

**Answer:** (1) Streamlit is appropriate. The tool is a job-match report tool — the user is trying to get a specific job done (find matched positions) using a specific tool, not trying out a general-purpose model. The "do work" use case maps to Streamlit, not Gradio. (2) The free-form prompt box is an alignment risk. A tool-using agent (ReAct) is powerful for adaptive search, but it has a specific input structure that produces reliable output: it works best with a defined target role, a defined location range, a defined level of experience, and any must-have or must-not-have criteria. A free-form prompt box ("Tell me what kind of job you're looking for") implies that the user can express anything and the system will handle it. In practice, vague inputs ("something in tech, maybe software, I'm open to remote") will produce poor-quality search results because the agent cannot disambiguate. The implied promise (conversational flexibility) exceeds the system's reliable capability. (3) Minimum viable interface: a structured input form with fields for: target role (text field), location or remote preference (dropdown + text), years of experience (numeric or range), must-have skills (multi-select or comma-separated), must-not-have criteria (optional text field). A processing status panel showing which stage the agent is in ("Searching job boards," "Reading listings," "Generating match report"). A structured report output with confidence labeling per match (high match / partial match / low match based on criteria coverage). These three elements (scoped input affordance, visible processing state, confidence-represented output) constitute the minimum viable interface.

**Common error:** Recommending Gradio because "the free-form prompt box feels more natural for a job search." The chapter's criterion is use case alignment, not user-interface aesthetics — the tool is a production job-match pipeline, not a demo.

*Chapter reference:* Chapter 23, "Streamlit vs. Gradio"; Chapter 22, "Four Patterns of AI Intelligence."

---

**Exercise 12** *(Scenario-Based Application)*

Riya is building a Creator-archetype generative music tool that takes a text description of a mood and generates a short musical piece. She has chosen Gradio for the interface because "users can try different prompts and experiment." She is planning to use a single free-form text box with no other guidance.

Conduct an abbreviated alignment audit (interaction model layer and brand surface layer only) for Riya's planned interface. Identify the implicit promises each layer makes, the system reality, whether there is a misalignment, and if so, what type.

*(Tests: alignment audit — interaction model + brand surface layers)*

**Answer:**
**Interaction model layer:**
- Implicit promise: A single free-form text box with no guidance implies the system can process any textual description and will produce a useful musical output. There is no signal about what kinds of descriptions work best, what length or specificity is needed, or what the system cannot handle.
- System reality: Generative music models produce better results with specific mood descriptors, genre cues, and tempo indicators than with vague or unstructured descriptions. A user who types "something sad but hopeful" may get a less useful result than a user who types "melancholy piano, 70 BPM, minor key with a major resolution." The system's capability is not uniformly responsive to any free-form input.
- Misalignment type: Capability misalignment — the interaction model promises broader, more uniformly capable input handling than the system reliably delivers.
- Fix: Add a brief prompt guide below the text box ("Include: mood, genre, tempo, instruments") and provide two to three example inputs with their outputs so users can calibrate their expectations.

**Brand surface layer:**
- Implicit promise: A Creator-archetype tool promises originality, expressiveness, and generative partnership — the experience of co-creating something unexpected. The brand surface should feel alive, exploratory, and encouraging of experimentation.
- System reality: A Gradio default interface with no styling communicates "this is a demo" rather than "this is a creative tool." The default Gradio visual surface and tone do not match the Creator archetype's brand surface promise.
- Misalignment type: Tone misalignment — the interface's personality (minimal, utilitarian, demo-adjacent) does not match the brand surface's promise (creative, expressive, original).
- Fix: Customize the Gradio interface with a visual and linguistic tone that matches the Creator archetype — evocative language in the interface copy, a visual surface that feels generative and creative rather than minimal.

**Common error:** Conducting the audit by listing problems without distinguishing between misalignment types and between layers. A well-formed audit names the specific layer, the specific implicit promise, the specific system reality, and the specific misalignment type.

*Chapter reference:* Chapter 23, "Conducting an Alignment Audit."

---

**Exercise 13** *(Application)*

The chapter warns that "a silent system is a broken system from the user's perspective." Explain in 2–3 sentences what this means for the deployment of a multi-agent pipeline, and describe two specific implementation choices that address this requirement.

*(Tests: minimum viable interface — visible processing state)*

**Answer:** A silent system — one that accepts input and provides no feedback about what it is doing while processing — is indistinguishable from a frozen or broken system from the user's perspective. For a multi-agent pipeline, this is especially significant because agent pipelines take 30–90 seconds to run (or more), which is far outside the user's typical expectation for a web application response. Without visible processing state, the user cannot know whether the system is working, stuck, or has failed — and will often refresh the page or assume failure, causing the pipeline to restart unnecessarily or for the user to disengage. Two specific implementation choices: (1) Agent status panel — a Streamlit component that updates in real time to show which agent is currently running (e.g., "Step 1 of 3: Research agent gathering sources..."), estimated progress, and which steps are complete. This requires streaming the n8n or CrewAI pipeline status to the Streamlit frontend via a polling endpoint or websocket. (2) Processing timestamp — a visible display of when processing started and how long it has been running ("Started 0:42 ago"), so users can distinguish "still processing" from "frozen." Combined with a clear success state when the pipeline completes, this creates the minimum visible processing state the minimum viable interface requires.

**Common error:** Describing visible processing state as only a UX nicety (a "nice to have" for the user experience). The chapter frames it as a required element of the minimum viable interface — its absence is a misalignment between the deployment surface's promise (the tool is working) and the user's experience (silence).

*Chapter reference:* Chapter 23, "Minimum Viable Interface — visible processing state."

---

**Exercise 14** *(Application)*

The chapter describes confidence misalignment as "the interface promises more certainty than the model has." For each of the following output designs, assess whether confidence is represented accurately, and if not, describe the specific misalignment and the fix.

(a) A research assistant tool produces a bulleted list of five findings, each with a source URL, formatted identically regardless of whether the source URL was found by search or inferred by the model.
(b) A competitive intelligence tool produces a structured JSON report with three fields per finding: `claim`, `source_url`, and `confidence: "verified" | "inferred" | "unverifiable"`. The UI renders all three fields, including the confidence label, with a color coding (green/yellow/red).
(c) A news summarization tool produces a two-paragraph summary in a confident, declarative voice with no hedging language, pulled from articles that may be up to 72 hours old.

*(Tests: minimum viable interface — output surface representing confidence accurately)*

**Answer:** (a) Confidence misalignment — formatting identically regardless of source origin implies the same certainty for search-found and model-inferred findings. Fix: add a source type indicator to each finding (e.g., a verified checkmark for search-found sources vs. an inference flag for model-generated claims), and include a visible key explaining the distinction. Alternatively, use the structured null-field pattern: if a source URL cannot be retrieved, the field is `null` with an explanatory note, not a model-generated placeholder URL. (b) Accurately represents confidence — the three-way confidence label with color coding surfaces uncertainty directly in the UI, and the JSON schema makes uncertainty machine-readable and human-visible simultaneously. This matches the chapter's Pattern 2 (structured output with null fields) and Pattern 3 (confidence labeling) anti-hallucination guard patterns. (c) Confidence misalignment — a confident, declarative summary in present tense implies current, verified information, but the underlying articles may be up to 72 hours old — outdated in a fast-moving news context. Fix: add a visible data currency note ("Based on articles published within the last 72 hours — verify breaking news before acting"), and use hedging language when summarizing rapidly evolving situations ("As of [date], reports indicate...").

**Common error:** Labeling (c) as accurate because "the tool says it summarizes articles, not that the articles are current." The chapter's confidence misalignment framework focuses on the implicit promises the interface makes — a two-paragraph declarative summary implicitly promises current information in a news context, regardless of what the product description says.

*Chapter reference:* Chapter 23, "Minimum Viable Interface — output surface representing confidence accurately."

---

## Tier 3 — Synthesis (Exercises 15–16)

*Bloom's Level: Analyze / Evaluate*
*Purpose: Connect this chapter's concepts to a concept from a prior chapter.*

---

**Exercise 15** *(Cross-Chapter Synthesis)*

In Chapter 21, you learned about *degraded modes* — the argument that a production pipeline must be designed with an explicit fallback for each failure scenario, so the system never simply stops when something breaks. The chapter provides four degraded mode examples: cached last-good-run, human-in-the-loop pause, partial result, and static fallback. In this chapter, you are working with *the deployment surface's implicit promise* — that the system will be available and functional at the URL where users encounter it.

A team's Streamlit app is running in production at a public URL. Their multi-agent pipeline calls an n8n webhook that coordinates three agents. Occasionally, the n8n instance becomes briefly unavailable (1–3 minutes), and the Streamlit app currently shows a generic "500 Internal Server Error" page when this happens.

Apply both chapters' frameworks to redesign the app's failure behavior. What degraded mode is most appropriate for this failure scenario, and how does that choice express or protect the deployment surface's implicit promise?

*This question connects degraded modes (Chapter 21) to the deployment surface implicit promise (Chapter 23).*

*What distinguishes a surface answer from a strong one:*
- A strong answer names a specific degraded mode from the chapter's list and explains why it is appropriate for this specific failure scenario
- A strong answer explains how the generic 500 error breaks the deployment surface's implicit promise and what specifically the degraded mode restores
- A strong answer notes the alignment between how the failure is communicated to the user and the brand surface's implicit promise

*(Tests: degraded modes + deployment surface implicit promise — Ch. 21 + Ch. 23)*

**Answer:** The most appropriate degraded mode for a 1–3 minute n8n unavailability is the partial result or human-in-the-loop pause pattern, depending on the system's run duration. If the pipeline runs in under 30 seconds, a human-in-the-loop pause with a visible status message is most appropriate: "Our processing pipeline is briefly unavailable (usually less than 3 minutes). Your request has been queued — the page will refresh when processing resumes." This communicates the failure honestly, tells the user what to do (wait), and sets a realistic expectation (3 minutes). The deployment surface's implicit promise is: "This tool is available at this URL." A generic 500 error breaks this promise in two ways: (1) it signals a system failure rather than a brief unavailability, which implies the tool may not work at all; (2) it gives the user no useful action to take. The 500 page does not make the deployment surface's promise recoverable — it simply withdraws it. The degraded mode restores the promise by keeping the system responsive (even if not functional) and giving the user accurate information about the failure's expected duration. Brand surface consideration: the language of the status message must match the tool's archetype. A Sage-archetype tool ("Briefly unavailable — estimated recovery: under 3 minutes") sounds different from a Creator-archetype tool ("We'll be right back — hold tight while we get things running again") — both communicate the same information but with different tonal promises.

*What a surface answer looks like:* "Use cached last-good-run when n8n is unavailable." This mentions a degraded mode but does not explain why it is or is not appropriate for this specific scenario (1–3 minute outage) or how it addresses the deployment surface promise.

*Common error:* Recommending static fallback (display a pre-written example output) for a 1–3 minute outage. Static fallback is appropriate when the system is fundamentally unavailable for an extended period, not for brief, predictable outages — and presenting a static output without clear labeling would violate confidence alignment.

*Chapter reference:* Chapter 23, "The Four Interface Layers — deployment surface"; Chapter 21, "Four Degraded Modes."

---

**Exercise 16** *(Cross-Chapter Synthesis)*

In Chapter 19, you learned about *coherence audits* — the framework for checking whether all visible outputs of a brand are consistent with one another and with the brand's core promise. The chapter describes the Airbnb IPO deck's three coherence properties: every visual element advances the narrative; every metric is presented in a way that is consistent with the brand's values; there are no internal contradictions between what the deck claims and what the deck shows. In this chapter, you are working with the *alignment audit* — the pre-launch check that maps implicit interface promises to system reality across four interface layers.

Compare the coherence audit and the alignment audit. In what ways are they the same discipline applied to different artifacts? In what specific way does the alignment audit extend beyond coherence — what can it detect that a coherence audit cannot?

*This question connects coherence audits (Chapter 19) to the alignment audit (Chapter 23).*

*What distinguishes a surface answer from a strong one:*
- A strong answer names the genuine shared discipline precisely — not just "both check consistency"
- A strong answer identifies what the coherence audit checks (internal consistency of visible outputs) and what the alignment audit checks (consistency between interface promises and system reality)
- A strong answer shows the extension: the alignment audit checks across the boundary between what users see and what the system actually does — the coherence audit cannot see this because it only examines visible outputs

*(Tests: coherence audit + alignment audit — Ch. 19 + Ch. 23)*

**Answer:** Shared discipline: both audits are diagnostic tools that compare two things — the coherence audit compares visible outputs to each other (are they internally consistent?), and the alignment audit compares visible promises to system reality (are interface promises consistent with what the system delivers?). Both audits are pre-publication or pre-launch, conducted before the artifact reaches its audience. Both produce a gap list, not a solution list — the output of each audit is a description of the discrepancies found, which the team then addresses. The extension: the alignment audit checks across the boundary between user-visible interface and system behavior, which the coherence audit cannot reach. The coherence audit can verify that the visual surface looks polished, that the interaction model language is consistent with the brand surface tone, and that the README's project description matches the demo's capabilities — all within the visible layer. What it cannot see is whether a polished, internally consistent interface is making promises about system behavior that the system cannot keep. A Google Bard interface can be perfectly internally coherent — the visual surface matches the brand, the interaction model is consistent, the tone is confident and helpful — and still produce the JWST confidence misalignment because the system's actual certainty level is lower than the interface implies. The alignment audit is the only check that crosses the interface boundary and examines what the system does, not just what the interface says.

*Common error:* Treating both audits as "the same thing applied to different contexts." A strong answer names the specific extension — the alignment audit's ability to detect mismatches between visible promises and invisible system behavior — rather than just noting that they differ in scope.

*Chapter reference:* Chapter 23, "Conducting an Alignment Audit"; Chapter 19, "The Coherence Audit."

---

## Tier 4 — Challenge (Exercise 17)

*Bloom's Level: Evaluate / Create*
*Purpose: Transfer beyond what was explicitly taught.*

---

**Exercise 17** *(Transfer Challenge)*

The chapter treats the three misalignment types (confidence, capability, tone) as problems to be diagnosed and fixed. But consider this counterargument: some successful AI products have deliberately used interface signals that slightly exceed the system's actual capability — presenting uncertain outputs with more confidence than they technically deserve, or framing a narrow capability as broadly applicable — and these products succeeded because users' perception of capability was shaped by the interface's promise, not by the system's measured performance.

Is deliberate misalignment ever a legitimate product design strategy? If so, under what specific conditions? If not, why not — and what specifically goes wrong when the gap between implicit promise and system reality is intentional rather than accidental?

*A strong response will address:*
- What distinguishes accidental misalignment from deliberate misalignment as a product strategy
- Whether there is a category of cases where deliberate overstatement of capability is defensible vs. indefensible
- What the long-run brand consequence of deliberate confidence misalignment is, and whether the chapter's framework can model this consequence

*(Tests: alignment audit and three misalignment types — extended to deliberate misalignment as a product strategy)*

---

## Answer Key

> Attempt all exercises before reading this section.
> For Tier 3 and Tier 4, your answer does not need to match the model exactly — use the "what a strong answer includes" criteria to evaluate your own response.

---

**Worked Example**
*No answer needed — the worked example is its own model.*

---

**Ex 1** — *Four interface layers*
*Model answer:* Visual surface: polish/craft promise. Interaction model: input affordance matches system scope. Deployment surface: available and functional at the URL. Brand surface: personality, tone, and output style consistent with archetype.
*Common error:* Treating all four as visual design choices.
*Chapter reference:* Ch. 23, "The Four Interface Layers."

---

**Ex 2** — *Three misalignment types*
*Model answer:* Confidence (Bard/JWST: wrong certainty level in output presentation). Capability (Tay/adversarial: interface promised a scope the system could not handle). Tone (Snapchat redesign: interface broke the tone contract users had built habits around).
*Common error:* Labeling Tay as confidence misalignment.
*Chapter reference:* Ch. 23, "Three Types of Interface Misalignment."

---

**Ex 3** — *Streamlit vs. Gradio*
*Model answer:* Streamlit = "do work." Gradio = "try the model." (a) Gradio (evaluating/demo). (b) Streamlit (production workflow). (c) Gradio (model sharing/evaluation). (d) Streamlit (production workflow).
*Common error:* Choosing Gradio for (b) because "it is simpler."
*Chapter reference:* Ch. 23, "Streamlit vs. Gradio."

---

**Ex 4** — *Minimum viable interface*
*Model answer:* (1) Input affordance matching system scope — signals what the system can take and prevents out-of-scope requests. (2) Visible processing state — distinguishes "processing" from "frozen." (3) Output surface representing confidence accurately — prevents confidence misalignment.
*Common error:* Describing as a visual design standard.
*Chapter reference:* Ch. 23, "Minimum Viable Interface."

---

**Ex 5** — *README as interface — six elements*
*Model answer:* (1) Deployed URL, (2) What it does, (3) How to use it, (4) Known limits, (5) Architecture, (6) Tech stack. URL first because the reader wants to know if the thing works before knowing what it is — the URL is the most important piece of information and should be immediately accessible.
*Common error:* Placing "What it does" first.
*Chapter reference:* Ch. 23, "README as Interface."

---

**Ex 6** — *Alignment audit — definition*
*Model answer:* Produces a two-column comparison table: implicit promises vs. system reality. Diagnostic, not prescriptive. Run before shipping (or when system capabilities change after launch).
*Common error:* Treating as post-launch QA or as a list of design changes.
*Chapter reference:* Ch. 23, "Conducting an Alignment Audit."

---

**Ex 7** — *Four interface layers + three misalignment types*
*Model answer:* (a) Visual surface + confidence: fix = uncertainty markers and data currency note. (b) Brand surface + tone: fix = improve model quality or calibrate brand surface language. (c) Deployment surface + capability: fix = health-check monitor and status indicator. (d) Interaction model + capability: fix = structured input with visible constraints.
*Common error:* Labeling all four as capability misalignment.
*Chapter reference:* Ch. 23, "Three Types of Interface Misalignment" and "The Four Interface Layers."

---

**Ex 8** — *README error analysis*
*Three problems:* No public deployed URL (localhost). Wrong ordering (tech stack before what/how/limits). Known limits buried.
*Corrected README format:* Deployed URL first, what/how/limits/architecture/tech stack in order.
*Chapter reference:* Ch. 23, "README as Interface."

---

**Ex 9** — *AI Interaction — alignment audit*
*Model answer:* Strongest: visible processing state mentioned. Gap: AI described generic UX testing, not the chapter's two-column implicit-promise vs. system-reality table organized by four layers and three misalignment types. Verification: audit is complete when all four layers have both columns filled and gaps are classified by type; second test is to have a new user describe what they think the system can do.
*Chapter reference:* Ch. 23, "Conducting an Alignment Audit."

---

**Ex 10** — *README as interface — implicit promises*
*Model answer:* README shapes the reader's expectation framework before they interact with the product. Example of an implicit promise broken without bad words: `localhost:8501` as the "live demo" URL — not false, but promises access the evaluator cannot have.
*Common error:* Describing only explicit claims as README promises.
*Chapter reference:* Ch. 23, "README as Interface."

---

**Ex 11** — *Cumulative: Streamlit vs. Gradio + four AI intelligence patterns*
*Model answer:* Streamlit appropriate (do-work use case). Free-form prompt box = capability misalignment (implies conversational flexibility, system works best with structured inputs). Minimum viable interface: structured form (role, location, experience, skills), processing status panel, structured report with confidence per match.
*Common error:* Recommending Gradio for naturalness of free-form input.
*Chapter reference:* Ch. 23, "Streamlit vs. Gradio"; Ch. 22, "Four Patterns of AI Intelligence."

---

**Ex 12** — *Alignment audit — interaction model + brand surface*
*Model answer:* Interaction model: free-form box implies uniformly capable processing → capability misalignment → fix: add prompt guide with example inputs. Brand surface: Gradio default styling implies demo, not creative tool → tone misalignment → fix: customize visual and language tone to match Creator archetype.
*Common error:* Listing problems without naming layer and misalignment type.
*Chapter reference:* Ch. 23, "Conducting an Alignment Audit."

---

**Ex 13** — *Visible processing state*
*Model answer:* A silent system is indistinguishable from a frozen system — especially critical for multi-agent pipelines with 30–90 second run times. Two implementations: agent status panel (which agent is running, progress) and processing timestamp (time elapsed since start).
*Common error:* Treating visible processing state as a UX nicety rather than a required minimum viable interface element.
*Chapter reference:* Ch. 23, "Minimum Viable Interface — visible processing state."

---

**Ex 14** — *Output surface representing confidence accurately*
*Model answer:* (a) Misalignment — formatting identically for search-found and model-inferred findings implies identical certainty. Fix: source type indicator or null-field schema. (b) Accurate — structured JSON with confidence labeling and color coding makes uncertainty visible and machine-readable. (c) Misalignment — declarative summary implies current information; 72-hour-old articles may be outdated. Fix: data currency note and hedging language for evolving situations.
*Common error:* Labeling (c) as accurate because the product description mentions articles.
*Chapter reference:* Ch. 23, "Minimum Viable Interface — output surface representing confidence accurately."

---

**Ex 15** — *Synthesis: degraded modes + deployment surface*
*Model answer:* Human-in-the-loop pause most appropriate for 1–3 minute outage — keep system responsive with visible status message ("briefly unavailable, usually under 3 minutes, request queued"). Generic 500 error breaks deployment surface promise by implying system failure rather than brief outage. Brand surface: status message language matches archetype.
*What a strong answer includes:* Named specific degraded mode with rationale; explained specifically how 500 error breaks deployment surface promise; noted brand surface alignment in failure communication.
*Common error:* Recommending static fallback for a brief outage.
*Chapter reference:* Ch. 23, "Deployment surface"; Ch. 21, "Four Degraded Modes."

---

**Ex 16** — *Synthesis: coherence audit + alignment audit*
*Model answer:* Shared discipline: diagnostic comparison of two things before publication. Both produce gap lists, not solution lists. Extension: alignment audit crosses the interface boundary to examine what the system does vs. what the interface implies — coherence audit only examines visible outputs' internal consistency. A perfectly coherent interface can still produce confidence misalignment if the system's behavior does not match what the interface implies.
*Common error:* Treating both as "the same thing in different contexts" without naming the extension.
*Chapter reference:* Ch. 23, "Conducting an Alignment Audit"; Ch. 19, "The Coherence Audit."

---

**Ex 17 — Challenge**
*No model answer provided.*
*A strong response will address:*
- Accidental vs. deliberate misalignment: accidental is a design oversight; deliberate is a strategy that depends on users not detecting the gap
- Possibly defensible conditions: early-stage demos where the implicit promise of the interface is calibrated for "what this will be," not "what this is now" — but only when this framing is explicit
- Indefensible: when the deliberate gap leads users to make consequential decisions based on overstated capability (medical, financial, safety-critical contexts)
- Long-run brand consequence: the chapter's three failure mode cases (Bard, Tay, Snapchat) all represent scenarios where the gap between promise and reality became visible. When deliberate misalignment is discovered, the trust collapse is more severe than accidental misalignment because users understand they were deliberately misled
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
