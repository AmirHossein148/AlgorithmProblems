MAX_N = 2000
MOD = 10 ** 9 + 7

array = [[0] * (MAX_N + 1) for _ in range(MAX_N + 1)]

for i in range(MAX_N + 1):
    array[i][0] = 1
    for j in range(1, i + 1):
        array[i][j] = (array[i - 1][j] + array[i - 1][j - 1]) % MOD

q = int(input())
for _ in range(q):
    n, r = map(int, input().split())
    print(array[n][r])


