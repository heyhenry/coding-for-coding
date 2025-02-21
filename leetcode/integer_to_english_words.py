class Solution:
    def number_to_word(self, num : int) -> str:
        # constraints: 0 <= num <= 2147483648 - 1
        # 2,147,483,648
        num = str(num)
        num_length = len(num)
        counter = 0
        lst = []
        section = ''
        total_num_length = 0
        # splitting the numbers into sections of 3s
        for i in num:
            section += i
            counter += 1
            # resetting the counter, adding the section to the lst list, resetting the counter and section variables
            if counter == 3:
                lst.append(section)
                counter = 0
                section = ''
        # checking the length of the sum length of the elements in the lst list
        for i in lst:
            total_num_length += len(i)
        # determines whether there are digits unaccounted for in the lst list
        if total_num_length < num_length:
            lst.append(section)
    
        
        




solution = Solution()

print(solution.number_to_word(123))

# test_cases = [
#     123,
#     12345,
#     1234567
# ]

# for i in range(len(test_cases)):
#     print(solution.number_to_word(test_cases[i]))