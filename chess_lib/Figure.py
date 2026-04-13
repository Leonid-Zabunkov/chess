from abc import ABC, abstractmethod
from .Position import Position


class Figure(ABC):
    def __init__(self, white=True):
        self.__white = white

    @property
    def white(self):
        return self.__white

    def __str__(self) -> str:
        return ("White " if self.white else "Black ") + self.__class__.__name__

    @abstractmethod
    def print(self) -> str:
        return "?"

    # @abstractmethod
    def can_move(self, position: Position, target: Position):
        pass

    # У пешки != can_move
    # @abstractmethod
    def can_beat(self, position: Position, target: Position):
        pass

    # *args превратиться в tuple
    # @abstractmethod
    def move(self, *args, target_figure: "Figure | None" = None):
        pass
