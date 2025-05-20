"""
Requirements
Implement the following features:

the board should be stored as a three-element list, while each element is another three-element list (the inner lists represent rows) so that all of the squares may be accessed using the following syntax:

board[row][column]
 

each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number (such a square is considered free)
the board's appearance should be exactly the same as the one presented in the example.
implement the functions defined for you in the editor.

Drawing a random integer number can be done by utilizing a Python function called randrange(). The example program below shows how to use it (the program prints ten random numbers from 0 to 8).
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
"""
from random import randrange

############# Display Board ###################

# To display board pattern as above

def display_board(board):
    print("+---------" * 3, "+", sep="")
    for row in range(3):
        print("|         " * 3, "|", sep ="")
        for col in range(3):
            print("|    " + str(board[row][col]) + "    ", end ="")
        print("|")
        print("|         " *3, "|", sep="")
        print("+---------" * 3, "+", sep="")

############# Enter Move ###################

"""
Getting input move from user 1 - 9
if the board is occupied, get the input again
get the row and column on the board based on the user input move
"""
def enter_move(board):
    flag = False
    while not flag:
        move = input("Enter your move: ")
        flag = len(move) == 1 and move >= '1' and move <= '9' # number between 1-9
        if not flag:
            print("Bad move - repeat your input")
            continue
        move = int(move) - 1 # cell 0 - 8
        row = move // 3
        cols = move % 3
        sign = board[row][cols]
        flag = sign not in ("X", "O")
        if not flag:
            print("Field already occupied - repeat your input")
            continue
        board[row][cols] = "O"

############# Free Cell ###################

# get free cell
# if the board cell is not occupied, then add to freecell
def make_list_free_fields(board):
    freecell = []
    for row in range(0,3):
        for col in range(0,3):
            if board[row][col] not in ({"X", "O"}):
                freecell.append((row, col))         # append new tuple to list

    return freecell

############# Victory For ###################
"""
if the sign - "X", its computer
if the sign - "O" its user
if any of the rows filled with "X" or "O"
if any of the columns filled with "X" or "O"
if any of the diagonal filled with "X" or "O"
then based on it, winner will be displayed
"""

def victory_for(board, sgn):
    if sgn == "X":
        who = "me"
    elif sgn =="O":
        who = "you"
    else:
        who = "None"
    cross1 = cross2 = True
    for i in range(0,3):
        if board[i][0] == sgn and board[i][1] == sgn and board[i][2] == sgn:  # check row
            return who
        if board[0][i] == sgn and board[1][i] == sgn and board[2][i] == sgn:   # check column
            return who
        if board[i][i] != sgn:  # check 1 diagonal
            cross1 = False
        if board[2 - i][2 -i] != sgn:   # check 2 diagonal
            cross2 = False
    if cross1 or cross2:
        return who
    return None

############# Draw Move ###################
# computer draw move based on the free fields

def draw_move(board):
    free = make_list_free_fields(board)   
    cnt = len(free)
    if cnt > 0:        
        this = randrange(cnt)
        print(this)
        print(free[this])
        row, col = free[this]
        board[row][col] = "X"

############# Main functionality - display board, getting moves and decide winner ###################
"""
Populating board with 1-9
Alternate human and computer turns
check for wins human or computer 
if neither wins, its tie
"""
board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] ="X"    
free = make_list_free_fields(board)
human_turn = True

while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board,"O")
    else:
        draw_move(board)
        victor = victory_for(board, "X")
    if victor != None:        
        break
    human_turn = not human_turn
    free = make_list_free_fields(board)

display_board(board)
if victor == "you":
    print("You won!")
elif victor == "me":
    print("I won!")
else:
    print("Tie")

        
