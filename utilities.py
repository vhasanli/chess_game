from chess_data_structures import Player, MoveType, PieceType, ROW, COL, board, MIN_ROW, MIN_COL, MAX_ROW, MAX_COL
from typing import List, Tuple

def is_opposite_piece(player, piece_at_next_location):
    if (player == "W") and (piece_at_next_location >= 7 and piece_at_next_location <= 12):
        return True
    elif (player == "B") and (piece_at_next_location >= 1 and piece_at_next_location <= 6):
        return True
    else:
        return False

#Search UP
def search_up(board:List[List[PieceType]], next_pos:tuple)->Tuple[PieceType, int]:
    row_num = next_pos[ROW] - 1
    while row_num >= MIN_ROW:
        piece = board[row_num][next_pos[COL]]
        if piece != PieceType.EMPTY:
            return piece, row_num
        else:
            row_num -= 1

    return PieceType.EMPTY, -1

#Search UP_LEFT Need to test this
def search_up_left(board:List[List[PieceType]], next_pos:tuple)->Tuple[PieceType, int]:
    row_num = next_pos[ROW] - 1
    col_num = next_pos[COL] - 1

    while row_num >= MIN_ROW or col_num >= MIN_COL:
        piece = board[row_num][col_num]
        if piece != PieceType.EMPTY:
            return piece, col_num
        else:
            row_num -= 1
            col_num -= 1

    return PieceType.EMPTY, -1

#Search DOWN
def search_down(board:List[List[PieceType]], next_pos:tuple)->Tuple[PieceType, int]:
    row_num = next_pos[ROW] + 1
    while row_num >= MAX_ROW:
        piece = board[row_num][next_pos[COL]]
        if piece != PieceType.EMPTY:
            return piece, row_num
        else:
            row_num += 1

    return PieceType.EMPTY, -1
        
#Search LEFT
def search_left(board:List[List[PieceType]], next_pos:tuple)->Tuple[PieceType, int]:
    col_num = next_pos[COL] - 1
    while col_num >= MIN_COL:
        piece = board[next_pos[ROW]][col_num]
        if piece != PieceType.EMPTY:
            return piece, col_num
        else:
            col_num -= 1

    return PieceType.EMPTY, -1


#Search RIGHT
def search_right(board:List[List[PieceType]], next_pos:tuple)->Tuple[PieceType, int]:
    col_num = next_pos[COL] + 1
    while col_num <= MAX_COL:
        piece = board[next_pos[ROW]][col_num]
        if piece != PieceType.EMPTY:
            return piece, col_num
        else:
            col_num += 1

    return PieceType.EMPTY, -1

        

def king_check_checker(board:List[List[PieceType]], player: str, cur_pos:tuple, next_pos:tuple)->bool:
    """
        Need to check if king will be in check if moves to next_pos.
        King can't move to a position where it can be targeted by an opposite piece
    """
    #UP
    if (cur_pos[COL] == next_pos[COL]) and ( cur_pos[ROW] > next_pos[ROW]):
        piece, index = search_up(board, next_pos)
        is_opposite = is_opposite_piece(player, piece.value)
        if is_opposite:                    
            if ((index == next_pos[ROW] - 1) and ((piece == PieceType.WHITE_KING) or (piece == PieceType.BLACK_KING)) ):
                print("Illegal Move: Kings cannot be next to each other!")
                return False
            else:        
                if ((piece ==  PieceType.BLACK_QUEEN) or
                    (piece ==  PieceType.WHITE_QUEEN) or
                    (piece ==  PieceType.BLACK_ROOK) or
                    (piece == PieceType.WHITE_ROOK)):
                    print(f"Illegal move: {player} King is checked by {piece}!")
                    return False
                else:
                    return True
        else:
            return True
                
    #UP_LEFT CI this one still need fixed.
    if (cur_pos[COL] > next_pos[COL]) and ( cur_pos[ROW] > next_pos[ROW]):
        piece, col_num = search_up_left(board, next_pos)
        is_opposite = is_opposite_piece(player, piece.value)
        if is_opposite:                    
            if ((col_num == next_pos[COL] - 1) and ((piece == PieceType.WHITE_KING) or (piece == PieceType.BLACK_KING)) ):
                print("Illegal Move: Kings cannot be next to each other!")
                return False
            else:        
                if ((piece ==  PieceType.BLACK_QUEEN) or
                    (piece ==  PieceType.WHITE_QUEEN) or
                    (piece ==  PieceType.BLACK_ROOK) or
                    (piece == PieceType.WHITE_ROOK)):
                    print(f"Illegal move: {player} King is checked by {piece}!")
                    return False
                else:
                    return True
        else:
            return True

    #DOWN            
    if (cur_pos[COL] == next_pos[COL]) and ( cur_pos[ROW] < next_pos[ROW]):
        piece, index = search_down(board, next_pos)
        is_opposite = is_opposite_piece(player, piece.value)
        if is_opposite:                    
            if ((index == next_pos[ROW] + 1) and ((piece == PieceType.WHITE_KING) or (piece == PieceType.BLACK_KING)) ):
                print("Illegal Move: Kings cannot be next to each other!")
                return False
            else:        
                if ((piece ==  PieceType.BLACK_QUEEN) or
                    (piece ==  PieceType.WHITE_QUEEN) or
                    (piece ==  PieceType.BLACK_ROOK) or
                    (piece == PieceType.WHITE_ROOK)):
                    print(f"Illegal move: {player} King is checked by {piece}!")
                    return False
                else:
                    return True
        else:
            return True
        

    #LEFT          
    if (cur_pos[ROW] == next_pos[ROW]) and ( cur_pos[COL] > next_pos[COL]):
        piece, index = search_left(board, next_pos)
        is_opposite = is_opposite_piece(player, piece.value)
        if is_opposite:                    
            if ((index == next_pos[COL] - 1) and ((piece == PieceType.WHITE_KING) or (piece == PieceType.BLACK_KING)) ):
                print("Illegal Move: Kings cannot be next to each other!")
                return False
            else:        
                if ((piece ==  PieceType.BLACK_QUEEN) or
                    (piece ==  PieceType.WHITE_QUEEN) or
                    (piece ==  PieceType.BLACK_ROOK) or
                    (piece == PieceType.WHITE_ROOK)):
                    print(f"Illegal move: {player} King is checked by {piece}!")
                    return False
                else:
                    return True
        else:
            return True
        
    #RIGHT          
    if (cur_pos[ROW] == next_pos[ROW]) and ( cur_pos[COL] < next_pos[COL]):
        piece, index = search_right(board, next_pos)
        is_opposite = is_opposite_piece(player, piece.value)
        if is_opposite:                    
            if ((index == next_pos[COL] + 1) and ((piece == PieceType.WHITE_KING) or (piece == PieceType.BLACK_KING)) ):
                print("Illegal Move: Kings cannot be next to each other!")
                return False
            else:        
                if ((piece ==  PieceType.BLACK_QUEEN) or
                    (piece ==  PieceType.WHITE_QUEEN) or
                    (piece ==  PieceType.BLACK_ROOK) or
                    (piece == PieceType.WHITE_ROOK)):
                    print(f"Illegal move: {player} King is checked by {piece}!")
                    return False
                else:
                    return True
        else:
            return True




def move_dir_finder(cur_pos, next_pos):
    if (cur_pos[ROW] > next_pos[ROW]) and (cur_pos[COL] == next_pos[COL]):
        move_type = MoveType.UP
        print("UP move")
    elif (cur_pos[ROW] < next_pos[ROW]) and (cur_pos[COL] == next_pos[COL]):
        move_type = MoveType.DOWN
        print("DOWN move")
    elif (cur_pos[COL] > next_pos[COL]) and (cur_pos[ROW] == next_pos[ROW]):
        move_type = MoveType.LEFT
        print("LEFT move")
    elif (cur_pos[COL] < next_pos[COL]) and (cur_pos[ROW] == next_pos[ROW]):
        move_type = MoveType.RIGHT
        print("RIGHT move")
    elif (cur_pos[ROW] > next_pos[ROW]) and (cur_pos[COL] > next_pos[COL]):
        move_type = MoveType.UP_LEFT
        print("UP and LEFT diagonal move")
    elif (cur_pos[ROW] < next_pos[ROW]) and (cur_pos[COL] > next_pos[COL]):
        move_type = MoveType.DOWN_LEFT
        print("DOWN and LEFT diagonal move")
    elif (cur_pos[ROW] > next_pos[ROW]) and (cur_pos[COL] < next_pos[COL]):
        move_type = MoveType.UP_RIGHT
        print("UP and RIGHT diagonal move")
    elif (cur_pos[ROW] < next_pos[ROW]) and (cur_pos[COL] < next_pos[COL]):
        move_type = MoveType.DOWN_RIGHT
        print("DOWN and RIGHT diagonal move")

    return move_type

def row_col_move_good(index, row_col, player, next_pos, piece_at_next_location):
    # this function activates when the first non-zero number item is found in a ray
    # check if the final position equals to the non-zero value position
    if (index == next_pos[row_col]):
        # check if the piece belong to the opposite player
        is_opposite = is_opposite_piece(player, piece_at_next_location.value)
        if is_opposite:
            return True
        else:
            print("Cannot capture your own piece")
            return False

    else:
        print("Obstacle: Cannot move over other pieces!")
        return False

