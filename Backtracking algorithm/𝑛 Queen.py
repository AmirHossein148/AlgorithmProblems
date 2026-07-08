n, k = map(int, input().split())


def make_board(n):
    return [[0 for _ in range(n)] for _ in range(n)]


def fill_board(board, row, col, n):
    for i in range(n):
        for j in range(n):
            # same row OR same column OR same diagonal
            if i == row or j == col or (i - j == row - col) or (i + j == row + col):
                board[i][j] = 1


def solve(board, placed, start_row, n, k):
    if placed == k:
        return 1

    if start_row >= n:
        return 0

    count = 0
    # try placing a minister in this row
    for col in range(n):
        if board[start_row][col] == 0:  # safe cell
            new_board = [row[:] for row in board]  # copy board
            fill_board(new_board, start_row, col, n)
            count += solve(new_board, placed + 1, start_row + 1, n, k)

    # also try skipping this row
    count += solve(board, placed, start_row + 1, n, k)

    return count


board = make_board(n)
result = solve(board, 0, 0, n, k)
print(result)

