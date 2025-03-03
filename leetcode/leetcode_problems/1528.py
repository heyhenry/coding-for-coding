class Solution:
    def restore_string(self, s : str, indices : list[str]) -> str:
        # method 1
        # s_dict = {}
        # size = len(s)
        # new_s = ''
        # for i in range(size):
        #     s_dict[indices[i]] = s[i]
        # for key, val in sorted(s_dict.items()):
        #     new_s += val
        # return new_s

        # method 2
        size = len(s)
        new_s = ['']*size
        for i in range(size):
            new_s[indices[i]] = s[i]
        return "".join(new_s)

solution = Solution()
test_cases = [
    ("codeleet", [4,5,6,7,0,2,1,3]),
    ("abc", [0,1,2])
]
for i in range(len(test_cases)):
    print(solution.restore_string(test_cases[i][0], test_cases[i][1]))