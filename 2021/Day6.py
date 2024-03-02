input = [2,5,5,3,2,2,5,1,4,5,2,1,5,5,1,2,3,3,4,1,4,1,4,4,2,1,5,5,3,5,4,3,4,1,5,4,1,5,5,5,4,3,1,2,1,5,1,4,4,1,4,1,3,1,1,1,3,1,1,2,
         1,3,1,1,1,2,3,5,5,3,2,3,3,2,2,1,3,1,3,1,5,5,1,2,3,2,1,1,2,1,2,1,2,2,1,3,5,4,3,3,2,2,3,1,4,2,2,1,3,4,5,4,2,5,4,1,2,1,3,5,
         3,3,5,4,1,1,5,2,4,4,1,2,2,5,5,3,1,2,4,3,3,1,4,2,5,1,5,1,2,1,1,1,1,3,5,5,1,5,5,1,2,2,1,2,1,2,1,2,1,4,5,1,2,4,3,3,3,1,5,3,
         2,2,1,4,2,4,2,3,2,5,1,5,1,1,1,3,1,1,3,5,4,2,5,3,2,2,1,4,5,1,3,2,5,1,2,1,4,1,5,5,1,2,2,1,2,4,5,3,3,1,4,4,3,1,4,2,4,4,3,4,
         1,4,5,3,1,4,2,2,3,4,4,4,1,4,3,1,3,4,5,1,5,4,4,4,5,5,5,2,1,3,4,3,2,5,3,1,3,2,2,3,1,4,5,3,5,5,3,2,3,1,2,5,2,1,3,1,1,1,5,1]
# input = [3, 4, 3, 1 , 2]
# input = [3]

def lanternfish(input):
    # for days in range(80):
    #     # print(f'days {days}')
    #     for fish in range(len(input)):
    #         input[fish] -= 1
    #         if input[fish] == -1:
    #             input[fish] = 6
    #             input.append(8)

    # num = 300
    # for i in range(len(input)):
    #     new_fish_born = (80 + input[i]) // 7
    #     # print(new_fish_born)
    #     num += new_fish_born
    #     for j in range(new_fish_born):
    #         new_new_fish_born = ((73 - 7*j) - input[i]) // 7
    #         num += new_new_fish_born
    # print(num)

    # dict = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
    list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    num_of_fish = 0
    for i in range(len(input)):
        list[input[i]] += 1
        num_of_fish += 1
    print(list)
    for i in range(256):
        temp = list[0]
        for i in range(len(list) - 1):
            list[i] = list[i + 1]
        list[6] += temp
        list[8] = temp
        num_of_fish += temp
    # for i in list:
    #     num_of_fish += i
    print(num_of_fish)


lanternfish(input)
# print(input)
# print(len(input))