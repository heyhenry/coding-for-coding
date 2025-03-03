class Solution:
    def count_matches(self, items : list[list[str]], rule_key : str, rule_value : str) -> int:
        matches_found = 0
        for item in items:
            if rule_key == "type" and rule_value == item[0]:
                matches_found += 1
            elif rule_key == "color" and rule_value == item[1]:
                matches_found += 1
            elif rule_key == "name" and rule_value == item[2]:
                matches_found += 1
        return matches_found

solution = Solution()
test_cases = [
    ([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"),
    ([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone") 
]
for i in range(len(test_cases)):
    print(solution.count_matches(test_cases[i][0], test_cases[i][1], test_cases[i][2]))