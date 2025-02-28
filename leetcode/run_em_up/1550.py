class Solution:
    def three_consecutive_odds(self, arr : list[int]) -> bool:
        # count of continuous odds found
        counter = 0
        for i in arr:
            # formula to check if the number is odd
            if i % 2 != 0:
                counter += 1
                # if the count equals 3, True boolean satisfied
                if counter == 3:
                    return True
            else:
                counter = 0
        # return False boolean if 3 consistent odds are not found
        return False

solution = Solution()
test_cases = [
    [2,6,4,1], 
    [1,2,34,3,4,5,7,23,12]
]
for i in range(len(test_cases)):
    print(solution.three_consecutive_odds(test_cases[i]))