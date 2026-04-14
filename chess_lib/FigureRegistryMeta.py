from abc import ABCMeta


class FigureRegistryMeta(ABCMeta):
    registry = {}

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if name != "Figure":
            FigureRegistryMeta.registry[name] = cls