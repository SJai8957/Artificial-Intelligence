#Write a Python Program to implement stemming for a given sentence using NLTK.

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download necessary resources
nltk.download('punkt')

# Create a PorterStemmer object
stemmer = PorterStemmer()

# Input sentence
sentence = input("Enter a sentence: ")

# Tokenize the sentence
words = word_tokenize(sentence)

# Apply stemming to each word
stemmed_words = [stemmer.stem(word) for word in words]

# Print the result
print("Original Sentence:")
print(sentence)
print("\nStemmed Words:")
print(stemmed_words)
