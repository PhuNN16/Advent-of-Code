ls = open('2023/inputs/day19input.txt', 'r').read().split('\n\n')

'''Part 1'''
workflows = ls[0].split()
dictionary = {}
for line in workflows:
    name, rule = line[:-1].split('{')
    dictionary[name] = rule
# print(dictionary)

parts = ls[1].strip().split()
count = 0
list_count = []
for part in parts:
    x, m, a, s = [x.split('=')[-1] for x in part[1:-1].split(',')]
    letters = {'x': x, 'm': m, 'a': a, 's': s}
    workflowName = 'in'
    while True:
        if workflowName == 'A' or workflowName == 'R':
            break
        instructions = dictionary[workflowName].split(',')
        for instr in instructions[:-1]: #dont include the last instruction because it is always accepted
            condition, destination = instr.split(':')
            if condition[1] == '>':
                if int(letters[condition[0]]) > int(condition[2:]):
                    workflowName = destination
                    break
            elif condition[1] == '<':
                if int(letters[condition[0]]) < int(condition[2:]):
                    workflowName = destination
                    break
        else:
            workflowName = instructions[-1]
    
    if workflowName == 'A':
        count = int(x) + int(m) + int(a) + int(s)
        list_count.append(count)
print(sum(list_count))


'''Part 2'''