class Solution:
    def num_jewels_in_stone(self, jewels : str, stones : str) -> int:
        found_jewels = 0
        for stone in stones:
            if stone in jewels:
                found_jewels += 1
        return found_jewels

solution = Solution()
test_cases = [
    ("aA", "aAAbbbb"),
    ("z", "ZZ")
]
for i in range(len(test_cases)):
    print(solution.num_jewels_in_stone(test_cases[i][0], test_cases[i][1]))