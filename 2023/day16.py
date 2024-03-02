import time
ls = open('2023/inputs/day16input.txt', 'r').read().split('\n')[:-1]

'''Part 1'''
# cavern = [list(a) for a in ls]
# # print(cavern)

# list_of_laser = [[0, -1, 'E']]
# direction = {'/' : {'N' : 'E', 'W' : 'S', 'S' : 'W', 'E' : 'N'}, 
#              '\\' : {'N' : 'W', 'W' : 'N', 'S' : 'E', 'E' : 'S'}, 
#              '|' : {'N' : 'N', 'S' : 'S', 'E' : 'NS', 'W' : 'NS'}, 
#              '-' : {'N' : 'WE', 'S' : 'WE', 'E' : 'E', 'W' : 'W'}, 
#              '.' : {'N' : 'N', 'W' : 'W', 'S' : 'S', 'E' : 'E'}}
# energized_tiles = {}
# loop_check = {}
# while list_of_laser:
#     for laser in list_of_laser:
#         energized_tiles[(laser[0], laser[1])] = 1
#         if (laser[0], laser[1], laser[2]) not in loop_check:
#             loop_check[(laser[0], laser[1], laser[2])] = 1
#         else:
#             list_of_laser.remove(laser)
#             continue

#         if laser[2] == 'N':
#             laser[0] -= 1
#             if laser[0] < 0 or laser[0] >= len(cavern) or laser[1] < 0 or laser[1] >= len(cavern[0]):
#                 list_of_laser.remove(laser)
#                 continue
#             laser[2] = direction[cavern[laser[0]][laser[1]]][laser[2]]
#         elif laser[2] == 'E':
#             laser[1] += 1
#             if laser[0] < 0 or laser[0] >= len(cavern) or laser[1] < 0 or laser[1] >= len(cavern[0]):
#                 list_of_laser.remove(laser)
#                 continue
#             laser[2] = direction[cavern[laser[0]][laser[1]]][laser[2]]
#         elif laser[2] == 'S':
#             laser[0] += 1
#             if laser[0] < 0 or laser[0] >= len(cavern) or laser[1] < 0 or laser[1] >= len(cavern[0]):
#                 list_of_laser.remove(laser)
#                 continue
#             laser[2] = direction[cavern[laser[0]][laser[1]]][laser[2]]
#         elif laser[2] == 'W':
#             laser[1] -= 1
#             if laser[0] < 0 or laser[0] >= len(cavern) or laser[1] < 0 or laser[1] >= len(cavern[0]):
#                 list_of_laser.remove(laser)
#                 continue
#             laser[2] = direction[cavern[laser[0]][laser[1]]][laser[2]]
#         elif laser[2] == 'NS':
#             if laser[0]+1 >= 0 and laser[0]+1 < len(cavern) and laser[1] >= 0 and laser[1] < len(cavern[0]):
#                 d1 = direction[cavern[laser[0]+1][laser[1]]]['S']
#                 list_of_laser.append([laser[0]+1, laser[1], d1]) #new laser
#             laser[0] -= 1
#             if laser[0] >= 0 and laser[0] < len(cavern) and laser[1] >= 0 and laser[1] < len(cavern[0]):
#                 laser[2] = direction[cavern[laser[0]][laser[1]]]['N']
#             else:
#                 list_of_laser.remove(laser)
#                 # continue
#         elif laser[2] == 'WE':
#             if laser[0] >= 0 and laser[0] < len(cavern) and laser[1]-1 >= 0 and laser[1]-1 < len(cavern[0]):
#                 d1 = direction[cavern[laser[0]][laser[1]-1]]['W']
#                 list_of_laser.append([laser[0], laser[1]-1, d1])
#             laser[1] += 1
#             if laser[0] >= 0 and laser[0] < len(cavern) and laser[1] >= 0 and laser[1] < len(cavern[0]):
#                 laser[2] = direction[cavern[laser[0]][laser[1]]]['E']
#             else:
#                 list_of_laser.remove(laser)
#                 # continue

# print(len(energized_tiles)-1)



'''Part 2'''
start_time = time.time()
cavern = [list(a) for a in ls]
# print(cavern)

direction = {'/' : {'N' : 'E', 'W' : 'S', 'S' : 'W', 'E' : 'N'}, 
             '\\' : {'N' : 'W', 'W' : 'N', 'S' : 'E', 'E' : 'S'}, 
             '|' : {'N' : 'N', 'S' : 'S', 'E' : 'NS', 'W' : 'NS'}, 
             '-' : {'N' : 'WE', 'S' : 'WE', 'E' : 'E', 'W' : 'W'}, 
             '.' : {'N' : 'N', 'W' : 'W', 'S' : 'S', 'E' : 'E'}}
list_of_et = []
for i in range(4):
    for j in range(len(cavern)):
        energized_tiles = {}
        loop_check = {}
        if i == 0:
            list_of_laser = [[j, -1, 'E']]
        if i == 1:
            list_of_laser = [[-1, j, 'S']]
        if i == 2:
            list_of_laser = [[j, len(cavern[0]) + 1, 'W']]
        if i  == 3:
            list_of_laser = [[len(cavern) + 1, j, 'N']]

        while list_of_laser:
            for laser in list_of_laser:
                energized_tiles[(laser[0], laser[1])] = 1
                # if (laser[0], laser[1], laser[2]) not in loop_check:
                    # loop_check[(laser[0], laser[1], laser[2])] = 1
                # else:
                #     list_of_laser.remove(laser)
                #     continue
                if (laser[0], laser[1], laser[2]) in loop_check:
                    list_of_laser.remove(laser)
                    continue

                if laser[2] == 'N':
                    laser[0] -= 1
                    if laser[0] < 0 or laser[0] >= len(cavern) or laser[1] < 0 or laser[1] >= len(cavern[0]):
                        list_of_laser.remove(laser)
                        continue
                    laser[2] = direction[cavern[laser[0]][laser[1]]][laser[2]]
                elif laser[2] == 'E':
                    laser[1] += 1
                    if laser[0] < 0 or laser[0] >= len(cavern) or laser[1] < 0 or laser[1] >= len(cavern[0]):
                        list_of_laser.remove(laser)
                        continue
                    laser[2] = direction[cavern[laser[0]][laser[1]]][laser[2]]
                elif laser[2] == 'S':
                    laser[0] += 1
                    if laser[0] < 0 or laser[0] >= len(cavern) or laser[1] < 0 or laser[1] >= len(cavern[0]):
                        list_of_laser.remove(laser)
                        continue
                    laser[2] = direction[cavern[laser[0]][laser[1]]][laser[2]]
                elif laser[2] == 'W':
                    laser[1] -= 1
                    if laser[0] < 0 or laser[0] >= len(cavern) or laser[1] < 0 or laser[1] >= len(cavern[0]):
                        list_of_laser.remove(laser)
                        continue
                    laser[2] = direction[cavern[laser[0]][laser[1]]][laser[2]]
                elif laser[2] == 'NS':
                    loop_check[(laser[0], laser[1], laser[2])] = 1
                    if laser[0]+1 >= 0 and laser[0]+1 < len(cavern) and laser[1] >= 0 and laser[1] < len(cavern[0]):
                        d1 = direction[cavern[laser[0]+1][laser[1]]]['S']
                        list_of_laser.append([laser[0]+1, laser[1], d1]) #new laser
                    laser[0] -= 1
                    if laser[0] >= 0 and laser[0] < len(cavern) and laser[1] >= 0 and laser[1] < len(cavern[0]):
                        laser[2] = direction[cavern[laser[0]][laser[1]]]['N']
                    else:
                        list_of_laser.remove(laser)
                        # continue
                elif laser[2] == 'WE':
                    loop_check[(laser[0], laser[1], laser[2])] = 1
                    if laser[0] >= 0 and laser[0] < len(cavern) and laser[1]-1 >= 0 and laser[1]-1 < len(cavern[0]):
                        d1 = direction[cavern[laser[0]][laser[1]-1]]['W']
                        list_of_laser.append([laser[0], laser[1]-1, d1])
                    laser[1] += 1
                    if laser[0] >= 0 and laser[0] < len(cavern) and laser[1] >= 0 and laser[1] < len(cavern[0]):
                        laser[2] = direction[cavern[laser[0]][laser[1]]]['E']
                    else:
                        list_of_laser.remove(laser)
                        # continue
        list_of_et.append(len(energized_tiles)-1)
        # print(len(energized_tiles)-1)
print(max(list_of_et))
print(time.time() - start_time)