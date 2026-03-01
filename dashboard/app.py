"""
Streamlit dashboard for Arab Twitter Sentiment Analysis.
Run with: streamlit run dashboard/app.py
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import sys
from pathlib import Path

# Add src to path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import DASHBOARD_PAGE_CONFIG, COLORS_SENTIMENT
from src.utils import load_dataset, get_sentiment_stats, format_for_display


# Page config
st.set_page_config(**DASHBOARD_PAGE_CONFIG)

# Custom styling
st.markdown("""
<style>
    .metric-box { 
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin: 10px 0;
    }
    .header-text {
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    """Load processed data from storage."""
    try:
        df = load_dataset("data/processed/analyzed_tweets.csv")
        return df
    except FileNotFoundError:
        st.error("Dataset not found! Run the analysis notebooks first.")
        return None


def main():
    # Header
    st.markdown('<div class="header-text">🎯 Arab Twitter Pulse</div>', unsafe_allow_html=True)
    st.markdown("*Sentiment & Trend Analysis Dashboard*")
    st.divider()
    
    # Load data
    df = load_data()
    
    if df is None:
        st.info("📊 Dashboard is ready! Download data from Kaggle/HuggingFace and run the analysis notebooks.")
        return
    
    # Sidebar filters
    st.sidebar.header("🔍 Filters")
    
    # Date filter
    if 'date' in df.columns:
        date_range = st.sidebar.date_input(
            "Date Range",
            value=(df['date'].min(), df['date'].max())
        )
        df = df[(df['date'] >= pd.Timestamp(date_range[0])) & 
                (df['date'] <= pd.Timestamp(date_range[1]))]
    
    # Sentiment filter
    if 'sentiment' in df.columns:
        sentiments = st.sidebar.multiselect(
            "Sentiment",
            options=df['sentiment'].unique(),
            default=df['sentiment'].unique()
        )
        df = df[df['sentiment'].isin(sentiments)]
    
    # Keyword search
    keyword = st.sidebar.text_input("Search keyword", "")
    if keyword:
        df = df[df['text'].str.contains(keyword, case=False, na=False)]
    
    # --- PANEL 1: Overview / KPIs ---
    st.header("📊 Panel 1: Overview & KPIs")
    
    if 'sentiment' in df.columns:
        stats = get_sentiment_stats(df)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Posts", stats['total_posts'])
        with col2:
            st.metric("😊 Positive", f"{stats['positive']} ({stats['positive_pct']}%)")
        with col3:
            st.metric("😞 Negative", f"{stats['negative']} ({stats['negative_pct']}%)")
        with col4:
            st.metric("😐 Neutral", f"{stats['neutral']} ({stats['neutral_pct']}%)")
        
        # Sentiment pie chart
        fig_pie = px.pie(
            values=[stats['positive'], stats['negative'], stats['neutral']],
            names=['Positive', 'Negative', 'Neutral'],
            color_discrete_map=COLORS_SENTIMENT,
            title="Sentiment Distribution"
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    st.divider()
    
    # --- PANEL 2: Sentiment Over Time ---
    st.header("📈 Panel 2: Sentiment Over Time")
    
    if 'date' in df.columns and 'sentiment' in df.columns:
        daily_sentiment = df.groupby(['date', 'sentiment']).size().unstack(fill_value=0)
        
        fig_time = go.Figure()
        for sentiment in ['positive', 'negative', 'neutral']:
            if sentiment in daily_sentiment.columns:
                fig_time.add_trace(go.Scatter(
                    x=daily_sentiment.index,
                    y=daily_sentiment[sentiment],
                    mode='lines+markers',
                    name=sentiment.capitalize(),
                    line=dict(color=COLORS_SENTIMENT.get(sentiment, '#95a5a6'), width=2)
                ))
        
        fig_time.update_layout(
            title="Sentiment Over Time",
            xaxis_title="Date",
            yaxis_title="Number of Posts",
            hovermode='x unified',
            height=400
        )
        st.plotly_chart(fig_time, use_container_width=True)
    else:
        st.info("Date and sentiment columns required for this panel.")
    
    st.divider()
    
    # --- PANEL 3: Topic Extraction ---
    st.header("🗂️ Panel 3: Top Topics")
    
    st.info("Topics will be extracted using TF-IDF in the analysis notebooks.")
    
    st.divider()
    
    # --- PANEL 4: Sentiment by Topic ---
    st.header("🔀 Panel 4: Sentiment by Topic")
    
    st.info("Cross-tab analysis will be generated after topic extraction.")
    
    st.divider()
    
    # --- PANEL 5: Raw Data Explorer ---
    st.header("🔍 Panel 5: Raw Data Explorer")
    
    st.write(f"Showing {len(df)} posts")
    
    # Display data with limited columns
    display_cols = ['text', 'sentiment', 'confidence'] if 'confidence' in df.columns else ['text', 'sentiment']
    if 'date' in df.columns:
        display_cols.insert(0, 'date')
    
    st.dataframe(
        format_for_display(df[display_cols], max_rows=100),
        use_container_width=True
    )
    
    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download filtered data as CSV",
        data=csv,
        file_name=f"sentiment_data_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )


if __name__ == "__main__":
    main()
