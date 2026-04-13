from .Bishop import Bishop

from .Rook import Rook
from .Knight import Knight
from .Pawn import Pawn
from .King import King
from .Queen import Queen
from .Board import Board
from .Position import Position
from .Move import MoveHistory, Move
from . import Notation as notation


class Game:
    def __init__(self):
        self.__board: Board
        self.__round = 1
        self.__turn_white = True
        self.__history = MoveHistory()

    @staticmethod
    def standard():
        g = Game()
        g.__board = Board()
        for i in range(8):
            g.__board.set_figure(Pawn(), Position(1, i))
            g.__board.set_figure(Pawn(white=False), Position(6, i))

        g.__board.set_figure(Rook(), Position(0, 0))
        g.__board.set_figure(Knight(), Position(0, 1))
        g.__board.set_figure(Bishop(), Position(0, 2))
        g.__board.set_figure(Queen(), Position(0, 3))
        g.__board.set_figure(King(), Position(0, 4))
        g.__board.set_figure(Bishop(), Position(0, 5))
        g.__board.set_figure(Knight(), Position(0, 6))
        g.__board.set_figure(Rook(), Position(0, 7))

        g.__board.set_figure(Rook(white=False), Position(7, 0))
        g.__board.set_figure(Knight(white=False), Position(7, 1))
        g.__board.set_figure(Bishop(white=False), Position(7, 2))
        g.__board.set_figure(Queen(white=False), Position(7, 3))
        g.__board.set_figure(King(white=False), Position(7, 4))
        g.__board.set_figure(Bishop(white=False), Position(7, 5))
        g.__board.set_figure(Knight(white=False), Position(7, 6))
        g.__board.set_figure(Rook(white=False), Position(7, 7))
        return g

    def __str__(self):
        return f"Game:\n{self.__board}"

    def print(
        self,
    ):
        turn_str = "белых" if self.__turn_white else "черных"
        board = self.__board.print(border=True)
        moves = self.__history.print(len(board), notation.move_to_str)
        res = []
        for i, row in enumerate(board):
            if i < len(moves):
                res.append(row + "    " + moves[i])
            else:
                res.append(row)
        return f"Раунд: {self.__round} {' ' * (len(board[0]) - 5)} История ходов:\n{'\n'.join(res)}\nХод {turn_str}:"

    def game_over(self, move: Move):
        return str(move.beats).endswith("King")

    @property
    def result(self):
        return f"Победили {'белые' if self.__turn_white else 'чёрные'} на {self.__round} ходу"

    def start(self):
        while True:
            print(self.print())
            move = notation.move(input())
            real_move = self.__board.apply_move(*move)
            # is Check | Mate
            # real_move.check = True
            # real_move.pate = True
            # real_move.check_mate = True
            self.__history + real_move

            if self.game_over(real_move):
                break

            self.__turn_white = not self.__turn_white
            if self.__turn_white:
                self.__round += 1

        print(self.print())
        print(self.result)
