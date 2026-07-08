import sys

input = sys.stdin.buffer.readline

def floyd_warshall(adj):
    dist = [row[:] for row in adj]

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

n, m = map(int, input().split())
INF = 10**18
adj = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    adj[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u][v] = w

dist = floyd_warshall(adj)

for i in range(1, n + 1):
    print(*[x if x < INF else -1 for x in dist[i][1:]])