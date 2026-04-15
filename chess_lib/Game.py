import asyncio
import concurrent.futures

from .Player import Player
from .Logging import log_call
from .PrintableMixin import PrintableMixin
from .GameError import GameError
from .Board import Board
from .Move import MoveHistory, Move
from . import Notation as notation


async def get_user_input(white=True):
    turn_str = "белых" if white else "черных"

    loop = asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, input, f"Ход {turn_str}:\n")


class Game(PrintableMixin):
    def __init__(self):
        self._board = Board()
        self._round = 1
        self._history = MoveHistory()

    def print(self):
        players = f"{self._white_player.print()}\n{self._black_player.print()}"
        board = self._board.print(border=True)
        moves = self._history.print(len(board), notation.move_to_str)
        res = []
        for i, row in enumerate(board):
            if i < len(moves):
                res.append(row + "    " + moves[i])
            else:
                res.append(row)
        return f"{"-"*80}\n{str(self)}\n{players}\n{"-"*80}\nРаунд: {self._round:<3} {' ' * (len(board[0]) - 8)} История ходов:\n{'\n'.join(res)}"

    def game_over(self, move: Move | None):
        fig = str(move.beats)
        return fig.endswith("King")

    @property
    def result(self):
        return f"Победили {'белые' if self._turn_white else 'чёрные'} на {self._round} ходу"

    @log_call
    def prepare(self, game_time=10):
        self.__game_over = False
        self._history.clear()
        self.total_timer_task = asyncio.create_task(self.start_timer(game_time))

    @log_call
    async def next_turn(self) -> None | Move:
        try:
            turn = await self._player.make_turn(self._board)
            src, tgt = notation.move(turn)
            return self._board.apply_move(src, tgt)
        except GameError as e:
            print(f"Неверный ход! {e}")
            return None

    @log_call
    async def start(self, white_player: Player, black_player: Player):
        self._white_player = white_player
        self._black_player = black_player
        self._player = white_player
        print(self.print())

        while True:
            real_move = await self.next_turn()
            if not real_move:
                continue

            self._history + real_move

            if self.game_over(real_move):
                self.__game_over = True
                break

            self.switch_player()

            # print("\033[F" * 19, end="")  # возврат каретки вверх на 16 строк
            print(self.print())

        self.finish()
        
    def switch_player(self):
        if self._player == self._white_player:
            self._player = self._black_player
        else:
            self._player = self._white_player
            self._round += 1


    def finish(self):
        self.total_timer_task.cancel()
        print(self.result)

    async def start_timer(self, seconds=10):
        try:
            while seconds > 0 and not self.__game_over:
                print(
                    f"                   [Времени осталось: {seconds}с]                ",
                    end="\r",
                )
                await asyncio.sleep(1)
                seconds -= 1
            if seconds <= 0:
                print("\nВремя вышло! Проигрыш.")
        except asyncio.CancelledError:
            pass
