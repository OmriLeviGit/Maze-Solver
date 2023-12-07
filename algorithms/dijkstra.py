import numpy as np
from Heap import Heap
from enum import Enum


# Dijkstra

class State(Enum):
    NOT_FOUND = 0
    FOUND = 1
    VISITED = 2


def solve(maze):
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

        if curr is maze.end:
            is_completed = True
            break

        for n in curr.neighbors:
            if n is None or visited[n.coordinates] == State.VISITED.value:
                continue

            # mark neighbor as found and push it to the heap
            if visited[n.coordinates] != State.FOUND.value:
                visited[n.coordinates] = State.FOUND.value
                heap.push(n)

            # distance from start to neighbor through current node
            temp_distance = curr.distance + n.distance_to(curr)

            if n.distance <= temp_distance:
                continue

            # if distance is shorter, update the distance and parent of neighbor.
            heap.update_distance(temp_distance, n)
            parent_dict[n] = curr

    path = []
    curr = end
    while curr in parent_dict:
        path.append(curr.coordinates)
        curr = parent_dict.get(curr)


    return path, is_completed
