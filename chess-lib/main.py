# --- ПРОВЕРКА ---
# Создаем так:
import Position
import Queen
import Pawn


start_pos = Position(3, 3)
q = Queen("Black", start_pos)

# Или в одну строку (используя дефолт в Position):
p = Pawn("White", Position(3, 2))

q.draw()  # Общий метод
q.move(5, 5)  # Специфичный метод (диагональ)

# Демонстрация перегрузки оператора сравнения
if q == p:
    print("Фигуры столкнулись!")
else:
    print("Клетки разные.")

# Демонстрация сложения (создание новой фигуры)
super_piece = q + p
print(f"Результат сложения: {type(super_piece).__name__} {super_piece.color}")
