class Solution:

    def is_signed_32bit(self, n):
        return -2_147_483_648 <= n <= 2_147_483_647

    def reverse(self, x : int) -> int:
        rev_num = 0
        is_negative = False
        if x < 0:
            x = abs(x)
            is_negative = True
        while x != 0:
            tail = x % 10
            rev_num *= 10
            rev_num += tail
            x //= 10
        if not self.is_signed_32bit(rev_num):
            return 0
        if is_negative:
            return -rev_num
        return rev_num

test_cases = [
    321,
    -123,
    120,
    1534236469
]

sol = Solution()

for i in range(len(test_cases)):
    print(sol.reverse(test_cases[i]))
