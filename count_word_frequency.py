import string
import re

def count_word_frequency(sentence : str):
    # remove all punctuations in sentence
    punctuation = string.punctuation
    sentence = re.sub(f"[{punctuation}]", "", sentence)
    # change all letters in sentence to lower case
    sentence = sentence.lower()
    # create a list of words found sentence
    words = sentence.split()
    # initialize dictionary to count word frequency
    count_dict = {}
    # check for an empty sentence
    if len(words) < 1:
        return count_dict
    # algorithm to count and store data of words and their frequency found in the given sentence
    for w in words:
        if w not in count_dict:
            count_dict[w] = 1
        else:
            count_dict[w] += 1
    # return the dictionary that contains word frequency counts
    return count_dict
    
test_cases = [
    "Hello world! Hello everyone.", #{"hello": 2, "world": 1, "everyone": 1}
    "Count, count, and COUNT again!", # {"count": 3, "and": 1, "again": 1}
    "  ", # {}
    "A journey of a thousand miles begins with a single step.", # {"a": 3, "journey": 1, "of": 1, "thousand": 1, "miles": 1, "begins": 1, "with": 1, "single": 1, "step": 1}
]

for i in range(len(test_cases)):
    print(f"Test Case {i}: {count_word_frequency(test_cases[i])}")