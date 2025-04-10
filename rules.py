from chess_data_structures import MoveType, PieceType

X = 0
Y = 1

def piece_rule_checker(board, player, piece, cur_pos, next_pos):
    piece_at_next_location = board[next_pos[X]][next_pos[Y]]
    if piece == PieceType.EMPTY:
        print("It is a empty")
    elif piece == PieceType.WHITE_PAWN:
        print("It is a white_pawn")
        return pawn_rule_checker(player, cur_pos, next_pos, piece_at_next_location)
    elif piece == PieceType.WHITE_KNIGHT:
        print("It is a white_knight")
    elif piece == PieceType.WHITE_BISHOP:
        print("It is a white_bishop")
    elif piece == PieceType.WHITE_ROOK:
        print("It is a white_rook")
        return rook_rule_checker(board, player, cur_pos, next_pos, piece_at_next_location)
    elif piece == PieceType.WHITE_QUEEN:
        print("It is a white_queen")
    elif piece == PieceType.WHITE_KING:
        print("It is a white_king")
    elif piece == PieceType.BLACK_PAWN:
        print("It is a black_pawn")
        return pawn_rule_checker(player, cur_pos, next_pos, piece_at_next_location)
    elif piece == PieceType.BLACK_KNIGHT:
        print("It is a black_knight")
    elif piece == PieceType.BLACK_BISHOP:
        print("It is a black_bishop")
    elif piece == PieceType.BLACK_ROOK:
        print("It is a black_rook")
    elif piece == PieceType.BLACK_QUEEN:
        print("It is a black_queen")
    elif piece == PieceType.BLACK_KING:
        print("It is a black_king")

def move_dir_finder(cur_pos, next_pos):
    if (cur_pos[X] > next_pos[X]) and (cur_pos[Y] == next_pos[Y]):
        move_type = MoveType.up.value
        print("UP move")
    elif (cur_pos[X] < next_pos[X]) and (cur_pos[Y] == next_pos[Y]):
        move_type = MoveType.down.value
        print("DOWN move")
    elif (cur_pos[Y] < next_pos[Y]) and (cur_pos[X] == next_pos[X]):
        move_type = MoveType.right.value
        print("RIGHT move")
    elif (cur_pos[Y] > next_pos[Y]) and (cur_pos[X] == next_pos[X]):
        move_type = MoveType.left.value
        print("LEFT move")
    elif (cur_pos[X] > next_pos[X]) and (cur_pos[Y] > next_pos[Y]):
        print("UP and LEFT diagonal move")
    elif (cur_pos[X] < next_pos[X]) and (cur_pos[Y] < next_pos[Y]):
        print("DOWN and RIGHT diagonal move")
    elif (cur_pos[X] < next_pos[X]) and (cur_pos[Y] > next_pos[Y]):
        print("DOWN and LEFT diagonal move")
    elif (cur_pos[X] > next_pos[X]) and (cur_pos[Y] < next_pos[Y]):
        move_type = MoveType.up_right.value
        print("UP and RIGHT diagonal move")
    return move_type

def move_legal_algo(board, cur_pos, next_pos):
    # for row in range(cur_pos[X] - next_pos[X]):
    #     tmp_piece = board[(cur_pos[X] - (row + 1))][next_pos[Y]]
    #     if tmp_piece > 0 and 
    #     print(tmp_piece)
        
    return True

def rook_rule_checker(board, player, cur_pos, next_pos, piece_at_next_location):
    if player == 0:
        # Forward move
        rook_move_dir = move_dir_finder(cur_pos, next_pos)
        # if rook move is legal then proceed, else return False
        if (rook_move_dir >= 0) and (rook_move_dir <=3):
            legal = move_legal_algo(board, cur_pos, next_pos)
            legal = True
            if legal:
                if ((piece_at_next_location == 0) or ((piece_at_next_location >= 7) and (piece_at_next_location <= 12))):
                    print("Rook move or capture legal")
            return True
    else:   
        pass
    return False

def pawn_rule_checker(player, cur_pos, next_pos, piece_at_next_location):
    if player == "W":
        print("Player White")
        # Can only go up and capture diagonally
            # Step left to capture
        if (next_pos[X] == (cur_pos[X] - 1)) and (next_pos[Y] == (cur_pos[Y] - 1)):
            if ((piece_at_next_location != PieceType.EMPTY) and ((piece_at_next_location >= PieceType.BLACK_PAWN) and (piece_at_next_location <= PieceType.BLACK_KING))):
                print("Move left and up once")
                return True
            # Forward move
        elif (next_pos[X] == (cur_pos[X] - 1)) and (next_pos[Y] == cur_pos[Y]):
            if (piece_at_next_location == PieceType.EMPTY):
                print("Forward move once")
                return True
            # Step right to capture
        elif (next_pos[X] == (cur_pos[X] - 1)) and (next_pos[Y] == (cur_pos[Y] + 1)):
            if ((piece_at_next_location != PieceType.EMPTY) and ((piece_at_next_location >= PieceType.BLACK_PAWN) and (piece_at_next_location <= PieceType.BLACK_KING))):
                print("Move right & up once")
                return True
        elif ((cur_pos[X] == 6) and # For initial double move
               (next_pos[X] == (cur_pos[X] - 2)) and
                cur_pos[Y] == next_pos[Y]):
                print("Move double")
                return True
                
    elif player == "B":
        print("Player Black")
            # Step left to capture
        if (next_pos[X] == (cur_pos[X] + 1)) and (next_pos[Y] == (cur_pos[Y] + 1)):
            if ((piece_at_next_location != PieceType.EMPTY) and ((piece_at_next_location >= PieceType.WHITE_PAWN) and (piece_at_next_location <= PieceType.WHITE_KING))):
                print("Move left and up once")
                return True
            # Forward move
        elif (next_pos[X] == (cur_pos[X] + 1)) and (next_pos[Y] == cur_pos[Y]):
            if (piece_at_next_location == PieceType.EMPTY):
                print("Forward move once")
                return True
                # Step right to capture
        elif (next_pos[X] == (cur_pos[X] + 1)) and (next_pos[Y] == (cur_pos[Y] - 1)):
            if ((piece_at_next_location != PieceType.EMPTY) and ((piece_at_next_location >= PieceType.WHITE_PAWN) and (piece_at_next_location <= PieceType.WHITE_KING))):
                print("Move right & up once")
                return True
        elif ((cur_pos[X] == 1) and # For initial double move
               (next_pos[X] == (cur_pos[X] + 2)) and
                cur_pos[Y] == next_pos[Y]):
                print("Move double")
                return True
    else:
        print("No such player")
    return False
