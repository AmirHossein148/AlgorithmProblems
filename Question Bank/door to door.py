import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [0] + list(map(int, input().split())) # 1-based array

B = int(n ** 0.5) + 1

dp = [[0] * (n + 1) for _ in range(B)]

for k in range(1, B):
    for i in range(1, n + 1):
        dp[k][i] = a[i]
        if i - k >= 1:
            dp[k][i] += dp[k][i - k]

for _ in range(m):
    l, r, k = map(int, input().split())
    if k < B:
        res = dp[k][r]
        if l - k >= 1:
            res -= dp[k][l - k]
        print(res)
    else:
        s = 0
        i = l
        while i <= r:
            s += a[i]
            i += k
        print(s)
