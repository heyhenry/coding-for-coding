import string

class Solution:
    def decode_message(self, key : str, message : str) -> str:
        alphabet = string.ascii_lowercase
        decoder = {}
        size = len(alphabet)
        new_key = ""
        decoded_message = ""
        for c in key:
            if c not in new_key and c.isalpha():
                new_key += c
        for i in range(size):
            decoder[new_key[i]] = alphabet[i]
        for c in message:
            if c == ' ':
                decoded_message += ' '
            else:
                decoded_message += decoder[c]
        return decoded_message

solution = Solution()
test_cases = [
    ("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"),
    ("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb")
]
for i in test_cases:
    print(solution.decode_message(i[0], i[1]))