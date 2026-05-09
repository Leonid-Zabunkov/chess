import asyncio

from tkinter import Tk
from StartWindow import ChessSettings

from chess_lib.Game_Puzzle import GamePuzzle
from chess_lib.Game_Standard import GameStandard
from chess_lib.Game_Fisher import GameFisher
from chess_lib.Player import HumanPlayer


def get_game_by_mode(mode: str, id: int | None):
    match mode:
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
        case _:
            game = GameStandard()

    return game


async def console_set(game_mode: str, id):
    game = get_game_by_mode(game_mode, id)

    white = HumanPlayer("Max", white=True)
    black = HumanPlayer("Leon", white=False)

    await game.start(white, black)


def get_game_settings():
    root = Tk()
    app = ChessSettings(root)
    root.mainloop()

    return app.get_data()


async def main(game_mode="w_mode"):

    if game_mode == "c_set":
        await console_set()

    else:
        data = get_game_settings()

        if not data:
            print("Настройки не были выбраны. Выход.")
            return

        mode = data.get("mode")
        id = data.get("puzzle_id")

        game = get_game_by_mode(mode, id)

        white = HumanPlayer(data["white"], white=True, timer=data["time_w"])
        black = HumanPlayer(data["black"], white=False, timer=data["time_b"])

        print(f"Запуск игры: {mode} ({data['white']} vs {data['black']})")
        await game.start(white, black)


if __name__ == "__main__":
    asyncio.run(main())
