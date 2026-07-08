def dfs(node, adj, mark):
    stack = [node]
    mark[node] = True
    while stack:
        v = stack.pop()
        for neighbor in adj[v]:
            if not mark[neighbor]:
                mark[neighbor] = True
                stack.append(neighbor)

n = int(input())
adj = {i: [] for i in range(1, n+1)}

x_map = {}
y_map = {}

for j in range(1, n+1):
    x, y = map(int, input().split())

    if x in x_map:
        for u in x_map[x]:
            adj[j].append(u)
            adj[u].append(j)
        x_map[x].append(j)
    else:
        x_map[x] = [j]

    if y in y_map:
        for u in y_map[y]:
            adj[j].append(u)
            adj[u].append(j)
        y_map[y].append(j)
    else:
        y_map[y] = [j]

mark = [False] * (n+1)
components = 0

for node in range(1, n+1):
    if not mark[node]:
        dfs(node, adj, mark)
        components += 1

print(components-1)