from rules import piece_rule_checker, X, Y
from chess_data_structures import PieceType, board

def pos_to_value():
    pass 

def get_move():

    player = int(input("Enter player: 0 for white, 1 for black: "))
    piece = int(input("Enter piece you'd like to move: "))

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
        board[next_pos[X]][next_pos[Y]] =  board[cur_pos[X]][cur_pos[Y]]
        board[cur_pos[X]][cur_pos[Y]] = 0 # clear old position
        print("Legal Move!")
    else:
        print("Illegal Move!")
    pass

def show_board():
    for row in board:
        print(row)

while True:
    print("############################")
    print("---------Chess Game---------")
    print("############################")
    show_board()

    cur_pos, next_pos, player, piece = get_move()
    
    attempt_move(board, player, piece, cur_pos, next_pos)
