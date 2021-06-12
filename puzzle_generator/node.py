import numpy as np
from math import sqrt
from helpers.legacy_helpers import formatBoardState
import os.path
from random import randint
from typing import List
from random import randint

# helpers used to get the move position ie: B4
HORIZONTAL = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
VERTICAL = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


class Node:
    def __init__(self, size: int):
        self.data = [0 for i in range(int(size)**2)]
        self.size = int(size)

    def make_random_move(self):
        self.flip_piece(randint(0, len(self.data) - 1))

    def getChildren(self):
        children = []
        for i in range(len(self.data)):
            children.append(self.flip_piece(i))
        # arbitrary sorting based on white pieces
        children.sort(key=lambda n: n.data, reverse=True)
        return children

    def isGoal(self):
        return 1 not in self.data

    def flip_piece(self, target: int):
        indices_to_flip = [target]
        indices_to_flip.extend(self.get_neighbours(target))
        new_data = self.data[:]
        for i in indices_to_flip:
            new_data[i] = (new_data[i] + 1) % 2
        self.data = new_data

    def getMove(self, target):
        rows = [list(arr) for arr in np.array_split(
            range(len(self.data)), self.size)]
        vertical_index = 0
        for i, row in enumerate(rows):
            if target in row:
                vertical_index = i
        horizontal_index = target % self.size
        return VERTICAL[vertical_index] + HORIZONTAL[horizontal_index]

    def get_neighbours(self, target):
        tentative_neighbours = []

        if target % self.size == 0:
            tentative_neighbours = [
                target - self.size, target + self.size, target + 1]
        elif target % self.size == self.size - 1:
            tentative_neighbours = [
                target - self.size, target + self.size, target - 1]
        else:
            tentative_neighbours = [target + 1, target - 1,
                                    target + self.size, target - self.size]

        correct_neighbours = []
        for index in tentative_neighbours:
            if index in [i for i in range(len(self.data))]:
                correct_neighbours.append(index)
        return correct_neighbours

    def print_data(self):
        print(
            f'data from node is: {self.data}, index_range: {self.index_range}')

    def print_board(self):
        rows = np.array_split(self.data, self.size)
        print(f'Move: {self.move}')
        print(f'Board:')
        for row in rows:
            print(row)
        print()

    def get_state_cli(self):
        cli_state = "".join([str(i) for i in self.data])
        return cli_state

    def print_solution(self, puzzle_index, sol_found, algorithm):
        to_write_to_file = []
        filename = f'{puzzle_index}_{algorithm}_solution.txt'
        to_write_to_file.append(filename)
        if sol_found:
            curr = self
            move_and_state_data = []
            while curr:
                move_and_state_data.append(
                    f'{curr.move}   {formatBoardState(curr.data)}')
                curr = curr.parent
            move_and_state_data.reverse()
            to_write_to_file.extend(move_and_state_data)
        else:
            no_sol = 'no solution'
            to_write_to_file.append(no_sol)
        self.write_to_file(to_write_to_file)

    def write_to_file(self, data_to_write):
        directory = os.path.join(f'results/{data_to_write.pop(0)}')
        with open(directory, 'w') as f:
            for line in data_to_write:
                f.write("%s\n" % line)
