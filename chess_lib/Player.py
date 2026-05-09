from abc import abstractmethod

from .PrintableMixin import PrintableMixin
from .Board import Board
from .Position import Position


class Player(PrintableMixin):
    def __init__(self, name: str, white=True):
        self.name = name
        self.white = white

    def print(self):
        return f"Белые: {self.name}" if self.white else f"Черные: {self.name}"

    @abstractmethod
    def make_turn(self, board: Board) -> tuple[Position, Position]:
        pass
