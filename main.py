import asyncio

from chess_lib.DB import add_sample_puzzles
from chess_lib.Game_Puzzle import GamePuzzle
from chess_lib.Game_Standard import GameStandard
from chess_lib.Game_Fisher import GameFisher
from chess_lib.Player import HumanPlayer

# add_sample_puzzles()

# game = GameStandard()
# game = GameFisher()
game = GamePuzzle.random()

timer_w = 30 # int(input("Введите время игры для белых "))
timer_b = 30 # int(input("Введите время игры для чёрных "))
white = HumanPlayer("Max", white=True, timer=timer_w)
black = HumanPlayer("Leon", white=False, timer=timer_b)

asyncio.run(game.start(white, black))
