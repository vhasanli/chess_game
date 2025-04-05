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

X = 0
Y = 1

def pos_to_value():
    pass 

def pawn_rule_checker(board, player, cur_pos, next_pos):
    if player == 0:
        print("Player White")
        # Can only go up and capture diagonally
            # Step left to capture
        if (next_pos[X] == (cur_pos[X] - 1)) and (next_pos[Y] == (cur_pos[Y] - 1)):
            if (board[next_pos[X]][next_pos[Y]]) != 0:
                print("Move left and up once")
                return True
            # Forward move
        elif (next_pos[X] == (cur_pos[X] - 1)) and (next_pos[Y] == cur_pos[Y]):
            if (board[next_pos[X]][next_pos[Y]]) == 0:
                print("Forward move once")
                return True
            # Step right to capture
        elif (next_pos[X] == (cur_pos[X] - 1)) and (next_pos[Y] == (cur_pos[Y] + 1)):
            if (board[next_pos[X]][next_pos[Y]]) != 0:
                print("Move right & up once")
                return True
        elif ((cur_pos[X] == 6) and # For initial double move
               (next_pos[X] == (cur_pos[X] - 2)) and
                cur_pos[Y] == next_pos[Y]):
                print("Move double")
                return True
    else:
        print("Player Black")
            # Step left to capture
        if (next_pos[X] == (cur_pos[X] + 1)) and (next_pos[Y] == (cur_pos[Y] + 1)):
            if (board[next_pos[X]][next_pos[Y]]) != 0:
                print("Move left and up once")
                return True
            # Forward move
        elif (next_pos[X] == (cur_pos[X] + 1)) and (next_pos[Y] == cur_pos[Y]):
            if (board[next_pos[X]][next_pos[Y]]) == 0:
                print("Forward move once")
                return True
                # Step right to capture
        elif (next_pos[X] == (cur_pos[X] + 1)) and (next_pos[Y] == (cur_pos[Y] - 1)):
            if (board[next_pos[X]][next_pos[Y]]) != 0:
                print("Move right & up once")
                return True
        elif ((cur_pos[X] == 1) and # For initial double move
               (next_pos[X] == (cur_pos[X] + 2)) and
                cur_pos[Y] == next_pos[Y]):
                print("Move double")
                return True

    return False

def piece_rule_checker(board, player, piece, cur_pos, next_pos):
    if piece == 0:
        print("It is a empty")
    elif piece == 1:
        print("It is a white_pawn")
        return pawn_rule_checker(board, player, cur_pos, next_pos)
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
        return pawn_rule_checker(board, player, cur_pos, next_pos)
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

def get_move(player):
    # Prompt the user to enter four values (current row, current column, next row, next column)
    move_input = input("Enter current row, current column, next row, next column (e.g., 1 2 3 4): ")
    
    # Split the input into separate values and convert them to integers
    cur_row, cur_col, next_row, next_col = map(int, move_input.split())

    cur_pos = (cur_row, cur_col)
    next_pos = (next_row, next_col)

    return cur_pos, next_pos, player

def attempt_move(board, player, piece, cur_pos, next_pos):

    legal = piece_rule_checker(board, player, piece, cur_pos, next_pos,)

    if legal:
        board[next_pos[X]][next_pos[Y]] =  board[cur_pos[X]][cur_pos[Y]]
        board[cur_pos[X]][cur_pos[Y]] = 0 # clear old position
        print("Legal Move!")
    else:
        print("Illegal Move!")
    pass

def show_board():
    for row in board:
        print(row)

while True:
    # For example, move 'b' from (1, 2) to (0, 0)
    print("############################")
    print("---------Chess Game---------")
    print("############################")
    show_board()

    cur_pos, next_pos, player = get_move(PlayerType.player_black.value)
    
    attempt_move(board, player, PieceType.black_pawn.value, cur_pos, next_pos)
