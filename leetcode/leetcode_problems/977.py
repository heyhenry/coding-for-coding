class Solution:
    def sorted_squares(self, nums : list[int]) -> list[int]:
        # method 1
        # new_nums = [nums[i]**2 for i in range(len(nums))]
        # return sorted(new_nums)

        # method 2
        # for i in range(len(nums)):
        #     nums[i] = nums[i]**2
        # return sorted(nums)

        # after seeing this solution, understood it and did it without looking at reference again
        # 2 pointer solution
        size = len(nums)
        left, right = 0, size-1
        result = [0]*size
        for i in range(size-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                value = nums[left]
                left += 1
            else:
                value = nums[right]
                right -= 1
            result[i] = value ** 2
        return result
            



solution = Solution()
test_cases = [
    [-4,-1,0,3,10],
    [-7,-3,2,3,11]
]
for i in test_cases:
    print(solution.sorted_squares(i))