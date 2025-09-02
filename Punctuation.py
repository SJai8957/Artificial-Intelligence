#Write a Python Program to remove punctuations from the given string.

import string

# Input string
text = "Hello!!!, he said --- and went."

# Remove punctuations
result = "".join(char for char in text if char not in string.punctuation)

print("Original String:", text)
print("Without Punctuation:", result)
