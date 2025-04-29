from chess_data_structures import Player, MoveType, PieceType, ROW, COL, board, MIN_ROW, MIN_COL, MAX_ROW, MAX_COL
from typing import List, Tuple

knight_moves = [
    (2, 1), (1, 2),
    (-1, 2), (-2, 1),
    (-2, -1), (-1, -2),
    (1, -2), (2, -1)
]

def is_opposite_piece(player, piece):
    if (player == "W") and (piece >= 7 and piece <= 12):
        return True
    elif (player == "B") and (piece >= 1 and piece <= 6):
        return True
    else:
        return False

def find_king(board:List[List[PieceType]], player)->Tuple[int, int]:
    for row in range(0, 8):
        for col in range(0, 8):
            piece = board[row][col]
            if (player == "W") and (piece == PieceType.WHITE_KING):
                print(piece)
                return (row, col)
            elif (player == "B") and (piece == PieceType.BLACK_KING):
                print(piece)
                return (row, col)

def is_king_checked(board:List[List[PieceType]], player, pos:tuple)->bool:

    #search up
    piece = search_up(board, pos)
    checked =  king_checked_by_queen_or_rook(piece, player)
    if checked:
        return True
    
    piece = search_up_right(board, pos)
    checked =  king_checked_by_queen_or_bishop(piece, player)
    if checked:
        return True
    
    piece = search_right(board, pos)
    checked =  king_checked_by_queen_or_rook(piece, player)
    if checked:
        return True
    

    piece = search_down_right(board, pos)
    checked =  king_checked_by_queen_or_bishop(piece, player)
    if checked:
        return True

    piece = search_down(board, pos)
    checked =  king_checked_by_queen_or_rook(piece, player)
    if checked:
        return True
    

    piece = search_down_left(board, pos)
    checked =  king_checked_by_queen_or_bishop(piece, player)
    if checked:
        return True

    piece = search_left(board, pos)
    checked =  king_checked_by_queen_or_rook(piece, player)
    if checked:
        return True
    
    piece = search_up_left(board, pos)
    checked =  king_checked_by_queen_or_bishop(piece, player)
    if checked:
        return True
    

    knight_attack_pieces = search_knight_attack(board, pos)

def king_checked_by_queen_or_rook(piece:PieceType, player:str)->bool:
    if player == "W":
        if ((piece ==  PieceType.BLACK_QUEEN) or
            (piece ==  PieceType.BLACK_ROOK)):
            print(f"Illegal move: {player} King is checked by {piece}!")
            return True
    else:
        if ((piece ==  PieceType.WHITE_QUEEN) or
            (piece ==  PieceType.WHITE_ROOK)):
            print(f"Illegal move: {player} King is checked by {piece}!")
            return True
    return False

def king_checked_by_queen_or_bishop(piece:PieceType, player:str)->bool:
    if player == "W":
        if ((piece ==  PieceType.BLACK_QUEEN) or
            (piece ==  PieceType.BLACK_BISHOP)):
            print(f"Illegal move: {player} King is checked by {piece}!")
            return True
    else:
        if ((piece ==  PieceType.WHITE_QUEEN) or
            (piece ==  PieceType.WHITE_BISHOP)):
            print(f"Illegal move: {player} King is checked by {piece}!")
            return True
    return False

#Search UP
def search_up(board:List[List[PieceType]], pos:tuple)->PieceType:
    row_num = pos[ROW] - 1
    while row_num >= MIN_ROW:
        piece = board[row_num][pos[COL]]
        if piece != PieceType.EMPTY:
            return piece
        else:
            row_num -= 1
    return PieceType.EMPTY

#Search UP_RIGHT
def search_up_right(board:List[List[PieceType]], pos:tuple)->PieceType:
    row_num = pos[ROW] - 1
    col_num = pos[COL] + 1

    while row_num >= MIN_ROW and col_num <= MAX_COL:
        piece = board[row_num][col_num]
        if piece != PieceType.EMPTY:
            return piece
        else:
            row_num -= 1
            col_num += 1

    return PieceType.EMPTY

#Search RIGHT
def search_right(board:List[List[PieceType]], pos:tuple)->PieceType:
    col_num = pos[COL] + 1
    while col_num <= MAX_COL:
        piece = board[pos[ROW]][col_num]
        if piece != PieceType.EMPTY:
            return piece
        else:
            col_num += 1

    return PieceType.EMPTY


#Search DOWN_RIGHT
def search_down_right(board:List[List[PieceType]], pos:tuple)->PieceType:
    row_num = pos[ROW] + 1
    col_num = pos[COL] + 1

    while row_num <= MAX_ROW and col_num <= MAX_COL:
        piece = board[row_num][col_num]
        if piece != PieceType.EMPTY:
            return piece
        else:
            row_num += 1
            col_num += 1

    return PieceType.EMPTY


#Search DOWN
def search_down(board:List[List[PieceType]], pos:tuple)->PieceType:
    row_num = pos[ROW] + 1
    while row_num <= MAX_ROW:
        piece = board[row_num][pos[COL]]
        if piece != PieceType.EMPTY:
            return piece
        else:
            row_num += 1

    return PieceType.EMPTY

#Search DOWN_LEFT
def search_down_left(board:List[List[PieceType]], pos:tuple)->PieceType:
    row_num = pos[ROW] + 1
    col_num = pos[COL] - 1

    while row_num <= MAX_ROW and col_num >= MIN_COL:
        piece = board[row_num][col_num]
        if piece != PieceType.EMPTY:
            return piece
        else:
            row_num += 1
            col_num -= 1

    return PieceType.EMPTY


#Search LEFT
def search_left(board:List[List[PieceType]], pos:tuple)->PieceType:
    col_num = pos[COL] - 1
    while col_num >= MIN_COL:
        piece = board[pos[ROW]][col_num]
        if piece != PieceType.EMPTY:
            return piece
        else:
            col_num -= 1

    return PieceType.EMPTY

#Search UP_LEFT
def search_up_left(board:List[List[PieceType]], pos:tuple)->PieceType:
    row_num = pos[ROW] - 1
    col_num = pos[COL] - 1

    while row_num >= MIN_ROW and col_num >= MIN_COL:
        piece = board[row_num][col_num]
        if piece != PieceType.EMPTY:
            return piece
        else:
            row_num -= 1
            col_num -= 1

    return PieceType.EMPTY

def search_knight_attack(board:List[List[PieceType]], pos:tuple)->list:
    knight_attack_pieces = []
    for move in knight_moves:
        knight_move_row = pos[ROW] + move[ROW]
        knight_move_col = pos[COL] + move[COL]
        if (MIN_ROW <= knight_move_row <= MAX_ROW) and (MIN_COL <= knight_move_col <= MAX_COL):
            # knight_attack_positions.append((knight_move_row, knight_move_col ))
            piece = board[knight_move_row][knight_move_col]
            if (piece == PieceType.BLACK_KNIGHT) or (piece == PieceType.WHITE_KNIGHT):
                knight_attack_pieces.append(piece)

    return knight_attack_pieces

        

def king_check_checker(board:List[List[PieceType]], player: str, cur_pos:tuple, next_pos:tuple)->bool:
    """
        Need to check if king will be in check if moves to next_pos.
        King can't move to a position where it can be targeted by an opposite piece
    """
    #UP
    if (cur_pos[COL] == next_pos[COL]) and ( cur_pos[ROW] > next_pos[ROW]):
        piece, row_num = search_up(board, next_pos)
        is_opposite = is_opposite_piece(player, piece.value)
        if is_opposite:                    
            if ((row_num == next_pos[ROW] - 1) and ((piece == PieceType.WHITE_KING) or (piece == PieceType.BLACK_KING)) ):
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
                
    #UP_LEFT CI this one still need fixed.
    if (cur_pos[COL] > next_pos[COL]) and ( cur_pos[ROW] > next_pos[ROW]):
        piece, row_num = search_up_left(board, next_pos)
        is_opposite = is_opposite_piece(player, piece.value)
        if is_opposite:                    
            if ((row_num == next_pos[ROW] - 1) and ((piece == PieceType.WHITE_KING) or (piece == PieceType.BLACK_KING)) ):
                print("Illegal Move: Kings cannot be next to each other!")
                return False
            else:        
                if ((piece ==  PieceType.BLACK_QUEEN) or
                    (piece ==  PieceType.WHITE_QUEEN) or
                    (piece ==  PieceType.BLACK_BISHOP) or
                    (piece == PieceType.WHITE_BISHOP)):
                    print(f"Illegal move: {player} King is checked by {piece}!")
                    return False
                else:
                    return True
        else:
            return True

    #DOWN_RIGHT
    if ((cur_pos[ROW] < next_pos[ROW]) and (cur_pos[COL] < next_pos[COL])):
        piece, row_num = search_down_right(board, next_pos)
        is_opposite = is_opposite_piece(player, piece.value)
        if is_opposite:                    
            if ((row_num == next_pos[ROW] + 1) and ((piece == PieceType.WHITE_KING) or (piece == PieceType.BLACK_KING)) ):
                print("Illegal Move: Kings cannot be next to each other!")
                return False
            else:        
                if ((piece ==  PieceType.BLACK_QUEEN) or
                    (piece ==  PieceType.WHITE_QUEEN) or
                    (piece ==  PieceType.BLACK_BISHOP) or
                    (piece == PieceType.WHITE_BISHOP)):
                    print(f"Illegal move: {player} King is checked by {piece}!")
                    return False
                else:
                    return True
        else:
            return True
        

    #LEFT Need to work on this some more, seems to be reversed         
    if (cur_pos[ROW] == next_pos[ROW]) and ( cur_pos[COL] > next_pos[COL]):
       is_checked = is_king_checked(board, player, next_pos)
       if is_checked:
           return False
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

