def make_board(n):
    return [[0 for _ in range(n)] for _ in range(n)]


def horse(attempt, row, col, n, k, house):
    # base case: after k moves, record position
    if attempt == k:
        house.add((row, col))
        return

    moves = [
        (-2, +1), (-2, -1),
        (+2, +1), (+2, -1),
        (+1, +2), (-1, +2),
        (+1, -2), (-1, -2)
    ]

    for dr, dc in moves:
        new_r, new_c = row + dr, col + dc
        # check boundaries
        if 0 <= new_r < n and 0 <= new_c < n:
            horse(attempt + 1, new_r, new_c, n, k, house)


n, k = map(int, input().split())
house = set()
horse(0, 0, 0, n, k, house)
print(len(house))
