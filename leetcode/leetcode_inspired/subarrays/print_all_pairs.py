# Q1. Print All Pairs
# Given a list 'arr', print every pair of numbers (order matters)
def print_all_pairs(lst : list[int]):
    size = len(lst)
    for i in range(size):
        for k in range(i, size):
            print((lst[i], lst[k]))

arr = [1, 2, 3]

print_all_pairs(arr)

# Expected output
(1, 1)
(1, 2)
(1, 3)
(2, 2)
(2, 3)
(3, 3)
