class Solution:
    def convert_temperature(self, celsius : float) -> list[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]

solution = Solution()
test_cases = [
    36.50,
    122.11
]
for i in test_cases:
    print(solution.convert_temperature(i))