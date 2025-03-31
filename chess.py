chess_board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],  # 8th rank (black pieces)
    ["p", "p", "p", "p", "p", "p", "p", "p"],  # 7th rank
    [".", ".", ".", ".", ".", ".", ".", "."],  # Empty squares
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],  # 2nd rank (white pieces)
    ["R", "N", "B", "Q", "K", "B", "N", "R"]   # 1st rank
]

board = [
    ["p", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."]
]

def findRowCol():
    found = False
    for row in range(len(board)):
        # print(f"row: {row}")
        for col in range(len(board[0])):
            # print(f"    col: {col}")
            if board[row][col] == "p":
                # print(board[row][col])
                found = True    
                break
        if found:
            print(f"Row and col of p: {row}, {col}")
            show_board(board)
            return row, col
    
def show_board(board):
    for row in board:
        print(" ".join(row))

def checkBounds(rowColNum):
    if rowColNum < 0:
        print("Out of bounds!")
        rowColNum +=1
    elif rowColNum >= len(board[0]):
            rowColNum -=1
            print(rowColNum)
    return rowColNum

def move_piece(board, old_row, old_col):
    new_row = old_row
    new_col = old_col

    wrong_operator = True
    while wrong_operator:
        key = input("Enter direction u, d, l, or r: ")

        if (key == "r"):
            new_col+=1
            new_col = checkBounds(new_col)
            break
        elif (key == "l"):
            new_col-=1
            new_col = checkBounds(new_col)
            break
        elif (key == "u"):
            new_row-=1
            new_row = checkBounds(new_row)
            break
        elif (key == "d"):
            new_row+=1
            new_row = checkBounds(new_row)
            break
        else:
            print("Wrong operator! Please use u,d,l, or r")
            wrong_operator = True

    if (new_row == old_row) and (new_col == old_col):
        print("Wrong move!")
    else:
        board[new_row][new_col] = board[old_row][old_col]
        board[old_row][old_col] = "."  # clear old position

while True:
    # For example, move 'b' from (1, 2) to (0, 0)
    old_row, old_col = findRowCol()

    move_piece(board, old_row, old_col)


