class Solution:
    def is_palindrome(self, x : int) -> bool:
        # string conversion solution
        # return str(x) == str(x)[::-1]
        
        # mathematics solution
        # check if the integer is a negative 
        rev_flag = False
        if x < 0:
            # flag if negative
            rev_flag = True
            # change integer value x into a positive
            x = abs(x)
        rev_x = 0
        original_x = x
        # maths algorithm for reversing an integer
        while x != 0:
            # get the tail(last) digit
            tail = x % 10
            # move the reverse integer value one position to the left
            rev_x *= 10
            # append the tail digit on the end of the reverse integer
            rev_x += tail
            # remove the tail digit from the original integer (x)
            x //= 10
        # turn reverse integer to negative if original integer flagged as a negative
        if rev_flag:
            rev_x = -rev_x
        # boolean check if original and reverse values are the same
        return original_x == rev_x
    
solution = Solution()

test_cases = [
    121,
    -121,
    10
]

for i in range(len(test_cases)):
    print(solution.is_palindrome(test_cases[i]))