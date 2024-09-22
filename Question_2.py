#Perform descriptive statistics on the text dataset, detect stopwords, visualize the most common non-stopwords using a bar chart, and create a word cloud for overall word distribution.

import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import string
from wordcloud import WordCloud
from collections import Counter
import re

# Download NLTK stopwords
nltk.download("stopwords")

# Load the dataset
df = pd.read_csv(r"H:\NLPCourse\Assignment #3\ecommerce_dataset.txt", sep='\t', header=None, names=['sentiment', 'text'], encoding='utf-16')

# Handle missing data
df.dropna(subset=['text'], inplace=True)

# Print total comments and average/median length
print("Total Comments:", len(df))
print("Average length of comments:", df["text"].apply(len).mean())
print("Median length of comments:", df["text"].apply(len).median())

# Display stopwords
stop_words = set(stopwords.words("english"))
print("Stopwords:", stop_words)

# Set of punctuation
punctuation = set(string.punctuation)
print("Punctuation:", punctuation)

# Text cleaning function
def clean_text_with_re(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)  # Remove numbers
    tokens = [word.lower() for word in text.split() if word.lower() not in stop_words]
    return ' '.join(tokens)

# Clean the text
df['clean_text'] = df['text'].apply(clean_text_with_re)

# Find the most common words in the cleaned text
words = ' '.join(df['clean_text']).split()
common_word = Counter(words).most_common(10)
print("Most common words:", common_word)

# Calculate total positive and negative comments
total_positive = df[df['sentiment'] == 1].shape[0]
total_negative = df[df['sentiment'] == 0].shape[0]

print("Total Positive Comments:", total_positive)
print("Total Negative Comments:", total_negative)

# Visualize sentiment distribution
sentiment_counts = df['sentiment'].value_counts()
plt.figure(figsize=(8, 8))
plt.bar(sentiment_counts.index, sentiment_counts.values, color=['blue', 'skyblue'])
plt.title("Sentiment Distribution")
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

# WordCloud generation
wordcloud = WordCloud(width=800, height=400, background_color="black", colormap="Blues").generate(' '.join(words))

# Display WordCloud
plt.figure(figsize=(8, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
