"""
Dataset Selection Guide for Arabic Sentiment Analysis
======================================================

This script provides information on the best publicly available Arabic sentiment datasets.
Choose one of these to download and place in data/raw/

"""

datasets_info = {
    "QCRI_ArSentiment": {
        "name": "ArSentiment - QCRI (Recommended)",
        "source": "https://huggingface.co/datasets/QCRI/ArSentiment",
        "language": "Modern Standard Arabic (MSA)",
        "dialects": "None (MSA focused)",
        "size": "~20,000+ tweets",
        "labels": ["positive", "negative", "neutral"],
        "format": "CSV/JSON",
        "date_range": "2014-2019",
        "pros": [
            "✅ Balanced dataset",
            "✅ Pre-labeled & validated",
            "✅ High quality annotations",
            "✅ Easy to load with HuggingFace datasets library",
            "✅ Multiple license-friendly file formats"
        ],
        "cons": [
            "❌ Older date range (2014-2019)",
            "❌ Only MSA, no dialects"
        ],
        "download_command": """
# Method 1: HuggingFace Hub (Recommended)
from datasets import load_dataset
dataset = load_dataset("QCRI/ArSentiment")
df = dataset['train'].to_pandas()

# Save locally
df.to_csv('data/raw/ArSentiment.csv', index=False)
        """,
        "expected_columns": ["text", "label"],
        "notes": "Very clean dataset, perfect for portfolio projects"
    },
    
    "QCRI_HARD": {
        "name": "HARD - Hate & Abusive Sentiments - QCRI",
        "source": "https://huggingface.co/datasets/QCRI/HARD",
        "language": "Modern Standard Arabic + Dialects",
        "dialects": "Egyptian, Levantine, Gulf, Maghrebi",
        "size": "~5,000 tweets",
        "labels": ["hate", "abusive", "normal"],
        "format": "CSV/JSON",
        "date_range": "Recent (2020s)",
        "pros": [
            "✅ Multiple Arabic dialects",
            "✅ More recent data",
            "✅ QCRI high-quality annotations",
            "✅ Important for moderation context"
        ],
        "cons": [
            "❌ Smaller dataset (5K tweets)",
            "❌ Focuses on hate/abuse labels (not standard sentiment)"
        ],
        "expected_columns": ["text", "label"],
        "notes": "Good for hate speech detection, not ideal for general sentiment"
    },
    
    "Tunisian_Dialect": {
        "name": "Tunisian Dialect Sentiment (Arabizi)",
        "source": "https://www.kaggle.com/datasets/mksaad/tunisian-sentiment-twitter-dataset",
        "language": "Tunisian Dialect (Arabizi)",
        "dialects": "Tunisian Arabizi (transliterated Arabic)",
        "size": "~1,700-3,000 tweets",
        "labels": ["positive", "negative", "neutral"],
        "format": "CSV",
        "date_range": "2020-2023",
        "pros": [
            "✅ LOCALLY RELEVANT - Perfect for Tunisian market",
            "✅ Arabizi & dialectal content",
            "✅ Recent data",
            "✅ Great for case study narrative"
        ],
        "cons": [
            "❌ Requires Kaggle account",
            "❌ Smaller dataset",
            "❌ Mixed quality annotations"
        ],
        "download_command": """
# Via Kaggle API
kaggle datasets download -d mksaad/tunisian-sentiment-twitter-dataset
unzip tunisian-sentiment-twitter-dataset.zip
mv data/raw/

# Or download manually from Kaggle website
        """,
        "expected_columns": ["text", "sentiment"],
        "notes": "BEST for your Tunisian company angle!"
    },
    
    "ASTD": {
        "name": "Arabic Social Media Tweet Dataset (ASTD)",
        "source": "https://huggingface.co/datasets/QCRI/ASTD",
        "language": "Modern Standard Arabic + Dialects",
        "dialects": "Egyptian, Levantine, Gulf",
        "size": "~10,000 tweets",
        "labels": ["objective", "subjective-positive", "subjective-negative"],
        "format": "CSV",
        "date_range": "2014-2016",
        "pros": [
            "✅ Diverse dialects",
            "✅ Large enough sample",
            "✅ Objective/Subjective distinction"
        ],
        "cons": [
            "❌ Older data",
            "❌ Different label scheme (objectivity-based)"
        ],
        "expected_columns": ["text", "label"],
        "notes": "Good alternative, but ASTD labels are less standard"
    },
    
    "Multi_Lingual_Arabic": {
        "name": "Arabic+French Mixed Social Media",
        "source": "https://huggingface.co/datasets/zeroshot/twitter-corpus-arabic-french",
        "language": "Arabic + French",
        "dialects": "MSA + dialectal Arabic + French",
        "size": "~50,000+ posts (mixed languages)",
        "labels": ["positive", "negative", "neutral"],
        "format": "JSON",
        "date_range": "2020-2023",
        "pros": [
            "✅ PERFECT for multi-lingual dashboard",
            "✅ Large dataset",
            "✅ Recent data",
            "✅ French content included"
        ],
        "cons": [
            "❌ May need filtering for quality",
            "❌ Language detection required"
        ],
        "expected_columns": ["text", "sentiment", "language"],
        "notes": "BEST if you want to show multi-lingual analysis!"
    }
}


def print_dataset_guide():
    """Print formatted guide for all datasets."""
    print("\n" + "="*80)
    print("ARABIC SENTIMENT ANALYSIS DATASET GUIDE")
    print("="*80 + "\n")
    
    for i, (key, info) in enumerate(datasets_info.items(), 1):
        print(f"\n{'='*80}")
        print(f"{i}. {info['name'].upper()}")
        print(f"{'='*80}")
        print(f"Source:     {info['source']}")
        print(f"Language:   {info['language']}")
        print(f"Dialects:   {info['dialects']}")
        print(f"Size:       {info['size']}")
        print(f"Labels:     {', '.join(info['labels'])}")
        print(f"Date Range: {info['date_range']}")
        
        print("\nPROS:")
        for pro in info['pros']:
            print(f"  {pro}")
        
        print("\nCONS:")
        for con in info['cons']:
            print(f"  {con}")
        
        if 'download_command' in info:
            print(f"\nDOWNLOAD:")
            print(info['download_command'])
        
        print(f"\nNOTES: {info['notes']}")


def get_recommendations():
    """Print personalized recommendations."""
    print("\n" + "="*80)
    print("RECOMMENDATIONS FOR YOUR PROJECT")
    print("="*80 + "\n")
    
    print("🎯 BEST FOR SPEED (Day 1-2):")
    print("   → Use: QCRI ArSentiment")
    print("     Why: Largest, cleanest, easiest to load")
    print("     Load: from datasets import load_dataset")
    print("           df = load_dataset('QCRI/ArSentiment')['train'].to_pandas()")
    
    print("\n🎯 BEST FOR STORYTELLING (Impress interviewers):")
    print("   → Use: Tunisian Dialect Dataset")
    print("     Why: Local relevance = compelling narrative")
    print("     Story: 'I analyzed what Tunisians actually say online'")
    
    print("\n🎯 BEST FOR COMPREHENSIVE ANALYSIS (Stretch goal):")
    print("   → Combine: ArSentiment + Tunisian + Multi-Lingual")
    print("     Why: Can show comparative analysis across dialects & languages")
    
    print("\n🎯 QUICK START RECOMMENDATION:")
    print("""
   1. Download ArSentiment from HuggingFace (easiest)
   2. Add Tunisian data if available (50% bonus storytelling)
   3. Run full pipeline on combined dataset
   4. Highlight Tunisian sentiment insights in dashboard
    """)


if __name__ == "__main__":
    print_dataset_guide()
    print("\n")
    get_recommendations()
