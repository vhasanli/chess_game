from chess_data_structures import MoveType, PieceType, Player, ROW, COL
from utilities import is_opposite_piece, move_dir_finder, move_legal_algo, row_col_move_good


def piece_rule_checker(board, player, piece, cur_pos, next_pos):
    piece_at_next_location = board[next_pos[ROW]][next_pos[COL]]

    if piece == PieceType.EMPTY:
        print("It is a empty")
    elif piece == PieceType.WHITE_PAWN:
        print("It is a white_pawn")
        return pawn_rule_checker(player, cur_pos, next_pos, piece_at_next_location.value)
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
        return pawn_rule_checker(player, cur_pos, next_pos, piece_at_next_location.value)
    elif piece == PieceType.BLACK_KNIGHT:
        print("It is a black_knight")
    elif piece == PieceType.BLACK_BISHOP:
        print("It is a black_bishop")
    elif piece == PieceType.BLACK_ROOK:
        print("It is a black_rook")
        return rook_rule_checker(board, player, cur_pos, next_pos, piece_at_next_location)
    elif piece == PieceType.BLACK_QUEEN:
        print("It is a black_queen")
    elif piece == PieceType.BLACK_KING:
        print("It is a black_king")

def rook_rule_checker(board, player, cur_pos, next_pos, piece_at_next_location):
    # UP or DOWN movement
    if cur_pos[COL] == next_pos[COL]:
        if cur_pos[ROW] < next_pos[ROW]: #DOWN
            # loop over each piece in ascending order untill non zero value is reached
            for i in range (cur_pos[ROW] + 1, next_pos[ROW] + 1):
                tmp_pos = board[i][cur_pos[COL]]
                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(i, ROW, player, tmp_pos, next_pos, piece_at_next_location)
            else:
                if (i == next_pos[ROW]):
                    return True
        else: # UP
            # loop over each piece in descending order untill non zero value is reached
            for i in range (cur_pos[ROW] - 1, next_pos[ROW] - 1,  -1):
                tmp_pos = board[i][cur_pos[COL]]
                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(i, ROW, player, tmp_pos, next_pos, piece_at_next_location)
                else:
                    if (i == next_pos[ROW]):
                        return True
                       
    else: # LEFT or RIGHT movement
        if cur_pos[COL] < next_pos[COL]: # RIGHT
            for i in range (cur_pos[COL] + 1, next_pos[COL] + 1):
                tmp_pos = board[cur_pos[ROW]][i]
                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(i, COL, player, tmp_pos, next_pos, piece_at_next_location)
                else:
                    if (i == next_pos[COL]):
                        return True
        else: # LEFT
            for i in range (cur_pos[COL] - 1, next_pos[COL] - 1,  -1):
                tmp_pos = board[cur_pos[ROW]][i]
                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(i, COL, player, tmp_pos, next_pos, piece_at_next_location)

                else:
                    if (i == next_pos[COL]):
                        return True

def pawn_rule_checker(player, cur_pos, next_pos, piece_at_next_location):
    move_dir = move_dir_finder(cur_pos, next_pos)
    print(move_dir) #How can I use this?
  
    if player == "W":
        print("Player White")
        # Can only go up and capture diagonally
            # Step left to capture
        if (next_pos[ROW] == (cur_pos[ROW] - 1)) and (next_pos[COL] == (cur_pos[COL] - 1)):
            return is_opposite_piece(Player.WHITE, piece_at_next_location)
        elif (next_pos[ROW] == (cur_pos[ROW] - 1)) and (next_pos[COL] == cur_pos[COL]):
            if (piece_at_next_location == PieceType.EMPTY.value):
                print("Forward move once")
                return True
            # Step right to capture
        elif (next_pos[ROW] == (cur_pos[ROW] - 1)) and (next_pos[COL] == (cur_pos[COL] + 1)):
            return is_opposite_piece(Player.WHITE, piece_at_next_location)
        elif ((cur_pos[ROW] == 6) and # For initial double move
               (next_pos[ROW] == (cur_pos[ROW] - 2)) and
                cur_pos[COL] == next_pos[COL]):
                print("Move double")
                return True
    elif player == "B":
        print("Player Black")
            # Step left to capture
        if (next_pos[ROW] == (cur_pos[ROW] + 1)) and (next_pos[COL] == (cur_pos[COL] + 1)):
            return is_opposite_piece(Player.BLACK, piece_at_next_location)
            # Forward move
        elif (next_pos[ROW] == (cur_pos[ROW] + 1)) and (next_pos[COL] == cur_pos[COL]):
            if (piece_at_next_location == PieceType.EMPTY.value):
                print("Forward move once")
                return True
                # Step right to capture
        elif (next_pos[ROW] == (cur_pos[ROW] + 1)) and (next_pos[COL] == (cur_pos[COL] - 1)):
            return is_opposite_piece(Player.BLACK, piece_at_next_location)
        elif ((cur_pos[ROW] == 1) and # For initial double move
               (next_pos[ROW] == (cur_pos[ROW] + 2)) and
                cur_pos[COL] == next_pos[COL]):
                print("Move double")
                return True
    else:
        print("No such player")
    return False
