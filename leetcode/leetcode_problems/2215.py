class Solution:
    def find_difference(self, nums1 : list[int], nums2 : list[int]) -> list[list[int]]:
        ans_nums1 = []
        ans_nums2 = []
        for i in nums1:
            if i not in nums2 and i not in ans_nums1:
                ans_nums1.append(i)
        for i in nums2:
            if i not in nums1 and i not in ans_nums2:
                ans_nums2.append(i)
        return [ans_nums1, ans_nums2]
        

solution = Solution()
test_cases = [
    ([1,2,3], [2,4,6]),
    ([1,2,3,3], [1,1,2,2])
]
for i in test_cases:
    print(solution.find_difference(i[0], i[1]))