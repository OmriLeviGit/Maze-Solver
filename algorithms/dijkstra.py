import numpy as np
from Heap import Heap
from CONST import FOUND, VISITED


# Dijkstra

def solve(maze):
    apply_dijkstra(maze)
    is_completed = False

    start = maze.start
    end = maze.end
    parent_dict = {start: None}

    heap = Heap()
    heap.push(start)

    # create a boolean array 'visited' to keep track of visited locations in the maze
    visited = np.zeros(maze.array.shape, dtype=np.uint8)
    start.cost = 0

    while True:
        if heap.is_empty():
            break

        curr = heap.pop()

        while visited[curr.coordinates] == VISITED:
            curr = heap.pop()

        visited[curr.coordinates] = VISITED

        if curr.coordinates == end.coordinates:
            is_completed = True
            break

        for n in curr.neighbors:
            if n is None or visited[n.coordinates] == VISITED:
                continue

            # distance from start to neighbor through current node
            distance_from_start = curr.cost + n.distance_to(curr)

            if n.cost <= distance_from_start:
                continue

            # if the new distance is shorter, update the distance and parent of neighbor.
            n.cost = distance_from_start
            parent_dict[n] = curr

            # if neighbor was found before, remove it from the heap and heapify to maintain heap property
            if visited[n.coordinates] == FOUND:
                heap.remove_and_heapify(n)

            # mark neighbor as found and push it to the heap
            visited[n.coordinates] = FOUND
            heap.push(n)

    path = []
    curr = end
    while curr in parent_dict:
        path.append(curr.coordinates)
        curr = parent_dict.get(curr)
    return path, is_completed


def apply_dijkstra(maze):
    """
    Adds each node a 'distance' attribute, and a comparator between nodes.
    The cost attribute: the distance from the start node, and is defaulted to 'inf'.
    """

    for n in maze.nodes:
        n.cost = float("inf")

    maze.Node.__lt__ = lambda self, other: self.cost < other.cost
