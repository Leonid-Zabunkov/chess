from typing import Callable

from .Position import Position
from .Figure import Figure


class Move:
    def __init__(
        self,
        figure: Figure,
        source: Position,
        target: Position,
        beats_figure: Figure | None = None,
    ):
        self.figure = figure
        self.source = source
        self.target = target
        self.beats = beats_figure
        self.check = False
        self.check_mate = False
        self.pate = False


class MoveHistory:
    def __init__(self):
        self.__moves: list[Move] = []

    def __add__(self, move: Move):
        self.__moves.append(move)

    @property
    def last(self):
        return self.__moves[-1]

    @property
    def last_white(self):
        last_move = self.__moves[-1]
        if last_move:
            return self.__moves[-1].__figure.white
        return None

    def print(self, rounds: int, move_to_str: Callable[["Move"], str]):
        res = []
        r, i = 0, 0
        s = ""
        while i < len(self.__moves) and r <= rounds:
            if not i % 2:
                s = f"{r + 1}. {move_to_str(self.__moves[i])}"
            else:
                s += " " + move_to_str(self.__moves[i])
                res.append(s)
                r += 1
            i += 1
        if i % 2:
            res.append(s)
        return res
