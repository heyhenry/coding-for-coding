class Solution:
    def search_insert(self, nums : list[int], target : int) -> int:
        # list size variable <-- less len() executions
        size = len(nums)
        # early return if target value is lower than initial element in the list
        if target < nums[0]:
            return 0
        # algorithm to check if a match is found, else determine possible insertion position
        for i in range(size):
            # found match
            if nums[i] == target:
                return i
            # found insertable position in list
            elif i > 0 and target < nums[i] and target > nums[i-1]:
                return i
        # target value is found to be the largest value
        return size
        
solution = Solution()

test_cases = [
    ([1,3,5,6], 5),
    ([1,3,5,6], 2),
    ([1,3,5,6], 7)
]

for i in range(len(test_cases)):
    print(solution.search_insert(test_cases[i][0], test_cases[i][1]))