class Solution:
    def repeated_character(self, s : str) -> str:
        s_dict = {}
        for c in s:
            if c not in s_dict:
                s_dict[c] = 1
            else:
                return c

solution = Solution()
test_cases = [
    "abccbaacz",
    "abcdd"
]
for i in test_cases:
    print(solution.repeated_character(i))