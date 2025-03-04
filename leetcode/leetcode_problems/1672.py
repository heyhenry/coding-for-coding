class Solution:
    def maximum_wealth(self, accounts : list[list[int]]) -> int:
        return sum(max(accounts, key=sum))

solution = Solution()
test_cases = [
    [[1,2,3],[3,2,1]],
    [[1,5],[7,3],[3,5]],
    [[2,8,7],[7,1,3],[1,9,5]]
]
for i in test_cases:
    print(solution.maximum_wealth(i))