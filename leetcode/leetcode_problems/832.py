class Solution:
    def flip_and_invert_image(self, image : list[list[int]]) -> list[list[int]]:    
        result = []
        for row in image:
            temp = []
            for i in row[::-1]:
                if i == 0:
                    temp.append(1)
                else:
                    temp.append(0)
            result.append(temp)
        return result

solution = Solution()
test_cases = [
    [[1,1,0],[1,0,1],[0,0,0]],
    [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
]
for i in test_cases:
    print(solution.flip_and_invert_image(i))