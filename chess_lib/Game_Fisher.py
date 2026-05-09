import random

from .Position import Position
from .Figure import Figure
from .Game_Standard import GameStandard, standard_heavy_figures


class GameFisher(GameStandard):
    def __init__(self):
        super().__init__() 
        self.__randomize_figures()
        
    def __str__(self):
        return "Шахматы Фишера (960)"
        
    def __randomize_figures(self):
        figures = standard_heavy_figures.copy()
        random.shuffle(figures)
        
        for i, name in enumerate(figures):
            self._board.set_figure(Figure.create(name, white=True), Position(0, i))
            self._board.set_figure(Figure.create(name, white=False), Position(7, i))
