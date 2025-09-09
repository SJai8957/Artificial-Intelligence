#Write a Python Program to implement Lemmatization using NLTK.

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Function to map NLTK POS tags to WordNet POS tags
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default to noun if not recognized

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Input sentence
sentence = "The striped bats are hanging on their feet and are not flying."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Get POS tags
pos_tags = nltk.pos_tag(tokens)

# Lemmatize each token with its POS tag
lemmatized_words = []
for word, tag in pos_tags:
    wordnet_pos = get_wordnet_pos(tag)
    lemmatized_word = lemmatizer.lemmatize(word, pos=wordnet_pos)
    lemmatized_words.append(lemmatized_word)

# Print the results
print("Original Sentence:")
print(sentence)
print("\nLemmatized Sentence:")
print(' '.join(lemmatized_words))
