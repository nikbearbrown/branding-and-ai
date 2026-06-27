# Chapter Quiz: Interface Design and Deployment

*Chapter 23 (Appendix S4) of Branding and AI: Building the Creative Engineer*

> **Instructions:** Attempt every question before checking the answer key.
> Do not look at the answers while working — the act of retrieval is the
> learning. If you are unsure, make your best attempt and mark it with (?).
> Review the answer key after completing all questions, not after each one.

---

## Learning Objectives Covered

This quiz assesses the following chapter objectives:

- Identify the four interface layers and explain the failure mode when each is misaligned with the underlying system
- Classify an interface failure as confidence misalignment, capability misalignment, or tone misalignment
- Run the alignment audit on a set of interface claims and identify which require fixes before deployment
- Select between Streamlit and Gradio based on the user's primary job with the tool
- Apply the minimum viable interface discipline to an AI tool and identify prohibited elements

---

## Section 1 — Recall and Recognition (Questions 1–5)

*Target: Bloom's Remember / Understand*
*Format: Multiple-choice (3 options) and True/False*
*Target difficulty: p = 0.77–0.85*

---

**Question 1** *(Multiple-Choice)*

The chapter identifies four interface layers. Which answer correctly names all four?

A) Frontend, backend, API, and database layers.
B) Visual surface, interaction model, deployment surface, and brand surface.
C) HTML, CSS, JavaScript, and accessibility layers.

---

**Question 2** *(True/False)*

The Bard February 2023 case is an example of capability misalignment — Google's interface implied the tool could handle a broader range of tasks than it actually could, as demonstrated by the factually incorrect exoplanet bullet point.

☐ True  ☐ False

---

**Question 3** *(Multiple-Choice)*

The chapter distinguishes Streamlit from Gradio as different interaction models for different use cases. Which answer correctly captures the deciding question?

A) Streamlit is for Python developers; Gradio is for non-technical users who need a no-code interface.
B) If the user's primary job is to do work (configure inputs, run a process, inspect and iterate results), choose Streamlit. If the user's primary job is to try the model (submit an input, see an output, submit another), choose Gradio.
C) Streamlit is better for deployment to Hugging Face Spaces; Gradio is better for deployment to Streamlit Community Cloud.

---

**Question 4** *(Multiple-Choice)*

The chapter names three required components and three prohibited components of a minimum viable interface. Which answer correctly identifies the three required components?

A) A login page, an API status indicator, and a user feedback form.
B) An input affordance that matches the system's actual inputs, a visible processing state, and an output surface that represents confidence accurately.
C) A hero image, a tagline, and a call-to-action button.

---

**Question 5** *(True/False)*

The chapter's alignment audit asks the developer to enumerate five implicit promises the interface makes and then check them against what the underlying system can actually deliver — and the fix for a misaligned claim is always to upgrade the system until it can keep the promise.

☐ True  ☐ False

---

## Section 2 — Application and Analysis (Questions 6–9)

*Target: Bloom's Apply / Analyze*
*Format: Multiple-choice (3 options) and Short-Answer*
*Target difficulty: p = 0.50–0.70*

---

**Question 6** *(Scenario-Based Multiple-Choice)*

A student builds an AI competitor news tool. The interface includes a large text box labeled "Ask anything about your competitive landscape" and a submit button labeled "Get AI Insights." The underlying system is a scoped n8n workflow that processes RSS feeds from a configured list and scores articles for sentiment — it cannot answer open-ended questions. What type of misalignment does this interface exhibit, and what is the fix?

A) Confidence misalignment — the interface should add a disclaimer that AI outputs may sometimes be incorrect.
B) Capability misalignment — the interface implies free-form conversational Q&A the system cannot deliver. The fix is to replace the open text box with structured inputs matching the system's actual scope: a URL field for RSS feeds and a date range selector, with copy that says "Analyze up to 10 RSS feeds for competitive signals" rather than "Ask anything."
C) Tone misalignment — the phrase "Get AI Insights" is too casual for a professional intelligence tool and should be replaced with more formal language.

---

**Question 7** *(Short-Answer)*

The chapter conducts an alignment audit on a sentiment analysis pipeline and finds that five interface claims need to be evaluated. For the claim "Analyzes your competitor news," the system reality is that the tool analyzes publicly available RSS content but cannot access content behind paywalls. What does the audit recommend, and what principle does this illustrate about the relationship between interface fixes and system improvements?

*Your answer:*

_____________________

---

**Question 8** *(Multiple-Choice)*

The Microsoft Tay case (March 2016) is used to illustrate capability misalignment. What was the specific mismatch that caused the brand failure?

A) Tay's responses were too slow for a Twitter audience, leading users to abandon the product before seeing its intended value.
B) The interface — an open Twitter account that anyone could mention — implied a system capable of beneficial public conversation that would improve with interaction. The system had no defenses against adversarial inputs; within sixteen hours, coordinated trolls had used this open architecture to produce offensive outputs.
C) Microsoft used marketing language that overstated Tay's conversational depth, leading users to expect a more sophisticated AI than was actually deployed.

---

**Question 9** *(Short-Answer)*

The chapter describes the README as "the last interface layer — the one the user encounters when they are trying to understand what they just used." Name the six elements of a portfolio-quality README that the chapter specifies, and explain which one the chapter says should appear first and why.

*Your answer:*

_____________________

---

## Section 3 — Synthesis and Evaluation (Questions 10–11)

*Target: Bloom's Evaluate / Create*
*Format: Short-Answer or Brief-Response*
*Target difficulty: p = 0.30–0.50*

---

**Question 10** *(Brief-Response)*

The chapter's "Still Puzzling" section identifies a persistent behavioral pattern: engineers consistently overpromise in first interfaces — buttons imply broader capability than the system delivers, "AI-powered" copy overstates the AI's role, missing uncertainty surfaces. The chapter suspects this is structural: "engineers think about interfaces as presentation layers to be made impressive, not as contracts to be kept." Evaluate this diagnosis. Is the cause structural (a framing problem that persists even after instruction) or is it a knowledge gap (engineers simply do not know the failure modes until they ship and observe them)? What evidence from the chapter supports your position?

*Your response (2–4 sentences):*

_____________________

---

**Question 11** *(Transfer — Brief-Response)*

The chapter's alignment audit logic — enumerate every implicit promise the interface makes, check each against the system's actual capability, fix the interface before deploying rather than fixing the system — is grounded in AI tool development. Apply this same logic to a medical device user interface. A new pulse oximeter displays readings with two decimal places of precision and uses the label "Clinical-Grade Accuracy." The device's actual accuracy specification is ±2% SpO2 under ideal conditions, with higher variance in patients with darker skin pigmentation or poor circulation. Run the alignment audit on these two interface elements and specify the fixes.

*Your response (2–4 sentences):*

_____________________

---

## Answer Key

> Read this section only after completing all questions.

---

**Q1 — B**
*Correct because:* The chapter names four layers explicitly: the visual surface (buttons, forms, layouts, colors), the interaction model (how the user thinks about working with the tool — chat, search, form, dashboard), the deployment surface (what the user encounters before the UI loads — URL, account creation requirement, latency), and the brand surface (the small things that compound — error messages, empty states, confidence signals, tone of copy).
*Why the distractors are wrong:*
- A) Frontend/backend/API/database is a technical stack description, not the chapter's four interface layers.
- C) HTML/CSS/JavaScript/accessibility are implementation technologies within Layer 1, not the four-layer taxonomy.
*Chapter reference:* What "Interface" Actually Means / four layers

---

**Q2 — False**
*Correct because:* The chapter classifies the Bard case explicitly as confidence misalignment: "The interface made a promise. The system broke it." The Bard bullet points were confident assertions presented as authoritative Google-quality information; the system could not support that level of confidence. This is not capability misalignment (which would mean the system could not handle questions about astronomy at all) but confidence misalignment (the interface presented the output with more certainty than the system's actual reliability warranted).
*Chapter reference:* Three Faces of Misalignment / Google Bard / confidence misalignment

---

**Q3 — B**
*Correct because:* The chapter's deciding question is the user's primary job: "do work" (configure, run, inspect, iterate) → Streamlit; "try the model" (input, output, repeat) → Gradio. The mismatch to avoid is deploying an orchestrated multi-agent system (structured, inspectable behavior) behind a Gradio free-form text box (implying exploratory natural-language interaction).
*Why the distractors are wrong:*
- A) The chapter does not distinguish by technical expertise of the user — both frameworks are Python-based.
- C) The chapter describes the opposite: Streamlit deploys to Streamlit Community Cloud, and Gradio deploys to Hugging Face Spaces.
*Chapter reference:* Streamlit and Gradio / choosing the right framework

---

**Q4 — B**
*Correct because:* The chapter names three required components for a minimum viable AI tool interface: an input affordance that matches the system's actual inputs (not a free-text box if the system takes structured inputs), a visible processing state (spinner, progress bar, or status message), and an output surface that represents confidence accurately (confidence scores, "verify with source" footers, handling "I don't know" gracefully).
*Why the distractors are wrong:*
- A) A login page, API status indicator, and feedback form are not the chapter's three required components.
- C) Hero image, tagline, and CTA are marketing elements, not the chapter's minimum viable interface requirements.
*Chapter reference:* Building the Interface / three required components

---

**Q5 — False**
*Correct because:* The chapter states the opposite: "fix the interface now, so the system and the interface are making the same promises. Do not fix the system — that comes later, in the Build-Measure-Learn loop." The alignment audit's purpose is to make the interface honest about what the system actually does, not to mandate system improvements before shipping. Narrowing a claim, adding a qualifier, or adding an uncertainty signal are interface fixes that require no system change.
*Chapter reference:* The Alignment Audit / fix the interface, not the system

---

**Q6 — B**
*Correct because:* A free-text box labeled "Ask anything" implies general conversational competence — a chat interface implies the system can handle open-ended natural-language queries. The underlying system is scoped to RSS feed processing and cannot answer open-ended questions. This is capability misalignment: the interface implies a capability the system does not have. The fix is to match the input affordance to the system's actual inputs — structured fields for URLs and parameters rather than a free-text prompt.
*Why the distractors are wrong:*
- A) Confidence misalignment would be the interface presenting the system's RSS-based outputs as more certain than they are, not implying a different kind of capability entirely.
- C) Tone misalignment would be the copy's register not matching the system's output style — "Get AI Insights" might be casual, but the structural problem is capability, not tone.
*Chapter reference:* Three Faces of Misalignment / capability misalignment / Building the Interface

---

**Q7 — Short-Answer**
*Model answer:* The alignment audit recommends narrowing the claim to match system reality: the claim "Analyzes your competitor news" should become "Analyzes publicly available RSS content from your configured feeds" — removing the implication that the system can access paywalled content. The audit explicitly does not recommend fixing the system to access paywalled content; it recommends fixing the interface to be honest about the system's actual scope. This illustrates the principle that the alignment audit is a promise-calibration exercise, not a system-requirements exercise: the job is to make the interface and the system make the same promises, and the interface is cheaper and faster to adjust than the system. This is the chapter's explicit instruction: "Do not fix the system — that comes later, in the Build-Measure-Learn loop. Fix the interface now."
*What a strong answer includes:*
- The specific narrowed claim
- The principle that interface is fixed, not system
- The connection to the Build-Measure-Learn loop timing
*Chapter reference:* The Alignment Audit / worked example

---

**Q8 — B**
*Correct because:* The chapter describes Tay's failure as capability misalignment: "The interface implied a system capable of beneficial public conversation that would improve with interaction. The system could not." The specific structural mismatch was that an open Twitter architecture — anyone could mention Tay and receive a response — implied defenses against adversarial use that the system did not have. The design lesson: "test the interface against the population that will actually use it, not the population you wish would use it."
*Why the distractors are wrong:*
- A) Response latency is not the chapter's identified cause of the Tay failure.
- C) Marketing language overstating conversational depth is confidence misalignment; the Tay failure was about what users could do to the system, not about stated performance claims.
*Chapter reference:* Three Case Studies / Microsoft Tay / capability misalignment

---

**Q9 — Short-Answer**
*Model answer:* The six elements of a portfolio-quality README are: (1) what the tool does (one paragraph, no marketing language — inputs, outputs, who it's for); (2) how to use it (step-by-step, as if the user has never seen the tool); (3) its limits (explicit — what it does not do, what inputs it handles poorly, output confidence); (4) the architecture diagram (a figure showing the pipeline flow); (5) the technology stack (Streamlit or Gradio, LLM API, n8n, storage); and (6) the deployed URL. The chapter specifies that the deployed URL should appear first — "at the top, before anything else" — because "the user should not have to read four paragraphs to find the link." The first element the user needs is the URL to access the product; putting it first respects that.
*What a strong answer includes:*
- All six elements named
- The deployed URL goes first
- Why it goes first (user's first need is the link)
*Chapter reference:* Deployment / The README as Interface / six elements

---

**Q10 — Brief-Response**
*Model answer:* The chapter's diagnosis points toward structural cause: "I have not yet found a teaching intervention that successfully installs the contract framing before the first interface is built rather than after the first interface fails." If it were a knowledge gap, explaining the failure modes in advance would be sufficient — students would learn the patterns and apply them. But the chapter suggests the problem persists even after instruction because engineers' default frame (presentation layers are for impressiveness) is deeply ingrained and is not overwritten by conceptual knowledge alone. Evidence from the chapter that supports the structural diagnosis: the behavior is described as "universal enough" to suspect structural causes, and the chapter's Still Puzzling section is about why the teaching intervention does not work, which implies the knowledge has been transmitted but the framing has not changed. A knowledge-gap diagnosis would predict the problem is solved by the chapter itself; the chapter's own doubt about its effectiveness suggests the cause runs deeper.
*What a strong answer includes:*
- A position on structural vs. knowledge-gap cause
- Evidence from the chapter supporting that position
- The framing distinction (presentation vs. contract) as the structural element
*Chapter reference:* Still Puzzling / structural cause of interface overpromise

---

**Q11 — Transfer Brief-Response**
*Model answer:* Running the alignment audit: The "two decimal places of precision" claim implies measurement accuracy to the hundredths — an implicit promise of precision that the ±2% specification does not support (2% error is 2 percentage points, not 0.01 percentage points). The fix is to display readings to one decimal place maximum, or to add a visible ±2% indicator, making the precision claim match the system's actual specification. The "Clinical-Grade Accuracy" label makes an implicit promise that the accuracy is uniform across patient populations — a promise the system cannot keep for patients with darker skin pigmentation or poor circulation. The fix is either to remove the clinical-grade label and replace it with the actual specification ("±2% SpO2 accuracy in typical conditions, may vary for some patients — verify with clinical assessment") or to limit deployment contexts to those where the accuracy specification holds. The principle the chapter establishes — fix the interface, not only the system — applies here as a harm-reduction discipline: narrowing the claim is faster than redesigning the sensor, and an honest label prevents clinical decisions being made on false precision assumptions.
*What a strong answer includes:*
- Analysis of both interface claims against system reality
- Specific fixes for each that do not require system redesign
- The harm-reduction implication in a medical context
*Chapter reference:* The Alignment Audit / worked example / three misalignment types (transfer application)

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

- Misclassifying Bard's February 2023 error as capability misalignment (it could not answer astronomy questions) rather than confidence misalignment (it answered with more certainty than its reliability warranted).
- Treating the alignment audit fix as a system improvement requirement rather than an interface narrowing exercise.
- Choosing Streamlit vs. Gradio by personal familiarity rather than by the user's primary job with the tool.

**Signs a student needs to return to the chapter before this quiz:**

- Cannot name all four interface layers and their distinct failure modes.
- Does not understand why the alignment audit's recommendation is to fix the interface rather than the system.

**Scaffolding adjustments:**

- *For students who score below 5:* Work through the alignment audit on the chapter's five-claim sentiment pipeline example before attempting any original analysis — the worked example makes the two-column audit structure concrete.
- *For students who score 11/11 on first attempt:* Ask them to run the alignment audit on their own deployed tool — enumerate five implicit promises the interface makes, check each against the actual system behavior, identify which need fixes, and implement at least one fix with documentation of what changed.
