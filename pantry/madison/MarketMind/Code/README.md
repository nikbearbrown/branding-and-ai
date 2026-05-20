# MarketMind 
**AI-Powered Market Research & Strategy Assistant**

 **Live App:** https://marketmind-17.onrender.com/

MarketMind is a Streamlit + CrewAI market research app that generates **pricing intel, source-aware sentiment, feature benchmarking, product demand trend**, and a **final strategy report** — all written as exportable artifacts in `./outputs/` and visualized in a clean dashboard.

Built for **founders, product managers, and strategy teams** who want fast, structured market intelligence with repeatable outputs.

---

## What MarketMind Does

MarketMind runs a multi-stage pipeline to generate:

- **Product + competitor pricing** → `competitor_prices.json`
- **Source-aware sentiment** (single truth used by chart + report) 
 → `sentiment_verified.json` + `review_sentiment.md`
- ⚙ **Feature scores (0–10)** for Product vs Competitors → `feature_scores.json` (radar chart)
- **Product demand / growth trend (product-level, not generic industry CAGR)** 
 → `market_growth.json` (line chart)
- **Executive-ready synthesis report** → `final_market_strategy_report.md`

All outputs are saved to `./outputs/` and visualized in the Streamlit UI.

---

## What’s New (Latest Behavior)

### 1) User-driven comparisons (no hardcoding)
Users can enter their own:
- **Competitors** (comma or newline separated)
- **Features to compare** (comma or newline separated)

These inputs are passed into `run_analysis()` and the AI generates artifacts specifically for the user’s selection.

### 2) Feature comparison table output is restored (clean “before format”)
MarketMind writes:
- `outputs/feature_comparison.md`

This report uses:
- **Real competitor names as columns** (no “Competitor A/B”)
- **ONLY user-entered features**
- **Price row patched from pricing JSON** (source of truth)

### 3) Single source of truth for sentiment (fixes mismatches)
Sentiment now writes:
- `outputs/sentiment_verified.json` **Used by the pie chart + report**
- `outputs/review_sentiment.md` (human-readable summary)

This prevents the donut chart and markdown report from showing different sentiment.

### 4) Themes hidden by default (cleaner, less “token noise”)
`review_sentiment.md` **does not show themes by default** to keep it customer-friendly.
(Themes can be added back later as an optional toggle if needed.)

### 5) Product trend is product-specific
The growth line chart is based on **product demand trend** (product-level), not generic industry growth.

---

## Key Features

- **Multi-Agent Orchestration (CrewAI)**
 - Strategy Consultant
 - Competitive Intelligence Analyst
 - Customer Persona Analyst
 - Sentiment & Review Analyst
 - Strategy Synthesizer

- **Interactive Dashboard**
 - Sentiment donut chart (from `sentiment_verified.json`)
 - Pricing bar chart (from `competitor_prices.json`)
 - Feature radar (from `feature_scores.json`)
 - Product demand trend (from `market_growth.json`)
 - Feature comparison markdown table (from `feature_comparison.md`)
 - Full report viewer for all `.md` outputs

- **Exportable Research**
 - Generates `.md` reports that can be pasted into docs, decks, and product briefs

---

## Architecture Overview

Streamlit UI (app.py) 
↓ 
`run_analysis()` (main.py) 
↓ 
CrewAI Orchestration 
- Agents (agents.py) 
- Tasks (tasks.py) → strict JSON + markdown outputs 
↓ 
Artifacts written to `./outputs/` 
↓ 
Streamlit dashboard visualizes outputs

---

## Project Structure

MarketMind/
│
├── app.py # Streamlit dashboard (UI)
├── main.py # Orchestration + artifact writing
├── agents.py # CrewAI agent definitions
├── tasks.py # Task definitions (STRICT JSON outputs)
│
├── tools/
│ └── scrape_pipeline.py # Search + scrape tooling (if enabled)
│
├── outputs/ # Generated artifacts (JSON + Markdown)
│ ├── competitor_prices.json
│ ├── feature_scores.json
│ ├── market_growth.json
│ ├── sentiment_verified.json
│ ├── sentiment_metrics.json
│ ├── review_sentiment.md
│ ├── feature_comparison.md
│ ├── research_plan.md
│ ├── customer_analysis.md
│ └── final_market_strategy_report.md
│
├── requirements.txt
└── README.md

---

## Outputs (What gets generated)

### JSON Artifacts (for charts)
- `competitor_prices.json` 
- `feature_scores.json` 
- `market_growth.json` *(product demand trend)*
- `sentiment_verified.json` *(pie chart + report source of truth)*
- `sentiment_metrics.json` *(derived convenience metrics)*

### Markdown Reports (for reading/export)
- `research_plan.md`
- `customer_analysis.md`
- `feature_comparison.md`
- `review_sentiment.md`
- `final_market_strategy_report.md`

---

## ⚙ Environment Variables

Set these in **Render → Environment Variables** (or locally with `.env`):

```env
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
LOG_LEVEL=INFO
