class Puzzle:
    def __init__(self, puzzle_index, size, max_d, max_pl, initial_data):
        self.puzzle_index = puzzle_index
        self.size = size
        self.max_d = int(max_d)
        self.max_pl = int(max_pl)
        self.initial_data = initial_data

    def printData(self):
        print(
            f'puzzle_index: {self.puzzle_index}, size: {self.size}, max_d: {self.max_d}, max_pl: {self.max_pl}, initial_data: {self.initial_data}')
