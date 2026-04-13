from typing import override

from .Figure import Figure


class Queen(Figure):
    @override
    def print(self):
        return "♕" if self.white else "♛"
