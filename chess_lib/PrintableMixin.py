class PrintableMixin:
    def __str__(self) -> str:
        color = "White " if self.white else "Black " if self.white == False else ""
        return f"{color}{self.__class__.__name__}"