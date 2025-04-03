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

def pawn_rule_checker(player, cur_pos, next_pos):
    if player == 0:
        # Can only go up
        if cur_pos[0] < next_pos[0]:
            print("Backwards move")
            return False
        else:
            pass    
    else:
        # Can only go down
        pass
    return True

def piece_rule_checker(player, piece, cur_pos, next_pos):
    if piece == 0:
        print("It is a empty")
    elif piece == 1:
        print("It is a white_pawn")
        return pawn_rule_checker(player, cur_pos, next_pos)
    elif piece == 2:
        print("It is a white_knight")
    elif piece == 3:
        print("It is a white_bishop")
    elif piece == 4:
        print("It is a white_rook")
    elif piece == 5:
        print("It is a white_queen")
    elif piece == 6:
        print("It is a white_king")
    elif piece == 7:
        print("It is a black_pawn")
    elif piece == 8:
        print("It is a black_knight")
    elif piece == 9:
        print("It is a black_bishop")
    elif piece == 10:
        print("It is a black_rook")
    elif piece == 11:
        print("It is a black_queen")
    elif piece == 12:
        print("It is a black_king")

def get_move(player, board):
    # Prompt the user to enter four values (current row, current column, next row, next column)
    move_input = input("Enter current row, current column, next row, next column (e.g., 1 2 3 4): ")
    
    # Split the input into separate values and convert them to integers
    cur_row, cur_col, next_row, next_col = map(int, move_input.split())

    cur_pos = (cur_row, cur_col)
    next_pos = (next_row, next_col)

    return cur_pos, next_pos

def attempt_move(player, piece, cur_pos, next_pos):
    print(board[cur_pos[0]][cur_pos[1]])
    print(board[next_pos[0]][next_pos[1]])

    legal = piece_rule_checker(player, piece, cur_pos, next_pos,)

    if legal:
        board[next_pos[0]][next_pos[1]] =  board[cur_pos[0]][cur_pos[1]]
        board[cur_pos[0]][cur_pos[1]] = 0 # clear old position
        print("Legal Move!")
    else:
        print("Illegal Move!")
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

    cur_pos, next_pos = get_move(PlayerType.player_white.value, board)
    
    attempt_move(PlayerType.player_white.value, PieceType.white_pawn.value, cur_pos, next_pos)

    show_board()
