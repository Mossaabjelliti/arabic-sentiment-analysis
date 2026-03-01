"""
Topic extraction and LDA modeling utilities.
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from typing import List, Dict, Tuple
from .text_cleaning import tokenize_text, remove_stopwords


class TopicExtractor:
    """Extract topics using TF-IDF and optionally LDA."""
    
    def __init__(self, max_features: int = 1000, min_df: int = 2, max_df: float = 0.8):
        """
        Initialize TopicExtractor.
        
        Args:
            max_features: Maximum number of features for TF-IDF
            min_df: Minimum document frequency
            max_df: Maximum document frequency
        """
        self.max_features = max_features
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            min_df=min_df,
            max_df=max_df,
            stop_words=self.get_stopwords()
        )
        self.lda_model = None
        self.feature_names = None
        self.tfidf_matrix = None
    
    @staticmethod
    def get_stopwords() -> List[str]:
        """Get Arabic and French stopwords."""
        arabic_stops = [
            'في', 'من', 'إلى', 'هذا', 'ذلك', 'التي', 'الذي', 'اللي',
            'أن', 'إن', 'هو', 'هي', 'هم', 'هن', 'و', 'ف', 'ب', 'ل', 'ال'
        ]
        french_stops = [
            'le', 'la', 'les', 'de', 'des', 'un', 'une', 'et', 'ou',
            'à', 'au', 'en', 'on', 'que', 'ce', 'est', 'sont'
        ]
        return arabic_stops + french_stops
    
    def fit(self, texts: List[str]) -> 'TopicExtractor':
        """
        Fit TF-IDF vectorizer on texts.
        
        Args:
            texts: List of documents
            
        Returns:
            self
        """
        self.tfidf_matrix = self.vectorizer.fit_transform(texts)
        self.feature_names = self.vectorizer.get_feature_names_out()
        return self
    
    def get_top_topics(self, n_topics: int = 10, top_terms: int = 5) -> List[Dict]:
        """
        Get top topics based on TF-IDF.
        
        Args:
            n_topics: Number of topics to extract
            top_terms: Number of top terms per topic
            
        Returns:
            List of {topic_id, terms, scores}
        """
        if self.tfidf_matrix is None:
            raise ValueError("Must call fit() first")
        
        # Get mean TF-IDF scores per term
        mean_tfidf = np.asarray(self.tfidf_matrix.mean(axis=0)).flatten()
        
        # Get top term indices
        top_indices = np.argsort(mean_tfidf)[-n_topics*top_terms:][::-1]
        
        topics = []
        for i in range(0, len(top_indices), top_terms):
            topic_indices = top_indices[i:i+top_terms]
            terms = [self.feature_names[idx] for idx in topic_indices]
            scores = [mean_tfidf[idx] for idx in topic_indices]
            
            topics.append({
                'topic_id': i // top_terms,
                'terms': terms,
                'scores': scores
            })
        
        return topics[:n_topics]
    
    def fit_lda(self, texts: List[str], n_topics: int = 8, max_iter: int = 10) -> 'TopicExtractor':
        """
        Fit LDA model for topic modeling.
        
        Args:
            texts: List of documents
            n_topics: Number of topics
            max_iter: Maximum iterations
            
        Returns:
            self
        """
        self.fit(texts)
        
        self.lda_model = LatentDirichletAllocation(
            n_components=n_topics,
            max_iter=max_iter,
            random_state=42,
            n_jobs=-1
        )
        self.lda_model.fit(self.tfidf_matrix)
        return self
    
    def get_lda_topics(self, n_words: int = 5) -> List[Dict]:
        """
        Get topics from LDA model.
        
        Args:
            n_words: Number of words per topic
            
        Returns:
            List of {topic_id, terms}
        """
        if self.lda_model is None:
            raise ValueError("Must call fit_lda() first")
        
        topics = []
        for topic_idx, topic in enumerate(self.lda_model.components_):
            top_indices = topic.argsort()[-n_words:][::-1]
            top_terms = [self.feature_names[i] for i in top_indices]
            
            topics.append({
                'topic_id': topic_idx,
                'terms': top_terms
            })
        
        return topics


def extract_topics_from_dataframe(
    df: pd.DataFrame,
    text_col: str = 'text',
    n_topics: int = 10,
    top_terms: int = 5
) -> Tuple[TopicExtractor, List[Dict]]:
    """
    Convenience function to extract topics from a DataFrame.
    
    Args:
        df: Input DataFrame
        text_col: Column containing text
        n_topics: Number of topics
        top_terms: Terms per topic
        
    Returns:
        (TopicExtractor object, list of topics)
    """
    extractor = TopicExtractor()
    extractor.fit(df[text_col].tolist())
    topics = extractor.get_top_topics(n_topics=n_topics, top_terms=top_terms)
    
    return extractor, topics


if __name__ == "__main__":
    # Test
    sample_texts = [
        "تونس بلد جميل وسياحة رائعة",
        "التكنولوجيا تغير العالم بسرعة",
        "الفيلم كان ممل جداً",
    ]
    
    extractor = TopicExtractor()
    extractor.fit(sample_texts)
    topics = extractor.get_top_topics(n_topics=3, top_terms=3)
    
    for topic in topics:
        print(f"Topic {topic['topic_id']}: {', '.join(topic['terms'])}")
