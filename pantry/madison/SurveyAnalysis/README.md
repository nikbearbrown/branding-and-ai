# Survey Analysis Platform

An AI-powered survey analysis tool that provides automated insights from survey data.

## Features
- Automated data ingestion from CSV files
- Sentiment analysis using AI
- Theme extraction and keyword analysis
- Trend identification over time
- Interactive dashboards
- PDF report generation
- Workflow automation

## Tech Stack

### Backend & Data Processing
- Python 3.11
- Pandas (data manipulation)
- NumPy (numerical computing)

### AI/ML
- OpenAI API (sentiment analysis, theme extraction)
- scikit-learn (machine learning algorithms) *[Week 2]*

### Visualization
- Plotly (interactive charts)
- Matplotlib (static plots, word clouds)

### Frontend
- Streamlit (web dashboard)

### Storage
- CSV/JSON (input data)
- SQLite (processed data storage) *[Week 2]*

### Automation
- n8n integration (workflow.json) *[Week 3]*

### Development Tools
- VS Code (IDE)
- python-dotenv (environment management)

*Items marked with [Week X] will be added in later phases*

## Project Structure
```
survey-analysis/
├── data/ # Survey data files
│ ├── raw/ # Original survey data
│ └── processed/ # Cleaned data
├── src/ # Source code
├── outputs/ # Generated reports and charts
│ ├── reports/ # PDF reports
│ └── charts/ # Visualizations
├── requirements.txt # Python dependencies
└── README.md # This file
```

## Installation

### Phase 1 - Core Dependencies (Week 1)
```bash
pip3 install -r requirements.txt
```

### Phase 2 - ML & Storage (Week 2)
```bash
pip3 install scikit-learn
# SQLite comes built-in with Python
```

### Phase 3 - Automation (Week 3)
*Instructions to be added*

## Development Status
 **Week 1 - Foundation & Core Features**
- [x] Project setup
- [x] Development environment configured
- [ ] Data ingestion module
- [ ] Basic sentiment analysis
- [ ] Simple dashboard

## Learning Goals
This project teaches:
- Data engineering (ETL pipelines)
- AI/ML integration (NLP, sentiment analysis)
- Web development (Streamlit dashboards)
- Data visualization (Plotly, Matplotlib)
- Software engineering best practices

## Author
Built as a learning project for AI/ML, data engineering, and web development skills.

What these are:
pandas - Works with data (like Excel but in code)
numpy - Math and calculations
streamlit - Creates web dashboards
plotly - Makes interactive charts
matplotlib - Makes static charts
openai - Connects to AI for analysis
python-dotenv - Manages secret keys safely