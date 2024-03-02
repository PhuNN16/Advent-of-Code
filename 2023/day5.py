import time
import math
ls = open('2023/inputs/day5input.txt', 'r').read().strip().split('\n\n')

'''Part 1'''
print('Part 1 answer:')
s = ls[0].split(':')[1].split()

mapped = []
for block in ls[1:]:
    line = block.split('\n')[1:]
    list = [x.split() for x in line]
    mapped.append(list)

list_of_loc = []
for seed in s:
    temp = int(seed)
    for chunk in mapped:
        for instr in chunk:
            if temp >= int(instr[1]) and temp < int(instr[1]) + int(instr[2]):
                temp = int(instr[0]) + (temp - int(instr[1]))
                break 
    list_of_loc.append(temp)
print(min(list_of_loc))


'''Part 2'''
s = ls[0].split(':')[1].split()

s2 = []
for abg in range(len(s)):
    if abg % 2 == 0:
        s2.append([int(s[abg]), int(s[abg+1])])

mapped = []
for block in ls[1:]:
    line = block.split('\n')[1:]
    list = [x.split() for x in line]
    mapped.append(list)

'''Method 1'''
print('loc to seed binary search  (also aiden):')
start_time = time.time()
# #this is going backwards
list_of_loc = []
start = 0
end = 100
incr = 10
old_var = None
# 78770000, 78775060, 1
tag = True
while tag:
    int_incr = int(incr)
    for location in range(start, end, int_incr):
        # print(location)
        loc = location
        temp = int(location)
        for chunk in mapped[::-1]:
            for instr in chunk:
                if temp >= int(instr[0]) and temp < int(instr[0]) + int(instr[2]):
                    temp = int(instr[1]) + (temp - int(instr[0]))
                    break 
        for sr in s2:
            if temp >= sr[0] and temp <= sr[0] + sr[1]:
                end = loc
                start = int(end - incr)
                incr = incr/10
                if incr < 1:
                    tag = False
                    break
                break
        else:
            continue
        break
    else:
        start = end
        end *= 10
        incr *= 10
print(loc)
elapsed_time = time.time() - start_time
print(f'took {elapsed_time} seconds')

'''Method 2'''
print('Aiden splitting list method: ')
start_time2 = time.time()
seedranges = [x for x in s2]
# print(seedranges)
for chunk in mapped:
    temp = []
    for instruction in chunk:
        outside = []
        for sr in seedranges:
            start_seedrange = sr[0]
            end_seedrange = sr[0] + sr[1] - 1
            start_source = int(instruction[1])
            start_destination = int(instruction[0])
            length = int(instruction[2])
            if start_seedrange >= start_source and end_seedrange <= start_source + length - 1:
                # If seed range is inside transitional range
                start_seedrange = (start_seedrange - start_source) + start_destination
                seedrange_length = sr[1]
                temp.append([start_seedrange, seedrange_length])
                
            elif start_seedrange < start_source and start_source <= end_seedrange <= start_source + length - 1:
                # If seed range is only partially in transitional range (leaking out the left)
                # we have to store [start of seed range, length of seed range]
                left_seed_start = start_seedrange
                left_seed_length = start_source - start_seedrange
                right_seed_start = start_destination
                right_seed_length = end_seedrange - start_source + 1
                outside.append([left_seed_start, left_seed_length])
                temp.append([right_seed_start, right_seed_length])
                
            elif start_source + length - 1 >= start_seedrange >= start_source and end_seedrange > start_source + length - 1:
                # If seed range is only partially in transitional range (leaking out the right)
                left_seed_start = (start_seedrange - start_source) + start_destination
                left_seed_length = (start_source + length - 1) - start_seedrange
                right_seed_start = start_source + length
                right_seed_length = end_seedrange - (start_source + length - 1)
                temp.append([left_seed_start, left_seed_length])
                outside.append([right_seed_start, right_seed_length])
                
            elif start_seedrange < start_source and end_seedrange > start_source + length - 1:
                # If seed range is larger than transitional range and fully encapsulates it
                left_seed_start = start_seedrange
                left_seed_length = start_source - start_seedrange # you dont include the left seeds
                middle_seed_start = start_destination
                middle_seed_length = length #this is the whole transition range
                right_seed_start = start_source + length #dont need +1 because the map range does not inclue the last number
                right_seed_length = end_seedrange - (start_source + length - 1)
                outside.append([left_seed_start, left_seed_length])
                temp.append([middle_seed_start, middle_seed_length])
                outside.append([right_seed_start, right_seed_length])
                
            elif start_seedrange > start_source + length -1 or end_seedrange < start_source:
                # If seed range does not intersect with transitional range
                #there are still other instructions to check so we cant just append yet
                outside.append(sr)
            seedranges = outside    
        # print(temp)
    seedranges = outside + temp
    # print(seedranges)
    # if mapped[2] == chunk:
    #     break
small = [x[0] for x in seedranges]
print(min(small))
elapsed_time = time.time() - start_time2
print(f'took {elapsed_time} seconds')
