"""
Name: Numbers with this digit inside 
Created by: user5036852

You have to search all numbers from inclusive 1 to inclusive a given number x, that have the given digit d in it.
The value of d will always be 0 - 9.
The value of x will always be greater than 0.

You have to return as an array

    1. the count of these numbers,
    2. their sum
    3. their product.

    For example:

    x = 11
    d = 1
    ->
    Numbers: 1, 10, 11
    Return: [3, 22, 110]


If there are no numbers, which include the digit, return [0,0,0]. 
"""
def numbers_with_digit_inside(x, d):
    d_count = 0
    d_sum = 0
    d_product = None
    results = [0]*3

    for i in range(1, x+1):
        if str(d) in str(i):
            d_count += 1
            d_sum += i
            if d_product is None:
                d_product = i
            else:
                d_product *= i
    
    results[0] = d_count
    results[1] = d_sum
    if d_product is not None:
        results[2] = d_product

    return results