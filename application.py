from puzzle_generator.puzzle_generator import get_starting_puzzle
from helpers.api_helper import extract_puzzle, extract_strategies
from puzzle_solver import run_solver
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json

application = Flask(__name__, static_url_path='',
                    static_folder='frontend/build', template_folder='frontend/build')
cors = CORS(application)


@application.route('/')
def render_homepage():
    return render_template('index.html')


@application.route('/solve_simple', methods=['POST'])
def solve_simple():
    """
    One of two puzzle solving endpoints.
    This one returns only:
        1. whether it was solved or not
        2. number of moves needed for solving
        3. how long it took to solve
        4. pretty formatted message for solving status
    """
    data = request.get_json()
    puzzle = extract_puzzle(data)
    strategies = extract_strategies(data)
    solving_statuses = run_solver(puzzle, strategies, False)

    response = {"statuses": solving_statuses}

    return jsonify(response)


@application.route('/solve_advanced', methods=['POST'])
def solve_advanced():
    """
    Second of two puzzle solving endpoints.
    This one returns all of the same things as the first one, and in addition:
        1. The steps to solve the puzzle
    Note: it would be very easy to merge these two endpoints into a single one. The reason I am
    choosing not to is because this one may take longer to send the data back (a long list of moves)
    so in the event when we just quickly want to know if a puzzle is solvable, we would use the
    solve_simple endpoint.
    """
    data = request.get_json()
    puzzle = extract_puzzle(data)
    strategies = extract_strategies(data)
    solving_statuses = run_solver(puzzle, strategies, True)

    response = {"statuses": solving_statuses}

    return jsonify(response)


@application.route('/generate_puzzle/<puzzle_size>/<difficulty>')
def generate_puzzle(puzzle_size, difficulty):
    puzzle_start_state = get_starting_puzzle(int(puzzle_size), difficulty)

    response = {"startingPuzzleState": puzzle_start_state}

    return jsonify(response)


@application.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
