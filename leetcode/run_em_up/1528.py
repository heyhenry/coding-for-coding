class Solution:
    def restore_string(self, s : str, indices : list[int]) -> str:
        # initialise a dictionary
        map = {}
        # populate dictionary with key[indices] = val[s]
        for c in range(len(indices)):
            map[indices[c]] = s[c]
        # initialise output variable
        result = ''
        # loop through the dictionary in sorted form
        for key, val in sorted(map.items()):
            # append each value (character) to the output variable
            result += val
        # return output
        return result

solution = Solution()
test_cases = [
    ("codeleet",[4,5,6,7,0,2,1,3]),
    ("abc",[0,1,2])
]
for i in range(len(test_cases)):
    print(solution.restore_string(test_cases[i][0], test_cases[i][1]))