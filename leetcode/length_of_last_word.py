def length_of_last_word(s : str) -> int:
    lst = s.split()
    return len(lst[-1])

test_cases = [
    "Hello World",
    "   fly me   to   the moon  ",
    "luffy is still joyboy"
]

for i in range(len(test_cases)):
    print(f"Test Case {i}: {length_of_last_word(test_cases[i])}")