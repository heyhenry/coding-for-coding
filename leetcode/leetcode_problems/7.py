class Solution:

    def is_32bit(self, i : int) -> bool:
        if -2_147_483_648 <= i <= 2_147_483_648 - 1:
            return True
        return False

    def reverse(self, x : int) -> int:
        rev_num = 0
        neg_flag = False

        if x < 0:
            x = abs(x)
            neg_flag = True
        
        while x != 0:
            tail = x % 10
            rev_num *= 10
            rev_num += tail
            x //= 10

        if neg_flag:
            rev_num = -rev_num

        if not self.is_32bit(rev_num):
            return 0
        
        return rev_num

    # -2_147_483_648 < i < 2_147_483_648

solution = Solution()
test_cases = [
    123,
    -123,
    120
]
for i in range(len(test_cases)):
    print(solution.reverse(test_cases[i]))