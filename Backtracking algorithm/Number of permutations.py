# Counting permutations with k inversions
def count_permutations_with_k_inversions(n, k):
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(k+1):
            for x in range(min(j, i-1)+1):
                dp[i][j] += dp[i-1][j-x]

    return dp[n][k]

n, k = map(int, input().split())
print(count_permutations_with_k_inversions(n, k))
