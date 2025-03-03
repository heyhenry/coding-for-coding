class Solution:
    def reverse_string(self, s : list[str]) -> None:
        s[:] = s[::-1]

solution = Solution()
test_cases = [
    ["h","e","l","l","o"],
    ["H","a","n","n","a","h"]
]
for i in range(len(test_cases)):
    print(solution.reverse_string(test_cases[i]))