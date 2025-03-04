class Solution:
    def build_array(self, nums : list[int]) -> list[int]:
        size = len(nums)
        ans = []
        for i in range(size):
            ans.append(nums[nums[i]])
        return ans

solution = Solution()
test_cases = [
    [0,2,1,5,3,4],
    [5,0,1,2,3,4]
]
for i in test_cases:
    print(solution.build_array(i))