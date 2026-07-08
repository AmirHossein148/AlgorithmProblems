import time
import sys

start_time = time.time()

input = sys.stdin.readline
INF = 10**18
n, m = map(int, input().split())
a = list(map(int, input().split()))

dist = [[INF] * (n) for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w < dist[u][v]:
        dist[u][v] = dist[v][u] = w

# Floyd-Warshall
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]


# full your gas tank on city i as a start point
cost = [[dist[i][j] * a[i] for j in range(n)] for i in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if cost[i][k] + cost[k][j] < cost[i][j]:
                cost[i][j] = cost[i][k] + cost[k][j]

for row in cost:
    sys.stdout.write(' '.join(map(str,row)) + '\n')




end_time = time.time()
print('Execution time: {:.6f} seconds'.format(end_time-start_time))