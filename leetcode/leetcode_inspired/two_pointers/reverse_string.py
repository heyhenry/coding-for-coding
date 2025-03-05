"""
reverse a string, in-place modification
"""

class Solution:
    def reverse_string(self, s: list[str]) -> None:
        left = 0
        right = len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        # output log to confirm reversed string
        # return s 

solution = Solution()
test_cases = [
    ['h', 'e', 'l', 'l', 'o']
]
for i in test_cases:
    print(solution.reverse_string(i))