class Solution:
    def remove_element(self, nums : list[int], val : int) -> int:
        result = []
        for i in nums:
            if i != val:
                result.append(i)
        nums.clear()
        nums += result
        return len(nums)

solution = Solution()
test_cases = [
    ([3,2,2,3], 3),
    ([0,1,2,2,3,0,4,2], 2)
]
for i in test_cases:
    print(solution.remove_element(i[0], i[1]))