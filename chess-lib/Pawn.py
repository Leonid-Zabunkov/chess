from Figure import Figure


class Pawn(Figure):
    def move(self, *args, target_figure: Figure = None):
        new_pos = self._normalize_pos(*args)
        new_x, new_y = new_pos

        # Доделать. Пока что: пешка только вперед на 1
        new_x, new_y = new_pos
        if new_x == self.pos.x and new_y == self.pos.y + 1:
            self.pos.x, self.pos.y = new_x, new_y
            print(f"Пешка шагнула вперед в {self.pos}")
        else:
            print("Неверный ход для пешки.")
