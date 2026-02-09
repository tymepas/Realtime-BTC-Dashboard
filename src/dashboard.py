import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="BTC Real-Time Dashboard",
    page_icon="₿",
    layout="wide"
)

# Title
st.title("₿ Bitcoin (BTC-USDT) Real-Time Trading Dashboard")

# File path
DATA_FILE = "data/btc_trades.csv"

# Check if file exists
if not os.path.exists(DATA_FILE):
    st.error("⚠️ No data file found! Please run `collect_data.py` first.")
    st.stop()

# Load data
@st.cache_data(ttl=5)  # Cache for 5 seconds, then reload
def load_data():
    df = pd.read_csv(DATA_FILE)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

df = load_data()

# Metrics section
col1, col2, col3, col4 = st.columns(4)

with col1:
    latest_price = df['price'].iloc[-1]
    st.metric(
        label="💰 Latest Price",
        value=f"${latest_price:,.2f}"
    )

with col2:
    total_trades = len(df)
    st.metric(
        label="📊 Total Trades",
        value=f"{total_trades}"
    )

with col3:
    avg_price = df['price'].mean()
    st.metric(
        label="📈 Average Price",
        value=f"${avg_price:,.2f}"
    )

with col4:
    price_change = df['price'].iloc[-1] - df['price'].iloc[0]
    price_change_pct = (price_change / df['price'].iloc[0]) * 100
    st.metric(
        label="📉 Change",
        value=f"${price_change:,.2f}",
        delta=f"{price_change_pct:.3f}%"
    )

# Line chart section
st.subheader("📈 Price Movement Over Time")

# Create a cleaner dataset for visualization (resample to 1-second intervals)
df_resampled = df.set_index('timestamp').resample('1s')['price'].mean().reset_index()
df_resampled = df_resampled.dropna()

st.line_chart(
    df_resampled.set_index('timestamp')['price'],
    use_container_width=True
)

# Statistics section
st.subheader("📊 Trading Statistics")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Price Range**")
    st.write(f"- **Highest**: ${df['price'].max():,.2f}")
    st.write(f"- **Lowest**: ${df['price'].min():,.2f}")
    st.write(f"- **Range**: ${df['price'].max() - df['price'].min():,.2f}")

with col2:
    st.markdown("**Volume Statistics**")
    total_volume = df['quantity'].sum()
    avg_trade_size = df['quantity'].mean()
    st.write(f"- **Total Volume**: {total_volume:.4f} BTC")
    st.write(f"- **Avg Trade Size**: {avg_trade_size:.5f} BTC")
    st.write(f"- **Largest Trade**: {df['quantity'].max():.5f} BTC")

# Buy vs Sell pressure
st.subheader("🔄 Market Pressure")
buy_orders = len(df[df['is_buyer_maker'] == False])  # False means buy order
sell_orders = len(df[df['is_buyer_maker'] == True])   # True means sell order

col1, col2 = st.columns(2)
with col1:
    st.metric("🟢 Buy Pressure", f"{buy_orders} trades ({buy_orders/len(df)*100:.1f}%)")
with col2:
    st.metric("🔴 Sell Pressure", f"{sell_orders} trades ({sell_orders/len(df)*100:.1f}%)")

# Raw data (optional, collapsible)
with st.expander("📋 View Raw Data"):
    st.dataframe(df.tail(20), use_container_width=True)

# Auto-refresh info
st.caption("💡 Dashboard auto-refreshes every 5 seconds. To collect more data, run `collect_data.py` in the background.")
