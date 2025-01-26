def merge(intervals : list[list[int]]) -> list[list[int]]:
    intervals = sorted(intervals)
    merged = []
    for interval in intervals:
        if len(merged) < 1:
            merged.append(interval)
        elif merged[-1][1] >= interval[0] and merged[-1][1] < interval[1]:
            merged[-1] = [merged[-1][0], interval[1]]
        elif merged[-1][1] >= interval[0] and merged[-1][1] >= interval[1]:
            continue
        else:
            merged.append(interval)
    return merged

test_cases = [
    [[1,3],[2,6],[8,10],[15,18]],
    [[1,4],[4,5]],
    [[1,4],[1,4]],
    [[1,4],[2,3]],
    [[1,4],[0,4]]
]

for i in range(len(test_cases)):
    print(f"Test case {i}: {merge(test_cases[i])}")