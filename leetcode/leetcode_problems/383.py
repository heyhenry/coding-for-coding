class Solution:
    def can_construct(self, ransom_note: str, magazine : str) -> bool:
        magazine_dict = {}
        for i in magazine:
            if i not in magazine_dict:
                magazine_dict[i] = 1
            else:
                magazine_dict[i] += 1

        for i in ransom_note:
            if i in magazine_dict and magazine_dict[i] != 0:
                magazine_dict[i] -= 1
            else:
                return False
        return True

solution = Solution()
test_cases = [
    ("a", "b"),
    ("aa", "ab"),
    ("aa", "aab")
]
for i in range(len(test_cases)):
    print(solution.can_construct(test_cases[i][0], test_cases[i][1]))