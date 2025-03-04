class Solution:
    def running_sum(self, nums : list[int]) -> list[int]:
        size = len(nums)
        for i in range(1, size):
            nums[i] += nums[i-1]
        return nums

solution = Solution()
test_cases = [
    [1,2,3,4],
    [1,1,1,1,1],
    [3,1,2,10,1]
]
for i in test_cases:
    print(solution.running_sum(i))