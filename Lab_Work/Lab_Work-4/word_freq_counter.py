'''Word Frequency Counter
Given a file article.txt,
Count frequency of each word (ignore case and punctuation).'''
import string
# Open the file in read mode
with open('article.txt', 'r') as file:
    # Read the contents of the file
    text = file.read().lower()  # Convert to lowercase for case insensitivity
    # Remove punctuation from the text
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split the text into words
    words = text.split()
    # Create a dictionary to count word frequencies
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
# Print the word frequencies
for word, freq in word_freq.items():
    print(f"{word}: {freq}")