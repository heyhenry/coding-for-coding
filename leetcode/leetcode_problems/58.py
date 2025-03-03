class Solution:
    def length_of_last_word(self, s : str) -> int:
        s = s.split()
        return len(s[-1])

solution = Solution()
test_cases = [
    "Hello World",
    "   fly me   to   the moon  ",
    "luffy is still joyboy"
]
for i in range(len(test_cases)):
    print(solution.length_of_last_word(test_cases[i]))