class Solution:
    def sum_of_unqiue(self, nums : list[int]) -> int:
        result = 0
        nums_dict = {}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i] += 1
        for key, val in nums_dict.items():
            if val == 1:
                result += key
        return result

solution = Solution()
test_cases = [
    [1,2,3,2],
    [1,1,1,1,1],
    [1,2,3,4,5]
]
for i in test_cases:
    print(solution.sum_of_unqiue(i))