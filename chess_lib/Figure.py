from abc import abstractmethod

from .PrintableMixin import PrintableMixin
from .Position import Position


class Figure(PrintableMixin):
    def __init__(self, white=True):
        self.__white = white

    @property
    def white(self):
        return self.__white

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
