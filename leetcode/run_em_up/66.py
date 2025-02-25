class Solution:
    def plus_one(self, digits : list[int]) -> list[int]:
        # solution - beats 100% of peers
        # list comprehension that converts digits's element to string
        # then joins them all together
        # then turns it into a whole integer
        # then adds 1 to said whole integer
        num = int("".join([str(i) for i in digits])) + 1
        # list comprehension that converts the new whole integer back into individual int type elements
        digits = [int(i) for i in str(num)]
        # return the newly revised digits list
        return digits

solution = Solution()
test_cases = [
    [1,2,3],
    [4,3,2,1],
    [9]
]
for i in range(len(test_cases)):
    print(solution.plus_one(test_cases[i]))