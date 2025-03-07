class Solution:
    def array_strings_are_equal(self, word1 : list[str], word2 : list[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

solution = Solution()
test_cases = [
    (["ab", "c"], ["a", "bc"]),
    (["a", "cb"], ["ab", "c"]),
    (["abc", "d", "defg"], ["abcddefg"])
]
for i in range(len(test_cases)):
    print(solution.array_strings_are_equal(test_cases[i][0], test_cases[i][1]))