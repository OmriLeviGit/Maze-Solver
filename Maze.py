import numpy as np


class Maze:
    class Node:
        def __init__(self, coordinates):
            self.coordinates = coordinates
            self.neighbors: list = [None] * 4

        def distance_to(self, other):
            """
            Calculate the Manhattan distance between two nodes in a grid-based system.

            Since the Euclidean distance considers straight lines that may not be applicable in grid-based movement,
            and can overestimate the path for the A* algorithm, the Manhattan distance is used.
            """
            y_n1, x_n1 = self.coordinates
            y_n2, x_n2 = other.coordinates

            return abs(y_n2 - y_n1) + abs(x_n2 - x_n1)  # Manhattan distance


    def __init__(self, image):
        self._array = np.array(image.point(lambda pixel: 255 if pixel > 127 else 0), dtype=np.uint8)
        self._start = None
        self._end = None
        self._nodes = []

        rows, columns = self._array.shape
        top_dict = {}  # maps x_value to the closed junction from above

        # Process the first row
        for i in range(columns):
            if self._array[0][i]:
                self._start = Maze.Node((0, i))
                self._nodes.append(self._start)
                top_dict[self._start.coordinates[1]] = self._start
                break

        # find junctions and attach neighbors
        top_dict = {self._start.coordinates[1]: self._start}  # maps x value to the closed junction from above

        for i in range(1, rows - 1):
            node_left = None  # node that will use as a left neighbor for future nodes

            for j in range(1, columns - 1):
                curr = self._array[i][j]

                # hit a wall
                if not curr:
                    top_dict.pop(j, None)
                    node_left = None
                    continue

                top_neighbor = self._array[i - 1][j] != 0
                bottom_neighbor = self._array[i + 1][j] != 0
                right_neighbor = self._array[i][j + 1] != 0
                left_neighbor = self._array[i][j - 1] != 0

                # if cell is not a junction, continue
                if not ((top_neighbor or bottom_neighbor) and (right_neighbor or left_neighbor)):
                    continue

                curr_node = Maze.Node((i, j))
                node_above = top_dict.pop(j, None)

                # attach current to the closed junction from the top
                if node_above:
                    curr_node.neighbors[0] = node_above
                    node_above.neighbors[2] = curr_node

                # attach current to the closed junction from the left
                if node_left:
                    curr_node.neighbors[3] = node_left
                    node_left.neighbors[1] = curr_node

                top_dict[j] = curr_node
                node_left = curr_node
                self._nodes.append(curr_node)


        # Process the last row
        for i in range(columns):
            if self._array[rows - 1][i]:
                self._end = Maze.Node((rows - 1, i))
                self._nodes.append(self._end)

                node_above = top_dict.pop(i, None)
                self._end.neighbors[0] = node_above
                node_above.neighbors[2] = self._end
                break


@property
def array(self):
    return self._array

@property
def start(self):
    return self._start

@property
def end(self):
    return self._end


@property
def nodes(self):
    return self._nodes
