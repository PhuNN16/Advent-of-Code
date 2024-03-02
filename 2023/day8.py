ls = open('2023/inputs/day8input.txt', 'r').read().split('\n')[:-1]
import math

'''Part 1'''
# instruction  = ls[0]

# dict = {}
# for line in ls[2:]:
#     line_split = line.split(' = ')
#     key = line_split[0]
#     movement = line_split[1].split('(')[1].split(')')
#     go_left = movement[0].split(', ')[0]
#     go_right = movement[0].split(', ')[1]
#     dict[key] = {'L': go_left, 'R': go_right}
# # print(dict)
# current = 'AAA'
# # print(current)
# steps = 0
# while current != 'ZZZ':
#     for instr in instruction:
#         current = dict[current][instr]
#         steps += 1
#         if steps % 1000 == 0:
#             print(steps)
#     if current == 'ZZZ':
#         break

# print(current)
# print(steps)




'''Part 2'''
instruction  = ls[0]

dict = {}
node = []
for line in ls[2:]:
    line_split = line.split(' = ')
    key = line_split[0]
    if key[-1] == 'A':
        node.append(key)
    movement = line_split[1].split('(')[1].split(')')
    go_left = movement[0].split(', ')[0]
    go_right = movement[0].split(', ')[1]
    dict[key] = {'L': go_left, 'R': go_right}
# print(dict)
# print(node)
# print(current)
steps = 0
list_of_steps = {}
while True:
    # print(node)
    for instr in instruction:
        num_z = 0
        for current in range(len(node)):
            node[current] = dict[node[current]][instr]
            if node[current][-1] == 'Z' and list_of_steps.get(node[current], None) is None:
                list_of_steps[node[current]] = steps + 1
        steps += 1
        if len(list_of_steps) == len(node):
                break
        if steps % 1000000 == 0:
            print(steps)
        # if num_z == len(node):
        #     break
    else:
        continue
    break

def LCM(a, b): 
    greater = max(a, b) 
    smallest = min(a, b) 
    for i in range(greater, a*b+1, greater): 
        if i % smallest == 0: 
            return i 
        
print(math.lcm(*list_of_steps.values()))


lcm = 1
lcm2 = 1
for i in list_of_steps.values():
    lcm = lcm*i//math.gcd(lcm, i)
    lcm2 = LCM(lcm2, i)
print(lcm)
print(lcm2)