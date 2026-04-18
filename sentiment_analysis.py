import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import matplotlib.pyplot as plt

# Download NLTK data (only first time)
nltk.download('vader_lexicon')

# Load dataset (make sure this file exists inside dataset/)
data = pd.read_csv('dataset/training.1600000.processed.noemoticon.csv', encoding='latin-1')
data.columns = ['target', 'ids', 'date', 'flag', 'user', 'text']

# Take only a small sample for testing (1000 rows)
sample = data.head(1000)

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Analyze sentiment for each tweet
sample['compound'] = sample['text'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
sample['sentiment'] = sample['compound'].apply(
    lambda c: 'positive' if c > 0 else ('negative' if c < 0 else 'neutral')
)

# Print the first few results
print(sample[['text', 'sentiment']].head())

# Plot sentiment counts
sample['sentiment'].value_counts().plot(kind='bar', title='Sentiment Distribution')
plt.show()
