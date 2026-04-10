from abc import ABC, abstractmethod
from Position import Position
from Queen import Queen
from Pawn import Pawn


class Figure(ABC):
    def __init__(self, white=True):
        self.__white = white
        self.pos: Position | None = None

    @property
    def white(self):
        return self.__white

    def __str__(self) -> str:
        return self.__name__ 

    @abstractmethod
    def draw_console(self) -> str:
        return "?"

    @abstractmethod
    def can_move(self, position: Position, target: Position):
        pass

    # У пешки != can_move
    @abstractmethod
    def can_beat(self, position: Position, target: Position):
        pass

    # *args превратиться в tuple
    @abstractmethod
    def move(self, *args, target_figure: "Figure | None" = None):
        pass

    def _normalize_pos(self, *args):
        if len(args) == 2:
            return Position(args[0], args[1])
        return args[0]

    # Превращение пешки )))
    def __add__(self, figure: "str | Figure"):

        registry = {"queen": Queen, "rook": Rook, "knight": Knight, "bishop": Bishop}

        if isinstance(figure, Figure):
            new_class = figure.__class__

        elif isinstance(figure, str):
            target_key = figure.lower()
            if target_key in registry:
                new_class = registry[target_key]
            else:
                print(
                    f"Ошибка: Фигура {figure} не существует. Создаём Ферзя по умолчанию"
                )
                new_class = Queen

        elif isinstance(figure, type):
            new_class = figure

        else:
            return NotImplemented

        return new_class(self.white, self.pos)

    def __eq__(self, other):
        if isinstance(other, Figure):
            return self.pos == other.pos
        return False


# Допилить взятие
class Rook(Figure):
    def move(self, *args, target_figure=None):
        new_pos = self._normalize_pos(*args)
        new_x, new_y = new_pos
        if self.pos.x == new_pos.x or self.pos.y == new_pos.y:
            self.pos.x, self.pos.y = new_pos.x, new_pos.y
            return True
        return False


class Knight(Figure):
    def move(self, *args, target_figure=None):
        pass


class Bishop(Figure):
    def move(self, *args, target_figure=None):
        pass
