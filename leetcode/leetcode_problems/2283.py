class Solution:
    def digit_count(self, num : str) -> bool:
        size = len(num)
        for i in range(size):
            if num.count(str(i)) != int(num[i]):
                return False
        return True

solution = Solution()
test_cases = [
    "1210",
    "030"
]
for i in test_cases:
    print(solution.digit_count(i))