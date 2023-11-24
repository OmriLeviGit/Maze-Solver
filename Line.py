from Point import Point


class Line:
    def __init__(self, start_point, end_point):
        self._start_point = start_point
        self._end_point = end_point

    def get_start_point(self):
        return self._start_point

    def get_end_point(self):
        return self._end_point

    def length(self):
        dx = self._end_point.get_x() - self._start_point.get_x()
        dy = self._end_point.get_y() - self._start_point.get_y()
        return ((dx ** 2) + (dy ** 2)) ** 0.5

    def middle_point(self):
        """
        Calculate and return the middle point of the line.
        """
        mid_x = int((self._start_point.get_x() + self._end_point.get_x()) / 2)
        mid_y = int((self._start_point.get_y() + self._end_point.get_y()) / 2)
        return Point(mid_x, mid_y)
