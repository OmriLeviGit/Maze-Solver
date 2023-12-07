import unittest
from Heap import Heap
from Maze import Maze


class HeapFunctionality(unittest.TestCase):
    def setUp(self):
        self.heap = Heap()

    def test_push(self):
        node = Maze.Node((0, 1))

        self.heap.push(node)

        self.assertFalse(self.heap.is_empty())

    def test_pop(self):
        node = Maze.Node((0, 1))

        self.heap.push(node)
        n_node = self.heap.pop()

        self.assertEqual(node, n_node)
        self.assertTrue(self.heap.is_empty())

    def test_update_distance_no_order_change(self):
        node1 = Maze.Node((0, 1))
        node2 = Maze.Node((2, 3))
        node1.distance = 10
        node2.distance = 11

        self.heap.push(node1)
        self.heap.push(node2)

        self.heap.update_distance(9, node1)
        self.heap.update_distance(12, node2)

        n_node1 = self.heap.pop()
        n_node2 = self.heap.pop()

        self.assertEqual(node1, n_node1)
        self.assertEqual(9, n_node1.distance)
        self.assertEqual(node2, n_node2)
        self.assertEqual(12, n_node2.distance)

    def test_update_distance_order_change(self):
        node1 = Maze.Node((0, 1))
        node2 = Maze.Node((2, 3))
        node1.distance = 10
        node2.distance = 11

        self.heap.push(node1)
        self.heap.push(node2)

        self.heap.update_distance(12, node1)
        self.heap.update_distance(9, node2)

        n_node1 = self.heap.pop()
        n_node2 = self.heap.pop()

        # check if the order was swapped according to the new value
        self.assertEqual(node2, n_node1)
        self.assertEqual(9, n_node1.distance)
        self.assertEqual(node1, n_node2)
        self.assertEqual(12, n_node2.distance)
