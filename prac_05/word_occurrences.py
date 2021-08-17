"""
CP1404/CP5632 Practical
Jeffrey Timms
Word occurrences count
"""

words_dictionary = {}
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    try:
        words_dictionary[word] += 1
    except KeyError:
        words_dictionary[word] = 1

words_list = list(words_dictionary.keys())
words_list.sort()

words_max_length = max((len(word) for word in words_list))
for word in words_list:
    print("{:{}} : {}".format(word, words_max_length, words_dictionary[word]))
