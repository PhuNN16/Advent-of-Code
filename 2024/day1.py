import sys
# Note to self: use python3 day#.py < inputs/day#.txt when using sys.stdin
from collections import defaultdict

ls = open('2024/inputs/day1.txt', 'r').read().split('\n')[:-1]

# part 1
left_list = []
right_list = []
for i in ls:
# for i in sys.stdin:
    left_num, right_num = i.split()
    left_list.append(int(left_num))
    right_list.append(int(right_num))
left_list.sort()
right_list.sort()

ans = 0
for i in range(len(left_list)):
    ans += abs(left_list[i] - right_list[i])
print(ans)

# One-liner solution to add all the numbers
ans1 = sum([abs(x - y) for x, y in zip(left_list, right_list)])
print(ans1)

#part 2
# left_list = []
# right_list = defaultdict(int)
# for i in ls:
#     left_num, right_num = i.split()
#     left_list.append(int(left_num))
#     right_list[int(right_num)] += 1

# ans = 0
# for i in range(len(left_list)):
#     ans += left_list[i] * right_list[left_list[i]]

# print(ans)

