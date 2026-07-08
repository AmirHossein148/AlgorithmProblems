def LCS(p, s):
    n, m = len(p), len(s)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = n, m
    subsequence = []
    while i > 0 and j > 0:
        if p[i - 1] == s[j - 1]:
            subsequence.append(p[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    subsequence.reverse()
    return dp[n][m], "".join(subsequence)


p = input()
s = input()

result = LCS(p, s)
print(result[0])
print(result[1])






