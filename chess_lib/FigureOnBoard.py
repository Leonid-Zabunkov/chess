from .Move import Move
from .Figure import Figure
from .Position import Position


class FigureOnBoard:
    def __init__(self, figure: Figure, position: Position):
        self.figure = figure
        self.position = position

    def __str__(self):
        return f"{self.figure} at {self.position}"

    def __add__(self, other: "FigureOnBoard") -> Move:
        return Move(self.figure, self.position, other.position, other.figure)
