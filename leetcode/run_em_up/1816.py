class Solution:
    def truncate_sentence(self, s : str, k : int) -> str:
        # turn s in to list of words
        s = s.split()
        result = ''
        # iterate through the list of words
        for i in range(k):
            # if not the last iteration, add a space to the concatentation of the word
            if i != k-1:
                result += (s[i] + ' ')
            # else refrain from adding a space after the word
            else:
                result += s[i]
        # return output
        return result

solution = Solution()
test_cases = [
    ("Hello how are you Contestant", 4),
    ("What is the solution to this problem", 4), 
    ("chopper is not a tanuki", 5)
]
for i in range(len(test_cases)):
    print(solution.truncate_sentence(test_cases[i][0], test_cases[i][1]))