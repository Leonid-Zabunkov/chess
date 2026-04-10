from Position import *
from Figure import *

class Move:
    def __init__(self, figure: Figure, source: Position, target: Position):
        self.__figure = figure
        self.__source = source
        self.__target = target

class MoveHistory:
    def __init__(self):
        self.__moves: list[Move] = []

    def __add__(self, move: Move):
        self.__moves.append(move)

    @property
    def last(self):
        self.__moves[-1]
        
    @property
    def last_white(self):
        last_move = self.__moves[-1]
        if last_move:
            return self.__moves[-1].__figure.white
        return None