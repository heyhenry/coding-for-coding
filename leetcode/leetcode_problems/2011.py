class Solution:
    def final_value_after_operations(self, operations : list[str]) -> int:
        x = 0
        for op in operations:
            if '-' in op:
                x -= 1
            else:
                x += 1
        return x

solution = Solution()
test_cases = [
    ["--X","X++","X++"],
    ["++X","++X","X++"],
    ["X++","++X","--X","X--"]
]
for i in test_cases:
    print(solution.final_value_after_operations(i))