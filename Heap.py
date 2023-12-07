import heapq


class Heap:
    def __init__(self):
        self.heap = []

    def push(self, node):
        heapq.heappush(self.heap, node)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def update_distance(self, value, node):
        # for some reason using an indices dict instead of remove gave much worse performance,
        # might update in the future
        self.heap.remove(node)
        node.distance = value
        self.push(node)

    def is_empty(self):
        if len(self.heap) == 0:
            return True
        return False
