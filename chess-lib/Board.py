from Figure import Figure
from Position import Position


# mixin ??
class FigureOnBoard:
    def __init__(self, figure: Figure, position: Position):
        self.figure = figure
        self.position = position


class Board:
    def __init__(self):
        self.__figures: list[FigureOnBoard] = []
        self.__board: list[list[Figure | None]] = [[None] * 8 for _ in range(8)]
        pass

    def set_figure(self, figure: Figure, position: Position):
        x, y = position
        if self.__board[x][y]:
            print("Position is busy")
            return False

        self.__figures.append(FigureOnBoard(figure, position))
        self.__board[x][y] = figure
        return True

    def __str__(self):
        return ""  # draw to console

    def get_figures(self, white: bool):
        return [f for f in self.__figures if f.figure.white == white]

    def reset(self):
        self.__init__()
