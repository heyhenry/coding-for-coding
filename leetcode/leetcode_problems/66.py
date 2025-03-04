class Solution:
    def plus_one(self, digits : list[int]) -> list[int]:
        num = ''
        for i in digits:
            num += str(i)
        num = int(num) + 1
        digits.clear()
        for i in str(num):
            digits.append(int(i))
        return digits

solution = Solution()
test_cases = [
    [1,2,3],
    [4,3,2,1],
    [9]
]
for i in test_cases:
    print(solution.plus_one(i))