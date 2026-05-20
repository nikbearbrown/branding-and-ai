# Pantry — INFO 7375 Canvas Course Reference

Two Canvas Common Cartridge exports of the legacy INFO 7375 (Branding and AI) course, available as raw reference for chapter authors. **This is not the new course.** The new course's outline lives in `outline.md` and its lectures live in `lectures/`. Pantry content is mined when chapter authors want to see how a topic was previously taught, what assignments were given, what readings were assigned, and how the framing evolved between iterations.

## Two snapshots, same course

Both exports contain the same 4-module structure (the course was duplicated when re-offered). Spring 2026 has substantially more files (~225 XML resources, ~17 images, ~3 PDFs) than Summer 2026 (~88 XML resources, ~8 images, ~3 PDFs). Spring is the deeper pantry; Summer is useful for comparing what the instructor cut or refined.

## How chapter skill should use this

During the research protocol (book.md §11), after gathering primary sources, also grep the pantry:

```bash
grep -rli '<concept>' books/branding-and-ai/pantry/ | head -20
```

Pages and assignments are HTML. Quizzes are QTI XML. Module structure is in each course's `course_settings/module_meta.xml`. The hash-named folders contain the actual files referenced from `imsmanifest.xml`.

Pantry content is **reference, not source of truth**. Chapter drafts cite primary sources (papers, model cards, blog posts, filings). Pantry pages can suggest framings, surface examples the instructor used, and provide continuity for students who took the prior version — but the chapter's claims and citations come from the open literature, not from a Canvas page.

---

## canvas-spring-2026

- **Modules:** 4
- **Resources (manifest):** 249
- **Files (uploaded materials):** 0
- **Syllabus:** `canvas-spring-2026/course_settings/syllabus.html`

### Module structure

**M1: Module 1: Introduction to Branding and AI's Role**

- WikiPage: *Module 1: Course Introduction & Foundation Setup* — `canvas-spring-2026/wiki_content/module-1-course-introduction-and-foundation-setup.html`
- Assignment: *Assignment 1: Course Introduction & Foundation Setup* — `canvas-spring-2026/g28d6054736ae84da55e74844bdfcebbe/assignment-1-course-introduction-and-foundation-setup.html`

**M2: Module 2: Madison Framework**

- WikiPage: *Module 2: Madison Framework Integration & n8n Automation Development* — `canvas-spring-2026/wiki_content/module-2-madison-framework-integration-and-n8n-automation-development.html`
- Assignment: *Assignment 2: "Plan Your Madison Project Like a Pro"* — `canvas-spring-2026/g6e2ba7a896b50f749475b23aee91def3/assignment-2-plan-your-madison-project-like-a-pro.html`
- Assignment: *Assignment 3: Build Your Data Pipeline* — `canvas-spring-2026/g5466bc7e2c89ab383ec030c2a9ddbe96/assignment-3-build-your-data-pipeline.html`
- Assignment: *Assignment 4: "Scale Your Thing & Add Intelligence"* — `canvas-spring-2026/g5a70c0491e5816a97a9ab2f7162fc424/assignment-4-scale-your-thing-and-add-intelligence.html`

**M3: Module 3: Creating Your Personal Brand**

- WikiPage: *Module 3: Brand Voice, Storytelling & Visual Identity* — `canvas-spring-2026/wiki_content/module-3-brand-voice-storytelling-and-visual-identity.html`

**M4: Module 4: Building Your Portfolio Website and Social Media Presence**

- WikiPage: *Module 4: AI-Enhanced Visual Branding & Digital Presence* — `canvas-spring-2026/wiki_content/module-4-ai-enhanced-visual-branding-and-digital-presence.html`
- Assignment: *Assignment 8: Brand-Aligned Digital Presence* — `canvas-spring-2026/ga19b9fd25ea3b327846d7607bcb18b45/assignment-8-brand-aligned-digital-presence.html`
- WikiPage: *Deployment on Vercel* — `canvas-spring-2026/wiki_content/deployment-on-vercel.html`
- Assignment: *Assignment 9: Brand Storytelling & Content Strategy* — `canvas-spring-2026/g042786be3f582f514bcc8505554c7194/assignment-9-brand-storytelling-and-content-strategy.html`
- Assignment: *Assignment 10: Show Your Work — Substack as a Brand Platform* — `canvas-spring-2026/gdb414a7dfa5a5d9b300197d1e9678a2e/assignment-10-show-your-work-substack-as-a-brand-platform.html`

---

## canvas-summer-2026

- **Modules:** 4
- **Resources (manifest):** 103
- **Files (uploaded materials):** 0
- **Syllabus:** `canvas-summer-2026/course_settings/syllabus.html`

### Module structure

**M1: Module 1: Introduction to Branding and AI's Role**

- WikiPage: *Module 1: Course Introduction & Foundation Setup* — `canvas-summer-2026/wiki_content/module-1-course-introduction-and-foundation-setup.html`
- Assignment: *Assignment 1: Course Introduction & Foundation Setup* — `canvas-summer-2026/g796ed2510c4ddda09b82b91983b2daa5/assignment-1-course-introduction-and-foundation-setup.html`

**M2: Module 2: Madison Framework**

- WikiPage: *Module 2: Madison Framework Integration & n8n Automation Development* — `canvas-summer-2026/wiki_content/module-2-madison-framework-integration-and-n8n-automation-development.html`
- Assignment: *Assignment 2: "Plan Your Madison Project Like a Pro"* — `canvas-summer-2026/gee07fccb423d3697dab48bef91c43f22/assignment-2-plan-your-madison-project-like-a-pro.html`
- Assignment: *Assignment 3: Build Your Data Pipeline* — `canvas-summer-2026/g2d93e65204a5642d8a3f769889922d1e/assignment-3-build-your-data-pipeline.html`
- Assignment: *Assignment 4: "Scale Your Thing & Add Intelligence"* — `canvas-summer-2026/g91b89ef629f9a1ce81015cb00b85d57e/assignment-4-scale-your-thing-and-add-intelligence.html`

**M3: Module 3: Creating Your Personal Brand**

- WikiPage: *Module 3: Brand Voice, Storytelling & Visual Identity* — `canvas-summer-2026/wiki_content/module-3-brand-voice-storytelling-and-visual-identity.html`

**M4: Module 4: Building Your Portfolio Website and Social Media Presence**

- WikiPage: *Module 4: AI-Enhanced Visual Branding & Digital Presence* — `canvas-summer-2026/wiki_content/module-4-ai-enhanced-visual-branding-and-digital-presence.html`
- Assignment: *Assignment 8: Brand-Aligned Digital Presence* — `canvas-summer-2026/g9ff2aceec904e792dd68bba2dbff86c0/assignment-8-brand-aligned-digital-presence.html`
- WikiPage: *Deployment on Vercel* — `canvas-summer-2026/wiki_content/deployment-on-vercel.html`
- Assignment: *Assignment 9: Brand Storytelling & Content Strategy* — `canvas-summer-2026/ge8ad9e1a2bb68d1521e920b32c87d869/assignment-9-brand-storytelling-and-content-strategy.html`
- Assignment: *Assignment 10: Show Your Work — Substack as a Brand Platform* — `canvas-summer-2026/g9b65fd5ea2635e2134fa325d450a384e/assignment-10-show-your-work-substack-as-a-brand-platform.html`


---

## Binary assets discovered on disk

Not all uploaded materials appear in module structure or files_meta.xml. These were found by walking the unzipped folders. Useful for chapter authors who want images, slide PDFs, or diagrams from the prior course.

### canvas-spring-2026

**PDFs:**

- `canvas-spring-2026/web_resources/Uploaded Media/Beautiful.ai - INFO7375 Branding and AI - Spring-2.pdf`
- `canvas-spring-2026/web_resources/Uploaded Media/Beautiful.ai - The Many Hats of Creative Engineering Why Wearing Multiple Hats is the Future-3.pdf`
- `canvas-spring-2026/web_resources/unfiled/Nina — Complete Assignment 7 Submission.pdf`

**Images (PNG):**

- `canvas-spring-2026/web_resources/Uploaded Media/image-1.png`
- `canvas-spring-2026/web_resources/Uploaded Media/image-2.png`
- `canvas-spring-2026/web_resources/Uploaded Media/image-3.png`
- `canvas-spring-2026/web_resources/Uploaded Media/image-4.png`
- `canvas-spring-2026/web_resources/Uploaded Media/image-5.png`
- `canvas-spring-2026/web_resources/Uploaded Media/image-6.png`
- `canvas-spring-2026/web_resources/Uploaded Media/image-7.png`
- `canvas-spring-2026/web_resources/Uploaded Media/image-7a6f4d24-b431-4610-ba9e-64e500453d5c.png`
- `canvas-spring-2026/web_resources/Uploaded Media/image-98547234-e263-4333-a138-c824cd69042c.png`
- `canvas-spring-2026/web_resources/Uploaded Media/image-af433072-b2f4-4dfe-b10d-718c70457134.png`
- `canvas-spring-2026/web_resources/Uploaded Media/image-b6088b89-74c2-43f5-a749-dc982ae35bb5.png`
- `canvas-spring-2026/web_resources/Uploaded Media/image-faad1f90-557a-43ac-8cae-53fbfdca5f3f.png`
- `canvas-spring-2026/web_resources/Uploaded Media/image.png`
- `canvas-spring-2026/web_resources/assessment_questions/image-1-1.png`
- `canvas-spring-2026/web_resources/assessment_questions/image-1.png`
- `canvas-spring-2026/web_resources/assessment_questions/image-2.png`
- `canvas-spring-2026/web_resources/assessment_questions/image-3.png`

**Markdown notes:**

- `canvas-spring-2026/web_resources/unfiled/Gru.md`
- `canvas-spring-2026/web_resources/unfiled/Nina_Tool.md`
- `canvas-spring-2026/web_resources/unfiled/ada-sdd-consultant.md`

**Quizzes (QTI XML):**

12 QTI files. Discover with: `find canvas-spring-2026 -name '*.qti'`

### canvas-summer-2026

**PDFs:**

- `canvas-summer-2026/web_resources/Uploaded Media/Beautiful.ai - INFO7375 Branding and AI - Spring-2.pdf`
- `canvas-summer-2026/web_resources/Uploaded Media/Beautiful.ai - The Many Hats of Creative Engineering Why Wearing Multiple Hats is the Future-3.pdf`
- `canvas-summer-2026/web_resources/unfiled/Nina — Complete Assignment 7 Submission.pdf`

**Images (PNG):**

- `canvas-summer-2026/web_resources/Uploaded Media/image-1.png`
- `canvas-summer-2026/web_resources/Uploaded Media/image-2.png`
- `canvas-summer-2026/web_resources/Uploaded Media/image-3.png`
- `canvas-summer-2026/web_resources/Uploaded Media/image.png`
- `canvas-summer-2026/web_resources/assessment_questions/image-1-1.png`
- `canvas-summer-2026/web_resources/assessment_questions/image-1.png`
- `canvas-summer-2026/web_resources/assessment_questions/image-2.png`
- `canvas-summer-2026/web_resources/assessment_questions/image-3.png`

**Markdown notes:**

- `canvas-summer-2026/web_resources/unfiled/Gru.md`
- `canvas-summer-2026/web_resources/unfiled/Nina_Tool.md`
- `canvas-summer-2026/web_resources/unfiled/ada-sdd-consultant.md`

**Quizzes (QTI XML):**

11 QTI files. Discover with: `find canvas-summer-2026 -name '*.qti'`


---

## madison/ — the framework repo

The full Madison framework source from GitHub. **This is the reference architecture Chapter 2 teaches and Chapters 4–7 build against.** Authors of those chapters read code, agent definitions, and n8n workflows here when explaining how a Madison tool is structured.

Madison (informally "Mads and Madison") is an open-source agent-based AI marketing framework from Humanitarians AI. Five collaborative agent layers, plus an orchestration layer:

1. **Intelligence Agents** — gather and analyze market data (sentiment, reputation, trends)
2. **Content Agents** — create, optimize, distribute marketing materials
3. **Research Agents** — survey analysis, synthetic personas, customer insight
4. **Experience Agents** — concierge systems, journey transformation
5. **Performance Agents** — multi-armed bandits, predictive analytics

Source: `madison/README.md` is the primary entry point. Full text on Humanitarians AI conventions, framework integration with Bellman/Popper, and core technologies.

### Top-level directories — what's where

| Directory | Agent layer / role | Notable contents |
| --- | --- | --- |
| `Intelligence-Agent/` | Layer 1 — Intelligence | Production-ready: `sentiment_analysis.py`, `n8n_workflow.json`, `Final Report.pdf`, `README.md` |
| `MarketMind/` | Layer 3 — Research (market) | `Code/` directory with full Python app (agents.py, app.py, models.py, tasks.py, tools/), plus `n8n-marketminds-workflow.json` |
| `SurveyAnalysis/` | Layer 3 — Research (survey) | Datasets, reports, benchmark scripts. Includes Amazon review CSVs, AutoML benchmark, music-instrument analysis reports |
| `SyntheticPersonas/` | Layer 3 — Research (personas) | `Synthetic_Personas.md` — full design doc on persona generation, Big-5 traits, GPT integration |
| `Social-Media-Scraping/` | Data collection (feeds Layer 1) | Two Instagram scrapers (`insta_scraper_02`, `insta_scrapper_01`) plus `social-media-scraping-v2/` |
| `brandguide.ai/` | Reference application | Full-stack app — Python `backend/` (Dockerfile, src/, tests/, uv.lock), React `frontend/` (TSX, components, hooks). Includes `color_gap_analysis.md`, `backend_report.md`, sample brand-guidelines PDF |
| `n8n-workflows/` | Build Chapter 5/6 reference | n8n workflow patterns — start here for the "how does a Madison workflow look" answer |
| `Archives/` | Earlier Madison projects | BrandEcho, Cicerone, AI_Whisperer, Census-Based Big-5 Personality Estimation, Core_Components, AI-Powered Marketing Content Generation, n8n_Workflows. Useful when Chapter 8 (brand strategy) or Chapter 10 (storytelling) wants a worked example. `Core_Components/` is the closest thing to a framework cross-cut. |

### Top-level files

- `README.md` — primary overview, the document Chapter 2 reads first
- `Content_Agent_full_workflow.json` — the Content agent layer's complete n8n workflow (26KB JSON). Worth showing to students who want to see what "production agent workflow" looks like.
- `LICENSE` — MIT

### How chapter authors use this

**Chapter 2 (Madison home):** read `README.md` first, then walk `Intelligence-Agent/` as the most production-ready exemplar of one agent layer. Use `Core_Components/` (in Archives) to extract cross-cutting patterns. The five-agent architecture in the README is the structure Chapter 2 teaches.

**Chapter 4 (PRD):** show the Intelligence-Agent README's "Key Capabilities" section as a worked example of what a PRD's outcomes section can look like.

**Chapter 5 (Pipelines):** start at `n8n-workflows/` and `Intelligence-Agent/n8n_workflow.json`. The Madison n8n workflow files are the running worked example for the chapter.

**Chapter 6 (AI Intelligence / Multi-Agent):** `Content_Agent_full_workflow.json` is the deepest single-file example of multi-agent orchestration. `MarketMind/Code/agents.py` shows agent definitions in code. Pair the JSON workflow view with the Python code view.

**Chapter 7 (UI / Deploy):** `brandguide.ai/` is the reference deployed app — backend + frontend + Docker. Show students what "deployed Madison tool" looks like in practice.

**Chapters 8–11 (Brand work):** `brandguide.ai/` is also the natural example for brand-strategy work. `color_gap_analysis.md` and the Slack brand-guidelines PDF give concrete artifacts to point at.

