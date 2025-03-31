board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],  # 8th rank (black pieces)
    ["p", "p", "p", "p", "p", "p", "p", "p"],  # 7th rank
    [".", ".", ".", ".", ".", ".", ".", "."],  # Empty squares
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],  # 2nd rank (white pieces)
    ["R", "N", "B", "Q", "K", "B", "N", "R"]   # 1st rank
]

def findRowCol(piece, col):
    found = False
    for row in range(len(board)):
        # print(f"row: {row}")
        if board[row][col] == piece:
            # print(board[row][col])
            found = True    
            break
        # for col in range(len(board[0])):
        #     # print(f"    col: {col}")
        #     if board[row][col] == piece:
        #         # print(board[row][col])
        #         found = True    
        #         break
    if found:
        print(f"Row and col of p: {row}, {col}")
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

def pawnMoveRules(old_pos, new_pos):
    # p can move only down one step at a time
    print(old_pos, new_pos)
    if old_pos[1] != new_pos[1]:
        print("Illegal move: right or left")
        return 1
    elif old_pos[0] > new_pos[0]:
        print("Illegal move: Backwards move!")
        return 2
    elif (new_pos[0] == old_pos[0]) and (new_pos[1] == old_pos[1]):
        # Out of bounds
        print("Out of bounds!")
        return 3
    else:
        print("Legal move")
        return 0
    
def move_piece(board, piece):
    old_row, old_col = findRowCol(piece)
    
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

    old_pos = (old_row, old_col)
    new_pos = (new_row, new_col)

    if piece == ("p" or "P"):
        status = pawnMoveRules(old_pos, new_pos)
        if status == 0:
            board[new_row][new_col] = board[old_row][old_col]
            board[old_row][old_col] = "."  # clear old position

def movePawn(board, piece, new_col):
    old_row, old_col = findRowCol(piece, col)    
    new_row = old_row
    wrong_operator = True
    while wrong_operator:
        new_row+=1
        new_row = checkBounds(new_row)
        old_pos = (old_row, old_col)
        new_pos = (new_row, new_col)
        status = pawnMoveRules(old_pos, new_pos)
        if status == 0:
            board[new_row][new_col] = board[old_row][old_col]
            board[old_row][old_col] = "."  # clear old position
            break
        else:
            print("Wrong operator! Please use u, d, l, or r")
            wrong_operator = True


while True:
    # For example, move 'b' from (1, 2) to (0, 0)
    print("############################")
    print("---------Chess Game---------")
    print("############################")

    show_board(board)
    piece = input("Which piece do you want to move? ")
    col = int(input("Which column? "))
    # move_piece(board, piece, col)
    movePawn(board, piece, col)


