from typing import override

from Figure import Figure


class Knight(Figure):
    @override
    def draw_console(self):
        return "♘" if self.white else "♞"

