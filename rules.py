from chess_data_structures import PieceType, Player, ROW, COL
from utilities import is_opposite_piece, row_col_move_good
from typing import List


def piece_rule_checker(board:List[List[PieceType]], player: str, 
                       piece:PieceType, cur_pos:tuple, next_pos:tuple)->bool:
    """
        this is a comment
        this is a comment
        this is a comment
    """
    piece_at_next_location = board[next_pos[ROW]][next_pos[COL]]

    if piece == PieceType.EMPTY:
        print("It is a empty")
    elif piece == PieceType.WHITE_PAWN:
        print("It is a white_pawn")
        return pawn_rule_checker(player, cur_pos, 
                                 next_pos, piece_at_next_location)
    elif piece == PieceType.WHITE_KNIGHT:
        print("It is a white_knight")
        return knight_rule_checker(player, cur_pos, next_pos, piece_at_next_location)
    elif piece == PieceType.WHITE_BISHOP:
        print("It is a white_bishop")
        return bishop_rule_checker(board, player, cur_pos, next_pos, piece_at_next_location)
    elif piece == PieceType.WHITE_ROOK:
        print("It is a white_rook")
        return rook_rule_checker(board, player, cur_pos, next_pos, piece_at_next_location)
    elif piece == PieceType.WHITE_QUEEN:
        print("It is a white_queen")
        return queen_rule_checker(board, player, cur_pos, next_pos, piece_at_next_location)
    elif piece == PieceType.WHITE_KING:
        print("It is a white_king")
    elif piece == PieceType.BLACK_PAWN:
        print("It is a black_pawn")
        return pawn_rule_checker(player, cur_pos, next_pos, piece_at_next_location)
    elif piece == PieceType.BLACK_KNIGHT:
        print("It is a black_knight")
        return knight_rule_checker(player, cur_pos, next_pos, piece_at_next_location)
    elif piece == PieceType.BLACK_BISHOP:
        print("It is a black_bishop")
        return bishop_rule_checker(board, player, cur_pos, next_pos, piece_at_next_location)
    elif piece == PieceType.BLACK_ROOK:
        print("It is a black_rook")
        return rook_rule_checker(board, player, cur_pos, next_pos, piece_at_next_location)
    elif piece == PieceType.BLACK_QUEEN:
        print("It is a black_queen")
        return queen_rule_checker(board, player, cur_pos, next_pos, piece_at_next_location)
    elif piece == PieceType.BLACK_KING:
        print("It is a black_king")

def queen_rule_checker(board, player, cur_pos, next_pos, piece_at_next_location):
    # UP or DOWN movement
    if cur_pos[COL] == next_pos[COL]:
        if cur_pos[ROW] < next_pos[ROW]: #DOWN
            # loop over each piece in ascending order untill non zero value is reached
            for i in range (cur_pos[ROW] + 1, next_pos[ROW] + 1):
                tmp_pos = board[i][cur_pos[COL]]
                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(i, ROW, player, next_pos, piece_at_next_location)
                else:
                    if (i == next_pos[ROW]):
                        return True
        else: # UP
            # loop over each piece in descending order untill non zero value is reached
            for i in range (cur_pos[ROW] - 1, next_pos[ROW] - 1,  -1):
                tmp_pos = board[i][cur_pos[COL]]
                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(i, ROW, player, next_pos, piece_at_next_location)
                else:
                    if (i == next_pos[ROW]):
                        return True
                       
    elif cur_pos[ROW] == next_pos[ROW]: # LEFT or RIGHT movement
        if cur_pos[COL] < next_pos[COL]: # RIGHT
            for i in range (cur_pos[COL] + 1, next_pos[COL] + 1):
                tmp_pos = board[cur_pos[ROW]][i]
                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(i, COL, player, next_pos, piece_at_next_location)
                else:
                    if (i == next_pos[COL]):
                        return True
        else: # LEFT
            for i in range (cur_pos[COL] - 1, next_pos[COL] - 1,  -1):
                tmp_pos = board[cur_pos[ROW]][i]
                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(i, COL, player, next_pos, piece_at_next_location)
                else:
                    if (i == next_pos[COL]):
                        return True
    #UP and LEFT
    elif ((cur_pos[ROW] > next_pos[ROW]) and (cur_pos[COL] > next_pos[COL])):
        if ((cur_pos[ROW] - next_pos[ROW]) == (cur_pos[COL] - next_pos[COL])):
            col_num =  cur_pos[COL] - 1
            for row_num in range (cur_pos[ROW] - 1, next_pos[ROW] - 1,  -1):
                tmp_pos = board[row_num][col_num]
                col_num-=1
                print(tmp_pos)

                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(row_num, ROW, player, next_pos, piece_at_next_location)
                else:
                    if (row_num == next_pos[ROW]):
                        return True
    #DOWN and RIGHT
    elif ((cur_pos[ROW] < next_pos[ROW]) and (cur_pos[COL] < next_pos[COL])):
        if ((next_pos[ROW] - cur_pos[ROW]) == (next_pos[COL] - cur_pos[COL])):
            col_num =  cur_pos[COL] + 1
            for row_num in range (cur_pos[ROW] + 1, next_pos[ROW] + 1):
                tmp_pos = board[row_num][col_num]
                col_num+=1
                print(tmp_pos)

                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(row_num, ROW, player, next_pos, piece_at_next_location)
                else:
                    if (row_num == next_pos[ROW]):
                        return True
    #UP and RIGHT
    elif ((cur_pos[ROW] > next_pos[ROW]) and (cur_pos[COL] < next_pos[COL])):
        if ((cur_pos[ROW] - next_pos[ROW]) == (next_pos[COL] - cur_pos[COL])):
            cur_row_num =  cur_pos[ROW] - 1
            for col_num in range(cur_pos[COL] + 1, next_pos[COL] + 1):
                tmp_pos = board[cur_row_num][col_num]
                cur_row_num-=1
                print(tmp_pos)

                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(col_num, COL, player, next_pos, piece_at_next_location)
                else:
                    if (col_num == next_pos[COL]):
                        return True
    #DOWN and LEFT
    elif ((cur_pos[ROW] < next_pos[ROW]) and (cur_pos[COL] > next_pos[COL])):
        if ((cur_pos[COL] - next_pos[COL]) == (next_pos[ROW] - cur_pos[ROW])):
            cur_col_num =  cur_pos[COL] - 1
            for row_num in range(cur_pos[ROW] + 1, next_pos[ROW] + 1):
                tmp_pos = board[row_num][cur_col_num]
                cur_col_num-=1
                print(tmp_pos)

                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(row_num, ROW, player, next_pos, piece_at_next_location)
                else:
                    if (row_num == next_pos[ROW]):
                        return True
    else:
        print("Illegal move for a Queen")
        return False
        
def bishop_rule_checker(board, player, cur_pos, next_pos, piece_at_next_location):
    #UP and LEFT
    if ((cur_pos[ROW] > next_pos[ROW]) and (cur_pos[COL] > next_pos[COL])):
        if ((cur_pos[ROW] - next_pos[ROW]) == (cur_pos[COL] - next_pos[COL])):
            col_num =  cur_pos[COL] - 1
            for row_num in range (cur_pos[ROW] - 1, next_pos[ROW] - 1,  -1):
                tmp_pos = board[row_num][col_num]
                col_num-=1
                print(tmp_pos)

                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(row_num, ROW, player, next_pos, piece_at_next_location)
                else:
                    if (row_num == next_pos[ROW]):
                        return True
    #DOWN and RIGHT
    elif ((cur_pos[ROW] < next_pos[ROW]) and (cur_pos[COL] < next_pos[COL])):
        if ((next_pos[ROW] - cur_pos[ROW]) == (next_pos[COL] - cur_pos[COL])):
            col_num =  cur_pos[COL] + 1
            for row_num in range (cur_pos[ROW] + 1, next_pos[ROW] + 1):
                tmp_pos = board[row_num][col_num]
                col_num+=1
                print(tmp_pos)

                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(row_num, ROW, player, next_pos, piece_at_next_location)
                else:
                    if (row_num == next_pos[ROW]):
                        return True
    #UP and RIGHT
    elif ((cur_pos[ROW] > next_pos[ROW]) and (cur_pos[COL] < next_pos[COL])):
        if ((cur_pos[ROW] - next_pos[ROW]) == (next_pos[COL] - cur_pos[COL])):
            cur_row_num =  cur_pos[ROW] - 1
            for col_num in range(cur_pos[COL] + 1, next_pos[COL] + 1):
                tmp_pos = board[cur_row_num][col_num]
                cur_row_num-=1
                print(tmp_pos)

                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(col_num, COL, player, next_pos, piece_at_next_location)
                else:
                    if (col_num == next_pos[COL]):
                        return True
    #DOWN and LEFT
    elif ((cur_pos[ROW] < next_pos[ROW]) and (cur_pos[COL] > next_pos[COL])):
        if ((cur_pos[COL] - next_pos[COL]) == (next_pos[ROW] - cur_pos[ROW])):
            cur_col_num =  cur_pos[COL] - 1
            for row_num in range(cur_pos[ROW] + 1, next_pos[ROW] + 1):
                tmp_pos = board[row_num][cur_col_num]
                cur_col_num-=1
                print(tmp_pos)

                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(row_num, ROW, player, next_pos, piece_at_next_location)
                else:
                    if (row_num == next_pos[ROW]):
                        return True
    else:
        print("Illegal move for a Bishop")
        return False
        


def knight_rule_checker(player, cur_pos, next_pos, piece_at_next_location):
    #knight can move into next_pos if the value is 0 or is_opposite
    if (piece_at_next_location == PieceType.EMPTY) or (is_opposite_piece(player, piece_at_next_location.value)):
        if cur_pos[ROW] == next_pos[ROW] + 2: #UP
            if cur_pos[COL] == next_pos[COL] + 1: #LEFT
                return True
            elif cur_pos[COL] == next_pos[COL] - 1: #RIGHT
                return True
            else:
                return False    
        elif cur_pos[ROW] == next_pos[ROW] - 2: #DOWN
            if cur_pos[COL] == next_pos[COL] + 1: #LEFT
                return True
            elif cur_pos[COL] == next_pos[COL] - 1: #RIGHT
                return True
            else:
                return False
        elif cur_pos[COL] == next_pos[COL] + 2: #LEFT
            if cur_pos[ROW] == next_pos[ROW] + 1: #UP
                return True
            elif cur_pos[ROW] == next_pos[ROW] - 1: #DOWN
                return True
            else:
                return False      
        elif cur_pos[COL] == next_pos[COL] - 2: #RIGHT
            if cur_pos[ROW] == next_pos[ROW] + 1: #UP
                return True
            elif cur_pos[ROW] == next_pos[ROW] - 1: #DOWN
                return True
            else:
                return False   
        else:
            return False
    else:
        print("Illegal move for a Knight")
        return False

def rook_rule_checker(board, player, cur_pos, next_pos, piece_at_next_location):
    # UP or DOWN movement
    if cur_pos[COL] == next_pos[COL]:
        if cur_pos[ROW] < next_pos[ROW]: #DOWN
            # loop over each piece in ascending order untill non zero value is reached
            for i in range (cur_pos[ROW] + 1, next_pos[ROW] + 1):
                tmp_pos = board[i][cur_pos[COL]]
                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(i, ROW, player, next_pos, piece_at_next_location)
                else:
                    if (i == next_pos[ROW]):
                        return True
        else: # UP
            # loop over each piece in descending order untill non zero value is reached
            for i in range (cur_pos[ROW] - 1, next_pos[ROW] - 1,  -1):
                tmp_pos = board[i][cur_pos[COL]]
                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(i, ROW, player, next_pos, piece_at_next_location)
                else:
                    if (i == next_pos[ROW]):
                        return True
                       
    elif cur_pos[ROW] == next_pos[ROW]: # LEFT or RIGHT movement
        if cur_pos[COL] < next_pos[COL]: # RIGHT
            for i in range (cur_pos[COL] + 1, next_pos[COL] + 1):
                tmp_pos = board[cur_pos[ROW]][i]
                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(i, COL, player, next_pos, piece_at_next_location)
                else:
                    if (i == next_pos[COL]):
                        return True
        else: # LEFT
            for i in range (cur_pos[COL] - 1, next_pos[COL] - 1,  -1):
                tmp_pos = board[cur_pos[ROW]][i]
                if (tmp_pos != PieceType.EMPTY):
                    # is final position == to this non zero value position
                    return row_col_move_good(i, COL, player, next_pos, piece_at_next_location)
                else:
                    if (i == next_pos[COL]):
                        return True
    else:
        print("Illegal move for a ROOK!")
        return False

def pawn_rule_checker(player, cur_pos, next_pos, piece_at_next_location)->bool:
    # move_dir = move_dir_finder(cur_pos, next_pos)
    # print(move_dir) #How can I use this?
  
    if player == "W":
        print("Player White")
        # Can only go up and capture diagonally
            # Step left to capture
        if (next_pos[ROW] == (cur_pos[ROW] - 1)) and (next_pos[COL] == (cur_pos[COL] - 1)):
            return is_opposite_piece(player, piece_at_next_location.value)
        elif (next_pos[ROW] == (cur_pos[ROW] - 1)) and (next_pos[COL] == cur_pos[COL]):
            if (piece_at_next_location == PieceType.EMPTY):
                print("Forward move once")
                return True
            # Step right to capture
        elif (next_pos[ROW] == (cur_pos[ROW] - 1)) and (next_pos[COL] == (cur_pos[COL] + 1)):
            return is_opposite_piece(player, piece_at_next_location.value)
        elif ((cur_pos[ROW] == 6) and # For initial double move
               (next_pos[ROW] == (cur_pos[ROW] - 2)) and
                cur_pos[COL] == next_pos[COL]):
                print("Move double")
                return True
    elif player == "B":
        print("Player Black")
            # Step left to capture
        if (next_pos[ROW] == (cur_pos[ROW] + 1)) and (next_pos[COL] == (cur_pos[COL] + 1)):
            return is_opposite_piece(player, piece_at_next_location.value)
            # Forward move
        elif (next_pos[ROW] == (cur_pos[ROW] + 1)) and (next_pos[COL] == cur_pos[COL]):
            if (piece_at_next_location == PieceType.EMPTY):
                print("Forward move once")
                return True
                # Step right to capture
        elif (next_pos[ROW] == (cur_pos[ROW] + 1)) and (next_pos[COL] == (cur_pos[COL] - 1)):
            return is_opposite_piece(player, piece_at_next_location.value)
        elif ((cur_pos[ROW] == 1) and # For initial double move
               (next_pos[ROW] == (cur_pos[ROW] + 2)) and
                cur_pos[COL] == next_pos[COL]):
                print("Move double")
                return True
    else:
        print("No such player")
    return False
