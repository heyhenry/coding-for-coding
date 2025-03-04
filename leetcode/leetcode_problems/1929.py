class Solution:
    def get_concatenation(self, nums : list[int]) -> list[int]:
        return nums*2

solution = Solution()
test_cases = [
    [1,2,1],
    [1,3,2,1]
]
for i in test_cases:
    print(solution.get_concatenation(i))