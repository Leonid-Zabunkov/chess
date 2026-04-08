from abc import ABC, abstractmethod
from Position import Position
from Queen import Queen
from Pawn import Pawn


class Figure(ABC):
    def __init__(self, color="white", pos: Position = None):
        self.__color = color
        self.__is_alive = True
        if pos:
            self.pos = Position(pos.x, pos.y)
        else:
            self.pos = Position()

    @property
    def color(self):
        return self.__color

    @property
    def is_alive(self):
        return self.__is_alive

    def draw(self):
        status = "На поле" if self.is_alive else "Взята"
        print(f"Фигура {self.__class__.__name__}({self.color}) сейчас: {status}")

    # *args превратиться в tuple
    @abstractmethod
    def move(self, *args, target_figure: "Figure" = None):
        pass

    def _normalize_pos(self, *args):
        if len(args) == 2:
            return Position(args[0], args[1])
        return args[0]

    def __add__(self, name_or_class):

        registry = {"queen": Queen, "rook": Rook, "knight": Knight, "bishop": Bishop}

        if isinstance(name_or_class, Figure):
            new_class = name_or_class.__class__

        elif isinstance(name_or_class, str):
            target_key = name_or_class.lower()
            if target_key in registry:
                new_class = registry[target_key]
            else:
                print(
                    f"Ошибка: Фигура {name_or_class} не существует. Создаём Ферзя по умолчанию"
                )
                new_class = Queen

        elif isinstance(name_or_class, type):
            new_class = name_or_class

        else:
            return NotImplemented

        return new_class(self.color, self.pos)

    def __eq__(self, other):
        if isinstance(other, Figure):
            return self.pos == other.pos
        return False

    def _die(self):
        self.__is_alive = False
        self.pos.x, self.pos.y = -1, -1

    def _capture(self, target: "Figure"):
        if target.color == self.color:
            print("Своих есть нельзя!")
            return False

        print(f"Взятие: {self.__class__.__name__} съел {target.__class__.__name__}")
        target._die()
        return True


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
