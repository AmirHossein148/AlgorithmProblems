import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]
targets = [tuple(map(int, input().split())) for _ in range(k)]

dp = [row[:] for row in weight]

for _ in range(2):
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            ni = (i + 1) % n
            nj = (j + 1) % m
            if dp[i][j] > dp[ni][j] + dp[i][nj]:
                dp[i][j] = dp[ni][j] + dp[i][nj]

total_energy = 0
for r, c in targets:
    total_energy += dp[r][c]

print(total_energy)