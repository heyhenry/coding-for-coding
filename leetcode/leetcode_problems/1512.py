class Solution:
    def num_identical_pairs(self, nums : list[int]) -> int:
        size = len(nums)
        pairs = 0
        for i in range(size):
            for j in range(i+1, size):
                if nums[i] == nums[j]:
                    pairs += 1
        return pairs

solution = Solution()
test_cases = [
    [1,2,3,1,1,3],
    [1,1,1,1],
    [1,2,3]
]
for i in test_cases:
    print(solution.num_identical_pairs(i))