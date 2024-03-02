ls = open('2023/inputs/day4input.txt', 'r').read().split('\n')[:-1]

'''Part 1'''
points = 0
for line in ls:
    n = 0
    scratch_card = line.split(':')[1]
    split_card = scratch_card.split('|')
    winning_number = split_card[0].split()
    numbers = split_card[1].split()
    for num in numbers:
        if num in winning_number:
            n += 1
    points += int(2**(n-1))
print(points)



'''Part 2 Method 1'''
dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
num_card = 0
for line in ls:
    num_card += 1
    n = 0
    scratch_card = line.split(':')[1]
    split_card = scratch_card.split('|')
    winning_number = split_card[0].split()
    numbers = split_card[1].split()
    for num in numbers:
        if num in winning_number:
            n += 1
    for i in range(n):
        dict[i+1] += 1 + dict[0]
        num_card += 1 + dict[0]
    for key in range(len(dict) - 1):
        dict[key] = dict[key+1]
    dict[10] = 0
print(num_card)


'''Part 2 Method 2'''
dict = {}
for key in range(len(ls)):
    dict[key] = 1
num_card = 0
for key, line in enumerate(ls):
    n = 0
    scratch_card = line.split(':')[1]
    split_card = scratch_card.split('|')
    winning_number = split_card[0].split()
    numbers = split_card[1].split()
    for num in numbers:
        if num in winning_number:
            n += 1
    for i in range(n):
        if key+i+1 < len(ls):
            dict[key + i + 1] += dict[key]

# print(dict)
print(sum(dict.values()))