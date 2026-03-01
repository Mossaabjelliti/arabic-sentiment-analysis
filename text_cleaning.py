"""
utils/text_cleaning.py
Reusable text preprocessing for Arabic, Tunisian dialect, and French text.
"""

import re


def remove_urls(text: str) -> str:
    return re.sub(r"http\S+|www\S+", "", text)


def remove_mentions_hashtags(text: str, keep_hashtag_text: bool = True) -> str:
    text = re.sub(r"@\w+", "", text)
    if keep_hashtag_text:
        text = re.sub(r"#(\w+)", r"\1", text)  # keep the word, drop the #
    else:
        text = re.sub(r"#\w+", "", text)
    return text


def remove_extra_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def normalize_arabic(text: str) -> str:
    """Normalize common Arabic character variants."""
    text = re.sub(r"[إأآا]", "ا", text)
    text = re.sub(r"ى", "ي", text)
    text = re.sub(r"ة", "ه", text)
    text = re.sub(r"گ", "ك", text)
    return text


def remove_punctuation_and_numbers(text: str) -> str:
    text = re.sub(r"[^\w\s\u0600-\u06FF]", " ", text)  # keep Arabic unicode range
    text = re.sub(r"\d+", "", text)
    return text


def clean_text(text: str, arabic_normalize: bool = True) -> str:
    """Full cleaning pipeline. Apply to every row in your dataset."""
    if not isinstance(text, str):
        return ""
    text = remove_urls(text)
    text = remove_mentions_hashtags(text)
    text = remove_punctuation_and_numbers(text)
    if arabic_normalize:
        text = normalize_arabic(text)
    text = remove_extra_whitespace(text)
    return text.lower()
