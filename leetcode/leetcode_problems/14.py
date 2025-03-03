class Solution:
    def longest_common_prefix(self, strs : list[str]) -> str:
        prefix = ''
        smallest_column = len(min(strs, key=len))
        for col in range(smallest_column):
            temp = ''
            for row in range(len(strs)):
                temp += strs[row][col]
            if temp == temp[0]*len(strs):
                prefix += temp[0]
            else:
                return prefix
        return prefix

solution = Solution()
test_cases = [
    ["flower","flow","flight"],
    ["dog","racecar","car"]
]
for i in range(len(test_cases)):
    print(solution.longest_common_prefix(test_cases[i]))