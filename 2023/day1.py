ls = open('2023/inputs/day1input.txt', 'r').read().split('\n')[:-1]

# ls = ['two1nine',
# 'eightwothree',
# 'abcone2threexyz',
# 'xtwone3four',
# '4nineeightseven2',
# 'zoneight234',
# '7pqrstsixteen',
# 'cmmplbcnml36threetrxnhrrdonelmspsbhfd9twonenn',
# 'fone'
# ]

'''part 1'''
print('part 1 answer')
answer = 0
for line in ls:
    for char in line:
        if char.isnumeric():
            left_num = char
            break
    
    for char2 in line[::-1]:
        if char2.isnumeric():
            right_num = char2
            break
    
    answer += int(str(left_num) + str(right_num))
print(answer)




'''part 2'''

print('part 2 method 1 answer:')
answer = 0
num_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
for line in ls:
    word = ''
    for char in line:
        if char.isnumeric():
            first_number = char
            break
        word += char
        for j in num_dict:
            if j in word:
                first_number = num_dict.get(j)
                break
        else:
            continue
        break
    word = ''
    for char2 in line[::-1]:
        if char2.isnumeric():
            second_number = char2
            break
        word = char2 + word
        for l in num_dict:
            if l in word:
                second_number = num_dict.get(l)
                break
        else:
            continue
        break
    number = first_number + second_number
    answer += int(number)
print(answer)


print('part 2 method 2 answer:')
answer = 0
one_letter = ['o', 't', 'f', 's', 'e', 'n']
two_letter = ['on', 'tw', 'th', 'fo', 'fi', 'si', 'se', 'ei', 'ni']
three_letter = ['one', 'two', 'thr', 'fou', 'fiv', 'six', 'sev', 'eig', 'nin']
four_letter = ['thre', 'four', 'five', 'seve', 'eigh', 'nine']
five_letter = ['three', 'seven', 'eight']
backward_one_letter = ['e', 'o', 'r', 'x', 'n', 't']
backward_two_letter = ['ne', 'wo', 'ee', 'ur', 've', 'ix', 'en', 'ht']
backward_three_letter = ['one', 'two', 'ree', 'our', 'ive', 'six', 'ven', 'ght', 'ine']
backward_four_letter = ['hree', 'four', 'five', 'even', 'ight', 'nine']
for line in ls:
    word = ''
    for char in line:
        if char.isnumeric():
            first_number = char
            break
        word += char
        if num_dict.get(word) is not None:
            first_number = num_dict[word]
            break
        if len(word) == 5 and word not in five_letter:
            word = word[1:]
        if len(word) == 4 and word not in four_letter:
            word = word[1:]
        if len(word) == 3 and word not in three_letter:
            word = word[1:]
        if len(word) == 2 and word not in two_letter:
            word = word[1:]
        if len(word) == 1 and word not in one_letter:
            word = word[1:]

    word = ''
    for char2 in line[::-1]:
        if char2.isnumeric():
            second_number = char2
            break
        word = char2 + word
        if num_dict.get(word) is not None:
            second_number = num_dict[word]
            break
        if len(word) == 5 and word not in five_letter:
            word = word[:-1]
        if len(word) == 4 and word not in backward_four_letter:
            word = word[:-1]
        if len(word) == 3 and word not in backward_three_letter:
            word = word[:-1]
        if len(word) == 2 and word not in backward_two_letter:
            word = word[:-1]
        if len(word) == 1 and word not in backward_one_letter:
            word = word[:-1]
    number = first_number + second_number
    answer += int(number)
print(answer)