# Module 20 — ShipIt: Product Requirements and Scope: Wonder Edition
## Companion Chapter

> **Wonder Edition:** Read this alongside the chapter, not instead of it.

**Content note:** Despite the filename "20-shipit-product-requirements-and-scope," this chapter is filed as Appendix S1 in the book. This companion follows the actual chapter content.

## The Strange Question

Linear is a project management tool that competes with Jira and Asana. It has fewer features than both. It is less configurable than both. Enterprise customers have offered significant annual contracts — the chapter names a $100,000-scale customization request as the representative example — and Linear has declined them.

Linear reached $35 million ARR in 2023 with a lean team and a product that, by design, does fewer things than its competitors.

The inverse also exists: a product that accepts every reasonable customization request from every enterprise customer who offers to pay for it. Over time, the product accumulates features, configuration surfaces, and branching logic. It becomes slower, more complex, harder to maintain, and harder to explain. The original users — the ones who came for the discipline — quietly move on.

How can saying no to a feature that a customer will pay for make a product more valuable, and how can saying yes to the same feature destroy it?

## First Intuition

The intuitive model: product decisions are accumulative. Each feature added is value added. Customer willingness to pay is the best signal that a feature is worth building. Refusing a paying customer is leaving money on the table. The product grows by growth.

This model feels right because it is individually rational at each decision point. A specific enterprise prospect, with a specific use case, offering a specific dollar amount, represents real value. The feature they want is not technically difficult. The argument for adding it is concrete and immediate. The argument against it is abstract and future-facing. The immediate wins; the abstract loses.

> **► Planning prompt:** Before reading further, write down your model of how to decide what to put in and out of a v1 product. Is the right filter "will users pay for this?" or something else? If an enterprise customer offered you $100,000 for a feature that would take two weeks to build, what would you need to know before deciding whether to build it? Write it down before continuing.

## The Surprise

But scope discipline compounds in a direction that individual feature decisions cannot predict. The chapter's mechanism: each time a product refuses a feature that would compromise the core, it preserves the coherence of the experience that made the product worth using. Over time, coherence becomes identity. Identity becomes brand. Brand attracts more users who value that specific coherence, which deepens it further.

Linear's product is faster than Jira because every rejected enterprise customization is also a rejected source of UI complexity, rejected backend branching logic, rejected on-call incident surface. The no to the customer is simultaneously a yes to speed. The $100,000 no is not just discipline — it is the mechanism that produces the experience engineers recommend to other engineers when they want to escape Jira.

The inverse compounds too. Each yes to a feature that compromises the core spends coherence for cash. The transaction is rational in the moment. Over time, the accumulated incoherence drives away the users who came for the discipline. The product looks fine from the inside — it has more features, more revenue — and has quietly lost what made it worth using.

> **► Monitoring prompt:** In your own words, describe what your initial model assumed about the relationship between scope decisions and product value. What specific mechanism does Linear's coherence-index trajectory reveal that the feature-accumulation model misses? What does your current model still fail to explain about why the $100,000 no is more valuable than the $100,000 yes in the long run?

## The Hidden Structure

Therefore, the PRD's deepest function is not specification — it is commitment. A PRD written before development is a contract with future-self: a record of the decisions made when thinking was clear, preserved for the moment when pressure arrives. The pressure always arrives. The customer is real, the budget is real, the feature is technically feasible. The PRD's out list, with the $100,000 no at its head, is the document that answers the question "should we build this?" not by re-evaluating it under pressure, but by having already evaluated it clearly.

The one-page PRD has four sections: Problem (specific user, specific task, specific frequency, specific cost), Gap (named competitors, specific failure modes for each), Tool (deliverable in user-facing terms, nothing technical), and MVP Boundary (explicit in-scope and explicit out-of-scope, with the $100,000 no first).

The what-versus-how discipline is the structural rule. The PRD specifies what the product does; engineering decides how. "The tool sends users a daily email summary" is a what. "The tool sends users a daily email summary via SendGrid at 7 a.m. Eastern using a Handlebars template" is a how in what's clothing. The how ends up in the PRD and gets treated as a requirement — and when implementation needs to change, the PRD becomes a source of false constraints.

> "It is tempting to think product scope decisions are made optimally one feature at a time — that customer willingness to pay is the right filter at each decision point and that a product grows by accumulating valuable additions. But Linear's coherence-index trajectory shows that scope discipline compounds: each refusal of a feature that compromises the core preserves the coherence that attracted users in the first place, while each acceptance of such a feature spends coherence for immediate cash. The correct model holds that the out-of-scope list is as important as the in-scope list, and that the $100,000 no — the feature refused despite real cost — is the mechanism that preserves coherence over time. The key distinction is between scope management as resource allocation (we cannot build everything) and scope discipline as identity (we refuse specific things to preserve the coherence of what we are)."

**The weak-vs-strong PRD comparison:**

| Section | Weak version | Failure mode | Strong version |
|---|---|---|---|
| Problem | "Marketing professionals need better competitive intelligence." | No user, no frequency, no cost | "Marketing managers at small B2B SaaS spend 2–3 hours every Monday manually aggregating competitor news — no tool does aggregation, filtering, and scoring in one step at their price point." |
| Tool | "An AI-powered competitive intelligence platform." | Marketing language — unbuildable | "A self-hosted n8n workflow pulling up to 10 RSS feeds, deduplicating by title similarity, scoring sentiment via GPT-4o-mini, and writing a daily summary to Google Sheets for under $20/month." |
| Out list | 2 generic items | Deferred in-list, not a boundary | 8 named exclusions, each with an archetype reason, the $100,000 no first |

## Try Looking At It This Way

**Target:** MVP boundary discipline — the practice of writing an explicit, named out-of-scope list before development begins, with the $100,000 no as the highest-priority exclusion, preserving the core experience that makes the product worth using.

**Base:** A restaurant's opening menu.

**Features:**
- The product corresponds to the restaurant
- The MVP boundary corresponds to the opening menu
- The $100,000 no corresponds to a dish the chef can technically make but has chosen not to offer because it does not fit the kitchen's concept
- A customer's request for an off-menu item corresponds to the enterprise customer's customization request
- The coherence of the dining experience corresponds to the coherence of the product experience

**Commonalities:** In both systems, what is absent from the menu is as defining as what is present. A restaurant that says yes to every off-menu request becomes a catering operation — it can execute any dish, but has no identity. The kitchen's mise en place, the sourcing relationships, the staff training are all calibrated to a specific menu; adding an off-menu dish at the last moment taxes each of those calibrations. A restaurant that maintains a specific menu — and declines requests for items that do not fit — produces a coherent dining experience and builds an identity that attracts guests who want exactly that experience. The $100,000 no for a product is the off-menu request the chef declines: not because it is impossible, but because saying yes would compromise the calibration of everything else.

**Boundaries:** A restaurant menu is evaluated by the experience of the meal — the diner's assessment is formed during a single visit and is primarily sensory. A product's coherence is evaluated across many sessions, by users who are also evaluating competitors, and whose standard for "coherent" evolves as they use the product more. A restaurant that adds one off-menu item does not necessarily become incoherent; a product that adds one feature that compromises the core may immediately register as incoherent to power users who have internalized the product's specific model. The restaurant analogy implies a more forgiving standard for coherence than product reality supports — one deviation from the menu is a special occasion; one architectural compromise in a product may be visible immediately to the users who came for the discipline.

**Conclusions:** Write the $100,000 no before writing anything else in the PRD. The out-of-scope list is the identity document; the in-scope list is the feature list. Both are required; the out list takes more discipline to write because every item on it is something someone wanted.

## Where The Analogy Breaks

Unlike a restaurant menu, which is changed seasonally or when customer feedback is strongly negative and consistently so, a product's scope decisions are made under continuous pressure from individual customers with specific, funded requests. A restaurant can close to new diners while it recalibrates the menu. A product team cannot pause development while it reconsiders every scope decision every sprint. This means the product team's equivalent of the menu discipline must be pre-decided and documented — the PRD's out list — rather than re-evaluated in real time at the moment of each request. A restaurant chef can say "no, that's not something we do" spontaneously and authoritatively; a product team that says "no" without documented rationale appears arbitrary to the customer making the request. The PRD's $100,000 no must be written in advance of the pressure, because the pressure — the funded customer with the specific request — does not arrive until development is already underway and re-evaluation is costly.

## Small Discovery

**Raw data:**

A city's public library system needed to decide which services to offer at a new branch in a mixed-use neighborhood. The library commission gathered community feedback and identified twelve services that residents wanted: computer labs, children's programming, adult literacy classes, community meeting rooms, 3D printing, seed library, tool lending, seed saving workshops, a makerspace, language learning programs, small business advisory, and a coffee shop partnership.

The branch had 4,200 square feet and a staff of six.

The commission chair proposed a rule: identify the three services that would be used by the most people the most often, and design the branch around those three. Every other service would be deferred to a later phase or referred to partner organizations.

Selected services: computer labs, children's programming, community meeting rooms.

Three-year utilization data:

| Metric | This branch | System average |
|---|---|---|
| Weekly active visitors | 1,840 | 890 |
| Program attendance / week | 412 | 198 |
| Staff overtime incidents / year | 3 | 31 |
| New library card registrations / year | 1,140 | 520 |

**Pattern search:** The branch that offered three focused services outperformed the system average on every metric, including metrics (new registrations, active visitors) that would seem to favor the branches offering more diverse services. What mechanism explains this — and what would the PRD's problem statement discipline say about why the commission chair's rule worked?

**Prediction:** If the commission added seed lending and 3D printing in year two — two high-interest services from the original community feedback list — would weekly active visitors go up, go down, or stay the same? Write your prediction before continuing.

---

**Revelation:** The focused branch built an identity that potential visitors could understand and remember. "Computer labs, children's programming, and community meeting rooms" is a comprehensible, memorable scope. Someone deciding which library to visit could predict their experience. Adding seed lending and 3D printing in year two would likely produce modest positive effects in the short term (new users attracted by the new services) and negative effects in the medium term: staff attention divided across more service types, operational complexity increased, the focused identity diluted. The branch's above-average performance came from the scope discipline, not from any individual service. The MVP boundary discipline — write the $100,000 no before development begins, maintain it under pressure — is exactly what the commission chair's rule institutionalized before the branch opened.

## What This Changes

1. **What question can the reader now answer?** Why Linear's $100,000 no was not a missed revenue opportunity but the mechanism that produced the coherent experience engineers recommend to other engineers — and why accepting the same feature would have spent coherence for cash in a way that compounds negatively.

2. **What looks different in a specific design decision?** The decision about what to put in the out-of-scope list. Before this chapter, the question is "what can we not build?" — a resource question. After this chapter, the question is "what would we decline even if we could build it, and why?" — an identity question. The out list is the product's point of view.

3. **Practice Bridge:** The student can now write their own product PRD with an explicit $100,000 no. The no goes first in the out-of-scope column. It is a feature that a real user will request, with a real argument for why it belongs in the product, and that the student declines anyway because including it would compromise the core. Writing the no requires having a point of view strong enough to hold under pressure — and holding it under the simulated pressure of writing the refusal down is the practice for holding it under the real pressure of the funded customer's request.

4. **What question does this leave open?** The PRD specifies the what. The next appendix (Pipelines and Workflow, Module 21) addresses the how — the pipeline architecture that implements what the PRD specifies. The Build-Measure-Learn loop requires that the MVP boundary be tight enough that the build takes weeks, not months; the pipeline architecture determines whether that constraint holds.

## Wonder Questions

1. The chapter says the $100,000 no is "disciplined precisely because it acknowledges the cost." A student whose AI tool has no paying users yet cannot have a $100,000 no in any literal sense — they have no enterprise customers offering real money. What is the student equivalent of the $100,000 no? What feature would you decline even if a hypothetical user asked for it compellingly, and what does naming it tell you about the product's core?

2. The PRD distinguishes "what the product does" from "how it does it" — the what-versus-how discipline. But some what decisions force a how: "the tool deduplicates articles" implies a deduplication mechanism, and different mechanisms produce different accuracy rates, which means the what is not fully separable from the how. Where is the actual boundary between what and how, and what is the test for whether a requirement has crossed it?

3. The Build-Measure-Learn loop works only if you know, before building, which assumption you are testing. A student building an AI tool for the first time has multiple untested assumptions simultaneously: that the problem is real, that users will open the output, that the format works, that the pricing is acceptable, that the technical implementation is reliable. Can you test more than one assumption in a single MVP, or does the PRD's hypothesis-per-build discipline require selecting one? What determines the priority?

4. The chapter's "still puzzling" section identifies the moment when scope discipline tips from productive constraint to sterile rigidity. Linear's discipline is grounded in a coherent point of view about how engineering teams should manage work. A student without a coherent point of view applying the same discipline can end up refusing features for no good reason. How do you distinguish a principled refusal from a reflexive one? What question would reveal the difference?

5. The PRD says to name actual competitors in the gap analysis and explain exactly what each gets wrong for the specific user. For a student building a first AI tool, the "named competitors" may be incumbent processes (spreadsheets, email threads, manual review) rather than other software products. Is a gap analysis against a manual process valid, or must the comparison be against an existing product? What changes about the analysis when the primary competitor is a behavior rather than a tool?

---

> **What the concept is:** MVP boundary discipline — the practice of writing an explicit, named out-of-scope list before development begins, with the $100,000 no as the first item, preserving the product's core coherence by refusing features that would compromise it even at real cost, and making the refusal a pre-committed record rather than a live judgment under pressure.
>
> **What it explains:** Why Linear reached $35M ARR with fewer features than Jira; why accepting a $100,000 customization request can destroy more value than it creates; why the PRD's out list is as important as its in list; why "cannot substantiate" in a claim-proof map and "out of scope" in a PRD are the same structural discipline applied to different domains.
>
> **What it does NOT mean:** That small products should refuse growth. The $100,000 no is not a refusal of growth — it is a refusal of incoherent growth. Features that advance the core, serve the target user, and fit the archetype belong in v2 after v1 has validated the hypothesis. The discipline is about which features to refuse at which stage, not about refusing all expansion permanently.
>
> **What comes next:** The PRD is the contract that specifies what to build. Module 21 (pipelines and workflow) addresses the build itself — the pipeline architecture that implements the PRD's in-scope list with the engineering discipline of treating every external dependency as a contract that will change.
