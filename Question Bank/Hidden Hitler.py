import sys
import heapq

def can_conquer(start, graph, power, n):
    visited = [False] * (n + 1)
    visited[start] = True
    current = power[start]
    out_source = 0

    pq = []
    for v in graph[start]:
        heapq.heappush(pq, (power[v], v))

    while pq:
        p, u = heapq.heappop(pq)
        if visited[u]:
            continue
        if p >= current:
            out_source += (p-current) + 1
            current = p + 1

        current += p
        visited[u] = True

        for v in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (power[v], v))

    return out_source



n, m = map(int, input().split())
power = [0] + list(map(int, input().split())) # to make indices one-based

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = []
for start in range(1,n+1):
    result.append(can_conquer(start, graph, power, n))

print(*result)
