def length_of_longest_substring(s : str) -> int:
    subs = []
    mini = ''
    for c in s:
        if c not in mini:
            mini += c
        else:
            subs.append(mini)
            prev_c_index = mini.rfind(c)
            mini = mini[prev_c_index+1:]
            mini += c
    subs.append(mini)
    return len(max(subs, key=len))

test_cases = [
    "abcabcbb",
    "bbbbb",
    "pwwkew"
]

for i in range(len(test_cases)):
    print(f"Test case {i}: {length_of_longest_substring(test_cases[i])}")