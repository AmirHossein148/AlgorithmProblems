import sys
from collections import deque
import math

input = sys.stdin.readline

def check(data, d, m):
    total = 0
    for profit, cost, ratio in data:
        if ratio < d:
            val = profit * d - cost
            if val > 0:
                total += val
    return total >= m

def min_day(data, m):
    lo, hi = 1, 2 * 10**9

    while lo < hi:
        mid = (lo + hi) // 2
        if check(data, mid, m):
            hi = mid
        else:
            lo = mid + 1

    return lo

n, m = map(int, input().split())
data = []
for _ in range(n):
    profit, cost = map(int, input().split())
    data.append((profit, cost, cost / profit))

print(min_day(data, m))