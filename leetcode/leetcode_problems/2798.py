class Solution:
    def number_of_employees_who_met_target(self, hours : list[int], target : int) -> int:
        good_employees = 0
        for i in hours:
            if i >= target:
                good_employees += 1
        return good_employees

solution = Solution()
test_cases = [
    ([0,1,2,3,4], 2),
    ([5,1,4,2,2], 6)
]
for i in test_cases:
    print(solution.number_of_employees_who_met_target(i[0], i[1]))