class Solution:
    def replace_digits(self, s : str) -> str:
        # solution 1
        # shift func
        # def shift(c : str, i : int):
        #    # finds the new character based on unicode maths
        #     return chr(ord(c)+int(i))
        # size = len(s)
        # new_s = ''
        # # iterates through the s string and creates a new updated string s
        # # replacing digits with leters
        # for i in range(size):
        #     # if the element (string) at this position in the string is a digit
        #     if s[i].isdigit():
        #         # then invoke the shift method and convert to the appropriate letter
        #         new_s += shift(s[i-1], s[i])
        #     else:
        #         # if not, then add normal letter to new string s
        #         new_s += s[i]
        # # update all element (letters etc) in the old s string with those of the new s string
        # s = new_s[:]
        # # return updated string s
        # return s

        # solution 2 - reduced code based on solution 1
        new_s = ''
        for i in range(len(s)):
            if s[i].isdigit():
                new_s += chr(ord(s[i-1])+int(s[i]))
            else:
                new_s += s[i]
        s = new_s[:]
        return s

solution = Solution()
test_cases = [
    "a1c1e1",
    "a1b2c3d4e"
]
for i in range(len(test_cases)):
    print(solution.replace_digits(test_cases[i]))