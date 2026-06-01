# 📈 MarketPulse: Real-Time Stock Market Analytics Dashboard

## Overview

MarketPulse is a financial analytics project designed to analyze and visualize stock market performance using historical market data. The system leverages Python-based data analysis techniques to compare stock performance, evaluate investment risk, identify market trends, and generate actionable insights through data visualization.

By integrating financial data from Yahoo Finance, the project enables investors and analysts to monitor stock behavior, compare multiple assets, assess volatility, and understand long-term market movements using quantitative techniques.

---

## Objectives

* Retrieve historical stock market data using Yahoo Finance.
* Compare the performance of multiple stocks over a selected time period.
* Analyze daily returns and market behavior.
* Measure stock volatility as a risk indicator.
* Identify trends using moving averages.
* Generate visual insights through financial data visualization.
* Support data-driven investment analysis and decision-making.

---

## Dataset

The project utilizes financial market data obtained through the Yahoo Finance API via the yFinance library.

Data includes:

* Historical Stock Prices
* Closing Prices
* Daily Returns
* Market Volatility Metrics
* Moving Average Trends

Stocks analyzed in the project:

* Apple (AAPL)
* Microsoft (MSFT)
* Google (GOOGL)

---

## Technologies Used

* **Python**
* **Pandas**
* **Matplotlib**
* **yFinance**

---

## Project Workflow

### 1. Data Collection

Historical stock data is downloaded directly from Yahoo Finance using the yFinance library.

The system retrieves:

* Daily Closing Prices
* Historical Trading Data
* Market Performance Information

---

### 2. Data Normalization

Stock prices are normalized to allow fair comparison between companies with different share prices.

This enables performance analysis on a common scale.

---

### 3. Performance Analysis

Normalized stock prices are compared over time to evaluate relative growth and market performance.

Key metrics include:

* Price Growth
* Relative Performance
* Historical Trends

---

### 4. Daily Return Analysis

Daily percentage returns are calculated to measure short-term market fluctuations.

This analysis helps identify:

* Price Momentum
* Daily Market Movement
* Return Variability

---

### 5. Risk Assessment

Volatility is calculated using the standard deviation of daily returns.

Higher volatility indicates:

* Greater market uncertainty
* Increased investment risk

Lower volatility indicates:

* More stable stock performance

---

### 6. Moving Average Analysis

A 50-day Moving Average (MA) is calculated to smooth short-term fluctuations and reveal long-term trends.

Moving averages help:

* Identify trend direction
* Detect market momentum
* Support investment decision-making

---

## Key Features

* Historical Stock Market Analysis
* Multi-Stock Performance Comparison
* Daily Return Analysis
* Volatility-Based Risk Assessment
* 50-Day Moving Average Analysis
* Financial Data Visualization
* Market Trend Identification
* Investment Insight Generation

---

## Visualizations

The project generates:

### Stock Performance Comparison

Compares normalized stock prices across multiple companies.

### Daily Return Analysis

Visualizes day-to-day stock return fluctuations.

### Volatility Assessment

Measures and compares stock risk levels.

### Moving Average Analysis

Displays stock prices alongside 50-day moving averages.

These visualizations provide insights into both performance and risk characteristics of different assets.

---

## Repository Structure

```text
MarketPulse/
│
├── FinancialDataAnalysis.py
└── README.md
```

---

## Installation & Setup

### Prerequisites

* Python 3.9+
* pip

### Clone the Repository

```bash
git clone https://github.com/janhavee-s/MarketPulse-Real-Time-Stock-Market-Analytics.git
cd MarketPulse-Real-Time-Stock-Market-Analytics
```

### Run the Project

From the project root directory:

```bash
python FinancialDataAnalysis.py
```

---

## Key Insights

* Stock normalization enables meaningful cross-company performance comparison.
* Daily returns reveal short-term market behavior and fluctuations.
* Volatility provides a quantitative measure of investment risk.
* Moving averages highlight long-term market trends and momentum.
* Historical analysis supports informed investment decisions.

---

## Skills Demonstrated

* Financial Data Analysis
* Time Series Analysis
* Data Visualization
* Quantitative Finance
* Python Programming
* Statistical Analysis
* Risk Assessment
* Market Trend Analysis
* API-Based Data Collection

---

## Future Enhancements

* Interactive Dashboard using Streamlit
* Portfolio Performance Analysis
* Technical Indicators (RSI, MACD, Bollinger Bands)
* Stock Price Forecasting with Machine Learning
* Real-Time Market Monitoring
* Portfolio Risk Optimization
* Automated Investment Insights

---

## Author

**Janhavee Singh**

B.Tech Computer Science | Artificial Intelligence | Machine Learning | Data Analytics

MarketPulse demonstrates practical expertise in financial data analysis, market trend evaluation, risk assessment, and data visualization using real-world stock market data.
