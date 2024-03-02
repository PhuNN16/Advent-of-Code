from copy import deepcopy
import time
ls = open('2023/inputs/day14input.txt', 'r').read().split('\n')[:-1]

'''Part 1'''
round_rocks = []
blocks = {}
for rows, value_x in enumerate(ls):
    for columns, value_y in enumerate(value_x):
        if value_y == 'O':
            round_rocks.append([rows, columns])
        elif value_y == '#':
            if blocks.get(columns, None) is None:
                blocks[columns] = [rows]
            else:
                blocks[columns].append(rows)
# print(round_rocks)
# print(blocks)
    
for idx_rr, roundrock in enumerate(round_rocks):
    if roundrock[1] not in blocks:
        temp = [0, roundrock[1]]
        blocks[roundrock[1]] = [0]
    else:
        for i in blocks[roundrock[1]][::-1]:
            if roundrock[0] > i:
                index_i = blocks[roundrock[1]].index(i)
                temp = [i + 1, roundrock[1]]
                blocks[roundrock[1]][index_i] = i + 1
                break
        else:
            temp = [0, roundrock[1]]
            blocks[roundrock[1]].insert(0, 0)
    round_rocks[idx_rr] = temp

    
# print(round_rocks)

load = 0
for rock in round_rocks:
    load += len(ls) - rock[0]
print(load)

'''Part 2'''
start_time = time.time()

def rock_go_up(platform):
    for rows in range(len(platform)):
        platform[rows] = list(platform[rows])

    for columns in range(len(platform[0])):
        block = -1
        for rows in range(len(platform)):
            value = platform[rows][columns]
            if value == '#':
                block = rows
            elif value == 'O':
                platform[rows][columns] = '.'
                block += 1
                platform[block][columns] = 'O'


map = []
for rows, value_x in enumerate(ls):
    temp = []
    for columns, value_y in enumerate(value_x):
        temp.append(value_y)
    map.append(temp)

repeat_maps = []
repeat = []
for cycles in range(1000000000): #found the start of the cycle at index 138
    for j in range(4):
        round_rocks = rock_go_up(map)
        map = list(zip(*map[::-1]))

    copy_map = deepcopy(map)
    if cycles == 0:
        repeat_maps.append(copy_map)
    for m in repeat_maps:
        if cycles == 0:
            continue
        if m == map:
            loop_start = repeat_maps.index(map)
            break
    else:
        if cycles == 0:
            continue
        repeat_maps.append(copy_map)
        continue
    break

# print(loop_start)
for asd in range(len(repeat_maps)):
    if asd < loop_start:
        repeat_maps.pop(0)
    else:
        break
map_idx = (1000000000 - (loop_start + 1)) % len(repeat_maps)
map = repeat_maps[map_idx]

load = 0
for rows, value_x in enumerate(map):
    for columns, value_y in enumerate(value_x):
        if value_y == 'O':
            load += len(map) - rows
print(load)
print(time.time() - start_time)