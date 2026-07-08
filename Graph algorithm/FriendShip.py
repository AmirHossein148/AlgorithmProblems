from collections import deque
import sys
sys.setrecursionlimit(10**5 + 100)

def bfs(start):
    dist[start] = 0
    q = deque([start])

    while q:
        size = len(q)
        res = []
        for _ in range(size):
            node = q.popleft()
            for nei in adj[node]:
                if dist[nei] == 10 ** 9:
                    dist[nei] = dist[node] + 1
                    if nei in person:
                        res.append(nei)
                    q.append(nei)
        if res:
            return min(res)


n = int(input())
adj = [list() for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[v].append(u)
    adj[u].append(v)

q = int(input())
person = set()
for _ in range(q):
    person.add(int(input()))

dist = [10**9] * (n+1)
print(bfs(1))