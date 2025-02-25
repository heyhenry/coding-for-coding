class Solution:
    def search_insert(self, nums : list[int], target : int) -> int:
        size = len(nums)
        if target < nums[0]:
            return 0
        for i in range(size):
            if nums[i] == target:
                return i
            elif i > 0 and target < nums[i] and target > nums[i-1]:
                return i

        return size
        
solution = Solution()

test_cases = [
    ([1,3,5,6], 5),
    ([1,3,5,6], 2),
    ([1,3,5,6], 7)
]

for i in range(len(test_cases)):
    print(solution.search_insert(test_cases[i][0], test_cases[i][1]))