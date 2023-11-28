import numpy as np


class Maze:
    class Node:
        def __init__(self, coordinate):
            self.coordinate = coordinate
            self.neighbors = [None, None, None, None]

    def __init__(self, image):
        self._array = np.array(image.point(lambda pixel: 255 if pixel > 127 else 0))
        self._entrances = self._find_entrances()
        self._nodes = self._find_nodes()

    def _find_entrances(self):
        entrances = []

        # iterate over the first and last rows
        for i in [0, self._array.shape[0] - 1]:
            for j in range(self._array.shape[1]):
                if self._array[i][j]:
                    entrances.append((i, j))

        # iterate over the first and last columns
        for i in range(1, self._array.shape[0] - 1):
            for j in [0, self._array.shape[1] - 1]:
                if self._array[i][j]:
                    entrances.append((i, j))

        return entrances

    def _find_nodes(self):
        def process_node(i, j, neighbor_type):
            if self._array[i][j]:
                curr = Maze.Node((i, j))

                # find if each neighbor exists
                top_neighbor = self._array[i - 1][j] != 0
                right_neighbor = self._array[i][j + 1] != 0
                bottom_neighbor = self._array[i + 1][j] != 0
                left_neighbor = self._array[i][j - 1] != 0

                # if a junction was found
                if (top_neighbor or bottom_neighbor) and (right_neighbor or left_neighbor):
                    if neighbor_type == 'top':
                        # attach top neighbor and current to each other
                        if top_nodes:
                            top, index = top_nodes[-1]
                            if index == j:
                                curr.neighbors[0] = top
                                top.neighbors[2] = curr
                                top_nodes.pop()
                        top_nodes.append((curr, j))

                    elif neighbor_type == 'left':
                        # attach left neighbor and current to each other
                        if left_nodes:
                            left = left_nodes.pop()
                            curr.neighbors[3] = left
                            left.neighbors[1] = curr
                        left_nodes.append(curr)

                    nodes.append(curr)

        nodes = []
        rows, columns = self._array.shape

        top_nodes = []  # nodes that will be top neighbors for future nodes
        left_nodes = []  # nodes that will be left neighbors for future nodes

        # Process the first row
        for i in range(columns):
            if self._array[0][i]:
                entrance = Maze.Node((0, i))
                top_nodes.append((entrance, i))
                nodes.append(entrance)

        for i in range(1, rows - 1):
            for j in range(columns):
                process_node(i, j, 'top')
                process_node(i, j, 'left')

            left_nodes = []  # reset on every new row

        # Process the last row
        for i in range(columns):
            if self._array[rows - 1][i]:
                end = Maze.Node((rows - 1, i))
                if top_nodes:
                    top, index = top_nodes[-1]
                    if index == i:
                        end.neighbors[0] = top
                        top.neighbors[2] = end
                        top_nodes.pop()
                nodes.append(end)

        return nodes

    """
        ### my version, the other one is gpt based
        # def _find_nodes(self):
        #     nodes = []
        #     rows = self._array.shape[0]
        #     columns = self._array.shape[1]
        #
        #     top_nodes = []  # nodes that will be top neighbors for future nodes
        #     left_nodes = []  # nodes that will be left neighbors for future nodes
        #     top_index = 0  # num of column of the last node in the top_nodes
        #
        #     # first row
        #     for i in range(columns):
        #         if self._array[0][i]:
        #             entrance = Maze.Node((0, i))
        #             top_nodes.append((entrance, i))
        #             nodes.append(entrance)
        #             continue
        #
        #     for i in range(1, rows - 1):
        #         for j in range(columns):
        #             if self._array[i][j]:
        #                 # find if each neighbors exist
        #                 top_neighbor = True if self._array[i - 1][j] != 0 else False
        #                 right_neighbor = True if self._array[i][j + 1] != 0 else False
        #                 bottom_neighbor = True if self._array[i + 1][j] != 0 else False
        #                 left_neighbor = True if self._array[i][j - 1] != 0 else False
        #
        #                 # if a junction was found
        #                 if (top_neighbor or bottom_neighbor) and (right_neighbor or left_neighbor):
        #                     curr = Maze.Node((i, j))
        #
        #                     # attach top neighbor and current to each other, and pop top from the list
        #                     if top_nodes:
        #                         top, index = top_nodes[-1]
        #                         if index == j:
        #                             curr.neighbors[0] = top
        #                             top.neighbors[2] = curr
        #                             top_nodes.pop()
        #
        #                     # attach left neighbor and current to each other
        #                     if left_nodes:
        #                         left = left_nodes.pop(-1)
        #                         curr.neighbors[3] = left
        #                         left.neighbors[1] = curr
        #
        #                     top_nodes.append((curr, top_index))
        #                     left_nodes.append(curr)
        #                     nodes.append(curr)
        #
        #             top_index += 1
        #
        #         left_nodes = []  # reset on every new row
        #         top_index = 0  # reset on every new row
        #
        #     # last row
        #     for i in range(columns):
        #         if self._array[rows - 1][i]:
        #             end = Maze.Node((rows - 1, i))
        #             if top_nodes:
        #                 top, index = top_nodes[-1]
        #                 if index == i:
        #                     end.neighbors[0] = top
        #                     top.neighbors[2] = end
        #                     top_nodes.pop()
        #
        #             nodes.append(end)
        #
        #     return nodes
    """

    @property
    def array(self):
        return self._array

    @property
    def entrances(self):
        return self._entrances

    @property
    def nodes(self):
        return self._nodes

