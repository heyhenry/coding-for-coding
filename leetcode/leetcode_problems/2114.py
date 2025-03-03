class Solution:
    def most_words_found(self, sentence : list[str]) -> int:
        max_word_count = 0
        for row in sentence:
            counter = 0
            for word in row.split():
                counter += 1
            if counter > max_word_count:
                max_word_count = counter
        return max_word_count

solution = Solution()
test_cases = [
    ["alice and bob love leetcode", "i think so too", "this is great thanks very much"],
    ["please wait", "continue to fight", "continue to win"]
]
for i in test_cases:
    print(solution.most_words_found(i))