import re
import string

def detect_palindrome_words(sentence : str):
    results = []
    if len(sentence) < 1 or sentence == " " * len(sentence):
        results.append(False)
        return results
    puncs = r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    puncs = re.escape(puncs)
    cleaned_sentence = re.sub(f"[{puncs}]", "", sentence)
    words = cleaned_sentence.split(" ")
    rev_words = [w[::-1] for w in words]
    for w in range(len(words)):
        if rev_words[w].lower() == words[w].lower():
            results.append(True)
        else:
            results.append(False)
    return results

test_cases = [
    "madam racecar apple",         # Expected: [True, True, False]
    "level radar civic",           # Expected: [True, True, True]
    "hello world",                 # Expected: [False, False]
    "",                            # Expected: [] 
    " ",                           # Expected: [] 
    "a",                           # Expected: [True]
    "Aba",                         # Expected: [True] False
    "Step on no pets",             # Expected: [False, False, False]
    "12321 45654 78987",           # Expected: [True, True, True]
    "Racecar Madam Civic",         # Expected: [True, True, True]
    "a" * 1000 + "b",              # Expected: [False]  # 1000 'a's followed by 'b'
    "a" * 1000,                    # Expected: [True]   # 1000 'a's
]

for i in range(len(test_cases)):
    print(f"Test {i} Result: {detect_palindrome_words(test_cases[i])}\n")