from typing import override

from .Figure import Figure


class King(Figure):
    @override
    def print(self):
        return "♚" if self.white else "♔"
