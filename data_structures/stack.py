class Stack():
    def __init__(self):
        self.data = []
        self.quick_access_states = set()

    def pop(self):
        if (len(self.data) > 0):
            self.quick_access_states.remove(self.to_str(self.data[-1].data))
            return self.data.pop()
        else:
            print('Error: stack empty')

    def push(self, node):
        self.data.append(node)
        self.quick_access_states.add(self.to_str(node.data))

    def getSize(self):
        return len(self.data)

    def isInStack(self, n):
        s = self.to_str(n.data)
        return s in self.quick_access_states

    def to_str(self, puzzle_state):
        return "".join([str(i) for i in puzzle_state])
