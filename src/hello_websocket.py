import websocket
import json

# Binance WebSocket URL for BTC-USDT real-time trades
BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"

def on_message(ws, message):
    """Called every time Binance sends us a trade update"""
    data = json.loads(message)
    
    # Extract key fields
    price = data['p']  # Trade price
    quantity = data['q']  # Trade quantity
    timestamp = data['T']  # Trade timestamp
    
    print(f"BTC-USDT Trade | Price: ${price} | Qty: {quantity} BTC | Time: {timestamp}")

def on_error(ws, error):
    """Called if there's an error"""
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    """Called when connection closes"""
    print("\n--- WebSocket connection closed ---")

def on_open(ws):
    """Called when connection opens successfully"""
    print("--- Connected to Binance WebSocket! ---")
    print("Streaming live BTC-USDT trades... (will stop after 10 seconds)\n")

if __name__ == "__main__":
    # Create WebSocket connection
    ws = websocket.WebSocketApp(
        BINANCE_WS_URL,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    
    # Run for 10 seconds then close
    ws.run_forever(ping_interval=60)
