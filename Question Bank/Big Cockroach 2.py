import heapq
import sys

def solve(n, a, b, children, parents_of):
    dp = a[:]

    current_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        current_sum[i] = sum(dp[c] for c in children[i])

    pq = [(dp[i], i) for i in range(1, n + 1)]
    heapq.heapify(pq)

    while pq:
        d, u = heapq.heappop(pq)
        if d != dp[u]:
            continue

        for p in parents_of[u]:
            new_val = b[p] + current_sum[p]

            if new_val < dp[p]:
                old = dp[p]
                dp[p] = new_val
                heapq.heappush(pq, (new_val, p))

                delta = new_val - old

                for gp in parents_of[p]:
                    current_sum[gp] += delta

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

print(solve(n, a, b, children, parents_of))
