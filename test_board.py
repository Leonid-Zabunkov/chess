from chess_lib.Board import Board
from chess_lib.Position import Position
from chess_lib.Figure import Figure  # Или конкретная фигура, например Queen


def test_chess_setup():
    board = Board()

    # Создаем тестовую фигуру (белая пешка/фигура)
    white_king = Figure(white=True)
    pos = Position(0, 0)  # Допустим, Position принимает x, y

    # Тест 1: Установка фигуры
    print("Установка фигуры...")
    success = board.set_figure(white_king, pos)
    print(f"Результат: {'OK' if success else 'FAIL'}")

    # Тест 2: Проверка занятости клетки
    print("\nПроверка занятости (должно быть 'Position is busy'):")
    another_figure = Figure(white=False)
    board.set_figure(another_figure, pos)

    # Тест 3: Получение фигур по цвету
    white_figures = board.get_figures(white=True)
    print(f"\nБелых фигур на доске: {len(white_figures)}")

    # Тест 4: Вывод доски
    print("\nВид доски:")
    print(board)


if __name__ == "__main__":
    test_chess_setup()
