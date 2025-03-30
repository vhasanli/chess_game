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
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."],
    ["p", ".", "."]
]

def findRowCol():
    found = False
    for row in range(len(board)):
        print(f"row: {row}")
        for col in range(len(board[0])):
            print(f"    col: {col}")
            if board[row][col] == "p":
                print(board[row][col])
                found = True    
                break
            else:
                print("a")
        if found:
            print(f"Row and col of p: {row}, {col}")
            print_board(board)
            return row, col
    
def print_board(board):
    for row in board:
        print(" ".join(row))

def move_piece(board, old_row, old_col, new_row, new_col):
    board[new_row][new_col] = board[old_row][old_col]
    board[old_row][old_col] = "."  # clear old position

print_board(board)

while True:
    # For example, move 'b' from (1, 2) to (0, 0)
    old_row, old_col = findRowCol()
    new_row = int(input("Enter new_row: "))
    new_col = int(input("Enter new_col: "))

    move_piece(board, old_row, old_col, new_row, new_col)
    print_board(board)


