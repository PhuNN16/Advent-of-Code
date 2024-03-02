ls = open('2023/inputs/day13input.txt', 'r').read().split('\n\n')
ls[-1] = ls[-1][:-1]

'''Part 1'''
# Make a function that has 2 ptrs that try to find rows that are identical.
# Make the center variable equal to the row number of the first pointer + 1 (which is ptr2) (we add or multiply with that number)
# if a pattern isnt found in rows, flip the patterns and use the function on the columns (it became the new rows)
def find_reflection(patt, old_center):
    for rows in range(len(patt)):
        ptr1 = rows
        ptr2 = rows + 1
        if ptr1 < 0 or ptr2 > len(patt) - 1:
            return None
        if patt[ptr1] == patt[ptr2]:
            center = ptr2
            if center == old_center:
                continue
            while patt[ptr1] == patt[ptr2]:
                ptr1 -= 1
                ptr2 += 1
                if ptr1 < 0 or ptr2 > len(patt) - 1:
                    return center


patterns = []
count = 0
for chunk in ls:
    count += 1
    line = chunk.split('\n')
    patterns.append(line)
# print(patterns)

notes = []
for p in patterns:
    result = find_reflection(p, -1)
    if result is None:
        p = list(zip(*p[::-1]))
        result = find_reflection(p, -1)
        notes.append(result)
    else:
        notes.append(100 * result)
print(sum(notes))

'''Part 2''' #UNFINISHED
patterns = []
for chunk in ls:
    temp1 = []
    lines = chunk.split('\n')
    for line in lines:
        temp2 = []  
        for char in line:
            temp2.append(char)
        temp1.append(temp2)
    patterns.append(temp1)
# print(patterns)

switch = {
        '.': '#',
        '#': '.'
}

notes = []
for p in patterns:
    # p = list(p)
    # print(p)
    result = find_reflection(p, -1)
    if result is None:
        p = list(zip(*p[::-1]))
        result = find_reflection(p, -1)
        reflection = ['column', result]
        for turn in range(3): #reset orientation of p
            p = list(zip(*p[::-1]))
    else:
        reflection = ['row', 100 * result]
    
    for i in range(len(p)):
        for j in range(len(p[0])):
            p[i] = list(p[i])
            p[i][j] = switch[p[i][j]]
            if type(p[(i+1) % len(p)]) is tuple:
                p[i] = tuple(p[i])
            result = find_reflection(p, reflection)
            if result is None:
                p = list(zip(*p[::-1]))
                result = find_reflection(p, reflection)
                new_reflection = ['column', result]
                for turn in range(3): #reset orientation of p
                    p = list(zip(*p[::-1]))
            else:
                new_reflection = ['row', 100 * result]

            p[i] = list(p[i])
            p[i][j] = switch[p[i][j]]
            if type(p[(i+1) % len(p)]) is tuple:
                p[i] = tuple(p[i])

            if new_reflection != reflection and new_reflection[1] is not None:
                notes.append(new_reflection[1])
                break
        else:
            continue
        break
print(sum(notes)) #answer is too low?!?!?!?!?!!??? 