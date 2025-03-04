class Solution:
    def shuffle(self, nums : list[int], n : int) -> list[int]:
        # method 1
        # size = len(nums)
        # y_nums = [nums[i] for i in range(n, size)]
        # y_size = len(y_nums)
        # new_nums = []
        # for i in range(y_size):
        #     new_nums.append(nums[i])
        #     new_nums.append(y_nums[i])
        # return new_nums

        # method 2
        new_nums = []
        for i in range(n):
            new_nums.append(nums[i])
            new_nums.append(nums[i+n])
        return new_nums

solution = Solution()
test_cases = [
    ([2,5,1,3,4,7], 3),
    ([1,2,3,4,4,3,2,1], 4),
    ([1,1,2,2], 2)
]
for i in test_cases:
    print(solution.shuffle(i[0], i[1]))
