# SentimentTrader

An AI-Driven Stock Trading Strategy Using Real-Time News & Social Sentiment

---

## Project Overview

SentimentTrader is an interactive trading assistant that analyzes real-time financial news to generate trading signals (Buy / Sell / Hold) based on natural language sentiment. Users can simulate trades, track a portfolio, and visualize sentiment trends across public stocks using a clean, browser-based UI.

---

## Features

- Live news sentiment analysis via NewsAPI and VADER
- Trade signal generation (Buy / Hold / Sell)
- Simulated trade execution and portfolio tracking
- Real-time stock prices from Yahoo Finance (`yfinance`)
- Modular Python backend designed for future RL or brokerage API integration

---
## Getting Started

### Installation

```bash
git clone https://github.com/aabbaraju/sentiment-trader.git
cd sentiment-trader
pip install -r requirements.txt
python app.py
