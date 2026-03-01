# 🎯 Arab Twitter Pulse — Sentiment & Trend Analysis Dashboard

## The Problem
Arabic and French-speaking social media communities are vibrant, but fragmented. What are they talking about? How does sentiment shift around key topics and events? Why should a Tunisian company care?

**Short answer**: Because sentiment drives engagement, brand perception, and product-market fit. This dashboard translates raw social media noise into actionable insights.

## The Solution
An interactive Streamlit dashboard that analyzes Arabic and French social media sentiment, extracts trending topics, and provides real-time insights for marketing, product, and comms teams.

**[🚀 Live Dashboard](your-huggingface-spaces-url-here)** | **[📊 View Notebooks](notebooks/)**

---

## 📊 Dashboard Panels

An executive dashboard with 5 evidence-based panels:

| Panel | Business Question | Data Source |
|---|---|---|
| 📊 **Overview / KPIs** | What's the overall sentiment landscape? | Summary stats |
| 📈 **Sentiment Over Time** | When did sentiment shift and why? | Time series + event annotations |
| 🗂️ **Topic Extraction** | What are people actually talking about? | TF-IDF top terms |
| 🔀 **Sentiment by Topic** | Which topics drive positive vs negative reactions? | Cross-tab analysis |
| 🔍 **Data Explorer** | Show me specific posts by keyword/sentiment | Filterable raw data table |

---

## 📊 Key Findings

> *(To be filled after analysis)*

- **Finding 1**: e.g. "Negative sentiment spiked 40% during [period], correlating with [event]"
- **Finding 2**: e.g. "Topic X dominated conversation with 28% of all posts"
- **Finding 3**: e.g. "Technology topics skew 65% positive, while Politics shows polarization"

---

## 🛠 Tech Stack

| Component | Technology | Why |
|-----------|-----------|-----|
| Data Wrangling | pandas, numpy | Fast + familiar |
| Sentiment Analysis | CAMeL-Lab BERT (HuggingFace) | SOTA for Arabic, no retraining needed |
| Topic Extraction | scikit-learn (TF-IDF, LDA) | Interpretable + fast |
| Visualization | Plotly | Interactive, looks great in Streamlit |
| Dashboard | Streamlit | Deploy in 30 mins, free hosting |
| Deployment | Hugging Face Spaces | Free, live URL for resume |

---

## 📁 Project Structure

```
arabic-sentiment-analysis/
├── data/
│   ├── raw/              # Original dataset (not in git)
│   └── processed/        # Cleaned, ready for analysis
├── notebooks/
│   ├── 01_eda.ipynb      # Exploratory data analysis
│   ├── 02_cleaning.ipynb # Data cleaning pipeline
│   ├── 03_sentiment.ipynb # Sentiment analysis
│   ├── 04_topics.ipynb    # Topic extraction
│   └── 05_panels.ipynb    # Build all 5 dashboard panels
├── src/
│   ├── __init__.py
│   ├── config.py         # Constants, paths, model names
│   ├── text_cleaning.py  # Text normalization + preprocessing
│   ├── sentiment.py      # Load & run sentiment models
│   ├── topics.py         # TF-IDF, LDA, topic extraction
│   └── utils.py          # Helper functions
├── dashboard/
│   └── app.py            # Streamlit dashboard entry point
├── docs/
│   └── findings.md       # Detailed insights & implications
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/yourusername/arabic-sentiment-analysis.git
cd arabic-sentiment-analysis
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Download Dataset
Place your dataset in `data/raw/` — see [Dataset Section](#-dataset) below for options.

### 3. Run Analysis
```bash
# Exploratory Data Analysis
jupyter notebook notebooks/01_eda.ipynb

# Then run cleaning, sentiment, topics (see notebooks/ folder)
```

### 4. Launch Dashboard
```bash
streamlit run dashboard/app.py
```
Open `http://localhost:8501` in your browser.

---

## 📊 Dataset

**Status**: [ ] Dataset selected | [ ] Downloaded | [ ] Explored

### Option A: Pre-Collected (Recommended for speed)
- **[HARD Dataset](https://huggingface.co/datasets/QCRI/HARD)** (HuggingFace) — Highly Recommended  
  Arabic Twitter sentiment with multiple dialects  
- **[ArSentiment](https://huggingface.co/datasets/QCRI/ArSentiment)** (HuggingFace)  
  Balanced Arabic sentiment dataset, 20K+ tweets
- **[ASTD](https://huggingface.co/datasets/QCRI/ASTD)** (HuggingFace)  
  Arabic sentiment tweets dataset
- **[Tunisian Dialect (Arabizi)](https://www.kaggle.com/datasets/mksaad/tunisian-sentiment-twitter-dataset)** (Kaggle)  
  Tunisian-specific data for local relevance

### Option B: Scrape Your Own (More impressive, longer timeline)
- **snscrape** (free Twitter scraping)
- **Reddit API** (free, unmoderated comments)
- Target: #Tunisia, #Maghreb, tech/startup hashtags

**Recommendation**: Start with Option A to move fast. Use one of the HuggingFace datasets to complete all 5 panels in one week.

---

## 🔍 Methodology

### Text Cleaning
- Normalize Arabic characters (remove diacritics)
- Remove URLs, @mentions, hashtags  
- Lowercase, strip extra whitespace
- Handle missing values (drop or impute)

### Sentiment Analysis Approach
- **Model**: CAMeL-Lab BERT (pre-trained on Arabic sentiment)  
  [camel-lab/bert-base-arabic-camelbert-da-sentiment](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment)
- **No Fine-Tuning**: Use pre-trained weights directly
- **Validation**: Spot-check 20+ samples manually
- **Output**: [positive, negative, neutral] + confidence scores

### Topic Extraction
- **TF-IDF**: Extract top 1000 features, identify significant terms
- **LDA** (optional): Latent Dirichlet Allocation for thematic clustering  
- **Filtering**: Remove Arabic + French stopwords, keep domain-relevant tokens
- **Visualization**: Bar chart of top 10-15 topics

### Dashboard & Filtering
- **Plotly** for interactive charts (zoom, hover, export)
- **Streamlit sidebar** filters: date range, sentiment, keyword search
- **Raw data table** with sorting + filtering capability

---

## 📈 Expected Outcomes

After one week, you should have:
- ✅ Clean, processed dataset in `data/processed/`
- ✅ Trained sentiment predictions on all posts  
- ✅ Extracted top topics (TF-IDF + top terms)
- ✅ All 5 dashboard panels in a notebook
- ✅ Streamlit app deployed to Hugging Face Spaces
- ✅ Polished README with key findings

---

## 🤝 How to Use This As a Portfolio Piece

1. **For interviews**: Share deployed dashboard URL + this README
2. **For learning**: Each notebook is a step; read markdown cells for narrative
3. **For replication**: Follow Quick Start with your own dataset

**Interview Question Ready**: *"I built an NLP sentiment dashboard for Arabic social media. I used a pre-trained multilingual BERT model, extracted topics with TF-IDF, and deployed via Streamlit. One key finding was [insight from Panel 2/4]. The entire pipeline is reproducible from the GitHub repo."*

---

## 📝 Next Steps

- [ ] Pick a dataset from the options above
- [ ] Download & explore (`notebooks/01_eda.ipynb`)
- [ ] Clean text & run sentiment (`notebooks/02_cleaning.ipynb`, `03_sentiment.ipynb`)
- [ ] Extract topics (`notebooks/04_topics.ipynb`)
- [ ] Build all 5 panels in a notebook (`notebooks/05_panels.ipynb`)
- [ ] Convert to Streamlit (`dashboard/app.py`)
- [ ] Deploy to Hugging Face Spaces
- [ ] Update README with findings + live URL

---

## 📄 License
MIT License — use as a template for your own projects.

**Built with ❤️ for Tunisian startups and data teams.**

> Raw data is not committed to this repo. See `data/README.md` for download instructions.

---

## About

Built by [Your Name] as part of a data science portfolio targeting the Tunisian and MENA tech market.  
Connect on [LinkedIn](your-linkedin-url)
