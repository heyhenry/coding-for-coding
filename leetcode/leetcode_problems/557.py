class Solution:
    def reverse_words(self, s : str) -> str:
        # first solution
        # s = s.split()
        # size = len(s)
        # new_s = ''
        # for i in range(size):
        #     if i != size-1:
        #         new_s += (s[i][::-1] + ' ')
        #     else:
        #         new_s += s[i][::-1]
        # return new_s

        # 2nd solution using .join() 
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        return ' '.join(s)

solution = Solution()
test_cases = [
    "Let's take LeetCode contest",
    "Mr Ding"
]
for i in range(len(test_cases)):
    print(solution.reverse_words(test_cases[i]))