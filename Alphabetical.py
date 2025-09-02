#Write a Python Program to sort the sentence in alphabetical order.

# Input sentence
sentence = "Python is a powerful and easy to learn language"

# Split into words
words = sentence.split()

# Sort words alphabetically
words.sort()

# Join back into a sentence
sorted_sentence = " ".join(words)

print("Original Sentence:", sentence)
print("Sorted Sentence:", sorted_sentence)
