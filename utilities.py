from chess_data_structures import Player, MoveType, PieceType, ROW, COL

def is_opposite_piece(player, piece_at_next_location):
    if (player == Player.WHITE) and (piece_at_next_location >= 7 and piece_at_next_location <= 12):
        return True
    elif (player == Player.BLACK) and (piece_at_next_location >= 1 and piece_at_next_location <= 6):
        return True
    else:
        print("No such player or piece")
        return False

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

def move_legal_algo(board, cur_pos, next_pos):
    counter = 0
    for row in range(cur_pos[ROW] - next_pos[ROW]):
        tmp_piece = board[(cur_pos[ROW] - (row + 1))][next_pos[COL]]
        if tmp_piece != PieceType.EMPTY:
            print(f"tmp_piece: {tmp_piece}")
            return counter
        counter+=1
    return counter
