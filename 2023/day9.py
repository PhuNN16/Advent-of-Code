ls = open('2023/inputs/day9sample.txt', 'r').read().split('\n')[:-1]

'''Part 1'''
history = []
for line in ls: #can solve part 2 by adding [::-1] after line.split()
    history.append(line.split())

tag = True
list_of_answer = []
for hist in history:
    last_num = []
    last_num.append(int(hist[-1]))
    while tag:
        temp = []
        for idx in range(1, len(hist)):
            temp.append(int(hist[idx]) - int(hist[idx - 1]))
        last_num.append(temp[-1])
        hist = temp
        for i in temp:
            if i != 0:
                break
        else:
            break
    last_num = last_num[::-1]
    answer = last_num[0] + last_num[1]
    for i in range(2, len(last_num)):
        answer += last_num[i]
    list_of_answer.append(answer)
# print(list_of_answer)
print(sum(list_of_answer))



'''Part 2'''
history = []
for line in ls:
    history.append(line.split())

list_of_answer = []
for hist in history:
    first_num = []
    first_num.append(int(hist[0]))
    while True:
        temp = []
        for idx in range(1, len(hist)):
            temp.append(int(hist[idx]) - int(hist[idx - 1]))
        first_num.append(temp[0])
        hist = temp
        for i in temp:
            if i != 0:
                break
        else:
            break
    first_num = first_num[::-1]
    # print(first_num)
    answer = first_num[1]
    for i in range(2, len(first_num)):
        answer = first_num[i] - answer
    list_of_answer.append(answer)
# print(list_of_answer)
print(sum(list_of_answer))