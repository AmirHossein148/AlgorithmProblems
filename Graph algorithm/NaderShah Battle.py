def battle(adj, start, diamond, n, a):
    parent = [0] * (n + 1)
    order = []
    stack = [start]
    visited = [False] * (n + 1)
    visited[start] = True

    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                stack.append(v)

    f = [0] * (n + 1)
    best_child = [0] * (n + 1)

    for u in reversed(order): # Going from leaves up to the root
        max_val = 0
        for v in adj[u]:
            if v != parent[u]: # Look at children
                if f[v] > max_val:
                    max_val = f[v]
                    best_child[u] = v
        f[u] = diamond[u] + max_val

    path_sums = []
    used = [False] * (n + 1)
    for u in order:
        if not used[u]:
            current_path_diamonds = 0
            curr = u
            while curr != 0 and not used[curr]:
                current_path_diamonds += diamond[curr]
                used[curr] = True
                curr = best_child[curr]
            if current_path_diamonds > 0:
                path_sums.append(current_path_diamonds)

    path_sums.sort(reverse=True)
    return sum(path_sums[:a])



t = int(input())
for _ in range(t):
    n, start, a = map(int,input().split())
    diamond = [0] + list(map(int, input().split()))
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)

    print(battle(adj, start, diamond, n, a))