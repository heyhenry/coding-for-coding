class Solution:
    def truncate_sentence(self, s : str, k : int) -> str:
        s = s.split()
        return " ".join(s[0:k])

solution = Solution()
test_cases = [
   ("Hello how are you Contestant", 4),
   ("What is the solution to this problem", 4),
   ("chopper is not a tanuki", 5)
]
for i in range(len(test_cases)):
    print(solution.truncate_sentence(test_cases[i][0], test_cases[i][1]))