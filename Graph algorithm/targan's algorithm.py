import sys

input = sys.stdin.readline

def targan_algorithm(start):
    global id, neighborhood_count
    ids[start] = low[start] = id
    id += 1
    onstack[start] = True
    stack.append(start)

    for node in adj[start]:
        if ids[node] == 0:
            targan_algorithm(node)
            low[start] = min(low[start], low[node])
        elif onstack[node]:
            low[start] = min(low[start], ids[node])


    if ids[start] == low[start]:
        current_neighborhood = []
        while True:
            rem = stack.pop()
            onstack[rem] = False
            current_neighborhood.append(rem)
            if rem == start:
                break
        neighborhoods.append(current_neighborhood)
        neighborhood_count += 1



n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)


ids = [0 for _ in range(n+1)]
low = [0 for _ in range(n+1)]
onstack = [False for _ in range(n+1)]
stack = []
id = 1
neighborhood_count = 0
neighborhoods = []

for i in range(1, n + 1):
    if ids[i] == 0:
        targan_algorithm(i)

print("Total Neighborhoods:", neighborhood_count)
print("Groupings:", neighborhoods)