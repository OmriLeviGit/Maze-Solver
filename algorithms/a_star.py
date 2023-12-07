import numpy as np
from Heap import Heap
from enum import Enum


# A Star

class State(Enum):
    NOT_FOUND = 0
    FOUND = 1
    VISITED = 2


def solve(maze):
    apply_a_star(maze)
    is_completed = False



    start = maze.start
    end = maze.end
    parent_dict = {start: None}

    heap = Heap()
    heap.push(start)

    # create a boolean array 'visited' to keep track of visited locations in the maze
    visited = np.zeros(maze.array.shape, dtype=np.uint8)
    start.distance = 0

    while True:
        if heap.is_empty():
            break

        curr = heap.pop()

        while visited[curr.coordinates] == State.VISITED.value:
            curr = heap.pop()

        visited[curr.coordinates] = State.VISITED.value

        if curr.coordinates == end.coordinates:
            is_completed = True
            break

        for n in curr.neighbors:
            if n is None or visited[n.coordinates] == State.VISITED.value:
                continue

            # distance from start to neighbor through current node
            distance_from_start = curr.distance + n.distance_to(curr)

            if n.distance <= distance_from_start:   # if the old distance is smaller, so is the total cost
                continue

            # if the new distance is shorter, update the distance, cost and parent of neighbor.
            n.distance = distance_from_start
            n.total_cost = distance_from_start + n.heuristic
            parent_dict[n] = curr

            # if neighbor was found before, remove it from the heap and push again to reorder the heap
            if visited[n.coordinates] == State.FOUND.value:
                heap.remove_push(n)
                continue

            # mark neighbor as found and push it to the heap
            visited[n.coordinates] = State.FOUND.value
            heap.push(n)

    path = []
    curr = end
    while curr in parent_dict:
        path.append(curr.coordinates)
        curr = parent_dict.get(curr)
    return path, is_completed


def apply_a_star(maze):
    """
    Adds each node, 'distance', 'heuristic' and total cost attributes, and a comparator between nodes.
    The distance attribute: the distance from the start, and is defaulted to 'inf'.
    The heuristic attribute: the estimated distance from the current node to the end node.
    The total cost: the sum of the distance and heuristic
    """

    for n in maze.nodes:
        n.distance = float("inf")
        n.heuristic = n.distance_to(maze.end)
        n.total_cost = float("inf")

    maze.Node.__lt__ = lambda self, other: self.total_cost < other.total_cost
