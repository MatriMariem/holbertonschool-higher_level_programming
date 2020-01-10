#!/usr/bin/python3
class MagicClass:

    def __init__(self, radius):
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self._MagicClass__radius = radius

    def area(self):
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        return (2 * math.pi) * self._MagicClass__radius
