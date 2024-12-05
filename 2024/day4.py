ls = open('2024/inputs/day4.txt', 'r').read().split('\n')[:-1]

ws = []
for i in ls:
    r = []
    for j in i:
        r.append(j)
    ws.append(r)

total = 0
for row in range(len(ws)):
    for column in range(len(ws[0])):
        list_strings = ["", "", "", ""]
        if column + 3 < len(ws[0]):
            # right side
            list_strings[0] = ws[row][column] + ws[row][column+1] + ws[row][column+2] + ws[row][column+3]
        if row + 3 < len(ws):
            # down
            list_strings[1] = ws[row][column] + ws[row+1][column] + ws[row+2][column] + ws[row+3][column]
        if column + 3 < len(ws[0]) and row + 3 < len(ws):
            # down and right
            list_strings[2] = ws[row][column] + ws[row+1][column+1] + ws[row+2][column+2] + ws[row+3][column+3]
        if column - 3 >= 0 and row + 3 < len(ws):
            #down and left
            list_strings[3] = ws[row][column] + ws[row+1][column-1] + ws[row+2][column-2] + ws[row+3][column-3]
        
        for string in list_strings:
            if string == "XMAS" or string == "SAMX":
                # Checking for XMAS but also the reversed
                total += 1
print(total)


# part 2

total = 0
for row in range(len(ws)):
    for column in range(len(ws[0])):
        xstring1, xstring2 = "", ""
        if row + 2 < len(ws) and column + 2 < len(ws[0]):
            xstring1 = ws[row][column] + ws[row+1][column+1] + ws[row+2][column+2]
            xstring2 = ws[row][column+2] + ws[row+1][column+1] + ws[row+2][column]
        
        if (xstring1 == "MAS" or xstring1 == "SAM") and (xstring2 == "MAS" or xstring2 == "SAM"):
            total += 1
print(total)