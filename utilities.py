from chess_data_structures import Player

def is_opposite_piece(player, piece_at_next_location):
    if (player == Player.WHITE) and (piece_at_next_location >= 7 and piece_at_next_location <= 12):
        return True
    elif (player == Player.BLACK) and (piece_at_next_location >= 1 and piece_at_next_location <= 6):
        return True
    else:
        print("No such player or piece")
        return False
