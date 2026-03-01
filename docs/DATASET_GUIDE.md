# Dataset Notes

Starting with **QCRI ArSentiment** — ~20K labeled Arabic tweets (positive/negative/neutral), easiest to load, decent quality. Plan is to add the Tunisian dialect dataset later for the local angle.

---

## Datasets Considered

### ArSentiment (current)
https://huggingface.co/datasets/QCRI/ArSentiment

~20K tweets, Modern Standard Arabic, labeled by QCRI researchers. Data is from 2014-2019 so it's a bit dated, and it's MSA-only (no dialects), but the annotations are reliable and it loads in 3 lines. Good enough to build the full pipeline.

```python
from datasets import load_dataset

dataset = load_dataset("QCRI/ArSentiment")
df = dataset['train'].to_pandas()
df.to_csv('data/raw/ArSentiment.csv', index=False)
```

Columns: `text`, `label` (positive / negative / neutral)

---

### Tunisian Dialect (next)
https://www.kaggle.com/datasets/mksaad/tunisian-sentiment-twitter-dataset

Smaller (~1,700-3,000 rows) but locally relevant — Arabizi (Tunisian dialect written in Latin script mixed with Arabic). Worth adding once the base pipeline works. Requires Kaggle account to download.

---

### Other options (not using for now)

**QCRI HARD** — 5K tweets, focused on hate/abusive speech detection. Labels don't map cleanly to sentiment, skipping.

**ASTD** — 10K tweets, uses "objective/subjective" labels rather than pos/neg/neutral. Different framing, not a good fit.

**Arabic+French mixed** (`zeroshot/twitter-corpus-arabic-french`) — 50K+ posts, bilingual. Might be worth revisiting if the multilingual angle becomes important.

---

## If you want to combine datasets later

Different datasets use slightly different label names. Normalize before merging:

```python
label_map = {
    'POSITIVE': 'positive', 'NEGATIVE': 'negative', 'NEUTRAL': 'neutral',
    'pos': 'positive', 'neg': 'negative', 'neu': 'neutral',
}
df['sentiment'] = df['label'].str.lower().map(label_map).fillna(df['label'])
```

