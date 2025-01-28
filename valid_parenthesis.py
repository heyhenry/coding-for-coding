def valid_parenthesis(s : str) -> bool:
    stack = []
    pairs = {')': '(', ']': ']', '}': '{'}
    for c in s:
        if c in '([{':
            stack.append(c)
        elif stack and stack[-1] == pairs.get(c):
            stack.pop()
        else:
            return False
    return not stack

test_cases = [
    "()",
    "()[]{}",
    "(]",
    "([])"
]

for i in range(len(test_cases)):
    print(f"Test Case {i+1}: {valid_parenthesis(test_cases[i])}")