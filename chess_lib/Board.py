from .GameError import MoveError
from .Move import Move
from .Figure import Figure
from .Position import Position


# mixin ??
class FigureOnBoard:
    def __init__(self, figure: Figure, position: Position):
        self.figure = figure
        self.position = position

    def __str__(self):
        return f"{self.figure} at {self.position}"


class Board:
    def __init__(self):
        self.__board: list[list[Figure | None]] = [[None] * 8 for _ in range(8)]

    def apply_move(self, source: Position, target: Position):
        figure = self.get_figure_at_position(source)
        if not figure:
            raise MoveError(f"No figure at position {source}")
        
        self.set_figure(None, source)
        old = self.set_figure(figure, target)
        return Move(figure, source, target, old)

    def set_figure(self, figure: Figure | None, position: Position):
        x, y = position
        old = self.__board[x][y]
        self.__board[x][y] = figure
        return old

    def __str__(self):
        return f"Board with figures:\n{'\n'.join(str(fig) for fig in self.__figures)}"

    def get_figure_at_position(self, position: Position):
        x, y = position
        return self.__board[x][y]
    
    ### Printing Board ###

    def __add_border(self, lines: list[str]):
        res = []
        res.append("╔══════════════════════════════╗")
        for line in lines:
            res.append("║ " + line + " ║")
        res.append("╚══════════════════════════════╝")
        return res

    def print(self, border=False):
        res = []
        res.append("   a  b  c  d  e  f  g  h   ")
        for i, row in enumerate(self.__board):
            row_str = []
            for j, figure in enumerate(row):
                cell = "   " if (i + j) % 2 else "░░░"
                row_str.append((" " + figure.print() + " ") if figure else cell)
            line = f"{i + 1} {''.join(row_str)} {i + 1}"
            res.insert(1, line)
        res.append("   a  b  c  d  e  f  g  h   ")
        if border:
            res = self.__add_border(res)
        return res
