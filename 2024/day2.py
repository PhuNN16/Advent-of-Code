from collections import defaultdict

ls = open('2024/inputs/day2.txt', 'r').read().split('\n')[:-1]

# part 1

# change = ''
# num_safe = 0
# for report in ls:
#     levels = report.split()
#     c = int(levels[0]) - int(levels[1])
#     if c > 0:
#         change = "d"
#     elif c < 0:
#         change = "i"
#     else:
#         continue

#     # print(change)
#     for i in range(len(levels) - 1):
#         new_c = int(levels[i]) - int(levels[i+1])
#         if new_c > 3 or new_c < -3:
#             break

#         if new_c > 0:
#             ch = "d"
#         elif new_c < 0:
#             ch = "i"
#         else:
#             ch = "fail"
        
#         # print(ch)
#         if ch != change:
#             break

#     else:
#         num_safe += 1

# print(num_safe)


# part 2
def basically_part_1(levels):
    c = int(levels[0]) - int(levels[1])
    change = ""
    if c > 0:
        change = "d"
    elif c < 0:
        change = "i"
    
    # print(change)
    for i in range(len(levels) - 1):
        new_c = int(levels[i]) - int(levels[i+1])
        if new_c > 3 or new_c < -3:
            return False

        if new_c > 0:
            ch = "d"
        elif new_c < 0:
            ch = "i"
        else:
            ch = "fail"
        
        # print(ch)
        if ch != change:
            return False

    else:
        return True


num_safe = 0
for report in ls:
    levelss = report.split()
    for i in range(len(levelss)):
        new_list = levelss[:i] + levelss[i+1:]
        result = basically_part_1(new_list)
        if result:
            num_safe += 1
            break

print(num_safe)
