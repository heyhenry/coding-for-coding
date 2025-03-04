class Solution:
    def sum_odd_length_subarrays(self, arr : list[int]) -> int:
        size = len(arr)
        result = 0
        for start in range(size):
            for end in range(start, size):
                if len(arr[start:end+1]) % 2 != 0:
                    result += sum(arr[start:end+1])
        return result
                
solution = Solution()
test_cases = [
    [1,4,2,5,3],
    # [1,2],
    # [10,11,12]
]
for i in test_cases:
    print(solution.sum_odd_length_subarrays(i))