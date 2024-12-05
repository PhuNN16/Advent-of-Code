from collections import defaultdict

ls = open('2024/inputs/day5.txt', 'r').read()


# part 1
sect1, sect2 = ls.split("\n\n")
# print(sect1)
section1 = sect1.split("\n")
ordering = defaultdict(list)
for i in section1:
    # print(i)
    l, r = i.split("|")
    ordering[l].append(r)

section2 = sect2.split("\n")
correct = []
for j in section2:
    # print(j)
    seen = []
    num_list = j.split(",")
    for k in num_list:
        seen.append(k)
        for l in ordering[k]:
            if l in seen:
                break
        else:
            continue
        break
    else:
        correct.append(num_list[len(num_list) // 2])


# print(correct)
total = 0
for i in correct:
    total += int(i)
print(total)


# part 2
incorrect = []
for j in section2:
    # print(j)
    seen = []
    num_list = j.split(",")
    for k in num_list:
        seen.append(k)
        for l in ordering[k]:
            if l in seen:
                incorrect.append(num_list)
                break
        else:
            continue
        break

# print(incorrect)
for m in incorrect:
    for n in m:
        for o in ordering[n]:
            if o in m[:m.index(n)]:
                m.pop(m.index(n))
                m.insert(m.index(o), n)

# print(incorrect)
total = 0
for f in incorrect:
    midnum = int(f[len(f) // 2])
    total += midnum
print(total)


