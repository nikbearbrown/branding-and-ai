# Chapter 11 — Portfolio as Product
*The artifact you build once and the returns that compound for a decade.*

---

In 2017, Brittany Chiang published a redesign of her personal portfolio website. The site was clean, minimal, dark-themed — a slate-blue background, mint-green accents, monospace typography. The code was open. Over the following years, as she moved through Upstatement, Apple, Spotify, and senior engineering roles at Klaviyo, something quiet happened to that portfolio: the GitHub repo for its fourth iteration accumulated over 9,000 stars and 6,000 forks. Generations of developers used her design as the foundation of their first portfolio. Her name traveled into commit histories and footer credits of sites she had never seen, built by people she had never met.

The portfolio was not the only factor in her career. The engineering work is excellent, the network is strong, the timing was good. But the portfolio did something the engineering work and the network could not do on their own: it compounded. The asset was built once and continued generating returns — brand impressions, name recognition, implicit credibility — for years after the work was done.

That is the mechanism this chapter is about, and it is the reason most graduate portfolios fail not from inadequacy but from under-ambition. An adequate portfolio gets through a hiring funnel. A designed portfolio compounds. The gap between them is roughly twenty hours of deliberate work. The return differential is a decade.

You need the prior chapters in hand before this one is useful. Specifically: your archetype from Chapters 1 and 3 — the portfolio expresses it, does not invent a new one. Your deployed AI tool from Chapter 7 at a public URL, which is the centerpiece this chapter wraps. Your brand strategy from Chapter 8 — the one-sentence positioning, the voice, the values. Your visual identity from Chapter 9. And the narrative content from Chapter 10 — the origin story, the case study draft, the thought-leadership piece. If any of these are missing, the portfolio will show the gap. Complete the prerequisite work even in rough form. A rough brand strategy and a rough case study produce a coherent portfolio. No brand strategy and no case study produce a placeholder site that will not compound.

---

The word *portfolio* is doing five different jobs in conversations about career development, and most graduates conflate them. A resume is a text document optimized for ATS systems and the thirty-second human skim. A portfolio website is a designed presentation of selected work optimized for the two-to-five-minute deep read. A GitHub profile is a technical-evidence surface, indexed and inspectable by engineers. A LinkedIn profile is the professional-network surface optimized for recruiter discovery via search. And then there is the thing this chapter is trying to produce: a portfolio-as-product, in which the first three surfaces tell the same story from three angles — same archetype, same voice, same selected projects, same positioning sentence — while serving their different reading speeds and audiences.

Convergence does not mean uniformity. A resume and a portfolio website serve different reading speeds, different audiences, different moments in the hiring funnel. The resume is skim-optimized; the portfolio is deep-read-optimized. But the same positioning sentence should appear in both. The same projects should be featured. The same archetype should be legible. A recruiter who reads both should have no doubt they are looking at documents about the same person.

<!-- → [TABLE: Five portfolio artifacts — columns: artifact, primary audience, reading speed, optimization goal, what alignment looks like across artifacts. One row per artifact.] -->

---

The deep principle to install before we talk about any technical tooling: a portfolio is a compounding asset. The time you invest in building it is bounded. The brand impressions it generates are not. Understanding the compounding mechanism changes what you build.

Three channels. Most graduates design for the first and ignore the second and third. The second and third are where the compounding lives.

**Direct hiring.** A recruiter finds your portfolio through a search, an application, or a referral. They look at it, pull up your resume, move you to the next stage. This is the channel every graduate thinks about. It is visible, predictable, and optimizable in obvious ways. The portfolio needs to be recruiter-legible to perform here.

**Indirect reference.** Someone — a developer, a hiring manager, a professor, someone you have never met — encounters your portfolio through a share, a link in a "best portfolios" article, a retweet, a forward. They do not have an open role right now. They bookmark it, or they remember your name. Weeks or months later, when a role opens, they mention you. The chain is invisible to you. You have no idea it happened until someone says "I heard about you from..."

This channel is impossible to optimize for directly and impossible to ignore. The portfolio that performs here is the one *worth referencing* — distinctive, coherent, executing with craft. The portfolio that does not perform here is the one that is adequate: recruiter-ready, by-the-numbers, indistinguishable from ten thousand others. Chiang's portfolio compounded through this channel for years before she was at Spotify. You cannot track Channel 2 returns. You can build for them.

**Template effects.** Your portfolio design or case study structure becomes a starting point for other developers. They clone the repo, fork the design, borrow the structure. Each derivative carries your name in its commit history, in the footer credit, in the "inspired by" acknowledgment. This channel operates at scale and on autopilot. Chiang's 6,000-plus forks are the most visible example of Channel 3 compounding, but the pattern runs at smaller scales too: a clean case study structure gets borrowed, a README format gets copied, a layout decision shows up in a dozen other sites.

The design implication is this: building a portfolio that only performs in Channel 1 is under-optimizing. Not in the sense that the direct-hiring return is insufficient — it may be sufficient for your immediate goal. In the sense that you are leaving the second and third channels on the table with no additional investment. A portfolio designed for all three is built with the same discipline you brought to the AI tool: scope, craft, archetype alignment, explicit content decisions, negative space as intentional as positive space.

<!-- → [FIGURE: Three compounding channels — central portfolio box on the left, three directed connectors fanning out to labeled cards. Channel 1 short and visible. Channel 2 long, dashed, highlighted — the high-compounding arrow. Channel 3 branching, autonomous, operating without the portfolio owner's involvement.] -->

---

A portfolio's power comes as much from what is absent as from what is present. The negative-space rule from Chapter 8 applies directly here: what you decline to include defines the product's point of view as clearly as what you include.

Most graduates make the same curation mistake: they include too many projects. They have ten projects, they put ten projects on the portfolio, and they reduce each to a thumbnail and a sentence because there is not room for more. The recruiter sees ten small things instead of three large things. The portfolio reads as "I have done things" rather than "I am this kind of engineer."

Three to six projects is the right number. Three is better than six if the three are excellent and the six would include mediocre work. The selection criteria are not "best by technical difficulty" or "most recent." They are: which three to six projects, combined, make the strongest possible case for the archetype and the positioning claim?

A Sage archetype whose positioning is "AI engineer building developer-first marketing intelligence tools" should select projects that demonstrate intelligence-building, not projects that demonstrate general-purpose web development. If the strongest project on the archetype axis is not the most technically complex project you have ever done, put the archetype-aligned project on the portfolio anyway. The portfolio is brand strategy, not a transcript.

The negative-space rule in practice: for every project on the portfolio, name one project that is not on it and write one sentence explaining the exclusion. If you cannot write that sentence — if you included everything and excluded nothing — the portfolio does not have a point of view.

What does not belong: a screenshot wall of every project. A skills section listing fifty technologies as icons. Personal hobbies unrelated to the archetype. Long lists of job titles and dates — that is the resume's job. Testimonials from people the audience has never heard of. A "currently learning X" list that implies the thing is not yet learned. Each of these reduces signal-to-noise in a context where the visitor has two to five minutes. Every item that is not archetype-reinforcing is a tax on their attention.

<!-- → [TABLE: Project curation decision matrix — columns: concept, what it means, how to use it. Content covers the selection criteria, the exclusion rule, the signal-to-noise principle.] -->

---

The tool you built in Chapters 4 through 7 is the centerpiece project. It is the project with the most supporting material — a PRD, a built pipeline, an architecture decision, a deployed interface, an alignment audit. It is also the project that most directly expresses the archetype and the brand strategy, because it was designed to do so from Chapter 4 onward.

The case study for this tool needs to perform four functions simultaneously. Most engineering case studies perform one or two. Performing all four is what sets the case study apart.

**Frame the problem.** The customer-as-hero opening from Chapter 10: a specific user, a specific pain, a specific frequency, a specific cost. *Marketing managers at small B2B SaaS companies spend two to three hours every Monday manually aggregating competitor news. The output is stale, inconsistent, and consumes time they do not have.* Specific. Recognizable. The reader should be able to find ten people who fit this description before they finish the sentence.

**Show the technical work.** The architecture — the Madison Intelligence Agent pattern, the n8n pipeline, the GPT-4o-mini sentiment layer. The key decisions from Chapters 5 and 6, with one-sentence justifications for each. The architecture diagram from the README as a starting point. Screenshots of the deployed interface. And — the piece most student case studies skip — specific metrics. Throughput, latency, accuracy on a test set, cost per run.

The metrics are worth dwelling on. A case study that says "the tool processes articles quickly and accurately" is not a case study; it is a marketing claim. A case study that says "the tool processes 870 articles in under three minutes at a cost of approximately $0.80 per run, with 90% deduplication efficiency" is a case study. The numbers make the claim verifiable. Verifiable claims build trust in a way unverifiable claims cannot.

**Connect to the brand.** A note on archetype, voice, and visual choices. Why the interface is designed the way it is. What the alignment audit revealed and what was changed. This is the section most engineering case studies omit entirely. Including it signals that you think about engineering as design — that you understand the relationship between technical decisions and the experience those decisions produce.

**Be honest about limits.** Name what the tool does not do. What the MVP boundary excluded and why. What a v2 would add. What the Build-Measure-Learn loop has revealed so far. Honesty about limits is a Feynman move — it builds trust in the claims you do make by demonstrating that you know what you do not know.

Length: 800 to 1,500 words. With visuals: a hero screenshot at the top, the architecture diagram in the technical section, two or three interface screenshots, one results image. Reading time: four to seven minutes for a thorough reader. This is the artifact a hiring manager who has passed the filter and wants depth will read before deciding whether to move you forward.

<!-- → [TABLE: Case study anatomy — columns: function, what it contains, what it signals to the reader, common failure mode when omitted, approximate word count. Four rows.] -->

---

You will not be starting from scratch on the portfolio's code. Three tools get you to a deployed portfolio at a fraction of the time hand-coded React would take, and each makes different tradeoffs worth understanding before you choose.

[v0](https://v0.app/) (from Vercel) generates React components from natural-language prompts. Output is shadcn/ui plus Tailwind. You describe the component you want, v0 generates working React, you refine through follow-up prompts, you deploy to Vercel in one click. The workflow for a portfolio: take the wireframe from Chapter 9, translate each section into a v0 prompt, generate and refine each component, assemble into pages, deploy. Time to a deployed draft: a weekend.

The output is real React code you can continue iterating in if you want to go beyond what prompts can express. The tradeoff: v0 output has a recognizable aesthetic. A portfolio built entirely from v0 prompts will look competent and on-trend, but it will look like other v0 portfolios. Distinction — the thing that enables Channel 2 and Channel 3 compounding — comes from the brand strategy, the visual identity, and the content you bring on top of the tool. The tool is a starting point. Your Chapter 8, 9, and 10 work is the ending point.

[Framer](https://framer.com/) is a design tool that became a code-generating tool. You design visually; the system produces a deployable site. Strong at the design-and-publish loop for users more comfortable in design tools than code editors. Less implementation control than v0; more control over precise visual expression. Framer's AI features can generate page layouts from prompts, adapt styles to match a visual brief, and handle responsive behavior automatically. The tradeoff: less implementation flexibility, and Framer sites are hosted on Framer's infrastructure. For a portfolio that needs to demonstrate React capability to a technical audience, v0's exportable React code is a stronger signal. For a portfolio where visual design is the primary demonstration, Framer's visual-first workflow may be faster.

Hand-coded React — using Chiang's open-source v4 as a reference or starting from scratch — gives full control, the most distinctive output, and the strongest technical signal to a React-oriented engineering team. The tradeoff is time. A hand-coded portfolio takes longer. For a course with a deadline, v0 is the right trade for most students.

For visual assets — hero images, project illustrations, branding assets — the current generation of image models (Midjourney, DALL-E 3, Flux, Imagen) can generate portfolio-quality visuals in minutes. The constraint that matters: consistency. Choose one model and stay with it across all generated assets. Midjourney's painterly aesthetic and Flux's photorealistic style do not mix coherently on the same page. Your archetype picks the aesthetic; one model expresses it consistently.

<!-- → [TABLE: v0 vs Framer vs hand-coded React — one column per tool, rows covering: control level, deployment path, technical signal sent, visual control, best fit use case, time to deployed draft.] -->

---

Deployment for a v0 portfolio is one click — Vercel is built into the v0 workflow. For Framer, deploy from within Framer to a Framer-hosted URL. For hand-coded React, `vercel deploy` from the project directory, or connect a GitHub repo to Vercel's dashboard. Three decisions to make before the URL goes live.

**The domain.** A random Vercel subdomain (`yourname.vercel.app`) is functional. A named domain (`yourname.dev` or `yourname.com`) signals that the portfolio is a maintained professional artifact. Register one this week if you do not have one. Under $20 per year. The signal is worth it.

**Accessibility.** WCAG AA compliance is not optional for a portfolio designed to be shared widely. Color contrast ratios above 4.5:1 for normal text and 3:1 for large text — test with the WebAIM Contrast Checker or Chrome DevTools accessibility panel. Alt text on every image. Keyboard navigation that reaches every interactive element. No information conveyed only through color. A portfolio that fails accessibility cannot be read by some fraction of your audience, and it is a signal that you do not think carefully about users.

**Performance.** Lighthouse score above 90 on the deployed version. The main failure mode is image size: full-resolution screenshots and AI-generated hero images are often several megabytes. Compress images before embedding. No auto-playing video. No blocking third-party scripts.

Then run the coherence audit before sharing the URL. Send your portfolio URL, your LinkedIn URL, and your resume to one person who has not seen them. Ask one question: does this feel like the same person from three angles? If the answer is no, identify the surface that has drifted and revise it.

Specifically: does the positioning sentence on the portfolio above-the-fold match the LinkedIn headline? Is the archetype legible in all three? Are the same three to five projects featured across the portfolio project section, the LinkedIn featured section, and the resume's project entries? Is the voice consistent — read the portfolio about section and the LinkedIn about section aloud back to back and ask whether they sound like the same person?

The coherence audit is not about making the three surfaces identical. It is about making them feel like three angles on one person rather than three separate presentations of three different candidates.

---

LinkedIn is the surface most graduates underuse. The minimum changes for archetypal alignment take two to three hours and have compounding returns, because LinkedIn is where recruiters encounter you most often and earliest.

The headline should be rewritten from the default ("Software Engineer at X") to a positioning sentence that matches the above-the-fold line on your portfolio website. "AI engineer building developer-first marketing intelligence tools" for a Sage. "AI engineer shipping multi-agent content systems and the brand strategy that makes them legible" for a Creator. The headline appears in search results, in messages, in connection suggestions. It should do work.

The about section: two to four short paragraphs, same voice as the portfolio's about section, slightly more personal. First paragraph is the positioning sentence expanded. Second is the origin story compressed — from Chapter 10's longer version, take the best two or three sentences. Third is the current focus. Read it aloud. If it sounds like a corporate bio, rewrite it.

The featured section: pin three things. Your portfolio URL. Your AI tool's deployed URL from Chapter 7. Your best published piece from Chapter 10. These three artifacts represent the full arc of the semester — the brand surface, the technical surface, and the narrative surface. LinkedIn will surface them prominently.

Experience descriptions: each role gets two to three sentences on what you built and why it mattered, with project links where possible. Narrative, not a bullet wall. Skills: prune to the ones directly relevant to the archetype-positioned brand. A Sage AI engineer keeps the AI and data skills; archives the general web development skills learned seven years ago. A wall of fifty technologies signals lack of focus.

The cumulative effect: a recruiter who looks at your LinkedIn, clicks through to your portfolio, and reads your resume encounters the same archetype from three angles.

<!-- → [TABLE: LinkedIn optimization — columns: element, default state and its failure signal, archetype-aligned version. Rows: headline, about section, featured section, experience descriptions, skills.] -->

---

The portfolio closes a loop that opened in Chapter 1.

Chapter 1 gave you an archetype — a theory of the kind of value you create and the mode in which you create it. Chapter 4 gave you a PRD with scope discipline. Chapter 7 gave you a deployed tool with an aligned interface. Chapter 8 gave you a brand strategy. Chapter 9 gave you a visual identity. Chapter 10 gave you a narrative voice. The portfolio is where all of those artifacts converge into a single product that can be encountered by the people you want to work with.

The convergence is not automatic. It requires the explicit work this chapter describes: selecting projects with the negative-space rule, writing a case study that performs all four functions, running the coherence audit across surfaces. Without that work, the artifacts remain separate — a strategy document, a visual brief, a few case studies — and the compounding does not happen.

> A portfolio is not a resume with images. It is the physical form of a brand strategy — the artifact where the theory of who you are and what you do becomes visible, navigable, and shareable. Build it once and build it well. The returns are non-linear.

---

## Chapter Summary

The chapter's central mechanism is compounding. Most graduates design portfolios for Channel 1 — the direct hiring funnel — and ignore Channel 2 (indirect reference) and Channel 3 (template effects), which is where the decade-long returns live. The gap between an adequate portfolio and a designed one is roughly twenty hours of deliberate work. The return differential is not close.

The negative-space rule is the curation discipline that makes compounding possible. What you exclude from a portfolio defines its point of view as clearly as what you include. Three to six projects, selected on archetype-alignment rather than technical difficulty or recency, with a named exclusion decision for every project left out. If everything is on the portfolio, nothing is the point of the portfolio.

The case study is the artifact that converts a hiring manager's filter pass into a forward motion. Four functions — frame the problem, show the technical work, connect to brand, be honest about limits — and specific, verifiable metrics where most student case studies offer marketing claims.

The Feynman test: show your portfolio to someone who has never heard your pitch and ask them to name your archetype, your positioning, and your strongest project — unprompted, in two minutes. If they can, the portfolio is legible. If not, you have more curation work to do.

---

## Connections Forward

Chapter 12 builds the final two-part pitch: the 10/20/30 presentation and the assembled portfolio handoff. The portfolio you deploy here is the artifact the Chapter 12 pitch drives traffic to. Write the README with Chapter 12 in mind. The presentation says "here is what I built and why it matters"; the portfolio says "here is the evidence."

Chapter 12 also finalizes the resume and the LinkedIn profile. The coherence audit you run in this chapter identifies the misalignments Chapter 12 will close. Run the audit now so the Chapter 12 work is revision, not construction.

**What would change my mind:** Strong evidence that hiring outcomes for AI engineers are uncorrelated with portfolio quality when controlling for technical skill, network, and timing. Chiang's career trajectory is consistent with the portfolio-compounding hypothesis but it is not proof — she had excellent technical skills, good timing, and a strong network that may have been more causal than the portfolio. A study comparing hiring outcomes for engineers with high-craft portfolios versus adequate portfolios, controlling for technical skill, would either strengthen or weaken this chapter substantially. I expect a real effect; I cannot prove it with the rigor I would want.

**Still puzzling:** The trade-off between distinctive portfolio design and clonable design. Chiang's site became influential partly because it was distinctive and simple enough to clone. Some highly distinctive sites are too idiosyncratic to template — they compound in Channel 2 but not Channel 3. Some clonable sites are too generic to be memorable — they compound in Channel 3 but not Channel 2. My best current heuristic: optimize for Channel 2 first (make it worth referencing), and let Channel 3 follow if the design is also clean enough to clone. I do not have a principled rule for finding that middle path deliberately.

---

## Exercises

### Warm-Up

**W1.** The chapter describes three compounding channels: direct hiring, indirect reference, and template effects. For each channel, write one concrete action you could take — while building the portfolio — that would increase its performance in that specific channel. The actions should be different for each channel; optimizing for one does not automatically optimize for the others.
*Tests: Objective 2 — identifying the three compounding channels.*
*Difficulty: Low.*

**W2.** Apply the negative-space rule to the following two hypothetical project lists. For each list, identify which two or three projects you would feature, which you would remove, and — for each removal — one sentence explaining what the portfolio's point of view would be undermined by including it.

- A Sage AI engineer: (a) a sentiment analysis pipeline for competitor news, (b) a to-do list app in React, (c) a survey analysis tool using clustering, (d) a personal finance tracker, (e) a RAG-based document Q&A system.
- A Creator AI engineer: (a) a multi-agent content generation pipeline, (b) a brand-voice classifier, (c) a CRUD web app for a client, (d) a prompt engineering library published on GitHub, (e) a student-project data visualization from three years ago.

*Tests: Objective 3 — curating with the negative-space rule.*
*Difficulty: Low-medium.*

**W3.** Write a five-item coherence audit checklist, with a specific yes/no question for each item answerable by someone who has never met the candidate. Then apply your checklist to a portfolio you can find online — not Chiang's, which is already discussed — and report the results.
*Tests: Objective 6 — auditing coherence across surfaces.*
*Difficulty: Low-medium.*

### Application

**A1.** Write the AI tool case study using the four-function structure: frame the problem, show the technical work, connect to brand, be honest about limits. Use your actual tool from Chapters 4–7. Length: 800–1,500 words. Include placeholders where you would embed a hero screenshot, architecture diagram, interface screenshots, and results image.
*Tests: Objective 4 — writing the AI tool case study.*
*Difficulty: Medium.*

**A2.** v0 and Framer make different tradeoffs. For each of the following portfolio types, choose between v0 and Framer and write a one-paragraph justification addressing: the primary job of the portfolio for this visitor, the technical signal the choice sends, and the visual control requirements given the brand strategy.

- A Sage AI engineer with a minimal, data-forward visual identity.
- A Creator AI engineer with expressive typography and bold color.
- A Caregiver AI engineer with warm, accessible tones.

*Tests: Objective 5 — selecting the deployment tool.*
*Difficulty: Medium.*

**A3.** Run the coherence audit on Brittany Chiang's portfolio (v4 at [github.com/bchiang7/v4](https://github.com/bchiang7/v4) and the deployed site). Use your five-item checklist from W3. Report which checks pass, which fail if any, and what the overall coherence verdict is. Then identify one specific change that would strengthen the archetype signal without altering the design.
*Tests: Objective 6 — conducting the coherence audit.*
*Difficulty: Medium.*

**A4.** Apply the LinkedIn optimization pass from this chapter to a profile — either your own or a hypothetical one for a specific archetype and positioning. Write: the new headline, the new about section (two to four paragraphs), a list of three items for the featured section, one rewritten experience description, and a pruned skills list of no more than twelve items. Annotate each choice with a one-sentence justification.
*Tests: Objective 6 — LinkedIn as a brand surface.*
*Difficulty: Medium.*

### Synthesis

**S1.** The chapter argues that adequacy is the portfolio's main failure mode — that an adequate portfolio gets through the filter but does not compound. Find a counterargument: identify a career context in which building an adequate portfolio is the *correct* strategic choice. What are the conditions under which portfolio compounding does not matter — where Channel 1 is sufficient and Channels 2 and 3 are irrelevant? Conclude with a statement of when the chapter's advice applies and when it does not.
*Tests: Objectives 1 and 2; stress-tests the chapter's central claim.*
*Difficulty: Medium-high.*

**S2.** The "Still puzzling" note identifies the tension between distinctive design and clonable design. Analyze three portfolios — one that optimizes for Channel 2 (memorability), one that optimizes for Channel 3 (templateability), and one that attempts both. For each: what specific design choices produce the channel optimization? What is sacrificed? Does the attempt to optimize for both in the third portfolio succeed or fail, and why? Conclude with your own rule of thumb for navigating the tradeoff.
*Tests: Objectives 1, 3, and 5.*
*Difficulty: High.*

**S3.** The chapter frames the portfolio as the convergence point of all prior work. Write a one-page diagnosis of a hypothetical student whose portfolio fails despite each component being individually strong: the archetype is clear, the tool is deployed, the brand strategy is documented, the visual identity is distinctive, the narrative is written. What specific failure at the integration stage could produce a weak portfolio from strong components? What is the structural fix?
*Tests: Objectives 1, 3, 4, and 6.*
*Difficulty: High.*

### Challenge

**C1.** The "What would change my mind" note identifies the limits of the correlational evidence for portfolio compounding. Design a study that could establish whether portfolio quality causally affects hiring outcomes for AI engineers. Specify: the population, how you would operationalize "portfolio quality" in a measurable and non-circular way, the dependent variable, the control variables (especially technical skill, network, and timing), the randomization strategy, and the minimum effect size you would need to change the chapter's recommendation. Evaluate whether the study is ethical, practically feasible, and what the most likely confound would be.
*Tests: Objective 1; stress-tests the chapter's empirical claim.*
*Difficulty: Very high.*

**C2.** The negative-space rule says that what you exclude defines the portfolio's point of view. Apply this rule to the entire job-search stack — portfolio, LinkedIn, resume, GitHub, email signature — and design a coherent exclusion strategy for a specific archetype (your own, or one you specify). Name at least ten specific things you would exclude across the five surfaces, justify each exclusion in terms of the archetype, and predict what brand signal each exclusion sends to the recruiter who notices the absence. Then identify the one exclusion that is hardest to defend — the thing you want to include but the archetype logic says to leave out — and make the argument for the archetype's position.
*Tests: Objectives 3 and 6; extends the negative-space rule beyond the portfolio to the full brand surface stack.*
*Difficulty: Very high.*

---

## LLM Exercise — Self-as-Project

**Project:** Self-as-Project
**What you're building this chapter:** A **deployed portfolio at a public URL**, archetype-aligned, with the AI tool you built in Chapters 4–7 integrated as a centerpiece case study.
**Tool:** Claude Code or v0.app — recommend v0 for most learners; Claude Code if you want to own the codebase.

**The Prompt:**

```
Generate a personal portfolio site for me using React + Tailwind + shadcn/ui.
The site should match the Personal Visual System v1 I produced in Chapter 9
(palette, typography, layout grid, archetype) and use the content I produced
in Chapter 10 (origin story, case study, thought-leadership piece).

Pages required:

1. HOME. Above the fold: my name, my one-sentence positioning (from Brand
   Strategy Ch 8), a clear primary CTA. Below: a "Selected Work" section
   with 3 project cards (use placeholders if not yet filled in). A "Writing"
   section with at least one published piece.

2. ABOUT. My origin story (from Chapter 10). Photo placeholder. Optional
   values list (from Brand Strategy). Contact-me CTA.

3. WORK / CASE STUDIES. List of all case studies as cards. One detail page
   per case study (use my Chapter 10 case study as the template).

4. WRITING. Index of published pieces. Each piece links to its published
   location — do not republish in full on the portfolio.

5. CONTACT. Email, LinkedIn, GitHub, optionally Twitter/X. No contact form
   unless I specifically want one.

Visual constraints:
- PALETTE: [paste your Chapter 9 palette hex codes]
- TYPOGRAPHY: [paste your Chapter 9 type pair, with sizes]
- ARCHETYPE: [paste your archetype name]
- TONE: [paste 3 tone words from your Chapter 9 brief]

Behavior constraints:
- Mobile-responsive at 375px, 768px, 1280px.
- WCAG AA contrast across all text.
- All images have alt text.
- Keyboard-navigable end to end.
- Lighthouse performance score 90+ on deployed version (no auto-playing
  media, images compressed).

Generate React components for all five pages plus shared header/footer.
Use shadcn/ui components where appropriate. Use Tailwind utility classes.
No CSS-in-JS.

After generating: deploy to Vercel (v0 makes this one click), or output the
file structure for Claude Code deployment. Give me the public URL when live.

Then audit your own output: name three things you would change before
sending recruiters there. Self-criticism, not affirmation.
```

**What this produces:** A live, deployed portfolio at a public URL. The most important single artifact of the semester for the job search. Every piece of work from Chapters 1–10 converges here.

**How to adapt:** If you already own a `.dev` or `.com` domain, point it at the Vercel deployment. If not, register one this week — your name, or an archetype-aligned word. The whole semester's work compounds at this URL; own the domain.

**Preview of next chapter:** Chapter 12 builds the final two-part pitch — the 10/20/30 presentation and the assembled portfolio handoff — and finalizes the resume and LinkedIn for the full job-search launch.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Charles and Ray Eames** built their portfolio across furniture, film, exhibitions, photography, and graphic design — the molded plywood chair, the Lounge Chair, the *Powers of Ten* short film, the IBM World's Fair pavilion, the Eames House itself — over four decades from 1941 onward. The portfolio reads as a single body of work, despite covering categories that have nothing to do with each other, because every piece is governed by the same design philosophy: rigorous problem framing, materials honestly used, the human experience as the unit of measurement. The chapter's argument that the portfolio is a *product* — a coherent artifact that compounds over time, not a directory of unrelated projects — is the Eames operating principle, applied to the Creative Engineer's first decade.

![Charles and Ray Eames, c. 1950s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](../images/charles-and-ray-eames.jpg)
*Charles and Ray Eames, c. 1950s. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who were Charles and Ray Eames, and how does their portfolio — varied across
furniture, film, and exhibition design but unified by a single design
philosophy — connect to the chapter's argument that the portfolio is itself
a product, with one coherent thesis underneath every artifact? Keep it to
three paragraphs. End with the single most surprising thing about their
career or ideas.
```

→ Search **"Charles and Ray Eames"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain how a portfolio across unrelated mediums can still cohere, in plain language
- Ask it to compare the Eameses' *Powers of Ten* to a Creative Engineer's case-study writing
- Add a constraint: "Answer as if you're writing the connecting thesis statement for a Creative Engineer's first ten-piece portfolio"

What changes? What gets better? What gets worse?

---

*Tags: portfolio · v0-vercel · framer-ai · brittany-chiang · linkedin-optimization · case-study · compounding · negative-space · coherence-audit · INFO-7375*
