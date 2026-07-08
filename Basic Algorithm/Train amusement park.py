def solve(X, Y, tx, ty, px, py):
    P = 2 * (X + Y)

    def pos(x, y):
        if y == 0: return x
        if x == X: return X + y
        if y == Y: return X + Y + (X - x)
        return 2 * X + Y + (Y - y)

    train_pos = pos(tx, ty)
    ans = 10**18

    moves = [
        (Y - py, px, Y),     # up
        (py, px, 0),         # down
        (X - px, X, py),     # right
        (px, 0, py)          # left
    ]

    for walk_time, tx2, ty2 in moves:
        target = pos(tx2, ty2)
        train_time = P - (target - train_pos + P) % P # Because we calculute unclockwise

        if train_time >= walk_time:
            ans = min(ans, train_time)

    return ans if ans < 10**18 else -1

t = int(input())
for _ in range(t):
    X, Y, train_X, train_Y, person_X, person_Y = map(int, input().split())
    print(solve(X, Y, train_X, train_Y, person_X, person_Y))

