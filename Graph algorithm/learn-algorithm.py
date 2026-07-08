import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs_count_pairs(adj, default_dic, start):
    # stack = [(start, path, visited)]
    stack = [(start, [start], {start})]
    total_paths = 0

    while stack:
        node, path, visited = stack.pop()

        has_next = False
        for neighbor in adj[node]:
            if neighbor not in visited and default_dic[neighbor].issubset(visited):
                has_next = True
                stack.append((neighbor, path + [neighbor], visited | {neighbor}))

        if not has_next:
            total_paths += 1
            for i in range(len(path) - 1):
                pair_count[(path[i], path[i+1])] += 1

    return total_paths


n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
default_dic = {i: set() for i in range(n + 1)}

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    default_dic[v].add(u)

pair_count = defaultdict(int)

sources = [i for i in range(1, n + 1) if len(default_dic[i]) == 0 and len(adj[i]) > 0]

total_paths = 0
for start in sources:
    total_paths += dfs_count_pairs(adj, default_dic, start)
universal_pairs = [(u, v) for (u, v), cnt in pair_count.items() if cnt == total_paths]

universal_pairs.sort()

print(len(universal_pairs))
if universal_pairs:
    for u, v in universal_pairs:
        print(u, v)
else:
    exit()




