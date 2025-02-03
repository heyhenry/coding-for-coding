import re
import string

def find_longest_word(sentence : str):
    punctuation = string.punctuation
    punctuation = re.escape(punctuation)
    clean_sentence = re.sub(f"[{punctuation}]", "", sentence)
    words = clean_sentence.split()
    result = ''
    for word in words:
        if len(word) > len(result):
            result = word
    return result

# run test cases
test_cases = [
    "asdfj!,asdfk^,>!!sodkf",
    "The quick brown fox jumped over the lazy dog.",
    "Hello, world!",
    "A journey of a thousand miles begins with a single step.",
    "",
    " "
]

for i in range(len(test_cases)):
    print(f"Test Case {i} Result: \"{find_longest_word(test_cases[i])}\"")