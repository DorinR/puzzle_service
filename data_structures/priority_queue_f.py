from node_a_star import Node


class PriorityQueueF:
    def __init__(self):
        self.queue = []
        self.quick_access_seen = {}

    def insert(self, data: Node):
        self.queue.append(data)
        s = self.to_str(data.data)
        if s in self.quick_access_seen:
            self.quick_access_seen[s] += 1
        else:
            self.quick_access_seen[s] = 0

    def getSize(self):
        return len(self.queue)

    def peek(self):
        return self.queue[0]

    def dequeue(self):
        node_to_return = None
        # find the correct node to remove
        if len(self.queue) > 0:
            max_index = 0
            for i in range(len(self.queue)):
                if self.queue[i].f < self.queue[max_index].f:
                    max_index = i
            node_to_return = self.queue.pop(max_index)
        else:
            return "Queue is empty"
        # remove from quick access list
        s = self.to_str(node_to_return.data)
        if self.quick_access_seen[s] > 1:
            self.quick_access_seen[s] -= 1
        else:
            self.quick_access_seen.pop(s, None)
        return node_to_return

    def isInQueue(self, n):
        s = self.to_str(n.data)
        return s in self.quick_access_seen

    def to_str(self, puzzle_state):
        return "".join([str(i) for i in puzzle_state])
