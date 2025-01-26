# success achieved in the leetcode sandbox as well.

def merge(intervals : list[list[int]]) -> list[list[int]]:
    # ensure the element lists are sorted smallest value to 
    # largest based on their starting interval value per element list
    intervals = sorted(intervals)
    merged = []
    for interval in intervals:
        # populare the merged list with an initial interval
        if len(merged) < 1:
            merged.append(interval)
        # compare merged's last interval's ending value against the current intervals starting value as well as end value
        # to determine whether a merge is applicable 
        elif merged[-1][1] >= interval[0] and merged[-1][1] < interval[1]:
            merged[-1] = [merged[-1][0], interval[1]]
        # if a duplicate is found, pass
        elif merged[-1][1] >= interval[0] and merged[-1][1] >= interval[1]:
            continue
        # if the current interval's starting value is largest than the last merged's interval's end value
        # then add the current interval to the merged's list
        else:
            merged.append(interval)
    return merged

# test cases
test_cases = [
    [[1,3],[2,6],[8,10],[15,18]],
    [[1,4],[4,5]],
    [[1,4],[1,4]],
    [[1,4],[2,3]],
    [[1,4],[0,4]]
]

# execute test cases
for i in range(len(test_cases)):
    print(f"Test case {i}: {merge(test_cases[i])}")