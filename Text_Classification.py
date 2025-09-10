#Write a Python Program to for Text Classification for the give sentence using NLTK.

import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Preprocessing function to extract features
def extract_features(sentence):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(sentence.lower())
    words = [w for w in words if w not in stop_words and w not in string.punctuation]
    features = {}
    for word in words:
        features[word] = True
    return features

# Training dataset
training_data = [
    ("Hello, how are you?", "greeting"),
    ("Good morning!", "greeting"),
    ("Hey there!", "greeting"),
    ("Goodbye, see you later!", "goodbye"),
    ("Bye bye!", "goodbye"),
    ("See you soon!", "goodbye")
]

# Convert training data into feature sets
train_set = [(extract_features(sentence), category) for (sentence, category) in training_data]

# Train the Naive Bayes classifier
classifier = NaiveBayesClassifier.train(train_set)

# Input sentence to classify
input_sentence = input("Enter a sentence to classify: ")

# Extract features from input sentence
features = extract_features(input_sentence)

# Predict the category
predicted_category = classifier.classify(features)

print(f"Predicted Category: {predicted_category}")

# Show the most informative features
classifier.show_most_informative_features()
