"""
Utility functions for data loading, formatting, and visualization.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Union, Tuple
import json


def load_dataset(file_path: Union[str, Path]) -> pd.DataFrame:
    """
    Load dataset from various formats.
    
    Args:
        file_path: Path to dataset (csv, json, xlsx, parquet)
        
    Returns:
        DataFrame
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if file_path.suffix == '.csv':
        return pd.read_csv(file_path)
    
    elif file_path.suffix == '.json':
        return pd.read_json(file_path)
    
    elif file_path.suffix in ['.xlsx', '.xls']:
        return pd.read_excel(file_path)
    
    elif file_path.suffix == '.parquet':
        return pd.read_parquet(file_path)
    
    else:
        raise ValueError(f"Unsupported file format: {file_path.suffix}")


def save_dataset(df: pd.DataFrame, file_path: Union[str, Path], format: str = 'csv') -> None:
    """
    Save DataFrame to various formats.
    
    Args:
        df: DataFrame to save
        file_path: Output path
        format: 'csv', 'json', 'parquet', or 'xlsx'
    """
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    if format == 'csv':
        df.to_csv(file_path, index=False)
    elif format == 'json':
        df.to_json(file_path, orient='records', force_ascii=False)
    elif format == 'parquet':
        df.to_parquet(file_path, index=False)
    elif format == 'xlsx':
        df.to_excel(file_path, index=False)
    else:
        raise ValueError(f"Unsupported format: {format}")


def get_sentiment_stats(df: pd.DataFrame, sentiment_col: str = 'sentiment') -> dict:
    """
    Calculate sentiment statistics.
    """
    value_counts = df[sentiment_col].value_counts()
    total = len(df)
    
    return {
        'total_posts': total,
        'positive': int(value_counts.get('positive', 0)),
        'negative': int(value_counts.get('negative', 0)),
        'neutral': int(value_counts.get('neutral', 0)),
        'positive_pct': round(value_counts.get('positive', 0) / total * 100, 2),
        'negative_pct': round(value_counts.get('negative', 0) / total * 100, 2),
        'neutral_pct': round(value_counts.get('neutral', 0) / total * 100, 2),
    }


def format_for_display(df: pd.DataFrame, max_rows: int = 100) -> pd.DataFrame:
    """
    Format DataFrame for display in Streamlit.
    """
    display_df = df.copy()
    
    # Truncate long text columns
    for col in display_df.columns:
        if display_df[col].dtype == 'object':
            display_df[col] = display_df[col].apply(
                lambda x: str(x)[:200] + "..." if len(str(x)) > 200 else x
            )
    
    return display_df.head(max_rows)


if __name__ == "__main__":
    # Example usage
    # df = load_dataset("data/raw/tweets.csv")
    # stats = get_sentiment_stats(df)
    # print(stats)
    pass
