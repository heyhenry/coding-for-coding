class Solution:
    def find_target_pair(self, nums: list[int], target : int) -> list[int]:
        size = len(nums)
        left = 0
        right = size-1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1 
        return []

solution = Solution()
test_cases = [
    ([1, 2, 3, 4, 6], 6), # [1, 3]
    ([2, 3, 5, 9], 8), # [0,2]
    ([2, 7], 9), #[0, 1]
    ([1, 3, 5, 7, 10], 11), # [0, 4]
    ([-4, -2, 0, 3, 5, 9], 3), # [1, 4]
    ([1, 10, 50, 100, 200], 150), # [2, 3]
    ([1, 2, 3, 9], 20) # []
]
for i in test_cases:
    print(solution.find_target_pair(i[0], i[1]))