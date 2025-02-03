def group_anagrams(lst : list):
    # initialise a dictionary to group anagrams
    anagram_groups = {}
    # iterate through the lst list
    for i in lst:
        # sort each word alphabetically and compare
        sorted_key = "".join(sorted(i))
        if sorted_key not in anagram_groups:
            anagram_groups[sorted_key] = [i]
        else:
            anagram_groups[sorted_key].append(i)
    
    # create a list based on the values of anagram_groups
    return list(anagram_groups.values())

# test cases
test_cases = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    ["dog", "god", "cat", "act", "odg"],
    ["abc", "def", "ghi"],
    ["a"],
    []
]

# execute test cases
for i in range(len(test_cases)):
    print(f"Test case {i}: {group_anagrams(test_cases[i])}")