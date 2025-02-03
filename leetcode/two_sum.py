# success achieved in the leetcode sandbox as well.

def two_sum(nums : list[int], target : int) -> list[int]:
    # iterate through the elements in the nums list
    for i in range(len(nums)):
        # iterate through the elemtsn in the nums list but start 1 element ahead
        for j in range(i+1, len(nums)):
            # find a match to the target value
            if nums[i] + nums[j] == target:
                # return the indexes of the numbers that make the sum of the target value
                return [i,j]

# test cases
test_cases = [
    ([2,7,11,15], 9),
    ([3,2,4], 6),
    ([3,3], 6)
]

# test case execution
for i in range(len(test_cases)):
    print(f"Test case {i}: {two_sum(test_cases[i][0], test_cases[i][1])}")