#List comprehension
# squares = [x ** 2 for x in range(8)]
# print(squares)

# twos = [2 ** i for i in range(8)]
# print(twos)

# odds = [x for x in squares if x != 0 ]
# print(odds)

# #two dimensional array
# board = []
# EMPTY = "ChessBoard"
# for i in range(3):
#     row = [EMPTY for i in range(3)]
#     board.append(row)
# print(board)

#Multi dimensional
# example 1
temps = [[0.0 for h in range(24)] for d in range(31)]

total = 0.0
for day in temps:
    total += day[11]

average = total/31
print("Average temp at noon", average)

# example 2
temps = [[0.0 for h in range(24)] for d in range(31)]

highest = -100.0

# 31 days 
for day in temps:
    # 24 hours
    for temp in day:
        if temp > highest:
            highest = temp
print("The highest temperature was", highest)

temps= [[0.0 for h in range(24)] for d in range(31)]

hot_days = 0
# 31 days
for day in temps:
    print(day)
    # hr 11
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")

"""
The first index (0 through 2) selects one of the buildings; the second (0 through 14) selects the floor, the third (0 through 19) selects the room number. All rooms are initially free.
"""
rooms = [[[False for r in range(20)] for f in range(15)] for b in range(3)]

"""
Now you can book a room for two newlyweds: in the second building, on the tenth floor, room 14:
"""
rooms[1][9][13] = True

"""
and release the second room on the fifth floor located in the first building:
"""
rooms[0][4][1] = False

print(rooms[1][9][13])
"""
Check if there are any vacancies on the 15th floor of the third building:
"""
vacancy = 0
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print(vacancy)