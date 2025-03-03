class Solution:
    def find_the_difference(self, s : str, t : str) -> str:
        # my solution
        # t_dict = {}
        # for i in t:
        #     if i not in t_dict:
        #         t_dict[i] = 1
        #     else:
        #         t_dict[i] += 1
        
        # for i in s:
        #     if i in t_dict and t_dict[i] != 0:
        #         t_dict[i] -= 1
        
        # for key, val in t_dict.items():
        #     if val == 1:
        #         return key

        # glimpsed ascii solution i tried without fully looking
        # i dont need to add the square bracketse to turn this into a list comprehension cos sum() takes in generator expressions aka the below.
        # essentially opt for the below way (i.e. exclude the square brakets) because including the square brackets means itll create the whole list before doing sum. aka an extra step.
        s1 = sum(ord(c) for c in s)
        t1 = sum(ord(c) for c in t)
        return chr(t1-s1)
    
solution = Solution()
test_cases = [
    ("abcd", "abcde"),
    ("", "y")
]
for i in range(len(test_cases)):
    print(solution.find_the_difference(test_cases[i][0], test_cases[i][1]))