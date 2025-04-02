from enum import Enum

class PieceType(Enum):
    empty = 0
    white_pawn = 1
    white_knight = 2
    white_bishop = 3
    white_rook = 4
    white_queen = 5
    white_king = 6
    black_pawn = 7
    black_knight = 8
    black_bishop = 9
    black_rook = 10
    black_queen = 11
    black_king = 12

class PlayerType(Enum):
    player_white = 0
    player_black = 1

board = [
    [PieceType.black_rook.value, PieceType.black_knight.value, PieceType.black_bishop.value, PieceType.black_queen.value, PieceType.black_king.value, PieceType.black_bishop.value, PieceType.black_knight.value, PieceType.black_rook.value],  # 8th rank (black pieces)
    [PieceType.black_pawn.value, PieceType.black_pawn.value, PieceType.black_pawn.value, PieceType.black_pawn.value, PieceType.black_pawn.value, PieceType.black_pawn.value, PieceType.black_pawn.value, PieceType.black_pawn.value],  # 7th rank
    [PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value],  # Empty squares
    [PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value],
    [PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value],
    [PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value],
    [PieceType.white_pawn.value, PieceType.white_pawn.value, PieceType.white_pawn.value, PieceType.white_pawn.value, PieceType.white_pawn.value, PieceType.white_pawn.value, PieceType.white_pawn.value, PieceType.white_pawn.value],  # 2nd rank (white pieces)
    [PieceType.white_rook.value, PieceType.white_knight.value, PieceType.white_bishop.value, PieceType.white_queen.value, PieceType.white_king.value, PieceType.white_bishop.value, PieceType.white_knight.value, PieceType.white_rook.value]   # 1st rank
]


def movePawn():
    pass

def getMove(player, board):
    cur_row = int(input("Enter current row of a piece: "))
    cur_col = int(input("Enter current column of a piece: "))
    next_row = int(input("Enter next row of a piece: "))
    next_col = int(input("Enter next column of a piece: "))
    cur_pos = (cur_row, cur_col)
    next_pos = (next_row, next_col)
    return cur_pos, next_pos

def attemptMove(cur_pos, next_pos):
    print(board[cur_pos[0]][cur_pos[1]])
    print(board[next_pos[0]][next_pos[1]])

    board[next_pos[0]][next_pos[1]] =  board[cur_pos[0]][cur_pos[1]]
    board[cur_pos[0]][cur_pos[1]] = 0 # clear old position

    pass

def show_board():
    for row in board:
        print(row)

show_board()



while True:
    # For example, move 'b' from (1, 2) to (0, 0)
    print("############################")
    print("---------Chess Game---------")
    print("############################")

    cur_pos, next_pos = getMove(PlayerType.player_white.value, board)
    
    attemptMove(cur_pos, next_pos)

    show_board()
