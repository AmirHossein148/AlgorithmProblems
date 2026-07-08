def dfs_iterative(start):
    stack = [start]
    mark[start] = True
    while stack:
        node = stack.pop()
        for neighbor in adj[node]:
            if not mark[neighbor]:
                mark[neighbor] = True
                stack.append(neighbor)
n = int(input())
r1 = input().strip()
r2 = input().strip()
adj = [[] for _ in range(2 * n)]

for i in range(n):
    if r1[i] == 'O':
        if i + 1 < n and r1[i + 1] == 'O':
            adj[i].append(i + 1)
            adj[i + 1].append(i)
        if r2[i] == 'O':
            adj[i].append(n + i)
            adj[n + i].append(i)

    if r2[i] == 'O':
        if i + 1 < n and r2[i + 1] == 'O':
            adj[n + i].append(n + i + 1)
            adj[n + i + 1].append(n + i)

start, finish = 0 , (2*n)-1
mark = [False] * (2*n)
dfs_iterative(start)
if mark[finish]:
    print('Hooraaay!:))')
else:
    print('Awww:((')

