class Solution:
    def di_string_match(self, s : str) -> list[int]:
        size = len(s)
        low = 0
        high = size
        perm = []
        for i in range(size):
            if s[i] == 'D':
                perm.append(high)
                high -= 1
            else:
                perm.append(low)
                low += 1
        perm.append(low)
        return perm

solution = Solution()
test_cases = [
    "IDID",
    "III",
    "DDI"
]
for i in range(len(test_cases)):
    print(solution.di_string_match(test_cases[i]))