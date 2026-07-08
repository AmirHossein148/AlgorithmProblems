from collections import deque

def bfs(adj, weight_dic, start):
    n = len(adj) - 1
    dist = [-1] * (n+1)

    q = deque([start])
    dist[start] = 0

    while q:
        node = q.popleft()
        for nei in adj[node]:
            if dist[nei] == -1:
                dist[nei] = dist[node] + int(weight_dic.get((node,nei)))
                q.append(nei)
    return max(dist)


n, m = map(int, input().split())

weight_dic = {}
adj = [[] for _ in range(n+1)]
final_list = [-1]
for _ in range(m):
    v, u, w = map(int, input().split())
    adj[v].append(u)
    adj[u].append(v)
    weight_dic.setdefault((v,u), w)

res = 10**9
for i in range(1, n+1):
    if bfs(adj, weight_dic, i) < res:
        final_list.pop()
        final_list.append(res)
    else:
        continue

