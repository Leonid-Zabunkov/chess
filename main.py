import asyncio

from chess_lib.Game_Standard import GameStandard
from chess_lib.Game_Fisher import GameFisher
from chess_lib.Game_Puzzle import GamePuzzle
from chess_lib.Player import HumanPlayer


async def main(game_mode, id):
    match game_mode:
        case None:
            game = GameStandard()
        case "standard":
            game = GameStandard()
        case "fisher":
            game = GameFisher()
        case "chess960":
            game = GameFisher()
        case "puzzle":
            game = GamePuzzle.random()
        case "puzzle_id":
            game = GamePuzzle.get(int(id))

    white = HumanPlayer("Max", white=True)
    black = HumanPlayer("Leon", white=False)

    await game.start(white, black)


# При импорте мейна в другой файл, он не запустится сам, а будет ждать вызова
if __name__ == "__main__":
    asyncio.run(main())
