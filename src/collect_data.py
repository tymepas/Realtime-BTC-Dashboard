import websocket
import json
import pandas as pd
import os
from datetime import datetime
import time

# Configuration
BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"
DATA_DIR = "data"
FILE_PATH = os.path.join(DATA_DIR, "btc_trades.csv")
MAX_TRADES = 5000  # Stop after collecting 100 trades (for testing)

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Counter for trades
trade_count = 0

def on_message(ws, message):
    """Called every time Binance sends a trade update"""
    global trade_count
    
    # Parse the JSON message
    data = json.loads(message)
    
    # Extract and structure the data
    trade_data = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'price': float(data['p']),
        'quantity': float(data['q']),
        'trade_time_ms': data['T'],
        'is_buyer_maker': data['m']
    }
    
    # Convert to DataFrame
    df = pd.DataFrame([trade_data])
    
    # Append to CSV
    file_exists = os.path.exists(FILE_PATH)
    df.to_csv(FILE_PATH, mode='a', header=not file_exists, index=False)
    
    # Increment counter
    trade_count += 1
    
    # Print progress
    print(f"Trade {trade_count}/{MAX_TRADES} | Price: ${trade_data['price']:,.2f} | Qty: {trade_data['quantity']:.5f} BTC")
    
    # Stop after reaching max trades
    if trade_count >= MAX_TRADES:
        print(f"\n✅ Collected {MAX_TRADES} trades successfully!")
        print(f"📁 Data saved to: {FILE_PATH}")
        ws.close()

def on_error(ws, error):
    """Called if there's an error"""
    print(f"❌ Error: {error}")

def on_close(ws, close_status_code, close_msg):
    """Called when connection closes"""
    print("\n--- WebSocket connection closed ---")
    print(f"Total trades collected: {trade_count}")

def on_open(ws):
    """Called when connection opens successfully"""
    print("🚀 Connected to Binance WebSocket!")
    print(f"📊 Collecting {MAX_TRADES} BTC-USDT trades...\n")

if __name__ == "__main__":
    print("Starting BTC-USDT trade collector...")
    print("Press Ctrl+C to stop manually\n")
    
    try:
        ws = websocket.WebSocketApp(
            BINANCE_WS_URL,
            on_open=on_open,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close
        )
        
        ws.run_forever(ping_interval=60)
        
    except KeyboardInterrupt:
        print("\n⚠️ Stopped by user (Ctrl+C)")
        print(f"Total trades collected: {trade_count}")
