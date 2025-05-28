import gradio as gr
import pandas as pd
from fetch_news import get_news
from sentiment_analysis import get_sentiment
from signal_generator import generate_signal

def analyze(ticker):
    articles = get_news(ticker)

    if not articles:
        return "No articles available.", "No data available."
    
    headlines = [title for title, url in articles]
    urls = [url for title, url in articles]
    sentiments = [get_sentiment(title) for title in headlines]
    decision = generate_signal(sentiments)

    markdown = "\n\n".join(
        f"[{title}]({url}) -- Sentiment: {score:.2f}"
        for (title,url), score in zip(articles,sentiments))
    return f"Trade Signal: {decision}", markdown
demo = gr.Interface(
    fn = analyze,
    inputs = "text",
    outputs=[
        gr.Textbox(label="Trade Decision"),
        gr.Markdown(label="Articles + Sentiment")
    ],
    title="SentimentTrader",
    description ="Enter a stock ticker to analyze news sentiment and get a trade signal."
)

if __name__ == "__main__":
    demo.launch()