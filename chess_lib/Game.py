import asyncio
import concurrent.futures

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
        self._turn_white = True
        self._history = MoveHistory()

    def print(self, clear=True):

        board = self._board.print(border=True)
        moves = self._history.print(len(board), notation.move_to_str)
        res = []
        for i, row in enumerate(board):
            if i < len(moves):
                res.append(row + "    " + moves[i])
            else:
                res.append(row)
        return f"{"-"*80}\n{str(self)}\nРаунд: {self._round:<3} {' ' * (len(board[0]) - 5)} История ходов:\n{'\n'.join(res)}"

    def game_over(self, move: Move | None):
        fig = str(move.beats)
        return fig.endswith("King")

    @property
    def result(self):
        return f"Победили {'белые' if self._turn_white else 'чёрные'} на {self._round} ходу"

    def prepare(self, game_time=10):
        self.__game_over = False
        self._history.clear()
        self.total_timer_task = asyncio.create_task(self.start_timer(game_time))

    async def next_turn(self) -> None | Move:
        try:
            user_move = await get_user_input(self._turn_white)
            src, tgt = notation.move(user_move)
            return self._board.apply_move(src, tgt)
        except GameError as e:
            print(f"Неверный ход! {e}")
            return None

    async def start(self, game_time=10 * 60):
        self.prepare(game_time)

        while True:
            print(self.print())
            real_move = await self.next_turn()
            if not real_move:
                continue

            self._history + real_move

            if self.game_over(real_move):
                self.__game_over = True
                break

            self._turn_white = not self._turn_white
            if self._turn_white:
                self._round += 1

            print("\033[F" * 17, end="")  # возврат каретки вверх на 16 строк

        self.finish()

    def finish(self):
        self.total_timer_task.cancel()
        print(self.print())
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
