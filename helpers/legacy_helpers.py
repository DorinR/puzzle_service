# Input: Board Data
# Output: Board data as a string


def formatBoardState(board_data_array):
    str_ = ''
    for board_slot in board_data_array:
        str_ += (str(board_slot) + ' ')

    return str_
