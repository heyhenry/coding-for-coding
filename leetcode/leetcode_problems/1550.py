class Solution:
    def three_consecutive_odds(self, arr : list[int]) -> bool:
        odd_counter = 0
        for i in arr:
            if i % 2 != 0:
                odd_counter += 1
                if odd_counter == 3:
                    return True
            else:
                odd_counter = 0
        return False

solution = Solution()
test_cases = [
    [2,6,4,1],
    [1,2,34,3,4,5,7,23,12]
]
for i in test_cases:
    print(solution.three_consecutive_odds(i))