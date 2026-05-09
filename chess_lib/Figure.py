from abc import abstractmethod

from .GameError import FigureError
from .PrintableMixin import PrintableMixin
from .FigureRegistryMeta import FigureRegistryMeta
from .Position import Position


class Figure(PrintableMixin, metaclass=FigureRegistryMeta):
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

    @staticmethod
    def create(name: str, white=True) -> "Figure":
        cls = FigureRegistryMeta.registry.get(name)
        if not cls:
            available = ", ".join(FigureRegistryMeta.registry.keys())
            raise FigureError(f"Фигура '{name}' не найдена. Доступны: {available}")
        return cls(white)
