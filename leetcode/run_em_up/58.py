class Solution:
    def length_of_last_word(self, s : str) -> int:
        words = []
        word = ''
        for c in s:
            if c.isalpha():
                word += c
            else:
                if len(word) > 0:
                    words.append(word)
                    word = ''
        if len(word) > 0:
            words.append(word)
        return len(words[-1])

solution = Solution()
test_cases = [
    "Hello World",
    "   fly me   to   the moon  ",
    "luffy is still joyboy"
]
for i in range(len(test_cases)):
    print(solution.length_of_last_word(test_cases[i]))