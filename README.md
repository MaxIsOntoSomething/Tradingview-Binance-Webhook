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

## License

This project is licensed under the MIT License.

## Contact

For any questions or support, contact me on Discord:

![Discord Logo](https://upload.wikimedia.org/wikipedia/commons/9/98/Discord_logo.svg) maskiplays