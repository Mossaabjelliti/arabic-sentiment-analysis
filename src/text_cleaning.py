"""
Text cleaning and normalization utilities for Arabic and French text.
"""

import re
import unicodedata
from typing import List
import nltk

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


def normalize_arabic_text(text: str) -> str:
    """
    Normalize Arabic text: remove diacritics, extra spaces, special chars.
    """
    # Remove diacritics
    text = re.sub(r'[\u064B-\u065F]', '', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # Remove @mentions and hashtags (but keep the text)
    text = re.sub(r'@\w+|#\w+', '', text)
    
    # Remove non-Arabic/non-ASCII characters but preserve important punctuation
    text = re.sub(r'[^\u0600-\u06FF\u0750-\u077Fa-zA-Z0-9\s\.\!\?،]', '', text)
    
    # Normalize space-like characters
    text = text.replace('\u200C', ' ').replace('\u200D', ' ')
    
    # Lowercase
    text = text.lower()
    
    return text.strip()


def clean_text(text: str, language: str = 'arabic') -> str:
    """
    Main text cleaning function. Routes to language-specific cleaners.
    
    Args:
        text: Raw text to clean
        language: 'arabic' or 'french'
    
    Returns:
        Cleaned text
    """
    if not text or not isinstance(text, str):
        return ""
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    
    # Remove @mentions
    text = re.sub(r'@\w+', '', text)
    
    # Remove hashtags but keep content
    text = re.sub(r'#(\w+)', r'\1', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    if language.lower() == 'arabic':
        text = normalize_arabic_text(text)
    elif language.lower() == 'french':
        text = text.lower()
    else:
        text = text.lower()
    
    return text.strip()


def tokenize_text(text: str, language: str = 'arabic') -> List[str]:
    """
    Tokenize text into words.
    """
    if not text:
        return []
    
    # Simple word tokenization
    if language.lower() == 'arabic':
        tokens = re.findall(r'[\u0600-\u06FF]+|[a-z]+', text.lower())
    else:
        tokens = re.findall(r'\b\w+\b', text.lower())
    
    return tokens


def remove_stopwords(tokens: List[str], language: str = 'arabic') -> List[str]:
    """
    Remove common stopwords.
    """
    arabic_stopwords = {
        'في', 'من', 'إلى', 'هذا', 'ذلك', 'التي', 'الذي', 'اللي',
        'أن', 'إن', 'هو', 'هي', 'هم', 'هن', 'أنا', 'أنت',
        'و', 'ف', 'ب', 'ل', 'ال', 'هل', 'ما', 'لا', 'نعم',
    }
    
    french_stopwords = {
        'le', 'la', 'les', 'de', 'des', 'un', 'une', 'et', 'ou',
        'à', 'au', 'en', 'on', 'que', 'qui', 'ce', 'est', 'sont',
        'pas', 'ne', 'pour', 'avec', 'par', 'mais', 'ou', 'donc',
    }
    
    if language.lower() == 'arabic':
        stopwords = arabic_stopwords
    else:
        stopwords = french_stopwords
    
    return [t for t in tokens if t not in stopwords and len(t) > 2]


if __name__ == "__main__":
    # Test examples
    test_ar = "مرحبا بك في تونس! 🇹🇳 #تونس @user http://example.com"
    test_fr = "Bonjour à tous! C'est un test. #Tunisia @somebody"
    
    print("Arabic:", clean_text(test_ar, 'arabic'))
    print("French:", clean_text(test_fr, 'french'))
