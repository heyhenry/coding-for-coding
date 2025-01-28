def valid_parenthesis(s : str) -> bool:
    stack = []
    size = len(s)
    for c in s:
        if c in '([{':
            stack.append(c)
        elif stack:
            if c == ')' and stack[-1] == '(':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop() 
            else:
                stack.append(c)
        else:
            stack.append(c)
    
    return len(stack) == 0

test_cases = [
    "()",
    "()[]{}",
    "(]",
    "([])"
]

for i in range(len(test_cases)):
    print(f"Test Case {i+1}: {valid_parenthesis(test_cases[i])}")