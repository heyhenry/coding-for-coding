class Solution:
    def defang_IP_addr(self, address : str) -> str:
        return address.replace('.', '[.]')

solution = Solution()
test_cases = [
    "1.1.1.1",
    "255.100.50.0"
]
for i in range(len(test_cases)):
    print(solution.defang_IP_addr(test_cases[i]))