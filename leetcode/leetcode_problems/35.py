class Solution:
    def search_insert(self, nums : list[int], target : int) -> int:
        size = len(nums)
        if target < nums[0]:
            return 0
        for i in range(size):
            if target == nums[i]:
                return i
            elif nums[i-1] < target < nums[i]:
                return i
        return size
        

solution = Solution()
test_cases = [
    ([1,3,5,6], 5),
    ([1,3,5,6], 2),
    ([1,3,5,6], 7),
    ([1,3], 2)
]
for i in test_cases:
    print(solution.search_insert(i[0], i[1]))