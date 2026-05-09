from chess_lib.Game_Standard import GameStandard
from chess_lib.Game_Fisher import GameFisher
from chess_lib.Player import Player


def main(game_mode="standard"):
    game = GameStandard() if game_mode == "standard" else GameFisher()

    white = Player("Max", white=True)
    black = Player("Leon", white=False)

    game.start(white, black)
