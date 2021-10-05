SIZE = 8
EMPTY = '-'
QUEEN = 'Q'
attacked_cols = set()
attacked_left_d = set()  # col-row
attacked_right_d = set()  # col+row
board = [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]


def can_place_queen(row, col):
    if col in attacked_cols:
        return False
    if (col-row) in attacked_left_d:
        return False
    if (col+row) in attacked_right_d:
        return False


def mark_attacked_positions(row, col):
    attacked_cols.add(col)
    attacked_left_d.add(col-row)
    attacked_right_d.add(col+row)
    board[row][col] = QUEEN


def unmark_attacked_positions(row, col):
    attacked_cols.remove(col)
    attacked_left_d.remove(col-row)
    attacked_right_d.remove(col+row)
    board[row][col] = EMPTY


def print_solution():
    for row in range(len(board)):
        print(' '.join(board[row]))
    print()


def place_queens(row):
    if row == SIZE:
        print_solution()
        return
    for col in range(SIZE):
        if can_place_queen(row, col):
            mark_attacked_positions(row, col)
            place_queens(row + 1)
            unmark_attacked_positions(row, col)


place_queens(0)
