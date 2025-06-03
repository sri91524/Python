"""
Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
If you need more details, you can find them here.

Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
"""
# A function that checks whether a list passed as an argument contains
# nine digits from '1' to '9'.
def checkset(digits):
    return sorted(digits) == [chr(x + ord('0')) for x in range(1,10)]

rows = [ ]
for r in range(0,9):
    ok = False
    while not ok:
        row = input("Enter row #" + str(r + 1) + ": ")
        ok = len(row) == 9 and row.isdigit()       
        if not ok:
            print("Enter valid 9 digits")
    rows.append(row)
# check if all rows are good
ok = True
for r in range(0,9):
    ok = checkset(rows[r])
    if not ok:
        ok = False
        break
# check all columns are good
if ok:
    for c in range(0,9):
        col =[]
        for r in range(0,9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# check if all subsquares are good
if ok:
    for r in range(0,9,3):
        for c in range(0,9,3):
            square = ''
            for i in range(0,3):
                square += rows[r+i][c:c+3]
            if not checkset(square):
                ok = False
                break

if ok:
    print("Yes")
else:
    print("No")



