def is_palindrome(x : int) -> bool:
    return str(x) == str(x)[::-1]

test_cases = [
    121,
    -121,
    10
]

for i in range(len(test_cases)):
    print(f"Test Case {i}: {is_palindrome(test_cases[i])}")