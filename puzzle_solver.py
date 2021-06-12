from puzzle import Puzzle
from dfs_runner import run_dfs
from bfs_runner import run_bfs
from a_star_runner import run_a_star
import time


def run_solver(puzzle: Puzzle, algo_to_run: list, get_moves: bool):
    print('===== Starting Solving ... =====')
    statuses = {}
    if algo_to_run[0]:
        start_time_1 = time.time()
        status, solving_status = run_dfs(puzzle, get_moves)
        total_time = time.time() - start_time_1
        pretty_status = f'Status: {status} ({solving_status["num_puzzles_checked"]} puzzles checked in {total_time}s)'
        print(pretty_status)
        solving_status['time_to_solve'] = total_time
        solving_status['pretty_status'] = pretty_status
        statuses['dfs'] = solving_status
    if algo_to_run[1]:
        start_time_2 = time.time()
        status, solving_status = run_bfs(puzzle, get_moves)
        total_time = time.time() - start_time_2
        pretty_status = f'Status: {status}  ({solving_status["num_puzzles_checked"]} puzzles checked in {total_time}s)'
        print(pretty_status)
        solving_status['time_to_solve'] = total_time
        solving_status['pretty_status'] = pretty_status
        statuses['bfs'] = solving_status
    if algo_to_run[2]:
        start_time_3 = time.time()
        status, solving_status = run_a_star(puzzle, get_moves)
        total_time = time.time() - start_time_3
        pretty_status = f'Status: {status}  ({solving_status["num_puzzles_checked"]} puzzles checked in {total_time}s)'
        print(pretty_status)
        solving_status['time_to_solve'] = total_time
        solving_status['pretty_status'] = pretty_status
        statuses['a_star'] = solving_status
    return statuses
