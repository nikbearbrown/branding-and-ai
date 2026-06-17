# Branding and AI
## Compact Tik TOC Architecture

**Book type:** Graduate course textbook / practitioner handbook (AI+1 series)
**Status:** Retrofit of a developed 14-chapter manuscript (16 files incl. front/back matter)
**Subtitle:** *AI+1, Hands on. Domain specific. No generic prompts.*

## Core Thesis

When AI collapses the cost of *building*, the scarce skill becomes knowing **what** to build
and making it **legible** to the audience it is for. Read through Spence's signaling
mechanism: the credentials that used to separate technical practitioners have cheapened, so
the durable signal moves to the four verbs — **Ideate, Build, Brand, Ship** — and to the
brand discipline that makes a *Creative Engineer* recognizable. This is a branding textbook
that teaches brand strategy as a system of decidable decisions, and uses AI as the tool that
executes once the strategic question is clear.

## Primary Reader

Technical graduate students, MBAs, founders, and creators whose credentials no longer
separate them and who must build a legible brand around real work.

## Spine (the distinctions the book is built on)

1. **Spence signaling** — why credentials cheapened and what now signals (Ch 1).
2. **The four verbs** — Ideate / Build / Brand / Ship as the unit of career value (Ch 1).
3. **Architecture as brand** — reading Madison's five agent roles as a brand surface (Ch 2, 6).
4. **Archetype as constraint** — twelve Jungian archetypes as the choice that makes every
   downstream decision decidable (Ch 3).
5. **Scope as refusal** — the "$100,000 no"; what you won't build defines the product (Ch 4).
6. **Contracts** — pipelines, interfaces, and dependencies as promises that will change (Ch 5, 7).
7. **Two brand paths** — personal (8a) and startup (8b) strands of the same strategy.
8. **Coherence, story, portfolio, presence** — visual identity, storytelling, portfolio-as-product,
   launch (Ch 9–12).

## Madison: the bundled AI tool

This repo **ships the Madison framework** (`madison/` — curated brand-relevant recipes + the
wrap-your-tool template + the plus-one prompt). *Branding and AI* teaches branding; **Madison
is the AI it runs on.** A reader downloads this repo and the exercises are runnable — no other
clone required. The companion volume *The Madison CLI Framework* documents the architecture but
is not needed to use the recipes here. Madison naming follows the public framework
(humanitarians.ai/madison).

## Chapter Architecture

Every chapter opens on a **brand decision**, not a tool. AI enters only after the strategic
question is set — as research assistant, pattern finder, draft generator, or critique partner.
Each chapter carries an in-chapter **AI+1 block**: a branding decision run through the mapped
Madison recipe (see `madison/README.md`), threaded as one **running brand project** (the
reader's own brand, forked along the personal 8a / startup 8b paths). The agent drafts; the
reader exercises the strategic judgment to accept, reject, or revise.

## Terminal Capability

The reader can fix an archetype, scope a brand/tool, stand up a signal pipeline, generate
on-voice story and copy, enforce a visual-identity system, assemble a portfolio-as-product,
and rehearse and ship a launch — each produced by running Madison with human strategic
accountability, end to end on their own brand.

## Adoption Risks

- AI tool examples date quickly — anchor to the brand decision, not the tool version.
- Brand theory must not disappear under tool demos; the decision leads, Madison follows.
- Agent-generated personas, claims, and market figures are drafts requiring an evidence check
  (the human half of AI+1).
- Keep the boundary clean: this book *applies* Madison; it does not re-teach the framework.

## Production Notes

- Exercises follow the AI+1 standard: per-chapter block keyed to the running brand project,
  pointing at a bundled `madison/recipes/*` file.
- Two intro/structure debts to clear: `00-introduction.md` is generic boilerplate with an
  off-by-one chapter list (drops Ch 8 Brand Strategy, mislabels 9–12); figures predate the
  CAJAL pantry pipeline.
- Use this Tik TOC — not the old generic one — to align downstream tooling (exercise
  generation, figure planning, bridge, assessments) to the real manuscript.
