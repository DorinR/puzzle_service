from node_bfs import Node


class MinHeap:
    def __init__(self):
        self.heap = []
        self.data_quick_lookup = {}

    def insert(self, data: Node):
        """
        Inserting an element into the puzzle
        """
        self.heap.append(data)
        self.sift_up(len(self.heap) - 1, self.heap)
        # quick lookup management
        s = self.to_str(data.data)
        if s in self.data_quick_lookup:
            self.data_quick_lookup[s] += 1
        else:
            self.data_quick_lookup[s] = 1

    def dequeue(self):
        """
        Getting the next element from the queue
        """
        self.swap(self.heap, 0, len(self.heap) - 1)
        value_to_remove = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)

        # quick lookup management
        s = self.to_str(value_to_remove.data)
        if s in self.data_quick_lookup:
            self.data_quick_lookup[s] -= 1
        else:
            self.data_quick_lookup.pop(s, None)

        return value_to_remove

    def isEmpty(self):
        """
        Check if the heap is empty or not
        """
        pass

    def isInQueue(self, data: Node):
        """
        Check if the heap contains a specific value
        """
        pass

    def getSize(self):
        return len(self.heap)

    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and heap[parent_idx].h > heap[current_idx].h:
            self.swap(heap, parent_idx, current_idx)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def sift_down(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and heap[child_two_idx].h > heap[child_one_idx].h:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            if heap[idx_to_swap].h > heap[current_idx].h:
                self.swap(self.heap, current_idx, idx_to_swap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return

    def swap(self, heap, i, j):
        heap[i], heap[j] = heap[j], heap[i]

    def to_str(self, puzzle_state):
        return "".join([str(i) for i in puzzle_state])
