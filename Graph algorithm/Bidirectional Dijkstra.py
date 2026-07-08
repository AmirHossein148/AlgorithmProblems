import sys
import io
import heapq

input = sys.stdin.buffer.readline

def build_reverse_graph(adj):
    reverse_adj = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v, w in adj[u]:
            reverse_adj[v].append((u, w))
    return reverse_adj

def two_dijkstra(start, target, adj, reverse_adj):
    dist_s = [10**18 for _ in range(n+1)]
    visited_s = [False for _ in range(n+1)]
    dist_s[start] = 0
    h_s = []
    heapq.heappush(h_s, (0, start))

    dist_t = [10 ** 18 for _ in range(n + 1)]
    visited_t = [False for _ in range(n + 1)]
    dist_t[target] = 0
    h_t = []
    heapq.heappush(h_t, (0, target))

    best = 10**8

    while h_s or h_t:
        top_s = h_s[0][0] if h_s else 10 ** 18
        top_t = h_t[0][0] if h_t else 10 ** 18

        if top_s >= best and top_t >= best:
            break

        if h_s:
            w, node = heapq.heappop(h_s)
            if w > dist_s[node] or visited_s[node]:
                continue

            visited_s[node] = True
            for neighbor, weight in adj[node]:
                new_dist = dist_s[node] + weight
                if new_dist < dist_s[neighbor]:
                    dist_s[neighbor] = new_dist
                    heapq.heappush(h_s, (new_dist, neighbor))

            if visited_t[node]:
                best = min(best, dist_s[node] + dist_t[node])

        if h_t:
            w, node = heapq.heappop(h_t)
            if w > dist_t[node] or visited_t[node]:
                continue

            visited_t[node] = True
            for neighbor, weight in reverse_adj[node]:
                new_dist = dist_t[node] + weight
                if new_dist < dist_t[neighbor]:
                    dist_t[neighbor] = new_dist
                    heapq.heappush(h_t, (new_dist, neighbor))

            if visited_s[node]:
                best = min(best, dist_t[node] + dist_s[node])

    return best if best < 10 ** 18 else -1

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

visited = [False for _ in range(n+1)]
dist = [10**18 for _ in range(n+1)]
start, target = map(int, input().split())

reverse_adj = build_reverse_graph(adj)

result = two_dijkstra(start, target, adj, reverse_adj)
print(result)

