class Solution:
    def is_happy(self, n : int) -> bool:
        # list to store unique nums
        nums = []
        # loop until n equals 1
        while n != 1:
            # reset new_n value
            new_n = 0
            # algorithm to compute new number based on requested formula
            for i in str(n):
                new_n += int(i)**2
            # if new number hasn't been computed before, add to nums list
            if new_n not in nums:
                nums.append(new_n)
                # update the n value to the latest unique number (new_n)
                n = new_n
            # if a duplicate new number is found, return False
            else:
                
                return False
        # if 1 is found, return True
        return True

solution = Solution()
test_cases = [
    19,
    2
]
for i in range(len(test_cases)):
    print(solution.is_happy(test_cases[i]))