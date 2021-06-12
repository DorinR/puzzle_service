from helpers.legacy_helpers import formatBoardState
import os.path


class Closed:
    def __init__(self):
        self.data = []
        self.quick_access_states = set()

    def add(self, node):
        self.data.append(node)
        self.quick_access_states.add(self.to_str(node.data))

    def isInClosed(self, n):
        s = self.to_str(n.data)
        return s in self.quick_access_states

    def print_searched(self, puzzle_index, search_algorithm):
        to_write_to_file = []
        filename = f'{puzzle_index}_{search_algorithm}_search.txt'
        to_write_to_file.append(filename)
        for node in self.data:
            to_write_to_file.append(
                f'{str(node.get_f())}  {str(node.get_g())}  {str(node.get_h())}    {formatBoardState(node.data)}')
        self.write_to_file(to_write_to_file)

    def write_to_file(self, data_to_write):
        directory = os.path.join(f'results/{data_to_write.pop(0)}')
        with open(directory, 'w') as f:
            for line in data_to_write:
                f.write("%s\n" % line)

    def get_size(self):
        return len(self.data)

    def to_str(self, puzzle_state):
        return "".join([str(i) for i in puzzle_state])
