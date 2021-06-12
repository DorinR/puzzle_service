class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.append(data)

    def getSize(self):
        return len(self.queue)

    def peek(self):
        return self.queue[0]

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def isInQueue(self, n):
        isInQueue = False
        for node in self.queue:
            if node.data == n.data:
                isInQueue = True
        return isInQueue
