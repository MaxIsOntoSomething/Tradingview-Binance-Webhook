import time
import json
import requests
from flask import Flask, request
from binance.client import Client
from binance.enums import *
# import schedule

import os
import json
import re

from ..scripts.logger import log_trade  # Use relative import for logger.py

# Load configuration from config.json
config_path = os.path.join(os.path.dirname(__file__), '../config/config.json')
with open(config_path) as config_file:
    config = json.load(config_file)

def save_config():
    with open(config_path, 'w') as config_file:
        json.dump(config, config_file, indent=4)

def setup_config():
    if not config.get("BINANCE_API_KEY"):
        config["BINANCE_API_KEY"] = input("Enter your Binance API Key: ").strip()
    if not config.get("BINANCE_API_SECRET"):
        config["BINANCE_API_SECRET"] = input("Enter your Binance API Secret: ").strip()
    if not config.get("TESTNET_API_KEY"):
        config["TESTNET_API_KEY"] = input("Enter your Binance Testnet API Key: ").strip()
    if not config.get("TESTNET_API_SECRET"):
        config["TESTNET_API_SECRET"] = input("Enter your Binance Testnet API Secret: ").strip()
    save_config()

setup_config()

app = Flask(__name__)

# Initialize Binance client
if config["USE_TESTNET"]:
    client = Client(config["TESTNET_API_KEY"], config["TESTNET_API_SECRET"])
    client.API_URL = 'https://testnet.binance.vision/api'
else:
    client = Client(config["BINANCE_API_KEY"], config["BINANCE_API_SECRET"])

def get_balance(asset):
    balance = client.get_asset_balance(asset=asset)
    return float(balance['free'])

def place_market_buy_order(symbol, quantity):
    order = client.order_market_buy(
        symbol=symbol,
        quantity=quantity
    )
    log_trade(order)  # Log the trade
    return order

@app.route('/webhook', methods=['POST'])
def webhook():
    data = json.loads(request.data)
    symbol = data['symbol']
    
    balance = get_balance('USDT')
    current_price = get_current_price(symbol)
    trade_amount = balance * config["TRADE_PERCENTAGE"]
    quantity = trade_amount / current_price
    
    order = place_market_buy_order(symbol, quantity)
    return {
        "message": "Order placed",
        "order": order
    }

@app.route('/email-webhook', methods=['POST'])
def email_webhook():
    email_body = request.form['body-plain']
    match = re.search(r'\{.*\}', email_body)
    if match:
        email_data = json.loads(match.group(0))
        symbol = email_data['symbol']
        
        balance = get_balance('USDT')
        current_price = get_current_price(symbol)
        trade_amount = balance * config["TRADE_PERCENTAGE"]
        quantity = trade_amount / current_price
        
        order = place_market_buy_order(symbol, quantity)
        return {
            "message": "Order placed",
            "order": order
        }
    else:
        return {
            "message": "Invalid email format"
        }, 400

def get_current_price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])

if __name__ == '__main__':
    use_testnet = input("Use Binance Testnet? (yes/no): ").strip().lower() == 'yes'
    config["USE_TESTNET"] = use_testnet
    
    trade_percentage = float(input("Enter trade percentage (e.g., 0.1 for 10%): ").strip())
    config["TRADE_PERCENTAGE"] = trade_percentage
    
    btc_price = get_current_price('BTCUSDT')
    eth_price = get_current_price('ETHUSDT')
    sol_price = get_current_price('SOLUSDT')
    
    print(f"Current BTCUSDT price: {btc_price}")
    print(f"Current ETHUSDT price: {eth_price}")
    print(f"Current SOLUSDT price: {sol_price}")
    
    # schedule_daily_report()  # Remove the daily report scheduling
    
    if config["USE_EMAIL"]:
        app.add_url_rule('/email-webhook', 'email_webhook', email_webhook, methods=['POST'])
    else:
        app.add_url_rule('/webhook', 'webhook', webhook, methods=['POST'])
    
    app.run(port=config["WEBHOOK_PORT"])
    
    while True:
        print("Bot is active and listening for signals...")
        time.sleep(60)
