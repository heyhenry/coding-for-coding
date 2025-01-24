import re
import string

def detect_palindrome_words(sentence : str): 
    # check cases with only spaces or zero string length
    if len(sentence) < 1 or sentence == " " * len(sentence):
        return []
    
    # remove special characters (punctuation) from the given sentence
    puncs = r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    puncs = re.escape(puncs)
    cleaned_sentence = re.sub(f"[{puncs}]", "", sentence)

    # turn sentence into a list of words
    words = cleaned_sentence.split()

    # algorithm to determine whether each word is a palindrome 
    results = []
    for word in words:
        if word[::-1].lower() == word.lower():
            results.append(True)
        else:
            results.append(False)
    return results

# run test cases
test_cases = [
    "madam racecar apple",         # Expected: [True, True, False]
    "level radar civic",           # Expected: [True, True, True]
    "hello world",                 # Expected: [False, False]
    "",                            # Expected: [] 
    " ",                           # Expected: [] 
    "a",                           # Expected: [True]
    "Aba",                         # Expected: [True] 
    "Step on no pets",             # Expected: [False, False, False, False]
    "12321 45654 78987",           # Expected: [True, True, True]
    "Racecar Madam Civic",         # Expected: [True, True, True]
    "a" * 1000 + "b",              # Expected: [False]
    "a" * 1000,                    # Expected: [True]   
]

for i in range(len(test_cases)):
    print(f"Test {i} Result: {detect_palindrome_words(test_cases[i])}\n")