from Figure import Figure


class Queen(Figure):
    def move(self, *args, target_figure: Figure = None):
        new_pos = self._normalize_pos(*args)
        new_x, new_y = new_pos

        if self.pos == new_pos:
            print("Фигура уже стоит в этой точке!")
            return

        if (
            abs(self.pos.x - new_x) == abs(self.pos.y - new_y)
            or self.pos.x == new_x
            or self.pos.y == new_y
        ):
            if target_figure:
                if self._capture(target_figure):
                    self.pos.x, self.pos.y = new_x, new_y
            else:
                self.pos.x, self.pos.y = new_x, new_y
                print(f"Ферзь переместился в {self.pos}")

        else:
            print("Так Ферзь ходить не может!")
