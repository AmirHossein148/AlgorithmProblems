import sys

input = sys.stdin.readline

def dfs_for_bridges(start, parent, bridges):
    global id
    visited[start] = True
    low[start] = idx[start] = id
    id += 1

    for node in adj[start]:
        if node == parent:
            continue
        if not visited[node]:
            dfs_for_bridges(node, start, bridges)
            low[start] = min(low[start], low[node])
            if idx[start] < low[node]:
                bridges.append((start, node))
        else:
            low[start] = min(low[start], idx[node])

    return bridges


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


idx = [0 for _ in range(n+1)]
low = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
bridges = []
id = 1

for i in range(1, n + 1):
    if not visited[i]:
        dfs_for_bridges(i, -1, bridges)

print(bridges)

