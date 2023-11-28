import unittest

import numpy as np

from Maze import Maze
from PIL import Image as Im


class NeighborDetection(unittest.TestCase):
    def setUp(self):
        self.tiny_maze = Maze(Im.open("img/11x11.bmp").convert("L"))

    def test_tiny(self):
        array = self.tiny_maze.array
        nodes = self.tiny_maze.nodes

        for node in nodes:
            x, y = node.coordinate
            array[x, y] = 127

        expected = np.array([[0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 127, 255, 255, 255, 255, 255, 255, 255, 127, 0],
                             [0, 255, 0, 0, 0, 0, 0, 0, 0, 255, 0],
                             [0, 255, 0, 127, 255, 255, 255, 127, 0, 255, 0],
                             [0, 255, 0, 255, 0, 0, 0, 255, 0, 0, 0],
                             [0, 255, 0, 255, 0, 255, 0, 127, 255, 127, 0],
                             [0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0],
                             [0, 127, 255, 127, 0, 127, 255, 127, 0, 255, 0],
                             [0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0],
                             [0, 255, 255, 127, 0, 255, 255, 255, 255, 127, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0]])

        np.testing.assert_array_equal(array, expected)


if __name__ == '__main__':
    unittest.main()
