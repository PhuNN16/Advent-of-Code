ls = open('2023/inputs/day10sample2.txt', 'r').read().split('\n')[:-1]

'''Part 1'''
map = []
for row in ls:
    list = []
    for columns in row:
        list.append(columns)
    map.append(list)

for rows, value_x in enumerate(map):
    for columns, value_y in enumerate(value_x):
        if value_y == 'S':
            starting_coord = [rows, columns]

directions_map = {'|': {'N':'N','S':'S'}, '7':{'E':'S', 'N':'W'}, 'L':{'S':'E', 'W':'N'}, 'J':{'S':'W', 'E':'N'}, 'F':{'N':'E', 'W':'S'}, '-':{'W':'W', 'E':'E'}, '.':{'':''}}#7

# print(map[starting_coord[0]+1][starting_coord[1]])
if directions_map[map[starting_coord[0] - 1][starting_coord[1]]].get('N', None) is not None:
    position = [starting_coord[0] - 1, starting_coord[1]]
    directions = directions_map[map[starting_coord[0] - 1][starting_coord[1]]]['N']

elif directions_map[map[starting_coord[0]][starting_coord[1] + 1]].get('E', None) is not None:
    position = [starting_coord[0], starting_coord[1] + 1]
    directions = directions_map[map[starting_coord[0]][starting_coord[1] + 1]]['E']

elif directions_map[map[starting_coord[0] + 1][starting_coord[1]]].get('S', None) is not None:
    position = [starting_coord[0] + 1, starting_coord[1]]
    directions = directions_map[map[starting_coord[0] + 1][starting_coord[1]]]['S']

elif directions_map[map[starting_coord[0]][starting_coord[1] - 1]].get('W', None) is not None:
    position = [starting_coord[0], starting_coord[1] - 1]
    directions = directions_map[map[starting_coord[0]][starting_coord[1] - 1]]['W']

steps = 1
while True:
    if directions == 'N':
        position = [position[0] - 1, position[1]]
    elif directions == 'E':
        position = [position[0], position[1] + 1]
    elif directions == 'S':
        position = [position[0] + 1, position[1]]
    elif directions == 'W':
        position = [position[0], position[1] - 1]
    steps += 1
    if map[position[0]][position[1]] == 'S':
        break
    directions = directions_map[map[position[0]][position[1]]][directions]
print(steps//2)

'''Part 2'''
map = []
for row in ls:
    list = []
    for columns in row:
        list.append(columns)
    map.append(list)

for rows, value_x in enumerate(map):
    for columns, value_y in enumerate(value_x):
        if value_y == 'S':
            starting_coord = [rows, columns]

directions_map = {'|': {'N':'N','S':'S'}, '7':{'E':'S', 'N':'W'}, 'L':{'S':'E', 'W':'N'}, 'J':{'S':'W', 'E':'N'}, 'F':{'N':'E', 'W':'S'}, '-':{'W':'W', 'E':'E'}, '.':{'':''}}#7
corners = [starting_coord]

# print(map[starting_coord[0]+1][starting_coord[1]])
if directions_map[map[starting_coord[0] - 1][starting_coord[1]]].get('N', None) is not None:
    # position = [starting_coord[0] - 1, starting_coord[1]]
    directions = directions_map[map[starting_coord[0] - 1][starting_coord[1]]]['N']

elif directions_map[map[starting_coord[0]][starting_coord[1] + 1]].get('E', None) is not None:
    position = [starting_coord[0], starting_coord[1] + 1]
    directions = directions_map[map[starting_coord[0]][starting_coord[1] + 1]]['E']
    # corners.append([starting_coord[0], starting_coord[1] + 1])

elif directions_map[map[starting_coord[0] + 1][starting_coord[1]]].get('S', None) is not None:
    # position = [starting_coord[0] + 1, starting_coord[1]]
    directions = directions_map[map[starting_coord[0] + 1][starting_coord[1]]]['S']

elif directions_map[map[starting_coord[0]][starting_coord[1] - 1]].get('W', None) is not None:
    # position = [starting_coord[0], starting_coord[1] - 1]
    directions = directions_map[map[starting_coord[0]][starting_coord[1] - 1]]['W']

steps = 1
while True:
    if directions == 'N':
        position = [position[0] - 1, position[1]]
    elif directions == 'E':
        position = [position[0], position[1] + 1]
    elif directions == 'S':
        position = [position[0] + 1, position[1]]
    elif directions == 'W':
        position = [position[0], position[1] - 1]
    steps += 1
    if map[position[0]][position[1]] == 'S':
        break
    old_direction = directions
    directions = directions_map[map[position[0]][position[1]]][directions]
    if directions != old_direction:
        corners.append(position)
print(corners)

answer = []
for i in range(len(corners) - 1):
    y1 = corners[i][0]
    x1 = corners[i][1]
    y2 = corners[i+1][0]
    x2 = corners[i+1][1]
    answer.append(x1*y2 - x2*y1)
print(answer)
print(sum(answer)/2)
