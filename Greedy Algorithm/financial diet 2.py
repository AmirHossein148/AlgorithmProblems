import sys

def solve(k, j, p_k, p_j, p_mix):
    max_a = max(k, j)
    min_cost = float('inf')

    for a in range(max_a + 1):
        b = max(0, (k - a + 1) // 2)  # number of K pairs needed after a mixed packs
        c = max(0, (j - a + 1) // 2)  # number of J pairs needed after a mixed packs

        cost = a * p_mix + b * p_k + c * p_j
        min_cost = min(min_cost, cost)

    return min_cost

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k, j = map(int, input().split())
    p_k, p_j, p_mix = map(int, input().split())
    print(solve(k, j, p_k, p_j, p_mix))