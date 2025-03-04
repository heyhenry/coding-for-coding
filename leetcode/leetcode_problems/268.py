class Solution:
    def missing_number(self, nums : list[int]) -> int:
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i

solution = Solution()
test_cases = [
    [3,0,1],
    [0,1],
    [9,6,4,2,3,5,7,0,1]
]
for i in test_cases:
    print(solution.missing_number(i))