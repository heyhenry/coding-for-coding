class Solution:
    def roman_to_int(self, s : str) -> int:
        # roman conversion dict
        roman_map = {
            'I': 1,
            'V': 5, 
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400, 
            'CM': 900
        }
        size = len(s)
        result = 0
        skip_flag = False
        # my first solution
        # # algorithm
        # for i in range(size):
        #     # skip an iteration if future i was already added to result
        #     if skip_flag:
        #         skip_flag = False
        #         continue
        #     # find integer conversion where there is a possibility of
        #     # two elements may be required
        #     if i+1 <= size-1:
        #         # see if conversion requires 2 elements i.e. IV, CM, CD
        #         if s[i]+s[i+1] in roman_map:
        #             result += roman_map[s[i]+s[i+1]]
        #             # flag to skip next iteration
        #             skip_flag = True
        #         else:
        #             result += roman_map[s[i]]
        #     else:
        #         result += roman_map[s[i]]
        # return result

        # my second solution (got by checking solution by 'The Subtle One' on leetcode)
        for i in range(size):
            if i+1 <= size-1 and roman_map[s[i]] < roman_map[s[i+1]]:
                result -= roman_map[s[i]]
            else:
                result += roman_map[s[i]]
        return result
        # mental issue grasping the solution in its entirey, understood the gist but 
        # couldnt completely wrap head around it in full mental clarity -
        # after some time found a good way to look at it that helped wrap it up in my head
        # the way: the reason for the -= is because it knows the next one is gonna be a big one i.e. 
        # current one is I, next one is V so if it's IV its 4 instead of I+V = 6
        # so the current i = I will start by negating the value before hand as the rest of the value will be supplemented by its upcoming duo/partner the V
        # i.e. result = 0 -> result -= I (1) and then result = -1 -> result += I (5) which will give a result of 4 which is reflective of IV
                    

solution = Solution()

test_cases = [
    # "III",
    # "LVIII",
    "MCMXCIV"
]

for i in range(len(test_cases)):
    print(solution.roman_to_int(test_cases[i]))