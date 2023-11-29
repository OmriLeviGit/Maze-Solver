from queue import Queue

import numpy as np


def solve(maze):
    entrances = maze.entrances
    start = entrances[0]
    end_nodes = []
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
            if neighbor in entrances:
                end_nodes.append(neighbor)

    curr = end_nodes.pop()

    while curr in parent_dict:
        print(curr.coordinate)
        curr = parent_dict.get(curr)
