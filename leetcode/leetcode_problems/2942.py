class Solution:
    def find_words_containing(self, words : list[str], x : str) -> list[int]:
        size = len(words)
        results = []
        for i in range(size):
            if x in words[i]:
                results.append(i)
        return results

solution = Solution()
test_cases = [
    (["leet","code"], "e"),
    (["abc","bcd","aaaa","cbc"], "a"),
    (["abc","bcd","aaaa","cbc"], "z")
]
for i in test_cases:
    print(solution.find_words_containing(i[0], i[1]))