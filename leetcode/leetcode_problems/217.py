class Solution:
    def contains_duplicate(self, nums : list[int]) -> bool:
        n = set(nums)
        return len(n) != len(nums)

solution = Solution()
test_cases = [
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,3,2,4,2]
]
for i in test_cases:
    print(solution.contains_duplicate(i))