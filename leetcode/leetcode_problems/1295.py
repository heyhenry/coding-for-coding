class Solution:
    def find_numbers(self, nums : list[int]) -> int:
        even_matches = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                even_matches += 1
        return even_matches

solution = Solution()
test_cases = [
    [12,345,2,6,7896],
    [555,901,482,1771]
]
for i in test_cases:
    print(solution.find_numbers(i))