"""
Configuration file for the sentiment analysis project.
Contains paths, model names, and constants.
"""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
DASHBOARD_DIR = PROJECT_ROOT / "dashboard"
SRC_DIR = PROJECT_ROOT / "src"

# Sentiment Model
ARABIC_SENTIMENT_MODEL = "CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment"
MULTILINGUAL_SENTIMENT_MODEL = "nlptown/bert-base-multilingual-uncased-sentiment"

# TF-IDF & Topic Extraction
TF_IDF_MAX_FEATURES = 1000
LDA_N_TOPICS = 8
LDA_MAX_ITER = 10

# Text Processing
STOPWORDS_ARABIC = ["في", "من", "إلى", "هذا", "ذلك", "التي", "الذي"]  # Add more
STOPWORDS_FRENCH = ["le", "la", "de", "et", "à", "en", "un", "une", "est"]  # Add more

# Visualization
COLORS_SENTIMENT = {
    "positive": "#2ecc71",  # Green
    "negative": "#e74c3c",  # Red
    "neutral": "#95a5a6"    # Gray
}

# Dashboard
DASHBOARD_PAGE_CONFIG = {
    "page_title": "Arab Twitter Pulse",
    "page_icon": "📊",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}
