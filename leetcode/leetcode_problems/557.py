class Solution:
    def reverse_words(self, s : str) -> str:
        s = s.split()
        size = len(s)
        new_s = ''
        for i in range(size):
            if i != size-1:
                new_s += (s[i][::-1] + ' ')
            else:
                new_s += s[i][::-1]
        return new_s

solution = Solution()
test_cases = [
    "Let's take LeetCode contest",
    "Mr Ding"
]
for i in range(len(test_cases)):
    print(solution.reverse_words(test_cases[i]))