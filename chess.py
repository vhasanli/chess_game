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
    
    new_row+=1  # advance to the next row
    new_row = checkBounds(new_row) # if out of bounds, don't advance

    old_pos = (old_row, old_col)
    new_pos = (new_row, old_col)

    status = pawnMoveRules(old_pos, new_pos)
    
    if status == 0:
        board[new_row][old_col] = board[old_row][old_col]
        board[old_row][old_col] = "."  # clear old position


while True:
    # For example, move 'b' from (1, 2) to (0, 0)
    print("############################")
    print("---------Chess Game---------")
    print("############################")

    show_board(board)
    file = input("Enter file of a piece: ")
    rank = input("Enter rank of a piece: ")

    if (ord(file) >= 97 and ord(file) <= 104) and (int(rank) >= 1 and int(rank) <= 8): 
        movePawn(board, file, rank)
    else:
        print("Please enter a valid values: ")


