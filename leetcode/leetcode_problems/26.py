class Solution:
    def remove_duplicates(self, nums : list[int]) -> int:
        s_nums = set(nums)
        nums.clear()
        nums += sorted(s_nums)
        return len(nums)

solution = Solution()
test_cases = [
    [1,1,2],
    [0,0,1,1,1,2,2,3,3,4]
]
for i in test_cases:
    print(solution.remove_duplicates(i))