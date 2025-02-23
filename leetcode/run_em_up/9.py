class Solution:
    def is_palindrome(self, x : int) -> bool:
        return str(x) == str(x)[::-1]
    
solution = Solution()

test_cases = [
    121,
    -121,
    10
]

for i in range(len(test_cases)):
    print(solution.is_palindrome(test_cases[i]))