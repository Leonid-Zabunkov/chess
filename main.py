import asyncio

from chess_lib.Game_Standard import GameStandard
from chess_lib.Game_Fisher import GameFisher

game = GameStandard()

asyncio.run(game.start(game_time=5 * 60))
