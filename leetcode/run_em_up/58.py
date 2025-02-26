class Solution:
    def length_of_last_word(self, s : str) -> int:
        words = []
        word = ''
        # loop through each character in the 's' string
        for c in s:
            # check is a character is a letter
            if c.isalpha():
                # append to word
                word += c
            else:
                # checker incase of empty word value
                if len(word) > 0:
                    # if not empty word value, add word to the words list
                    words.append(word)
                    # reset word value
                    word = ''
        # check if the word value is a valid string
        if len(word) > 0:
            # if so, add word to the words list
            words.append(word)
        # return the length of the last element in the words list
        return len(words[-1])

solution = Solution()
test_cases = [
    "Hello World",
    "   fly me   to   the moon  ",
    "luffy is still joyboy"
]
for i in range(len(test_cases)):
    print(solution.length_of_last_word(test_cases[i]))