def is_palindrome(x : int) -> bool:
    original_num = x
    rev_num = 0
    if x <= 0:
        return False
    while x != 0:
        # get the tail digit
        tail = x % 10
        # push current digits in rev_num 1 position to the left
        rev_num *= 10
        # add the tail to the end of the rev_num
        rev_num += tail
        # remove the tail from the x
        x //= 10
    return original_num == rev_num

test_cases = [
    121,
    -121,
    10
]

for i in range(len(test_cases)):
    print(is_palindrome(test_cases[i]))