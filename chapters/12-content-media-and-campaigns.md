# Chapter 12 — Content, Media & Campaigns
*AI made content free to produce. That is exactly why most of it is worthless.*

> **TL;DR:** Content needs a planning layer above the copy — what to say, where, why, and how it's paid for. This chapter teaches the PESO media model and integrated marketing communications, the campaign brief, and reach/frequency basics, then has you build a campaign plan and a channel-ready content set with Madison drafting and you owning the message and every claim.
>
> | Section | Preview |
> |---|---|
> | The Flood and the Filter | Why cheap AI content raises, not lowers, the value of editorial judgment. |
> | PESO: Four Kinds of Media | The paid, earned, shared, and owned channels, and why they work as a system. |
> | One Voice: IMC | The discipline of saying one consistent thing across every channel. |
> | The Campaign Brief | The short document that turns strategy into a coordinated campaign. |
> | Reach, Frequency, Mix | The media-planning basics that decide whether a message lands. |
> | Worked Example: Plan a Campaign | Building a campaign plan and content set, with claims checked. |

---

The cost of producing a competent paragraph, image, or video has collapsed toward zero. The naive conclusion is that content is now easy. The real consequence is the opposite: when everyone can flood every channel with fluent, on-trend, generic content, the scarce thing becomes a *reason to publish this* and the *judgment to make it good and true*. Content strategy is the filter on the flood. This chapter adds the planning layer the book was missing — the campaign and media discipline above the copy recipes.

## The Flood and the Filter

AI is genuinely good at drafting variants at volume. It is genuinely bad at deciding what's worth saying, whether it's true, and whether it sounds like you. So the workflow inverts: the brander spends less time producing and more time selecting, verifying, and shaping. The five-part AI+1 block in this chapter is built around exactly that split.

## PESO: Four Kinds of Media

Gini Dietrich's **PESO model** is the modern channel taxonomy:

- **Paid** — advertising you buy (search, social, display).
- **Earned** — coverage others give you (press, reviews, word of mouth).
- **Shared** — social and community channels.
- **Owned** — your site, blog, email list, the surfaces you control.

The power is in integration, not silos: owned content earns press, paid amplifies the best owned pieces, shared spreads earned coverage. A campaign uses all four deliberately.

## One Voice: IMC

**Integrated Marketing Communications** (Don Schultz) is the discipline of making every channel say one consistent thing. Fragmented communication — a different message per channel — confuses the audience and wastes the equity each touch could have built. IMC is the campaign-level version of the consistency rule that runs through the whole book: one archetype, one voice, one message, expressed appropriately per channel.

## The Campaign Brief

A campaign is driven by a short brief: **objective** (what change you want) → **audience** (from Chapter 4) → **message** (from positioning, Chapter 6) → **channel mix** (PESO) → **budget** → **measurement** (Chapter 13). The brief forces the campaign to be *about* something measurable, not just "more content." If you can't state the objective and how you'll know it worked, you don't have a campaign — you have output.

## Reach, Frequency, Mix

Two media basics decide whether a message lands: **reach** (how many distinct people see it) and **frequency** (how many times each does). Awareness goals favor reach; persuasion and memory favor frequency. The **media mix** allocates budget across channels to hit the goal. You don't need a media-buying career — you need to know that spreading one impression across everyone (high reach, low frequency) rarely changes behavior.

## Worked Example: Plan a Campaign

For your running-project brand, this chapter adds a campaign plan plus a small channel-ready content set. Madison constructs the plan and drafts the content; you own the message, sign off the voice, and verify every factual claim.

---

## AI+1 — Self-as-Project on Madison

**Project:** Self-as-Project — *your brand, end to end*
**This chapter adds:** a campaign plan + a channel-ready content set.
**Madison recipes:** [`madison-campaign-construction`](../madison/recipes/madison-campaign-construction.md), [`madison-copy-content-generation`](../madison/recipes/madison-copy-content-generation.md), [`content-agent`](../madison/recipes/content-agent.md)

> Madison plans and drafts at volume; *you* choose the message, approve the voice, and clear every claim. Selection and verification are the +1.

### Exercise 1 — When to Use AI
- *Draft the PESO channel plan from the brief.* **Why it works:** structure-drafting.
- *Generate copy variants per channel.* **Why it works:** option generation at volume.
- *Spot off-archetype or unsupported copy.* **Why it works:** pattern-spotting.

**Tell:** you can tell, line by line, whether it's true and on-voice.

### Exercise 2 — When NOT to Use AI
- *Choosing the campaign objective and message.* **Why it fails:** strategy, not output.
- *Approving the brand voice.* **Why it fails:** authenticity; readers detect generic copy.
- *Letting a claim or statistic into copy.* **Why it fails:** fabrication risk destroys trust (and may breach ad rules).

**Tell:** you've crossed the line when you ship copy you can't stand behind or source.
**Series connection:** Tier 4 (metacognitive) — supervising fluent output for truth and fit.

### Exercise 3 — Recipe Exercise
**Build:** a campaign plan + content set. **Run:** [`madison-campaign-construction`](../madison/recipes/madison-campaign-construction.md) → [`madison-copy-content-generation`](../madison/recipes/madison-copy-content-generation.md)/[`content-agent`](../madison/recipes/content-agent.md). **Tool:** Claude Project.

```
Using the Madison campaign-construction + copy-content-generation recipe approach,
from my positioning + audience below: (1) a campaign brief (objective | audience |
message | PESO mix | one KPI); (2) one piece per channel (paid/earned/shared/owned)
in MY voice. Use only facts I supply; tag any invented specific [FABRICATED —
remove]. Match my voice samples, not generic brand-speak.

Positioning + audience + voice samples:
[PASTE]
```
**Adapt:** swap the channel mix to fit where your audience actually is.

### Exercise 4 — CLI Exercise
**Build:** `your-brand/campaign.md` + `your-brand/content-set.md`. **Tool:** [`wrap-your-tool`](../madison/wrap-your-tool/) or Claude Code.

```
Write your-brand/campaign.md (the brief) and your-brand/content-set.md (channel |
copy | claim-check). Tag unverifiable claims [FABRICATED]. Invent no metrics,
awards, or quotes. Stop after writing the files.
```
**Inspect:** the brief has one measurable KPI; zero fabricated specifics. **If it goes wrong:** the model adds a plausible false stat — strip every unverifiable claim.

### Exercise 5 — AI Validation Exercise
**Validate:** the campaign + content. Pass / Fail / Cannot-determine + evidence:
- **Correctness:** every factual specific true and sourced?
- **Completeness:** brief + one piece per PESO channel?
- **Scope:** campaign + content — not a full media buy?
- **Brand-specific:** one consistent message and voice across channels (IMC)?
- **Failure-mode:** list every [FABRICATED] tag; confirm each removed or sourced; check ad-disclosure where paid/influencer.
**AI Use Disclosure:** two sentences — what the recipes produced; one thing they could not determine (truth/voice fit) that needed your judgment.

---

## Key terms
PESO (paid / earned / shared / owned) · integrated marketing communications (IMC) · campaign brief · reach vs. frequency · media mix · editorial calendar · content provenance.

## Bridge
You're publishing across channels. Chapter 13 asks the question that keeps content honest: is any of it actually working? — measurement.
