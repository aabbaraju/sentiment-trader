from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer

def getSentiment(text):
    scores = analyzer.polarity_scores(text)
    return scores['compound']