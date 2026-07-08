import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    tasks = [tuple(map(int, input().split())) for _ in range(n)]
    early = []
    late = []

    tasks.sort(key=lambda x: min(x[0], x[1]))
    for a, b in tasks:
        if a <= b:
            early.append((a, b))
        else:
            late.append((a, b))
    sequence = early + late[::-1]

    S = W = 0
    for a, b in sequence:
        S += a
        W = max(W, S) + b
    print(W)

