class Solution:
    def is_palindrome(self, x :int) -> bool:
        # string solution
        # return str(x) == str(x)[::-1]

        # mathematical solution
        rev_num = 0
        og = x

        if x < 0:
            return False

        while x != 0:
            tail = x % 10
            rev_num *= 10
            rev_num += tail
            x //= 10
        
        return og == rev_num

solution = Solution()
test_cases = [
    121, 
    -121, 
    10
]
for i in range(len(test_cases)):
    print(solution.is_palindrome(test_cases[i]))