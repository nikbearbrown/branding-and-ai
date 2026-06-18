# Chapter 16 — Crisis & Reputation Management
*Reputation is built in years and lost in hours. The playbook is written before the fire, not during it.*

> **TL;DR:** A crisis is the highest-stakes brand moment, and social media has compressed the response window to hours. This chapter teaches how to match a response to a crisis type (SCCT), the gold-standard Tylenol case, and how to build a monitoring-to-response playbook — then has you stand up reputation monitoring and a crisis playbook for your brand with AI watching and you deciding.
>
> | Section | Preview |
> |---|---|
> | Years to Build, Hours to Lose | Why crisis response is a brand discipline, not just a comms task. |
> | Matching Response to Crisis | A model for choosing deny / diminish / rebuild based on responsibility. |
> | The Tylenol Standard | The 1982 case that still defines a well-handled crisis. |
> | The Playbook | What to decide before a crisis: thresholds, holding statements, escalation. |
> | Speed vs. Wrong-Speed | When to respond fast, and when fast makes it worse. |
> | Worked Example: Monitor and Plan | Standing up reputation monitoring and a response playbook with AI. |

---

A brand can spend a decade building trust and lose a meaningful share of it in an afternoon, because a video spread faster than any approval chain could move. Crisis is where reputation — the external face of brand equity — is tested under maximum pressure and minimum time. The book had a reputation *monitor* recipe but no theory of *responding*. This chapter adds it, because detection without a response plan just means you watch the fire start.

## Years to Build, Hours to Lose

A crisis is rarely only a communications problem; it's usually an operations or values problem that communications then has to address. The brand consequence is real and asymmetric: the upside of a perfect response is survival; the downside of a bad one is lasting damage. So the discipline is preparation — deciding how you'll respond *before* you need to, when judgment is calm.

## Matching Response to Crisis

W. Timothy Coombs's **Situational Crisis Communication Theory (SCCT)** gives the core logic: match the response strategy to how much **responsibility** the public assigns the organization.

- **Victim crises** (the org is also a victim — natural disaster, sabotage) → low responsibility → *deny / bolster* strategies fit.
- **Accidental crises** (unintentional — technical failure) → moderate → *diminish* (explain, contextualize).
- **Preventable crises** (misconduct, known risk ignored) → high → *rebuild* (full apology, corrective action) is the only thing that works.

Benoit's **Image Repair Theory** adds the response palette: denial, evasion of responsibility, reducing offensiveness, corrective action, and **mortification** (accepting blame). The mistake is using a low-responsibility strategy (deny) on a high-responsibility crisis — it reads as evasion and deepens the damage.

## The Tylenol Standard

Johnson & Johnson's 1982 Tylenol response remains the benchmark: when poisoned capsules killed several people, J&J pulled the product nationwide at enormous cost, communicated openly, prioritized customer safety over short-term financials, and rebuilt with tamper-evident packaging. It maps to SCCT's *rebuild* with full corrective action — and it worked because the behavior matched the words. Contrast with slow, defensive responses that protect the balance sheet first and lose the brand anyway.

## The Playbook

You cannot improvise a good crisis response. A **playbook** decides in advance: monitoring and alert thresholds (what counts as a crisis), a severity triage, **holding statements** (pre-drafted "we're aware and investigating" messages that buy time without committing), an escalation path (who decides, who speaks), and channel plans. Pre-deciding means the live moment is execution, not panic.

## Speed vs. Wrong-Speed

"Always respond fast" is wrong advice. Speed matters — silence while a story spreads cedes the narrative — but **wrong-fast** (a defensive or tone-deaf statement) accelerates the damage. The holding statement resolves the tension: it's fast *and* non-committal, buying time to get the real response right. The playbook sets the thresholds so you know which mode you're in.

## Worked Example: Monitor and Plan

For your running-project brand, this chapter adds reputation monitoring plus a crisis playbook. Madison watches and triages signals; you write the response strategy and the holding statements, and you make the go/quiet call — never the agent.

---

## AI+1 — Self-as-Project on Madison

**Project:** Self-as-Project — *your brand, end to end*
**This chapter adds:** reputation monitoring + a crisis response playbook.
**Madison recipe:** [`madison-brand-news-reputation-monitor`](../madison/recipes/madison-brand-news-reputation-monitor.md)

> Madison detects and triages; *you* decide whether and how to respond, and write what gets said. The response decision is the +1 — never auto-sent.

### Exercise 1 — When to Use AI
- *Monitor sources and surface emerging reputation signals.* **Why it works:** retrieval + pattern-spotting at scale/speed.
- *Triage signal severity into a draft ranking.* **Why it works:** classification you confirm.
- *Draft holding-statement templates.* **Why it works:** structure-drafting you edit and approve.

**Tell:** you can verify a flagged signal is real before acting.

### Exercise 2 — When NOT to Use AI
- *The go/quiet decision and the response strategy.* **Why it fails:** high-stakes judgment with reputational and legal weight.
- *Sending any statement automatically.* **Why it fails:** crisis comms must be human-approved, always.
- *Assigning responsibility/severity from a spike alone.* **Why it fails:** a spike is a prompt to investigate, not a verdict.

**Tell:** you've crossed the line when a monitor alert triggers a response without human judgment.
**Series connection:** Tier 7 (wisdom) — accountable judgment under pressure the machine can't own.

### Exercise 3 — Recipe Exercise
**Build:** monitoring + a playbook. **Run:** [`madison-brand-news-reputation-monitor`](../madison/recipes/madison-brand-news-reputation-monitor.md). **Tool:** Claude / Claude Code.

```
Using the Madison brand-news-reputation-monitor recipe approach for [MY BRAND]:
(1) define monitoring sources + alert thresholds; (2) a severity triage (signal |
severity | crisis type per SCCT | first action); (3) holding-statement templates
for victim/accidental/preventable crises. Recommend response strategy by crisis
type; do not write final public statements or auto-send. Sample mode only.
```
**Adapt:** map your category's likely crisis types (data breach, claim failure, founder misstep).

### Exercise 4 — CLI Exercise
**Build:** `your-brand/crisis-playbook.md`. **Tool:** [`wrap-your-tool`](../madison/wrap-your-tool/) or Claude Code.

```
Write your-brand/crisis-playbook.md: alert thresholds, severity triage table,
SCCT response-by-type, holding-statement templates, and an escalation path
(who decides / who speaks). Mark every statement DRAFT — human approval required.
No live monitoring calls without approval. Stop after writing the file.
```
**Inspect:** response strategy matches crisis type; all statements marked draft + human-gated. **If it goes wrong:** the model writes "send" logic — replace with human-approval gates.

### Exercise 5 — AI Validation Exercise
**Validate:** the playbook. Pass / Fail / Cannot-determine + evidence:
- **Correctness:** does each crisis type map to the right SCCT strategy (not deny-on-preventable)?
- **Completeness:** thresholds + triage + holding statements + escalation?
- **Scope:** plan only — no auto-send, no live calls?
- **Brand-specific:** are the likely crisis types for this brand covered?
- **Failure-mode:** any path where a monitor alert triggers a public response without human approval? Hard fail.
**AI Use Disclosure:** two sentences — what the monitor produced; one thing it could not determine (whether/how to respond) that needed your judgment.

---

## Key terms
reputation management · Situational Crisis Communication Theory (SCCT) · crisis types (victim / accidental / preventable) · Image Repair Theory · mortification · holding statement · severity triage · escalation path.

## Bridge
You can defend the brand under fire at home. Chapter 17 takes it across borders — global and cross-cultural branding, where the same message can mean opposite things.
