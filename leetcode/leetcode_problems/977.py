class Solution:
    def sorted_squares(self, nums : list[int]) -> list[int]:
        new_nums = [nums[i]**2 for i in range(len(nums))]
        return sorted(new_nums)

solution = Solution()
test_cases = [
    [-4,-1,0,3,10],
    [-7,-3,2,3,11]
]
for i in test_cases:
    print(solution.sorted_squares(i))