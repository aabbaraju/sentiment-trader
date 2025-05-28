import gradio as gr
from fetch_news import get_news
from sentiment_analysis import get_sentiment
from signal_generator import generate_signal

def analyze(ticker):
    news = get_news(ticker)
    sentiments = [get_sentiment(article) for article in news]
    decision = generate_signal(sentiments)
    return f"Trade Signal: {decision}", list(zip(news, sentiments))
demo = gr.Interface(
    fn = analyze,
    inputs = "text",
    outputs=["text","dataframe"],
    title="SentimentTrader",
    description ="Enter a stock ticker to analyze news sentiment and get a trade signal."
)

if __name__ == "__main__":
    demo.launch()