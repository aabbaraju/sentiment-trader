import datetime
import yfinance as yf

portfolio = {}
trade_history  = []

def get_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        return stock.info['regularMarketPrice']
    except Exception as e:
        print(f"Error fetching market price for {ticker}: {e}")
        return 0
def execute_trade(ticker, action, qty=1, price = 100.0):
    price = get_price(ticker)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H: %M: %S")

    if action == "BUY":
        portfolio[ticker] = portfolio.get(ticker,0) + qty
    elif action == "SELL":
        portfolio[ticker] = max(portfolio.get(ticker,0)-qty,0)

    trade_history.append({
        "Time": timestamp,
        "Ticker": ticker, 
        "Action": action, 
        "Quantity": qty, 
        "Price": round(price, 2)
    })

    return f"{action} executed for {ticker} at ${round(price,2)}" , portfolio.copy(), trade_history.copy()