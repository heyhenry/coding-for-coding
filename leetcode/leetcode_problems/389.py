class Solution:
    def find_the_difference(self, s : str, t : str) -> str:
        t_dict = {}
        for i in t:
            if i not in t_dict:
                t_dict[i] = 1
            else:
                t_dict[i] += 1
        
        for i in s:
            if i in t_dict and t_dict[i] != 0:
                t_dict[i] -= 1
        
        for key, val in t_dict.items():
            if val == 1:
                return key
    
solution = Solution()
test_cases = [
    ("abcd", "abcde"),
    ("", "y")
]
for i in range(len(test_cases)):
    print(solution.find_the_difference(test_cases[i][0], test_cases[i][1]))