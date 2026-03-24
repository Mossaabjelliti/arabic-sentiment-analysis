"""
Text cleaning and normalization utilities for Arabic text.
"""

import re
from typing import List


def clean_arabic(text: str) -> str:
    """
    Clean a single Arabic tweet.
    Steps: remove URLs/mentions/hashtag symbols, strip diacritics,
    normalize letter forms (alef variants, teh marbuta, alef maqsura),
    remove tatweel and non-Arabic characters, collapse whitespace.
    """
    if not isinstance(text, str) or not text.strip():
        return ""

    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#(\w+)', r'\1', text)
    text = re.sub(r'[\u064B-\u065F]', '', text)   # diacritics
    text = re.sub(r'[أإآٱ]', 'ا', text)            # alef variants
    text = re.sub(r'ة', 'ه', text)                 # teh marbuta
    text = re.sub(r'ى', 'ي', text)                 # alef maqsura
    text = re.sub(r'ـ', '', text)                  # tatweel
    text = re.sub(r'[^\u0600-\u06FF\s]', '', text) # non-Arabic
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def clean_batch(texts: List[str]) -> List[str]:
    """Apply clean_arabic to a list of texts."""
    return [clean_arabic(t) for t in texts]

