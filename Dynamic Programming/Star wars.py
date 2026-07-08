import time
start_time = time.time()

def max_black_knockout(array, n, m):
    dp = [[-1] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if array[i][j] == 'W':
                dp[i][j] = 0

    for i in range(n - 1, 0, -1):
        for j in range(m):
            if dp[i][j] == -1:
                continue
            for dj in (-1, 0, 1):
                nj = j + dj
                if 0 <= nj < m and array[i - 1][nj] != 'W':
                    gain = 1 if array[i - 1][nj] == 'B' else 0
                    dp[i - 1][nj] = max(dp[i - 1][nj], dp[i][j] + gain)

    result = 0
    for i in range(n):
        for j in range(m):
            result = max(result, dp[i][j])
    return result

n, m = map(int, input().split())
array = [list(input()) for _ in range(n)]

print(max_black_knockout(array, n, m))

end_time = time.time()
print('Execution time: {:.6f} seconds'.format(end_time-start_time))