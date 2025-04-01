board2 = [
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
    [" ", "a", "b", "c", "d", "e", "f", "g", "h", " "],  
    ["8", "r", "n", "b", "q", "k", "b", "n", "r", "8"],  
    ["7", "p", "p", "p", "p", "p", "p", "p", "p", "7"],  
    ["6", ".", ".", ".", ".", ".", ".", ".", ".", "6"],  
    ["5", ".", ".", ".", ".", ".", ".", ".", ".", "5"],  
    ["4", ".", ".", ".", ".", ".", ".", ".", ".", "4"],  
    ["3", ".", ".", ".", ".", ".", ".", ".", ".", "3"],  
    ["2", "P", "P", "P", "P", "P", "P", "P", "P", "2"],  
    ["1", "R", "N", "B", "Q", "K", "B", "N", "R", "1"],  
    [" ", "a", "b", "c", "d", "e", "f", "g", "h", " "]   
]

def chess_to_index(file, rank):
    col = ord(file) - ord('a') + 1  # Convert 'a' -> 1, 'b' -> 2, ..., 'h' -> 8
    row = 9 - int(rank)  # Convert '8' -> 1, '7' -> 2, ..., '1' -> 8 (in board index)
    return row, col

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
    if rowColNum < 1:
        print("Out of bounds!")
        rowColNum +=1
    elif rowColNum >= (len(board[0]) - 1):
        rowColNum -=1
        print("Out of bounds!")
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
    

def movePawn(board, file, rank):
    old_row, old_col = chess_to_index(file, rank)    
    new_row = old_row
    new_row+=1
    new_row = checkBounds(new_row)
    old_pos = (old_row, old_col)
    new_pos = (new_row, old_col)
    status = pawnMoveRules(old_pos, new_pos)
    if status == 0:
        board[new_row][old_col] = board[old_row][old_col]
        board[old_row][old_col] = "."  # clear old position

    
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


while True:
    # For example, move 'b' from (1, 2) to (0, 0)
    print("############################")
    print("---------Chess Game---------")
    print("############################")

    show_board(board)
    file = input("Enter file of a piece: ")
    rank = input("Enter rank of a piece: ")

    movePawn(board, file, rank)


