from .Game import Game

from .Figure import Figure
from .Position import Position

standard_heavy_figures = [
    "Rook",
    "Knight",
    "Bishop",
    "Queen",
    "King",
    "Bishop",
    "Knight",
    "Rook",
]

standard_game_figures = [
    # White
    *[(Figure.create(f), Position(0, i)) for i, f in enumerate(standard_heavy_figures)],
    *[(Figure.create("Pawn"), Position(1, i)) for i in range(8)],
    #  Black
    *[(Figure.create("Pawn", white=False), Position(6, i)) for i in range(8)],
    *[
        (Figure.create(f, white=False), Position(7, i))
        for i, f in enumerate(standard_heavy_figures)
    ],
]


class GameStandard(Game):
    def __init__(self):
        super().__init__()
        for fig, pos in standard_game_figures:
            self._board.set_figure(fig, pos)

    def __str__(self):
        return "Шахматы"