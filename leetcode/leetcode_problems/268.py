class Solution:
    def missing_number(self, nums : list[int]) -> int:
        # method 1
        # n = len(nums)
        # for i in range(n+1):
        #     if i not in nums:
        #         return i

        # method 2
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            if i != nums[i]:
                return i
        return n

solution = Solution()
test_cases = [
    [3,0,1],
    [0,1],
    [9,6,4,2,3,5,7,0,1]
]
for i in test_cases:
    print(solution.missing_number(i))