def LIS(arr, n):
    dp = [1] * n
    parent = [-1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    max_len = max(dp)
    idx = dp.index(max_len)

    lis = []
    while idx != -1:
        lis.append(arr[idx])
        idx = parent[idx]

    lis.reverse()
    return max_len, lis


n = int(input())
arr = list(map(int, input().split()))

result = LIS(arr, n)
print(result[0])
print(*result[1])


