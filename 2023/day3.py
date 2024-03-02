ls = open('2023/inputs/day3input.txt', 'r').read().split('\n')[:-1]


'''part 1'''
map = []
list_of_added = []
gears = {}

for rows in ls:
    list = []
    for columns in rows:
        list.append(columns)
    map.append(list)
    
for rows, list in enumerate(map):
    num_string = ''
    add_num = False
    mul_num = False
    star = ()
    for columns, value in enumerate(list):
        if value.isnumeric():
            num_string += value
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if rows + i < 0 or rows + i > len(map) - 1:
                        continue
                    if columns + j < 0 or columns + j > len(list) - 1:
                        continue
                    if map[rows+i][columns+j] != '.' and not map[rows+i][columns+j].isnumeric():
                        if map[rows+i][columns+j] == '*':
                            mul_num = True
                            star = (rows+i, columns+j)
                        add_num = True  
        else:
            if add_num:
                list_of_added.append(int(num_string))
                add_num = False
                if mul_num:
                    if star not in gears:
                        gears[star] = [int(num_string)]
                    else:
                        gears[star].append(int(num_string))
            num_string = ''
            mul_num = False
            star = ()
    else:
        if add_num:
            list_of_added.append(int(num_string))
            add_num = False
            if mul_num:
                if star not in gears:
                    gears[star] = [int(num_string)]
                else:
                    gears[star].append(int(num_string))
        num_string = ''
        mul_num = False
        star = ()
gear_ratio = 0
for i in gears:
    if len(gears[i]) == 2:
        gear_ratio += gears[i][0] * gears[i][1]

# print(gears)
print(gear_ratio)
# print(list_of_added)
print(sum(list_of_added))
