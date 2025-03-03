class Solution:
    def is_valid(self, s : str) -> bool:
        stack = []
        brackets = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in '([{':
                stack.append(c)
            elif stack and brackets[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0

solution = Solution()
test_cases = [
    "()",
    "()[]{}",
    "(]",
    "([])"
]
for i in range(len(test_cases)):
    print(solution.is_valid(test_cases[i]))