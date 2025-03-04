class Solution:
    def separate_digits(self, nums : list[int]) -> list[int]:
        digits = ''
        for i in nums:
            digits += str(i)
        return [int(i) for i in digits]

solution = Solution()
test_cases = [
    [13,25,83,77],
    [7,1,3,9]
]
for i in test_cases:
    print(solution.separate_digits(i))