# 📊 Dataset Selection Guide

## Overview
You have 5 good options for Arabic sentiment datasets. Each has tradeoffs between size, quality, recency, and relevance.

**TL;DR**: Start with **QCRI ArSentiment** for speed. Combine with **Tunisian dialect data** for better storytelling.

---

## 🏆 Recommended: QCRI ArSentiment

**Source**: https://huggingface.co/datasets/QCRI/ArSentiment

### Why This One?
- ✅ **20,000+ tweets** — large enough for solid analysis
- ✅ **Pre-labeled** — positive/negative/neutral (ready to use)
- ✅ **High quality** — QCRI is trusted research org
- ✅ **Easy to load** — 3 lines of Python code
- ✅ **No authentication** — download directly from HuggingFace

### Download
```python
from datasets import load_dataset

# Load
dataset = load_dataset("QCRI/ArSentiment")
df = dataset['train'].to_pandas()

# Save locally
df.to_csv('data/raw/ArSentiment.csv', index=False)

# Explore
print(df.head())
print(df.columns)
print(df['sentiment'].value_counts())
```

### Dataset Structure
| Column | Type | Example |
|--------|------|---------|
| text | string | "مرحبا بك في تونس" |
| sentiment | string | "positive" |

### Pros & Cons
| Pros | Cons |
|------|------|
| Balanced class distribution | Data from 2014-2019 (older) |
| Validated annotations | MSA focused (no dialects) |
| ~20K samples (good size) | Twitter may have removed original tweets |
| Modern Standard Arabic | |

---

## 🌟 Local Relevance: Tunisian Dialect Dataset

**Source**: https://www.kaggle.com/datasets/mksaad/tunisian-sentiment-twitter-dataset

### Why Consider This?
- ✅ **LOCAL** — Tunisian data for Tunisian audience
- ✅ **Arabizi** — How Tunisians actually write online (mix of Arabic + French + Latin script)
- ✅ **Recent** — 2020-2023 data
- ✅ **Great story** — "I analyzed what Tunisians are actually talking about"

### Download
```bash
# Option 1: Kaggle API (requires setup)
pip install kaggle
kaggle datasets download -d mksaad/tunisian-sentiment-twitter-dataset
unzip tunisian-sentiment-twitter-dataset.zip
mv *.csv data/raw/

# Option 2: Download manually
# Go to: https://www.kaggle.com/datasets/mksaad/tunisian-sentiment-twitter-dataset
# Click "Download" and place in data/raw/
```

### Pros & Cons
| Pros | Cons |
|------|------|
| **Local + relevant** | Smaller dataset (~1,700-3,000 rows) |
| Arabizi (realistic dialect) | Less polished annotations |
| Recent data | Requires Kaggle account |
| Great interview story | May have some duplicates |

---

## Other Options

### 🔥 QCRI HARD (Hate & Abusive Speech)
**Source**: https://huggingface.co/datasets/QCRI/HARD
- Size: 5,000 tweets
- Labels: hate, abusive, normal
- Dialects: Egyptian, Levantine, Gulf, Maghrebi
- **Use case**: If you want to show content moderation analysis
- **Con**: Labels are for hate detection, not standard sentiment

### 📚 ASTD (Arabic Social Media Tweet Dataset)
**Source**: https://huggingface.co/datasets/QCRI/ASTD
- Size: 10,000 tweets
- Labels: objective, subjective-positive, subjective-negative
- Approach: Subjectivity-based instead of sentiment-based
- **Con**: Different label scheme (less standard)

### 🌍 Multi-Lingual (Arabic + French)
**Source**: https://huggingface.co/datasets/zeroshot/twitter-corpus-arabic-french
- Size: 50,000+ posts
- Languages: Arabic + French
- Perfect if you want multi-lingual comparative analysis
- **Con**: May need quality filtering

---

## 🚀 Quick Start: 3-Step Process

### Step 1: Pick Your Dataset
If unsure, pick **ArSentiment**. If you want local storytelling, pick **Tunisian Dialect**.

### Step 2: Download & Explore
```bash
# Copy one of these commands based on your choice:

# ArSentiment:
python load_dataset.py --source huggingface --dataset QCRI/ArSentiment

# Tunisian (after Kaggle download):
python load_dataset.py --source csv --dataset data/raw/tunisian_tweets.csv
```

### Step 3: Start Analysis
The script will automatically:
1. Download/load the data
2. Show you the structure (columns, sizes, distributions)
3. Save to `data/raw/arabic_tweets.csv`
4. You're ready for `notebooks/01_eda.ipynb`

---

## 💡 Pro Tips

### Combining Datasets
You can combine multiple datasets for a richer analysis:

```python
import pandas as pd

# Load multiple datasets
df_arsentiment = pd.read_csv('data/raw/ArSentiment.csv')
df_tunisian = pd.read_csv('data/raw/tunisian_tweets.csv')

# Standardize column names
df_arsentiment = df_arsentiment.rename(columns={'sentiment': 'label'})
df_tunisian = df_tunisian.rename(columns={'sentiment': 'label'})

# Combine
combined = pd.concat([df_arsentiment, df_tunisian], ignore_index=True)

print(f"Combined: {len(combined)} tweets")
```

### Label Mapping
Some datasets use different label names. Standardize them:

```python
label_mapping = {
    'positive': 'positive',
    'negative': 'negative',
    'neutral': 'neutral',
    'POSITIVE': 'positive',
    'NEGATIVE': 'negative',
    'NEUTRAL': 'neutral',
    'joy': 'positive',
    'sadness': 'negative',
    'anger': 'negative',
}

df['sentiment'] = df['label'].map(label_mapping)
```

---

## 📊 Expected Data Quality

| Dataset | Quality | Speed | Size | Dialect |
|---------|---------|-------|------|---------|
| ArSentiment | ⭐⭐⭐⭐⭐ | 🚀🚀 | 20K | MSA |
| Tunisian | ⭐⭐⭐⭐ | 🚀 | 2K | Dialectal |
| HARD | ⭐⭐⭐⭐⭐ | 🚀 | 5K | Dialectal |
| ASTD | ⭐⭐⭐⭐ | 🚀 | 10K | Dialectal |
| Multi-Lingual | ⭐⭐⭐ | 🚀 | 50K | Mixed |

---

## Next Steps

1. **Choose a dataset** (→ ArSentiment recommended)
2. **Run**: `python load_dataset.py --dataset QCRI/ArSentiment`
3. **Review output** and check if data looks good
4. **Open**: `notebooks/01_eda.ipynb` for deeper exploration
5. **Clean & analyze** using the pipeline

Done! 🎉

---

## Questions?

- **"Which dataset is best?"** → ArSentiment for speed; Tunisian for storytelling
- **"Can I use multiple?"** → Yes! See "Combining Datasets" section above
- **"What if I want recent data?"** → Tunisian or multi-lingual options
- **"What if I want large size?"** → Multi-lingual (50K) or combine datasets

