# Dataset Notes

Starting with **ajgt_twitter_ar** — 1800 labeled Arabic tweets (binary: positive/negative). Small but clean and fast to work with. Plan is to add a 3-class dataset or the Tunisian dialect data later.

---

## Datasets Considered

### ajgt_twitter_ar (current)
https://huggingface.co/datasets/ajgt_twitter_ar

1800 tweets, Modern Standard Arabic, perfectly balanced (900 positive, 900 negative). Labels are binary integers: `1 = positive`, `0 = negative`. No neutral class. Data is from Arabic Twitter, mixed dialects.

```python
from datasets import load_dataset
import pandas as pd

ds = load_dataset('ajgt_twitter_ar')
df = ds['train'].to_pandas()

# Map integer labels to strings
df['sentiment'] = df['label'].map({1: 'positive', 0: 'negative'})
df.to_csv('data/raw/ajgt_twitter_ar.csv', index=False)
```

Columns after loading: `text`, `label` (0/1), `sentiment` (after mapping)

One thing to keep in mind: binary labels mean no neutral class, which limits the analysis a bit. Worth combining with another dataset down the line.

---

### Tunisian Dialect (next)
https://www.kaggle.com/datasets/mksaad/tunisian-sentiment-twitter-dataset

Smaller (~1,700-3,000 rows) but locally relevant — Arabizi (Tunisian dialect written in Latin script mixed with Arabic). Worth adding once the base pipeline works. Requires Kaggle account to download.

---

### QCRI/ArSentiment (tried, not accessible)
Was the original plan but the dataset path doesn't exist on the Hub anymore. Might have been taken down or moved.

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
    1: 'positive', 0: 'negative',
}
df['sentiment'] = df['label'].map(label_map)
```


