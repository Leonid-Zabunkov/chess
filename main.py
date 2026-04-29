import asyncio

from tkinter import Tk
from chess_lib.StartWindow import ChessSettings

from chess_lib.DB import add_sample_puzzles
from chess_lib.Game_Puzzle import GamePuzzle
from chess_lib.Game_Standard import GameStandard
from chess_lib.Game_Fisher import GameFisher
from chess_lib.Player import HumanPlayer


async def console_set():
    # Для добавления тестовых данных в бд
    # add_sample_puzzles()

    game = GameStandard()
    # game = GamePuzzle.get(2)
    # game = GameFisher()
    timer_w = 500  # int(input("Введите время игры для белых "))
    timer_b = 400  # int(input("Введите время игры для чёрных "))
    white = HumanPlayer("Max", white=True, timer=timer_w)
    black = HumanPlayer("Leon", white=False, timer=timer_b)

    await game.start(white, black)


def get_game_settings():
    root = Tk()
    root.geometry("300x300")
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

        mode = data["mode"]
        if mode == "standard":
            game = GameStandard()
        elif mode == "fisher":
            game = GameFisher()
        elif mode == "puzzle":
            game = GamePuzzle.get(data["puzzle_id"])
        else:
            game = GameStandard()

        # 3. Создаем игроков
        white = HumanPlayer(data["white"], white=True, timer=data["time_w"])
        black = HumanPlayer(data["black"], white=False, timer=data["time_b"])

        # 4. Запускаем асинхронную игру
        print(f"Запуск игры: {mode} ({data['white']} vs {data['black']})")
        await game.start(white, black)


# При импорте мейна в другой файл, он не запустится сам, а будет ждать вызова
if __name__ == "__main__":
    asyncio.run(main())
