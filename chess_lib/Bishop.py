from typing import override

from Figure import Figure


class Bishop(Figure):
    @override
    def draw_console(self):
        return "♗" if self.white else "♝"
