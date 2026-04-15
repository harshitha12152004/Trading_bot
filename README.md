🚀 Binance Futures Trading Bot (Testnet)

📌 Overview

This project is a Python-based CLI trading bot that interacts with the Binance Futures Testnet (USDT-M). It allows users to place Market and Limit orders, along with advanced features like Leverage, Stop Loss, and Take Profit.
The application is designed with a modular structure, proper logging, and error handling, making it suitable for real-world usage and interviews.

🛠️ Features

✅ Place Market Orders

✅ Place Limit Orders

✅ Supports BUY / SELL

✅ Set Leverage

✅ Add Stop Loss

✅ Add Take Profit

✅ CLI-based input using Typer

✅ Logging of API requests and responses

✅ Exception handling for errors

🧱 Project Structure

trading_bot/ │── client.py # Binance API interaction │── cli.py # Command-line interface │── config.py # API configuration │── logger.py # Logging setup │── .env # API keys (not pushed to GitHub) │── requirements.txt │── README.md 

⚙️ Setup Instructions

1️⃣ Clone the Repository

git clone <your-repo-link> cd trading_bot 

2️⃣ Create Virtual Environment

python -m venv venv venv\Scripts\activate # Windows 

3️⃣ Install Dependencies

pip install -r requirements.txt 

🔐 API Setup

Go to Binance Futures Testnet

Create API Key

Enable Futures Trading

Create a .env file:
API_KEY=your_api_key_here API_SECRET=your_secret_here 

▶️ Usage

🔹 Market Order

python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001 

🔹 Limit Order

python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 60000 

🔹 With Leverage + Stop Loss + Take Profit

python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001 --leverage 10 --stop-loss 60000 --take-profit 70000 

📊 Example Output

--- Order Request --- BTCUSDT BUY MARKET 0.001 --- Response --- Order ID: 123456 Status: FILLED Executed Qty: 0.001 ✅ Success 

📝 Logging

Logs are stored in:
trading_bot.log 
Includes:

API requests

Responses

Errors

⚠️ Error Handling

The bot handles:

Invalid inputs

API errors

Network issues

Insufficient margin

🔒 Security

API keys are stored using environment variables

.env file is ignored using .gitignore

No sensitive data is exposed

🚀 Future Improvements

📡 WebSocket for live price tracking

🧠 Automated trading strategies

🗄️ Database integration (PostgreSQL/MySQL)

🌐 React-based frontend dashboard

🎯 Interview Explanation

“I developed a CLI-based trading bot using Python that integrates with Binance Futures Testnet. It supports order execution with leverage, stop-loss, and take-profit, and follows a modular architecture with proper logging and error handling.”

📜 License

This project is for educational and demonstration purposes only.
