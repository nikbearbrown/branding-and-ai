# Chapter 8 — Naming, Trademark & Brand Protection
*A great name you cannot own is a liability with good marketing.*

> **TL;DR:** Naming is where branding meets the law: the same spectrum that makes a name memorable also makes it protectable, and getting it wrong is expensive — sometimes fatal. This chapter teaches the trademark-strength spectrum, the difference between owning a name, a domain, and a company, and how to use AI to generate and pre-screen candidates while routing real clearance to a lawyer.
>
> | Section | Preview |
> |---|---|
> | Three Things You Think Are One | Why a name, a domain, and a company registration are separate rights. |
> | The Strength Spectrum | The scale from generic to fanciful that decides both memorability and legal protection. |
> | Likelihood of Confusion | The core test that decides whether a name infringes another. |
> | Clearance Before Commitment | The searches that catch a doomed name before you invest in it. |
> | What AI Can and Cannot Clear | Why AI generates names well and clears them not at all. |
> | Worked Example: Name and Protect | Generating, screening, and stress-testing a name for your brand. |

---

A startup spent six months and a chunk of seed money building a brand around a name, only to receive a cease-and-desist from a company in the same software class with a prior registration. The name was memorable, the logo was done, the domain was bought — and none of it mattered, because they never ran a trademark search. The name had to go, and with it the six months. Naming is the one branding decision that is also a legal decision, and the cost of treating it as purely creative is the highest in the book.

## Three Things You Think Are One

Founders routinely conflate three separate rights:

- **A trademark** — the legal right to use a name/mark for specific goods or services, enforceable against confusingly similar uses.
- **A domain** — a rented address. Owning `example.com` grants *no* trademark rights and vice versa.
- **A company registration** — an entity name with the state, which also is not a trademark.

You can hold all three, one, or none independently. "I bought the domain, so I own the name" is the most common and most dangerous error.

## The Strength Spectrum

US trademark law (the *Abercrombie* spectrum) ranks marks by distinctiveness, and — usefully — the same scale predicts memorability:

- **Generic** ("Software" for software) — never protectable.
- **Descriptive** ("Cold and Creamy" ice cream) — weak; protectable only after acquiring "secondary meaning."
- **Suggestive** ("Netflix") — hints at the benefit; protectable.
- **Arbitrary** ("Apple" for computers) — a real word, unrelated to the product; strong.
- **Fanciful** ("Kodak," "Xerox") — invented words; strongest.

The lesson cuts against intuition: descriptive names feel clear and safe but are the *hardest* to protect and easiest to get lost among. Arbitrary and fanciful names cost more to teach but are defensible assets.

## Likelihood of Confusion

Infringement turns on **likelihood of confusion** — would a reasonable consumer confuse your mark with an existing one in a related class? It's broader than an exact-string match: similar sound, appearance, meaning, and related goods all count. This is why a clean exact-match search is not the same as being cleared.

## Clearance Before Commitment

Minimum diligence before you commit:

- Search the relevant trademark register (in the US, the USPTO system) for the name *and phonetic variants*, in your goods/services class (software is typically Nice Class 9/42). `[verify current USPTO search tooling — TESS was replaced/updated.]`
- Check domain availability and acquisition cost.
- For anything beyond a quick screen, **consult a trademark attorney.** This book gives you literacy, not legal clearance — clearance is a lawyer's job, and this is a route-to-counsel chapter.

## What AI Can and Cannot Clear

AI is excellent at the *generative* half: producing dozens of candidates, classifying them on the strength spectrum, checking obvious domain availability, and flagging glaring conflicts. AI is dangerous at the *clearance* half: it will confidently assert a mark is "available" based on nothing, hallucinating the one fact that matters. Every AI "available" is `[verify with counsel]`. This is the chapter's sharpest AI+1 line.

## Worked Example: Name and Protect

For your running-project brand, this chapter adds a cleared (to first-pass) name plus a protection checklist. AI generates and screens; you decide; counsel clears.

---

## AI+1 — Self-as-Project on Madison

**Project:** Self-as-Project — *your brand, end to end*
**This chapter adds:** a name candidate set, first-pass screened, plus a protection checklist.
**Madison:** no recipe fits — **ad-hoc prompt (candidate for a future `madison-naming` recipe).** Clearance routes to counsel.

> AI generates and screens names; *you* choose; a lawyer clears. AI never clears a trademark — that's the +1 (and a hard legal line).

### Exercise 1 — When to Use AI
- *Generate name candidates across the strength spectrum.* **Why it works:** option generation.
- *Classify each candidate (generic → fanciful) + check domain availability.* **Why it works:** reformatting/retrieval.
- *Flag obvious conflicts and cross-language problems.* **Why it works:** pattern-spotting.

**Tell:** you can independently judge strength and memorability.

### Exercise 2 — When NOT to Use AI
- *Concluding a name is legally available.* **Why it fails:** hallucination of the one fact that matters; only a search + counsel clears it.
- *Choosing the final name.* **Why it fails:** a strategic + values call.
- *Interpreting likelihood of confusion.* **Why it fails:** a legal judgment.

**Tell:** you've crossed the line when an AI "it's available" becomes your reason to commit.
**Series connection:** Tier 4 (metacognitive) — knowing the AI cannot know this, and routing it to counsel.

### Exercise 3 — LLM Exercise
**Build:** a screened name shortlist. **Tool:** Claude.

```
Generate 15 name candidates for [MY BRAND], spanning the trademark-strength
spectrum (label each generic/descriptive/suggestive/arbitrary/fanciful). For each:
note memorability, obvious cross-language issues, and whether the .com is plausibly
available. Then shortlist 3 strongest-and-protectable. Tag EVERY availability/legal
note [VERIFY WITH SEARCH + COUNSEL]. Do not claim any name is legally available.
```
**Adapt:** add your archetype so candidates fit the brand's voice.

### Exercise 4 — CLI Exercise
**Build:** `your-brand/naming.md` + `your-brand/protection-checklist.md`. **Tool:** Claude Code.

```
Write your-brand/naming.md (shortlist: name | spectrum class | memorability | domain
status [VERIFY] | notes) and your-brand/protection-checklist.md (the three rights:
trademark search status, domain, entity — each a checkbox routed to the right owner,
counsel for the mark). Assert no legal availability. Stop after writing.
```
**Inspect:** every legal/availability item is tagged for verification; the three rights are separated. **If it goes wrong:** the model declares a name "cleared" — replace with [VERIFY WITH COUNSEL].

### Exercise 5 — AI Validation Exercise
**Validate:** the naming shortlist. Pass / Fail / Cannot-determine + evidence:
- **Correctness:** is each name classified on the spectrum correctly?
- **Completeness:** memorability + domain + conflict noted for each?
- **Scope:** screening only — no legal-clearance claim?
- **Brand-specific:** do shortlisted names fit the archetype?
- **Failure-mode:** any name asserted as legally available without [VERIFY]? Treat as a hard fail.
**AI Use Disclosure:** two sentences — what AI produced; the one thing it could not determine (legal availability) that required a search and counsel.

---

## Key terms
trademark vs. domain vs. entity · trademark-strength spectrum (generic / descriptive / suggestive / arbitrary / fanciful) · secondary meaning · likelihood of confusion · clearance search · Nice classification · trade dress · route-to-counsel.

## Bridge
You have a name you can own. Chapter 9 gives it a face — the visual identity system that makes the brand recognizable on sight.
