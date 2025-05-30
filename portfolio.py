import datetime

portfolio = {}
trade_history  = []

def execute_trade(ticker, action, qty=1, price = 100.0):
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
        "Price": price
    })

    return f"{action} executed for {ticker}", portfolio.copy(), trade_history.copy()