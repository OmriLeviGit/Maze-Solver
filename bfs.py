from queue import Queue

import numpy as np


def solve(maze):
    start = maze.start
    end = maze.end
    is_completed = False
    parent_dict = {}

    visited = np.zeros(maze.array.shape)

    queue = Queue()
    queue.put(start)
    visited[start.coordinate] = 1

    while queue.not_empty:
        curr = queue.get()
        visited[curr.coordinate] = 1
        neighbors = curr.neighbors

        for neighbor in neighbors:
            if neighbor is None or visited[neighbor.coordinate] == 1:
                continue

            parent_dict[neighbor] = curr
            queue.put(neighbor)

            if neighbor is end:
                is_completed = True
                break

        if is_completed:
            break

        if queue.empty():
            return -1

    path = []
    curr = end

    while curr in parent_dict:
        path.append(curr.coordinate)
        curr = parent_dict.get(curr)

    path.append(start.coordinate)       # add the first

    return path, is_completed
