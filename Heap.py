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

    def update_distance(self, distance, node):
        self.heap.remove(node)
        node.distance = distance
        self.push(node)


    def is_empty(self):
        if len(self.heap) == 0:
            return True
        return False
