import numpy as np
from Heap import Heap
from enum import Enum


# Dijkstra

class State(Enum):
    FOUND = 1
    VISITED = 2


def solve(maze):
    end = maze.end
    is_completed = False

    # create a boolean array 'visited' to keep track of visited locations in the maze
    visited = np.zeros(maze.array.shape, dtype=np.uint8)
    parent_dict = {}
    heap = Heap()

    maze.start.distance = 0
    heap.push(maze.start)

    while True:
        if heap.is_empty():
            break

        curr = heap.pop()

        while visited[curr.coordinates] == State.VISITED:
            curr = heap.pop()

        visited[curr.coordinates] = State.VISITED.value

        if curr is maze.end:
            is_completed = True
            break

        print(curr.coordinates)

        for n in curr.neighbors:
            if n is None or visited[n.coordinates] == State.VISITED.value:
                continue

            # mark neighbor as found and push it to the heap
            if visited[n.coordinates] != State.FOUND:
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

    path.append(maze.start.coordinates)  # add the start to the path

    return path, is_completed
