def generate_signal(sentiment_scores):
    avg_score = sum(sentiment_scores) / len(sentiment_scores)
    if avg_score > 0.2:
        return "BUY"
    elif avg_score < -0.2:
        return "SELL"
    else:
        return "HOLD"