from typing import override

from Figure import Figure


class King(Figure):
    @override
    def draw_console(self):
        return "♔" if self.white else "♚"
