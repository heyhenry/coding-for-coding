def remove_element(nums : list[int], val : int) -> int:
    lst = []
    for i in nums:
        if i != val:
            lst.append(i)
    nums.clear()
    nums += lst
    return len(nums)

test_cases = [
    ([3,2,2,3], 3),
    ([0,1,2,2,3,0,4,2], 2)
]

for i in range(len(test_cases)):
    print(f"Test Case {i}: {remove_element(test_cases[i][0], test_cases[i][1])}")