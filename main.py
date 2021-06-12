from puzzle_data_loader import load_puzzle_data
from puzzle_solver import run_solver
from puzzle_generator.puzzle_generator import run_puzzle_generator
import sys

# remove first argument
sys.argv.pop(0)

# get path to data file
if (len(sys.argv) < 1):
    print('ERROR: Please specify relative path to file containing puzzles to solve')
PATH_TO_PUZZLE_DATA = sys.argv[0]

# mode 0 => solve puzzle
# mode 1 => generate 10 solvable puzzles
program_mode = 0
puzzle_size = ''
number_of_puzzles = ''
distance_from_goal = ''

if sys.argv[0][0] != '/':
    program_mode = 1
    puzzle_size = int(sys.argv[0])
    number_of_puzzles = int(sys.argv[1])
    distance_from_goal = int(sys.argv[2])


if program_mode == 0:
    # === CHOOSE WHICH STRATEGIES TO RUN ===
    RUN_DFS = True
    RUN_BFS = True
    RUN_A_STAR = True
    ALGORITHMS_TO_RUN = [RUN_DFS, RUN_BFS, RUN_A_STAR]

    # load in puzzle data
    puzzle_data_objects = load_puzzle_data(PATH_TO_PUZZLE_DATA)

    # solve
    for puzzle in puzzle_data_objects:
        statuses = run_solver(puzzle, ALGORITHMS_TO_RUN)
        for status in statuses:
            print(status)
else:
    run_puzzle_generator(puzzle_size, number_of_puzzles, distance_from_goal)
