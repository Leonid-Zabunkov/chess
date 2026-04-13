from .Position import Position
from .Pawn import Pawn
from .Knight import Knight
from .Bishop import Bishop
from .Rook import Rook
from .Queen import Queen
from .King import King

registry = {"K": King, "Q": Queen, "R": Rook, "B": Bishop, "N": Knight, "P": Pawn}


# Parse d3 -> Position
def position(s: str):
    col, row = s[0:2]
    return Position(ord(row) - ord("1"), ord(col) - ord("a"))


def figure(notation: str):
    white = True
    if notation.startswith("W"):
        white = notation.startswith("W")

    key = notation[-1]
    if key in registry:
        figure_class = registry[key]
        return figure_class(white)

    raise Exception("Incorrect figure")


# Simple notation: d1-h5
def move(turn: str) -> tuple[Position, Position]:
    s = position(turn[0:2])
    t = position(turn[3:5])
    return (s, t)
