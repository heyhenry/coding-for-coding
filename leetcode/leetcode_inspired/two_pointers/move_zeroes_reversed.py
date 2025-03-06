# instead of moving zeroes to the back, left move em to the front

class Solution:
    def move_zeroes(self, nums: list[int]) -> None:
        # method 1
        size = len(nums)
        right = size-1
        for left in range(size-1, -1, -1):
            if nums[left] != 0:
                nums[right] = nums[left]
                if right != left:
                    nums[left] = 0
                right -= 1
        return nums

solution = Solution()
test_cases = [
    [0, 1, 0, 3, 12],
    [1, 0, 2, 0, 3]
]
for i in test_cases:
    print(solution.move_zeroes(i))