class Solution:
    def is_palindrome(self, s : str) -> bool:
        s = "".join([c for c in s.lower() if c.isalnum()])
        return s == s[::-1]

solution = Solution()
test_cases = [
    "A man, a plan, a canal: Panama", 
    "race a car",
    " "
]
for i in range(len(test_cases)):
    print(solution.is_palindrome(test_cases[i]))