import logging
from datetime import datetime, timedelta
import pandas as pd
# import schedule
import time

# Configure logging
logging.basicConfig(filename='../logs/trades.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Function to log a trade
def log_trade(trade):
    logging.info(f"Trade executed: {trade}")

# Function to calculate average accumulation price
def calculate_average_price():
    try:
        df = pd.read_csv('../logs/trades.log', sep=' - ', header=None, names=['timestamp', 'message'])
        trades = df['message'].str.extract(r'Trade executed: (.*)')
        prices = trades[0].str.extract(r'price: (\d+\.\d+)').astype(float)
        average_price = prices.mean()[0]
        logging.info(f"Average accumulation price: {average_price}")
    except Exception as e:
        logging.error(f"Error calculating average price: {e}")

if __name__ == "__main__":
    # schedule_daily_report()  # Remove the daily report scheduling
    pass
