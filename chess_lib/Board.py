from chess_lib import Move

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
        # Избыточное состояние: надо избавиться
        self.__figures: list[FigureOnBoard] = []
        self.__board: list[list[Figure | None]] = [[None] * 8 for _ in range(8)]

    def apply_move(self, source: Position, target: Position):
        """
        Осуществляет перемещение фигуры с позиции source в позицию target.

        :param source: позиция "откуда"
        :param target: позиция "куда"
        :return: Move - ход с информацией о ходе
        """
        figure = self.get_figure_at_position(source)
        if not figure:
            raise Exception("No figure at position " + source)
        figure2 = self.get_figure_at_position(target)
        self.set_figure(None, source)
        self.set_figure(figure, target)
        return Move(figure, source, target, figure2)

    def set_figure(self, figure: Figure | None, position: Position):
        x, y = position
        if self.__board[x][y]:
            print("Position is busy")
            return False

        self.__figures.append(FigureOnBoard(figure, position))
        self.__board[x][y] = figure
        return True

    def __str__(self):
        return f"Board with figures:\n{'\n'.join(str(fig) for fig in self.__figures)}"

    def get_figures(self, white: bool):
        return [f for f in self.__figures if f.figure.white == white]

    def get_figure_at_position(self, position: Position):
        return [x for x in self.__figures if x.position == position][0]

    def reset(self):
        self.__init__()

    def __add_border(self, lines: list[str]):
        res = []
        res.append("╔══════════════════════════════╗")
        for line in lines:
            res.append("║ " + line + " ║")
        res.append("╚══════════════════════════════╝")
        return res

    def print(self, border=False) -> str:
        res = []
        res.append("   a  b  c  d  e  f  g  h   ")
        for i, row in enumerate(self.__board):
            row_str = []
            for j, figure in enumerate(row):
                cell = "   " if (i + j) % 2 else "░░░"
                row_str.append((" " + figure.print() + " ") if figure else cell)
            line = f"{8 - i} {''.join(row_str)} {8 - i}"
            res.append(line)
        res.append("   a  b  c  d  e  f  g  h   ")
        if border:
            res = self.__add_border(res)
        return "\n".join(res)
