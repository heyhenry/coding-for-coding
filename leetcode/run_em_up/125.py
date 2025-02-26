class Solution:
    def is_palindrome(self, s : str) -> bool:
        # join all the found chars and digits as a single revised string in lower case
        s = "".join([i for i in s.lower() if i.isalnum()])
        # compare the string with its reverse, and return result
        return s == s[::-1]

solution = Solution()
test_cases = [
    "A man, a plan, a canal: Panama",
    "race a car",
    " "
]
for i in range(len(test_cases)):
    print(solution.is_palindrome(test_cases[i]))