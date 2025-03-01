class Solution:
    def sum_of_unique(self, nums : list[int]) -> int:
        nums_map = {}
        # map the num and their frequency into nums_map dictionary
        for i in nums:
            if i not in nums_map:
                nums_map[i] = 1
            else:
                nums_map[i] += 1

        result = 0
        # target the numbers that have a single frequency and add to result sum
        for key, val in nums_map.items():
            if val == 1:
                result += key
        # return the resulting sum of unique numbers added
        return result

solution = Solution()
test_cases = [
    [1,2,3,2], 
    [1,1,1,1,1], 
    [1,2,3,4,5]
]
for i in range(len(test_cases)):
    print(solution.sum_of_unique(test_cases[i]))