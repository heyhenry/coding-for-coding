class Solution:
    def count_seniors(self, details : list[str]) -> int:
        found = 0
        for passenger in details:
            if int(passenger[11:13]) > 60:
                found += 1
        return found

solution = Solution()
test_cases = [
    ["7868190130M7522","5303914400F9211","9273338290F4010"],
    ["1313579440F2036","2921522980M5644"]
]
for i in test_cases:
    print(solution.count_seniors(i))