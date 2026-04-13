from typing import override

from .Figure import Figure


class Bishop(Figure):
    @override
    def print(self):
        return "♗" if self.white else "♝"
