class Solution:
    def array_strings_are_equal(self, word_1 : list[str], word_2 : list[str]) -> bool:
        # boolean expression between the joined/concatenated string versions of the two words
        return "".join(word_1) == "".join(word_2)

solution = Solution()
test_cases = [
    (["ab", "c"], ["a", "bc"]),
    (["a", "cb"], ["ab", "c"]),
    (["abc", "d", "defg"], ["abcddefg"])
]
for i in range(len(test_cases)):
    print(solution.array_strings_are_equal(test_cases[i][0], test_cases[i][1]))