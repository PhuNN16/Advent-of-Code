ls = open('2023/inputs/day2input.txt', 'r').read().split('\n')[:-1]
from functools import reduce

# ls = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
# 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
# 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
# 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
# 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

'''Part 1'''
color = {'red': 12, 'green': 13, 'blue': 14}
sum = 0
for line in ls:
    split_line = line.split(':')
    game_id = int(split_line[0].split(' ')[1])
    sets = split_line[1].split(';')
    for rolls in sets:
        dices = rolls.split(',')
        for cube in dices:
            penis = cube.split(' ')
            if int(penis[1]) > color.get(penis[2]):
                break
        else:
            continue
        break
    else:
        sum += game_id
print(sum)
    
    


'''Part 2'''
sum = 0
for line in ls:
    color = {'red': 0, 'green': 0, 'blue': 0}
    split_line = line.split(':')
    sets = split_line[1].split(';')
    for rolls in sets:
        dices = rolls.split(',')
        for cube in dices:
            penis = cube.split(' ')
            if int(penis[1]) > color.get(penis[2]):
                color[penis[2]] = int(penis[1])
    powerset = 1  
    for i in color:
        powerset *= color[i]
    sum += powerset

print(sum)