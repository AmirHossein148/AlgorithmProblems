import time
start_time = time.time()

import sys
import heapq

input = sys.stdin.readline
INF = 10**30

n, m = map(int, input().split())
a = list(map(int, input().split()))

g = [[] for _ in range(n)]
for _ in range(m):
    v, u, w = map(int, input().split())
    v -= 1
    u -= 1
    g[v].append((u, w))
    g[u].append((v, w))

ans = [[INF]*n for _ in range(n)]

for s in range(n):
    dist = [[INF]*n for _ in range(n)]
    pq = []
    dist[s][s] = 0
    heapq.heappush(pq, (0, s, s))

    while pq:
        cost, u, mn = heapq.heappop(pq)
        if cost > dist[u][mn]:
            continue
        for v, w in g[u]:
            new_mn = mn if a[mn] < a[v] else v
            new_cost = cost + w * a[mn]
            if new_cost < dist[v][new_mn]:
                dist[v][new_mn] = new_cost
                heapq.heappush(pq, (new_cost, v, new_mn))

    for t in range(n):
        ans[s][t] = min(dist[t])

for i in range(n):
    print(*ans[i])


end_time = time.time()
print('Execution time: {:.6f} seconds'.format(end_time-start_time))