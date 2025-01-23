def fizz_buzz_twist(lst : list):
    results = []
    for i in lst:
        if i % 3 == 0 and i % 5 == 0:
            results.append('FizzBuzz')
        elif i % 3 == 0:
            results.append('Fizz')
        elif i % 5 == 0:
            results.append('Buzz')
        else:
            results.append(i)
        
    return results


# test cases
test_cases = [
    [1, 3, 5, 15, 22],
    [0, 3, 5, 15, 7, 9, 10, 13],
    [1, 2, 4, 7, 8, 11],
    [3, 6, 9, 12, 18],
    [5, 10, 20, 25, 40],
    [15, 30, 45, 60],
    [0],
    [-3, -5, -15, -4, -7],
    []
]

# run test cases
for test in range(len(test_cases)):
    print(f"Test {test}: {fizz_buzz_twist(test_cases[test])}")

"""
Expected Results:
Test 0: [1, 'Fizz', 'Buzz', 'FizzBuzz', 22]
Test 1: ['FizzBuzz', 'Fizz', 'Buzz', 'FizzBuzz', 7, 'Fizz', 'Buzz', 13]
Test 2: [1, 2, 4, 7, 8, 11]
Test 3: ['Fizz', 'Fizz', 'Fizz', 'Fizz', 'Fizz']
Test 4: ['Buzz', 'Buzz', 'Buzz', 'Buzz', 'Buzz']
Test 5: ['FizzBuzz', 'FizzBuzz', 'FizzBuzz', 'FizzBuzz']
Test 6: ['FizzBuzz']
Test 7: ['Fizz', 'Buzz', 'FizzBuzz', -4, -7]
Test 8: []
"""