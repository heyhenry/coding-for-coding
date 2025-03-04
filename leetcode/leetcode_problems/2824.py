class Solution:
    def count_pairs(self, nums : list[int], target : int) -> int:
        size = len(nums)
        pairs = 0
        for i in range(size):
            for j in range(i+1, size):
                if nums[i] + nums[j] < target:
                    pairs += 1
        return pairs

solution = Solution()
test_cases = [
    ([-1,1,2,3,1], 2),
    ([-6,2,5,-2,-7,-1,3], -2)
]
for i in test_cases:
    print(solution.count_pairs(i[0], i[1]))