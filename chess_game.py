from rules import piece_rule_checker, ROW, COL
from chess_data_structures import PieceType, board

def pos_to_value():
    pass 

def get_move():
    player = input("Enter player: W for white or B for black: ")
    piece = PieceType[input("Enter piece you'd like to move (Ex: WHITE_PAWN): ")]
    # Prompt the user to enter four values (current row, current column, next row, next column)
    move_input = input("Enter current row, current column, next row, next column (e.g., 1 2 3 4): ")
    # Split the input into separate values and convert them to integers
    cur_row, cur_col, next_row, next_col = map(int, move_input.split())
    # Pack row and col into a tuple
    cur_pos = (cur_row, cur_col)
    next_pos = (next_row, next_col)

    return cur_pos, next_pos, player, piece

def attempt_move(board, player, piece, cur_pos, next_pos):
    legal = piece_rule_checker(board, player, piece, cur_pos, next_pos,)

    if legal:
        board[next_pos[ROW]][next_pos[COL]] =  board[cur_pos[ROW]][cur_pos[COL]]
        board[cur_pos[ROW]][cur_pos[COL]] = PieceType.EMPTY # clear old position
        print("Legal Move!")
    else:
        print("Illegal Move!")
    pass

def show_board():
    for row in board:
        for col in row:
            print(col.value, end=' ')
        print()


while True:
    print("############################")
    print("---------Chess Game---------")
    print("############################")
    show_board()

    cur_pos, next_pos, player, piece = get_move()
    
    attempt_move(board, player, piece, cur_pos, next_pos)
