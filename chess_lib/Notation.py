from .Figure import Figure
from .Move import Move
from .Position import Position
from .Pawn import Pawn
from .Knight import Knight
from .Bishop import Bishop
from .Rook import Rook
from .Queen import Queen
from .King import King

__registry = {"K": King, "Q": Queen, "R": Rook, "B": Bishop, "N": Knight, "P": Pawn}


# Parse d3 -> Position
def position(s: str):
    col, row = s[0:2]
    return Position(ord(row) - ord("1"), ord(col) - ord("a"))


def to_str(arg: Position | Figure | Move):
    if isinstance(arg, Position):
        return pos_to_str(arg)

    if isinstance(arg, Figure):
        return fig_to_str(arg)

    if isinstance(arg, Move):
        return move_to_str(arg)


def figure(notation: str):
    white = True
    if notation.startswith("W"):
        white = notation.startswith("W")

    key = notation[-1]
    if key in __registry:
        figure_class = __registry[key]
        return figure_class(white)

    raise Exception("Incorrect figure")


# Simple notation: d1-h5
def move(turn: str) -> tuple[Position, Position]:
    s = position(turn[0:2])
    t = position(turn[3:5])
    return (s, t)


def pos_to_str(pos: Position):
    x, y = pos
    return chr(y + ord("a")) + chr(x + ord("1"))


def fig_to_str(figure: Figure):
    for key, value in __registry.items():
        if value == figure.__class__:
            return key
    return "?"


def move_to_str(move: Move):
    fig = fig_to_str(move.figure)
    source = pos_to_str(move.source)
    target = pos_to_str(move.target)
    type = "x" if move.beats else "-"
    tail = "*" if move.check_mate else "+" if move.check else "#" if move.pate else ""

    return f"{fig}{source}{type}{target}{tail}"
