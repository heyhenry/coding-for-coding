class Solution:
    def roman_to_int(self, s : str) -> int:
        size = len(s)
        result = 0
        numerals = {
            'I': 1, 
            'V': 5, 
            'X': 10,
            'L': 50, 
            'C': 100,
            'D': 500, 
            'M': 1000
        }
        for i in range(size):
            # only reason this logic works is because it is for roman numerals
            # this is because, roman numerals' law/logic strictly follows that
            # the only time a number is bigger after a smaller number is because it's a subtractive pair (i.e. IV, IX),
            # if there was a number that was bigger after a smaller number and wasn't a subtractive pair, then it was an
            # invalid roman numeral to begin with

            # also leetcode denotes that it will provide only valid roman numerals.
            if i != size-1 and numerals[s[i]] < numerals[s[i+1]]:
                result -= numerals[s[i]]
            else:
                result += numerals[s[i]]
        return result


solution = Solution()
test_cases = [
    "III", 
    "LVIII",
    "MCMXCIV"
]
for i in range(len(test_cases)):
    print(solution.roman_to_int(test_cases[i]))