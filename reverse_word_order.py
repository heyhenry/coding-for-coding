def reverse_word_order(s : str):
    s = s.split()
    return " ".join(s[::-1])

# run test cases
test_cases = [
    "Hello World",
    "The quick brown fox jumps over the lazy dog.",
    "",
    " ",
    " Hello World ",
    "Python is fun!",
    " This is a test.",
    "A single_word",
    "One-word",
    "Hello, World!",
    "Multiple spaces and punctuation, here!",
    "1 2 3 4 5"
]

for words in range(len(test_cases)):
    print(f"Test {words}: \"{reverse_word_order(test_cases[words])}\"")
