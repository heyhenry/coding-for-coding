class Solution:
    def height_checker(self, heights : list[int]) -> int:
        size = len(heights)
        expected_heights = sorted(heights)
        mismatch = 0
        for i in range(size):
            if heights[i] != expected_heights[i]:
                mismatch += 1
        return mismatch

solution = Solution()
test_cases = [
    [1,1,4,2,1,3],
    [5,1,2,3,4],
    [1,2,3,4,5]
]
for i in test_cases:
    print(solution.height_checker(i))