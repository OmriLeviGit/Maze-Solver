from collections import deque

import numpy as np


# Breadth First Search

def solve(maze):
    is_completed = False

    start = maze.start
    end = maze.end
    parent_dict = {start: None}

    n_queue = deque()
    n_queue.append(start)

    # Create a boolean array 'visited' to keep track of visited locations in the maze
    visited = np.full(maze.array.shape, False, dtype=bool)

    while n_queue:
        curr = n_queue.popleft()
        visited[curr.coordinates] = True
        neighbors = curr.neighbors

        for neighbor in neighbors:
            if neighbor is None or visited[neighbor.coordinates]:
                continue

            parent_dict[neighbor] = curr
            n_queue.append(neighbor)

        if curr.coordinates == end.coordinates:
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

    return path, is_completed
