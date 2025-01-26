# success achieved in the leetcode sandbox as well.

def length_of_longest_substring(s : str) -> int:
    subs = []
    mini = ''
    for c in s:
        if c not in mini:
            # appending characters while there arent duplicates
            mini += c
        else:
            subs.append(mini)
            # find the last occurence of the c character prior to this iteration
            prev_c_index = mini.rfind(c)
            # update the mini's string to start from the character after the 
            # last occurence of the c character prior to this iteration
            mini = mini[prev_c_index+1:]
            mini += c
    # ensure to include the last mini entry to the list
    subs.append(mini)
    # determine the longest length found via the elements gathered in the subs list
    return len(max(subs, key=len))

# test cases
test_cases = [
    "abcabcbb",
    "bbbbb",
    "pwwkew"
]

# test case execution 
for i in range(len(test_cases)):
    print(f"Test case {i}: {length_of_longest_substring(test_cases[i])}")