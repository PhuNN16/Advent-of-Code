ls = open('2024/inputs/day4.txt', 'r').read().split('\n')[:-1]

ws = []
for i in ls:
    r = []
    for j in i:
        r.append(j)
    ws.append(r)
# print(ws[0])

total = 0
for row in range(len(ws)):
    for column in range(len(ws[0])):
        string1 = ""
        string2 = ""
        string3 = ""
        string4 = ""
        if column + 3 < len(ws[0]):
            string1 = ws[row][column] + ws[row][column+1] + ws[row][column+2] + ws[row][column+3]
        if row + 3 < len(ws):
            string2 = ws[row][column] + ws[row+1][column] + ws[row+2][column] + ws[row+3][column]
        if column + 3 < len(ws[0]) and row + 3 < len(ws):
            string3 = ws[row][column] + ws[row+1][column+1] + ws[row+2][column+2] + ws[row+3][column+3]
        if column - 3 >= 0 and row + 3 < len(ws):
            string4 = ws[row][column] + ws[row+1][column-1] + ws[row+2][column-2] + ws[row+3][column-3]
        
        if string1 == "XMAS" or string1 == "SAMX":
            total += 1
        if string2 == "XMAS" or string2 == "SAMX":
            total += 1
        if string3 == "XMAS" or string3 == "SAMX":
            total += 1
        if string4 == "XMAS" or string4 == "SAMX":
            total += 1

        # print(string1, string2, string3, string4)

# print(total)


# part 2

total = 0
for row in range(len(ws)):
    for column in range(len(ws[0])):
        xstring1 = ""
        xstring2 = ""
        if row + 2 < len(ws) and column + 2 < len(ws[0]):
            xstring1 = ws[row][column] + ws[row+1][column+1] + ws[row+2][column+2]
            xstring2 = ws[row][column+2] + ws[row+1][column+1] + ws[row+2][column]
        
        if (xstring1 == "MAS" or xstring1 == "SAM") and (xstring2 == "MAS" or xstring2 == "SAM"):
            total += 1
print(total)