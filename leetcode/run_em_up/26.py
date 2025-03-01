class Solution:
    def remove_duplicates(self, nums : list[int]) -> int:
        # new list with only unique numbers in ascending order
        unique_nums = sorted(set(nums))
        # clear the original contents of nums list
        nums.clear()
        # repopulate nums list with unique_nums list's content
        nums += unique_nums
        # return the length of the newly revised nums list
        return len(nums)

solution = Solution()
test_cases = [
    [1,1,2], 
    [0,0,1,1,1,2,2,3,3,4]
]
for i in range(len(test_cases)):
    print(solution.remove_duplicates(test_cases[i]))