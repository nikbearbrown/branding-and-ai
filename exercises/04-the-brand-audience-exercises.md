# Chapter 4 — The Brand Audience: Practice Exercises

**Course:** INFO 7375 — Branding and AI: Building the Creative Engineer
**Chapter learning objectives tested:** STP framework (Segmentation/Targeting/Positioning); five bases of segmentation; demographic descriptor vs. needs-based segment distinction; Jobs-to-be-Done (JTBD) framework (Christensen); cultural tension lens (Douglas Holt); persona construction with evidence-status tagging (confirmed/needs evidence/inferred).

---

## Worked Example

**Problem:** A startup is building an AI-powered tool that helps engineers document their internal APIs. The product team has segmented their audience as "software engineers at mid-size technology companies." A user researcher challenges this: "That's not a segment—that's a job title combined with a company description. We can't position to it."

Using the STP framework and the demographic vs. needs-based distinction from Chapter 4, explain why the user researcher is correct and produce a better-formed segment description.

**Approach:** Apply the chapter's definition of a needs-based segment: a group of people who share a specific unmet need, experience a specific cost when that need is unmet, and would respond similarly to the same solution. Then evaluate the existing segment description against this definition, and rewrite it.

**Answer:** "Software engineers at mid-size technology companies" is a demographic descriptor (job title + company size), not a segment. It describes who they are but says nothing about what they need, what problem they have with current solutions, or why they would value the product differently from other groups. Two software engineers at a mid-size tech company could have completely different documentation needs: one writes internal APIs for a small, stable team and documents them once annually; the other maintains a public-facing SDK used by hundreds of external developers and documents multiple times per week under deadline pressure. These two people would respond very differently to the same product—meaning they belong in different segments.

A better-formed segment: "Engineers who maintain APIs consumed by external developers at companies without a dedicated technical writing team, who experience friction between shipping new API features and keeping the documentation current—often resulting in documentation that lags the product by weeks and generates support requests from confused external consumers." This description identifies a specific need (current documentation), a specific cost (support requests, external developer confusion), and a specific context (no technical writer) that would make the same solution highly valuable to this group and allow the product to be positioned precisely.

**What to notice:** The JTBD (Jobs-to-be-Done) insight from Chapter 4 is embedded here: the segment is not defined by who these people are but by the *job* they are struggling to accomplish (keep external API documentation current) and the *progress* they are trying to make (ship with confidence that consumers won't be confused). The milkshake insight applies: the engineer's "job" is not "document my API"—it is "ship faster without sacrificing consumer confidence."

---

## Tier 1 — Remember and Understand

### Contrastive Classification (Required)

**1.1** Below are two audience descriptions for the same product—a tool that generates test data for software teams. Classify each as either a *demographic descriptor* or a *needs-based segment*, and explain the classification in one sentence for each.

Description A: "QA engineers at enterprise software companies with more than 200 developers."

Description B: "Software teams who spend more than two hours per sprint manually creating test data for edge cases, causing test coverage gaps that only surface after release."

`(Tests: demographic descriptor vs. needs-based segment distinction)`

**Answer:** Description A is a *demographic descriptor*: it identifies who people are (QA engineers) in an organizational context (enterprise companies, team size) but says nothing about what they need, what they are struggling with, or why they would respond to this specific solution. Description B is a *needs-based segment*: it identifies a specific problem (manually creating test data for edge cases), a measurable cost (more than two hours per sprint), and a consequence (coverage gaps, post-release failures) that would make a targeted solution clearly valuable to this group and allow precise positioning.

*Common error:* Students often accept a description with some specificity ("more than 200 developers") as needs-based because it has a quantified criterion. Quantification of a demographic descriptor does not make it a segment.

*Chapter reference:* Chapter 4, "Demographic Descriptor vs. Needs-Based Segment."

---

**1.2** The chapter describes five bases of segmentation. Name all five and, for each, write one sentence describing the kind of knowledge about the audience it produces and one limitation it has on its own.

`(Tests: five bases of segmentation)`

**Answer:**

*Demographic:* Produces descriptive population data (age, gender, income, job title, company size) that is easy to measure and widely available, but tells you who the audience is rather than what they need or why they would choose one solution over another.

*Geographic:* Produces location-based groupings (region, market, urban/rural) that are useful for distribution and localization decisions, but geography alone does not explain what people need or why they would pay for a solution.

*Behavioral:* Produces data on how people interact with products or categories (usage frequency, feature adoption, purchase patterns) that directly reflects action, but does not explain why people behave as they do or what job they are hiring the product to do.

*Psychographic:* Produces data on values, personality, and lifestyle orientation that explains motivation better than demographics, but is difficult to measure reliably and can lead to stereotyping if applied at the individual level.

*Needs-based:* Produces groups defined by a shared unmet need, cost, and job-to-be-done—the most actionable basis for positioning because it directly connects audience description to product value—but requires primary research to discover and is harder to operationalize for targeting than demographic or behavioral data.

*Chapter reference:* Chapter 4, "Five Bases of Segmentation."

---

**1.3** In Christensen's milkshake study, customers who bought milkshakes in the morning were hiring the milkshake for a different job than customers who bought them in the afternoon. Describe the two jobs and explain what this distinction implies for how the product should be positioned differently for each segment.

`(Tests: JTBD framework — job identification and positioning implication)`

**Answer:** Morning customers hired the milkshake for the job of "keeping me engaged on a long, boring commute without making a mess"—they needed something thick (so it would last), portable, and consumed alone in a car. Afternoon customers hired the milkshake for the job of "being a special treat for my child during an outing"—they needed something that could be consumed more quickly and shared in a social moment. The positioning implication: a milkshake positioned for "rich, creamy satisfaction" is not wrong, but it is generic. Morning commuters would respond to positioning that emphasizes thickness, duration, and convenience; afternoon family customers would respond to flavor variety, portion size, and the treat occasion. The same product, positioned identically to both segments, underperforms what it could be to each. The JTBD framework predicts that the real competition for the morning commuter milkshake is not another milkshake—it is a banana, a bagel, or an energy bar (other things people hire for the same commute-occupation job).

*Chapter reference:* Chapter 4, "JTBD Framework," "Milkshake Study."

---

**1.4** The chapter distinguishes between three evidence-status tags that should be applied to claims within a persona document: *confirmed*, *needs evidence*, and *inferred*. Give one example of each tag applied to a specific claim that might appear in a persona for an engineering manager in a mid-size software company.

`(Tests: persona construction — evidence-status tagging)`

**Answer:**

*Confirmed:* "Engineering managers in companies with 50–150 engineers spend an average of 6 hours per week in status and alignment meetings" [CONFIRMED — from 2023 Engineering Management survey, n=412].

*Needs evidence:* "This persona segment prefers async communication over real-time meetings" [NEEDS EVIDENCE — assumed based on anecdotal comments in initial user interviews; requires structured survey to validate at scale].

*Inferred:* "Engineering managers who have transitioned from IC roles within the last two years are more likely to experience imposter syndrome around strategic planning" [INFERRED — plausible based on transition research in adjacent fields, but no direct evidence from this segment].

*Chapter reference:* Chapter 4, "Persona Evidence-Status Tagging."

---

**1.5** Douglas Holt's cultural tension lens identifies cultural contradictions as the source of brand opportunity. Using an example from your own field of study or professional context (not one from the chapter), identify a cultural tension and explain what brand opportunity it creates.

`(Tests: cultural tension lens — application to a novel context)`

**Answer (example model — any defensible example is acceptable):** In the machine learning engineering field, there is a cultural tension between the dominant narrative that "AI democratizes everything" (the field aspires to be accessible and open) and the lived reality that deploying reliable AI in production requires deep, expensive, hard-won expertise that most organizations lack. This tension creates a brand opportunity for tools or courses that speak honestly to the practitioner's difficulty—"this is harder than it looks, and here's how to do it right"—rather than the oversimplified democratization claim. The brand that names the gap between aspiration (accessible AI) and reality (high failure rates in production) can build resonance with practitioners who feel gaslit by the mainstream narrative.

*Chapter reference:* Chapter 4, "Cultural Tension Lens," "Douglas Holt."

---

## Tier 2 — Apply and Analyze

### Error Analysis (Required)

**2.1** A student team has built the following persona for their AI-powered meeting summary tool:

> **Alex Chen, 34, Product Manager at a tech company**
> Alex is a busy professional who has lots of meetings every day and struggles to keep track of everything. Alex wants to be more productive and save time. Alex is tech-savvy and open to new tools. Alex has a positive attitude and believes AI can help professionals work smarter.
>
> Alex's pain points: too many meetings, too many emails, information overload.
> Alex's goal: be more productive and use time better.

Identify at least three specific violations of good persona construction practice from Chapter 4, and rewrite the persona correctly.

`(Tests: persona construction — specificity, JTBD, evidence tagging, demographic vs. needs-based clarity)`

**Answer — Violations:**

Violation 1: *The persona has no evidence-status tagging.* Every claim about Alex—the number of meetings, the pain points, the attitude toward AI—is stated as fact with no source, no distinction between confirmed and inferred, and no indication of what research produced the characterization.

Violation 2: *The persona describes symptoms (too many meetings, too many emails) rather than a specific job-to-be-done.* "Wants to be more productive" is a goal category, not a job. What specific progress is Alex trying to make? What is the friction point in the existing workflow—what does Alex currently do to manage meeting outputs and why does it fail? Without a specific job, the persona cannot drive positioning decisions.

Violation 3: *"Alex Chen, 34, Product Manager at a tech company" is a demographic descriptor, not a segment anchor.* The persona combines demographic details (age, title, company) without specifying what needs-based segment Alex represents. Two product managers at tech companies with the same demographics may have completely different workflows and meeting-management needs.

Violation 4 (bonus): *The persona contains abstract positive attributes ("positive attitude," "open to new tools") that cannot differentiate Alex from any other professional.* These traits are so generic that they do not produce any design or positioning decisions.

**Rewritten persona:** 

> **Product Manager, mid-size B2B SaaS, 3–5 direct reports** [NEEDS EVIDENCE for team size distribution]
>
> *Core job:* After a strategy or planning meeting, needs to capture and distribute the specific decisions and action items to multiple stakeholders who were not present, without spending more than 20 minutes on the task. Currently writes manual notes during the meeting and spends 30–45 minutes producing a summary afterward—often losing or misattributing action items. [CONFIRMED — from 6 user interviews; NEEDS EVIDENCE for time estimate at scale]
>
> *Progress blocked by:* Notes taken during the meeting are not structured for distribution; items attributed to the wrong participant; action items mixed with context rather than separated. [CONFIRMED — from interview observation]
>
> *What they will not compromise on:* The summary must be accurate enough that a stakeholder who was not present trusts it as the record of what was decided. Quality of record is the constraint; speed is the benefit. [INFERRED — based on expressed concern for accuracy in interviews; requires testing]

*Chapter reference:* Chapter 4, "Persona Construction," "JTBD Framework," "Evidence-Status Tagging."

---

### Self-Explanation Exercise (Required)

**2.2** The chapter argues that "targeting" in the STP framework is not simply "choosing the biggest segment." Using only Chapter 4's vocabulary and concepts, explain what criteria actually govern the targeting decision and why size alone is an insufficient criterion.

`(Tests: STP framework — principled reasoning about targeting criteria)`

**Answer (model):** The targeting decision should be governed by at least three criteria beyond size: *segment accessibility* (whether you can reach this segment through available channels), *segment fit with your offering* (whether the segment's specific needs match what you are distinctively positioned to provide), and *competitive intensity* (whether the segment is already well-served by existing solutions, in which case entering requires either a significant advantage or a price-concession that may undermine your positioning). A large segment that is inaccessible (no channel to reach them), poorly fitted to your offering (their needs are adjacent to your capability, not central), or already saturated (strong incumbents serve the same job well) is a worse target than a smaller segment where you have a genuine advantage. The JTBD insight also implies a targeting criterion that size obscures: a small segment with a high-intensity, specific job where current solutions fail badly may generate more equity and revenue than a large segment with a diffuse, low-urgency need that many alternatives partly satisfy. The chapter's persona framework reinforces this: a persona built on a specific job-to-be-done will reveal whether your solution actually addresses the job, which the demographic size of the segment cannot tell you.

*Chapter reference:* Chapter 4, "STP Framework," "Targeting," "JTBD."

---

### Cumulative Exercise (Required — integrates Chapter 2 concepts)

**2.3** Chapter 2 describes brand equity as built through consistent experiences that accumulate in the audience's memory, and measured through the three outcomes of premium willingness, retention, and forgiveness. Chapter 4 argues that the quality of audience definition drives the quality of brand positioning. Apply both frameworks to the following scenario:

A software developer tool has been growing steadily for two years. The founding team defined their initial audience broadly as "developers who want to be more productive"—a demographic descriptor with no needs-based specificity. They now have 15,000 users, positive reviews, and an NPS of +38. However, their renewal rate is 67%—below their category benchmark of 80%—and price sensitivity is high (a recent 10% price increase produced a 15% cancellation rate).

Diagnose the problem using both Chapter 4's audience framework and Chapter 2's brand equity framework.

`(Tests: STP/JTBD audience quality [Chapter 4] + brand equity manifestations [Chapter 2] — integrated diagnosis)`

**Answer (model):** From Chapter 4: "developers who want to be more productive" is a demographic descriptor, not a segment. Without a specific job-to-be-done, the product was positioned to be useful to many developers in many contexts—which meant it was never precisely positioned for any specific job. When developers arrive with different underlying jobs (writing faster, reducing bugs, learning new frameworks, documenting code), the product may partially satisfy each but fully satisfy none. This creates a diffuse user base with weak attachment because the tool doesn't solve their specific problem at the level of intensity that would generate loyalty.

From Chapter 2: The equity diagnostics are revealing. 67% renewal rate (below 80% benchmark) indicates weak loyalty—users are not committed enough to stay when any friction or alternative arises. High price sensitivity (10% price increase → 15% cancellation) indicates weak price-premium equity—users evaluate the tool on cost-benefit at each renewal decision rather than from a position of strong preference. This pattern is consistent with a tool that is useful but not necessary—it is satisfying a diffuse productivity desire rather than solving a specific, painful, high-urgency job. Strong equity produces retention and premium tolerance; this tool has neither because it was never positioned to a specific enough job to build the deep need that sustains both.

Synthesis: the audience-definition failure (no needs-based segment, no specific JTBD) produced a positioning failure (generic productivity value proposition), which produced an equity-building failure (no specific job solved well enough to generate loyalty and premium tolerance).

*Chapter reference:* Chapter 4, "STP/JTBD"; Chapter 2, "Brand Equity Manifestations."

---

### AI Interaction Exercise (Required)

**2.4** Choose Option A or Option B.

**Option A (Evaluate and Verify):** Ask an AI assistant: "What is the Jobs-to-be-Done framework, and how does it differ from traditional persona-based audience research?"

(1) Record the response (or a representative excerpt).
(2) Identify one thing the AI correctly explained.
(3) Identify one claim the AI made about JTBD that you can evaluate against Chapter 4—specifically, whether the AI captured the "progress" and "hiring" metaphors correctly, and whether it mentioned the milkshake study accurately.
(4) Write a corrected explanation of how JTBD differs from persona-based research using Chapter 4's framework.

`(Tests: JTBD framework — AI response evaluation with specific accuracy check)`

**Option B (Answer First, Then Compare):** Before using any AI tool, write your own two-paragraph explanation of how JTBD differs from demographic persona research—what JTBD reveals that demographic personas cannot, and vice versa. Then ask the AI the same question.

(1) Where did the AI agree with your explanation?
(2) Where did the AI identify a limitation of JTBD that you had not included?
(3) Where did the AI's description differ from Chapter 4's treatment in a way you believe is inaccurate?
(4) Write a synthesis explanation you are confident is accurate.

`(Tests: JTBD vs. persona research — self-assessment and comparative analysis)`

*Verification step (required for both options):* Find and read the original HBR article or book chapter by Clayton Christensen that introduced the milkshake study (often found in "Competing Against Luck," 2016, or in HBR articles from the same era). Confirm whether the AI's description of the study is accurate or introduces modifications. Note one specific point.

*Chapter reference:* Chapter 4, "JTBD Framework," "Milkshake Study."

---

**2.5** A brand strategy consultant argues: "Personas are fictional characters. The moment you give them a name and a headshot, the team falls in love with the fiction and stops treating them as research artifacts. The evidence-status tagging approach from this chapter can't fix that problem because it's an emotional problem, not an evidential one." Evaluate this argument in two to three sentences.

`(Tests: persona construction — evidence-status tagging as methodological discipline)`

**Answer:** The consultant correctly identifies a real risk—personas can become characters the team protects rather than hypotheses the team tests. However, the evidence-status tagging approach addresses this partially at a structural level: tagging every claim as CONFIRMED, NEEDS EVIDENCE, or INFERRED makes the persona visibly incomplete and explicitly provisional, which creates an organizational norm that the persona must be updated rather than defended. The deeper intervention the consultant is pointing to—resisting anthropomorphization of research artifacts—is a design process and facilitation challenge that the chapter's approach mitigates but may not fully resolve without additional team practices (periodic persona-update rituals, naming the persona as a segment hypothesis rather than a person).

*Chapter reference:* Chapter 4, "Persona Construction," "Evidence-Status Tagging."

---

## Tier 3 — Analyze and Evaluate

**3.1** Nike's cultural tension (the chapter cites Nike as navigating the tension between individual athletic achievement and the broader social justice questions that athletics surfaces) is used to illustrate how brands can build position at the site of a cultural contradiction rather than around a product feature. Apply the cultural tension lens to a technology brand of your choice (not Nike, not Dove, not an example from the chapter). Identify: (a) the cultural tension the brand navigates; (b) what each side of the tension represents; (c) how the brand's positioning takes a specific side or bridges the two; (d) what would happen to the brand's equity if the tension resolved (if one side won culturally).

*(References Chapter 4's cultural tension lens; also draws on Chapter 2's brand equity accumulation concepts.)*

`(Tests: cultural tension lens — applied to a novel technology brand case)`

**Model answer (using Notion as an example—any defensible technology brand is acceptable):**

(a) *Cultural tension:* The tension between "productivity culture" (the belief that more structured work, faster execution, and optimized systems are always better) and the countermovement of "slow thinking" and "analog intentionality" (the belief that deep work requires friction, resistance to digital distraction, and freedom from productivity optimization).

(b) *Each side:* The productivity-culture side believes that everything should be measured, organized, and optimized—the promise of technology is to remove friction from thinking. The slow-thinking side believes that friction is valuable—that forcing yourself to write things out, to use an imperfect system, to make decisions without a digital assistant is how complex ideas develop.

(c) *Notion's position:* Notion navigates this tension by presenting itself as the tool for "structured thinking"—it adds enough friction (you must decide how to organize information) that it appeals to people who value intentionality, while also being digital and efficient enough to satisfy productivity culture. It positions itself as the thoughtful alternative to chaotic note-taking and to overly rigid enterprise tools—claiming both intentionality and productivity.

(d) *If the tension resolved:* If productivity culture won decisively, Notion would face competition from faster, more automated alternatives (an AI that organizes everything without user input). If the slow-thinking movement won decisively, Notion would lose relevance to paper advocates and truly analog practitioners. The brand's equity depends on the tension persisting—on both sides remaining culturally active.

*Common error:* Identifying a tension that is not genuinely cultural (e.g., "people want cheap tools but also want quality") rather than a contradiction in values that a significant portion of the target audience feels.

*Chapter reference:* Chapter 4, "Cultural Tension Lens"; Chapter 2, "Brand Equity Accumulation."

---

**3.2** The STP framework is presented in Chapter 4 as a linear sequence: segment first, then target, then position. A classmate argues that this sequence is backwards in practice: "Successful companies often develop a product or a position first and then identify who responds to it—they discover their segment through the market, not in advance." Evaluate this argument. Under what conditions is the classmate's claim correct? Under what conditions does the chapter's sequential STP approach produce better outcomes?

*(References Chapter 4's STP framework and JTBD; also draws on Chapter 1's Spence signaling concepts.)*

`(Tests: STP framework — evaluating the sequence claim against a coherent alternative; integration with Chapter 1 signaling`

**Model answer:** The classmate's argument is correct for a specific condition: early-stage exploration where the product creator has a strong intuition about a solution but has not yet identified the segment that has the corresponding job. Many products are discovered this way—a developer builds a tool for themselves, ships it, and discovers through usage patterns which specific segment of users finds it most valuable. This is empirical segmentation, and it works.

However, the chapter's sequential approach produces better outcomes under two conditions. First, when the product development investment is substantial enough that building without knowing who you're building for creates significant risk of over-engineering features the discovered segment doesn't need. Second—connecting to Chapter 1's Spence signaling—when positioning is a separating signal itself: a product that was designed for a specific, deeply understood segment produces a more coherent signal of expertise than one that discovered its segment post-hoc. The JTBD framework's contribution to the sequential approach is that it makes the pre-development targeting more rigorous than demographic guessing: identifying a specific job with a specific cost to the specific person who has that job is actionable research, not speculation. The classmate's approach and the chapter's approach are both valid; their relative merit depends on the cost and reversibility of the product investment.

*Chapter reference:* Chapter 4, "STP Framework"; Chapter 1, "Spence Signaling."

---

## Tier 4 — Evaluate and Create

**4.1 — Challenge Exercise**

The chapter argues that personas should be treated as research artifacts with explicit evidence-status tagging, not as fictional characters. But all research involves interpretation, and the line between "inferred" and "invented" is not always clear in practice.

Design a quality-control protocol that a product team could use to evaluate whether a persona has been built rigorously or whether it has drifted into fiction. The protocol should:

- Define specific criteria for distinguishing a confirmed claim from an inferred claim in a persona context
- Specify what evidence is required to move a claim from "inferred" to "confirmed"
- Identify at least three specific warning signs that a persona has become a fictional character rather than a research artifact
- Address how to handle the case where the team has emotional investment in the existing persona

Your response should be 400–600 words. Evaluate based on:
- Does the protocol produce actionable pass/fail criteria, or only vague aspirations?
- Does it address the emotional investment problem the chapter names?
- Does it distinguish among the three evidence statuses in a way that is operationalizable?
- Does the response engage the difficulty of converting inferred claims to confirmed ones in resource-constrained environments?

`(Tests: persona construction — rigorous quality control of research artifacts; designing a practical protocol)`

---

## Answer Key

| Item | Correct Answer | Common Error | Chapter Reference |
|------|---------------|--------------|-------------------|
| 1.1 | A = demographic descriptor; B = needs-based segment | Accepting quantified demographic criteria as needs-based | Ch. 4, Demographic vs. Needs-Based |
| 1.2 | Five bases: demographic, geographic, behavioral, psychographic, needs-based — each with distinct knowledge and limitation | Treating all five as equivalent or interchangeable | Ch. 4, Five Bases of Segmentation |
| 1.3 | Morning job: commute occupation/duration; afternoon job: social treat; positioning differs for each | Describing milkshake study without extracting positioning implication | Ch. 4, JTBD / Milkshake Study |
| 1.4 | Confirmed (with source), needs evidence (unexplored assumption), inferred (reasoned from adjacent evidence) | All three tags used but without differentiation of the evidence basis | Ch. 4, Evidence-Status Tagging |
| 1.5 | Identifies a genuine values contradiction (not a market gap), names both sides, identifies brand opportunity | Describing a feature gap rather than a cultural tension | Ch. 4, Cultural Tension Lens |
| 2.1 | Three violations: no evidence tagging; no JTBD; demographic not needs-based; rewritten persona corrects all three | Missing one of the violations; accepting the demographic basis | Ch. 4, Persona Construction |
| 2.2 | Targeting criteria beyond size: accessibility, fit, competitive intensity, JTBD fit | Treating size as the only criterion with minor caveats | Ch. 4, STP Targeting |
| 2.3 | Audience-definition failure → positioning failure → equity-building failure; renewal and price-sensitivity data interpreted through equity manifestations | Treating the diagnosis as purely a marketing problem without connecting to equity outcomes | Ch. 4 + Ch. 2 integration |
| 2.5 | Consultant partly right (emotional problem); evidence tagging mitigates but doesn't fully solve | Dismissing the consultant's concern entirely | Ch. 4, Persona Construction |
| 3.1 | Cultural tension identified with both sides named; brand position mapped; equity-if-resolved analysis included | Identifying a product feature gap rather than a values contradiction | Ch. 4, Cultural Tension Lens |
| 3.2 | Classmate correct for exploration conditions; sequential approach better for high-investment decisions; both valid in different conditions | Accepting one approach as universally correct | Ch. 4, STP Framework |

---

## Instructor Notes

**Tier 1 volume:** 5 items (chapter has 5+ LOs)
**Worked example:** Uses API documentation tool scenario to model the demographic-vs-needs-based distinction and the JTBD application before exercises begin
**Contrastive classification (1.1):** Targets the most common misconception — accepting a quantified demographic description as needs-based; both descriptions are plausible audience definitions in real product contexts
**Error analysis (2.1):** Three genuine persona construction violations; the student persona is a realistic example of what students actually produce without training in the chapter's framework
**Self-explanation (2.2):** Requires reasoning from targeting criteria to explain why size is insufficient; prevents surface-level restatement of "you need to think about more than size"
**Cumulative (2.3):** Integrates Chapter 2 (equity manifestations: renewal rate, price sensitivity) with Chapter 4 (audience definition quality, JTBD); explicitly requires referencing both chapters; renewal rate and price-sensitivity data are the equity diagnostics
**AI interaction (2.4):** Verification step requires locating the Christensen milkshake source; plausible AI response expected to describe JTBD correctly at a high level but may use the "hiring" metaphor without fully explaining "progress" or may conflate JTBD with persona research
**Synthesis exercises (3.1–3.2):** Both reference Chapter 4 explicitly; 3.1 requires identifying a technology brand's cultural tension; 3.2 integrates Chapter 1 (Spence signaling) as a second framework for evaluating the sequence question
**Challenge (4.1):** Tests protocol design ability; no model answer; rubric criteria listed; the hardest element is addressing the emotional investment problem, which the chapter names but does not fully solve
