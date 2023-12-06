import unittest

import numpy as np

from Maze import Maze
from PIL import Image as Im


class JunctionDetection(unittest.TestCase):
    def setUp(self):
        self.small_maze = Maze(Im.open("input/11x11, Tiny.bmp").convert("L"))

    def test_small_perfect(self):
        array = self.small_maze.array
        nodes = self.small_maze.nodes

        for node in nodes:
            x, y = node.node
            array[x, y] = 127

        expected = np.array(
            [[0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 127, 255, 255, 255, 255, 255, 255, 255, 127, 0],
             [0, 255, 0, 0, 0, 0, 0, 0, 0, 255, 0],
             [0, 255, 0, 127, 255, 255, 255, 127, 0, 255, 0],
             [0, 255, 0, 255, 0, 0, 0, 255, 0, 0, 0],
             [0, 255, 0, 255, 0, 255, 0, 127, 255, 127, 0],
             [0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0],
             [0, 127, 255, 127, 0, 127, 255, 127, 0, 255, 0],
             [0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0],
             [0, 255, 255, 127, 0, 255, 255, 255, 255, 127, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0]], dtype=np.uint8)

        np.testing.assert_array_equal(array, expected)



if __name__ == '__main__':
    unittest.main()
