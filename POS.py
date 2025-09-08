#Write a Python Program to POS (Parts of Speech) tagging for the give sentence using NLTK.

import nltk

# Download required NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input sentence
sentence = input("Enter a sentence: ")

# Tokenize the sentence into words
words = nltk.word_tokenize(sentence)

# Perform POS tagging
pos_tags = nltk.pos_tag(words)

# Display the result
print("POS Tags:")
print(pos_tags)
