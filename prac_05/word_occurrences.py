"""
CP1404/CP5632 Practical
Jeffrey Timms
Count occurrences of words in a string
"""

words_dictionary = {}
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    try:
        words_dictionary[word] += 1
    except KeyError:
        words_dictionary[word] = 1

