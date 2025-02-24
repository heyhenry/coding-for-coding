class Solution:
    def longest_common_prefix(self, strs : list[str]) -> str:
        prefix = ''
        # find the smallest length from the element for column size
        col_size = len(min(strs, key=len))
        # algorithm 
        # this algorithm uses a 'column-wise iteration' also known as vertical traversal
        # this gives the first character of each element before proceeding with the next character of each element and so forth
        for col in range(col_size):
            # temporary value to compare and evaluate add-on for prefix
            temp = ''
            for row in range(len(strs)):
                # add all the characters of each element at the same position
                temp += strs[row][col]
            # check using temp if all characters in temp is the same
            # if so, it indicates that all elements share the same character
            if temp == temp[0]*len(temp):
                # add it to the prefix
                prefix += temp[0]
            # if all characters at the same position in the element are not the same
            # then finish running the algorithm and output the resulting prefix
            # *as anything after this point isnt considered a prefix, 
            # you cant continue adding anymore characters to said prefix*
            else:
                return prefix
        # alternatively output a prefix result that may have never triggered the else statement in the for loop
        return prefix

solution = Solution()

test_cases = [
    # ["flower","flow","flight"],
    # ["dog","racecar","car"],
    # [""],
    # ["a"]
    # ["ab", "a"]
]

for i in range(len(test_cases)):
    print(solution.longest_common_prefix(test_cases[i]))