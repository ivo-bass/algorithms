"""
You are given a labyrinth. Your goal is to find all paths from the start (cell 0, 0) to the exit, marked with 'e'.
    • Empty cells are marked with a dash '-'.
    • Walls are marked with a star '*';
On the first line, you will receive the dimensions of the labyrinth. Next you will receive the actual labyrinth.
The order of the paths does not matter.

Example 1:
    Input:
        3
        3
        ---
        -*-
        --e

    Output:
        RRDD
        DDRR

Example 2:
    Input:
        3
        5
        -**-e
        -----
        *****

    Output:
        DRRRRU
        DRRRUR
"""

WALL = '*'
EXIT = 'e'

MOVES = {
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
    'U': (-1, 0),
}

START_CELL = (0, 0)

ROWS = int(input())
COLS = int(input())
LAB = [list(input()) for _ in range(ROWS)]


def get_exit_cell():
    for row in range(ROWS):
        for col in range(COLS):
            if LAB[row][col] == EXIT:
                return row, col


EXIT_CELL = get_exit_cell()

path = []
visited = set()
visited.add((0, 0))


def is_valid_row(row):
    return 0 <= row < ROWS


def is_valid_col(col):
    return 0 <= col < COLS


def can_go(row, col):
    if not is_valid_row(row):
        return False
    if not is_valid_col(col):
        return False
    if LAB[row][col] == WALL:
        return False
    if (row, col) in visited:
        return False
    return True


def mark_path(letter, row, col):
    path.append(letter)
    visited.add((row, col))


def unmark_path(row, col):
    path.pop()
    visited.remove((row, col))


def find_path(row, col):
    if (row, col) == EXIT_CELL:
        print(''.join(path))
        return
    for letter, delta in MOVES.items():
        delta_r = delta[0]
        delta_c = delta[1]
        new_row = row + delta_r
        new_col = col + delta_c
        if can_go(new_row, new_col):
            mark_path(letter, new_row, new_col)
            find_path(new_row, new_col)
            unmark_path(new_row, new_col)


find_path(*START_CELL)
