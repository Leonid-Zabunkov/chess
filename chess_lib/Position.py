class Position:
    def __init__(self, x=0, y=0):
        if isinstance(x, Position):
            self.x, self.y = x.x, x.y
        else:
            self.x = x
            self.y = y


    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

    # Нужно для: x, y = new_position
    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self):
        return f"({self.x}, {self.y})"
