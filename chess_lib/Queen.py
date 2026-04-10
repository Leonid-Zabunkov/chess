from typing import override

from Figure import Figure


class Queen(Figure):
    @override
    def draw_console(self):
        return "♕" if self.white else "♛"
