num = '2147483648'
# 2,147,483,648

# base digit conversion to english 
base_num = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

ten_base = {
    '1': 'teen',
    '2': 'twenty',
    '3': 'thirty',
    '4': 'fourty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
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
    check_num_length += len(i)

# check if lst has all elements from num
if check_num_length < num_length:
    lst.append((section, group_counter+1))

# reverse the list to reflect groupings of 3s to reflect base num's order
lst = lst[::-1]
print(lst)

positional_values = {
    2: 'thousand',
    3: 'million',
    4: 'billion'
}

new_sentences = []
full_word = ''
for i in lst:
    the_word = ''
    if len(i[0]) == 3:
        the_word += (f" {base_num[i[0][0]]} " + 'hundred')
        if i[1] == '1':
            the_word += f" {base_num[i[0][2]]} "
            the_word += f" {ten_base[i[0][1]]} "
        else:
            the_word += f" {ten_base[i[0][1]]} "
            the_word += f" {base_num[i[0][2]]} "
    elif len(i[0]) == 2:
        if i[1] == '1':
            the_word += f" {base_num[i[0][1]]} "
            the_word += f" {ten_base[i[0][0]]} "
    else:
        the_word += f" {base_num[i[0]]} "
    if i[1] in positional_values:
        the_word += f" {positional_values[i[1]]} "
    full_word += the_word

print(full_word)
