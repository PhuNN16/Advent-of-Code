from collections import defaultdict
ls = open('2023/inputs/day15input.txt', 'r').read().strip().split(',')

'''Part 1'''
# list_of_current_val = []
# for strings in ls:
#     print(strings)
#     current_val = 0
#     for char in strings:
#         current_val += ord(char)
#         current_val *= 17
#         current_val = current_val % 256
#     list_of_current_val.append(current_val)
# print(list_of_current_val)
# print(sum(list_of_current_val))


'''Part 2'''
boxes = {}
for strings in ls:
    # print(strings)
    label = ''
    box_num = 0
    for char in strings:
        if char == '=' or char == '-': 
            break
        label += char
        box_num += ord(char)
        box_num *= 17
        box_num = box_num % 256
    if boxes.get(box_num, None) is None: #creates a dictionary so .get() doesnt error
        boxes[box_num] = {}
    if '-' in strings:
        if boxes[box_num].get(label, None) is not None:
            boxes[box_num].pop(label)
    elif '=' in strings:
        focal_length = strings[-1]
        if boxes[box_num].get(label, None) is None:
            boxes[box_num][label] = focal_length
        else:
            boxes[box_num][label] = focal_length

list_of_fp = []
for box in boxes:
    count = 1
    for label in boxes[box]:
        focusing_power = (box + 1) * count * int(boxes[box][label])
        list_of_fp.append(focusing_power)
        count += 1
print(sum(list_of_fp))