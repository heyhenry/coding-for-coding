class Solution:
    def is_signed_32bit(self, n):
        return -2_147_483_648 <= n <= 2_147_483_647
    
    # solution 1 using maths
    # def reverse(self, x : int) -> int:
    #     rev_flag = False
    #     if x < 0:
    #         x = abs(x)
    #         rev_flag = True
    #     rev_x = 0
    #     # reverse integer algorithm
    #     while x != 0:
    #         tail = x % 10
    #         rev_x *= 10
    #         rev_x += tail
    #         x //= 10
    #     # check if reversed integer is larger than 32bit
    #     if not self.is_signed_32bit(rev_x):
    #         return 0
    #     if rev_flag:
    #         return -rev_x
    #     return rev_x

    # solution 2 using string conversions
    def reverse(self, x : int) -> int:
        rev_flag = False
        if x < 0:
            rev_flag = True
            x = abs(x)
        x = str(x)[::-1]
        if rev_flag:
            x = -int(x)
        else:
            x = int(x)
        if not self.is_signed_32bit(x):
            return 0
        return x

solution = Solution()

test_cases = [
    123,
    -123,
    120
]

for i in range(len(test_cases)):
    print(solution.reverse(test_cases[i]))