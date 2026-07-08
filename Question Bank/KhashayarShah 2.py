import sys

input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n)]

for i in range(n):
    line = input().strip()
    adj[i] = [j for j in range(n) if line[j] == '1']

uncovered = set(range(n))
chosen = []

while uncovered:
    scores = [(i, len(uncovered & set(adj[i]))) for i in range(n)]
    best = max(scores, key=lambda x: x[1])[0]
    chosen.append(best)
    uncovered -= set(adj[best]) | {best}

print(len(chosen))
print(*chosen)

