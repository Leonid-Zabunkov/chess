from typing import override

from Figure import Figure


class Rook(Figure):
    @override
    def draw_console(self):
        return "♖" if self.white else "♜"
