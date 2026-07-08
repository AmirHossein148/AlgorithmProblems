import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))

adj = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append((v, w))
    adj[v].append((u, w))

max_w = 1000
dist = [[float('inf')] * (max_w + 1) for _ in range(n)]
pq = [(0, 0, 0)]
dist[0][0] = 0

while pq:
    d, u, k = heapq.heappop(pq)

    if d > dist[u][k]:
        continue

    if k + 1 < max_w:
        new_dist = d + t[u]
        if new_dist < dist[u][k + 1]:
            dist[u][k + 1] = new_dist
            heapq.heappush(pq, (new_dist, u, k + 1))

    for v, w in adj[u]:
        actual_w = w - k
        if actual_w > 0:
            if d + actual_w < dist[v][k]:
                dist[v][k] = d + actual_w
                heapq.heappush(pq, (dist[v][k], v, k))

ans = min(dist[n - 1])

if ans == float('inf'):
    print("-1")
else:
    print(ans)


