
from .Position import Position
from .Figure import Figure


class Move:
    def __init__(
        self,
        figure: Figure,
        source: Position,
        target: Position,
        beats_figure: Figure | None = None,
    ):
        self.figure = figure
        self.source = source
        self.target = target
        self.beats = beats_figure
        self.check = False
        self.check_mate = False
        self.pate = False

