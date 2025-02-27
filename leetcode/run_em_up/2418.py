class Solution:
    def sort_people(self, names : list[str], heights : list[int]) -> list[str]:
        # intialise dictionary, list and a size varable
        map = {}
        size = len(names)
        result = []
        # iterate through the 2 lists and create key/val (height/name) for each iteration 
        for i in range(size):
            map[heights[i]] = names[i]
        # loop through the dictionary in descending order
        for key, val in sorted(map.items(), reverse=True):
            # store the values (names) into the output list 
            result.append(val)
        # return the resulting output
        return result

solution = Solution()
test_cases = [
    (["Mary","John","Emma"], [180,165,170]),
    (["Alice","Bob","Bob"], [155,185,150])
]
for i in range(len(test_cases)):
    print(solution.sort_people(test_cases[i][0], test_cases[i][1]))