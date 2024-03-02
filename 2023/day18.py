import numpy as np
ls = open('2023/inputs/day18sample.txt', 'r').read().split('\n')[:-1]

'''Part 1'''

def shoelace(x_y): #Taken from StackOverflow to learn about
    x_y = np.array(x_y)
    x_y = x_y.reshape(-1,2)

    x = x_y[:,0]
    y = x_y[:,1]

    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    area = .5*np.absolute(S1 - S2)

    return area


point = [0, 0]
dugged = []
y = []
x = []
left_border = 0
right_border = 0
down_border = 0
up_border = 0
for line in ls:
    direction, meters, color = line.split()
    for steps in range(int(meters)):
        new_point = [point[0], point[1]]
        if direction == 'U':
            new_point[0] -= 1
        elif direction == 'D':
            new_point[0] += 1
        elif direction == 'L':
            new_point[1] -= 1
        elif direction == 'R':
            new_point[1] += 1
        dugged.append(new_point)
        point = new_point

        if new_point[0] < up_border:
            up_border -= 1
        elif new_point[0] > down_border:
            down_border += 1
        
        if new_point[1] < left_border:
            left_border -= 1
        elif new_point[1] > right_border:
            right_border += 1
    
    y.append(new_point[0])
    x.append(new_point[1])

print(dugged)
print(len(dugged))
print(left_border, right_border, up_border, down_border)

# digging = -1
# height = abs(left_border) + right_border + 1
# length = down_border + abs(up_border) + 1
# for i in range(height):
#     for j in range(length):
#         if digging > 0:
#             dugged.append([i, j])
#         if [i, j] in dugged:
#             digging *= -1

# print(dugged)
# print(len(dugged))

'''part 2'''