# Binance Trading Bot

This bot executes trades on Binance based on signals sent via TradingView alerts. It uses a specified percentage of your account balance to place market buy orders and can operate on both the Binance Testnet and live account.

## Features

- Executes trades based on signals from TradingView alerts.
- Uses the current market price for immediate execution.
- Places a market buy order at the current market price.
- Option to use email alerts instead of webhook alerts.
- Configurable trade percentage and API keys.

## Setup and Configuration

1. **Install required packages**:
   ```sh
   pip install -r requirements.txt
   ```

2. **Configure API keys and settings**:
   - Update `config.json` with your Binance API keys and desired settings:
     ```json
     {
         "BINANCE_API_KEY": "your_binance_api_key",
         "BINANCE_API_SECRET": "your_binance_api_secret",
         "USE_TESTNET": true,
         "TRADE_PERCENTAGE": 0.1,
         "WEBHOOK_PORT": 5000,
         "TESTNET_API_KEY": "your_testnet_api_key",
         "TESTNET_API_SECRET": "your_testnet_api_secret",
         "USE_EMAIL": true  // Set to true to use email alerts, false to use webhook
     }
     ```

3. **Set up TradingView alerts**:
   - Create an alert in TradingView with the webhook URL or email address provided by your email-to-webhook service.
   - The alert message should be a JSON object containing `symbol`, e.g.:
     ```json
     {
       "symbol": "BTCUSDT"
     }
     ```

4. **Run the bot**:
   ```sh
   python bot.py
   ```

## Disclaimer

This bot is provided as-is and is intended for educational purposes only. Use it at your own risk. The author is not financially accountable for any losses incurred while using this bot.

## License

This project is licensed under the MIT License.

## Contact

For any questions or support, contact me on Discord:

![Discord Logo](https://camo.githubusercontent.com/466cd9b81abcedb1db7d8f6fcd75148b6728e1eb8e443ab320928e924b93a4e0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446973636f72642d3732383944413f7374796c653d666f722d7468652d6261646765266c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465) maskiplays