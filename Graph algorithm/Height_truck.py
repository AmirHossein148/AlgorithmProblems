import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

q = int(input())
queries = []

for i in range(q):
    s, f, w = map(int, input().split())
    queries.append((w, s, f, i))

edges.sort(reverse=True)
queries.sort(reverse=True)

parent = list(range(n + 1))
size = [1] * (n + 1)

def find(x): # Find the parent
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return

    if size[ra] < size[rb]: # Be sure that ra is parent
        ra, rb = rb, ra

    parent[rb] = ra
    size[ra] += size[rb]

ans = ["NO"] * q

j = 0
for w, s, f, idx in queries:

    while j < m and edges[j][0] >= w:
        _, u, v = edges[j]
        union(u, v)
        j += 1

    if find(s) == find(f):
        ans[idx] = "YES"

print(*ans, sep="\n")




