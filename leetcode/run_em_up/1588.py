class Solution:
    def sum_odd_length_subarrays(self, arr : list[int]) -> int:
        result = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if len(arr[i:j+1]) % 2 != 0:
                    result += sum(arr[i:j+1])
        return result

solution = Solution()
test_cases = [
    [1,4,2,5,3],
    # [1,2],
    # [10,11,12]
]
for i in range(len(test_cases)):
    print(solution.sum_odd_length_subarrays(test_cases[i]))