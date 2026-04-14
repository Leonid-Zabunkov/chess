class GameError(ValueError):
    def __init__(self, message: str, figure=None, target_pos=None):
        super().__init__(message)
        self.figure = figure
        self.target_pos = target_pos

    def __str__(self):
        base_msg = super().__str__()
        details = f" [Figure: {self.figure}, Target: {self.target_pos}]" if self.figure else ""
        return f"Ошибка игры: {base_msg}{details}"
    
class MoveError(GameError):
    """Ошибка логики хода"""
    pass

class PositionError(GameError):
    """Ошибка указания координат фигуры"""
    pass

class FigureError(GameError):
    """Ошибка указания фигуры"""
    pass