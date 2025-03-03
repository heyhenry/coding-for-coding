class Solution:
    def shift(self, c : str, i : int) -> str:
        return chr(ord(c)+int(i))
    
    def replace_digits(self, s : str) -> str:
        size = len(s)
        new_s = ''
        for c in range(size):
            if s[c].isdigit():
                new_s += self.shift(s[c-1], int(s[c]))
            else:
                new_s += s[c]
        return new_s

solution = Solution()
test_cases = [
    "a1c1e1",
    "a1b2c3d4e"
]
for i in test_cases:
    print(solution.replace_digits(i))