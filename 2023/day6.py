ls = open('2023/inputs/day6input.txt', 'r').read().split('\n')[:-1]
import math

'''Part 1'''
time = ls[0].split(':')[1].split()
distance = ls[1].split(':')[1].split()

answer = 1
for race in range(len(time)):
    num_of_wins = 0
    for t in range(int(time[race])):
        if (int(time[race]) - t) * t > int(distance[race]):
            num_of_wins += 1
    answer *= num_of_wins
print(answer)



'''Part 2 method 1'''
time = ls[0].split(':')[1].split()
distance = ls[1].split(':')[1].split()

new_time = ''
new_distant = ''
for i in range(len(time)):
    new_time += time[i]
    new_distant += distance[i]
new_time = int(new_time)
new_distant = int(new_distant)

start = math.ceil(new_distant / new_time)
for i in range(start, new_time):
    if (new_time - i) * i > new_distant:
        start = i
        break
print(new_time - 2*start + 1)



'''Part 2 method 2'''
discriminant = math.sqrt(new_time ** 2 - 4*new_distant)
x1 = math.ceil((-new_time + discriminant) / -2)
# x2 = math.floor((-new_time - discriminant) / -2)
print(new_time - (2*x1) + 1)

print(new_time - (2*math.ceil((-new_time + math.sqrt(new_time ** 2 - 4*new_distant)) / -2)) + 1)