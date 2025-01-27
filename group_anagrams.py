def group_anagrams(lst : list):
    h_anagrams = {}
    for i in lst:
        if "".join(sorted(i)) not in h_anagrams:
            h_anagrams["".join(sorted(i))] = [i]
        else:
            h_anagrams["".join(sorted(i))].append(i)
    
    results = []
    for i in h_anagrams.values():
        results.append(i)

    return results

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