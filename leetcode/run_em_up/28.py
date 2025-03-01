class Solution:
    def str_str(self, haystack : str, needle: str) -> int:
        # length of strings
        haystack_size = len(haystack)
        needle_size = len(needle)
        # iterate through the haystack chars
        for i in range(haystack_size):
            # if haystack sliced section equals the needle string
            if haystack[i:needle_size+i] == needle:
                # return the index at which it started
                return i
        # no hits, return -1
        return -1

solution = Solution()
test_cases = [
    ("sadbutsad", "sad"),
    ("leetcode", "leeto")
]
for i in range(len(test_cases)):
    print(solution.str_str(test_cases[i][0], test_cases[i][1]))