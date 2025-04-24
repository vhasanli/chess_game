from chess_data_structures import Player, MoveType, PieceType, ROW, COL, board, MIN_ROW, MIN_COL, MAX_ROW, MAX_COL
from typing import List

def is_opposite_piece(player, piece_at_next_location):
    if (player == "W") and (piece_at_next_location >= 7 and piece_at_next_location <= 12):
        return True
    elif (player == "B") and (piece_at_next_location >= 1 and piece_at_next_location <= 6):
        return True
    else:
        return False

def king_check_checker(board:List[List[PieceType]], player: str, cur_pos:tuple, next_pos:tuple)->bool:
    """
        Need to check if king will be in check if moves to next_pos.
        King can't move to a position where it can be targeted by opposite piece
    """

    #RIGHT
    # check if opposite side king is located in next_pos[COL] + 1
        #if so, can't move there
    piece = board[next_pos[ROW]][next_pos[COL]+1]
    if ((piece == PieceType.WHITE_KING) or (piece == PieceType.BLACK_KING) ):
        print("Illegal Move: Kings cannot be next to each other!")
        return False
    #check the rest of the positions
        #if not empty then see if any is_opposite
            # if is_opposite, ant piece that can have a straigh shot like rook or queen?
    for i in range(next_pos[COL] + 1, MAX_COL + 1):
        piece = board[next_pos[ROW]][i]
        is_opposite = is_opposite_piece(player, piece.value)
        if is_opposite:
            if piece != PieceType.EMPTY:
                if ((piece ==  PieceType.BLACK_QUEEN) or
                    (piece ==  PieceType.WHITE_QUEEN) or
                    (piece ==  PieceType.BLACK_ROOK) or
                    (piece ==  PieceType.WHITE_ROOK)):
                    print(f"Illegal move: {player} King is checked!")
                    return False

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

