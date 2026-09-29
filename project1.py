
import pandas as pd
import numpy as np
import yfinance as yf

tickers = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META",
    "NVDA", "JPM", "XOM", "JNJ", "PG"
]

prices = yf.download(tickers, start='2015-01-01', end = '2026-01-01', auto_adjust=True)

close = prices["Close"]

print(close.head())