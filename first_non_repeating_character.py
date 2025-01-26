def first_non_repeating_character(s : str):
    # turn all characters into lowercase
    s = s.lower()

    # check if the string is empty or only contains white spaces
    if len(s) == 0 or len(s)*" " == s:
        return None
    
    # tally and store each character and it's frequency
    chars = {}
    for c in s:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    
    # iterate through the characters and their frequency values
    non_repeat = None
    for key, val in chars.items():
        # update the non_repeat value with the lowest frequency character
        if non_repeat is None:
            non_repeat = (key, val)
        elif val < non_repeat[1]:
            non_repeat = (key, val)
        # if a character with a frequency of 1 is found, immediately end,
        # this is because it would be the first non-repeating character found
        if non_repeat[1] == 1:
            return non_repeat[0]
    
    # if the function didn't end during the dictionary iteration
    # it is safe to assume that there were no non-repeating characters found
    return None

# test cases
test_cases = [
    "aAbBcCdDe",
    "aabbcc",
    "abcABC",
    "",
    "xxyz",
    " ",
    "aAaBbCcDdEeFfG",
    "helloHELLOworld"
]

# execute test cases
for i in range(len(test_cases)):
    print(f"Test case {i}: {first_non_repeating_character(test_cases[i])}")