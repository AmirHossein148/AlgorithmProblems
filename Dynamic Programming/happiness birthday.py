def solve():
    N, M = map(int, input().split())
    prices = list(map(int, input().split()))

    NEG_INF = -1
    dp = [NEG_INF] * (N + 1)
    dp[0] = 0  # base case: 0 happiness, 0 sum

    for h in range(N + 1):
        if dp[h] == NEG_INF:
            continue
        S = dp[h]  # current max sum at happiness h
        for v in prices:
            new_h = h + S + v
            new_s = S + v
            if new_h <= N:
                dp[new_h] = max(dp[new_h], new_s)

    print(dp[N])  

t = int(input())
for _ in range(t):
    solve()