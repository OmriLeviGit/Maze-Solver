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

    def remove_and_heapify(self, node):
        """
        After extensive testing, it's found that a custom priority queue implementation with a 'decrease key' operation 
        that has log(n) complexity, performs worse compared to using Python's heapq module, despite the
        O(n) complexity of 'remove' and 'heapify'.
        
        Since heapq lacks direct access to an item's index for manual manipulation, substituting the 'remove' and 
        'heapify' methods with a 'sifting' method while still using heapq as a backbone does not seem possible.
        
        "Overall, the performance remains acceptable despite the O(n) complexity."
        """

        self.heap.remove(node)
        heapq.heapify(self.heap)

    def is_empty(self):
        if len(self.heap) == 0:
            return True
        return False
