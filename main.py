import asyncio

from chess_lib.Game_Standard import GameStandard
from chess_lib.Game_Fisher import GameFisher
from chess_lib.Player import HumanPlayer

game = GameStandard()

white = HumanPlayer("Max", white=True, timer=600)
black = HumanPlayer("Leon", white=False, timer=300)

asyncio.run(game.start(white, black))
