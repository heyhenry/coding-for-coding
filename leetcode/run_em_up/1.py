class Solution:
    def two_sum(self, nums : list[int], target : int) -> list[int]:
        size = len(nums)
        for i in range(size):
            for j in range(i+1, size):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        return []

solution = Solution()

test_cases = [
    ([2,7,11,15], 9),
    ([3,2,4], 6),
    ([3,3], 6)
]

for i in range(len(test_cases)):
    print(solution.two_sum(test_cases[i][0], test_cases[i][1]))