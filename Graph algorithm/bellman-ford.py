import sys

def bellman_ford(n, edges, start_node):
    INF = 10**9
    distances = [INF] * n
    distances[start_node] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if distances[u] != INF and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    return distances


input = sys.stdin.readline
n, m = map(int, input().split())
edges = []

for _ in range(m):
    u, v, w = map(int,input().split())
    u -= 1
    v -= 1
    edges.append((u, v, w))

start_node = 0
dist = bellman_ford(n, edges, start_node)
print(*dist)



