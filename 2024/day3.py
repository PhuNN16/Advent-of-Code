import re

ls = open('2024/inputs/day3sample.txt', 'r').read()

#part1
total = 0
f = re.findall("mul\(\d+,\d+\)", ls)
# print(f)
for j in f:
    num1, num2 = j[4:-1].split(",")
    total += int(num1) * int(num2)
print(total)

#part2

def basically_part_1(ls, total):
    f = re.findall("mul\(\d+,\d+\)", ls)
    # print(f)
    for j in f:
        num1, num2 = j[4:-1].split(",")
        total += int(num1) * int(num2)
    return total

total = 0

while True:
    index = ls.find("don't()")
    if index == -1:
        #If we ran out of don't() the index should be len(ls) in case there is a mul() right at the end
        index = len(ls) 
    total = basically_part_1(ls[:index], total)
    # Already calculated mul() are removed so we don't recalculate
    ls = ls[index:]
    if index == len(ls):
        # This is called once we ran out of don't() which means we ended on do() so calculate the rest before breaking
        break
    index2 = ls.find("do()")
    # print(index2)
    if index2 == -1:
        # This is called when we ran out of do() which means we ended on don't() and dont need to calculate the rest
        break
    # Move the string forward to where we need to start calculating
    ls = ls[index2+4:]
print(total)