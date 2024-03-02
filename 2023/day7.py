ls = open('2023/inputs/day7input.txt', 'r').read().split('\n')[:-1]

'''Part 1'''
# There is a point system that
# card_strength = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}

# result = {}
# for line in ls:
#     card_count = {}
#     hand, bid = line.split()[0], line.split()[1]
#     pts = 0
#     for card in range(len(hand)):
#         pts += card_strength[hand[card]] * (100**(5-card))
#         if card_count.get(hand[card]) == None:
#             card_count[hand[card]] = 1
#         else:
#             card_count[hand[card]] += 1
#     print(hand, pts)
#     print(card_count)
#     if len(card_count) == 1:
#         result[100000000000000*pts] = bid
#     elif len(card_count) == 2:
#         first = list(card_count)[0]
#         if card_count[first] == 1 or card_count[first] == 4:
#             result[1000000000000*pts] = bid
#         elif card_count[first] == 2 or card_count[first] == 3:
#             result[10000000000*pts] = bid
#     elif len(card_count) == 3:
#         for key in card_count:
#             if card_count[key] == 3:
#                 result[100000000*pts] = bid
#                 break
#         else:
#             result[1000000*pts] = bid
#     elif len(card_count) == 4:
#         result[10000*pts] = bid
#     else:
#         result[100*pts] = bid
# print(sorted(result))

# winnings = 0
# for rank, key in enumerate(sorted(result)):
#     winnings += (rank+1) * int(result[key])
# print(winnings)
        



'''Part 2'''
card_strength = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 11, 'K': 12, 'A': 13}

result = {}
for line in ls:
    card_count = {}
    hand, bid = line.split()[0], line.split()[1]
    pts = 0
    for card in range(len(hand)):
        pts += card_strength[hand[card]] * (100**(5-card))
        if card_count.get(hand[card]) == None:
            card_count[hand[card]] = 1
        else:
            card_count[hand[card]] += 1
    print(hand, pts)
    print(card_count)
    if len(card_count) == 1:
        #five of a kind
        result[100000000000000*pts] = [hand, bid]
    elif len(card_count) == 2:
        first = list(card_count)[0]
        if card_count.get('J', -1) >= 1:
            #five of a kind
            result[100000000000000*pts] = [hand, bid]
        elif card_count[first] == 1 or card_count[first] == 4:
            #four of a kind
            result[1000000000000*pts] = [hand, bid]
        elif card_count[first] == 2 or card_count[first] == 3:
            #full house
            result[10000000000*pts] = [hand, bid]
    elif len(card_count) == 3:
        if card_count.get('J', -1) >= 2:
            #four of a kind
            result[1000000000000*pts] = [hand, bid]
            continue
        for key in card_count:
            if card_count[key] == 3 and card_count.get('J', -1) == 1:
                #four of a kind
                result[1000000000000*pts] = [hand, bid]
                break
            elif card_count[key] == 3:
                #three of a kind
                result[100000000*pts] = [hand, bid]
                break
        else:
            if card_count.get('J', -1) == 1:
                #full house
                result[10000000000*pts] = [hand, bid]
            else:
                #two pair
                result[1000000*pts] = [hand, bid]
    elif len(card_count) == 4:
        if card_count.get('J', -1) >= 1:
            #three of a kind
            result[100000000*pts] = [hand, bid]
        else:
            #one pair
            result[10000*pts] = [hand, bid]
    else:
        if card_count.get('J', -1) == 1:
            #one pair
            result[10000*pts] = [hand, bid]
        else:
            #high card
            result[100*pts] = [hand, bid]
# print(sorted(result))

winnings = 0
for rank, key in enumerate(sorted(result)):
    print(rank+1, result[key][0], key)
    winnings += (rank+1) * int(result[key][1])
print(winnings)