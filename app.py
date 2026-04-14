import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    trades = pd.read_csv('historical_data.csv')
    fgi = pd.read_csv('fear_greed_index.csv')
    
    trades['Date'] = pd.to_datetime(trades['Timestamp IST'], format='%d-%m-%Y %H:%M').dt.date
    trades['Date'] = pd.to_datetime(trades['Date'])
    fgi['Date'] = pd.to_datetime(fgi['date'])
    
    def simplify_sentiment(x):
        if 'Fear' in x: return 'Fear'
        elif 'Greed' in x: return 'Greed'
        return 'Neutral'
    fgi['Sentiment'] = fgi['classification'].apply(simplify_sentiment)
    
    df = trades.merge(fgi[['Date', 'value', 'Sentiment']], on='Date', how='inner')
    df['Win'] = (df['Closed PnL'] > 0).astype(int)
    return df

st.title("Crypto Trader Behavioral Dashboard")
st.write("Analyze how Fear and Greed impacts trading performance.")

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
selected_sentiment = st.sidebar.multiselect("Select Market Sentiment", options=df['Sentiment'].unique(), default=df['Sentiment'].unique())

filtered_df = df[df['Sentiment'].isin(selected_sentiment)]

# KPIs
st.header("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Trades", len(filtered_df))
col2.metric("Total PnL ($)", f"{filtered_df['Closed PnL'].sum():,.2f}")
col3.metric("Average Trade Size ($)", f"{filtered_df['Size USD'].mean():,.2f}")

# Charts
st.header("Visualizations")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(data=filtered_df[filtered_df['Size USD'] < filtered_df['Size USD'].quantile(0.95)], x='Size USD', hue='Sentiment', bins=50, kde=True, ax=ax)
ax.set_title("Distribution of Trade Sizes (Bottom 95%)")
st.pyplot(fig)