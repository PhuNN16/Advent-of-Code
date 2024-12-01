import numpy as np
import math
ls = open('2023/inputs/day18sample.txt', 'r').read().split('\n')[:-1]



def shoelace_formula(coords):
    area = 0
    for i in range(len(coords) - 1, -1, -1):
        num1 = coords[i][0] * coords[(i+1) % len(coords)][1]
        num2 = coords[i][1] * coords[(i+1) % len(coords)][0]
        # print(num1, num2)
        area += num1 - num2
    return abs(area) / 2 


'''Part 1''' #UNFINISHED

directions = {'R': [1, 0], 'D': [0, -1], 'L':[-1, 0], 'U': [0, 1]}
coord = [0, 0]
list_coord = []
idx = 0
for i in ls:
    # if idx == 3:
    #     break
    idx += 1
    dir, dist, color = i.split()
    dist = int(dist)
    for i in range(dist):
        coord = [coord[0] + directions[dir][0], coord[1] + directions[dir][1]]

    # new_vector = [directions[dir][0] * dist, directions[dir][1] * dist]
    # coord = [x + y for x, y in zip(coord, new_vector)]

    list_coord.append(coord)
print(list_coord)
print(shoelace_formula(list_coord))

'''part 2'''