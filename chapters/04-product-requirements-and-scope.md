# Chapter 4: Product Requirements and Scope

> **Voice anchor:** `voice-unanchored`. Voice for this draft is Feynman per CLAUDE.md §6 + textbook:chapter SKILL.md.

## Suggested titles

1. *The $100,000 No*
2. *Scope as a Creative Constraint*
3. *Product Requirements and Scope*

## TL;DR

A PRD is not a document; it is a contract with future-you about what the product will be and — more importantly — what it will not be. Every "yes" to a feature is a "no" to the speed of shipping the core. The discipline compounds.

---

A startup is on the phone with a Fortune 500 prospect. The prospect wants Linear, the project-management tool, but with one customization. They want a particular workflow: an extra approval step inserted between *In Progress* and *Done* statuses, with an audit trail tied to a compliance calendar. They are willing to pay $100,000 a year for the customization. The startup is two years old.

The Linear team [says no](https://www.figma.com/blog/the-linear-method-opinionated-software/).

Not "let us see if we can do it." Not "we will put it on the roadmap." A flat no. Linear's published [product philosophy](https://linear.app/method/introduction) describes the move directly: their software is *opinionated*. It is built around a specific point of view on how engineering teams should work. Custom workflows that violate that point of view are not friction-free additions; they are doors into a different product. Once you ship the door, the next prospect asks for the next door. Two years later you have a Jira clone — slower, less coherent, and the original 10,000 customers who chose Linear for its simplicity have started looking for something else.

The $100,000 no is the work this chapter is about. Not because you should refuse every feature request — early on you cannot refuse anything; you do not have customers — but because the discipline that makes the no possible later is built at the PRD stage, before the first line of code.

By the end of this chapter you will be able to write a PRD for the AI tool you will build through Chapters 5–7. You will know what belongs in it, what does not, and how to think about the boundary that separates a focused product from a bloated one.

---

## What a PRD actually is

A Product Requirements Document is a written specification of what a product will do, who it is for, and what success looks like. The simplest version, from Marty Cagan and the Silicon Valley Product Group, has [four sections](https://www.cimit.org/documents/20151/228904/How%20To%20Write%20a%20Good%20PRD.pdf):

1. **Purpose** — why this product exists and what problem it solves.
2. **Features** — what the product does, in user-facing terms.
3. **Release criteria** — what has to be true before the product ships.
4. **Timing** — rough schedule and milestones.

That is it. A real PRD can be one page or twenty, but it answers those four questions. Cagan's enduring rule on PRDs: *the PRD specifies the what, not the how*. How the engineering team implements multi-tenant authentication is engineering's call. Whether the product needs multi-tenant authentication at all is the PRD's call.

This sounds simple. It is not. Most PRDs students write are too long, too vague, or both. A PRD that says "the product will help users be more productive" is not a PRD; it is a wish. A PRD that says "the product will support 47 features across 9 categories" is not a PRD; it is a wishlist that has not been pruned.

The version of the PRD I want you to learn to write fits on one page. It answers four questions clearly enough that another engineer could read it and know what to build. Here is the structure:

**Problem.** What specific problem are you solving? *For whom?* The audience must be a real person you can describe, not "everyone interested in AI." A good problem statement reads like: *Marketing managers at small B2B companies spend three hours a week manually compiling competitor news from RSS feeds and email digests, and the work is repetitive and error-prone.*

**Gap.** What exists already, and where does it fall short? Name actual competitors. Not "there are tools, but..." — name them. *Google Alerts is free but noisy and uncategorized. Feedly Pro aggregates well but has no sentiment analysis. Brand24 has analytics but starts at $99/month.* A real gap analysis tells the reader why your product needs to exist.

**Tool.** What will you build? One sentence, plain language. *A self-hosted RSS-to-sentiment pipeline that gives a marketing manager a daily Google Sheet of categorized, scored competitor news for under $20/month in API costs.* That is a tool. "An AI-powered platform for marketing intelligence" is not — it is a marketing slogan you accidentally put in the PRD.

**MVP boundary.** What is in scope for the first version, and — explicitly — what is out? The "out" list is more important than the "in" list. *In: 10 RSS feeds per user, sentiment scoring, daily email summary. Out: multi-user accounts, custom dashboards, social-media monitoring, mobile app.* The out list is the doors you are refusing to open in v1. It is the chapter's central discipline.

That is the whole PRD. One page. Four questions. The version your AI tool needs is not more complicated than that.

---

## Why scope is creative, not restrictive

The instinct most engineers bring to a PRD is to maximize. *List every feature; describe every edge case; don't leave anything out.* This produces a PRD that reads as comprehensive but ships nothing. The reason scope discipline is hard to teach is that it requires reframing the thing students think they are doing.

You are not building a description of every feature the product could have. You are building the smallest version of the product that delivers a complete experience to a real user, fast enough to learn from. That is an MVP — *minimum viable product* — and the term is doing more work than most students realize.

Eric Ries, who coined the term in his 2011 book *The Lean Startup*, [defined an MVP](https://leanstartup.co/resources/articles/what-is-an-mvp/) as "a version of a new product which allows a team to collect the maximum amount of validated learning about customers with the least effort." Three pieces of that sentence matter:

- **A version of a new product.** Not a prototype, not a pitch deck, not a Figma mock. A version of the product, with users.
- **Maximum validated learning.** The MVP's job is not to make the customer happy; it is to teach you whether the underlying assumption is right. If the customer is delighted but did not pay, the assumption was wrong. If the customer is grumpy about the polish but pays anyway, the assumption was right.
- **Least effort.** This is the constraint that produces the discipline. Anything that does not contribute to validated learning gets cut.

The pattern Ries names — *Build, Measure, Learn* — is a feedback loop. You build the smallest thing that tests an assumption, measure what users do with it, learn whether the assumption held, and update the next build. The PRD's scope discipline is what makes this loop tight. A PRD that scopes too widely takes too long to ship; you build for six months, learn nothing, and spend another six months iterating on a product no user has touched yet.

The reframing: *what features to leave out* is the real PRD work. Inclusion is automatic — every team member has features they want to add. Exclusion requires judgment, and judgment is what the document records.

A useful test, when looking at any feature on your "in scope" list: *what does shipping without this feature feel like?* If the answer is "the product still does the core thing, just with rougher edges" — keep it out for v1. If the answer is "the product cannot be used at all" — keep it in. Most features fall into the first category. Most students put them in v1 anyway.

### A worked case: the Linear PRD discipline

Linear is the cleanest public example of scope discipline as a brand commitment. The company [publishes its product method](https://linear.app/method/introduction) — the principles behind which features they include, which they decline, and how they think about the boundary.

The principles include "Build for the long term," "Say no to busy work," and "Start simple, evolve over time." These sound like every startup's about page. The difference is that Linear *enforces* them. The Figma blog post on Linear's method describes the discipline directly: when an enterprise prospect asks for a workflow customization that violates Linear's point of view on how engineering teams should work, Linear declines. They do not build the customization, even at the cost of the contract.

Two consequences flow from this discipline. First, the product stays coherent. A user picking up Linear in 2026 finds a product that feels like the product Linear's earliest users picked up in 2019, only better. Second — and this is the part the chapter wants you to see — the *brand* is the discipline. Linear's identity is not a logo or a color; it is "the project management tool that says no." Engineers who hate Jira's bloat seek Linear out specifically because Linear has refused the requests that bloated Jira. The discipline produces the product *and* the brand together.

When you write your PRD, think about what your "$100,000 no" will be. What feature will you refuse, even when refusing costs you something? The answer to that question is your scope discipline made visible. You should be able to name it before you write the first line of code.

---

## Mapping your PRD against Madison

The Madison framework gives you a concrete reference architecture, and the framework's existing tools are the right size of PRD to study. Open `pantry/madison/Intelligence-Agent/README.md`. The README is, effectively, a PRD: it states the purpose ("real-time sentiment analysis, competitive benchmarking, actionable marketing insights"), the features ("multi-source data gathering, AI-powered analysis, competitive benchmarking, risk monitoring"), the release criteria ("production-ready, processes 870+ articles daily, sub-3-minute latency, 90% deduplication"), and the technology stack.

Read the Madison Intelligence Agent README before you write your own PRD. Notice what it does *not* include: it is not a research paper, it is not a marketing pitch, it is not exhaustive. It tells you what the agent does and what success looks like, and it stops.

When you write your own PRD, do the same. Find the Madison tool whose pattern most closely fits your archetype's chosen project, and use its README as the size and shape your PRD should be. If your tool is a research-style tool, study MarketMind. If your tool is a content-generation tool, study Content Agent. If your tool is a customer-experience tool, study the Experience Agent material. Pattern-match on shape, not on content. Your tool will solve a different problem; the PRD's *shape* will be familiar.

The PRD template you produce should be one page. Four sections: problem, gap, tool, MVP boundary. A short stack of technology choices ("we will use n8n for orchestration, OpenAI for analysis, Google Sheets for storage" — exactly the Madison stack, by the way, because Madison made those choices for the same reasons you should). A two-line statement of what success looks like at v1.

Then put it in front of one other person and ask them whether they can tell you what the tool does without paraphrasing your PRD back to you. If they have to paraphrase, the PRD is not specific enough. Rewrite.

---

## What you walk out with

A working PRD template. A definition of MVP that is not "the smallest possible thing" but "the smallest thing that produces validated learning." A scope-discipline mindset that treats every "out" decision as more important than every "in" decision. Linear's $100,000 no as a behavioral example of what scope discipline looks like under pressure.

I should be honest about the limits of this framework. PRD discipline does not guarantee a successful product; it guarantees a *coherent* one. A perfectly scoped PRD for a tool nobody wants is a clean failure. The mechanism the chapter describes — scope discipline as compounding advantage — assumes the underlying problem is real and the audience is reachable. The Build-Measure-Learn loop is what tests those assumptions. The PRD is what makes the loop fast enough to be useful.

Marty Cagan himself has [evolved past PRDs](https://www.svpg.com/discovery-vs-documentation/) — he now argues that high-fidelity prototypes do the work PRDs used to do, and that PMs should spend less time writing and more time discovering. The argument has merit. For a graduate course where students are building their first AI tool, a one-page PRD is a useful constraint that slows down the rush to code. By the time you are on your third or fourth product, the PRD may compress further into a prototype plus a one-paragraph note. That progression is fine. Start with the one-page PRD now.

---

## Embedded exercise: write your one-page PRD

Before Chapter 5, draft a one-page PRD for your tool with the four sections above:

1. **Problem.** Name a specific user, a specific pain, and a specific frequency. Avoid "everyone" and "always."
2. **Gap.** Name three actual competitors and what each is missing.
3. **Tool.** One sentence describing what your tool does. No marketing language.
4. **MVP boundary.** A two-column list — *In* and *Out*. The Out column should have at least three items.

Read your draft aloud to a classmate. If they cannot tell you what the tool does in their own words after reading it, rewrite the *Tool* section. If they can list features beyond your *In* column, rewrite the *MVP boundary*.

Bring the PRD to Chapter 5. Chapter 5 builds the data pipeline that the PRD's Tool section described.

---

**What would change my mind:** A controlled study of student-built AI tools showing that those built without an explicit PRD ship faster and reach more users than those built with one. The current evidence is correlational and largely industrial; the experimental case for PRDs in early-stage student work is thinner than I'd like.

**Still puzzling:** The exact moment when scope discipline tips from *useful constraint* to *creative restriction*. Linear's discipline is sharp because it is matched to a clear point of view on engineering teams. A startup with a vaguer point of view that practices the same discipline can end up paralyzed — refusing features without a coherent reason for doing so. The discipline depends on the point of view. I do not yet have a clean way to teach the point of view.

---

**Tags:** PRD · scope-discipline · MVP · lean-startup · linear · cagan · madison-architecture · INFO-7375
