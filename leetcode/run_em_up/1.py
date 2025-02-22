class Solution:
    def two_sum(self, nums : list[int], target : int) -> list[int]:
        # nested for loop solution (aka brute force)
        # size = len(nums)
        # for i in range(size):
        #     for j in range(i+1, size):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # double loop solution 
        nums_dict = {}
        size = len(nums)
        for i in range(size):
            nums_dict[nums[i]] = i

        for i in range(size):
            complement = target - nums[i]
            if complement in nums_dict and complement != i:
                return [i, nums_dict[complement]]

solution = Solution()

print(solution.two_sum([2,7,11,2,15], 9))

# test_cases = [
#     ([2,7,11,15], 9),
#     ([3,2,4], 6),
#     ([3,3], 6)
# ]

# for i in range(len(test_cases)):
#     print(solution.two_sum(test_cases[i][0], test_cases[i][1]))