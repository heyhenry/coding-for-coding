# Q3. Sum All Subarrays
# Print the sum of each subarray instead of the subarray itself

def sum_all_subarrays(lst : list[int]):
    size = len(lst)
    for start in range(size):
        for end in range(start, size):
            # +1 cause end slicing notation excludes the last number 'end'
            print(sum(lst[start:end+1]))

arr = [1, 2, 3]

sum_all_subarrays(arr)

# Expected output
# 1
# 3
# 6
# 2
# 5
# 3
