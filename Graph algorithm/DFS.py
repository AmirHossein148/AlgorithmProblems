import sys
sys.setrecursionlimit(10**7)

def dfs_iterative(start):
    stack = [start]
    while stack:
        node = stack.pop()
        for neighbor in adj[node]:
                if neighbor == t:
                    return  True, count
                stack.append(neighbor)

n, m, s, t = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    v, u = map(int, input().split())
    adj[v].append(u)
    adj[u].append(v)

dfs_iterative(start)
