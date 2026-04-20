from abc import abstractmethod
import asyncio
from typing import override

import concurrent

from .PrintableMixin import PrintableMixin
from .Board import Board
from .Position import Position


class Player(PrintableMixin):
    def __init__(self, name: str, white=True):
        self.name = name
        self.white = white
        
    def print(self):
        return f"Белые: {self.name}" if self.white else f"Черные: {self.name}"

    @abstractmethod
    async def make_turn(slef, board: Board) -> tuple[Position, Position]:
        pass


def time_to_str(timer: int):
    m = timer // 60
    s = timer % 60
    return f"Время {m:02}:{s:02}"


class HumanPlayer(Player):
    def __init__(self, name: str, white=True, timer=600):
        super().__init__(name, white)
        self.timer = timer

    @override
    def print(self):
        s = super().print()
        return f"{s:<20} [{time_to_str(self.timer)}]"

    @override
    async def make_turn(self, board: Board):
        self._timer_task = asyncio.create_task(self.start_timer())
        turn = await self.get_user_input()
        self._timer_task.cancel()
        return turn

    def get_prompt(self):
        turn_str = "белые" if self.white else "черные"
        return f"Ходит {self.name} ({turn_str}) [{time_to_str(self.timer)}]: "

    async def get_user_input(self):
        loop = asyncio.get_event_loop()
        with concurrent.futures.ThreadPoolExecutor() as pool:
            return await loop.run_in_executor(pool, input, self.get_prompt())

    async def start_timer(self):
        try:
            while self.timer > 0:
                # print("\r" + self.get_prompt(), end="")
                await asyncio.sleep(1)
                self.timer -= 1
            if self.timer <= 0:
                print("\nВремя вышло! Проигрыш.")
        except asyncio.CancelledError:
            pass
