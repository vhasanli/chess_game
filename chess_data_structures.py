from enum import Enum

class PieceType(Enum):
    EMPTY = 0
    WHITE_PAWN = 1
    WHITE_KNIGHT = 2
    WHITE_BISHOP = 3
    WHITE_ROOK = 4
    WHITE_QUEEN = 5
    WHITE_KING = 6
    BLACK_PAWN = 7
    BLACK_KNIGHT = 8
    BLACK_BISHOP = 9
    BLACK_ROOK = 10
    BLACK_QUEEN = 11
    BLACK_KING = 12


class MoveType(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    UP_LEFT = 4
    UP_RIGHT = 5
    DOWN_LEFT = 6
    DOWN_RIGHT = 7

class Player(Enum):
    WHITE = 0
    BLACK = 1


# board = [
#     [PieceType.BLACK_ROOK, PieceType.black_knight.value, PieceType.black_bishop.value, PieceType.black_queen.value, PieceType.black_king.value, PieceType.black_bishop.value, PieceType.black_knight.value, PieceType.black_rook.value],  # 8th rank (black pieces)
#     [PieceType.black_pawn.value, PieceType.black_pawn.value, PieceType.black_pawn.value, PieceType.black_pawn.value, PieceType.black_pawn.value, PieceType.black_pawn.value, PieceType.black_pawn.value, PieceType.black_pawn.value],  # 7th rank
#     [PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value],  # Empty squares
#     [PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value],
#     [PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value],
#     [PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value, PieceType.empty.value],
#     [PieceType.white_pawn.value, PieceType.white_pawn.value, PieceType.white_pawn.value, PieceType.white_pawn.value, PieceType.white_pawn.value, PieceType.white_pawn.value, PieceType.white_pawn.value, PieceType.white_pawn.value],  # 2nd rank (white pieces)
#     [PieceType.white_rook.value, PieceType.white_knight.value, PieceType.white_bishop.value, PieceType.white_queen.value, PieceType.white_king.value, PieceType.white_bishop.value, PieceType.white_knight.value, PieceType.white_rook.value]   # 1st rank
# ]


correct_board = [
    [PieceType.BLACK_ROOK, PieceType.BLACK_KNIGHT, PieceType.BLACK_BISHOP, PieceType.BLACK_QUEEN, PieceType.BLACK_KING, PieceType.BLACK_BISHOP, PieceType.BLACK_KNIGHT, PieceType.BLACK_ROOK],  # 8th rank (black pieces)
    [PieceType.BLACK_PAWN, PieceType.BLACK_PAWN, PieceType.BLACK_PAWN, PieceType.BLACK_PAWN, PieceType.BLACK_PAWN, PieceType.BLACK_PAWN, PieceType.BLACK_PAWN, PieceType.BLACK_PAWN],  # 7th rank
    [PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY],  # Empty squares
    [PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY],
    [PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY],
    [PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY],
    [PieceType.WHITE_PAWN, PieceType.WHITE_PAWN, PieceType.WHITE_PAWN, PieceType.WHITE_PAWN, PieceType.WHITE_PAWN, PieceType.WHITE_PAWN, PieceType.WHITE_PAWN, PieceType.WHITE_PAWN],  # 2nd rank (white pieces)
    [PieceType.WHITE_ROOK, PieceType.WHITE_KNIGHT, PieceType.WHITE_BISHOP, PieceType.WHITE_QUEEN, PieceType.WHITE_KING, PieceType.WHITE_BISHOP, PieceType.WHITE_KNIGHT, PieceType.WHITE_ROOK]   # 1st rank
]

board = [
    [PieceType.BLACK_ROOK, PieceType.BLACK_KNIGHT, PieceType.BLACK_BISHOP, PieceType.BLACK_QUEEN, PieceType.EMPTY, PieceType.BLACK_BISHOP, PieceType.BLACK_KNIGHT, PieceType.BLACK_ROOK],  # 8th rank (black pieces)
    [PieceType.BLACK_PAWN, PieceType.BLACK_PAWN, PieceType.BLACK_PAWN, PieceType.EMPTY, PieceType.BLACK_PAWN, PieceType.BLACK_PAWN, PieceType.BLACK_PAWN, PieceType.BLACK_PAWN],  # 7th rank
    [PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY],  # Empty squares
    [PieceType.EMPTY, PieceType.EMPTY, PieceType.WHITE_KING, PieceType.WHITE_QUEEN, PieceType.EMPTY, PieceType.BLACK_KING, PieceType.EMPTY, PieceType.EMPTY],
    [PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.BLACK_KING, PieceType.BLACK_QUEEN],
    [PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.EMPTY, PieceType.BLACK_KING, PieceType.BLACK_KING, PieceType.EMPTY, PieceType.EMPTY],
    [PieceType.WHITE_PAWN, PieceType.WHITE_PAWN, PieceType.WHITE_PAWN, PieceType.WHITE_PAWN, PieceType.WHITE_PAWN, PieceType.WHITE_PAWN, PieceType.WHITE_PAWN, PieceType.WHITE_PAWN],  # 2nd rank (white pieces)
    [PieceType.WHITE_ROOK, PieceType.WHITE_KNIGHT, PieceType.WHITE_BISHOP, PieceType.WHITE_QUEEN, PieceType.EMPTY, PieceType.WHITE_BISHOP, PieceType.WHITE_KNIGHT, PieceType.WHITE_ROOK]   # 1st rank
]

ROW = 0
COL = 1

MIN_ROW = 0
MIN_COL = 0
MAX_ROW = 7
MAX_COL = 7