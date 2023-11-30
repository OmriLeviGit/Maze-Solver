import math


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x}, {self._y})"

    def distance_to(self, other_point):
        """
        Calculate the Euclidean distance between two points.
        """
        dx = self._x - other_point.get_x
        dy = self._y - other_point.get_y
        return math.sqrt(dx ** 2 + dy ** 2)

    def get_x(self):
        return int(self._x)

    def get_y(self):
        return int(self._y)
