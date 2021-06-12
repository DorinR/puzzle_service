from puzzle import Puzzle
from math import sqrt


def extract_puzzle(data):
    index = 0
    size = get_puzzle_size(data['state'])
    state = data['state']

    # get max_d
    try:
        max_d = data['searchOptions']['max_d']
        limit_d = get_max_depth(len(state))
        if int(max_d) > limit_d:
            max_d = limit_d
    except:
        max_d = get_max_depth(len(state))

    # get max_p
    try:
        max_p = data['searchOptions']['max_p']
        limit_p = 1000
        if int(max_p) > limit_p:
            max_p = limit_p
    except:
        max_p = 1000

    return Puzzle(index, size, max_d, max_p, state)


def get_max_depth(size):
    if size == 9:
        return 10
    elif size == 16:
        return 4
    else:
        return 2


def get_puzzle_size(state):
    return sqrt(len(state))


def extract_strategies(data):
    run_dfs = data['strategies']['dfs']
    run_bfs = data['strategies']['bfs']
    run_a_star = data['strategies']['a_star']

    strategies_to_run = [run_dfs, run_bfs, run_a_star]

    return strategies_to_run
