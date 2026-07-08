import sys

sys.setrecursionlimit(2000)
input = sys.stdin.readline

n, m = map(int, input().split())

adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color_sets = []
for i in range(n):
    color_sets.append(set(map(int, input().split())))

candidates = []
for i in range(n):
    c = color_sets[i].copy()
    for j in adj[i]:
        c &= color_sets[j]
    candidates.append(list(c))

match_color_to_v = {}
res_colors = [0] * n

def can_match(u, visited):
    for c in candidates[u]:
        if c not in visited:
            visited.add(c)
            if c not in match_color_to_v or can_match(match_color_to_v[c], visited):
                match_color_to_v[c] = u
                return True
    return False

for i in range(n):
    can_match(i, set())

for c, v in match_color_to_v.items():
    res_colors[v] = c

print(*(res_colors))

