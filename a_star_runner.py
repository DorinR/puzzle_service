from puzzle import Puzzle
from data_structures.closed import Closed
from data_structures.priority_queue_f import PriorityQueueF
from node_a_star import Node

SEARCH_STRATEGY = 'astar'


def run_a_star(puzzle: Puzzle, get_moves: bool):
    # initializing the closed list as empty and the open list containing the root node.
    closed = Closed()
    open_ = PriorityQueueF()
    root_node = Node(puzzle.initial_data, puzzle.size, 0, '0 ', None)
    open_.insert(root_node)

    solving_status = {}

    # main loop that solves puzzle
    isSolved = False
    children = []
    puzzles_checked = 0
    while(open_.getSize() > 0 and not isSolved):
        if isSolved or puzzles_checked >= puzzle.max_pl:
            break
        # check for solution
        nextNode = open_.dequeue()
        if nextNode.isGoal():
            if get_moves:
                solving_status['moves'] = nextNode.get_solution_moves()
            isSolved = True
        # get children and add some of them to the open list.
        children = nextNode.getChildren()
        closed.add(nextNode)
        for child in children:
            if (not closed.isInClosed(child)) and (not open_.isInQueue(child)):
                open_.insert(child)
        # increment number of puzzles checked
        puzzles_checked += 1

    # Print status messages after solving algorithm to say whether or not solving succeeded.
    status = ""
    if isSolved:
        status = '🟢'
    else:
        status = '🔴'
        Node([], puzzle.size, 0, '00', root_node).print_solution(
            puzzle.puzzle_index, False, SEARCH_STRATEGY)

    # Whether solved or not save the search path
    closed.print_searched(puzzle.puzzle_index, SEARCH_STRATEGY)

    solving_status["solved"] = isSolved
    solving_status["num_puzzles_checked"] = puzzles_checked

    return status, solving_status
