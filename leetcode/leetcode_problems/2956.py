class Solution:
    def find_intersection_values(self, nums1 : list[int], nums2 : list[int]) -> list[int]:
        # method 1
        ans = []
        counter = 0
        for i in nums1:
            if i in nums2:
                counter += 1
        ans.append(counter)
        counter = 0
        for i in nums2:
            if i in nums1:
                counter +=1
        ans.append(counter)
        return ans


solution = Solution()
test_cases = [
    ([2,3,2], [1,2]),
    ([4,3,2,3,1], [2,2,5,2,3,6]),
    ([3,4,2,3], [1,5])
]
for i in test_cases:
    print(solution.find_intersection_values(i[0], i[1]))