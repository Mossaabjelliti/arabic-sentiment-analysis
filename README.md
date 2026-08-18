# Arabic Social Media Sentiment Analysis 🇹🇳🤖

> An NLP analytics dashboard for Arabic social-media content, combining transformer-based sentiment classification with topic extraction and interactive data exploration.

This project takes a corpus of Arabic social-media posts, processes the text, performs sentiment analysis, extracts recurring topics, and presents the results through an interactive Streamlit dashboard.

The focus is applied NLP: turning unstructured Arabic text into information that a product, communications, or research team could explore.

## What the dashboard answers

1. **Overview** — What is the overall sentiment distribution and date range?
2. **Sentiment over time** — How does sentiment change across the observed period?
3. **Top topics** — Which themes appear most frequently?
4. **Sentiment by topic** — Which topics are associated with positive or negative sentiment?
5. **Data explorer** — Which posts match a keyword, sentiment, or date filter?

## NLP pipeline

```text
Arabic social-media posts
          ↓
Text cleaning / normalization
          ↓
Transformer-based sentiment model
          ↓
Sentiment predictions
          ↓
TF-IDF topic extraction
          ↓
Aggregation & analysis
          ↓
Interactive Streamlit dashboard
```

## Technical approach

### Sentiment analysis

The project uses the pretrained **CAMeL-Lab Arabic BERT / CamelBERT sentiment model** from Hugging Face rather than training a transformer from scratch.

This is a deliberate engineering choice: for a portfolio-scale applied NLP project, a domain-relevant pretrained model provides a strong baseline while keeping the pipeline practical and reproducible.

### Topic extraction

TF-IDF is used to identify representative terms and recurring themes in the corpus. The approach is lightweight and interpretable, making it useful for exploratory analysis.

## Tech stack

| Component | Technology |
|---|---|
| Language | Python |
| Data processing | pandas, NumPy |
| NLP | Hugging Face Transformers |
| Sentiment model | CAMeL-Lab Arabic BERT / CamelBERT |
| Topic extraction | scikit-learn TF-IDF |
| Visualization | Plotly |
| Dashboard | Streamlit |

## Dataset

The baseline uses the `ajgt_twitter_ar` Arabic Twitter dataset available through Hugging Face. The current dataset contains 1,800 binary-labeled Arabic tweets and is balanced between positive and negative examples.

Raw data is not committed to the repository. A Tunisian-dialect dataset is planned as an additional evaluation source to make the analysis more representative of local Arabic usage.

## Project structure

```text
├── data/
│   ├── raw/             # gitignored source data
│   └── processed/       # cleaned/processed outputs
├── notebooks/           # EDA and analysis notebooks
├── src/                 # reusable processing and NLP modules
├── dashboard/
│   └── app.py           # Streamlit entry point
├── docs/
│   └── DATASET_GUIDE.md
├── requirements.txt
└── README.md
```

## Running locally

```bash
git clone https://github.com/Mossaabjelliti/arabic-sentiment-analysis.git
cd arabic-sentiment-analysis

python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

Download the dataset:

```python
from datasets import load_dataset

ds = load_dataset("ajgt_twitter_ar")
ds["train"].to_pandas().to_csv("data/raw/ajgt_twitter_ar.csv", index=False)
```

Run the dashboard:

```bash
streamlit run dashboard/app.py
```

## Evaluation

The project should be evaluated using standard classification metrics:

- Accuracy
- Precision
- Recall
- F1 score
- Confusion matrix

> Evaluation numbers should be added after the final preprocessing/model pipeline is frozen. This README intentionally avoids inventing benchmark results.

## Limitations

- The baseline dataset is relatively small.
- Arabic social-media language contains dialects, slang, spelling variation, emojis, and code-switching.
- A pretrained Arabic model may not fully represent Tunisian dialect usage.
- TF-IDF topics are interpretable but do not capture semantic relationships as deeply as embedding-based topic models.

## Roadmap

- [ ] Finish the end-to-end preprocessing pipeline
- [ ] Add reproducible evaluation and benchmark metrics
- [ ] Evaluate Tunisian-dialect data
- [ ] Add confusion-matrix and error-analysis views
- [ ] Add model comparison
- [ ] Deploy the Streamlit dashboard

## Author

**Mossaab Jelliti**

Data science and software engineering portfolio project focused on Arabic NLP and practical analytics.

- GitHub: [@Mossaabjelliti](https://github.com/Mossaabjelliti)
