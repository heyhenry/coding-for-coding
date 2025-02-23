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
        # algorithm
        for i in range(size):
            # skip an iteration if future i was already added to result
            if skip_flag:
                skip_flag = False
                continue
            # find integer conversion where there is a possibility of
            # two elements may be required
            if i+1 <= size-1:
                # see if conversion requires 2 elements i.e. IV, CM, CD
                if s[i]+s[i+1] in roman_map:
                    result += roman_map[s[i]+s[i+1]]
                    # flag to skip next iteration
                    skip_flag = True
                else:
                    result += roman_map[s[i]]
            else:
                result += roman_map[s[i]]
        return result

solution = Solution()

test_cases = [
    "III",
    "LVIII",
    "MCMXCIV"
]

for i in range(len(test_cases)):
    print(solution.roman_to_int(test_cases[i]))