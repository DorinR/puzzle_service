from puzzle import Puzzle
from data_structures.stack import Stack
from data_structures.closed import Closed
from node import Node

SEARCH_STRATEGY = 'dfs'


def run_dfs(puzzle: Puzzle, get_moves: bool):
    # initialize closed to empty and open to contain the root node
    closed = Closed()
    open_ = Stack()
    root_node = Node(puzzle.initial_data, puzzle.size, 1, '0 ', None)
    open_.push(root_node)

    solving_status = {}

    # main loop that solves puzzle
    isSolved = False
    children = []
    puzzles_checked = 0
    while(open_.getSize() > 0 and not isSolved):
        nextNode = open_.pop()
        # print(f'DFS - # of puzzles checked: {puzzle_number}')
        if nextNode.isGoal():
            if get_moves:
                solving_status['moves'] = nextNode.get_solution_moves()
            isSolved = True
        if not isSolved and nextNode.depth <= puzzle.max_d:
            children = nextNode.getChildren()
            closed.add(nextNode)
            for child in children:
                if (not closed.isInClosed(child)) and (not open_.isInStack(child)):
                    open_.push(child)
        puzzles_checked += 1

    # Print status messages after solving algorithm to say whether or not solving succeeded.
    status = ""
    if isSolved:
        status = '🟢'
    else:
        status = '🔴'
        Node([], puzzle.size, 1, '00', root_node).print_solution(
            puzzle.puzzle_index, False, SEARCH_STRATEGY)

    # Whether solved or not save the search path
    closed.print_searched(puzzle.puzzle_index, SEARCH_STRATEGY)

    solving_status["solved"] = isSolved
    solving_status["num_puzzles_checked"] = puzzles_checked

    return status, solving_status
