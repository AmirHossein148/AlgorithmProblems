import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(node, adj, visited, result):
    visited[node] = True
    for neighbor, weight in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, adj, visited, result)
    result.append(node)  # post-order: append AFTER visiting all descendants

def topological_sort(adj, visited, result):
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, adj, visited, result)

    result.reverse()
    return result

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
source = int(input())
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

visited = [False] * (n + 1)
result = []

order = topological_sort(adj, visited, result)

INF = 10**18
dist = [INF for _ in range(n+1)]
dist[source] = 0
for item in order:
    if dist[item] == INF:
        continue
    for v, w in adj[item]:
        if dist[item] + w < dist[v]:
            dist[v] = dist[item] + w

print(*[dist[i] if dist[i] != INF else "INF" for i in range(1, n + 1)])

# IF WE WANT TO FIND LONGEST PATH, WE CAN MULTIPLY OUR WEIGHTS BY MINUS 1 (-1)
