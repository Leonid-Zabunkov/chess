from . import Position, Pawn, Knight, Bishop, Rook, Queen, King

registry = {"K": King, "Q": Queen, "R": Rook, "B": Bishop, "N": Knight, "P": Pawn}


def position(notation: str):
    col, row = notation
    return Position(ord(row) - ord("1"), ord(col) - ord("a"))


def figure(notation: str):
    white = True
    if notation.startswith("W") or notation.startswith("B"):
        white = notation.startswith("W")

    key = notation[-1]
    if key in registry:
        figure_class = registry[key]
        return figure_class(white)
    
    raise Exception("Incorrect figure")

