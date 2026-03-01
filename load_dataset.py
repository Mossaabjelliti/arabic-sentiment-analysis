"""
Data Loading & Exploration Helper Script
=========================================

This script provides utilities to download and explore Arabic sentiment datasets.

Usage:
    python load_dataset.py --source huggingface --dataset QCRI/ArSentiment
"""

import pandas as pd
import argparse
from pathlib import Path
from typing import Tuple
import sys

# Try importing datasets library (for HuggingFace datasets)
try:
    from datasets import load_dataset
    HAS_DATASETS = True
except ImportError:
    HAS_DATASETS = False
    print("⚠️  Install datasets library: pip install datasets")


def load_from_huggingface(dataset_name: str) -> pd.DataFrame:
    """Load dataset from HuggingFace Datasets Hub."""
    if not HAS_DATASETS:
        raise ImportError("Install datasets library: pip install datasets")
    
    print(f"📥 Loading {dataset_name} from HuggingFace...")
    
    try:
        dataset = load_dataset(dataset_name)
        
        # Convert to DataFrame (usually 'train' split)
        if 'train' in dataset:
            df = dataset['train'].to_pandas()
        else:
            # If no 'train' split, use first available
            first_split = list(dataset.keys())[0]
            df = dataset[first_split].to_pandas()
        
        print(f"✅ Loaded {len(df)} rows")
        return df
    
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        raise


def load_from_csv(file_path: str) -> pd.DataFrame:
    """Load dataset from CSV file."""
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    print(f"📥 Loading from {file_path}...")
    df = pd.read_csv(file_path)
    print(f"✅ Loaded {len(df)} rows")
    
    return df


def explore_dataset(df: pd.DataFrame) -> None:
    """Print dataset exploration report."""
    print("\n" + "="*80)
    print("DATASET EXPLORATION REPORT")
    print("="*80 + "\n")
    
    # Basic info
    print(f"📊 Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"\n📋 Columns: {list(df.columns)}")
    print(f"\n🔍 Data Types:\n{df.dtypes}")
    
    # Missing values
    print(f"\n⚠️  Missing Values:\n{df.isnull().sum()}")
    
    # Sample data
    print(f"\n📝 Sample Rows:")
    print(df.head(3).to_string())
    
    # Sentiment distribution (if applicable)
    potential_sentiment_cols = ['sentiment', 'label', 'emotion']
    for col in potential_sentiment_cols:
        if col in df.columns:
            print(f"\n😊 {col.upper()} Distribution:")
            print(df[col].value_counts())
            print(f"   Percentages:")
            print((df[col].value_counts() / len(df) * 100).round(2))
            break
    
    # Text length stats (if text column exists)
    text_cols = ['text', 'tweet', 'content', 'message']
    for col in text_cols:
        if col in df.columns:
            lengths = df[col].str.len()
            print(f"\n📏 {col.upper()} Stats:")
            print(f"   Min length: {lengths.min()}")
            print(f"   Max length: {lengths.max()}")
            print(f"   Avg length: {lengths.mean():.0f}")
            break
    
    print("\n" + "="*80 + "\n")


def save_dataset(df: pd.DataFrame, output_path: str = "data/raw/arabic_tweets.csv") -> None:
    """Save dataset to CSV."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(output_path, index=False)
    print(f"💾 Saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Load and explore Arabic sentiment datasets"
    )
    parser.add_argument(
        "--source",
        choices=["huggingface", "csv"],
        default="huggingface",
        help="Data source"
    )
    parser.add_argument(
        "--dataset",
        default="QCRI/ArSentiment",
        help="Dataset name (HuggingFace) or path (CSV)"
    )
    parser.add_argument(
        "--output",
        default="data/raw/arabic_tweets.csv",
        help="Output CSV path"
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Don't save to CSV"
    )
    
    args = parser.parse_args()
    
    # Load dataset
    if args.source == "huggingface":
        df = load_from_huggingface(args.dataset)
    else:
        df = load_from_csv(args.dataset)
    
    # Explore
    explore_dataset(df)
    
    # Save
    if not args.no_save:
        save_dataset(df, args.output)
        print(f"Next step: Open notebooks/01_eda.ipynb to analyze further")


if __name__ == "__main__":
    main()
