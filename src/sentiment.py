"""
Sentiment analysis module using pre-trained HuggingFace models.
"""

import torch
from transformers import pipeline
from typing import Dict, List, Tuple
import pandas as pd
from tqdm import tqdm


class SentimentAnalyzer:
    """Wrapper for HuggingFace sentiment models."""
    
    def __init__(self, model_name: str = "CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment"):
        """
        Initialize sentiment analyzer.
        
        Args:
            model_name: HuggingFace model identifier
        """
        self.device = 0 if torch.cuda.is_available() else -1
        self.model_name = model_name
        self.pipeline = pipeline(
            "sentiment-analysis",
            model=model_name,
            device=self.device
        )
        
    def predict(self, text: str) -> Dict:
        """
        Get sentiment for a single text.
        
        Args:
            text: Input text
            
        Returns:
            {label: str, score: float}
        """
        if not text or len(text.strip()) == 0:
            return {"label": "neutral", "score": 0.0}
        
        result = self.pipeline(text, top_k=None)
        # Get highest confidence
        best = max(result, key=lambda x: x['score'])
        return best
    
    def predict_batch(self, texts: List[str], batch_size: int = 32) -> List[Dict]:
        """
        Get sentiment for multiple texts (efficient batching).
        
        Args:
            texts: List of input texts
            batch_size: Batch size for processing
            
        Returns:
            List of {label, score} dicts
        """
        results = []
        for i in tqdm(range(0, len(texts), batch_size), desc="Sentiment Analysis"):
            batch = texts[i:i+batch_size]
            batch_results = self.pipeline(batch, top_k=None)
            
            # Extract top result for each
            for result in batch_results:
                best = max(result, key=lambda x: x['score'])
                results.append(best)
        
        return results


def analyze_sentiment_dataframe(df: pd.DataFrame, text_col: str = 'text', 
                                 model_name: str = "CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment") -> pd.DataFrame:
    """
    Add sentiment predictions to a DataFrame.
    
    Args:
        df: Input DataFrame
        text_col: Column name containing text
        model_name: HuggingFace model to use
        
    Returns:
        DataFrame with new 'sentiment' and 'confidence' columns
    """
    analyzer = SentimentAnalyzer(model_name)
    
    # Get predictions
    predictions = analyzer.predict_batch(df[text_col].tolist())
    
    # Extract labels and scores
    df['sentiment'] = [p['label'] for p in predictions]
    df['confidence'] = [p['score'] for p in predictions]
    
    return df


if __name__ == "__main__":
    # Test
    analyzer = SentimentAnalyzer()
    
    test_texts = [
        "هذا فيلم رائع جداً! أحببته كثيراً.",  # Arabic: Great movie!
        "هذا سيء جداً. لم أعجب به.",  # Arabic: This is bad.
    ]
    
    results = analyzer.predict_batch(test_texts)
    for text, result in zip(test_texts, results):
        print(f"Text: {text}")
        print(f"Sentiment: {result}\n")
