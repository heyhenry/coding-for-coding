class Solution:
    def most_frequent_even(self, nums : list[int]) -> int:
        even_dict = {}
        for i in nums:
            if i % 2 == 0 and i not in even_dict:
                even_dict[i] = 1
            elif i % 2 == 0:
                even_dict[i] += 1
        if not even_dict:
            return -1
        most_frequent_tally = []
        most_frequent = max(even_dict.values())
        for key, val in sorted(even_dict.items()):
            if val == most_frequent:
                most_frequent_tally.append(key)
        return most_frequent_tally[0]

solution = Solution()
test_cases = [
    [0,1,2,2,4,4,1],
    [4,4,4,9,2,4],
    [29,47,21,41,13,37,25,7]
]
for i in test_cases:
    print(solution.most_frequent_even(i))