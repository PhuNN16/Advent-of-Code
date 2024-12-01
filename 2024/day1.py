from collections import defaultdict

ls = open('2024/inputs/day1.txt', 'r').read().split('\n')[:-1]

# part 1
left_list = []
right_list = []
for i in ls:
    left_num, right_num = i.split()
    left_list.append(int(left_num))
    right_list.append(int(right_num))
left_list.sort()
right_list.sort()

sum = 0
for i in range(len(left_list)):
    sum += abs(left_list[i] - right_list[i])

print(sum)

#part 2
left_list = []
right_list = defaultdict(int)
for i in ls:
    left_num, right_num = i.split()
    left_list.append(int(left_num))
    right_list[int(right_num)] += 1

sum = 0
for i in range(len(left_list)):
    sum += left_list[i] * right_list[left_list[i]]

print(sum)