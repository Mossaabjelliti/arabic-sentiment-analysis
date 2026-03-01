# Arab Twitter Pulse

Sentiment and topic analysis dashboard for Arabic social media content, built with a Tunisian market focus.

The idea: take a raw corpus of Arabic tweets, run sentiment classification and topic extraction on it, and present the results in a way that's actually useful — not just "here's a chart." Each panel in the dashboard answers a specific question a comms or product team would actually ask.

**[Live Dashboard](#)** — coming once deployed to HuggingFace Spaces

---

## What the dashboard shows

Five panels, each with a purpose:

1. **Overview** — total posts, date range, overall sentiment split. The 10-second summary.
2. **Sentiment over time** — line chart by week. If there's a spike, I annotate it.
3. **Top topics** — TF-IDF extracted themes, shown as a bar chart by volume.
4. **Sentiment by topic** — cross-tab: for each topic, what's the sentiment breakdown? This one usually surfaces the interesting stuff.
5. **Data explorer** — filterable table. Search by keyword, filter by sentiment or date.

---

## Stack

- `pandas` / `numpy` — data wrangling
- `transformers` (HuggingFace) — sentiment model ([CAMeL-Lab arabic BERT](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment))
- `scikit-learn` — TF-IDF for topic extraction
- `plotly` — all charts
- `streamlit` — dashboard

No custom model training. The CAMeL-Lab model is pre-trained on Arabic social media text — using it directly makes more sense than fine-tuning from scratch for this scope.

---

## Dataset

Currently using [ajgt_twitter_ar](https://huggingface.co/datasets/ajgt_twitter_ar) — 1800 Arabic tweets, binary labeled (positive / negative), perfectly balanced. Small but clean. Planning to layer in the [Tunisian dialect dataset](https://www.kaggle.com/datasets/mksaad/tunisian-sentiment-twitter-dataset) from Kaggle once the base pipeline is solid.

Data lives in `data/raw/` which is gitignored. See [docs/DATASET_GUIDE.md](docs/DATASET_GUIDE.md) for notes on other datasets considered.

---

## Project structure

```
├── data/
│   ├── raw/          # gitignored
│   └── processed/    # cleaned output
├── notebooks/        # one notebook per step
├── src/              # reusable modules (cleaning, sentiment, topics, utils)
├── dashboard/
│   └── app.py        # streamlit entry point
└── docs/
    └── DATASET_GUIDE.md
```

---

## Running locally

```bash
git clone https://github.com/Mossaabjelliti/arabic-sentiment-analysis.git
cd arabic-sentiment-analysis
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
```

Download the dataset:
```python
from datasets import load_dataset
ds = load_dataset('ajgt_twitter_ar')
ds['train'].to_pandas().to_csv('data/raw/ajgt_twitter_ar.csv', index=False)
```

Run notebooks in order (`notebooks/01_eda.ipynb` → ...), then:
```bash
streamlit run dashboard/app.py
```

---

## Status

Work in progress. EDA done, cleaning and sentiment pipeline next.

Key findings will go here once the analysis is complete.


> Raw data is not committed to this repo. See `data/README.md` for download instructions.

---

## About

Built by [Your Name] as part of a data science portfolio targeting the Tunisian and MENA tech market.  
Connect on [LinkedIn](your-linkedin-url)
