from enum import Enum


class Piece:
    Color = Enum('colors', ('white', 'black'))

    def __init__(self, color, kind):
        self._color = color
        self._kind = kind

    def getColor(self):
        return self._color

    def getKind(self):
        return self._kind