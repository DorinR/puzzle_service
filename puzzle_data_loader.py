import os
import sys
from puzzle import Puzzle


def load_puzzle_data(relative_puzzle_data_path):
    # get the path to the current directory
    current_directory = sys.path[0]

    # construct the absolute path to the file containing the puzzle data
    absolute_puzzle_data_path = current_directory + relative_puzzle_data_path

    # read-in data file
    with open(absolute_puzzle_data_path, 'r') as f:
        data = f.readlines()

    # remove newline characters
    data_no_whitespaces = []
    for line in data:
        data_no_whitespaces.append(line.strip())

    # build objects to save each of the puzzles' data
    puzzle_data_objects = []
    for i, line in enumerate(data_no_whitespaces):
        d = line.split()
        puzzle_data_objects.append(Puzzle(i, d[0], d[1], d[2], d[3]))

    return puzzle_data_objects
