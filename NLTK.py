#Write a Python Program to remove stop words for a given passage from a text file using NLTK.

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

# Instead of reading from a file, use a passage directly
passage = "This is a sample passage. It contains some stop words that should be removed using NLTK."

# Tokenize
words = word_tokenize(passage)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Join words
filtered_passage = " ".join(filtered_words)

print("Original Passage:\n", passage)
print("\nFiltered Passage:\n", filtered_passage)

