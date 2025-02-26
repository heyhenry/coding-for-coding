class Solution:
    def reverse_string(self, s : list[str]) -> None:
        # solution 1
        rev = s[::-1]
        for i in range(len(s)):
            s[i] = rev[i]
        return s

solution = Solution()
test_cases = [
    ["h","e","l","l","o"],
    ["H","a","n","n","a","h"]
]
for i in range(len(test_cases)):
    print(solution.reverse_string(test_cases[i]))