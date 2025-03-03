class Solution:
    def str_str(self, haystack : str, needle : str) -> int:
        haystack_size = len(haystack)
        needle_size = len(needle)
        for i in range(haystack_size):
            if haystack[i:i+needle_size] == needle:
                return i
        return -1

solution = Solution()
test_cases = [
    ("sadbutsad", "sad"),
    ("leetcode", "leeto")
]
for i in range(len(test_cases)):
    print(solution.str_str(test_cases[i][0], test_cases[i][1]))