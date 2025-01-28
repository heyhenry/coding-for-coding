def valid_parenthesis(s : str) -> bool:
    # initialize stack list to store parenthesis
    stack = []
    # intialize pair dictionary for reference of parenthesis pairings
    pairs = {')': '(', ']': '[', '}': '{'}
    # iterate through the string of parenthesis
    for c in s:
        # if its an opening parenthesis store in stack
        if c in '([{':
            stack.append(c)
        # check if stack is empty
        # compare last element in stack against pair's key value for match
        elif stack and stack[-1] == pairs.get(c):
            stack.pop()
        # early exit if a closing parenthesis is to be added to the stack
        else:
            return False
    # check if stack is empty for boolean result
    return not stack

test_cases = [
    "()",
    "()[]{}",
    "(]",
    "([])"
]

for i in range(len(test_cases)):
    print(f"Test Case {i+1}: {valid_parenthesis(test_cases[i])}")