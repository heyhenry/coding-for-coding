class Solution:
    def count_matches(self, items : list[list[str]], rule_key : str, rule_value : str) -> int:
        # intialise variable to count matches found
        matches = 0
        for i in range(len(items)):
            # check against the given rule type and values
            if rule_key == 'type' and rule_value == items[i][0]:
                # add to the matches counter if match is found for any of the if statements
                matches += 1
            elif rule_key == 'color' and rule_value == items[i][1]:
                matches += 1
            elif rule_key == 'name' and rule_value == items[i][2]:
                matches += 1
        # return total matches found
        return matches

solution = Solution()
test_cases = [
    ([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"),
    ([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone")
]
for i in range(len(test_cases)):
    print(solution.count_matches(test_cases[i][0], test_cases[i][1], test_cases[i][2]))