class Solution:
    def maximum_number_of_string_pairs(self, words : list[str]) -> int:
        size = len(words)
        pairs = 0
        for i in range(size):
            for j in range(i+1, size):
                if words[i] == words[j][::-1]:
                    pairs += 1
        return pairs

solution = Solution()
test_cases = [
    ["cd","ac","dc","ca","zz"],
    ["ab","ba","cc"],
    ["aa","ab"]
]
for i in test_cases:
    print(solution.maximum_number_of_string_pairs(i))