class Solution:
    def final_value_after_operations(self, operations : list[str]) -> int:
        result = 0
        for i in operations:
            if '-' in i:
                result -= 1
            else:
                result += 1
        return result

solution = Solution()
test_cases = [
    ["--X","X++","X++"], 
    ["++X","++X","X++"],
    ["X++","++X","--X","X--"]
]
for i in range(len(test_cases)):
    print(solution.final_value_after_operations(test_cases[i]))