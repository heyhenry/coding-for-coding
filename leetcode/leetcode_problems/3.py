class Solution:
    def length_of_longest_substring(self, s : str) -> int:
        subs = []
        sub_s = ''
        for c in s:
            if c not in sub_s:
                sub_s += c
            else:
                subs.append(sub_s)
                sub_s = (sub_s[sub_s.rfind(c)+1:] + c)
        subs.append(sub_s)
        return len(max(subs, key=len))

solution = Solution()
test_cases = [
    "abcabcbb", 
    "bbbbb",
    "pwwkew",
    " ",
    ""
]
for i in range(len(test_cases)):
    print(solution.length_of_longest_substring(test_cases[i]))