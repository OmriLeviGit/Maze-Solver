import unittest

import numpy as np
from queue import Queue


from Maze import Maze
from PIL import Image as Im


class NeighborDetection(unittest.TestCase):
    def setUp(self):
        self.small_maze = Maze(Im.open("img/small_perfect.bmp").convert("L"))
        self.medium_maze = Maze(Im.open("img/medium_perfect.bmp").convert("L"))

    def test_small_perfect(self):
        array = self.small_maze.array
        nodes = self.small_maze.nodes

        for node in nodes:
            x, y = node.coordinate
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
        self.assertEquals(len(nodes), 14)

    def test_medium_perfect(self):
        array = self.medium_maze.array
        nodes = self.medium_maze.nodes

        for node in nodes:
            x, y = node.coordinate
            array[x, y] = 127

        expected = np.array(
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0, 0, 0, 0, 0],
             [0, 127, 255, 127, 0, 127, 255, 255, 255, 127, 0, 127, 255, 127, 255, 127, 0, 127, 255, 127, 0],
             [0, 255, 0, 255, 0, 255, 0, 0, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0],
             [0, 255, 0, 255, 0, 127, 255, 127, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0],
             [0, 0, 0, 255, 0, 0, 0, 255, 0, 255, 0, 255, 0, 255, 0, 0, 0, 255, 0, 255, 0],
             [0, 127, 255, 127, 0, 127, 255, 127, 0, 127, 255, 127, 0, 255, 0, 127, 255, 127, 0, 255, 0],
             [0, 255, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 255, 0, 255, 0, 0, 0, 255, 0],
             [0, 127, 255, 127, 0, 127, 255, 127, 0, 127, 255, 255, 0, 255, 0, 255, 0, 127, 255, 127, 0],
             [0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 0, 0, 255, 0, 255, 0, 255, 0, 0, 0],
             [0, 255, 0, 255, 0, 255, 0, 255, 0, 127, 255, 255, 255, 127, 255, 127, 0, 127, 255, 127, 0],
             [0, 0, 0, 255, 0, 255, 0, 255, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0],
             [0, 127, 255, 127, 0, 255, 0, 255, 0, 127, 255, 127, 0, 255, 255, 255, 255, 127, 255, 127, 0],
             [0, 255, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0, 0],
             [0, 255, 0, 255, 0, 255, 0, 127, 255, 127, 255, 127, 0, 127, 255, 255, 255, 127, 0, 255, 0],
             [0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0],
             [0, 127, 255, 127, 255, 127, 0, 255, 0, 127, 255, 255, 0, 127, 255, 255, 255, 255, 255, 127, 0],
             [0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 255, 0, 127, 255, 127, 255, 127, 0, 127, 255, 255, 255, 127, 0, 127, 255, 255, 255, 127, 0],
             [0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 0, 0, 255, 0, 255, 0, 0, 0, 255, 0],
             [0, 127, 255, 127, 0, 255, 0, 127, 255, 127, 0, 255, 255, 127, 255, 127, 0, 255, 255, 127, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0, 0, 0, 0, 0]], dtype=np.uint8
        )

        np.testing.assert_array_equal(array, expected)
        self.assertEquals(len(nodes), 64)



if __name__ == '__main__':
    unittest.main()
