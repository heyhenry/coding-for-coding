class Solution:
    def number_to_word(self, num : int) -> str:
        if num == 0:
            return 'Zero'
        
        num = str(num)
        
        # base digit conversion to english 
        base_num = {
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine'
        }

        ten_base = {
            '1': 'teen',
            '2': 'Twenty',
            '3': 'Thirty',
            '4': 'Forty',
            '5': 'Fifty',
            '6': 'Sixty',
            '7': 'Seventy',
            '8': 'Eighty',
            '9': 'Ninety'
        }

        num_length = len(num)
        check_num_length = 0
        counter = 0
        section = ''
        lst = []
        group_counter = 0

        # group digits into 3s from left to right
        for i in num[::-1]:
            counter += 1
            section += i
            if counter == 3:
                group_counter += 1
                # reverse each group of numbers to correlate with base num
                lst.append((section[::-1], group_counter))
                counter = 0
                section = ''

        # supply num length checker variable with existing list element length
        for i in lst:
            check_num_length += len(i[0])

        # check if lst has all elements from num
        if check_num_length < num_length:
            lst.append((section[::-1], group_counter+1))

        # reverse the list to reflect groupings of 3s to reflect base num's order
        lst = lst[::-1]

        positional_values = {
            2: 'Thousand',
            3: 'Million',
            4: 'Billion'
        }
        special_nums = {
            '10': 'Ten',
            '11': 'Eleven',
            '12': 'Twelve',
            '13': 'Thirteen',
            '14': 'Fourteen',
            '15': 'Fifteen',
            '16': 'Sixteen',
            '17': 'Seventeen',
            '18': 'Eighteen',
            '19': 'Nineteen'
        }

        full_word = ''
        for i in lst:
            the_word = ''
            if len(i[0]) == 3:
                the_word += (f"{base_num[i[0][0]]} " + 'Hundred ') 
                if int(i[0][1]+i[0][2]) in range(10, 20):
                    the_word += f"{special_nums[i[0][1]+i[0][2]]}"
                else:
                    if i[0][2] == '0':
                        the_word += f"{ten_base[i[0][1]]} "
                    else:
                        the_word += f"{ten_base[i[0][1]]} "
                        the_word += f"{base_num[i[0][2]]} "
            elif len(i[0]) == 2:
                if int(i[0]) in range(10,20):
                    the_word += f"{special_nums[[i][0][0]]} " 
                else:
                    if i[0][1] == '0':
                        the_word += f"{ten_base[i[0][0]]} "
                    else:
                        the_word += f"{ten_base[i[0][0]]} "
                        the_word += f"{base_num[i[0][1]]} "
            else:
                the_word += f"{base_num[i[0]]} "
            if i[1] in positional_values:
                the_word += f"{positional_values[i[1]]} "
            full_word += the_word
        
        full_word = full_word.strip()

        return full_word
    
solution = Solution()

print(solution.number_to_word(12003))

# Current Issue: 
# cant deal with more than 1 0 on the end i.e. 100, 1000, 100000, 1000000 also stuff like 12003

# test_cases = [
#     123,
#     12345,
#     1234567
# ]

# for i in range(len(test_cases)):
#     print(solution.number_to_word(test_cases[i]))