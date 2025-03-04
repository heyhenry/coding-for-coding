class Solution:
    def sort_people(self, names : list[str], heights : list[int]) -> list[str]:
        # method 1
        # size = len(names)
        # hn_dict = {}
        # updated_names = []
        # for i in range(size):
        #     hn_dict[heights[i]] = names[i]
        # for key, val in sorted(hn_dict.items(), reverse=True):
        #     updated_names.append(val)
        # return updated_names

        # method 2
        size = len(names)
        d = {}
        for i in range(size):
            d[heights[i]] = names[i]
        counter = 0
        for key, val in sorted(d.items(), reverse=True):
            names[counter] = val
            counter += 1
        return names

solution = Solution()
test_cases = [
    (["Mary","John","Emma"], [180,165,170]),
    (["Alice","Bob","Bob"], [155,185,150])
]
for i in test_cases:
    print(solution.sort_people(i[0], i[1]))