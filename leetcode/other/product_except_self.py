def product_except_self(nums : list[int]) -> list[int]:
    size = len(nums)

    # prefix poduct of each element
    prefix_array = [1] * size
    for i in range(1, size):
        prefix_array[i] = prefix_array[i-1] * nums[i-1]

    # suffix product of each element
    suffix = 1
    suffix_array = [1] * size
    for i in range(size-1, -1, -1):
        suffix_array[i] = suffix
        suffix *= nums[i]
    
    # combine prefix and suffix products
    results = [1] * size
    for i in range(size):
        results[i] = prefix_array[i] * suffix_array[i]

    return results

# test cases
test_cases = [
    [1,2,3,4],
    [-1,1,0,-3,3]
]

# execute test cases
for i in range(len(test_cases)):
    print(f"Test case {i}: {product_except_self(test_cases[i])}")