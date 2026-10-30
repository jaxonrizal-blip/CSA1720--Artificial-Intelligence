from textblob import TextBlob

# Get user input
text = input("Enter a sentence: ")

# Perform sentiment analysis
blob = TextBlob(text)
polarity = blob.sentiment.polarity

print("Sentiment Polarity:", polarity)

if polarity > 0:
    print("Sentiment: Positive")
elif polarity < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
