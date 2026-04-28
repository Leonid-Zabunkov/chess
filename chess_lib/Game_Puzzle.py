from .DB import ChessPuzzle, get_puzzle, get_random_puzzle

from .Game import Game

from .Figure import Figure
from .Position import Position

figure_factories = {
    "k": lambda: Figure.create("King", white=True),
    "K": lambda: Figure.create("King", white=False),
    "q": lambda: Figure.create("Queen", white=True),
    "Q": lambda: Figure.create("Queen", white=False),
}


class GamePuzzle(Game):
    def __init__(self, puzzle: ChessPuzzle):
        super().__init__()
        self.__puzzle = puzzle
        self._white_turn = puzzle.white_turn
        
        lines = puzzle.board.split("/")
        for x, line in enumerate(lines):
            for y, f in enumerate(line):
                fig_factory = figure_factories.get(f)
                if not fig_factory: continue
                self._board.set_figure(fig_factory(), Position(x, y))

    def __str__(self):
        return f"Задача {self.__puzzle.id}. Ход {"белых" if self._white_turn else "черных"}. Мат в {self.__puzzle.moves_to_win} ход(а)."
    
    @staticmethod
    def random():
        puzzle = get_random_puzzle()
        return GamePuzzle(puzzle)
    
    @staticmethod
    def get(index: int):
        puzzle = get_puzzle(index)
        return GamePuzzle(puzzle)
