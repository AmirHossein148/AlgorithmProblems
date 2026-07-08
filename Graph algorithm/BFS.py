from collections import deque
import sys

input = sys.stdin.readline

def bfs(adj, start, finish):
    n = len(adj) - 1
    dist = [-1] * (n+1)
    parent = [-1] * (n+1)

    q = deque([start])
    dist[start] = 0

    while q:
        node = q.popleft()
        if node == finish:
            break
        for nei in adj[node]:
            if dist[nei] == -1:
                dist[nei] = dist[node] + 1
                parent[nei] = node
                q.append(nei)

    if dist[finish] == -1:
        return -1, None

    path = []
    cur = finish
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path = path[::-1] # instead of path.reverse()

    return dist[finish], path

t = int(input())
for _ in range(t):
    n, m, start, finish = map(int, input().split())

    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        v, u = map(int, input().split())
        adj[v].append(u)
        adj[u].append(v)


    length, path = bfs(adj, start, finish)
    if length == -1:
        print(-1)
    else:
        print(length+1)



