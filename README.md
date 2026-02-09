# ₿ Real-Time Bitcoin (BTC-USDT) Trading Dashboard

A complete **real-time data pipeline and analytics dashboard** for Bitcoin (BTC-USDT) trades, built with Python, WebSockets, and Streamlit.

![Dashboard Screenshot](screenshot.png)

## 🚀 Project Overview

This project demonstrates end-to-end real-time data engineering:
- Connects to **Binance WebSocket API** to stream live BTC-USDT trades
- Captures every trade event (price, quantity, timestamp, market side) in real-time
- Stores structured data in CSV format
- Visualizes live trading activity with an interactive **Streamlit dashboard**

### Key Metrics Displayed
- 💰 Latest Bitcoin Price
- 📊 Total Trades Collected
- 📈 Average Price
- 📉 Price Change & Percentage
- 📊 Line chart of price movement over time
- 🔄 Buy vs Sell pressure analysis
- 📋 Trading statistics (volume, range, trade sizes)

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.12** | Core programming language |
| **websocket-client** | Real-time WebSocket connection to Binance |
| **pandas** | Data processing and analysis |
| **Streamlit** | Interactive web dashboard |
| **Binance API** | Live BTC-USDT trade stream |

## 📂 Project Structure

realtime-btc-dashboard/
├── data/ # Generated data files (not committed to Git)
│ └── btc_trades.csv # Collected trade data
├── src/
│ ├── collect_data.py # WebSocket data collector
│ └── dashboard.py # Streamlit dashboard
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
└── README.md # This file

## 🤝 Contributing

This is a portfolio project, but suggestions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

MIT License - feel free to use this project for learning purposes.

## 👤 Author

**[Your Name]**
- GitHub: https://github.com/tymepas
- LinkedIn: https://linkedin.com/in/garvitai/
- Portfolio: https://shorturl.at/1Qdr5

---

⭐ If you find this project helpful, please give it a star on GitHub!
