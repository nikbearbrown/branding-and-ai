# Chapter 7 — Brand Architecture & Portfolio
*Every brand is a system of brands. The question is whether you designed the system or inherited it.*

> **TL;DR:** Real branding manages *systems* of brands — the structural choice that decides naming, how equity flows between offerings, and how risk is contained. This chapter teaches the branded-house ↔ house-of-brands spectrum, sub-brands and endorsements, extension and co-branding, and has you map and decide the architecture for your brand (yes — even a personal brand has sub-brands).
>
> | Section | Preview |
> |---|---|
> | The Relationship Spectrum | The range from one master brand to many independent brands, and the trade-offs along it. |
> | Sub-brands and Endorsements | The middle of the spectrum: when to qualify a master brand vs. let a child stand alone. |
> | Extension and Its Risk | Stretching a brand to new offerings — the leverage and the dilution it carries. |
> | Co-branding and Ingredients | Borrowing equity through partnerships, and what each party risks. |
> | Pruning Is Strategy | Why more brands usually means less value, and how to decide what to cut. |
> | Worked Example: Map Your Portfolio | Mapping the chosen brand's offerings and choosing an architecture with AI's help. |

---

P&G owns Tide, Pampers, Gillette, and Crest — and most shoppers have no idea they share a parent. Google owns Search, Android, YouTube, and Waymo — and brands some of them tightly to Google and lets others run free. These are not accidents of history; they are *architecture* decisions, and they govern how each company names, launches, and protects everything it makes. This chapter is about that layer — the system of brands — which the book had ignored by treating every brand as a single, standalone thing.

## The Relationship Spectrum

Aaker and Joachimsthaler's **Brand Relationship Spectrum** (*Brand Leadership*) is the canonical map, running between two poles:

- **Branded House** — one master brand stretched across everything (Google, Apple, Virgin, FedEx). Efficient: every product builds the same equity; one reputation to manage. Risky: a failure anywhere stains the whole.
- **House of Brands** — a portfolio of independent brands with the parent invisible (P&G, Unilever). Risk-isolated and precisely targeted: Tide can fail without touching Pampers. Expensive: each brand must be built from scratch.

In between sit **sub-brands** (the master brand plus a descriptive child — Apple → iPhone) and **endorsed brands** (an independent child blessed by the parent — Courtyard *by Marriott*).

The choice is a theory of how equity and risk should flow. A branded house bets on shared reputation; a house of brands bets on containment and targeting.

## Sub-brands and Endorsements

The middle is where most real decisions live. **Sub-brand** when the new offering benefits from the master's equity and is close to its core (iPhone trades on Apple). **Endorsed brand** when the offering needs its own identity for a different audience but still wants the parent's credibility as a trust signal (Marriott's tiers serve different travelers under one reassurance). The test: how much does this offering want to borrow from the parent, and how much does it need to differ?

## Extension and Its Risk

A **brand extension** uses existing equity to enter a new category (line extension = same category, new variant; category extension = new category). Extensions are equity *leverage* — and dilution *risk*. Kapferer and Aaker both warn that each extension reshapes the parent's associations. Stretch too far and the brand means nothing specific (the "elastic brand" snaps). The discipline: does the extension reinforce the core associations, or blur them?

## Co-branding and Ingredients

Two brands can combine equity. **Co-branding** (Nike × Apple) pairs two consumer brands for mutual lift. **Ingredient branding** (Intel Inside, Gore-Tex) brands a component inside another product. Both borrow trust — and both expose each partner to the other's failures. The risk is symmetric: you inherit your partner's crises.

## Pruning Is Strategy

The counterintuitive rule: more brands usually means *less* total value. Portfolio bloat splits attention, budget, and equity across offerings that cannibalize each other. The strongest portfolio moves are often subtractions — killing or merging brands so the survivors concentrate equity. For your project: every offering must earn its place by carrying distinct, valuable associations.

## Worked Example: Map Your Portfolio

Even a personal brand is a portfolio — your projects, talks, products, and public writing are sub-offerings that either reinforce one identity or scatter it. This chapter adds an architecture map: the offerings, their relationships, and a decision about which model you're running.

---

## AI+1 — Self-as-Project on Madison

**Project:** Self-as-Project — *your brand, end to end*
**This chapter adds:** a brand-architecture decision + portfolio map.
**Madison recipe:** [`madison-brand-portfolio-dashboard`](../madison/recipes/madison-brand-portfolio-dashboard.md)

> The dashboard maps and surfaces overlap; *you* choose the architecture and what to prune. The cut is the +1.

### Exercise 1 — When to Use AI
- *Inventory the brand's offerings/sub-brands into a grid.* **Why it works:** reformatting.
- *Surface overlap and cannibalization across offerings.* **Why it works:** pattern-spotting.
- *Draft the spectrum placement options.* **Why it works:** generating options.

**Tell:** you can defend each placement against the trade-offs.

### Exercise 2 — When NOT to Use AI
- *Choosing the architecture model.* **Why it fails:** a strategic equity/risk bet.
- *Deciding what to prune.* **Why it fails:** a values + resource judgment.
- *Approving an extension.* **Why it fails:** dilution risk requires brand judgment.

**Tell:** you've crossed the line when "the dashboard suggested it" replaces the architecture rationale.
**Series connection:** Tier 5 (causal) — reasoning about how equity flows, not just listing offerings.

### Exercise 3 — Recipe Exercise
**Build:** a portfolio map + architecture decision. **Run:** [`madison-brand-portfolio-dashboard`](../madison/recipes/madison-brand-portfolio-dashboard.md). **Tool:** Claude / Claude Code.

```
Using the Madison brand-portfolio-dashboard recipe approach, from my list of
offerings below: (1) map them on the branded-house ↔ house-of-brands spectrum;
(2) flag overlaps/cannibalization; (3) propose sub-brand vs. endorsed treatment
for each. Recommend, do not decide. Note one extension that would dilute the core.

Offerings:
[PASTE]
```
**Adapt:** personal brand → offerings are your projects/talks/products.

### Exercise 4 — CLI Exercise
**Build:** `your-brand/architecture.md`. **Tool:** [`wrap-your-tool`](../madison/wrap-your-tool/) or Claude Code.

```
Write your-brand/architecture.md: offering | relationship to master (branded/
sub/endorsed/independent) | equity it borrows | overlap risk. End with my chosen
model and a one-line "what to prune". Invent no offerings. Stop after writing.
```
**Inspect:** every offering has a relationship + rationale; a prune candidate is named. **If it goes wrong:** the model adds offerings you don't have — remove them.

### Exercise 5 — AI Validation Exercise
**Validate:** the architecture map. Pass / Fail / Cannot-determine + evidence:
- **Correctness:** does each placement match the spectrum definitions?
- **Completeness:** all offerings placed; overlaps flagged?
- **Scope:** architecture only — not a full identity redesign?
- **Brand-specific:** does the model fit the brand's equity-and-risk reality?
- **Failure-mode:** any recommended extension that would actually dilute the core?
**AI Use Disclosure:** two sentences — what the dashboard produced; one thing it could not decide (the architecture/prune) that needed your judgment.

---

## Key terms
brand architecture · Brand Relationship Spectrum · branded house · house of brands · sub-brand · endorsed brand · brand extension (line / category) · co-branding · ingredient branding · portfolio pruning · cannibalization.

## Bridge
You've structured the system of brands. Chapter 8 names them — and protects the names — where branding meets trademark law.
