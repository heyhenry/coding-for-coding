# Q2. Print All Subarrays
# Given 'arr', print every subarray
def print_every_subarray(lst : list[int]):
    size = len(lst)
    for start in range(size):
        for end in range(start, size):
            print(lst[start:end+1])

arr = [4, 5, 6]

print_every_subarray(arr)

# Expected output
# [4]
# [4, 5]
# [4, 5, 6]
# [5]
# [5, 6]
# [6]
