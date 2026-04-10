from typing import override

from Figure import Figure


class Pawn(Figure):
    @override
    def draw_console(self):
        return "♙" if self.white else "♟"
