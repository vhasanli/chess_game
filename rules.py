X = 0
Y = 1

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