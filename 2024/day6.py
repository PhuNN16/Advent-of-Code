import numpy as np

ls = open('2024/inputs/day6sample.txt', 'r').read().split('\n')[:-1]

g = []
for i in range(len(ls)):
    row = []
    for j in range(len(ls[0])):
        if ls[i][j] == '^':
            start = [i, j]
        row.append(ls[i][j])
    g.append(row)


#part 1
# curr = start
# front = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
# dir = 0
# path = [curr]
# while True:
#     next = [a + b for a, b in zip(curr, front[dir])]
#     if next[0] < 0 or next[1] < 0 or next[0] >= len(g) or next[1] >= len(g):
#         break
#     elif g[next[0]][next[1]] == '#':
#         dir = (dir + 1) % 4
#         continue
#     curr = next
#     if curr not in path:
#         path.append(curr)
# print(len(path))


# part 2

def modified_part_1(start, graph):
    c = start
    direction = 0
    front = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
    p = [(c, direction)]
    while True:
        n = [a + b for a, b in zip(c, front[direction])]
        if n[0] < 0 or n[1] < 0 or n[0] >= len(g) or n[1] >= len(g):
            return False
        elif graph[n[0]][n[1]] == '#':
            direction = (direction + 1) % 4
            continue
        c = n
        if c in p:
            return True
        p.append((c, direction))

total_position = 0
for row in range(len(g)):
    for column in range(len(g[0])):
        if g[row][column] == '#' or g[row][column] == '^':
            continue
        g[row][column] = '#'
        res = modified_part_1(start, g)
        print((row, column), res)
        if res:
            total_position += 1
        g[row][column] = '.'

print(total_position)
        
