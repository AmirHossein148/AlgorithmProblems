import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]
targets = [tuple(map(int, input().split())) for _ in range(k)]

dp = [row[:] for row in weight]

queue = deque()
in_queue = [[True] * m for _ in range(n)]

for r in range(n):
    for c in range(m):
        queue.append((r, c))

while queue:
    r, c = queue.popleft()
    in_queue[r][c] = False

    for dr, dc in [(-1, 0), (0, -1)]:
        nr, nc = (r + dr) % n, (c + dc) % m

        new_val = dp[(nr + 1) % n][nc] + dp[nr][(nc + 1) % m]

        if dp[nr][nc] > new_val:
            dp[nr][nc] = new_val
            if not in_queue[nr][nc]:
                queue.append((nr, nc))
                in_queue[nr][nc] = True

total_energy = 0
for row, col in targets:
    total_energy += dp[row][col]

print(total_energy)