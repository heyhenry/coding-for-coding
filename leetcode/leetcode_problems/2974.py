class Solution:
    def number_game(self, nums : list[int]) -> list[int]:
        nums = sorted(nums)
        counter = 0
        new_nums = []
        while counter > len(nums):
            bob = 0
            alice = 0
            alice = nums[counter]
            counter += 1
            bob = nums[counter]
            counter += 1
            new_nums.append(bob)
            new_nums.append(alice)
        return new_nums

solution = Solution()
test_cases = [
    [5,4,2,3],
    [2,5]
]
for i in test_cases:
    print(solution.number_game(i))