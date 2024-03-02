from copy import deepcopy
ls = open('2023/inputs/day11sample.txt', 'r').read().split('\n')[:-1]

'''Part 1''' #Part 2 can solve part 1
# map = []
# for row in ls:
#     list = []
#     for columns in row:
#         list.append(columns)
#     map.append(list)
# # print(map)

# map2 = []
# for rows, value_x in enumerate(map):
#     copy_list = deepcopy(value_x)
#     map2.append(copy_list)
#     for columns, value_y in enumerate(value_x):
#         if value_y == '#':
#             break
#     else:
#         copy_list2 = deepcopy(copy_list)
#         map2.append(copy_list2)

# for columns in range(len(map[0]) - 1, -1, -1):
#     for rows in range(len(map)):
#         if map[rows][columns] == '#':
#             break
#     else:
#         for rows in range(len(map2)):
#             map2[rows].insert(columns, '.')

# galaxies = []
# for rows, value_x in enumerate(map2):
#     for columns, value_y in enumerate(value_x):
#         if value_y == '#':
#             galaxies.append([rows, columns])

# list_of_dist = []
# for i in range(len(galaxies) - 1):
#     for j in range(i, len(galaxies)):
#         if i == j:
#             continue
#         distance = abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1])
#         list_of_dist.append(distance)

# print(sum(list_of_dist))

'''Part 2'''
map = []
galaxies = []
for rows, value_x in enumerate(ls):
    list = []
    for columns, value_y in enumerate(value_x):
        list.append(value_y)
        if value_y == '#':
            galaxies.append([rows, columns])
    map.append(list)

rows_expand = []
for rows, value_x in enumerate(map):
    for columns, value_y in enumerate(value_x):
        if value_y == '#':
            break
    else:
        rows_expand.append(rows)

columns_expand = []
for columns in range(len(map[0])):
    for rows in range(len(map)):
        if map[rows][columns] == '#':
            break
    else:
        columns_expand.append(columns)

for gal in galaxies:
    temp1 = 0
    temp2 = 0
    for rows in rows_expand:
        if gal[0] > rows:
            temp1 += 999999 #change this value to change row expansion
    for columns in columns_expand:
        if gal[1] > columns:
            temp2 += 999999
    gal[0] += temp1
    gal[1] += temp2

list_of_dist = []
for i in range(len(galaxies) - 1):
    for j in range(i, len(galaxies)):
        if i == j:
            continue
        distance = abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1])
        list_of_dist.append(distance)
print(sum(list_of_dist))