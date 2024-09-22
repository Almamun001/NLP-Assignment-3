# How can I add custom stopwords to an existing list of stopwords in Python?

import nltk
from nltk.corpus import stopwords

# Download the stopwords if you haven't already
nltk.download('stopwords')

# Load the existing stopwords in English
stop_words = set(stopwords.words('english'))

# Define your custom stopwords
custom_stopwords = {'Innovative_Solution_BD', 'NLP_Course', 'Batch_3'}

# Add the custom stopwords to the existing stopwords set
stop_words.update(custom_stopwords)

# Now, `stop_words` contains both default and custom stopwords
print(stop_words)
