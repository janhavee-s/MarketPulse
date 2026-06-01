#STOCK COMPARISON AND RISK ANALYSIS PROJECT MINI PROJECT

#DESCRIPTION: this mini project analyzes and compares the performance of multiple stocks using historical market data for the year 2023-2024.
#stock price data is collected using financial libraries aka "yfinance".
#closing prices are normalized so that different stocks can be compared fairly on the same scale. 
#daily returns are calculated to understand how stock prices change in day-to-day life.
#volatility is computed using standard deviation to measure the risk associated with each stock.
#moving averages are used to identify price trends over time (50-days in this case).
#graphs are plotted for visualizing mathematical data to compare stock performance and risk.
#this project helps investors understand which stock performs better and which comes with more risk.

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

#define stocks and period
stocks = ["AAPL", "MSFT", "GOOGL"]
start_date = "2023-01-01"
end_date = "2024-01-01"

#download data
data = yf.download(stocks, start=start_date, end=end_date)

#closing prices
close_price = data["Close"]

#intial information about stocks
print("closing price data:")
print(close_price.head())
print("\ncolumns:")
print(close_price.columns)

#use normalization
normalized_price = close_price / close_price.iloc[0]

#visualization and plotting of graphs
plt.figure(figsize=(12, 8))

for stock in stocks:
    plt.plot(normalized_price.index,
             normalized_price[stock],
             label=stock)

plt.title("stock performance comparison (2023–2024)")
plt.xlabel("date")
plt.ylabel("normalized price")
plt.legend()
plt.grid(True)
plt.show()

#daily stock prices 
daily_returns = close_price.pct_change()

print("\ndaily returns:")
print(daily_returns.head())

#graph of daily stock prices
plt.figure(figsize=(12, 8))

for stock in stocks:
    plt.plot(daily_returns.index,
             daily_returns[stock],
             label=stock,
             alpha=0.7)

plt.title("daily return comparison")
plt.xlabel("date")
plt.ylabel("daily return")
plt.legend()
plt.grid(True)
plt.show()

#market movement of stocks aka volatility
volatility = daily_returns.std()

print("\nstock volatility (risk measure):")
print(volatility)

#volatility average for last 50 days
ma_50 = close_price.rolling(window=50).mean()

plt.figure(figsize=(12, 8))

for stock in stocks:
    plt.plot(close_price.index,
             close_price[stock],
             label=f"{stock} Price",
             alpha=0.5)
    plt.plot(ma_50.index,
             ma_50[stock],
             linestyle="--",
             label=f"{stock} 50-Day MA")

plt.title("50-day moving average comparison")
plt.xlabel("date")
plt.ylabel("price (USD)")
plt.legend()
plt.grid(True)
plt.show()

#statistical summary
print("\nstatistical summary of closing prices:")
print(close_price.describe())

#final conclusion of mini project
print("\nPROJECT CONCLUSION")
print("\nmini project executed successfully")
print("\nthis analysis helps compare stock performance and risk of three companies:\n APPLE, MICROSOFT, GOOGLE.")
