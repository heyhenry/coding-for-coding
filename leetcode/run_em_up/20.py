class Solution:
    def is_valid(self, s : str) -> bool:
        # method 1
        parenthesis = {')': '(', ']': '[', '}': '{'}
        stack = []
        for p in s:
            if p in '([{':
                stack.append(p)
            elif len(stack) > 0 and p in parenthesis and parenthesis[p] == stack[-1]:
                stack.pop()
            else:
                return False
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