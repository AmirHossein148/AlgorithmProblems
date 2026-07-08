import sys
from collections import deque

input = sys.stdin.readline

m, n, maxBoxes, maxWeight = map(int, input().split())

ports = [0] * (n + 1)
weight = [0] * (n + 1)

for i in range(1, n + 1):
    p, w = map(int, input().split())
    ports[i] = p
    weight[i] = w

prefixWeight = [0] * (n + 1)
for i in range(1, n + 1):
    prefixWeight[i] = prefixWeight[i - 1] + weight[i]

portChange = [0] * (n + 1)
for i in range(2, n + 1):
    portChange[i] = portChange[i - 1] + (1 if ports[i] != ports[i - 1] else 0)

dp = [0] * (n + 1)
dq = deque()
dq.append(0)

for i in range(1, n + 1):
    while dq and (i - dq[0] > maxBoxes or prefixWeight[i] - prefixWeight[dq[0]] > maxWeight):
        dq.popleft()

    j = dq[0]
    dp[i] = portChange[i] + 2 + (dp[j] - portChange[j + 1])

    if i != n:
        val = dp[i] - portChange[i + 1]
        while dq and dp[dq[-1]] - portChange[dq[-1] + 1] >= val:
            dq.pop()
        dq.append(i)

print(dp[n])



