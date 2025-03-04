class Solution:
    def difference_of_sum(self, nums : list[int]) -> int:
        digits = ''
        for i in nums:
            digits += str(i)
        digits = [int(i) for i in digits]
        return abs(sum(digits) - sum(nums))

solution = Solution()
test_cases = [
    [1,15,6,3],
    [1,2,3,4]
]
for i in test_cases:
    print(solution.difference_of_sum(i))