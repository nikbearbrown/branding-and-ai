# Chapter 13 — Measuring Brand Equity & Impact
*A number that moved is not a verdict. It is a question.*

> **TL;DR:** If a brand is an asset, you have to track it — and most teams track the wrong things or over-trust a single metric. This chapter teaches brand tracking, NPS and its limits, the difference between brand and performance metrics, and the hard problem of attribution, then has you build a measurement plan with honest baselines (and refuse the fabricated ones).
>
> | Section | Preview |
> |---|---|
> | What to Measure, and Why | The split between brand metrics and performance metrics, and what each answers. |
> | Brand Tracking | The longitudinal panel — awareness, consideration, preference — that watches equity over time. |
> | NPS and Its Limits | The popular loyalty metric, what it's good for, and where it misleads. |
> | The Attribution Problem | Why a metric moving rarely proves the brand work caused it. |
> | Vanity vs. Value | Telling the metrics that flatter from the metrics that matter. |
> | Worked Example: A Measurement Plan | Building a metric plan with sourced, blank-until-measured baselines. |

---

A brand is the asset from Chapter 2; this chapter is how you watch it move. The instinct most teams have is to grab whatever number is easy — followers, impressions, an NPS score — and treat its movement as proof the brand is working. That instinct is the enemy of honest measurement. The discipline here is choosing metrics that actually reflect equity, knowing each one's limits, and resisting the leap from "this number moved" to "our work caused it." It is the same judgment the AI+1 thesis trains: a signal is not a verdict.

## What to Measure, and Why

Two families, answering different questions:

- **Brand metrics** — awareness, consideration, preference, associations, sentiment, equity. They move slowly and predict the future. (Lagging on the asset, leading on the business.)
- **Performance metrics** — conversion, customer acquisition cost (CAC), return on ad spend (ROAS), retention. They move fast and report the present.

Both matter; confusing them is a classic error. A campaign can lift performance while eroding brand (deep discounts), or build brand while performance looks flat. Measure both, and know which you're reading.

## Brand Tracking

A **brand tracking study** is a repeated survey of the same questions over time: **aided** and **unaided awareness**, consideration, preference, and key associations. The value is the trend line — equity is a slow-moving asset, and tracking is how you see it accumulate or leak. Keller's brand audit and brand value chain connect these measures back to the CBBE pyramid: are you climbing toward resonance, or stuck at salience?

## NPS and Its Limits

**Net Promoter Score** (Fred Reichheld) — "how likely are you to recommend us?" on 0–10, promoters minus detractors — is the most widely used loyalty metric. It's useful as a simple, trackable proxy. But teach its well-documented limits: it's a single item, it's culturally skewed (scoring norms differ by country), it compresses information, and a good NPS is not a strategy. Use it as one lagging signal, not the verdict on brand health.

## The Attribution Problem

The hard one. When sales rise after a campaign, did the campaign *cause* it — or did seasonality, a competitor stumble, or a price change? **Attribution** (multi-touch models) and **marketing-mix modeling (MMM)** try to answer, and both are estimates with real uncertainty. **Brand-lift studies** (control vs. exposed) are the cleaner design. This is correlation-vs-causation in its native habitat, and it's precisely where AI dashboards mislead: they report the correlation fluently and leave the causal leap to you.

## Vanity vs. Value

A **vanity metric** flatters without informing: impressions, follower counts, raw pageviews. A **value metric** ties to a decision or a dollar: qualified conversion, retention, equity movement, price premium. The test (from Farris's *Marketing Metrics*): if the number changed, would you do anything differently? If not, it's vanity.

## Worked Example: A Measurement Plan

For your running-project brand, this chapter adds a measurement plan: the few metrics worth tracking, each with a source and a baseline. Crucially, baselines are blank until you actually measure — Madison drafts the structure, never the numbers.

---

## AI+1 — Self-as-Project on Madison

**Project:** Self-as-Project — *your brand, end to end*
**This chapter adds:** a brand measurement plan (metric | baseline | target | source).
**Madison recipes:** [`madison-performance-reporting`](../madison/recipes/madison-performance-reporting.md), [`madison-category-sentiment-dashboard`](../madison/recipes/madison-category-sentiment-dashboard.md)

> Madison assembles the dashboard and structure; *you* interpret results and refuse fabricated baselines. Interpretation — and the refusal of invented numbers — is the +1.

### Exercise 1 — When to Use AI
- *Draft the metric plan structure (metric | source | cadence).* **Why it works:** structure-drafting.
- *Assemble a sentiment/category dashboard from public signal.* **Why it works:** retrieval + reformatting.
- *Flag vanity metrics in a proposed set.* **Why it works:** pattern-spotting.

**Tell:** you can tie each metric to a decision it would change.

### Exercise 2 — When NOT to Use AI
- *Interpreting whether a metric move means the brand worked.* **Why it fails:** the attribution/causal problem — the chapter's core lesson.
- *Supplying a baseline you haven't measured.* **Why it fails:** fabrication; an invented baseline corrupts every later comparison.
- *Choosing which metrics matter.* **Why it fails:** a strategic judgment about what the brand is for.

**Tell:** you've crossed the line when a dashboard movement becomes your conclusion without a causal check.
**Series connection:** Tier 5 (causal) — refusing to let a correlation masquerade as a caused effect.

### Exercise 3 — Recipe Exercise
**Build:** a measurement plan + sentiment dashboard. **Run:** [`madison-performance-reporting`](../madison/recipes/madison-performance-reporting.md) + [`madison-category-sentiment-dashboard`](../madison/recipes/madison-category-sentiment-dashboard.md). **Tool:** Claude / Claude Code.

```
Using the Madison performance-reporting + category-sentiment-dashboard recipe
approach, propose a brand measurement plan for [MY BRAND]: 5–7 metrics (brand vs.
performance labeled), each with metric | source | cadence | why-it-matters.
Leave BASELINE and TARGET blank for me. Invent no numbers. Flag any vanity metrics
you were tempted to include and why you excluded them.
```
**Adapt:** personal brand → metrics like inbound opportunities, profile reach, referral mentions.

### Exercise 4 — CLI Exercise
**Build:** `your-brand/measurement-plan.md`. **Tool:** [`wrap-your-tool`](../madison/wrap-your-tool/) or Claude Code.

```
Write your-brand/measurement-plan.md: table metric | brand/performance | source |
cadence | baseline (BLANK) | target (BLANK) | decision-it-informs. Invent no
baselines or targets. Stop after writing the file.
```
**Inspect:** every metric names a source and a decision; baselines blank. **If it goes wrong:** the model fills baselines with plausible numbers — blank them.

### Exercise 5 — AI Validation Exercise
**Validate:** the measurement plan. Pass / Fail / Cannot-determine + evidence:
- **Correctness:** is each metric labeled brand vs. performance correctly?
- **Completeness:** source + cadence + decision for each?
- **Scope:** plan only — no fabricated data?
- **Brand-specific:** does each metric tie to a decision (not vanity)?
- **Failure-mode:** any invented baseline/target? Any correlation framed as proof of impact?
**AI Use Disclosure:** two sentences — what the recipes produced; one thing they could not determine (whether the work caused the movement) that needed your judgment.

---

## Key terms
brand metrics vs. performance metrics · brand tracking study · aided/unaided awareness · Net Promoter Score (and its limits) · attribution · marketing-mix modeling · brand-lift study · vanity vs. value metric.

## Bridge
You can measure the brand. Chapter 14 is how you keep it coherent over time and decide when to change it — management, governance, and rebranding.
