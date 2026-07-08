from collections import deque

def bfs(start):
    dist = [-1] * (n+1)
    dist[start] = 0
    q = deque([start])

    farthest_node = start
    while q:
        node = q.popleft()
        for nei in adj[node]:
            if dist[nei] == -1:
                dist[nei] = dist[node] + 1
                q.append(nei)
                if dist[nei] > dist[farthest_node]:
                    farthest_node = nei
    return farthest_node, dist[farthest_node]

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

A, _ = bfs(1)
B, diameter = bfs(A)

print(diameter)
