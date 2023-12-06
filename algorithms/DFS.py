from collections import deque

import numpy as np


# Depth First Search

def solve(maze):
    end = maze.end
    is_completed = False
    parent_dict = {}

    # Create a boolean array 'visited' to keep track of visited locations in the maze
    visited = np.full(maze.array.shape, False, dtype=bool)

    n_queue = deque()
    n_queue.append(maze.start)
    visited[maze.start.coordinates] = True

    while n_queue:
        curr = n_queue.pop()
        visited[curr.coordinates] = True
        neighbors = curr.neighbors

        for neighbor in neighbors:
            if neighbor is None or visited[neighbor.coordinates]:
                continue

            parent_dict[neighbor] = curr
            n_queue.append(neighbor)

            if neighbor is end:
                is_completed = True
                break

        if is_completed:
            break

        if not n_queue:
            is_completed = False
            end = curr
            break

    path = []
    curr = end

    while curr in parent_dict:
        path.append(curr.coordinates)
        curr = parent_dict.get(curr)

    path.append(maze.start.coordinates)  # add the start to the path

    return path, is_completed
