from collections import deque

import numpy as np


# Breadth First Search

def solve(maze):
    start = maze.start
    end = maze.end
    is_completed = False
    parent_dict = {}

    # Create a boolean array 'visited' to keep track of visited locations in the maze
    visited = np.full(maze.array.shape, False, dtype=bool)

    n_queue = deque()
    n_queue.append(start)
    visited[start.coordinate] = True

    while n_queue:
        curr = n_queue.popleft()
        visited[curr.coordinate] = True
        neighbors = curr.neighbors

        for neighbor in neighbors:
            if neighbor is None or visited[neighbor.coordinate]:
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
        path.append(curr.coordinate)
        curr = parent_dict.get(curr)

    path.append(start.coordinate)  # add the start to the path

    return path, is_completed
