# Chapter Quiz: Product Requirements and Scope

*Chapter 20 (Appendix S1) of Branding and AI: Building the Creative Engineer*

> **Instructions:** Attempt every question before checking the answer key.
> Do not look at the answers while working — the act of retrieval is the
> learning. If you are unsure, make your best attempt and mark it with (?).
> Review the answer key after completing all questions, not after each one.

---

## Learning Objectives Covered

This quiz assesses the following chapter objectives:

- Distinguish the "what" from the "how" in a PRD and identify when the how has been smuggled into the what
- Write a problem statement with a specific user, specific task, specific frequency, and specific cost
- Explain what "minimum viable product" actually means using the three key terms: version, validated, learning
- Interpret the Linear "$100,000 no" as a product discipline and explain its compound effects over time
- Identify the four sections of a one-page PRD and the failure mode of each

---

## Section 1 — Recall and Recognition (Questions 1–5)

*Target: Bloom's Remember / Understand*
*Format: Multiple-choice (3 options) and True/False*
*Target difficulty: p = 0.77–0.85*

---

**Question 1** *(Multiple-Choice)*

The chapter states that a PRD specifies the "what," not the "how." Which of the following correctly illustrates a "how" smuggled into a "what"?

A) "The tool sends users a daily email summary."
B) "The tool scores articles for sentiment using GPT-4o-mini with a temperature of 0.2 and a custom system prompt that rates each article on a five-point scale."
C) "The tool writes a daily summary to a Google Sheet the user already owns."

---

**Question 2** *(True/False)*

According to the chapter, the word "minimum" in "minimum viable product" means building the least possible — the smallest number of features — regardless of whether the reduced scope still allows the core hypothesis to be tested.

☐ True  ☐ False

---

**Question 3** *(Multiple-Choice)*

The chapter defines MVP using three key terms from Eric Ries's definition. Which answer correctly identifies all three and their specific meaning in the MVP context?

A) Speed (ship fast), simplicity (remove all complexity), and scalability (design for growth from day one).
B) Version (the MVP is a real product, not a mock), validated (the learning came from what users did, not what they said), and learning (the purpose is to test an assumption, not simply to ship).
C) Measurement (track all metrics), iteration (update weekly), and feedback (collect user responses through surveys).

---

**Question 4** *(Multiple-Choice)*

The chapter presents the Linear case as an illustration of "scope discipline as identity." What specifically does Linear refuse, and what is the compound effect of that refusal?

A) Linear refuses to ship new features without extensive user research — this slows development but produces higher-quality features.
B) Linear has repeatedly declined enterprise customization requests — including configurations worth significant annual contracts — that would conflict with its product philosophy, and this discipline preserves the coherence of the experience that engineers love, which becomes Linear's identity and brand.
C) Linear refuses to compete on price, maintaining premium pricing as a signal of quality in the project management category.

---

**Question 5** *(True/False)*

The chapter's "$100,000 no" means refusing any feature that would cost more than $100,000 to implement, as a cost-discipline filter for the MVP boundary.

☐ True  ☐ False

---

## Section 2 — Application and Analysis (Questions 6–9)

*Target: Bloom's Apply / Analyze*
*Format: Multiple-choice (3 options) and Short-Answer*
*Target difficulty: p = 0.50–0.70*

---

**Question 6** *(Scenario-Based Multiple-Choice)*

A student building an AI writing tool for medical documentation has written the following problem statement: "Healthcare professionals need better documentation tools." Using the chapter's problem statement criteria, what is wrong with this statement and what would a strong version include?

A) The statement is too long and should be condensed to one sentence: "Doctors need AI writing help."
B) The statement is too abstract — it has no specific user (which healthcare professionals? in what setting?), no specific task (what type of documentation?), no frequency (how often?), and no cost (what does the documentation burden actually cost them in time or quality?). A strong version would specify: which professional type, which documentation task, how often it occurs, and what the actual consequence of the current process is.
C) The statement focuses on technology rather than business outcomes — it should reference revenue impact rather than operational processes.

---

**Question 7** *(Short-Answer)*

The chapter identifies four sections of a one-page PRD, each with a characteristic failure mode. Name all four sections, state the question each answers, and name the failure mode for at least two of them.

*Your answer:*

_____________________

---

**Question 8** *(Multiple-Choice)*

The chapter's Build-Measure-Learn loop requires that the hypothesis be testable within the MVP window. Which of the following hypotheses is testable in that sense, and why?

A) "Our tool will become the category-defining competitor intelligence platform for SMBs" — this is testable because market leadership can be assessed at any time.
B) "Marketing managers will open a daily Google Sheet of scored competitor news at least three times per week after the first two weeks of use" — this is testable because it has a measurable behavioral outcome, a specific timeframe, and a falsifiable threshold.
C) "Users will prefer our tool to existing alternatives" — this is testable because preference surveys can be administered after any beta period.

---

**Question 9** *(Short-Answer)*

The chapter argues that the MVP boundary is what makes the Build-Measure-Learn loop fast, and that "a PRD that puts too much in v1 takes six months to ship — you learn nothing for six months." Explain the strategic cost of delayed learning using the chapter's competitor comparison argument.

*Your answer:*

_____________________

---

## Section 3 — Synthesis and Evaluation (Questions 10–11)

*Target: Bloom's Evaluate / Create*
*Format: Short-Answer or Brief-Response*
*Target difficulty: p = 0.30–0.50*

---

**Question 10** *(Brief-Response)*

The chapter's "Still Puzzling" section identifies the moment when scope discipline tips from useful constraint to creative restriction — a student without a coherent point of view practicing the $100,000 no can end up refusing features for no good reason. Evaluate what distinguishes productive scope discipline from sterile refusal. What is the underlying principle that makes Linear's refusals productive and would make a random student refusal potentially meaningless?

*Your response (2–4 sentences):*

_____________________

---

**Question 11** *(Transfer — Brief-Response)*

The chapter frames the PRD as "a contract with future-you: a record of the decisions you made when you were thinking clearly, preserved for the moment when you are thinking under pressure." Apply this contract logic to a non-product context: a researcher designing a six-month study. The researcher must make early decisions (study design, sample criteria, data collection methodology) that will constrain what can be validly concluded later, even under pressure from advisors or findings that suggest expanding scope. What is the equivalent of the "$100,000 no" in a research design context, and why does writing it down in advance matter?

*Your response (2–4 sentences):*

_____________________

---

## Answer Key

> Read this section only after completing all questions.

---

**Q1 — B**
*Correct because:* The chapter uses this exact example to illustrate "how" smuggled into "what." "The tool scores articles for sentiment using GPT-4o-mini with a temperature of 0.2 and a custom system prompt" specifies implementation decisions — model choice, temperature setting, and prompt structure — that belong to engineering, not to the PRD.
*Why the distractors are wrong:*
- A) "The tool sends users a daily email summary" is a clean "what" statement — it says nothing about the email infrastructure, scheduler, or renderer.
- C) "Writes a daily summary to a Google Sheet the user already owns" is a what statement — it specifies the output destination without dictating the implementation of how data gets written.
*Chapter reference:* What a PRD Actually Is / what vs. how distinction

---

**Q2 — False**
*Correct because:* The chapter states: "'Minimum' doesn't mean 'the least possible.' It means 'the smallest thing that produces validated learning.'" The chapter warns that an out list that is too long — removing things genuinely necessary for the core experience — means users will be blocked from the behavior you are trying to measure, making the measure step invalid.
*Chapter reference:* What "Minimum Viable Product" Actually Means / definition of minimum

---

**Q3 — B**
*Correct because:* The chapter quotes Ries's definition and then explains the three key words: version (a real product, not a mock or prototype, because validated behavior requires real stakes and real workflow), validated (the learning came from what users did, not what they said, because users reliably tell you they will do things they will not do), and learning (the purpose is to test a specific assumption — if you do not know what you are testing, you cannot interpret the results).
*Why the distractors are wrong:*
- A) Speed, simplicity, and scalability are not Ries's three terms and are not the chapter's definition.
- C) Measurement, iteration, and feedback are related lean concepts but are not the chapter's three key terms in the MVP definition.
*Chapter reference:* What "Minimum Viable Product" Actually Means / version, validated, learning

---

**Q4 — B**
*Correct because:* The chapter describes Linear repeatedly declining enterprise customization requests worth significant annual contracts because they would conflict with the product philosophy. The compound effect is that each refusal preserves the coherence of the experience engineers love, and that coherence becomes the brand: "the identity becomes the brand. The brand attracts more users who value that specific coherence, which deepens it further."
*Why the distractors are wrong:*
- A) User research requirements are not the chapter's description of Linear's refusal discipline.
- C) Pricing strategy is not what the chapter's Linear case is about.
*Chapter reference:* Scope Discipline as Identity / The Linear Case / $100,000 no

---

**Q5 — False**
*Correct because:* The chapter defines the $100,000 no as "the feature you would decline even if declining cost you something real" — a feature a real user asks for, with a real argument for why it belongs, that you decline because including it would compromise the core. The $100,000 is illustrative of the cost being real (Linear's enterprise customization was worth significant contract value), not a dollar threshold for implementation cost.
*Chapter reference:* The $100,000 No / definition

---

**Q6 — B**
*Correct because:* The chapter's problem statement criteria require: a specific user (not "healthcare professionals" generally), a specific task, a specific frequency, a specific output, and a specific failure mode. The chapter contrasts "Marketing professionals need better competitive intelligence" (a wish, too abstract) with a version that has "a specific user, a specific task, a specific frequency, a specific output, and a specific failure mode." Option B correctly identifies all the missing components.
*Why the distractors are wrong:*
- A) The problem with the statement is abstraction, not length — condensing it further produces an even more abstract version.
- C) The chapter does not instruct problem statements to focus on revenue impact rather than operational processes; the instruction is to be specific about the user's actual situation.
*Chapter reference:* What a PRD Actually Is / Problem section / failure modes

---

**Q7 — Short-Answer**
*Model answer:* The four sections of a one-page PRD are: (1) Problem — answers "what specific problem are you solving, for whom, and how often does it cost them something?" Failure mode: abstracting the user or describing a symptom instead of a cause. (2) Gap — answers "what already exists to solve this problem, and where does it fall short?" Failure mode: vagueness — naming no actual products or explaining exactly what each gets wrong. (3) Tool — answers "what, exactly, will you build?" Failure mode: marketing language ("an AI-powered platform") that tells the reader nothing buildable and passes the "read it to someone" test by describing nothing specific. (4) MVP Boundary — answers "what is in scope for v1, and what is out?" Failure mode: only writing the "in" column; the out list is what requires discipline, and most PRDs never write it.
*What a strong answer includes:*
- All four section names
- The question each answers
- At least two specific failure modes
*Chapter reference:* What a PRD Actually Is / four sections

---

**Q8 — B**
*Correct because:* The chapter states: "A testable hypothesis has a measurable behavioral outcome in a realistic timeframe." Option B specifies: a behavioral outcome (opening the sheet), a measurable threshold (at least three times per week), a timeframe (after the first two weeks), and falsifiability (if open rate drops, the hypothesis failed). The chapter contrasts this with a vision ("category-defining platform"), which is not testable in v1.
*Why the distractors are wrong:*
- A) "Category-defining platform" is a vision, not a hypothesis — the chapter explicitly uses this type of language as the example of what is untestable in v1.
- C) "Users will prefer our tool" is too vague — it has no behavioral threshold, no specific timeframe, and preference surveys capture what users say they will do rather than what they actually do (violating the "validated" criterion).
*Chapter reference:* What "Minimum Viable Product" Actually Means / testable hypothesis

---

**Q9 — Short-Answer**
*Model answer:* The chapter argues: "The competitor who shipped a worse product four months ago has already run three learn cycles and is now on v4. You are still on v1." The strategic cost is not just delay — it is that competitors operating on a tight Build-Measure-Learn loop learn what works, correct what does not, and iterate into a better product while a team with an overloaded v1 is still building. By the time the overloaded team ships, the market has already formed opinions, competitor products have accumulated user behavior data, and the team is starting with a hypothesis that a faster-moving competitor may have already tested and refined. Scope discipline is not just an efficiency choice — it is a learning-rate choice, and learning faster than competitors is a durable advantage.
*What a strong answer includes:*
- The specific competitor-learning-cycle argument from the chapter
- The distinction between delay as timing and delay as learning-rate disadvantage
- The connection between MVP scope and competitive learning speed
*Chapter reference:* What "Minimum Viable Product" Actually Means / MVP boundary / learning rate

---

**Q10 — Brief-Response**
*Model answer:* The underlying principle that makes Linear's refusals productive is that each refusal is grounded in a coherent point of view about what the product is for and who it is for — Linear has a specific model of how engineering teams should manage work, and every refusal preserves that model. A student refusal without a coherent point of view is sterile because it cannot answer the question "why does this feature conflict with what the product is supposed to be?" — the refusal is based on constraint rather than on identity. The practical distinction: a productive $100,000 no can be completed with a sentence that names the product's purpose and shows how the refused feature would compromise it; a sterile refusal can only say "out of scope for v1." The PRD's archetype connection — the problem statement extends the archetype into a specific user context — is what gives student scope discipline its equivalent grounding.
*What a strong answer includes:*
- The coherent point of view as the necessary precondition for productive refusal
- The distinction between constraint-based and identity-based refusal
- Connection to the PRD's archetype grounding
*Chapter reference:* The $100,000 No / Scope Discipline as Identity / Still Puzzling

---

**Q11 — Transfer Brief-Response**
*Model answer:* The research design equivalent of the $100,000 no is the pre-registration decision — specifying in advance which comparisons will be primary outcomes and which will be exploratory, and committing that adding new primary outcomes after seeing preliminary data is out of scope for this study. Writing it down in advance matters for the same reason the PRD contract matters: when preliminary findings are surprising, or when an advisor suggests an additional analysis that the data could support, the pressure to expand scope is intense and feels like improvement. Without a pre-written commitment, the "decision made when thinking clearly" — that this study tests exactly this hypothesis and no others as primary — is replaced by the in-the-moment pressure decision, which systematically expands scope and produces research with inflated false-positive rates. The out-of-scope list in a research design PRD is the pre-registration document; it exists to hold the contract against the pressure.
*What a strong answer includes:*
- Identification of the research-design equivalent (pre-registration or out-of-scope analysis list)
- The "thinking clearly vs. under pressure" mechanism from the chapter
- Why scope expansion under pressure produces a research failure analogous to the product failure
*Chapter reference:* What the PRD Is Actually Doing / PRD as contract (transfer application)

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

- Misunderstanding "minimum" in MVP as "fewest features" rather than "smallest thing that tests the core hypothesis."
- Treating the $100,000 no as a cost threshold rather than as an identity-grounded refusal.
- Writing problem statements with abstract users ("users," "customers," "professionals") rather than specific, findable people.

**Signs a student needs to return to the chapter before this quiz:**

- Cannot name all four PRD sections with their failure modes.
- Does not understand why the out-of-scope list requires more discipline to write than the in-scope list.

**Scaffolding adjustments:**

- *For students who score below 5:* Work through the problem-statement rewriting exercise from the chapter's Worked Example — take a weak statement and produce three iterations toward specificity before attempting the quiz again.
- *For students who score 11/11 on first attempt:* Ask them to write a complete one-page PRD for their own AI tool, including a specific $100,000 no with a one-paragraph explanation of why building it would compromise the tool's archetype-grounded point of view.
