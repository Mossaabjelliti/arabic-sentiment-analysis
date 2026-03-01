"""
app/main.py
Arab Pulse — Streamlit Dashboard Entry Point
"""

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Arab Pulse",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Sidebar ────────────────────────────────────────────────────────────────────
st.sidebar.title("🧠 Arab Pulse")
st.sidebar.markdown("Social Media Sentiment & Trend Analysis")
st.sidebar.divider()

panel = st.sidebar.radio(
    "Navigate",
    ["📊 Overview", "📈 Sentiment Over Time", "🗂️ Topic Clusters", "🔀 Sentiment by Topic", "🔍 Data Explorer"],
)

st.sidebar.divider()
st.sidebar.markdown("**Filters**")
# These will be populated once data is loaded
date_range = st.sidebar.date_input("Date range", [])
sentiment_filter = st.sidebar.multiselect(
    "Sentiment", ["Positive", "Neutral", "Negative"], default=["Positive", "Neutral", "Negative"]
)
keyword_filter = st.sidebar.text_input("Keyword search", placeholder="e.g. technologie")


# ── Data loader ────────────────────────────────────────────────────────────────
@st.cache_data
def load_data() -> pd.DataFrame:
    """Load processed data. Replace path with your actual processed CSV."""
    try:
        df = pd.read_csv("data/processed/labeled_data.csv", parse_dates=["date"])
        return df
    except FileNotFoundError:
        # Return sample structure so the app shell still renders during dev
        st.warning("⚠️ No data found at `data/processed/labeled_data.csv`. Showing placeholder UI.")
        return pd.DataFrame(columns=["text", "cleaned_text", "sentiment", "sentiment_score", "date", "language", "topic"])


df = load_data()


# ── Panel routing ──────────────────────────────────────────────────────────────
if panel == "📊 Overview":
    st.title("📊 Overview")
    st.markdown("High-level snapshot of the dataset and overall sentiment distribution.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Posts", f"{len(df):,}")
    col2.metric("Positive", f"{(df['sentiment'] == 'Positive').sum():,}" if len(df) else "—")
    col3.metric("Negative", f"{(df['sentiment'] == 'Negative').sum():,}" if len(df) else "—")
    col4.metric("Neutral", f"{(df['sentiment'] == 'Neutral').sum():,}" if len(df) else "—")

    st.info("👈 Build out each panel in `app/panels/` and import them here.")

elif panel == "📈 Sentiment Over Time":
    st.title("📈 Sentiment Over Time")
    st.markdown("How did sentiment shift across the dataset's time range?")
    # TODO: import and call panels/sentiment_over_time.py

elif panel == "🗂️ Topic Clusters":
    st.title("🗂️ Topic Clusters")
    st.markdown("What are the dominant topics in the dataset?")
    # TODO: import and call panels/topic_clusters.py

elif panel == "🔀 Sentiment by Topic":
    st.title("🔀 Sentiment by Topic")
    st.markdown("Which topics drive the most positive or negative reactions?")
    # TODO: import and call panels/sentiment_by_topic.py

elif panel == "🔍 Data Explorer":
    st.title("🔍 Data Explorer")
    st.markdown("Browse and filter individual posts.")
    if len(df):
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Data will appear here once your pipeline is complete.")
