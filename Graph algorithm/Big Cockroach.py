import heapq
import sys

def solve(a, b, children, parents_of):
    dp = [a[i] for i in range(n + 1)]
    pq = [(dp[i], i) for i in range(1, n + 1)]
    heapq.heapify(pq)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dp[u]:
            continue
        for p in parents_of[u]:
            new_total = b[p] + sum(dp[c] for c in children[p])
            if new_total < dp[p]:
                dp[p] = new_total
                heapq.heappush(pq, (dp[p], p))

    return dp[1]

input = sys.stdin.readline

n = int(input())
a = [0] * (n + 1)
b = [0] * (n + 1)
children = [[] for _ in range(n + 1)]
parents_of = [[] for _ in range(n + 1)]

for i in range(1, n+1):
    data = input().split()
    spread_cost = int(data[0])
    finish_cost = int(data[1])
    type_num = int(data[2])

    a[i] = finish_cost
    b[i] = spread_cost

    for j in map(int, data[3:]):
        children[i].append(j)
        parents_of[j].append(i)


print(solve(a, b, children, parents_of))













