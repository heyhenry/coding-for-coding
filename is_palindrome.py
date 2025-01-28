def is_palindrome(num : int) -> bool:
    original_num = num
    reverse_num = 0
    while num > 0:
        # find the last digit in num
        tail = num % 10
        # remove the last digit in num
        num //= 10
        # shift all digits in reverse_num 1 position to the left and add as a '0' placeholder
        reverse_num *= 10
        # add the tail digit to the end of the reverse_num
        reverse_num += tail

    # check if the original_num equals the reverse_num
    return original_num == reverse_num

test_cases = [
    121,
    -121,
    10
]

for i in range(len(test_cases)):
    print(f"Test Case {i}: {is_palindrome(test_cases[i])}")