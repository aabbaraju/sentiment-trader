import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

def get_news(ticker):
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={ticker}&"
        f"language=en&"
        f"sortBy=publishedAt&"
        f"apiKey={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()

    if "articles" not in data:
        return []
    return [(article["title"], article["url"]) for article in data["articles"][:5]]