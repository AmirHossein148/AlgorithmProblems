sudoku_board = []
for _ in range(9):
    sudoku_board.append(list(map(int, input().split())))


def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))


def find_empty(board):
    # Find an empty cell (0 means empty)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(board, num, pos):
    row, col = pos

    if num in board[row]:
        return False

    if num in [board[i][col] for i in range(9)]:
        return False

    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False

    return True


def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # backtrack

    return False


if solve(sudoku_board):
    print_board(sudoku_board)
else:
    print("No solution exists")
