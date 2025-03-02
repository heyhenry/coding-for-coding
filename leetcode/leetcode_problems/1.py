class Solution:
    def two_sum(self, nums : list[int], target : int) -> list[int]:
        # solution 1 (brute force)
        # size = len(nums)
        # for i in range(size):
        #     for j in range(i+1, size):
        #         if nums[i]+nums[j] == target:
        #             return [i, j]
    
        # 2 loops solution
        # nums_map = {}
        # size = len(nums)
        # for i in range(size):
        #     nums_map[nums[i]] = i
        # for i in range(size):
        #     part = target - nums[i]
        #     if part in nums_map and nums_map[part] != i:
        #         return [i, nums_map[part]] # <--- the indexes can be in any order, because the dictionary was created before this loop, so part can be indexed anywhere
        # return []

        # 1 loop solution
        nums_map = {}
        size = len(nums)
        for i in range(size):
            component = target - nums[i]
            if component in nums_map:
                return [nums_map[component], i]
            nums_map[nums[i]] = i
        return []

solution = Solution()
test_cases = [
    ([2,7,11,15], 9), 
    ([3,2,4], 6),
    ([3,3], 6)
]
for i in range(len(test_cases)):
    print(solution.two_sum(test_cases[i][0], test_cases[i][1]))