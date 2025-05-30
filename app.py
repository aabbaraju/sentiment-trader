import gradio as gr
import pandas as pd
from fetch_news import get_news
from sentiment_analysis import get_sentiment
from signal_generator import generate_signal
from portfolio import execute_trade

global last_decision, last_ticker
last_decision = ""
last_ticker = ""

def analyze(ticker):
    global last_decision, last_ticker
    articles = get_news(ticker)

    if not articles:
        return "No articles available.", "No data available."
    
    headlines = [title for title, url in articles]
    urls = [url for title, url in articles]
    sentiments = [get_sentiment(title) for title in headlines]
    decision = generate_signal(sentiments)

    last_decision = decision
    last_ticker = ticker

    markdown = "\n\n".join(
        f"[{title}]({url}) -- Sentiment: {score:.2f}"
        for (title,url), score in zip(articles,sentiments))
    
    return f"Trade Signal: {decision}", markdown

def confirm_trade(action):
    if not last_ticker or action not in ["BUY", "SELL", "HOLD"]:
        return "Invalid trade.", pd.DataFrame()
    
    message, updated_portfolio,  history = execute_trade(last_ticker,action)
    return message, str(updated_portfolio), pd.DataFrame(history)
    
with gr.Blocks() as demo:
    title = gr.HTML("<h1>Sentiment Trader</h1>")
    with gr.Row():
        ticker_input = gr.Textbox(label="Stock Ticker")
        analyze_btn = gr.Button("Analyze")

    output_decision = gr.Textbox(label="Trade Signal")
    article_markdown = gr.Markdown()

    analyze_btn.click(analyze, inputs=ticker_input, outputs=[output_decision, article_markdown])

    with gr.Row():
        buy_btn = gr.Button("Buy")
        sell_btn = gr.Button("Sell")
        hold_btn = gr.Button("Hold")

    trade_status = gr.Textbox(label="Trade Result")
    portfolio_view = gr.Textbox(label="Portfolio Snapshot")
    trade_log = gr.Dataframe(label="Trade History")

    buy_btn.click(confirm_trade, inputs=[gr.Textbox(value="BUY", visible=False)], outputs=[trade_status, portfolio_view, trade_log])
    sell_btn.click(confirm_trade, inputs=[gr.Textbox(value="SELL", visible=False)], outputs=[trade_status, portfolio_view, trade_log])
    hold_btn.click(confirm_trade, inputs=[gr.Textbox(value="HOLD", visible=False)], outputs=[trade_status, portfolio_view, trade_log])

if __name__ == "__main__":
    demo.launch()