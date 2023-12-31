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

    def remove_push(self, node):
        self.heap.remove(node)
        self.push(node)

    def is_empty(self):
        if len(self.heap) == 0:
            return True
        return False
