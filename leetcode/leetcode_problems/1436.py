class Solution:
    def dest_city(self, paths : list[list[str]]) -> str:
        city_a = [i[0] for i in paths]
        for i in paths:
            if i[1] not in city_a:
                return i[1]

solution = Solution()
test_cases = [
    [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]],
    [["B","C"],["D","B"],["C","A"]],
    [["A","Z"]]
]
for i in range(len(test_cases)):
    print(solution.dest_city(test_cases[i]))