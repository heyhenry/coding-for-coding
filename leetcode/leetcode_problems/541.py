class Solution:
    def reverse_str(self, s : str, k : int) -> str:
        s = [i for i in s]
        size = len(s)
        for i in range(0, size, 2*k):
            s[i:i+k] = s[i:i+k][::-1]
        return "".join(s)

solution = Solution()
test_cases = [
    ("abcdefg", 2),
    ("abcd", 2)
]
for i in range(len(test_cases)):
    print(solution.reverse_str(test_cases[i][0], test_cases[i][1]))