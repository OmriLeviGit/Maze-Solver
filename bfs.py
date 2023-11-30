from queue import Queue

import numpy as np


def solve(maze):
    start = maze.start
    end = maze.end
    is_completed = False
    parent_dict = {}

    visited = np.zeros(maze.array.shape)

    n_queue = Queue()
    n_queue.put(start)
    visited[start.coordinate] = 1

    while n_queue.not_empty:
        curr = n_queue.get()
        visited[curr.coordinate] = 1
        neighbors = curr.neighbors

        for neighbor in neighbors:
            if neighbor is None or visited[neighbor.coordinate] == 1:
                continue

            parent_dict[neighbor] = curr
            n_queue.put(neighbor)

            if neighbor is end:
                is_completed = True
                break

        if is_completed:
            break

        if n_queue.empty():
            return -1

    path = []
    curr = end

    while curr in parent_dict:
        path.append(curr.coordinate)
        curr = parent_dict.get(curr)

    path.append(start.coordinate)       # add the start to the path

    return path, is_completed
