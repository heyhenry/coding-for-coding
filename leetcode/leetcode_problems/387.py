class Solution:
    def first_uniq_char(self, s : str) -> int:
        s1 = set(s)
        s_dict = {}
        for i in s1:
            s_dict[i] = s.count(i)
        for c in range(len(s)):
            if s_dict[s[c]] == 1:
                return c
        return -1

solution = Solution()
test_cases = [
    "leetcode",
    "loveleetcode",
    "aabb"
]
for i in range(len(test_cases)):
    print(solution.first_uniq_char(test_cases[i]))